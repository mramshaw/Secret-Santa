#!/usr/bin/env python

"""
A simple gift exchange.

Family members register for a gift exchange.
The partner of a family member cannot receive a gift from that family member
(and vice-versa). Everyone else will receive a gift from a random family member.
"""

from random import *


class GiftExchange:

    def __init__(self):
        self._GIFT_EXCHANGERS = {}
        self._PARTNERS = {}

    def add_family_member(self, member):
        if member in self._GIFT_EXCHANGERS:
            raise Exception("Duplicate family member entered")
        self._GIFT_EXCHANGERS[member] = 1

    def add_partners(self, member, partner):

        self.add_family_member(partner)
        if member in self._PARTNERS:
            raise Exception("Duplicate partner entered")
        self._PARTNERS[member] = partner
        if partner in self._PARTNERS:
            raise Exception("Duplicate partner entered")
        self._PARTNERS[partner] = member

    def get_family_member_count(self):
        return len(self._GIFT_EXCHANGERS)

    def get_partner_count(self):
        return len(self._PARTNERS)

    def get_unmatched_members_count(self):
        count = 0
        for mbr in self._GIFT_EXCHANGERS:
            if self._GIFT_EXCHANGERS[mbr] == 1:
                count += 1
        return count

    def get_next_free_present_giver(self, items, i):
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
        raise Exception("Did not find an unmatched giver")

    def check_for_valid_giver(self, items, i, indx):
        if items[i] in self._PARTNERS:
            if items[indx] == self._PARTNERS[items[i]]:
                # print "\nPARTNERS FOUND:", items[i], "<=", items[indx] 
                return False
        if self._GIFT_EXCHANGERS[items[indx]] == 0:
            return False
        return True

    def match_members(self):
        items = self._GIFT_EXCHANGERS.keys()
        shuffle(items)
        solved = {}
        for i in range(len(items)):
            solved[items[i]] = self.get_next_free_present_giver(items, i)
        if self.get_unmatched_members_count() > 0:
            raise Exception("Unmatched givers found, did not solve")
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

    # print gift_exchange._GIFT_EXCHANGERS
    # print gift_exchange._PARTNERS

    solution = gift_exchange.match_members()
    for s in solution:
        print s, "<=", solution[s]
