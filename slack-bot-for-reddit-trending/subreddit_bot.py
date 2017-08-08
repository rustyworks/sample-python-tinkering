import os
import time
import urllib.request

from urllib.error import URLError

from bs4 import BeautifulSoup
from slackclient import SlackClient


BOT_NAME = 'subreddit'
# https://api.slack.com/apps/<code app>/oauth?success=1
SLACK_BOT_TOKEN = os.environ.get('SLACK_BOT_TOKEN')
# https://api.slack.com/methods/channels.list/test
CHANNEL_ID = os.environ.get('CHANNEL_ID')
SLACK_BOT_ID = os.environ.get('SLACK_BOT_ID')
AT_BOT = '<@{slack_bot_id}>'.format(slack_bot_id=SLACK_BOT_ID)

slack_client = SlackClient(SLACK_BOT_TOKEN)


def parse_slack_output(slack_rtm_output):
    output_list = slack_rtm_output
    if output_list:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                return output['text'].split(AT_BOT)[1].strip().lower(), output['channel']
    return (None, None)

def handle_command(command, channel):
    response = 'Silakan masukkan subreddit yang ingin dicek (saat ini hanya limited ke Python, machinelearning, datascience, nosleep, dan TwoSentenceHorror)'

    if command in ['python', 'machinelearning', 'datascience', 'nosleep', 'twosentencehorror']:
        response = 'Top 5\n'
        top_5 = parse_subreddit(command)
        for top in top_5:
            response += top[0] + '\n'
            response += top[1] + '\n\n'
    slack_client.api_call('chat.postMessage', channel=channel, text=response, as_user=True)

def parse_subreddit(subreddit):
    url = 'https://www.reddit.com/r/{subreddit}/top'.format(subreddit=subreddit)
    result = []
    try:
        response = urllib.request.urlopen(url).read()
        html = response.decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        all_threads = soup.findAll(class_='thing')
        for i in range(5):
            thread = all_threads[i].find('a')
            title = thread.text
            link = thread.attrs['href']
            if not 'http' in link:
                link = 'https://www.reddit.com' + link
            result.append([title, link])
    except URLError:
        print('Connection Error')

    return result


if __name__ == '__main__':
    # source learning: http://whiterabot.com/create_slack_bot/
    READ_WEBSOCKET_DELAY= 1

    if slack_client.rtm_connect():
        print('Bot connected and running')

        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())

            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print('Connection error or bot authentication failed')
