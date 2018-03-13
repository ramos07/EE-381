from scipy import stats

X = stats.binom(8, 0.16666666667)
prob = X.cdf(3)
rProb = round(prob, 3)

print ('Probability of getting "5" less than 3 times out of 8 die throws is: ', rProb)
