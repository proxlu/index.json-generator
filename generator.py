import os
import json
from datetime import datetime

def load_existing_index(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {
        "cache": {
            "backdrop": {"_dirname": "Backdrop", "backdrop": "backdrop.png"},
            "battle": {"_dirname": "Battle"},
            "battle2": {"_dirname": "Battle2"},
            "battlecharset": {"_dirname": "BattleCharSet"},
            "battleweapon": {"_dirname": "BattleWeapon"},
            "charset": {"_dirname": "CharSet", "char": "char.png"},
            "chipset": {"_dirname": "ChipSet", "templatetileset": "templatetileset.png"},
            "faceset": {"_dirname": "FaceSet", "faceset": "faceset.png"},
            "frame": {"_dirname": "Frame"},
            "gameover": {"_dirname": "GameOver"},
            "map0001.lmu": "Map0001.lmu",
            "monster": {"_dirname": "Monster", "monster": "monster.png"},
            "music": {"_dirname": "Music"},
            "panorama": {"_dirname": "Panorama"},
            "picture": {"_dirname": "Picture"},
            "rpg_rt.ini": "RPG_RT.ini",
            "rpg_rt.ldb": "RPG_RT.ldb",
            "rpg_rt.lmt": "RPG_RT.lmt",
            "sound": {"_dirname": "Sound"},
            "system": {"_dirname": "System", "system": "System.png"},
            "system2": {"_dirname": "System2"},
            "title": {"_dirname": "Title"}
        },
        "metadata": {"date": datetime.now().strftime("%Y-%m-%d"), "version": 2}
    }

def generate_index():
    base_dir = os.getcwd()
    index_file = os.path.join(base_dir, "index.json")
    script_name = os.path.basename(__file__).lower()
    index_data = load_existing_index(index_file)
    
    existing_cache = index_data.get("cache", {})
    
    for root, _, files in os.walk(base_dir):
        if root == base_dir:
            continue
        
        dir_name = os.path.basename(root)
        dir_key = dir_name.lower()
        
        if dir_key not in existing_cache:
            existing_cache[dir_key] = {"_dirname": dir_name}
        
        for file in sorted(files, key=str.casefold):
            if file.lower() in {script_name, "index.json"}:
                continue
            
            name_without_ext, _ = os.path.splitext(file)
            name_without_ext = name_without_ext.lower()
            
            if name_without_ext not in existing_cache[dir_key]:
                existing_cache[dir_key][name_without_ext] = file
    
    index_data["cache"] = existing_cache
    index_data["metadata"]["date"] = datetime.now().strftime("%Y-%m-%d")
    
    with open(index_file, "w", encoding="utf-8") as f:
        json.dump(index_data, f, separators=(',', ':'), ensure_ascii=False, sort_keys=False)
    
    print("Arquivo index.json atualizado com sucesso!")

if __name__ == "__main__":
    generate_index()
