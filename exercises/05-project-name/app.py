import requests

url = "https://assets.breatheco.de/apis/fake/sample/project1.php"  
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    project_name = data.get("name", "Project Name Not Found") 
    print("Project Name:", project_name)
