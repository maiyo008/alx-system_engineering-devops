# 0x16. API advanced

## Background Context
Questions involving APIs are common for interviews. Sometimes they’re as simple as ‘write a Python script that queries a given endpoint’, sometimes they require you to use recursive functions and format/sort the results.

A great API to use for some practice is the Reddit API. There’s a lot of endpoints available, many that don’t require any form of authentication, and there’s tons of information to be parsed out and presented. Getting comfortable with API calls now can save you some face during technical interviews and even outside of the job market, you might find personal use cases to make your life a little bit easier.

## Resources
**Read or watch:**

* [Reddit API Documentation](https://www.reddit.com/dev/api/)
* [Query String](https://en.wikipedia.org/wiki/Query_string)

## Tasks

### Task 0. How many subs?
<Details>
Write a function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.

Hint: No authentication is necessary for most features of the Reddit API. If you’re getting errors related to Too Many Requests, ensure you’re setting a custom User-Agent.

Requirements:

* Prototype: def number_of_subscribers(subreddit)
* If not a valid subreddit, return 0.
* NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.
</Details>

### Task 1. Top ten
<Details>
Write a function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.

Requirements:

* Prototype: def top_ten(subreddit)
* If not a valid subreddit, print None.
* NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.
</Details>

### Task 2. Recurse it
<Details>
Write a recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function should return None.

Hint: The Reddit API uses pagination for separating pages of responses.

Requirements:

* Prototype: def recurse(subreddit, hot_list=[])
* Note: You may change the prototype, but it must be able to be called with just a subreddit supplied. AKA you can add a counter, but it * must work without supplying a starting value in the main.
* If not a valid subreddit, return None.
NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.
Your code will NOT pass if you are using a loop and not recursively calling the function! This /can/ be done with a loop but the point is to use a recursive function. :)
</Details>