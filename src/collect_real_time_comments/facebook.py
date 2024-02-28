import facebook

# Set up the Facebook Graph API client
graph = facebook.GraphAPI(access_token='YOUR_ACCESS_TOKEN', version='v13.0')

# Retrieve comments from a post
comments = graph.get_connections(id='POST_ID', connection_name='comments')
