#!/usr/bin/env python

import pytest

from secret_santa import GiftExchange


@pytest.fixture()
def gift_exchange():
    gift_exchange = GiftExchange()
    return gift_exchange


def test_ExceptionWithDuplicateFamilyMember(gift_exchange):
    with pytest.raises(Exception):
        gift_exchange.add_family_member("Fred")
        gift_exchange.add_family_member("Fred")


def test_ExceptionWithPartnerAsDuplicatedFamilyMember(gift_exchange):
    with pytest.raises(Exception):
        gift_exchange.add_partners("Fred", "Fred")


def test_ExceptionWithDuplicateMember(gift_exchange):
    with pytest.raises(Exception):
        gift_exchange.add_partners("Fred", "Wilma")
        gift_exchange.add_partners("Fred", "Betty")


def test_ExceptionWithDuplicatePartner(gift_exchange):
    with pytest.raises(Exception):
        gift_exchange.add_partners("Fred", "Wilma")
        gift_exchange.add_partners("Barney", "Wilma")


def test_canAddFamilyMembers(gift_exchange):
    gift_exchange.add_family_member("Fred")
    gift_exchange.add_partners("Fred", "Wilma")
    gift_exchange.add_family_member("Barney")
    gift_exchange.add_partners("Barney", "Betty")
    gift_exchange.add_family_member("Pebbles")
    gift_exchange.add_family_member("Bambam")
    assert gift_exchange.get_family_member_count() == 6
    assert gift_exchange.get_partner_count() == 4


def test_getUnmatchedMembersCount(gift_exchange):
    gift_exchange.add_family_member("Fred")
    gift_exchange.add_partners("Fred", "Wilma")
    assert gift_exchange.get_unmatched_members_count() == 2


def test_checkForValidGiver(gift_exchange):
    gift_exchange.add_family_member("Fred")
    gift_exchange.add_partners("Fred", "Wilma")
    assert gift_exchange.check_for_valid_giver(["Fred", "Wilma"], 0, 1) == False


def test_ExceptionWithOnlyPartners(gift_exchange):
    gift_exchange.add_family_member("Fred")
    gift_exchange.add_partners("Fred", "Wilma")
    with pytest.raises(Exception):
        gift_exchange.match_members()


def test_ExceptionWithOnlyFamily(gift_exchange):
    gift_exchange.add_family_member("Fred")
    gift_exchange.add_partners("Fred", "Wilma")
    gift_exchange.add_family_member("Pebbles")
    with pytest.raises(Exception):
        gift_exchange.match_members()


def test_canSolveGoodSolution1(gift_exchange):
    gift_exchange.add_family_member("Ren")
    gift_exchange.add_family_member("Stimpy")
    gift_exchange.match_members()
    assert gift_exchange.get_unmatched_members_count() == 0


def test_canSolveGoodSolution2(gift_exchange):
    gift_exchange.add_family_member("Larry")
    gift_exchange.add_family_member("Curly")
    gift_exchange.add_family_member("Moe")
    gift_exchange.match_members()
    assert gift_exchange.get_unmatched_members_count() == 0


def test_canSolveGoodSolution3(gift_exchange):
    gift_exchange.add_family_member("Fred")
    gift_exchange.add_partners("Fred", "Wilma")
    gift_exchange.add_family_member("Barney")
    gift_exchange.add_partners("Barney", "Betty")
    gift_exchange.add_family_member("Pebbles")
    gift_exchange.add_family_member("Bambam")
    gift_exchange.match_members()
    assert gift_exchange.get_unmatched_members_count() == 0
