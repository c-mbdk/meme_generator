# meme_generator

## About this project
This project interacts with a JSON API that scrapes a random meme from Reddit, specifically from the subreddit r/ProgrammerHumor. The app can be run locally. 

Underneath each meme, the URL of the Reddit post and the image are displayed - both are clickable links. You can download the meme to your Documents folder, but you can choose the selected download location by updating the app.py file. 

## How to Run

1. Install virtualenv:
```
$ pip install virtualenv
```

2. Open a terminal in the project root directory and run:
```
$ virtualenv env
```

3. Then run the command:
```
$ .\env\Scripts\activate
```

4. Then install the dependencies:
```
$ (env) pip install -r requirements.txt
```

5. Finally, start the web server:
```
$ (env) python app.py
```

6. This server will start on port 80. You can change this by updating the following line in app.py to this:
```
if __name__ == "__main__":
    app.run(debug=True, port=<desired port>)
```

