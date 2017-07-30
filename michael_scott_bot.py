import praw
import os
from match_comment import get_quote


def authenticate():
    print("Authenticating...")
    reddit = praw.Reddit(
        "michaelscottbot",
        user_agent="nasotrang's Michael Scott Test v0.1")
    print("Authenticated as {}".format(reddit.user.me()))
    return reddit


def main():
    reddit = authenticate()
    idlist = get_saved_comments()
    while True:
        bot_run(reddit, idlist)


def bot_run(reddit, idlist):
    print("Scanning comments...")
    for comment in reddit.subreddit('test').comments(limit=1000):
        if comment.id not in idlist and comment.author != reddit.user.me():
            quote = get_quote(comment.body)
            if quote == None:
                return
            print("Found!")
            rep = ">" + quote
            rep += "\n\n\n - Michael Scott"
            comment.reply(rep)
            print("Repplied to comment: " + comment.id)
            idlist.append(comment.id)
            with open("idlist.txt", "a") as f:
                f.write(comment.id + "\n")


def get_saved_comments():
    if not os.path.isfile("idlist.txt"):
        idlist = []
    else:
        with open("idlist.txt", "r") as f:
            idlist = f.read()
            idlist = idlist.split("\n")
            idlist = list(filter(None, idlist))
    return idlist


if __name__ == "__main__":
    main()