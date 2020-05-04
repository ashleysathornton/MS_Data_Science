import GetOldTweets3 as got
from pandas import Series, DataFrame
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#2019 tweets, capped at 10k
tweetCriteria = got.manager.TweetCriteria().setQuerySearch('airbnb')\
											.setSince("2019-01-01")\
											.setUntil("2020-01-01")\
											.setMaxTweets(10000)\
											.setTopTweets(True)
tweets1 = got.manager.TweetManager.getTweets(tweetCriteria)[0:10000]
tweets2019 = []
for tweet in tweets1 :
    tweets2019.append(tweet.text)

#1st week of March 2020, capped at 10k
tweetCriteria2 = got.manager.TweetCriteria().setQuerySearch('airbnb')\
											.setSince("2020-03-01")\
											.setUntil("2020-03-08")\
											.setMaxTweets(10000)\
											.setTopTweets(True)
tweets2 = got.manager.TweetManager.getTweets(tweetCriteria2)[0:10]
tweetsmar1thru72020 = []
for tweet in tweets2 :
    tweetsmar1thru72020.append(tweet.text)

#2nd week of March 2020, capped at 10k
tweetCriteria3 = got.manager.TweetCriteria().setQuerySearch('airbnb')\
											.setSince("2020-03-08")\
											.setUntil("2020-03-15")\
											.setMaxTweets(10000)\
											.setTopTweets(True)
tweets3 = got.manager.TweetManager.getTweets(tweetCriteria3)[0:10000]
tweetsmar8thru142020 = []
for tweet in tweets3 :
    tweetsmar8thru142020.append(tweet.text)

#3rd week of March 2020, capped at 10k
tweetCriteria4 = got.manager.TweetCriteria().setQuerySearch('airbnb')\
											.setSince("2020-03-15")\
											.setUntil("2020-03-22")\
											.setMaxTweets(10000)\
											.setTopTweets(True)
tweets4 = got.manager.TweetManager.getTweets(tweetCriteria4)[0:10000]
tweetsmar15thru212020 = []
for tweet in tweets4 :
    tweetsmar15thru212020.append(tweet.text)

#4th week of March 2020, capped at 10k
tweetCriteria5 = got.manager.TweetCriteria().setQuerySearch('airbnb')\
											.setSince("2020-03-22")\
											.setUntil("2020-03-29")\
											.setMaxTweets(10000)\
											.setTopTweets(True)
tweets5 = got.manager.TweetManager.getTweets(tweetCriteria5)[0:10000]
tweetsmar22thru282020 = []
for tweet in tweets5 :
    tweetsmar22thru282020.append(tweet.text)

#1st week of April 2020, capped at 10k
tweetCriteria6 = got.manager.TweetCriteria().setQuerySearch('airbnb')\
											.setSince("2020-03-29")\
											.setUntil("2020-04-05")\
											.setMaxTweets(10000)\
											.setTopTweets(True)
tweets6 = got.manager.TweetManager.getTweets(tweetCriteria6)[0:10000]
tweetsmar29thruapr42020 = []
for tweet in tweets6 :
    tweetsmar29thruapr42020.append(tweet.text)

#2nd week of April 2020, capped at 10k
tweetCriteria7 = got.manager.TweetCriteria().setQuerySearch('airbnb')\
											.setSince("2020-04-05")\
											.setUntil("2020-04-12")\
											.setMaxTweets(10000)\
											.setTopTweets(True)
tweets7 = got.manager.TweetManager.getTweets(tweetCriteria7)[0:10000]
tweetsapr5thru112020 = []
for tweet in tweets7 :
    tweetsapr5thru112020.append(tweet.text)

#3rd week of April 2020, capped at 10k
tweetCriteria8 = got.manager.TweetCriteria().setQuerySearch('airbnb')\
											.setSince("2020-04-12")\
											.setUntil("2020-04-19")\
											.setMaxTweets(10000)\
											.setTopTweets(True)
tweets8 = got.manager.TweetManager.getTweets(tweetCriteria8)[0:10000]
tweetsapr12thru182020 = []
for tweet in tweets8 :
    tweetsapr12thru182020.append(tweet.text)


#sentiment analysis

#tweets2019

a_compound = []
a_pos = []
a_neu = []
a_neg = []

analyzer = SentimentIntensityAnalyzer()

for tweet in tweets2019:
    a_compound.append(analyzer.polarity_scores(tweet)['compound'])
    a_pos.append(analyzer.polarity_scores(tweet)['pos'])
    a_neu.append(analyzer.polarity_scores(tweet)['neu'])
    a_neg.append(analyzer.polarity_scores(tweet)['neg'])

tweets2019_df = DataFrame({'Comment': tweets2019,
                'Compound': a_compound,
                'Positive': a_pos,
                'Neutral': a_neu,
                'Negative': a_neg})


#tweetsmar1thru72020

b_compound = []
b_pos = []
b_neu = []
b_neg = []

for tweet in tweetsmar1thru72020:
    b_compound.append(analyzer.polarity_scores(tweet)['compound'])
    b_pos.append(analyzer.polarity_scores(tweet)['pos'])
    b_neu.append(analyzer.polarity_scores(tweet)['neu'])
    b_neg.append(analyzer.polarity_scores(tweet)['neg'])

tweetsmar1thru72020_df = DataFrame({'Comment': tweetsmar1thru72020,
                'Compound': b_compound,
                'Positive': b_pos,
                'Neutral': b_neu,
                'Negative': b_neg})


#tweetsmar7thru142020

c_compound = []
c_pos = []
c_neu = []
c_neg = []

for tweet in tweetsmar8thru142020:
    c_compound.append(analyzer.polarity_scores(tweet)['compound'])
    c_pos.append(analyzer.polarity_scores(tweet)['pos'])
    c_neu.append(analyzer.polarity_scores(tweet)['neu'])
    c_neg.append(analyzer.polarity_scores(tweet)['neg'])

tweetsmar8thru142020_df = DataFrame({'Comment': tweetsmar8thru142020,
                'Compound': c_compound,
                'Positive': c_pos,
                'Neutral': c_neu,
                'Negative': c_neg})


#tweetsmar15thru212020

d_compound = []
d_pos = []
d_neu = []
d_neg = []

for tweet in tweetsmar15thru212020:
    d_compound.append(analyzer.polarity_scores(tweet)['compound'])
    d_pos.append(analyzer.polarity_scores(tweet)['pos'])
    d_neu.append(analyzer.polarity_scores(tweet)['neu'])
    d_neg.append(analyzer.polarity_scores(tweet)['neg'])

tweetsmar15thru212020_df = DataFrame({'Comment': tweetsmar15thru212020,
                'Compound': d_compound,
                'Positive': d_pos,
                'Neutral': d_neu,
                'Negative': d_neg})


#tweetsmar22thru282020

e_compound = []
e_pos = []
e_neu = []
e_neg = []

for tweet in tweetsmar22thru282020:
    e_compound.append(analyzer.polarity_scores(tweet)['compound'])
    e_pos.append(analyzer.polarity_scores(tweet)['pos'])
    e_neu.append(analyzer.polarity_scores(tweet)['neu'])
    e_neg.append(analyzer.polarity_scores(tweet)['neg'])

tweetsmar22thru282020_df = DataFrame({'Comment': tweetsmar22thru282020,
                'Compound': e_compound,
                'Positive': e_pos,
                'Neutral': e_neu,
                'Negative': e_neg})


#tweetsmar29thruapr42020

f_compound = []
f_pos = []
f_neu = []
f_neg = []

for tweet in tweetsmar29thruapr42020:
    f_compound.append(analyzer.polarity_scores(tweet)['compound'])
    f_pos.append(analyzer.polarity_scores(tweet)['pos'])
    f_neu.append(analyzer.polarity_scores(tweet)['neu'])
    f_neg.append(analyzer.polarity_scores(tweet)['neg'])

tweetsmar29thruapr42020_df = DataFrame({'Comment': tweetsmar29thruapr42020,
                'Compound': f_compound,
                'Positive': f_pos,
                'Neutral': f_neu,
                'Negative': f_neg})


#tweetsapr5thru112020

g_compound = []
g_pos = []
g_neu = []
g_neg = []

for tweet in tweetsapr5thru112020:
    g_compound.append(analyzer.polarity_scores(tweet)['compound'])
    g_pos.append(analyzer.polarity_scores(tweet)['pos'])
    g_neu.append(analyzer.polarity_scores(tweet)['neu'])
    g_neg.append(analyzer.polarity_scores(tweet)['neg'])

tweetsapr5thru112020_df = DataFrame({'Comment': tweetsapr5thru112020,
                'Compound': g_compound,
                'Positive': g_pos,
                'Neutral': g_neu,
                'Negative': g_neg})


#tweetsapr12thru182020

h_compound = []
h_pos = []
h_neu = []
h_neg = []

for tweet in tweetsapr12thru182020:
    h_compound.append(analyzer.polarity_scores(tweet)['compound'])
    h_pos.append(analyzer.polarity_scores(tweet)['pos'])
    h_neu.append(analyzer.polarity_scores(tweet)['neu'])
    h_neg.append(analyzer.polarity_scores(tweet)['neg'])

tweetsapr12thru182020_df = DataFrame({'Comment': tweetsapr12thru182020,
                'Compound': h_compound,
                'Positive': h_pos,
                'Neutral': h_neu,
                'Negative': h_neg})


#Pull average from each dataframe. The average of the compound score is the overall sentiment for that period of time.

tweets2019_df.mean()
tweetsmar1thru72020_df.mean()
tweetsmar8thru142020_df.mean()
tweetsmar15thru212020_df.mean()
tweetsmar22thru282020_df.mean()
tweetsmar29thruapr42020_df.mean()
tweetsapr5thru112020_df.mean()
tweetsapr12thru182020_df.mean()


#Look at Mar 11, Mar 14, and Mar 30 to see if there are spikes
tweetCriteria9 = got.manager.TweetCriteria().setQuerySearch('airbnb')\
											.setSince("2020-03-14")\
											.setUntil("2020-03-15")\
											.setMaxTweets(10000)\
											.setTopTweets(True)
tweets9 = got.manager.TweetManager.getTweets(tweetCriteria9)[0:10000]
tweetsmar14 = []
for tweet in tweets9 :
    tweetsmar14.append(tweet.text)

tweetCriteria10 = got.manager.TweetCriteria().setQuerySearch('airbnb')\
											.setSince("2020-03-30")\
											.setUntil("2020-03-31")\
											.setMaxTweets(10000)\
											.setTopTweets(True)
tweets10 = got.manager.TweetManager.getTweets(tweetCriteria10)[0:10000]
tweetsmar30 = []
for tweet in tweets10 :
    tweetsmar30.append(tweet.text)

tweetCriteria11 = got.manager.TweetCriteria().setQuerySearch('airbnb')\
											.setSince("2020-03-11")\
											.setUntil("2020-03-12")\
											.setMaxTweets(10000)\
											.setTopTweets(True)
tweets11 = got.manager.TweetManager.getTweets(tweetCriteria11)[0:10000]
tweetsmar11 = []
for tweet in tweets11 :
    tweetsmar11.append(tweet.text)

i_compound = []
i_pos = []
i_neu = []
i_neg = []

for tweet in tweetsmar14:
    i_compound.append(analyzer.polarity_scores(tweet)['compound'])
    i_pos.append(analyzer.polarity_scores(tweet)['pos'])
    i_neu.append(analyzer.polarity_scores(tweet)['neu'])
    i_neg.append(analyzer.polarity_scores(tweet)['neg'])

tweetsmar14_df = DataFrame({'Comment': tweetsmar14,
                'Compound': i_compound,
                'Positive': i_pos,
                'Neutral': i_neu,
                'Negative': i_neg})

j_compound = []
j_pos = []
j_neu = []
j_neg = []

for tweet in tweetsmar30:
    j_compound.append(analyzer.polarity_scores(tweet)['compound'])
    j_pos.append(analyzer.polarity_scores(tweet)['pos'])
    j_neu.append(analyzer.polarity_scores(tweet)['neu'])
    j_neg.append(analyzer.polarity_scores(tweet)['neg'])

tweetsmar30_df = DataFrame({'Comment': tweetsmar30,
                'Compound': j_compound,
                'Positive': j_pos,
                'Neutral': j_neu,
                'Negative': j_neg})

k_compound = []
k_pos = []
k_neu = []
k_neg = []

for tweet in tweetsmar11:
    k_compound.append(analyzer.polarity_scores(tweet)['compound'])
    k_pos.append(analyzer.polarity_scores(tweet)['pos'])
    k_neu.append(analyzer.polarity_scores(tweet)['neu'])
    k_neg.append(analyzer.polarity_scores(tweet)['neg'])

tweetsmar11_df = DataFrame({'Comment': tweetsmar11,
                'Compound': k_compound,
                'Positive': k_pos,
                'Neutral': k_neu,
                'Negative': k_neg})

tweetsmar14_df.mean()
tweetsmar30_df.mean()
tweetsmar11_df.mean()


#Put data into CSVs

tweets2019_df.to_csv(r'C:\Users\ashle\OneDrive\Documents\Personal\School\Indiana University\Spring 2020\Social Media Mining\Twitter\csvs\tweets2019.csv', index=False, header=True)
tweetsmar1thru72020_df.to_csv(r'C:\Users\ashle\OneDrive\Documents\Personal\School\Indiana University\Spring 2020\Social Media Mining\Twitter\csvs\tweetsmar1thru72020.csv', index=False, header=True)
tweetsmar8thru142020_df.to_csv(r'C:\Users\ashle\OneDrive\Documents\Personal\School\Indiana University\Spring 2020\Social Media Mining\Twitter\csvs\tweetsmar8thru142020.csv', index=False, header=True)
tweetsmar15thru212020_df.to_csv(r'C:\Users\ashle\OneDrive\Documents\Personal\School\Indiana University\Spring 2020\Social Media Mining\Twitter\csvs\tweetsmar15thru212020.csv', index=False, header=True)
tweetsmar22thru282020_df.to_csv(r'C:\Users\ashle\OneDrive\Documents\Personal\School\Indiana University\Spring 2020\Social Media Mining\Twitter\csvs\tweetsmar22thru282020.csv', index=False, header=True)
tweetsmar29thruapr42020_df.to_csv(r'C:\Users\ashle\OneDrive\Documents\Personal\School\Indiana University\Spring 2020\Social Media Mining\Twitter\csvs\tweetsmar29thruapr42020.csv', index=False, header=True)
tweetsapr5thru112020_df.to_csv(r'C:\Users\ashle\OneDrive\Documents\Personal\School\Indiana University\Spring 2020\Social Media Mining\Twitter\csvs\tweetsapr5thru112020_df.csv', index=False, header=True)
tweetsapr12thru182020_df.to_csv(r'C:\Users\ashle\OneDrive\Documents\Personal\School\Indiana University\Spring 2020\Social Media Mining\Twitter\csvs\tweetsapr12thru182020.csv', index=False, header=True)
tweetsmar14_df.to_csv(r'C:\Users\ashle\OneDrive\Documents\Personal\School\Indiana University\Spring 2020\Social Media Mining\Twitter\csvs\tweetsmar14_df.csv', index=False, header=True)
tweetsmar30_df.to_csv(r'C:\Users\ashle\OneDrive\Documents\Personal\School\Indiana University\Spring 2020\Social Media Mining\Twitter\csvs\tweetsmar30_df.csv', index=False, header=True)
tweetsmar11_df.to_csv(r'C:\Users\ashle\OneDrive\Documents\Personal\School\Indiana University\Spring 2020\Social Media Mining\Twitter\csvs\tweetsmar11.csv', index=False, header=True)
