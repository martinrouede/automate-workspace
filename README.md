# automate-workspace

A simple script to facilitate the setup and running your projects.

This script open a gnome terminal and a VS code window from the folder you configure, and runs some commands you want to run as well,

like a React App with `npm run start`.

## Usage

First you need to create a file named **commands.json** and the content like that:
```
[
    {
        "path": "absolute path of your repo 1",
        "scripts": [
            "first script you want to run in repo 1",
            "second script you want to run if you need in repo 1"
        ]
    },
    {
        "path": "absolute path of your repo 2",
        "scripts": [
            "first script you want to run in repo 2"
        ]
    }
]
```
And now for run the script you need to pass for parameter the command index that you want to run

`python3 automate-workspace/workspace.py 0`
