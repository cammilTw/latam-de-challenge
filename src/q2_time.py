from typing import List, Tuple
import json
from collections import Counter
from emoji import EMOJI_DATA

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    #Keep track of emojis
    tweetedEmojis = []

    #Read whole file
    with open(file_path, "r") as f:
        rawContent = f.read()

    #Split the file by newlines
    for tweet in map(json.loads, rawContent.splitlines()): #Using splitlines will allow to skip newlines which may be present on the tweet's content
        #Parse tweet, find emojis and add them to the tracker
        tweetedEmojis += [c for c in tweet['content'] if c in EMOJI_DATA]

    return Counter(tweetedEmojis).most_common(10)