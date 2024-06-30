#!/usr/bin/python3

"""
This script queries the Reddit API and prints the titles of the top 10 hot posts 
from a given subreddit.

Requirements:
- requests library
"""

import requests

def top_ten(subreddit):
  """Prints titles of the top 10 hot posts from a subreddit.

  Args:
    subreddit: The name of the subreddit to query (string).

  Returns:
    None if subreddit is invalid, otherwise prints titles.
  """
  # Base URL for Reddit API endpoint
  url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

  # Make the request without following redirects
  response = requests.get(url, allow_redirects=False)

  # Check for successful response (200 OK)
  if response.status_code == 200:
    # Parse the JSON data
    data = response.json()
    
    # Check for valid data structure (avoid following potential redirects)
    if data.get('data') and data['data'].get('children'):
      # Extract titles of the top 10 posts
      for post in data['data']['children'][:10]:
        print(post['data']['title'])
    else:
      print("Subreddit may be invalid or private.")
  else:
    print(f"Error: {response.status_code}")

# Example usage
subreddit = "python"
top_ten(subreddit)
