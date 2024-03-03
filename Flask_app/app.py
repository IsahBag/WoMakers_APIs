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
    all_episodes = [] 

    for page in range(1, 4):  
        url = f"https://rickandmortyapi.com/api/episode?page={page}" 
        response = urllib.request.urlopen(url) 
        episodes = response.read() 
        dict = json.loads(episodes) 
        all_episodes.extend(dict["results"])    

    return render_template("episodes.html", episodes=all_episodes)


@app.route("/episode/<id>")
def get_profile_episode(id):
    url = f"https://rickandmortyapi.com/api/episode/{id}"
    response = urllib.request.urlopen(url) 
    data = response.read() 
    episode_data = json.loads(data)    

    characters = []
    for character_url in episode_data["characters"]:
        response = urllib.request.urlopen(character_url)
        character_data = json.loads(response.read())
        characters.append({
            "id": character_data["id"],
            "name": character_data["name"]
        })
    
    return render_template("episode.html", episode=episode_data, characters=characters)