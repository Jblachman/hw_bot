
import random
import praw
import time
reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit("politics")

for i, submission in enumerate(subreddit.top(limit = 300)):
    reddit.validate_on_submit = True
    try:
        reddit.subreddit("BotTown2").submit(title = submission.title,url=submission.url)
    except praw.exceptions.RedditAPIException:
        pass
    print(submission.title)
    print("count =" ,i)
    time.sleep(5)