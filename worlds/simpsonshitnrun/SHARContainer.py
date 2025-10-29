import os
import json
import Utils
import zipfile
from worlds.Files import APPlayerContainer

class SHARContainer(APPlayerContainer):
    game: str = "The Simpsons Hit And Run"

    def __init__(self, ID, TitleID, card_table, traffic_table, mission_locks, base_path: str, output_directory: str,
                 player=None, player_name: str = "", server: str = ""):
        self.ID = ID
        self.TitleID = TitleID
        self.card_table = card_table
        self.traffic_table = traffic_table
        self.mission_locks = mission_locks
        self.output_directory = output_directory
        self.file_path = base_path
        container_path = os.path.join(output_directory, base_path)
        self.patch_file_ending = ".zip"
        super().__init__(container_path, player, player_name, server)

    def write_contents(self, opened_zipfile: zipfile.ZipFile):
        safe_player = str(self.player).replace(" ", "_")
        filename = f"SHAR.ini"

        ini_data = f"[IDENTIFIER]\n"
        ini_data += f"ID={self.ID}\n"
        ini_data += f"TitleID={self.TitleID}\n\n"
        i = 1
        for card in self.card_table:
            ini_data += "[CARD]\n"
            ini_data += f"Name=card{card['level'][-1]}{i}\n"
            ini_data += f"CardName={card['name']}\n"
            ini_data += f"X={card['X']}\n"
            ini_data += f"Y={card['Y']}\n"
            ini_data += f"Z={card['Z']}\n"
            ini_data += f"APID={card['id']}\n\n"
            i = i + 1 if i < 7 else 1

        for car in self.traffic_table:
            ini_data += "[TRAFFIC]\n"
            ini_data += f"Name={car}\n\n"

        for mission, car in self.mission_locks.items():
            ini_data += "[MISSIONLOCK]\n"
            ini_data += f"Mission={mission}\n"
            ini_data += f"Car={car}\n\n"

        opened_zipfile.writestr(filename, ini_data)
        super().write_contents(opened_zipfile)

def gen(output_directory, mod_name, ID, TitleID, card_table, traffic_table, mission_locks, player):
    mod_dir = os.path.join(output_directory, f"{mod_name}_{Utils.__version__}")
    mod = SHARContainer(
        ID,
        TitleID,
        card_table,
        traffic_table,
        mission_locks,
        mod_dir,
        output_directory,
        player
    )
    mod.write()

