
from wrappers import r
from wrappers import db
from wrappers import subreddit_limit
from datetime import datetime
from praw.models import MoreComments


temp_dict = {}

def comment_collect(sub):
    temp_dict[sub.id] = {}
    temp_dict[sub.id]['title'] = sub.title
    temp_dict[sub.id]['permalink'] = sub.permalink
    temp_dict[sub.id]['stickied'] = sub.stickied
    temp_dict[sub.id]['score'] = sub.score
    temp_dict[sub.id]['total_awards_received'] = sub.total_awards_received
    temp_dict[sub.id]['author'] = sub.author
    temp_dict[sub.id]['clicked'] = sub.clicked
    temp_dict[sub.id]['downs'] = sub.downs
    temp_dict[sub.id]['ups'] = sub.ups
    temp_dict[sub.id]['upvote_ratio'] = sub.upvote_ratio
    temp_dict[sub.id]['gilded'] = sub.gilded
    temp_dict[sub.id]['gildings'] = sub.gildings
    temp_dict[sub.id]['likes'] = sub.likes
    temp_dict[sub.id]['view_count'] = sub.view_count
    temp_dict[sub.id]['visited'] = sub.visited
    temp_dict[sub.id]['num_comments'] = sub.num_comments
    temp_dict[sub.id]['num_crossposts'] = sub.num_crossposts
    temp_dict[sub.id]['num_reports'] = sub.num_reports


    sub.comments.replace_more()
    for top_level_comment in sub.comments:
        temp_dict[sub.id][top_level_comment.id] = {}
        temp_dict[sub.id][top_level_comment.id]['body'] = top_level_comment.body
        temp_dict[sub.id][top_level_comment.id]['author'] = top_level_comment.author
        temp_dict[sub.id][top_level_comment.id]['controversiality'] = top_level_comment.controversiality
        temp_dict[sub.id][top_level_comment.id]['distinguished'] = top_level_comment.distinguished
        temp_dict[sub.id][top_level_comment.id]['downs'] = top_level_comment.downs
        temp_dict[sub.id][top_level_comment.id]['gilded'] = top_level_comment.gilded
        temp_dict[sub.id][top_level_comment.id]['gildings'] = top_level_comment.gildings
        temp_dict[sub.id][top_level_comment.id]['likes'] = top_level_comment.likes
        temp_dict[sub.id][top_level_comment.id]['score'] = top_level_comment.score
        temp_dict[sub.id][top_level_comment.id]['stickied'] = top_level_comment.stickied
        temp_dict[sub.id][top_level_comment.id]['total_awards_received'] = top_level_comment.total_awards_received
        temp_dict[sub.id][top_level_comment.id]['ups'] = top_level_comment.ups
        temp_dict[sub.id][top_level_comment.id]['replies'] = {}

        for x in top_level_comment.replies:
            if isinstance(x, MoreComments):
                continue
            temp_dict[sub.id][top_level_comment.id]['replies']['body'] = x.body          
            temp_dict[sub.id][top_level_comment.id]['replies']['author'] = x.author
            temp_dict[sub.id][top_level_comment.id]['replies']['controversiality'] = x.controversiality
            temp_dict[sub.id][top_level_comment.id]['replies']['distinguished'] = x.distinguished
            temp_dict[sub.id][top_level_comment.id]['replies']['downs'] = x.downs
            temp_dict[sub.id][top_level_comment.id]['replies']['gilded'] = x.gilded
            temp_dict[sub.id][top_level_comment.id]['replies']['gildings'] = x.gildings
            temp_dict[sub.id][top_level_comment.id]['replies']['likes'] = x.likes
            temp_dict[sub.id][top_level_comment.id]['replies']['score'] = x.score
            temp_dict[sub.id][top_level_comment.id]['replies']['stickied'] = x.stickied
            temp_dict[sub.id][top_level_comment.id]['replies']['total_awards_received'] = x.total_awards_received
            temp_dict[sub.id][top_level_comment.id]['replies']['ups'] = x.ups
            




if __name__ == '__main__':
    wsb_hot_submissions = r.subreddit("wallstreetbets").top(limit=1)


    for submission in wsb_hot_submissions:
        comment_collect(submission)





