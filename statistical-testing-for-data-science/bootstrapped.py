import bootsrapped.bootstrap as bs
import bootstrapped.compare_functions as bs_compare
import bootstrapped.stats_functions as bs_stats

bs.bootstrap_ab(test=ab_df['b_sale'].values,
                ctrl=ab_df['a_sale'].values,
                stat_func=bs_stats.mean,
                compare_func=bs_compare.difference,
                alpha=0.05)