# Work Session Notes

## Assumptions

**Assumption 1**:
Different types of people choose to fund different types of loans.

**Assumption 2**:
People make loans based on information presented to them about the loans.

**Assumption 3**:
Similar "types" of people choose to fund the same groups of loans.

**Assumption 4**:
It is useful to target these subgroups differently to find loans they are more
likely to fund.

## Methods

We can use [principal component analysis]() on the co-occurrence matrix of
people to loans. This will give us a way to cluster users based on latent
factors.

We can then, for each cluster of users, perform a linear regression on those
users and the loans to see which factors are important to those users (and how
they affect whether the user lends).
