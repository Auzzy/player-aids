import json
import pathlib

from boardgamegeek import BGGClient

from app.app import app

GAMES_ROOT = pathlib.Path.cwd() / pathlib.Path("app", "aids")
GAMES_INFO_FILEPATH = GAMES_ROOT / "games.json"

BGG = BGGClient()

@app.route("/greeting")
def greeting():
    return {"greeting": "Hello from Flask!"}

@app.route("/games")
def game_list():
    with open(GAMES_INFO_FILEPATH) as games_info_file:
        games_info = json.load(games_info_file)

    game_listings = {}
    for info in games_info["games"]:
        bgg_game_info = BGG.game(game_id=info["bggId"])
        game_listings[info["name"]] = {
            "id": info["bggId"],
            "name": info["name"],
            "image": bgg_game_info.image,
            "year": bgg_game_info.yearpublished,
            "designers": bgg_game_info.designers
        }

    return {"games": game_listings}

@app.route("/games/<game>/info")
def game_info(game):
    return {
        "name": game
    }

@app.route("/games/<game>/")
@app.route("/games/<game>/aid")
def game_aid(game):
    return {}