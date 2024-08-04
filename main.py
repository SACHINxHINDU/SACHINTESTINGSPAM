import sys
import glob
import asyncio
import logging
import importlib
import urllib3
from pathlib import Path
from config import SACHIN0, SACHIN1, SACHIN2, SACHIN3, SACHIN4, SACHIN5, SACHIN6, SACHIN7, SACHIN8, SACHIN9

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def load_plugins(plugin_name):
    path = Path(f"SACHIN/modules/{plugin_name}.py")
    spec = importlib.util.spec_from_file_location(f"SACHIN.modules.{plugin_name}", path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["SACHIN.modules." + plugin_name] = load
    print("Snatani Spam has Imported " + plugin_name)


files = glob.glob("SACHIN/modules/*.py")
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))
        

print("Sanatani Bot Deployed Successfully.")


async def main():
    await SACHIN0.run_until_disconnected()
    await SACHIN1.run_until_disconnected()
    await SACHIN2.run_until_disconnected()
    await SACHIN3.run_until_disconnected()
    await SACHIN4.run_until_disconnected()
    await SACHIN5.run_until_disconnected()
    await SACHIN6.run_until_disconnected()
    await SACHIN7.run_until_disconnected()
    await SACHIN8.run_until_disconnected()
    await SACHIN9.run_until_disconnected()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
