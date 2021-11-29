import praw
import prawcore
import random
import time
import datetime
from textblob import TextBlob
from praw.reddit import Subreddit

reddit = praw.Reddit('bot1')

url = 'https://old.reddit.com/r/BotTown2/comments/r37esc/this_is_my_test_submission_for_bot1/?'
submission = reddit.submission(url=url)
subreddit = reddit.subreddit('BotTown2')

upvotes = 0
downvotes = 0
subup = 0
subdown = 0

words = ['democracy','freedom']

while True:

    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)

    blob = TextBlob(str(submission.selftext))
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    for word in words:   
        if word in submission.title.lower() and polarity > 0.5:
            submission.upvote()
            print('upvote')
            subup += 1
            break
        
        if word in submission.title.lower() and subjectivity > 0:
            submission.upvote()
            print('upvote')
            subup += 1
            break

        if word in submission.title.lower() and polarity < 0.5:
            submission.downvote()
            print('downvote')
            subdown += 1
            break

        if word in submission.title.lower() and subjectivity < 0:
            submission.downvote()
            print('downvote')
            subdown += 1
            break

        if 'republican' in submission.title.lower():
            submission.downvote()
            print('downvote')
            subdown += 1
            break

        if 'putin' in submission.title.lower():
            submission.downvote()
            print('downvote')
            subdown += 1
            break
        
        else:
            print('Words not found')

    submission.comments.replace_more(limit=None)
    all_comments = submission.comments.list()
    not_my_comments = []

    for comment in all_comments:
        if str(comment.author) != 'cs40-robot':
            not_my_comments.append(comment)

    for comment in not_my_comments:

        blob = TextBlob(str(comment.body))
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity

        for word in words:

            if word in comment.body.lower() and polarity > 0.5:
                comment.upvote()
                comment.refresh
                print('upvote')
                upvotes += 1
                break

            if word in comment.body.lower() and subjectivity > 0:
                comment.upvote()
                comment.refresh
                print('upvote')
                upvotes += 1
                break
            
            if word in comment.body.lower() and polarity < 0.5:
                comment.downvote()
                comment.refresh()
                print('downvote')
                downvotes += 1
                break

            if word in comment.body.lower() and subjectivity < 0:
                comment.downvote()
                comment.refresh()
                print('downvote')
                downvotes += 1
                break

            if 'republican' in comment.body.lower():
                comment.downvote()
                print('downvote')
                downvotes += 1
                break
            
            else:
                print('Words not found')
    
    print()
    print('Comment upvotes =', upvotes)
    print('Comment downvotes =', downvotes)
    print('Submission upvotes =' , subup)
    print('Submission downvotes' , subdown)
    print()

    hotsubmissions = []
    for entry in reddit.subreddit('BotTown2').top(limit=300):
        hotsubmissions.append(entry)
    submission = random.choice(hotsubmissions)

    print('Next Submission Title =', submission.title)
    print()
    print('taking a breath before the next iteration...')
    time.sleep(10)

