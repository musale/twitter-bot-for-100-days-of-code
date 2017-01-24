# twitter-bot-for-100-days-of-code
A simple twitter bot that posts your commits to your 100-days-of-code forked repo.

What it does is get all the commits for your 100-days-of-code repo, gets the latest commit and tweets it out

## Setup
1. clone this repo and install requirements using ```pip```
2. re-name ```.sample_dot_env``` to ```.env```
3. go to [twitter developer](https://apps.twitter.com) and create an app. this gives you the credentials you need so fill them in you ```.env``` variables.
4. change the ```url``` in ```run.py``` to point to your ```100-days-of-code``` repo
5. test by running ```./run.py```
6. check twitter for your tweet
7. make a cron, use a scheduler, make it your own!
