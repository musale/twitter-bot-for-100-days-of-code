"""run file which houses the bot logic."""
import json
import os
from os.path import dirname, join

import requests
import twitter
from dotenv import load_dotenv

MAX_CHARS = 140

# load the environment variables
dotenv_path = join(dirname("__file__"), '.env')
load_dotenv(dotenv_path)
my_consumer_key = os.environ.get("my_consumer_key")
my_consumer_secret = os.environ.get("my_consumer_secret")
my_access_token_key = os.environ.get("my_access_token_key")
my_access_token_secret = os.environ.get("my_access_token_secret")


# GET all the commits of the repo
# Change this URL unless you want to tweet my silly commits
response = requests.get(
    "https://api.github.com/repos/musale/100-days-of-code/commits")

# get the commit message of the latest commit
commit = json.loads(response.content)[0]['commit']['message']

# read existing logged commit
logs = open("logs.txt", "r")
previous_commit = logs.readline()


def break_down_tweet(full_tweet):
    """Break a string tweet into a list of strings <= 140 characters."""
    if len(full_tweet) > MAX_CHARS:
        full_tweet = [full_tweet[i * MAX_CHARS:i * MAX_CHARS + MAX_CHARS]
                      for i, blah in enumerate(full_tweet[::MAX_CHARS])]
    return full_tweet


def main():
    """Main function."""
    if commit == previous_commit:
        # No new commit, do something weird
        print "No new commit mate"
    else:
        # New commit, tweet it!
        # Attach hashtag
        full_tweet = "#100DaysOfCode %s" % (commit,)

        # if full_tweet is more than 140 chars, break it down the post as
        # thread
        final_tweet = break_down_tweet(full_tweet)
        try:
            tweet = twitter.Api(consumer_key=my_consumer_key,
                                consumer_secret=my_consumer_secret,
                                access_token_key=my_access_token_key,
                                access_token_secret=my_access_token_secret)

            # tweet first tweet
            if isinstance(final_tweet, str):
                print "final str: %s" % (final_tweet,)
                update = tweet.PostUpdate(full_tweet)
            elif isinstance(final_tweet, list):
                print "final list: %s" % (final_tweet,)
                update_list = iter(final_tweet)
                update = tweet.PostUpdate(next(update_list))
                # get id for first tweet to make a thread
                id = update.id

                # tweet the rest if they exist
                try:
                    for next_update in update_list:
                        print next_update
                        tweet.PostUpdate(next_update, in_reply_to_status_id=id)
                except Exception:
                    pass
            elif isinstance(final_tweet, unicode):
                print "final unicode: %s" % (final_tweet,)
                update = tweet.PostUpdate(str(full_tweet))
            else:
                print "weird tweet:: %s" % (type(final_tweet),)

            # write commit to log file
            new_log = open("logs.txt", "w")
            new_log.write(commit)
            new_log.close()
        except Exception:
            print "failed tweeting"


if __name__ == '__main__':
    print "bot up ..."
    main()
    print "checking out ..."
