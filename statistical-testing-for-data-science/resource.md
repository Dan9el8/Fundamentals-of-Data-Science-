### Statistical testing for data science
In this topic we will leverage that understanding to perform statistical tests that we can use to test hypothesis. We'll cover the following statistical tests in this chapter:
The t-test, z-test, and bootstraping for comparing the means of data(A/B testing)
The ANOVA test for comparing the means of groups
Testing if data comes from a distribution 
Testing for outliers with the scikit-posthocs package
Tests for relationships between variables (Pearson and chi-squared tests) 

# Statistical testing basics and sample comparison tests
We use statistical tests to check if the data supports or rejects our hypothesis.In statistics, the base case, or no-effect case is called the null hypothesis

# The t-test and z-test
The history of t-test dates back in 1908 when William Gosset invented the method while working at the Guiness brewery in Ireland.
Gosset wanted a method for taking a sample of beer and testing that is was within quality control specificatiions.
The t-test has a few variants:
One- and two-sided
One- and two-sample
Paired

One-sided test are for determining if a value is greater than or less than a specific value by a statistically significant amount.
Two-sided tests determine if a value is either greater or less than a specified value.
One-sample t-tests are for a single sample
Two-sample t-tests are for comparing two samples
Paired t-tests are for comparing the same group before and after taking a medication.

# One-sample, two-sided t-test
Our null hypothesis in the one-sample test is that the sample mean is no different from the expected mean of 14%.
The two-sided parts means that our sample mean could be above or below the expected value of 14%.
To carry out this test in Python. we can use scipy after loading our data.
check out t-test.py

# The z-test
The proper test to use for larger sample sizes is the z-test.
However we can use this from the statsmodels package.

check out z-test.py

# One-sided tests.py
Let's say we want to make sure the average efficiency of our latest batch of solar cells is greater than 14%
We can perform  this test with scipy like so:

check out one-sided-tests.py


# Two-sample t- and z-tests: A?B testing
Suppose we have a website selling laptops and want to experiment with the design to try and drive more sales.
We will change the layout in a B version of the site and compare our sales rates to the A version

ztest(ab_df['a_sale'], ab_df[b_sale])

# Paired t- and z-tests
This is for paired samples like before-and-after treatment, we could measure blood pressure of people before and after taking a medication to see if there is an effect.
A function that vcan be used for this is scipy.stats.ttest_rel, whuch can be used like this:

scipy.stats.ttest_rel(before, after)

This will return a t-statistic and p-value like with other scipy t-test functions

# Bootstraping
Its another method for A/B testing, with this we can use sampling with replacement(bootstrapping) to calculate many means of our A and B datasets, then get the confidence intervals of the difference in means that does'nt pass through 0, we can say with a certain percent confidence that the means are different.
We can use bootstrapped package

Check out bootsrapped.py

# ANOVA
Let's say we want to test several design at a time and compare them all to see which is best A, B and C designs, here we can use ANOVA test