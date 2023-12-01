from typing import List, Tuple
from datetime import datetime, date
from memory_profiler import profile
import json
import argparse

@profile
def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    #Keep track of tweet count by date
    tweetCountByDate = {}

    #Keep track of user tweet count by date
    tweetUsersByDate = {}

    #Read file, by line
    with open(file_path, "r") as f:
        for line in f:
            #Parse line, get username and date
            parsedLine = json.loads(line)
            tweetDate = date.fromisoformat(parsedLine['date'].split('T')[0]) #Didn't use strptime due to local Python version
            tweetUsername = parsedLine['user']['username']

            #Add values to trackers
            tweetCountByDate[tweetDate] = tweetCountByDate.get(tweetDate, 0) + 1
            tweetUsersByDate[tweetDate] = tweetUsersByDate.get(tweetDate, {})
            tweetUsersByDate[tweetDate][tweetUsername] = tweetUsersByDate[tweetDate].get(tweetUsername, 0) + 1

        #Sort dates by tweet count then for each date sort their respective users to get the top one
        output = []
        sortedDates = sorted(tweetCountByDate, key=lambda d: tweetCountByDate[d], reverse=True)[0:10]
        for dateId in sortedDates:
            mostTweetsUser = sorted(tweetUsersByDate[dateId], key=lambda username: tweetUsersByDate[dateId][username], reverse=True)[0]
            output.append((dateId, mostTweetsUser))

        return output

# If running from main, allow receiving a filename as an argument, used for benchmarking from included jupyter notebook
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    q1_memory(args.filename)