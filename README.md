# Secret Santa

[![Known Vulnerabilities](http://snyk.io/test/github/mramshaw/Secret-Santa/badge.svg?style=plastic&targetFile=requirements.txt)](http://snyk.io/test/github/mramshaw/Secret-Santa?style=plastic&targetFile=requirements.txt)
[![Build status](http://travis-ci.org/mramshaw/Secret-Santa.svg?branch=master)](http://travis-ci.org/mramshaw/Secret-Santa)
[![Coverage Status](http://codecov.io/github/mramshaw/Secret-Santa/coverage.svg?branch=master)](http://codecov.io/github/mramshaw/Secret-Santa?branch=master)
[![GitHub release](http://img.shields.io/github/release/mramshaw/Secret-Santa.svg?style=flat-square)](http://github.com/mramshaw/Secret-Santa/releases)

A simple Secret Santa gift exchange

## Motivation

At seasonal parties and other gatherings, attendees may register for a gift exchange.
Partners of attendees cannot receive gifts from that attendee (and vice-versa).
Everyone else will receive a gift from a random attendee.

Each attendee (and partner) must have a unique name. Duplicate names will create exceptions.

[TDD](http://en.wikipedia.org/wiki/Test-driven_development) was used for this exercise
 with the [pytest](http://docs.pytest.org/en/latest/) framework.

[This was a fun exercise - I knocked out my first effort in a half-day or so. But it turned
 out that I had not fully understood the problem. Like a lot of random walks, the solution
 is not always deterministic. This led to some re-work. Luckily, TDD makes this relatively
 easy, at least in terms of testing time.]

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

## Code Coverage

There seem to be two main options for Python code coverage reporting:

* [coverage](http://pypi.org/project/coverage/)
* [pytest-cov](http://pytest-cov.readthedocs.io/en/latest/readme.html)

As we are already using `pytest` we will use the second option.

[We will not need _parallel_ or _distributed_ testing, so no need to install `pytest-xdist` at this time.]

We can get code coverage statistics as follows:

```bash
$ pytest -v --cov=./
==================================================================================================================== test session starts =====================================================================================================================
platform linux2 -- Python 2.7.12, pytest-3.10.1, py-1.7.0, pluggy-0.8.0 -- /usr/bin/python
cachedir: .pytest_cache
rootdir: /home/owner/Documents/Python/Secret-Santa, inifile:
plugins: cov-2.6.0
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

---------- coverage: platform linux2, python 2.7.12-final-0 ----------
Name                   Stmts   Miss  Cover
------------------------------------------
secret_santa.py           74     16    78%
secret_santa_test.py      64      0   100%
------------------------------------------
TOTAL                    138     16    88%


================================================================================================================= 11 passed in 0.10 seconds ==================================================================================================================
$
```

Code coverage is __88%__ which seems acceptable.

[Opinions differ on what is an acceptable level of code coverage.
As 100% code coverage is not always reasonable (for instance in this
case), my opinion is that 70% is a minimum acceptable value. But a
higher level of code coverage is of course very desirable.]

Of course, we can drill down into the code with an HTML report as well:

```bash
$ pytest -v --cov=./ --cov-report=html
==================================================================================================================== test session starts =====================================================================================================================
platform linux2 -- Python 2.7.12, pytest-3.10.1, py-1.7.0, pluggy-0.8.0 -- /usr/bin/python
cachedir: .pytest_cache
rootdir: /home/owner/Documents/Python/Secret-Santa, inifile:
plugins: cov-2.6.0
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

---------- coverage: platform linux2, python 2.7.12-final-0 ----------
Coverage HTML written to dir htmlcov


================================================================================================================= 11 passed in 0.09 seconds ==================================================================================================================
$
```

Looking at `htmlcov/index.html` and drilling down into `secret_santa.py` we can see that
we do not have any coverage in our `main` routine (this is expected) but there are also
two exceptions that do not get tested. The second is a catch-all, so cannot be fixed.

However, the first exception not being tested is an oversight. This means another test
should be written to check for this exception. And so code coverage has highlighted a
soft area in our testing. This is unlikely to be critical, but better safe than sorry.

[Adding a test for the first uncaught exception raises the code coverage to __89%__.]

## Run

Run the application as follows:

    $ python secret_santa.py

This should look something like the following:

```bash
$ python secret_santa.py
Enter gathering attendees and their partners

Attendee (or CR to stop): Fred
Attendee's partner (CR if none): Wilma

Attendee (or CR to stop): Barney
Attendee's partner (CR if none): Betty

Attendee (or CR to stop): Pebbles
Attendee's partner (CR if none):

Attendee (or CR to stop): Bambam
Attendee's partner (CR if none):

Attendee (or CR to stop):

All gathering attendees entered, working out exchanges

Solved = {'Pebbles': 'Bambam', 'Barney': 'Wilma', 'Fred': 'Pebbles', 'Betty': 'Fred', 'Bambam': 'Betty', 'Wilma': 'Barney'} 

Pebbles <= Bambam
Barney <= Wilma
Fred <= Pebbles
Betty <= Fred
Bambam <= Betty
Wilma <= Barney
$
```

## Failure

For some combinations of gift exchangers, a solution may not be possible.

In that case an error message will be printed and the app will terminate:

```bash
$ python secret_santa.py
Enter gathering attendees and their partners

Attendee (or CR to stop): fred
Attendee's partner (CR if none): wilma

Attendee (or CR to stop):

All gathering attendees entered, working out exchanges

Not enough unpartnered members for a solution!
$
```

## Retries

For some combinations of gift exchangers, the algorithm may not produce a solution.

In that case, the user will be prompted to retry. This should look like:

```bash
$ python secret_santa.py
Enter gathering attendees and their partners

Attendee (or CR to stop): fred
Attendee's partner (CR if none): wilma

Attendee (or CR to stop): pebbles
Attendee's partner (CR if none):

Attendee (or CR to stop): dino
Attendee's partner (CR if none):

Attendee (or CR to stop):

All gathering attendees entered, working out exchanges

Failed to solve, retry ('n' to stop)?
Solved = {'pebbles': 'fred', 'dino': 'wilma', 'wilma': 'dino', 'fred': 'pebbles'}

pebbles <= fred
dino <= wilma
wilma <= dino
fred <= pebbles

I hope your gathering is successful!
$
```

Of course, the user can stop the retries by entering "__n__" at any time:

```bash
$ python secret_santa.py
Enter gathering attendees and their partners

Attendee (or CR to stop): fred
Attendee's partner (CR if none): wilma

Attendee (or CR to stop): pebbles
Attendee's partner (CR if none):

Attendee (or CR to stop): dino
Attendee's partner (CR if none):

Attendee (or CR to stop):

All gathering attendees entered, working out exchanges

Failed to solve, retry ('n' to stop)? n
Okay, stopping now
$
```

## Versions

* python __2.7.12__
* pytest __3.10.1__
* pytest-cov __2.6.0__

## To Do

- [x] Add custom exceptions
- [x] Add logic for unsolvable cases
- [x] Add retry logic for bad solutions
- [x] Add coverage reporting
- [x] Increase code coverage
- [x] Refactor to extend to seasonal (rather than simply family) gatherings
- [ ] Conform code to `pylint`
- [x] Conform code to `pycodestyle`
- [x] Conform code to `pydocstyle`
- [x] Conform code to `pydoc`
- [ ] Optional enhancement - prevent circular gift exchanges
- [ ] Optional enhancement - prevent intra-family gift exchanges
