import requests,os
from dotenv import load_dotenv
from predict import predicting 

load_dotenv()
api=os.getenv("API_key")
def search_g(name):
    RAWG_CONSOLE_MAP = {
        # --- PlayStation Family ---
        "playstation 5": "PS4",  # Generational Mapping (PS5 -> PS4)
        "playstation 4": "PS4",
        "playstation 3": "PS3",
        "playstation 2": "PS2",
        "playstation": "PS",
        "ps vita": "PSV",
        "psp": "PSP",
        "pc":"PC",
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

    #search ten nearest ids
    params={
        "key":api,
        "search":name,
        "search_precise":True,
        "page_size":10
    }
    games=requests.get("https://api.rawg.io/api/games",params=params).json()["results"]
    #idx=["id","name","platform","genre","developer","background_image"]
    ans=[]
    for game in games:
        trans={}
        trans["id"]=game["id"]
        trans["name"]=game["name"].strip()
        trans["platform"]=RAWG_CONSOLE_MAP[(game["platforms"][0]["platform"]["name"]).lower().strip()] if (game["platforms"][0]["platform"]["name"]).lower().strip() in RAWG_CONSOLE_MAP else "Nan" 
        trans["image"]=game["background_image"]
        
        trans["genre"] = game["genres"][0]["name"] if game.get("genres") else "Unknown"
        
        #trans["developer"] = game["developers"][0]["name"].strip() if game.get("developers") else "Unknown"
        
        #trans["description"] = game.get("description_raw", "No description available")
        
        trans["metacritic"] = game.get("metacritic", 0)
        
        trans["sales"] = round(game.get("rating", 0), 1)
        
        ans.append(trans)
    return ans
    
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
        "pc":"PC",
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
    return {   
            "name":det["name"],
            "developer":(det["developers"][0]["name"]).strip(),
            "platform":RAWG_CONSOLE_MAP[(det["platforms"][0]["platform"]["name"]).lower().strip()] if (det["platforms"][0]["platform"]["name"]).lower().strip() in RAWG_CONSOLE_MAP else "Nan",
            "image":det["background_image"],
            "genre":det["genres"][0]["name"],
            "critics":(det["metacritic"]),
            "release":det["released"][:4],
            "description":det["description_raw"],
            }
if __name__=="__main__":
    detail("3498")
