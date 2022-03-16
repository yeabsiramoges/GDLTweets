import requests
import os
import json
import datetime

#Relevant country codes: BR, IN, US, CA, ZA
#Key issues: Disability, Incarceration, Disability
search_country = 'US'
key_issue = 'disability'

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = os.environ.get("BEARER_TOKEN")

search_url = "https://api.twitter.com/2/tweets/search/all"

# Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
# expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields
query_params = {    
    'query': f'dignity {key_issue} -is:retweet place_country:{search_country}',
    'expansions': 'author_id,geo.place_id',
    'tweet.fields': 'author_id,created_at,id,geo,lang,public_metrics,text,withheld',
    'user.fields': 'description,location,name,protected,username,verified',
    'place.fields': 'contained_within,country,country_code,full_name,id,geo,name,place_type',
    'max_results': '10',
    'start_time': '2017-01-01T00:00:00.00Z',
    'end_time': '2022-03-16T13:00:00.00Z'
    }


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2FullArchiveSearchPython"
    return r

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main():
    json_response = connect_to_endpoint(search_url, query_params)
    print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()