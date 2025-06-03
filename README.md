# GitHub User Activity CLI

A simple command-line tool that fetches and displays a GitHub user's recent public activity using the GitHub API.

---

## Requirements
- Python 3.x
- `requests`library for handling HTTP requests and APIs

---

## Features

- Fetch public GitHub events from the GitHub API  
- Display event type, repository name, and time of the event  
- Error Handling - Handles the following:
    - Invalid or missing usernames
    - Network/API failures
    - Empty or malformed responses  

---

## What You'll Learn
- How to work with the GitHub API
- How to parse JSON responses in Python
- How to build a simple and clean CLI interface
- How to handle errors and invalid inputs gracefully

---

## Installation

Follow these steps to get your GitHub User Activity CLI app and running:

1. **Download or clone the repository**

   - To download - as a ZIP, click the **Code** button and select **Download ZIP**.  
   - Or clone via Git (if you have Git installed):  
     ```bash
     git clone https://github.com/anu-techie/git-user-activity.git
     ```

2. **Navigate to the project directory**

   ```bash
   cd git-user-activity
   ```
3. **Ensure you have Python 3 & installed**

    ```bash
   python --version
   ```
   If Python is not installed, download it from python.org.

4. **Install required packagee**
   
    If you don’t have requests installed, run:
   
   ```bash
   pip install requests
    ```
   or download it from [https://pypi.org/project/requests/] (https://pypi.org/project/requests/)

4. **Run the Task Tracker CLI**
    ```bash
    python github_activity.py <username>
    ```
---

## Acknowledgments

This project was inspired by and developed following the excellent guidance from [roadmap.sh](https://roadmap.sh). Special thanks to their clear tutorials and project ideas.

---

## Project URL

For detailed project guidelines and ideas, visit:
[https://roadmap.sh/projects/github-user-activity](https://roadmap.sh/projects/github-user-activity)

---
🙋‍♀️ Author : Anusuyadevi | Learning Python and APIs by building cool projects ❤️
