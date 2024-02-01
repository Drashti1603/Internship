import requests

def get_attachment_by_id(attachment_id):
    url = "https://assets.breatheco.de/apis/fake/sample/posts.php"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json().get("posts", [])

        for post in posts:
            attachments = post.get("attachments", [])
            for attachment in attachments:
                if attachment.get("id") == attachment_id:
                    return attachment.get("title")

    return None  

title = get_attachment_by_id(22)

if title is not None:
    print("Title:", title)
