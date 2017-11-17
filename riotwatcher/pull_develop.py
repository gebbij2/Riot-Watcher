from riotwatcher import *
from LoL import LoL
import json

#Updated imports in all Handlers/LoL, relative imports removed in Python 3.5
watcher = RiotWatcher('RGAPI-8c951269-bdec-41d0-9cae-6ba64078ce55')
my_region = 'na1'

me = watcher.summoner.by_name(my_region, 'SMACK THE POON') #I'm so sorry, I'll fix this soon
print(me)


#matches fix for timeline

# all objects are returned (by default) as a dict
# get my 1 mastery page i keep changing
# my_mastery_pages = json.dumps(watcher.masteries.by_summoner(my_region, me['id']))
# print("My Mastery Pages: ")
# print(json.loads(my_mastery_pages))
# print()

# # this function name has changed from (leagues_by_summoner) in new version
# my_ranked_stats = json.dumps(watcher.league.positions_by_summoner(my_region, me['id']))
# print("My Ranked Stats: ")
# print(json.loads(my_ranked_stats))
# print()

# # Lets some champions
# static_champ_list = json.dumps(watcher.static_data.champions(my_region))
# print("Static Champ List")
# print(json.loads(static_champ_list))
# print()

# timeline_data = json.dumps(watcher.match.timelines_by_match())
match_data = json.dumps(watcher.match.participantidentities)
# timeline_tmp = json.dumps(watcher.match)
print("Match:")
print(json.loads(match_data))


# Error checking requires importing HTTPError from requests
from requests import HTTPError

try:
    response = watcher.summoner.by_name(my_region, 'didn\'t find name')
except HTTPError as err:
    if err.response.status_code == 429:
        print('We should retry in {} seconds.'.format(e.headers['Retry-After']))
        print('this retry-after is handled by default by the RiotWatcher library')
        print('future requests wait until the retry-after time passes')
    elif err.response.status_code == 404:
        print('Summoner with that ridiculous name not found.')
    else:
        raise