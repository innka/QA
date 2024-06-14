import requests

class GitHubEmoji():
    
    def get_emogi(self):
        r = requests.get("https://api.github.com/emojis")
        if r.status_code == 200:
            body = r.json()
        else:
            r.raise_for_status()
        #print(body)
        return body