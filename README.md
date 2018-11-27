# Secret Santa

A simple Secret Santa gift exchange

## Motivation

Family members register for a gift exchange. Partners of family members cannot
receive gifts from that family member (and vice-versa). Everyone else will
receive a gift from a random family member.

[TDD](http://en.wikipedia.org/wiki/Test-driven_development) was used for this exercise
 with the [pytest framework](http://docs.pytest.org/en/latest/).

## Prerequisites

Install prerequisites as follows:

    $ pip install --user -r requirements.txt

## Tests

Run unit tests as follows:

    $ pytest -v

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
