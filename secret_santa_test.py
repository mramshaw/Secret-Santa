#!/usr/bin/env python

import pytest

from secret_santa import GiftExchange


@pytest.fixture()
def gift_exchange():
    gift_exchange = GiftExchange()
    return gift_exchange


def test_ExceptionWithDuplicateFamilyMember(gift_exchange):
    with pytest.raises(GiftExchange.DuplicateFamilyMemberException) as exc_info:
        gift_exchange.add_family_member("Fred")
        gift_exchange.add_family_member("Fred")
    assert exc_info.value.args[0] == "Fred"


def test_ExceptionWithPartnerAsDuplicatedFamilyMember(gift_exchange):
    with pytest.raises(GiftExchange.DuplicatePartnerException) as exc_info:
        gift_exchange.add_partners("Fred", "Fred")
    assert exc_info.value.args[0] == "partner"


def test_ExceptionWithDuplicateMember(gift_exchange):
    with pytest.raises(GiftExchange.DuplicatePartnerException) as exc_info:
        gift_exchange.add_partners("Fred", "Wilma")
        gift_exchange.add_partners("Fred", "Betty")
    assert exc_info.value.args[0] == "member"
    assert exc_info.value.args[1] == "Fred"


def test_ExceptionWithDuplicatePartner(gift_exchange):
    with pytest.raises(GiftExchange.DuplicateFamilyMemberException) as exc_info:
        gift_exchange.add_partners("Fred", "Wilma")
        gift_exchange.add_partners("Barney", "Wilma")
    assert exc_info.value.args[0] == "Wilma"


def test_canAddFamilyMembers(gift_exchange):
    gift_exchange.add_family_member("Fred")
    gift_exchange.add_partners("Fred", "Wilma")
    gift_exchange.add_family_member("Barney")
    gift_exchange.add_partners("Barney", "Betty")
    gift_exchange.add_family_member("Pebbles")
    gift_exchange.add_family_member("Bambam")
    assert gift_exchange.get_family_member_count() == 6
    assert gift_exchange.get_partnership_count() == 2


def test_getUnmatchedMembersCount(gift_exchange):
    gift_exchange.add_family_member("Fred")
    gift_exchange.add_partners("Fred", "Wilma")
    assert gift_exchange.get_unmatched_members_count() == 2


def test_checkForValidGiver(gift_exchange):
    gift_exchange.add_family_member("Fred")
    gift_exchange.add_partners("Fred", "Wilma")
    assert gift_exchange.check_for_valid_giver(["Fred", "Wilma"], 0, 1) == False


def test_NoValidSolution1(gift_exchange):
    gift_exchange.add_family_member("Fred")
    with pytest.raises(GiftExchange.NoSolutionPossibleException) as exc_info:
        gift_exchange.check_for_valid_solution()
    assert exc_info.value.args[0] == "Not enough family members for a solution!"


def test_NoValidSolution2(gift_exchange):
    gift_exchange.add_family_member("Fred")
    gift_exchange.add_partners("Fred", "Wilma")
    with pytest.raises(GiftExchange.NoSolutionPossibleException) as exc_info:
        gift_exchange.check_for_valid_solution()
    assert exc_info.value.args[0] == "Not enough unpartnered members for a solution!"


def test_NoValidSolution3(gift_exchange):
    gift_exchange.add_family_member("Fred")
    gift_exchange.add_partners("Fred", "Wilma")
    gift_exchange.add_family_member("Pebbles")
    with pytest.raises(GiftExchange.NoSolutionPossibleException) as exc_info:
        gift_exchange.check_for_valid_solution()
    assert exc_info.value.args[0] == "Not enough unpartnered members for a solution!"


def test_canShuffleMembers(gift_exchange):
    gift_exchange.add_family_member("Fred")
    gift_exchange.add_partners("Fred", "Wilma")
    gift_exchange.add_family_member("Barney")
    gift_exchange.add_partners("Barney", "Betty")
    gift_exchange.add_family_member("Pebbles")
    gift_exchange.add_family_member("Bambam")
    items = gift_exchange.shuffle_members()
    assert len(items) == 6


def test_resetUnmatchedMembersCount(gift_exchange):
    gift_exchange.add_family_member("Ren")
    gift_exchange.add_family_member("Stimpy")
    gift_exchange.match_members(gift_exchange.shuffle_members())
    assert gift_exchange.get_unmatched_members_count() == 0
    gift_exchange.reset_unmatched_members_count()
    assert gift_exchange.get_unmatched_members_count() == 2


def test_canSolveGoodSolution1(gift_exchange):
    gift_exchange.add_family_member("Ren")
    gift_exchange.add_family_member("Stimpy")
    gift_exchange.match_members(gift_exchange.shuffle_members())
    assert gift_exchange.get_unmatched_members_count() == 0


def test_canSolveGoodSolution2(gift_exchange):
    gift_exchange.add_family_member("Larry")
    gift_exchange.add_family_member("Curly")
    gift_exchange.add_family_member("Moe")
    gift_exchange.match_members(gift_exchange.shuffle_members())
    assert gift_exchange.get_unmatched_members_count() == 0


# Certain orders of the Flintstones are solvable,
#   but others are not. We will check both.


def test_canSolveFlintstones1(gift_exchange):
    gift_exchange.add_family_member("Fred")
    gift_exchange.add_partners("Fred", "Wilma")
    gift_exchange.add_family_member("Barney")
    gift_exchange.add_partners("Barney", "Betty")
    gift_exchange.add_family_member("Pebbles")
    gift_exchange.add_family_member("Bambam")
    solvable_order = ['Barney', 'Wilma', 'Bambam', 'Betty', 'Fred', 'Pebbles']
    gift_exchange.match_members(solvable_order)
    assert gift_exchange.get_unmatched_members_count() == 0


def test_canSolveFlintstones2(gift_exchange):
    gift_exchange.add_family_member("Fred")
    gift_exchange.add_partners("Fred", "Wilma")
    gift_exchange.add_family_member("Barney")
    gift_exchange.add_partners("Barney", "Betty")
    gift_exchange.add_family_member("Pebbles")
    gift_exchange.add_family_member("Bambam")
    solvable_order = ['Wilma', 'Bambam', 'Betty', 'Fred', 'Pebbles', 'Barney']
    gift_exchange.match_members(solvable_order)
    assert gift_exchange.get_unmatched_members_count() == 0


def test_cannotSolveFlintstones1(gift_exchange):
    gift_exchange.add_family_member("Fred")
    gift_exchange.add_partners("Fred", "Wilma")
    gift_exchange.add_family_member("Barney")
    gift_exchange.add_partners("Barney", "Betty")
    gift_exchange.add_family_member("Pebbles")
    gift_exchange.add_family_member("Bambam")
    unsolvable_order = ['Barney', 'Pebbles', 'Bambam', 'Betty', 'Fred', 'Wilma']
    with pytest.raises(gift_exchange.SolutionNotFoundException):
        gift_exchange.match_members(unsolvable_order)


def test_cannotSolveFlintstones2(gift_exchange):
    gift_exchange.add_family_member("Fred")
    gift_exchange.add_partners("Fred", "Wilma")
    gift_exchange.add_family_member("Barney")
    gift_exchange.add_partners("Barney", "Betty")
    gift_exchange.add_family_member("Pebbles")
    gift_exchange.add_family_member("Bambam")
    unsolvable_order = ['Wilma', 'Barney', 'Bambam', 'Betty', 'Pebbles', 'Fred']
    with pytest.raises(gift_exchange.SolutionNotFoundException):
        gift_exchange.match_members(unsolvable_order)
