import maya.cmds as cmds


def addBlankspace():
    i = 0
    for i in range(1, 4):
        cmds.text(l="", h=10, w=100)
        i = i + 1


def addBlankButton():
    cmds.text(l="", w=100)


def addSeparator():
    i = 0
    for i in range(1, 4):
        cmds.separator(style="in", w=100)
        i = i + 1


def addTitleBar(n):
    cmds.text(l=n, h=25, w=360)
    cmds.text(l="", h=25, w=120)
    cmds.text(l="", h=25, w=120)


def setProjectDir(link):
    cmds.workspace(dir=cmds.textField(link, text=1, q=1))
    print 'project folder has been set to:', link


# start define window UI

GPwinID = cmds.window(w=410)

# create 2 rows, left is menu icon buttons, right is GP tools UI
mlo = cmds.rowColumnLayout(nc=2, cat=[1, 'right', 1], cw=[(1, 40), (2, 360)])

# make left row for the bar of icon buttons
sideMenuLayout = cmds.columnLayout(cat=['left', 0])

# 'start left row: bar with icon buttons'
numOfib = 13
i = 0
for item in range(numOfib):
    ibName = "ib_" + str(i + 1)
    cmds.button(l=ibName, h=40, w=40, )
    cmds.text(l='', h=7.5)
    i = i + 1
numOfblank = 4
i = 0

for item in range(numOfblank):
    cmds.text(l='', h=38, w=40)
    i = i + 1

    # 'end of right row'
# go to mlo layer to create right row
cmds.setParent(mlo)

# 'start right row'
# Create the tLayout /master layer
tabControls = cmds.tabLayout()

# create t1 /1st layer
t1 = cmds.paneLayout(configuration='horizontal2')

# 'start right row top section'
# Make column layout for top sections /2nd layer
# create menu bar
# file
menuBar = cmds.menuBarLayout()
cmds.menu(label='File', tearOff=True)
cmds.menuItem(label='New')
cmds.menuItem(label='Open')
cmds.menuItem(label='Save')
cmds.menuItem(divider=True)
cmds.menuItem(label='Quit')

# about
cmds.menu(label='Help', helpMenu=True)
cmds.menuItem('Application..."', label='"About')

t1_trrlo1 = cmds.columnLayout()

# 'scene setup section'
# Make a Collapsable frame style layout /3nd layer
t1_trrlo1_f1 = cmds.frameLayout(label="Scene Setup", collapsable=True)

# creat rows for SCENE SETUP section /4rd layer
t1_trrlo1_f1_lo1 = cmds.rowColumnLayout(nc=3, cat=[1, 'right', 1], cw=[(1, 60), (2, 270), (3, 20)])

getLink = cmds.workspace(q=1, rd=1)
cmds.button(l='set project', w=60, command='setProjectDir(getLink)')

curPth = cmds.textField(text=getLink)

cmds.symbolButton(ann='open folder project', image='GPopenFolder.png', command='cmds.OpenScene()')
# 'end scene Setup section'

# go up to framelayout layer for GP tools section /3nd layer
cmds.setParent(t1_trrlo1)

# 'GP tools section'
# Make a Collapsable frame style layout /3nd layer
t1_trrlo1_f2 = cmds.frameLayout(label="GP tools", collapsable=True)

# creat rows for GP TOOLS section /4rd layer
t1_trrlo1_f2_lo1 = cmds.rowColumnLayout(nc=3, cat=[1, "both", 0], cw=[(1, 120), (2, 120), (3, 120)])

addTitleBar(n='MODELING')

cmds.button(label="Center Pivot", command='Centerpivot()')
cmds.button(label="Freeze Trans", command='freezeTransformation()')
cmds.button(label="Delete History", command='deleteHis()')

cmds.button(label="Normal on/off", command='normalOnOff()')
cmds.button(label="Chop", command='Chop()')
cmds.button(label="Reverse normal", command='reverseNormal()')

addTitleBar(n='RIGGING')

cmds.button(label="Select Children", command='ChildSel()')
cmds.button(label="Ori On", command='JointOn()')
cmds.button(label="Off", command='JointOff()')

cmds.button(label="Parent", command='ParentCons()')
cmds.button(label="Orien", command='OrientCons()')
cmds.button(label="Arm", command='ArmCons()')

cmds.button(label="LR to RB", command='CtrlsColor()')
cmds.button(label="Yeallow", command='Yeallow()')
cmds.button(label="Cyan", command='Cyan()')

addTitleBar(n='LIGHTING & TEXTURING')

cmds.button(label="Node Editor", command='openNodeEditor()')
cmds.button(label="Hypershader", command='openHypershader()')
cmds.button(label="Auto Assign", command='autoAssignMat()')

addTitleBar(n='RENDERING')

cmds.button(label="Vray VFB", command='openVrayVFB()')
cmds.button(label="Render Setting", command='openRenderSetting()')
cmds.button(label="Plugin", command='openPluinManager()')

# 'end GP tool section'
# 'end right row top section'

# go back to t1 layer /1st layer
cmds.setParent(t1)

# 'start bot right row section'
# create layout for bot right row section /2st layer
t1_brrlo1 = cmds.tabLayout()

# create sub tab 1 for bot right row section /3rd layer
t1_brrlo1_st1 = cmds.columnLayout()
cmds.button()
# go back to sub tap layer/2rd layer
cmds.setParent(t1_brrlo1)

# create sub tab 2 for bot right row section /3rd layer
t1_brrlo1_st2 = cmds.columnLayout()
cmds.button()
# go back to sub tap layer/2rd layer
cmds.setParent(t1_brrlo1)

# create sub tab 2 for bot right row section /3rd layer
t1_brrlo1_st3 = cmds.columnLayout()
cmds.button()

# go back to sub tap layer/2rd layer
cmds.setParent(t1_brrlo1)

# define sub tabs of bot right row section
cmds.tabLayout(t1_brrlo1, edit=True,
               tabLabel=((t1_brrlo1_st1, "Display"), (t1_brrlo1_st2, "Option"), (t1_brrlo1_st3, "Display")))

# 'end bot right row section'
# 'end right row'
# go back to tab layout of right row /1st layer
cmds.setParent(tabControls)

# Create colunm layout for tab 2 /4th layer
t2 = cmds.paneLayout(configuration='horizontal2')

# Create tittle
t3_lo1 = cmds.frameLayout(l='RENAMER')

# Create Rename tool work with Outliner
t2_lo2 = cmds.rowColumnLayout(nc=3, cat=[1, "both", 0], cw=[(1, 120), (2, 120), (3, 120)], h=50)

obj_Name = cmds.textField(text='geo')
part_Name = cmds.textField(text='left')
version_Name = cmds.textField(text='01')


def Rename():
    part1 = cmds.textField(obj_Name, text=1, q=1)
    part2 = cmds.textField(part_Name, text=1, q=1)
    part3 = cmds.textField(version_Name, text=1, q=1)

    a = cmds.ls(sl=True)

    numOfobj = len(a)

    i = 0
    for i in range(numOfobj):
        newName = cmds.rename(a[i], part1 + "_" + part2 + "_" + part3 + str(i),ignoreShape=True)
        b = cmds.listRelatives(newName)
        cmds.rename(b[0],part1 + "_" + part2 + "_" + part3 + str(i)+"Shape")
        i = i + 1

cmds.button(label='Rename', command='Rename()')
cmds.button(label='Group.Name', command='RenameViaGroup()')
cmds.button(label='Auto Rename', command='autoRenaming()')

cmds.setParent(t2)

t2_lo3 = cmds.outlinerPanel()

# go back to master layer /master layer
cmds.setParent(tabControls)

# Create appropriate labels for the ts
cmds.tabLayout(tabControls, edit=True, tabLabel=((t1, "GP tool"), (t2, "GP Oliner")))
# Display the UI
allowedAreas = ['right', 'left']


def quickCheck():
    try:
        GPdockID
    except NameError:
        print 'Tool is not created - Initing Tool'
    else:
        if GPdockID:
            cmds.deleteUI(GPdockID)


quickCheck()

GPdockID = cmds.dockControl(l="Jimmy's tool v1.0.3", area='left', content=GPwinID, allowedArea=allowedAreas)
