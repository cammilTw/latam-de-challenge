from typing import List, Tuple
from emoji import EMOJI_DATA
import json
from memory_profiler import profile
import argparse

@profile
def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    #Keep track of emojis
    emojiCount = {}

    #Read file, by line
    with open(file_path, "r") as f:
        for line in f:
            #Parse line, find emojis and add them to the tracker
            emojis = [c for c in json.loads(line)['content'] if c in EMOJI_DATA]
            for emoji in emojis:
                emojiCount[emoji] = emojiCount.get(emoji, 0) + 1

    #Sort emojis by count
    sortedEmojis = sorted(emojiCount, key=lambda e: emojiCount[e], reverse=True)[0:10]
    return [(emoji, emojiCount[emoji]) for emoji in sortedEmojis]

# If running from main, allow receiving a filename as an argument, used for benchmarking from included jupyter notebook
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    q2_memory(args.filename)