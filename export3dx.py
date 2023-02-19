from pathlib import Path
import numpy as np

ext = ".x3d"
savedir = Path(r'C:\GithubData\OpenFOAM_Vis_Blender\cal_data\PV_x3d')
savedir.mkdir(exist_ok=True)

# time steps
tk = GetTimeKeeper()
timesteps = tk.TimestepValues
numTimesteps = len(timesteps)

animationScene1 = GetAnimationScene()
renderView1 = GetActiveViewOrCreate('RenderView')
animationScene1.PlayMode = 'Snap To TimeSteps'
animationScene1.GoToFirst()
for i, time in enumerate(timesteps):
    animationScene1.AnimationTime=time
    timeStr = f'{i:04d}_time={time:04.2f}'
    ofn = savedir/ (timeStr + ext)
    print(ofn)
    ExportView(str(ofn), view=renderView1)