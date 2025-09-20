import os
import json
import Utils
import zipfile
from worlds.Files import APPlayerContainer

class SHARContainer(APPlayerContainer):
    game: str = "The Simpsons Hit And Run"

    def __init__(self, card_table, base_path: str, output_directory: str,
                 player=None, player_name: str = "", server: str = ""):
        self.card_table = card_table
        self.output_directory = output_directory
        self.file_path = base_path
        container_path = os.path.join(output_directory, base_path)
        self.patch_file_ending = ".zip"
        super().__init__(container_path, player, player_name, server)

    def write_contents(self, opened_zipfile: zipfile.ZipFile):
        safe_player = str(self.player).replace(" ", "_")
        filename = f"{safe_player}_SHAR.json"

        json_data = json.dumps({"Cards": self.card_table}, indent=4)
        opened_zipfile.writestr(filename, json_data)
        super().write_contents(opened_zipfile)

def gen(output_directory, mod_name, card_table, player):
    mod_dir = os.path.join(output_directory, f"{mod_name}_{Utils.__version__}")
    mod = SHARContainer(
        card_table,
        mod_dir,
        output_directory,
        player
    )
    mod.write()

