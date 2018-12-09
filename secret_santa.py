#!/usr/bin/env python

"""
A simple gift exchange.

Gathering attendees register for a gift exchange. The partner of an
attendee cannot receive a gift from that attendee (and vice-versa).
Everyone else will receive a gift from a random attendee.
"""

from random import shuffle

import sys


class GiftExchange:
    """GiftExchange represents a gift exchange."""

    class DuplicateAttendeeException(Exception):
        """Gathering attendee names must be unique."""

        pass

    class DuplicatePartnerException(Exception):
        """Partner names must be unique & can only be in 1 partnership."""

        pass

    class NoSolutionPossibleException(Exception):
        """There are not enough attendees for a solution."""

        pass

    class SolutionNotFoundException(Exception):
        """The solution was not found on this walk, can retry."""

        pass

    def __init__(self):
        """Initialize the gift exchangers and their partners."""
        self._GIFT_EXCHANGERS = {}
        self._PARTNERS = {}

    def add_attendee(self, attendee):
        """Add a gift exchanger."""
        if attendee in self._GIFT_EXCHANGERS:
            raise self.DuplicateAttendeeException(attendee)
        self._GIFT_EXCHANGERS[attendee] = 1

    def add_partnership(self, attendee, partner):
        """
        Add a gift exchangers' partnership.

        First add the gift echangers' partner,
        and then both ends of the partnership.
        """
        self.add_attendee(partner)
        if attendee in self._PARTNERS:
            raise self.DuplicatePartnerException("attendee", attendee)
        self._PARTNERS[attendee] = partner
        if partner in self._PARTNERS:
            raise self.DuplicatePartnerException("partner", partner)
        self._PARTNERS[partner] = attendee

    def get_attendee_count(self):
        """Get the count of gift exchangers."""
        return len(self._GIFT_EXCHANGERS)

    def get_partnership_count(self):
        """Get the count of partnerships."""
        return len(self._PARTNERS) / 2

    def get_unmatched_attendees_count(self):
        """Get the count of unmatched gathering attendees."""
        count = 0
        for mbr in self._GIFT_EXCHANGERS:
            if self._GIFT_EXCHANGERS[mbr] == 1:
                count += 1
        return count

    def get_next_free_present_giver(self, items, i):
        """Get the next free present giver."""
        indx = i + 1
        while indx < len(items):
            if self.check_for_valid_giver(items, i, indx):
                self._GIFT_EXCHANGERS[items[indx]] = 0
                return items[indx]
            indx += 1
        indx = 0
        while indx < i:
            if self.check_for_valid_giver(items, i, indx):
                self._GIFT_EXCHANGERS[items[indx]] = 0
                return items[indx]
            indx += 1
        raise self.SolutionNotFoundException()

    def reset_unmatched_attendees_count(self):
        """Reset the present counts for all of the gift exchangers."""
        for exchgr in self._GIFT_EXCHANGERS:
            self._GIFT_EXCHANGERS[exchgr] = 1

    def check_for_valid_giver(self, items, i, indx):
        """Check if there is a valid donor."""
        if items[i] in self._PARTNERS:
            if items[indx] == self._PARTNERS[items[i]]:
                return False
        if self._GIFT_EXCHANGERS[items[indx]] == 0:
            return False
        return True

    def check_for_valid_solution(self):
        """Check if a valid solution is possible."""
        attendee_count = self.get_attendee_count()
        partnership_count = self.get_partnership_count()
        if attendee_count < 2:
            raise self.NoSolutionPossibleException(
                    "Not enough attendees for a solution!")
        if attendee_count == 2 and partnership_count == 1:
            raise self.NoSolutionPossibleException(
                    "Not enough unpartnered attendees for a solution!")
        if attendee_count == 3 and partnership_count == 1:
            raise self.NoSolutionPossibleException(
                    "Not enough unpartnered attendees for a solution!")

    def shuffle_attendees(self):
        """
        Shuffle the gift exchangers.

        (This is only pseudo-random but that's good enough).
        """
        items = self._GIFT_EXCHANGERS.keys()
        shuffle(items)
        return items

    def match_attendees(self, items):
        """Solve the gift exchange."""
        self.check_for_valid_solution()
        self.reset_unmatched_attendees_count()
        solved = {}
        for i in range(len(items)):
            solved[items[i]] = self.get_next_free_present_giver(items, i)
        if self.get_unmatched_attendees_count() > 0:
            raise self.SolutionNotFoundException()
        print "Solved =", solved, "\n"
        return solved


if __name__ == '__main__':

    ge = GiftExchange()

    print "Enter gathering attendees and their partners"

    while True:
        NAME = raw_input("\nAttendee (or CR to stop): ")
        if NAME == "":
            break
        ge.add_attendee(NAME)
        PARTNER = raw_input("Attendee's partner (CR if none): ")
        if PARTNER != "":
            ge.add_partnership(NAME, PARTNER)

    print "\nAll gathering attendees entered, working out exchanges\n"

    retry = True
    while retry:
        try:
            solution = ge.match_attendees(ge.shuffle_attendees())
            for s in solution:
                print s, "<=", solution[s]
            retry = False
        except ge.SolutionNotFoundException:
            if raw_input("Failed to solve, retry ('n' to stop)? ").strip() \
                 == "n":
                print "Okay, stopping now"
                sys.exit(1)
        except ge.NoSolutionPossibleException as nspe:
            print nspe.args[0]
            sys.exit(1)

    print "\nI hope your gathering is successful!"
