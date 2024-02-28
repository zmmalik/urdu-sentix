import instaloader

# Create an instance of Instaloader
loader = instaloader.Instaloader()

# Login (optional)
# loader.login("your_username", "your_password")

# Retrieve comments from a specific post
post_url = 'https://www.instagram.com/p/POST_SHORTCODE/'
post = instaloader.Post.from_shortcode(loader.context, POST_SHORTCODE)

comments = []
for comment in post.get_comments():
    comments.append(comment.text)

# Print or process the comments as needed
for comment in comments:
    print(comment)
