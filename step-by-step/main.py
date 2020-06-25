import json
import sys

sys.path.append('code')
import code_generator as code_g
import atomizer as atom
from functions_file import *
import functions_file

import asyncio
import time
from pyppeteer import launch


with open('globo_test.json') as file:
    recipe = json.load(file)

with open('steps.py', 'w+') as file:
    print(code_g.generate_code(recipe, functions_file))
    file.write(code_g.generate_code(recipe, functions_file))


async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto('http://www.in.gov.br/web/guest/inicio')

    steps = __import__('steps')

    await steps.execute_steps(page = page)

    await browser.close()
    return

asyncio.get_event_loop().run_until_complete(main())





