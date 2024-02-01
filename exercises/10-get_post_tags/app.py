import requests

def get_post_tags(post_id):
    url = f"https://assets.breatheco.de/apis/fake/sample/posts.php"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json().get("posts", [])

        for post in posts:
            if post["id"] == post_id:
                return post.get("tags", [])

    return [] 

# Example of using the function
post_id = 234
tags = get_post_tags(post_id)
print(tags)
