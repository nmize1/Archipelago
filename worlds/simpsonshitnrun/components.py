from worlds.LauncherComponents import Component, SuffixIdentifier, components, Type, icon_paths
import asyncio
from pathlib import Path

def run_client(ap_url=None):
    asyncio.run(run_client_async(ap_url))

async def run_client_async(ap_url=None):
    from .SHARClient import SHARContext
    ctx = SHARContext()
    await ctx.initialize()
    if ap_url:
        await ctx.handle_apshar(Path(ap_url))
    else:
        await ctx.start()

def _launch_shar_client_process():
    import os, sys, subprocess
    client_path = os.path.join(os.path.dirname(__file__), "SHARClient.py")
    subprocess.Popen([sys.executable, client_path])


icon_paths["Donut"] = f"ap:{__name__}/icons/Donut.png"
components.append(
    Component(
        "Simpsons Hit & Run Client",
        func=run_client,
        game_name="Simpsons Hit and Run",
        component_type=Type.CLIENT,
        file_identifier=SuffixIdentifier(".apshar"),
        cli=False,
        icon="Donut"
    )
)