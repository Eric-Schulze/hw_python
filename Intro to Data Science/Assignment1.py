#Eric Schulze
#C498 Summer 2017
#Programming Assignment 1
#5/16/17

import pandas as pa
import numpy as np

def buildDataFrame():
    countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
                        'Netherlands', 'Germany', 'Switzerland', 'Belarus',
                        'Austria', 'France', 'Poland', 'China', 'Korea', 
                        'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
                        'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
                        'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

    gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
    silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
    bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]


    df = pa.DataFrame({'country': pa.Series(countries), 'gold': pa.Series(gold), 
                                    'silver':pa.Series(silver), 'bronze': pa.Series(bronze)})
    return df
    

def findAvgBronzeAtLeastOneGold(df):
    at_least_one_gold = df['bronze'][df['gold'] >= 1]
    
    return np.mean(at_least_one_gold)
    
    
def avgMedalCount(df):
    medal_df = df[['gold','silver','bronze']]
    avg_medal_df = pa.DataFrame(medal_df.apply(np.mean))
    avg_medal_df.append(["Avg Medal Count"], ignore_index=False)

    return avg_medal_df
    
def calculateOlympicPoints(df):
    medal_df = df[['gold','silver','bronze']]
    point_values = [4,2,1]
    
    points_df = pa.DataFrame({'Points':np.dot(medal_df, point_values), 'Country':df['country']})
    return(points_df)


olympic_medal_counts_df = buildDataFrame()

avg_bronze_at_least_one_gold = findAvgBronzeAtLeastOneGold(olympic_medal_counts_df)

avg_medal_count = avgMedalCount(olympic_medal_counts_df)

olympic_points_df = calculateOlympicPoints(olympic_medal_counts_df)


print (olympic_medal_counts_df)
print()
print ("Average Bronze From Countries with at Least 1 Gold Medal: " + 
            str(avg_bronze_at_least_one_gold))
print()
print("Average Medal Counts: " + str(avg_medal_count))
print()
print("Points earned by country: \n" + str(olympic_points_df))