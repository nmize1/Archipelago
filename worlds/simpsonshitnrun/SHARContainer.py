import os
import json
import Utils
import zipfile
from worlds.Files import APPlayerContainer

class SHARContainer(APPlayerContainer):
    game: str = "The Simpsons Hit And Run"

    def __init__(self, card_table, traffic_table, base_path: str, output_directory: str,
                 player=None, player_name: str = "", server: str = ""):
        self.card_table = card_table
        self.traffic_table = traffic_table
        self.output_directory = output_directory
        self.file_path = base_path
        container_path = os.path.join(output_directory, base_path)
        self.patch_file_ending = ".zip"
        super().__init__(container_path, player, player_name, server)

    def write_contents(self, opened_zipfile: zipfile.ZipFile):
        safe_player = str(self.player).replace(" ", "_")
        filename = f"SHAR.ini"

        ini_data = ""
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


        opened_zipfile.writestr(filename, ini_data)
        super().write_contents(opened_zipfile)

def gen(output_directory, mod_name, card_table, traffic_table, player):
    mod_dir = os.path.join(output_directory, f"{mod_name}_{Utils.__version__}")
    mod = SHARContainer(
        card_table,
        traffic_table,
        mod_dir,
        output_directory,
        player
    )
    mod.write()

