from typing import List, Tuple
from re import compile
import json
from collections import Counter
from memory_profiler import profile
import argparse

@profile
def q3_time(file_path: str) -> List[Tuple[str, int]]:
    #Keep track of mentioned users
    mentionedUsers = []

    #Compile a regex to find '@' mentions
    regex = compile(r'(@\w+)')

    #Read whole file
    with open(file_path, "r") as f:
        rawContent = f.read()

    #Split the file by newlines
    for tweet in map(json.loads, rawContent.splitlines()): #Using splitlines will allow to skip newlines which may be present on the tweet's content
        #Parse tweet, find mentioned users and add them to the tracker
        mentionedUsers += regex.findall(tweet['content'])

    return Counter(mentionedUsers).most_common(10)

# If running from main, allow receiving a filename as an argument, used for benchmarking from included jupyter notebook
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    q3_time(args.filename)