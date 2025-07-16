from statsmodels.stats.weightstats import ztest

ztest(solar_data['efficiency'], value=14)