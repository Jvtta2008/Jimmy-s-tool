import maya.cmds as cmds
if not cmds.commandPort(':7002', q=True):
    cmds.commandPort(n=':7002')
