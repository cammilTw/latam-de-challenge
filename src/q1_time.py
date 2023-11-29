from typing import List, Tuple
from datetime import datetime, date
from collections import Counter
import json

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    #Open the whole file
    with open(file_path, "r") as f:
        rawContent = f.read()

    #Keep track of dates
    dates = []

    #Keep a list for each date, holding the username for each tweet on that date
    usersByDate = {}

    #Split the file by newlines
    for tweet in map(json.loads, rawContent.splitlines()): #Using splitlines will allow to skip newlines which may be present on the tweet's content
        #Parse tweet, get username and date, add them to the trackers
        tweetDate = date.fromisoformat(tweet['date'].split('T')[0]) #Didn't use strptime due to local Python version
        dates.append(tweetDate)
        tweetUsername = tweet['user']['username']
        if tweetDate in usersByDate:
            usersByDate[tweetDate].append(tweetUsername)
        else:
            usersByDate[tweetDate] = [tweetUsername]

    #Get the dates with most tweets
    mostTweetedDates = Counter(dates).most_common(10)

    #For the top 10 dates with most tweet counts get the most active user
    output = []
    for tweetDate in mostTweetedDates:
        dateId = tweetDate[0]
        output.append((dateId, Counter(usersByDate[dateId]).most_common(1)[0][0]))

    return output