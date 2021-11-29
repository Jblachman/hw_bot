import praw
import random
import time
import datetime
from praw.reddit import Subreddit

# FIXME:
# copy your generate_comment function from the madlibs assignment here
madlibs = [
    "I appreciate the [PROGRESSIVE] leaders who [FIGHT] for our [FREEDOM] and [DEMOCRACY].  Keep on [BELIEVING]!"
    "At some point in time there were [HATERS] who labelled us [WEAK] and [INSIGNIFICANT].  I look around at all my [BROTHERS] and see that is not [TRUE]"
    "The [MINORITY] has become the [MAJORITY].  The [LAUGHED] at has become the [JOKER]. We know what is [ON THE HORIZON]."
    "So [RISE] up and [CALL] your [NEIGHBOR].  Reach out to you [LOVED] ones and rise to the [OCCASION]."
    "So why do we [CARE] about this? Why are we all [HERE] [TODAY]? To answer that [QUESTION] we must go back to our roots as [AMERICANS]. There was a time when we were [INFRINGED] upon and [DOMINATED] by men."
    "In this [ERA] we find ourselves in the [SAME] position.  [NEVER] again shall we [SETTLE] for the disrespect of [POLITICIANS]. Today is the first day of our pursuit of [FREEDOM]."
]

replacements = {
    'PROGRESSIVE': ['Democrats', 'Hilary Clinton', 'Bernie Sanders', 'Obama', 'Bloomberg'],
    'FIGHT': ['war', 'battle', 'struggle', 'effort', 'uptake'],
    'FREEDOM': ['democracy', 'right to believe', 'constitution', 'individualism'],
    'DEMOCRACY': ['america', 'progressiveness', 'republic', 'politics', 'free world'],
    'BELIEVING': ['optimism', 'trust', 'confidence', 'understanding', 'judgement'],
    'WEAK': ['can not bench', 'small', 'tiny', 'enemy', 'embarrassing'],
    'INSIGNIFICANT': ['weak', 'minor', 'lesser', 'small', 'ants'],
    'BROTHERS': ['siblings', 'by blood', 'fellows', 'amigos', 'friends'],
    'TRUE': ['right', 'accuriat', 'legitimate', 'natural', 'fact'],
    'HATERS': ['trump', 'republicans', 'fragile', 'jealous', 'Putin'],
    'MINORITY': ['lesser', 'rebublicans', 'small', 'insignificant', 'fearful'],
    'MAJORITY': ['bigger', 'democrats', 'huge', 'significant', 'feared'],
    'LAUGHED': ['made fun of', 'butt of jokes', 'anxiety', 'smirked', 'pushed over'],
    'JOKER': ['Movie', 'crazy', 'insane', 'mentally superier', 'confident'],
    'ON THE HORIZON': ['edge of tomorrow', 'mountains', 'the next up', 'superior' 'el proximp'],
    'RISE': ['stand up', 'extend', 'the sun', 'stretch', 'awake'],
    'CALL': ['hit the telly', 'send a message', 'facetime' 'whatsapp'],
    'NEIGHBOR': ['next door', 'acquintence', 'close to you', 'here and there', ],
    'LOVED': ['friend', 'care about', 'related', 'family'],
    'OCCASION': ['the day', 'holiday', 'celebratory', 'this evening'],
    'CARE': ['feel for', 'emotional about', 'close to home', 'passionate'],
    'HERE': ['present', 'in the moment', 'attendence', 'did not skip'],
    'TODAY': ['right now', 'momentary', 'state', 'as of now', 'not tomorrow'],
    'QUESTION': ['confused about', 'propose a statment', 'not sure of the answer', 'curious', 'ready to be enlightened'],
    'AMERICANS': ['not foreign', 'domestic', 'democrats' 'metling pot', 'citizens', 'best country on earth'],
    'INFRINGED': ['violated', 'inferior', 'stepped on', 'rejected'],
    'DOMINATED': ['overruled', 'made submissive', 'drowned out', 'not heard', 'lack of voice'],
    'ERA': ['history', 'century', 'time', 'scale', 'moment'],
    'SAME': ['identical', 'mirror', 'akin', 'literally exact', 'similar'],
    'NEVER': ['not in a million years', 'seriously no', 'will not happen', 'not again', 'not once'],
    'SETTLE': ['relax', 'lower standards', 'accept', 'roll over', 're-evaluate'],
    'POLITICIANS': ['soul-sucking demons', 'right wing', 'abusers of power', 'Donald', 'russia'],
    'FREEDOM': ['America', 'uncontrolled', 'not Russia', 'choice', 'not restrained']

}


def generate_comment():

    s = random.choice(madlibs)
    for k in replacements.keys():
        s = s.replace('['+ k +']', random.choice(replacements[k]))
    return(s)


reddit = praw.Reddit('bot1')


# select a "home" submission in the /r/BotTown subreddit to post to,
# and put the url below
submission_url = 'https://old.reddit.com/r/BotTown2/comments/r37esc/this_is_my_test_submission_for_bot1/?'
submission = reddit.submission(url=submission_url)

# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code,
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once

while True:

# printing the current time will help make the output messages more informative
# since things on reddit vary with time

    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)
    
# (task 0): get a list of all of the comments in the submission
# HINT: this requires using the .list() and the .replace_more() functions
  
    allcoments = []
    submission.comments.replace_more(limit=None)
    submission.comments.list
    all_comments = submission.comments.list()

# HINT:
# we need to make sure that our code is working correctly,
# and you should not move on from one task to the next until you are 100% sure that
# the previous task is working;
# in general, the way to check if a task is working is to print out information
# about the results of that task,
# and manually inspect that information to ensure it is correct;
# in this specific case, you should check the length of the all_comments variable,
# and manually ensure that the printed length is the same as the length displayed on reddit;
# if it's not, then there are some comments that you are not correctly identifying,
# and you need to figure out which comments those are and how to include them.
    
    print('Total Comments =', len(all_comments))

# FIXME (task 1): filter all_comments to remove comments that were generated by your bot
# HINT:
# use a for loop to loop over each comment in all_comments,
# and an if statement to check whether the comment is authored by you or not

    not_my_comments = []

    for comment in all_comments:
        if str(comment.author) != 'cs40-robot':
            not_my_comments.append(comment)

# HINT:
# checking if this code is working is a bit more complicated than in the previous tasks;
# reddit does not directly provide the number of comments in a submission
# that were not gerenated by your bot,
# but you can still check this number manually by subtracting the number
# of comments you know you've posted from the number above;
# you can use comments that you post manually while logged into your bot to know
# how many comments there should be.

    print('Total Comments that Are Not Mine=', len(not_my_comments))

# if the length of your all_comments and not_my_comments lists are the same,
# then that means you have not posted any comments in the current submission;
# (your bot may have posted comments in other submissions);
# your bot will behave differently depending on whether it's posted a comment or not

    has_not_commented = len(not_my_comments) == len(all_comments)

    print('has not commented = ', has_not_commented)

# FIXME (task 2)
# if you have not made any comment in the thread, then post a top level comment
#
# HINT:
# use the generate_comment() function to create the text,
# and the .reply() function to post it to reddit;
# a top level comment is created when you reply to a post instead of a message
    comments_without_replies = []

    if has_not_commented:
        text = generate_comment()
        submission.reply(text)


# FIXME (task 3): filter the not_my_comments list to also remove comments that
# you've already replied to
# HINT:
# there are many ways to accomplish this, but my solution uses two nested for loops
# the outer for loop loops over not_my_comments,
# and the inner for loop loops over all the replies of the current comment from the outer loop,
# and then an if statement checks whether the comment is authored by you or not
    
    else:
        for comment in not_my_comments:
            for reply in comment.replies:
                if str(reply.author) != 'cs40-robot':
                    comments_without_replies.append(comment)
                else:   
                    continue
                try:
                    comment.reply(generate_comment())
                except praw.exceptions.RedditAPIException:
                    pass


# HINT:
# this is the most difficult of the tasks,
# and so you will have to be careful to check that this code is in fact working correctly

        print('len(comments_without_replies)=', len(comments_without_replies))

# FIXME (task 4): randomly select a comment from the comments_without_replies list,
# and reply to that comment

    text = generate_comment()
    
    try:
        comment = random.choice(comments_without_replies)
        comment.reply(text)
    except IndexError:
        pass
    except praw.exceptions.APIException:
        print('This comment was previously deleted')

# HINT:
# use the generate_comment() function to create the text,
# and the .reply() function to post it to reddit;
# these will not be top-level comments;
# so they will not be replies to a post but replies to a message
# FIXME (task 5): select a new submission for the next iteration;
# your newly selected submission should be randomly selected from the 5 hottest submissions
# submission_list=[]

    submission = random.choice(list(reddit.subreddit("BotTown2").hot(limit=5)))
    print('Submission Title=', submission.title)

# This doesn't avoid rate limiting
# (since we're not sleeping for a long period of time),
# but it does make the program's output more readable.

    time.sleep(5)