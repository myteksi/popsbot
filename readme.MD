# PopsBot

Install Requirements:

```
pip install -r r.txt
```

open slackbot_settings.py

```
import os

API_TOKEN = os.environ.get('SLACKBOT_API_TOKEN', '')
PLUGINS = [
    'logics'
]
ETCDHOST = os.environ.get('SLACKBOT_ETCDHOST', '')
ETCDUSER = os.environ.get('SLACKBOT_ETCDUSER', '')
ETCDPASSWD = os.environ.get('SLACKBOT_ETCDPASSWD', '')
ETCDPORT = int(os.environ.get('SLACKBOT_ETCDPORT', 0))
ETCDPROTOCOL = os.environ.get('SLACKBOT_ETCDPROTOCOL', '')
```

Let's look at them 1 by 1

- list plugins to include.

```
PLUGINS = [
    'logics'
]
```

- specify slack api token (this is the token you need to connect the bot user to slack)

```
API_TOKEN = os.environ.get('SLACKBOT_API_TOKEN', '')
```

list of @cd configurations:

```
ETCDHOST = os.environ.get('SLACKBOT_ETCDHOST', '')
ETCDUSER = os.environ.get('SLACKBOT_ETCDUSER', '')
ETCDPASSWD = os.environ.get('SLACKBOT_ETCDPASSWD', '')
ETCDPORT = int(os.environ.get('SLACKBOT_ETCDPORT', 0))
ETCDPROTOCOL = os.environ.get('SLACKBOT_ETCDPROTOCOL', '')
```

once you have all these, you are set to run:

```
python run.py
```

The bot will:

1. connect to @cd and retrieve initial knowledge base
2. connect to slack. The bot user will **light up** (appear online) when this is successful.