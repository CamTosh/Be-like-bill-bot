import tweepy
import http.client


def download(mention):
    # Call api with Twitter name to create image

    user = mention.user.screen_name
    conn = http.client.HTTPConnection("localhost")
    url = "/bill/billgen-API.php?default=1&name=" + user
    conn.request("GET", url)

    res = conn.getresponse()
    res.read()


def reply(api, mention):
    # Reply to the tweet who mention the bot with image saved in tmp/<username>.jpg

    id = mention.id
    user = mention.user.screen_name

    img = "tmp/" + user + ".jpg"
    print(img)
    # For documentation view Twitter API's documentation
    api.update_with_media(img, "Be like Bill, proudly, @" + user, id)


if __name__ == '__main__':
    # You can add your Twitter Secret Application keys here. Go to https://dev.twitter.com

    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_secret = ''

    # Use Oauth to connect application
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth)

    # Get the last mention
    mentions = api.mentions_timeline(count=1)

    for mention in mentions:

        download(mention)
        reply(api, mention)
