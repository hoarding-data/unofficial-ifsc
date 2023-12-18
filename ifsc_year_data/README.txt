replace all \u00a0\u00a0


for all 2019 and below need to change lead format.
pre start 2020:
{
    "category_round_id": 5504,
    "round_name": "Qualification",
    "score": "17+ 58.  |  Top 1. [15.26]",
    "speed_elimination_stages": []
},
post start 2020:
{
    "category_round_id": 6181,
    "round_name": "Qualification",
    "score": "1.41",
    "ascents": [
        {
            "route_id": 1279,
            "route_name": "1",
            "top": true,
            "plus": false,
            "rank": 1,
            "corrective_rank": 1,
            "score": "TOP"
        },
        {
            "route_id": 1280,
            "route_name": "2",
            "top": true,
            "plus": false,
            "rank": 1,
            "corrective_rank": 2,
            "score": "TOP"
        }
    ]
},

score is [   ]
ascents is split("|")
for route:
- route_name is index+1
- top is =="Top"
- plus is if {\d+}\+
- score is composed of <score> <rank>.
- corrective rank will be null because calculating that would be too much of a pain