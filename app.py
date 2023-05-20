from flask import Flask, render_template, url_for, send_file, request
import requests
import json
import os

app = Flask(__name__) 

def fetch_meme():
    url = "https://meme-api.com/gimme/programmerhumor"
    response = json.loads(requests.request("GET", url).text)
    meme_image = response['preview'][-1]
    subreddit = response['subreddit']
    download_url = response['url']
    post_link = response['postLink']
    ups = response['ups']
    return meme_image, subreddit, download_url, post_link, ups


@app.route('/', methods=['GET', 'POST'])
def index():
    meme_pic, subreddit, download_url, post_link, ups = fetch_meme()
    if request.method == 'POST':
        if request.form.get('action1') == 'Download':
            img_download = requests.get(download_url)
            with open(os.path.join(os.path.expanduser('~'),'Documents',f'{ups}_techmeme.png'), 'wb') as fp:
                fp.write(img_download.content)
        else:
            pass

    return render_template('index.html', meme_pic=meme_pic, subreddit=subreddit, download_url=download_url, post_link=post_link)
    

if __name__ == "__main__":
     app.run(host="0.0.0.0", port=80, debug=True)
