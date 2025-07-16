## Statitistics for Data Science
Probabilities lay foundation for machine learning and statistical methods, therefore in this chapter we'll look at the basics of probability.

# Probability, distribution and Sampling
In this chapter we'll cover the following:
Foundational probability concepts
Common Sampling techniques distribution in data science
Useful sampling techniques for data science.

# Probability basics
Probability is all about uncertainity, for example a flip of a normal coin we.re never sure if it will land on one side or the other.
Probability function is that we count the number of times the desired event happens over the total number of outcomes
P(coinflip == H) = 0.5 and P(coinflip == T) = 0.5.
A continuos variable is one that can take any value between two points, like time or length
In a process where efficiencies are not are not always the same are randomness is acalled stochastic

# Independent and Conditional Probabilities
When the outcome of one event affects the probability of another event happening, we describe this as conditional probability.
Let's start the experiment over with 3 of each type of candy in the bag and find the probability of getting 2 red candies in a row. To do this, we simply multiply the two probabilities we got above - 1/3 * 1/4 = 1/12, which is roughly 8.3%

P(R1 and R2) = P(R1) * P(R2 | R1)

The P() represent probabilities of an event as before. The R1 and R2 notation represents drawing a red candy in our first and second draws respectively.
The P(R2 | R1) notation means the probability of drawing a red candy on the second draw (R2) given we drew candy on the first draw (R1).
The pipe symbol (|) is a mathematical way of representing conditional or dependence in probanility equations like these
P(R1) = 1/3
P(R2 | R1) = 1/4
P(R1 and R2) = 1/12

# Bayes' Theorem
Bayes' Theorem(sometimes called Bayes' law or Bayes' rule) is named after a reverend from the 1700s, Thpmas bayes who partially invented it. The theorem can be written as an equation:
P(A|B) = P(A) * P(B|A) / P(B)
We can see there are some independent probabilites for two events, A and B and two conditional probabilites: the probability of A given B, P(A|B) and the probability of B given P(B|A)

Another way to write this is with a hypothesis (a condition we can test), H and evidence E
P(H|E) = p(H) * p(E|H) / P(E)

# Distributions
Probability distributions are a way of describing all possible outcomes a random variable can take within a sample space. Thereare alot of probability distributions.

# The normal distribtuion and using scipy to generate distributions
The normal distribution is also called the Gaussian or the bell curve and shows up often.
We can generate most common distribution in Python using Scipy

We can install Scipy using conda install -c conda-forge scipy -y
Then we can create and plot a normal distribution see normal-dist.py

# Descriptive statistics of distributions.
Distributions are mathematical equations charecterized by parameters. For example the normal distribution's PDF is represented with an equation 
![alt text](image.png)
ann nabwire