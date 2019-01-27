#!/usr/bin/env python

# pylint: disable=C0103,W0621

"""Tests for a simple gift exchange."""

import pytest

from secret_santa import GiftExchange


@pytest.fixture()
def gift_exchange():
    """Initialize a GiftExchange object as a convenience."""
    gift_exchange = GiftExchange()
    return gift_exchange


def test_ExceptionWithDuplicateAttendeeName(gift_exchange):
    """Test for a duplicated attendee name."""
    with pytest.raises(GiftExchange.DuplicateAttendeeException) as exc_info:
        gift_exchange.add_attendee("Fred")
        gift_exchange.add_attendee("Fred")
    assert exc_info.value.args[0] == "Fred"


def test_ExceptionWithPartnerAsDuplicatedAttendee(gift_exchange):
    """Test for a duplicated partner."""
    with pytest.raises(GiftExchange.DuplicatePartnerException) as exc_info:
        gift_exchange.add_partnership("Fred", "Fred")
    assert exc_info.value.args[0] == "partner"


def test_ExceptionWithDuplicatedAttendee(gift_exchange):
    """Test for an attendee with more than one partner."""
    with pytest.raises(GiftExchange.DuplicatePartnerException) as exc_info:
        gift_exchange.add_partnership("Fred", "Wilma")
        gift_exchange.add_partnership("Fred", "Betty")
    assert exc_info.value.args[0] == "attendee"
    assert exc_info.value.args[1] == "Fred"


def test_ExceptionWithDuplicatedPartner(gift_exchange):
    """Test for a duplicated partner."""
    with pytest.raises(GiftExchange.DuplicateAttendeeException) as exc_info:
        gift_exchange.add_partnership("Fred", "Wilma")
        gift_exchange.add_partnership("Barney", "Wilma")
    assert exc_info.value.args[0] == "Wilma"


def test_canAddAttendees(gift_exchange):
    """Test that it is possible to add attendees."""
    gift_exchange.add_attendee("Fred")
    gift_exchange.add_partnership("Fred", "Wilma")
    gift_exchange.add_attendee("Barney")
    gift_exchange.add_partnership("Barney", "Betty")
    gift_exchange.add_attendee("Pebbles")
    gift_exchange.add_attendee("Bambam")
    assert gift_exchange.get_attendee_count() == 6
    assert gift_exchange.get_partnership_count() == 2


def test_getUnmatchedAttendeesCount(gift_exchange):
    """Test for the correct attendee count."""
    gift_exchange.add_attendee("Fred")
    gift_exchange.add_partnership("Fred", "Wilma")
    assert gift_exchange.get_unmatched_attendees_count() == 2


def test_checkForValidGiver(gift_exchange):
    """Check than an attendee is rejected as a donor for their partner."""
    gift_exchange.add_attendee("Fred")
    gift_exchange.add_partnership("Fred", "Wilma")
    assert not gift_exchange.check_for_valid_giver(["Fred", "Wilma"], 0, 1)


def test_NoValidSolution1(gift_exchange):
    """Test that an unsolvable gathering raises an exception."""
    gift_exchange.add_attendee("Fred")
    with pytest.raises(GiftExchange.NoSolutionPossibleException) as exc_info:
        gift_exchange.check_for_valid_solution()
    assert exc_info.value.args[0] == "Not enough attendees for a solution!"


def test_NoValidSolution2(gift_exchange):
    """Test that an unsolvable gathering raises an exception."""
    gift_exchange.add_attendee("Fred")
    gift_exchange.add_partnership("Fred", "Wilma")
    with pytest.raises(GiftExchange.NoSolutionPossibleException) as exc_info:
        gift_exchange.check_for_valid_solution()
    assert (exc_info.value.args[0] ==
            "Not enough unpartnered attendees for a solution!")


def test_NoValidSolution3(gift_exchange):
    """Test that an unsolvable gathering raises an exception."""
    gift_exchange.add_attendee("Fred")
    gift_exchange.add_partnership("Fred", "Wilma")
    gift_exchange.add_attendee("Pebbles")
    with pytest.raises(GiftExchange.NoSolutionPossibleException) as exc_info:
        gift_exchange.check_for_valid_solution()
    assert (exc_info.value.args[0] ==
            "Not enough unpartnered attendees for a solution!")


def test_canShuffleAttendees(gift_exchange):
    """Test to see that the attendees can be shuffled."""
    gift_exchange.add_attendee("Fred")
    gift_exchange.add_partnership("Fred", "Wilma")
    gift_exchange.add_attendee("Barney")
    gift_exchange.add_partnership("Barney", "Betty")
    gift_exchange.add_attendee("Pebbles")
    gift_exchange.add_attendee("Bambam")
    items = gift_exchange.shuffle_attendees()
    assert len(items) == 6


def test_resetUnmatchedAttendeesCount(gift_exchange):
    """Test to see that the unmatched attendee count is reset correctly."""
    gift_exchange.add_attendee("Ren")
    gift_exchange.add_attendee("Stimpy")
    gift_exchange.match_attendees(gift_exchange.shuffle_attendees())
    assert gift_exchange.get_unmatched_attendees_count() == 0
    gift_exchange.reset_unmatched_attendees_count()
    assert gift_exchange.get_unmatched_attendees_count() == 2


def test_canSolveGoodSolution1(gift_exchange):
    """Test to see that a circular exchange can be solved."""
    gift_exchange.add_attendee("Ren")
    gift_exchange.add_attendee("Stimpy")
    gift_exchange.match_attendees(gift_exchange.shuffle_attendees())
    assert gift_exchange.get_unmatched_attendees_count() == 0


def test_canSolveGoodSolution2(gift_exchange):
    """Test to see that a completely solvable exchange can be solved."""
    gift_exchange.add_attendee("Larry")
    gift_exchange.add_attendee("Curly")
    gift_exchange.add_attendee("Moe")
    gift_exchange.match_attendees(gift_exchange.shuffle_attendees())
    assert gift_exchange.get_unmatched_attendees_count() == 0


# Certain orders of the Flintstones are solvable,
#   but others are not. We will check both.


def test_canSolveFlintstones1(gift_exchange):
    """Test that a solvable arrangement gets solved."""
    gift_exchange.add_attendee("Fred")
    gift_exchange.add_partnership("Fred", "Wilma")
    gift_exchange.add_attendee("Barney")
    gift_exchange.add_partnership("Barney", "Betty")
    gift_exchange.add_attendee("Pebbles")
    gift_exchange.add_attendee("Bambam")
    solvable_arr = ['Barney', 'Wilma', 'Bambam', 'Betty', 'Fred', 'Pebbles']
    gift_exchange.match_attendees(solvable_arr)
    assert gift_exchange.get_unmatched_attendees_count() == 0


def test_canSolveFlintstones2(gift_exchange):
    """Test that a solvable arrangement gets solved."""
    gift_exchange.add_attendee("Fred")
    gift_exchange.add_partnership("Fred", "Wilma")
    gift_exchange.add_attendee("Barney")
    gift_exchange.add_partnership("Barney", "Betty")
    gift_exchange.add_attendee("Pebbles")
    gift_exchange.add_attendee("Bambam")
    solvable_arr = ['Wilma', 'Bambam', 'Betty', 'Fred', 'Pebbles', 'Barney']
    gift_exchange.match_attendees(solvable_arr)
    assert gift_exchange.get_unmatched_attendees_count() == 0


def test_cannotSolveFlintstones1(gift_exchange):
    """Test that an unsolvable arrangement raises an exception."""
    gift_exchange.add_attendee("Fred")
    gift_exchange.add_partnership("Fred", "Wilma")
    gift_exchange.add_attendee("Barney")
    gift_exchange.add_partnership("Barney", "Betty")
    gift_exchange.add_attendee("Pebbles")
    gift_exchange.add_attendee("Bambam")
    unsolvable_arr = ['Barney', 'Pebbles', 'Bambam', 'Betty', 'Fred', 'Wilma']
    with pytest.raises(gift_exchange.SolutionNotFoundException):
        gift_exchange.match_attendees(unsolvable_arr)


def test_cannotSolveFlintstones2(gift_exchange):
    """Test that an unsolvable arrangement raises an exception."""
    gift_exchange.add_attendee("Fred")
    gift_exchange.add_partnership("Fred", "Wilma")
    gift_exchange.add_attendee("Barney")
    gift_exchange.add_partnership("Barney", "Betty")
    gift_exchange.add_attendee("Pebbles")
    gift_exchange.add_attendee("Bambam")
    unsolvable_arr = ['Wilma', 'Barney', 'Bambam', 'Betty', 'Pebbles', 'Fred']
    with pytest.raises(gift_exchange.SolutionNotFoundException):
        gift_exchange.match_attendees(unsolvable_arr)


# Now run some benchmarks for historical comparison purposes.


def test_canSolveBenchmark1(benchmark):
    """Benchmark a solvable arrangement getting solved."""
    ge = GiftExchange()
    ge.add_attendee("Fred")
    ge.add_partnership("Fred", "Wilma")
    ge.add_attendee("Barney")
    ge.add_partnership("Barney", "Betty")
    ge.add_attendee("Pebbles")
    ge.add_attendee("Bambam")
    solvable_arr = ['Barney', 'Wilma', 'Bambam', 'Betty', 'Fred', 'Pebbles']
    result = benchmark(ge.match_attendees, solvable_arr)
    assert ge.get_unmatched_attendees_count() == 0


def test_canSolveBenchmark2(benchmark):
    """Benchmark a solvable arrangement getting solved."""
    ge = GiftExchange()
    ge.add_attendee("Fred")
    ge.add_partnership("Fred", "Wilma")
    ge.add_attendee("Barney")
    ge.add_partnership("Barney", "Betty")
    ge.add_attendee("Pebbles")
    ge.add_attendee("Bambam")
    solvable_arr = ['Wilma', 'Bambam', 'Betty', 'Fred', 'Pebbles', 'Barney']
    result = benchmark(ge.match_attendees, solvable_arr)
    assert ge.get_unmatched_attendees_count() == 0
