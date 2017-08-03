from slackbot.bot import default_reply, respond_to, listen_to
import kbase
from kbase import matches
from kbase import mapping
import re
import shlex
import json


@respond_to('who.*wrote.*you', re.IGNORECASE)
@respond_to('who.*program.*you', re.IGNORECASE)
@respond_to('author', re.IGNORECASE)
def author(message):
    message.reply('A Mystical Man')


@respond_to('^hello$', re.IGNORECASE)
def hello(message):
    message.reply('good day to you!')


def prepare(item):
    result = item
    for pattern in [('<http', 1), ('<mailto:', 8)]:
        index1 = result.find(pattern[0])
        if index1 != -1:
            index2 = result.find('>', index1)
            if index2 != -1:
                result = result[:index1] + result[index1 +
                                                  pattern[1]: index2] + result[index2 + 1:]
    return result


def auth(message):
    chang = message._client.find_user_by_name('chang')
    jiann = message._client.find_user_by_name('jiannyeu.yong')
    chinyin = message._client.find_user_by_name('chinyin.ong')
    michael = message._client.find_user_by_name('michael.wright')
    lyesam = message._client.find_user_by_name('lyesam.tho')
    joseph = message._client.find_user_by_name('joseph.sundram')
    admins = [chang, jiann, chinyin, michael, lyesam, joseph]
    userid = message._get_user_id()
    return userid in admins


@respond_to('^list$')
def list(message):
    if not auth(message):
        message.reply(
            'sorry but I cannot let you do this. please contact jiannyeu.yong or chang.')
        return
    message.reply('```' + json.dumps(mapping, indent=4) + '```')


@respond_to('^train (.*)$')
def train(message, thing):
    if not auth(message):
        message.reply(
            'sorry but I cannot let you do this. please contact jiannyeu.yong or chang.')
        return
    try:
        things = shlex.split(thing)
        if len(things) != 2:
            message.reply('hey, I am confused.')
            return
        things[1] = prepare(things[1])
        kbase.update(things[0], things[1])
        message.reply('ok, got it. answer to {} will be {}'.format(
            things[0], things[1]))
    except Exception as e:
        message.reply('I am utterly confused: {}'.format(e))


@respond_to('^clear(.*)$')
def clear(message, thing):
    if not auth(message):
        message.reply(
            'sorry but I cannot let you do this. please contact jiannyeu.yong or chang.')
        return
    try:
        things = shlex.split(thing)
        if len(things) != 1:
            message.reply('hey, I am confused.')
            return
        kbase.clear(things[0])
        message.reply('ok, key {} removed'.format(things[0]))
    except Exception as e:
        message.reply('Something wrong : {}'.format(e))


@listen_to('anyone.*help', re.IGNORECASE)
def help(message):
    message.reply(
        'I ll try my best to help you, please talk to me')


@default_reply
def handle_all(message):
    msg = message._body.get('text', None)
    for k, v in matches.iteritems():
        if k.match(msg):
            message.reply(v)
            return
    message.reply('not sure how I can help you with that')
