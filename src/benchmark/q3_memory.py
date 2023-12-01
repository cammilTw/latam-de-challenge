from typing import List, Tuple
from re import compile
import json
from memory_profiler import profile
import argparse

@profile
def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    #Keep track of mentioned users
    mentionedUsersCount = {}

    #Compile a regex to find '@' mentions
    regex = compile(r'(@\w+)')

    #Read file, by line
    with open(file_path, "r") as f:
        for line in f:
            #Find mentions on tweet
            mentionedUsers = regex.findall(json.loads(line)['content'])

            #Add users to the tracker
            for mentionedUser in mentionedUsers:
                mentionedUsersCount[mentionedUser] = mentionedUsersCount.get(mentionedUser, 0) + 1

    #Sort mentioned users by count then return
    sortedMentionedUsers = sorted(mentionedUsersCount, key=lambda e: mentionedUsersCount[e], reverse=True)[0:10]
    return [(mentionedUser, mentionedUsersCount[mentionedUser]) for mentionedUser in sortedMentionedUsers]

# If running from main, allow receiving a filename as an argument, used for benchmarking from included jupyter notebook
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    q3_memory(args.filename)