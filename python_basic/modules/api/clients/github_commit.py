import requests

class GitHubCommit():

    def get_list_commits(self, owner, repo):
        r = requests.get(f"https://api.github.com/repos/{owner}/{repo}/commits")
        body = r.json()
        #print(body)
        return body

    def get_commit(self,owner, repo, sha):
        r = requests.get(f"https://api.github.com/repos/{owner}/{repo}/commits/{sha}")
        body = r.json()
        #print(body)
        return body
    

    def get_commit_status(self,owner, repo,sha):
        r = requests.get(f"https://api.github.com/repos/{owner}/{repo}/commits/{sha}/status")
        body = r.json()

        return body

    def get_list_commit_coments_repo(self,owner, repo):
        r = requests.get(f" https://api.github.com/repos/{owner}/{repo}/comments")
        body = r.json()
        #print(body)

        return body
    
    def get_commit_coment(self,owner, repo,comment_id):
        r = requests.get(f"https://api.github.com/repos/{owner}/{repo}/comments/{comment_id}")
        body = r.json()
        #print(body)

        return body