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
