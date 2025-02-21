from tqdm import tqdm
import time

def flow():
    # ------------- 配置好进度条 ------------- 
    
    pbar = tqdm(total=100)
    pbar.set_description(' Flow ')
    update = lambda *args: pbar.update()
    for _ in range(10):
        time.sleep(1)
        update()

flow()