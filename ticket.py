import requests
import json



# Jira API endpoint for creating issues
url = "https://alihasan312.atlassian.net/rest/api/3/issue"

# Request headers
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

def gen_ticket(data):
    payload = {
        "fields": {
            "project": {
                "key": "SCRUM" 
            },
            "summary": data["Title"],
            "description": {
                "type": "doc",
                "version": 1,
                "content": [
                    {
                        "type": "paragraph",
                        "content": [
                            {
                                "type": "text",
                                "text": data["Summary"]
                            }
                        ]
                    }
                ]
            },
            "issuetype": {
                "name": "Task"
            }
        }
    }


   
    auth = (
        "YOUR_EMAIL",
        "YOUR_ATLASSIAN_API_KEY"
    )

    response = requests.post(
        url,
        headers=headers,
        json=payload, 
        auth=auth
    )

    try:
        return response.json()
    except Exception:
        return {
            "error": "Failed to parse response",
            "response_text": response.text,
            "status_code": response.status_code
        }
