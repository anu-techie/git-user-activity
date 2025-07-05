import sys, requests

def user(username):
    try:
        response = requests.get(f"https://api.github.com/users/{username}/events")
        if response.status_code == 200:
            user_activity = response.json()
            if not user_activity:
                print("There are no activity in the repository")
            else:
                has_activity = False
                for activity in user_activity:
                    if activity['type'] == "PushEvent":
                        com = activity['payload']['commits']
                        repository_name = activity["repo"]["name"]
                        print(f"Pushed {len(com)} commits to {repository_name}")
                        has_activity = True
                    elif activity["type"] == "CreateEvent":
                        repository_name = activity["repo"]["name"]
                        print(f"Created new repository - {repository_name}")
                        has_activity = True
                if not has_activity:
                    print("There are no push and create activity in the repository")
                
        elif response.status_code == 404:
            print("Invalid User Name")
        elif response.status_code in [403,429]:
            print("Rate Limit Exceeded")
        else:
            print("Unexpected Response : Please try again later")
    except requests.exceptions.RequestException as e:
        print(f"Connection Error {e}")
        
def main():
    input = sys.argv
    if len(input) == 2:
        user(input[1])
    else:
        print("Please give username followed by filename \n\n 'example : github_user.py anu-techie'\n")

main()