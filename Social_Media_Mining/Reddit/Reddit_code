#import packages
import praw
from praw.models import MoreComments
from pandas import Series, DataFrame
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
lem = WordNetLemmatizer()
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


#create a reddit object
reddit = praw.Reddit(client_id='xxxxx', \
                     client_secret='xxxxx', \
                     user_agent='Ashley Thornton', \
                     username='ashthorn2', \
                     password='xxxxx')

#connect to intermittent fasting subreddit
i_subreddit = reddit.subreddit('intermittentfasting')

#getting submissions
i_submissions = i_subreddit.search('intermittent fasting')

#create a list for the comments from the fitness subreddit to reside
intermittentfastingcomments = []

#place comments into list
for submission in i_submissions :
    submission.comments.replace_more(limit=0)
    for comment in submission.comments :
        intermittentfastingcomments.append(comment.body)

#repeat for nutrition subreddit
n_subreddit = reddit.subreddit('nutrition')
n_submissions = n_subreddit.search('intermittent fasting')
nutritioncomments = []
for submission in n_submissions :
    submission.comments.replace_more(limit=0)
    for comment in submission.comments :
        nutritioncomments.append(comment.body)

#repeat for fitness subreddit
f_subreddit = reddit.subreddit('fitness')
f_submissions = f_subreddit.search('intermittent fasting')
fitnesscomments = []
for submission in f_submissions :
    submission.comments.replace_more(limit=0)
    for comment in submission.comments :
        fitnesscomments.append(comment.body)

#repeat for weight loss subreddit
w_subreddit = reddit.subreddit('Weightlosstechniques')
w_submissions = w_subreddit.search('intermittent fasting')
weightlosscomments = []
for submission in w_submissions :
    submission.comments.replace_more(limit=0)
    for comment in submission.comments :
        weightlosscomments.append(comment.body)


######## Sentiment analysis

analyzer = SentimentIntensityAnalyzer()

#intermittent fasting
i_compound = []
i_pos = []
i_neu = []
i_neg = []
for comment in intermittentfastingcomments:
    i_compound.append(analyzer.polarity_scores(comment)['compound'])
    i_pos.append(analyzer.polarity_scores(comment)['pos'])
    i_neu.append(analyzer.polarity_scores(comment)['neu'])
    i_neg.append(analyzer.polarity_scores(comment)['neg'])

intermittentfasting_df = DataFrame({'Comment': intermittentfastingcomments,
                'Compound': i_compound,
                'Positive': i_pos,
                'Neutral': i_neu,
                'Negative': i_neg})

#nutrition
n_compound = []
n_pos = []
n_neu = []
n_neg = []
for comment in nutritioncomments:
    n_compound.append(analyzer.polarity_scores(comment)['compound'])
    n_pos.append(analyzer.polarity_scores(comment)['pos'])
    n_neu.append(analyzer.polarity_scores(comment)['neu'])
    n_neg.append(analyzer.polarity_scores(comment)['neg'])

nutrition_df = DataFrame({'Comment': nutritioncomments,
                'Compound': n_compound,
                'Positive': n_pos,
                'Neutral': n_neu,
                'Negative': n_neg})

#fitness
f_compound = []
f_pos = []
f_neu = []
f_neg = []

for comment in fitnesscomments:
    f_compound.append(analyzer.polarity_scores(comment)['compound'])
    f_pos.append(analyzer.polarity_scores(comment)['pos'])
    f_neu.append(analyzer.polarity_scores(comment)['neu'])
    f_neg.append(analyzer.polarity_scores(comment)['neg'])

fitness_df = DataFrame({'Comment': fitnesscomments,
                'Compound': f_compound,
                'Positive': f_pos,
                'Neutral': f_neu,
                'Negative': f_neg})

#weight loss
w_compound = []
w_pos = []
w_neu = []
w_neg = []

for comment in weightlosscomments:
    w_compound.append(analyzer.polarity_scores(comment)['compound'])
    w_pos.append(analyzer.polarity_scores(comment)['pos'])
    w_neu.append(analyzer.polarity_scores(comment)['neu'])
    w_neg.append(analyzer.polarity_scores(comment)['neg'])

weightloss_df = DataFrame({'Comment': weightlosscomments,
                'Compound': w_compound,
                'Positive': w_pos,
                'Neutral': w_neu,
                'Negative': w_neg})

#Find average of the compound column of each df
intermittentfasting_df.loc[:,"Compound"].mean()
nutrition_df.loc[:,"Compound"].mean()
fitness_df.loc[:,"Compound"].mean()
weightloss_df.loc[:,"Compound"].mean()


######## Tokenize, remove stop words, then lemmatize

#tokenize
intermittentfastingcomments_tokenized = [sub.split() for sub in intermittentfastingcomments]
nutritioncomments_tokenized = [sub.split() for sub in nutritioncomments]
fitnesscomments_tokenized = [sub.split() for sub in fitnesscomments]
weightlosscomments_tokenized = [sub.split() for sub in weightlosscomments]

#define stop words
stop_words = stopwords.words('english')

#remove stop words
intermittentfastingcomments_edited = []
for list in intermittentfastingcomments_tokenized:
	for word in list:
		if word not in stop_words:
			intermittentfastingcomments_edited.append(word)

nutritioncomments_edited = []
for list in nutritioncomments_tokenized:
	for word in list:
		if word not in stop_words:
			nutritioncomments_edited.append(word)

fitnesscomments_edited = []
for list in fitnesscomments_tokenized:
	for word in list:
		if word not in stop_words:
			fitnesscomments_edited.append(word)

weightlosscomments_edited = []
for list in weightlosscomments_tokenized:
	for word in list:
		if word not in stop_words:
			weightlosscomments_edited.append(word)

#lemmatize
for word in intermittentfastingcomments_edited:
	lem.lemmatize(word)

for word in nutritioncomments_edited:
	lem.lemmatize(word)

for word in fitnesscomments_edited:
	lem.lemmatize(word)

for word in weightlosscomments_edited:
	lem.lemmatize(word)


######## Create a word cloud for each subreddit

#intermittent fasting
intermittentfasting_string =(" ").join(intermittentfastingcomments_edited)
i_wordcloud=WordCloud(max_font_size=50, max_words=100, background_color="white").generate(intermittentfasting_string)
plt.imshow(i_wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

#nutrition
nutrition_string =(" ").join(nutritioncomments_edited)
n_wordcloud=WordCloud(max_font_size=50, max_words=100, background_color="white").generate(nutrition_string)
plt.imshow(n_wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

#fitness
fitness_string =(" ").join(fitnesscomments_edited)
f_wordcloud=WordCloud(max_font_size=50, max_words=100, background_color="white").generate(fitness_string)
plt.imshow(f_wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

#weight loss
weightloss_string =(" ").join(weightlosscomments_edited)
w_wordcloud=WordCloud(max_font_size=50, max_words=100, background_color="white").generate(weightloss_string)
plt.imshow(w_wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()


######## Export data into CSVs

intermittentfasting_df.to_csv(r'C:\Users\ashle\OneDrive\Documents\Personal\School\Indiana University\Spring 2020\Social Media Mining\Reddit\csv\intermittentfasting.csv', index=False, header=True)
nutrition_df.to_csv(r'C:\Users\ashle\OneDrive\Documents\Personal\School\Indiana University\Spring 2020\Social Media Mining\Reddit\csv\nutrition.csv', index=False, header=True)
fitness_df.to_csv(r'C:\Users\ashle\OneDrive\Documents\Personal\School\Indiana University\Spring 2020\Social Media Mining\Reddit\csv\fitness.csv', index=False, header=True)
weightloss_df.to_csv(r'C:\Users\ashle\OneDrive\Documents\Personal\School\Indiana University\Spring 2020\Social Media Mining\Reddit\csv\weightloss.csv', index=False, header=True)
