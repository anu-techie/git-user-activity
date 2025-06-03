import sys
import requests

def fetch_user(username):
    url = f'https://api.github.com/users/{username}/events'
    response = requests.get(url)

    if response.status_code !=200:
        print(f'Error fetching data for user {username}.Status code : {response.status_code}')
        return None
    
    return response.json()

def display_events(user_info):
    if not user_info:
        print('No recent activity found')
        return
    
    for event in user_info:
        event_type = event.get('type', 'UnknownEvent')
        repo = event.get('repo',{}).get('name', 'UnknownRepository')
        
        if event_type == 'PushEvent':
            pushed_events = event.get('payload',{}).get('commits',[])
            commits = len(pushed_events)
            print(f'Pushed {commits} commits to {repo}')
        elif event_type == "IssuesEvent":
            action = event.get("payload", {}).get("action", "did something")
            print(f"- {action.capitalize()} an issue in {repo}")
        
        elif event_type == "WatchEvent":
            print(f"- Starred {repo}")
        
        else:
            print(f"- {event_type} at {repo}")

def main():
    if len(sys.argv)!=2:
        print('usage : command github_activity.py <username>')
        return
    
    username = sys.argv[1]
    user_info = fetch_user(username)
    if user_info is not None:
        display_events(user_info)

if __name__=="__main__":
    main()

