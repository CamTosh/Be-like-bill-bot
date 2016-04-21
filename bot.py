import tweepy
import http.client


def download(mention):

    user = mention.user.screen_name
    conn = http.client.HTTPConnection("localhost")
    url = "/bill/billgen-API.php?default=1&name=" + user
    conn.request("GET", url)

    res = conn.getresponse()
    res.read()


def reply(api, mention):

    id = mention.id
    user = mention.user.screen_name

    img = "tmp/" + user + ".jpg"
    print(img)
    api.update_with_media(img, "Be like Bill, proudly, @" + user, id)


if __name__ == '__main__':

    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_secret = ''

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth)

    mentions = api.mentions_timeline(count=1)

    for mention in mentions:

        download(mention)
        reply(api, mention)
