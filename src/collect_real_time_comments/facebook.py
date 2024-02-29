import os
import sys
sys.path.append('../../')
from config import fb_config
def get_fb_comments():
  max_comments = 5000
  limit = 25
  id = os.environ.get('FB_USER_ID')
  graph = fb_config()
  posts = graph.get_connections(id=id, connection_name='posts', limit=limit)
  all_comments = []
  for post in posts['data']:
    offset = 0
    for itr in range(16):
      offset = itr * limit
      comments = graph.get_connections(id=post['id'], connection_name='comments', limit=limit, offset=offset)
      all_comments.extend(comments["data"])
    if(len(all_comments) >= max_comments):
      break
  comment_messages = [comment["message"] for comment in all_comments]
  return comment_messages
