import instaloader
import os

def insta_config():
    max_comments = 5000
    id = os.environ.get('INSTA_USER_ID')
    loader = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(loader.context, id)
    all_comments = []
    for item in profile.get_posts():
        post = instaloader.Post.from_shortcode(loader.context, item.mediaid)
        comments = post.get_comments()
        all_comments.extend(comments)
        if(len(all_comments) >= max_comments):
            break
    comment_messages = [comment["text"] for comment in all_comments]
    return comment_messages