from flask import Flask, render_template
import urllib.request, json

app = Flask(__name__)

@app.route("/")
def get_list_characters_page():
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("characters.html", characters = dict["results"])

@app.route("/profile/<id>")
def get_profile(id):
    url = "https://rickandmortyapi.com/api/character/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("profile.html", profile = dict)

@app.route("/lista")
def get_list_characters():
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    characters = response.read()
    dict = json.loads(characters)

    characters = []

    for character in dict["results"]:
        character = {
            "name": character["name"],
            "status": character["status"]
        }

        characters.append(character)
    
    return {"characters": characters}

@app.route("/episodes")  

def get_list_episodes_page():
    url = "https://rickandmortyapi.com/api/episode" 
    response = urllib.request.urlopen(url)  
    episodes = response.read()  
    dict = json.loads(episodes) 

    return render_template("episodes.html", episodes = dict["results"]) 


@app.route("/listepisodes")

def get_episodes():
    url = "https://rickandmortyapi.com/api/episode"
    response = urllib.request.urlopen(url) 
    episodes = response.read() 
    dict = json.loads(episodes) 
    episodes = [] 
    
    for episode in dict["results"]: 
        episode = {  
            "episode":episode["episode"],
            "name":episode["name"],
            "air_date":episode["air_date"],
            "id":episode["id"]
        }        
        episodes.append(episode) 

    return {"episodes":episodes} 


@app.route("/episode/<id>") 

def get_episode(id):
    url = f"https://rickandmortyapi.com/api/episode/{id}"
    response = urllib.request.urlopen(url) 
    data = response.read(); 
    episode_dict = json.loads(data)
    
    return render_template("episode.html", episode=episode_dict) 