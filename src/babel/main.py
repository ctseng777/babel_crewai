#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from babel.crew import TweetTranslationCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the tweet translation crew.
    """
    tweet = {
      "data": {
        "author_id": "2244994945",
        "created_at": "Wed Jan 06 18:40:40 +0000 2021",
        "id": "1346889436626259968",
        "text": "Learn how to use the user Tweet timeline and user mention timeline endpoints in the X API v2 to explore Tweet\u2026 https://t.co/56a0vZUx7i",
        "username": "XDevelopers"
      },
      "errors": [
        {
          "detail": "my detail",
          "status": 123,
          "title": "my title",
          "type": "my type"
        }
      ],
      "includes": {
        "media": [
          {
            "height": 1,
            "media_key": "my media key",
            "type": "my media type",
            "width": 1
          }
        ],
        "places": [
          {
            "contained_within": [
              "f7eb2fa2fea288b1"
            ],
            "country": "United States",
            "country_code": "US",
            "full_name": "Lakewood, CO",
            "geo": {
              "bbox": [
                -105.193475,
                39.60973,
                -105.053164,
                39.761974
              ],
              "geometry": {
                "coordinates": [
                  -105.18816086351444,
                  40.247749999999996
                ],
                "type": "Point"
              },
              "properties": {},
              "type": "Feature"
            },
            "id": "f7eb2fa2fea288b1",
            "name": "Lakewood",
            "place_type": "city"
          }
        ],
        "polls": [
          {
            "duration_minutes": 5042,
            "end_datetime": "2023-11-07T05:31:56Z",
            "id": "1365059861688410112",
            "options": [
              {
                "label": "<string>",
                "position": 123,
                "votes": 123
              }
            ],
            "voting_status": "open"
          }
        ],
        "topics": [
          {
            "description": "All about technology",
            "id": "<string>",
            "name": "Technology"
          }
        ],
        "tweets": [
          {
            "author_id": "2244994945",
            "created_at": "Wed Jan 06 18:40:40 +0000 2021",
            "id": "1346889436626259968",
            "text": "Learn how to use the user Tweet timeline and user mention timeline endpoints in the X API v2 to explore Tweet\u2026 https://t.co/56a0vZUx7i",
            "username": "XDevelopers"
          }
        ],
        "users": [
          {
            "created_at": "2013-12-14T04:35:55Z",
            "id": "2244994945",
            "name": "X Dev",
            "protected": False, # twitter API returns "false" instead of "False". For the convenient of development, we convert it to "False" 
            "username": "TwitterDev"
          }
        ]
      }
    }
    inputs = {'tweet': tweet}

    try:
        TweetTranslationCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "Tweet translation"
    }
    try:
        TweetTranslationCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        TweetTranslationCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

# def test():
#     """
#     Test the crew execution and returns the results.
#     """
#     inputs = {
#         "topic": "Tweet translation",
#         "current_year": str(datetime.now().year)
#     }
#     try:
#         TweetTranslationCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

#     except Exception as e:
#         raise Exception(f"An error occurred while testing the crew: {e}")
