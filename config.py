import facebook
import os

def fb_config():
  access_token = os.environ.get('FB_ACCESS_TOKEN')
  version = os.environ.get('FB_API_VERSION')
  graph = facebook.GraphAPI(access_token=access_token, version=version)
  return graph