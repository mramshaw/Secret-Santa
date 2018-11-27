# Secret Santa

A simple Secret Santa gift exchange

## Motivation

Family members register for a gift exchange. Partners of family members cannot
receive gifts from that family member (and vice-versa). Everyone else will
receive a gift from a random family member.

[TDD](http://en.wikipedia.org/wiki/Test-driven_development) was used for this exercise
 with the [pytest framework](http://docs.pytest.org/en/latest/).

[This was a fun exercise that I knocked out in a half-day or so.]

## Prerequisites

Install prerequisites as follows:

    $ pip install --user -r requirements.txt

## Tests

Run unit tests as follows:

    $ pytest -v

This should look as follows:

```bash
$ pytest -v
==================================================================================================================== test session starts =====================================================================================================================
platform linux2 -- Python 2.7.12, pytest-3.10.1, py-1.7.0, pluggy-0.8.0 -- /usr/bin/python
cachedir: .pytest_cache
rootdir: /home/owner/Documents/Python/Secret-Santa, inifile:
collected 11 items

secret_santa_test.py::test_ExceptionWithDuplicateFamilyMember PASSED                                                                                                                                                                                   [  9%]
secret_santa_test.py::test_ExceptionWithPartnerAsDuplicatedFamilyMember PASSED                                                                                                                                                                         [ 18%]
secret_santa_test.py::test_ExceptionWithDuplicatePartner PASSED                                                                                                                                                                                        [ 27%]
secret_santa_test.py::test_canAddFamilyMembers PASSED                                                                                                                                                                                                  [ 36%]
secret_santa_test.py::test_getUnmatchedMembersCount PASSED                                                                                                                                                                                             [ 45%]
secret_santa_test.py::test_checkForValidGiver PASSED                                                                                                                                                                                                   [ 54%]
secret_santa_test.py::test_ExceptionWithOnlyPartners PASSED                                                                                                                                                                                            [ 63%]
secret_santa_test.py::test_ExceptionWithOnlyFamily PASSED                                                                                                                                                                                              [ 72%]
secret_santa_test.py::test_canSolveGoodSolution1 PASSED                                                                                                                                                                                                [ 81%]
secret_santa_test.py::test_canSolveGoodSolution2 PASSED                                                                                                                                                                                                [ 90%]
secret_santa_test.py::test_canSolveGoodSolution3 PASSED                                                                                                                                                                                                [100%]

================================================================================================================= 11 passed in 0.09 seconds ==================================================================================================================
$
```

## Run

Run the application as follows:

    $ python secret_santa.py

This should look something like the following:

```bash
$ python secret_santa.py
Enter family members and their partners

Family member (or CR to stop): Fred
Family member's partner (CR if none): Wilma

Family member (or CR to stop): Barney
Family member's partner (CR if none): Betty

Family member (or CR to stop): Pebbles
Family member's partner (CR if none): 

Family member (or CR to stop): Bambam
Family member's partner (CR if none): 

Family member (or CR to stop): 

All family members entered, working out exchanges

Solved = {'Pebbles': 'Bambam', 'Barney': 'Wilma', 'Fred': 'Pebbles', 'Betty': 'Fred', 'Bambam': 'Betty', 'Wilma': 'Barney'} 

Pebbles <= Bambam
Barney <= Wilma
Fred <= Pebbles
Betty <= Fred
Bambam <= Betty
Wilma <= Barney
$
```

## Versions

* python __2.7.12__
* pytest __3.10.1__

## To Do

- [ ] Conform code to `pylint`
- [ ] Conform code to `pycodestyle`
- [ ] Conform code to `pydocstyle`
- [ ] Optional enhancement - prevent circular gift exchanges
