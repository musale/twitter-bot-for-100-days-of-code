"""run file which houses the bot logic."""
import json

import requests

response = requests.get("https://api.github.com/repos/musale/100-days-of-code/commits")

commit = json.loads(response.content)[0]['commit']['message']
logs = open("logs.txt", "r")
previous_commit = logs.readline()

if commit == previous_commit:
    # No new commit, do something weird
    print "No new commit mate"
else:
    # New commit, tweet it!
    print "Tweeting %s" % (commit,)
    new_log = open("logs.txt", "w")
    new_log.write(commit)
    new_log.close()
