import sys 
sys.path.append("code")
from functions_file import *

async def execute_steps(**missing_argument):
    await clique(**{'xpath': '//*[@id="banner"]/div[1]/div[2]/div[1]/div/div/ul/li[3]/a'}, **missing_argument)
    await clique(**{'xpath': '//*[@id="portlet_leituradou_INSTANCE_GKE7NRmaCXgl"]/div/div[2]/div/div[1]/div[3]/button[4]'}, **missing_argument)
    wait(**{'segs': 3})
