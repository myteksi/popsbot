import etcd
import json
import re
import slackbot_settings as ss
import traceback

client = etcd.Client(host=ss.ETCDHOST, port=ss.ETCDPORT,
                     username=ss.ETCDUSER, password=ss.ETCDPASSWD, protocol=ss.ETCDPROTOCOL)

mapping = {}
matches = {}

kbname = '/{}/popsbot-kb'.format(ss.ETCDUSER)


def init():
    global mapping
    global matches
    global kbname
    errored_key = ''
    try:
        f = client.read(kbname).value
        if len(f) == 0:
            return

        mapping = json.loads(f)
        for k, v in mapping.iteritems():
            value = [v, [], None]
            matches[k] = value
            try:
                value[1] = k.split('.*')
                value[2] = re.compile('.*' + k + '.*', re.IGNORECASE)
            except:
                print 'canot compile {} as regex'.format(k)
    except Exception as e:
        print errored_key
        traceback.print_exc()
        print 'error while loading kb from etcd: {}'.format(e)
        return


def clear(k):
    global mapping
    global matches
    global kbname
    mapping.pop(k, None)
    matches.pop(k, None)
    try:
        client.write(kbname, json.dumps(mapping))
    except Exception as e:
        print 'error while saving kb to etcd: {}'.format(e)


def update(k, v):
    global mapping
    global matches
    global kbname
    mapping[k] = v
    value = [v, [], None]
    matches[k] = value
    try:
        value[1] = k.split('.*')
        value[2] = re.compile('.*' + k + '.*', re.IGNORECASE)
    except:
        print 'cannot compile {} as regex'.format(k)
    try:
        client.write(kbname, json.dumps(mapping))
    except Exception as e:
        print 'error while saving kb to etcd: {}'.format(e)
