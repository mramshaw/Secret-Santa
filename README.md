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

Or (for Python 3):

    $ pip3 install --user -r requirements.txt

## Tests

Run unit tests as follows:

    $ pytest -v

Or (for Python 3):

    $ python3 -m pytest -v

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

## Benchmarks

Capturing historical benchmarks is probably yet another ___best practice___.

Whenever code changes result in a substantial difference in execution time, this needs
to be investigated. Of course, to do so we will need to capture historical benchmarks.

The [pytest-benchmark](http://pypi.org/project/pytest-benchmark/) module was designed
for just such a purpose.

Run them as follows:

```bash
$ pytest -v --benchmark-only --benchmark-autosave
==================================================================================================================== test session starts =====================================================================================================================
platform linux2 -- Python 2.7.12, pytest-3.10.1, py-1.7.0, pluggy-0.8.0 -- /usr/bin/python
cachedir: .pytest_cache
benchmark: 3.2.2 (defaults: timer=time.time disable_gc=False min_rounds=5 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=100000)
rootdir: /home/owner/Documents/Python/Secret-Santa, inifile:
plugins: cov-2.6.0, benchmark-3.2.2
collected 20 items

secret_santa_test.py::test_ExceptionWithDuplicateAttendeeName SKIPPED                                                                                                                                                                                  [  5%]
secret_santa_test.py::test_ExceptionWithPartnerAsDuplicatedAttendee SKIPPED                                                                                                                                                                            [ 10%]
secret_santa_test.py::test_ExceptionWithDuplicatedAttendee SKIPPED                                                                                                                                                                                     [ 15%]
secret_santa_test.py::test_ExceptionWithDuplicatedPartner SKIPPED                                                                                                                                                                                      [ 20%]
secret_santa_test.py::test_canAddAttendees SKIPPED                                                                                                                                                                                                     [ 25%]
secret_santa_test.py::test_getUnmatchedAttendeesCount SKIPPED                                                                                                                                                                                          [ 30%]
secret_santa_test.py::test_checkForValidGiver SKIPPED                                                                                                                                                                                                  [ 35%]
secret_santa_test.py::test_NoValidSolution1 SKIPPED                                                                                                                                                                                                    [ 40%]
secret_santa_test.py::test_NoValidSolution2 SKIPPED                                                                                                                                                                                                    [ 45%]
secret_santa_test.py::test_NoValidSolution3 SKIPPED                                                                                                                                                                                                    [ 50%]
secret_santa_test.py::test_canShuffleAttendees SKIPPED                                                                                                                                                                                                 [ 55%]
secret_santa_test.py::test_resetUnmatchedAttendeesCount SKIPPED                                                                                                                                                                                        [ 60%]
secret_santa_test.py::test_canSolveGoodSolution1 SKIPPED                                                                                                                                                                                               [ 65%]
secret_santa_test.py::test_canSolveGoodSolution2 SKIPPED                                                                                                                                                                                               [ 70%]
secret_santa_test.py::test_canSolveFlintstones1 SKIPPED                                                                                                                                                                                                [ 75%]
secret_santa_test.py::test_canSolveFlintstones2 SKIPPED                                                                                                                                                                                                [ 80%]
secret_santa_test.py::test_cannotSolveFlintstones1 SKIPPED                                                                                                                                                                                             [ 85%]
secret_santa_test.py::test_cannotSolveFlintstones2 SKIPPED                                                                                                                                                                                             [ 90%]
secret_santa_test.py::test_canSolveBenchmark1 PASSED                                                                                                                                                                                                   [ 95%]
secret_santa_test.py::test_canSolveBenchmark2 PASSED                                                                                                                                                                                                   [100%]
Saved benchmark data in: /home/owner/Documents/Python/Secret-Santa/.benchmarks/Linux-CPython-2.7-64bit/0014_8a13a4792486bbd1810a8463f268a7c841cdb6bf_20190127_224954_uncommited-changes.json



-------------------------------------------------------------------------------------- benchmark: 2 tests --------------------------------------------------------------------------------------
Name (time in us)               Min                Max               Mean            StdDev             Median               IQR            Outliers  OPS (Kops/s)            Rounds  Iterations
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_canSolveBenchmark2     16.9277 (1.0)      34.0939 (1.0)      17.9517 (1.0)      0.7467 (1.0)      17.8814 (1.0)      0.2384 (1.0)     5924;5924       55.7049 (1.0)       27777           1
test_canSolveBenchmark1     17.8814 (1.06)     44.1074 (1.29)     19.0119 (1.06)     1.3694 (1.83)     19.0735 (1.07)     0.2384 (1.0)      607;3869       52.5987 (0.94)      14267           1
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
============================================================================================================ 2 passed, 18 skipped in 3.22 seconds ============================================================================================================
$
```

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

There are some slight version differences between Python 2 and Python 3.

#### Python 2

* python __2.7.12__
* pytest __3.10.1__
* pytest-benchmark __3.2.2__
* pytest-cov __2.6.0__

#### Python 3

* python __3.5.2__
* pytest __4.1.1__
* pytest-benchmark __3.2.2__
* pytest-cov __2.6.1__

## To Do

- [x] Add custom exceptions
- [x] Add logic for unsolvable cases
- [x] Add retry logic for bad solutions
- [x] Add coverage reporting
- [x] Increase code coverage
- [x] Add benchmarks for historical comparison purposes
- [x] Refactor to extend to seasonal (rather than simply family) gatherings
- [x] Conform code to `pylint`
- [x] Conform code to `pycodestyle`
- [x] Conform code to `pydocstyle`
- [x] Conform code to `pydoc`
- [x] Make code Python 2 and Python 3 compatible
- [ ] Optional enhancement - prevent circular gift exchanges
- [ ] Optional enhancement - prevent intra-family gift exchanges
- [ ] Optional enhancement - allow for more than 1 present
