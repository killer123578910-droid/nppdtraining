import requests,os
from dotenv import load_dotenv
from predict import predicting 

load_dotenv()
api=os.getenv("API_key")
def search_g(name):
    #search ten nearest ids
    params={
        "key":api,
        "search":name,
        "search_precise":True,
        "page_size":10
    }
    games=requests.get("https://api.rawg.io/api/games",params=params).json()["results"]
    names=[]
    trans={}
    for game in games:
        names.append(game["name"])
        trans[game["name"]]=game["id"]
    return names,trans
def detail(id):
    # Rawg Platform Name (lower-case) -> Dataset Console Code
    RAWG_CONSOLE_MAP = {
        # --- PlayStation Family ---
        "playstation 5": "PS4",  # Generational Mapping (PS5 -> PS4)
        "playstation 4": "PS4",
        "playstation 3": "PS3",
        "playstation 2": "PS2",
        "playstation": "PS",
        "ps vita": "PSV",
        "psp": "PSP",
        # --- Xbox Family ---
        "xbox series x": "XOne",  # Generational Mapping (XSX -> XOne)
        "xbox series s/x": "XOne",
        "xbox one": "XOne",
        "xbox 360": "X360",
        "xbox": "XB",
        # --- Nintendo Family ---
        "nintendo switch": "NS",
        "nintendo 3ds": "3DS",
        "nintendo ds": "DS",
        "nintendo dsi": "DS",
        "wii u": "WiiU",
        "wii": "Wii",
        "gamecube": "GC",
        "nintendo 64": "N64",
        "snes": "SNES",
        "nes": "NES",
        "game boy advance": "GBA",
        "game boy color": "GBC",
        "game boy": "GB",
        # --- PC & Mobile ---
        "pc": "PC",
        "macintosh": "OSX",
        "macos": "OSX",
        "linux": "PC",  # Quy về PC
        "ios": "Mob",
        "android": "Mob",
        # --- Sega Family ---
        "sega genesis": "GEN",
        "sega saturn": "SAT",
        "sega dreamcast": "DC",
        "sega cd": "SCD",
        "sega game gear": "GG",
        "sega master system": "GEN",
        # --- Retro / Niche Consoles ---
        "atari 2600": "2600",
        "neo geo": "NG",
        "3do": "3DO",
        "wonderswan": "WS",
    }
    params={
        "key":api,
    }
    det=requests.get(f"https://api.rawg.io/api/games/{id}",params=params).json()
    name=det["name"]
    dev=(det["developers"][0]["name"]).strip()
    cons=det["platforms"][0]["platform"]["name"]
    cons=RAWG_CONSOLE_MAP[cons.lower().strip()]
    genr=det["genres"][0]["name"]
    critics=(det["metacritic"])/10
    release=det["released"][:4]
    description=det["description_raw"]
    print(f"{name}\n{dev}\n{cons}\n{genr}\n{release}\n{critics}\n{description}")
    predicting(dev,cons,genr,critics,release)
    #print(det)

if __name__=="__main__":
    detail("3498")

