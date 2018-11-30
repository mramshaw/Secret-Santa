#!/usr/bin/env python

"""
A simple gift exchange.

Family members register for a gift exchange.
The partner of a family member cannot receive a gift from that family member
(and vice-versa). Everyone else will receive a gift from a random family member.
"""

from random import *

import sys


class GiftExchange:
    """GiftExchange represents a gift exchange."""

    class DuplicateFamilyMemberException(Exception):
        """Family member names must be unique."""

        pass

    class DuplicatePartnerException(Exception):
        """Partner names must be unique & can only be in 1 partnership."""

        pass

    class NoSolutionPossibleException(Exception):
        """There are not enough family members (of the correct types) for a solution."""

        pass

    class SolutionNotFoundException(Exception):
        """The solution was not found on this walk, can retry."""

        pass

    def __init__(self):
        """Initialize the gift exchangers and their partners."""
        self._GIFT_EXCHANGERS = {}
        self._PARTNERS = {}

    def add_family_member(self, member):
        """Add a gift exchangers."""
        if member in self._GIFT_EXCHANGERS:
            raise self.DuplicateFamilyMemberException(member)
        self._GIFT_EXCHANGERS[member] = 1

    def add_partners(self, member, partner):
        """Add a gift exchangers' partner, and then add both ends of the partnership."""
        self.add_family_member(partner)
        if member in self._PARTNERS:
            raise self.DuplicatePartnerException("member", member)
        self._PARTNERS[member] = partner
        if partner in self._PARTNERS:
            raise self.DuplicatePartnerException("partner", partner)
        self._PARTNERS[partner] = member

    def get_family_member_count(self):
        """Get the count of gift exchangers."""
        return len(self._GIFT_EXCHANGERS)

    def get_partnership_count(self):
        """Get the count of partnerships."""
        return len(self._PARTNERS) / 2

    def get_unmatched_members_count(self):
        """Get the count of unmatched members."""
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

    def reset_unmatched_members_count(self):
        """Reset the present counts for the gift exchangers."""
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
        """Check if a valid solutions is possible."""
        if self.get_family_member_count() < 2:
            raise self.NoSolutionPossibleException("Not enough family members for a solution!")
        if self.get_family_member_count() == 2 and self.get_partnership_count() == 1:
            raise self.NoSolutionPossibleException("Not enough unpartnered members for a solution!")
        if self.get_family_member_count() == 3 and self.get_partnership_count() == 1:
            raise self.NoSolutionPossibleException("Not enough unpartnered members for a solution!")

    def shuffle_members(self):
        """Shuffle the gift exchangers (only pseudo-random but that's good enough)."""
        items = self._GIFT_EXCHANGERS.keys()
        shuffle(items)
        return items

    def match_members(self, items):
        """Solve the gift exchanges."""
        self.check_for_valid_solution()
        solved = {}
        for i in range(len(items)):
            solved[items[i]] = self.get_next_free_present_giver(items, i)
        if self.get_unmatched_members_count() > 0:
            raise self.SolutionNotFoundException()
        print "Solved =", solved, "\n"
        return solved


if __name__ == '__main__':

    gift_exchange = GiftExchange()

    print "Enter family members and their partners"

    while True:
        NAME = raw_input("\nFamily member (or CR to stop): ")
        if NAME == "":
            break
        else:
            gift_exchange.add_family_member(NAME)
            PARTNER = raw_input("Family member's partner (CR if none): ")
            if PARTNER != "":
                gift_exchange.add_partners(NAME, PARTNER)

    print "\nAll family members entered, working out exchanges\n"

    retry = True
    while retry:
        try:
            gift_exchange.reset_unmatched_members_count()
            solution = gift_exchange.match_members(gift_exchange.shuffle_members())
            for s in solution:
                print s, "<=", solution[s]
            retry = False
        except gift_exchange.SolutionNotFoundException:
            if raw_input("Failed to solve, retry ('n' to stop)? ").strip() == "n":
                print "Okay, stopping now"
                sys.exit(1)
        except gift_exchange.NoSolutionPossibleException as nspe:
            print nspe.args[0]
            sys.exit(1)

    print "\nI hope your gathering is successful!"
