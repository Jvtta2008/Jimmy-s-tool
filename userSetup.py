#gate for mayaCharm

import maya.cmds as cmds

print "check port 7002 for mayaCharm communication - this is for developer"

if not cmds.commandPort(':7002', q=True):
    cmds.commandPort(n=':7002')