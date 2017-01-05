import maya.cmds as cmds

print 'loading GPbuttonsFunction.py'

def gotoObjectmod():
    a = cmds.ls(sl=True)

    if ( len(a) > 0 ):
        pick1st = a[0]
        ioF = pick1st.index('f')-1
        objName = pick1st[0:ioF]
        cmds.select(objName, r=1)
    
def Chop():
    a = cmds.ls(sl=True)
    if ( len(a) > 0 ):
        cmds.polyChipOff(ch=1, kft=1, dup=0, off=0)
        gotoObjectmod()
        cmds.polySeparate();

def reverseNormal():
    a = cmds.ls(sl=True)
    if ( len(a) > 0 ):
        cmds.polyNormal(nm=0)

def normalOnOff():
    a = cmds.ls(sl=True)
    if ( len(a) > 0 ):
        cmds.ToggleFaceNormalDisplay();

def deleteHis():
    a = cmds.ls(sl=True)
    if ( len(a) > 0 ):
        cmds.DeleteHistory();
    
def freezeTransformation():
    a = cmds.ls(sl=True)
    if ( len(a) > 0 ):
        cmds.makeIdentity(apply=True)

def Centerpivot():
    a = cmds.ls(sl=True)
    if ( len(a) > 0 ):
        cmds.xform(cp=True)

def JointOff():
    JointsSel = cmds.ls(sl=True)
    Joints = []
    
    for item in JointsSel:
        Joints.append(item)
    
    NumOfJoints = int(len(JointsSel))
    i = 0
    
    for item in range(NumOfJoints):
        JointsName = Joints[i]
        cmds.setAttr(JointsName + '.displayLocalAxis',0)
        i = i + 1
    
def JointOn():
    JointsSel = cmds.ls(sl=True)
    Joints = []
    
    for item in JointsSel:
        Joints.append(item)
    
    NumOfJoints = int(len(JointsSel))
    i = 0
    
    for item in range(NumOfJoints):
        JointsName = Joints[i]
        cmds.setAttr(JointsName + '.displayLocalAxis',1)
        i = i + 1

def ChildSel():
    a = cmds.ls(sl=True)
    if ( len(a) > 0 ):
        cmds.select(hi=True)

def ArmCons():
    a = cmds.ls(sl=True)
    if ( len(a) > 0 ):
        cmds.aimConstraint(mo=True, weight = 1)

def OrientCons():
    a = cmds.ls(sl=True)
    if ( len(a) > 0 ):
        cmds.orientConstraint(mo=True, weight = 1)
    
def ParentCons():
    a = cmds.ls(sl=True)
    if ( len(a) > 0 ):
        cmds.parentConstraint(mo=True, weight = 1)

def CtrlsColor():
    LNurbs=[]
    RNurbs=[]
    nurbs = cmds.ls(sl=True)
    letterL = str("_L")
    letterR = str("_R")
    
    for item in nurbs:
        if letterL in item:
            LNurbs.append(item)
    
    numberOfL = int(len(LNurbs))
    i = 0
    
    for item in range(numberOfL):
        overRideTar = LNurbs[i]
        overRideTarRename = overRideTar + "Shape"
        cmds.setAttr(overRideTarRename + '.overrideEnabled', 1)
        cmds.setAttr(overRideTarRename + '.overrideColor', 13)
        i = i + 1
    
    for item in nurbs:
        if letterR in item:
            RNurbs.append(item)
    
    numberOfR = int(len(RNurbs))
    i = 0
    
    for item in range(numberOfR):
        overRideTar = RNurbs[i]
        overRideTarRename = overRideTar + "Shape"
        cmds.setAttr(overRideTarRename + '.overrideEnabled', 1)
        cmds.setAttr(overRideTarRename + '.overrideColor', 6)
        i = i + 1

def Yeallow():
    CtrlsSel = cmds.ls(sl=True)
    Ctrls = []
        
    for item in CtrlsSel:
        Ctrls.append(item)
    
    NumOfCtrls = int(len(CtrlsSel))
    i = 0
    
    for item in range(NumOfCtrls):
        CtlrName = Ctrls[i]
        CtlrNameNode = CtlrName + "Shape"
        cmds.setAttr(CtlrNameNode + '.overrideEnabled', 1)
        cmds.setAttr(CtlrNameNode + '.overrideColor', 17)
        i = i + 1

def Cyan():
    CtrlsSel = cmds.ls(sl=True)
    Ctrls = []
    
    
    for item in CtrlsSel:
        Ctrls.append(item)
    
    NumOfCtrls = int(len(CtrlsSel))
    i = 0
    
    for item in range(NumOfCtrls):
        CtlrName = Ctrls[i]
        CtlrNameNode = CtlrName + "Shape"
        cmds.setAttr(CtlrNameNode + '.overrideEnabled', 1)
        cmds.setAttr(CtlrNameNode + '.overrideColor', 18)
        i = i + 1

def openHypershader():
    ohs = cmds.HypershadeWindow()

def openNodeEditor():
    one = cmds.NodeEditorWindow()

def openPluinManager():
    opm = cmds.PluginManager()

def currentSel():
    curSel = cmds.ls(sl=True)
    numOfCur = int(len(curSel))
    print "UPDATE NUMBER OF CURRENT SELECT:", numOfCur
    print curSel

def assignMatToSel():
    a = cmds.ls(sl=True)
    
    numOfObjs = int(len(a))
    
    i = 0
    for item in range(numOfObjs):
        objName = a[i]
        shaderName = objName+"_mat"
        cmds.select(a[i])
        cmds.hyperShade(assign = shaderName)
        i = i + 1

def deselectShapeNode():
    shapeList = cmds.ls(shapes=True)
    numOfShapes = int(len(shapeList))

    i = 0
    for item in shapeList:
        shapeName = shapeList[i]
        cmds.select(shapeName, d=True)
        i = i + 1

def deselectGroup():
    a = cmds.ls(sl=True)
    groupList = []
    groupLetter = str("_group")
    for item in a:
        if groupLetter in item:
            groupList.append(item)
            
    NumOfGrp = int(len(groupList))
    i = 0
    for item in range(NumOfGrp):
        groupName = groupList[i]
        cmds.select(groupName, d=True)
        i = i + 1

def deselectLight():
    a = cmds.ls(sl=True)
    lightsList = []
    lightLetter = str("_light")
    for item in a:
        if lightLetter in item:
            lightsList.append(item)

    NumOfLight = int(len(lightsList))
    i = 0
    for item in range(NumOfLight):
        lightName = lightsList[i]
        cmds.select(lightName, d=True)
        i = i + 1

def deselectCam():
    camList = cmds.ls(ca=1)
        
    NumOfCam = int(len(camList))
    
    i = 0
    for item in range(NumOfCam):
        camName = camList[i]
        NumChac = len(camName) - 5
        cmds.select(camName[0:NumChac], d=True)
        i = i + 1

def deselectCtrl():
    a = cmds.ls(sl=True)

    ctrlLet = str("_ctrl")
    ctrlList = []
    
    for item in a:
        if ctrlLet in item:
            ctrlList.append(item)
        
        numOfCtrl = int(len(ctrlList))
        i = 0
        
        for item in range(numOfCtrl):
            ctrlName = ctrlList[i]
            cmds.select(ctrlName, d=True)
            i = i + 1

def deselectCheckerBalls():    
    a = cmds.ls(sl=True)
    ballList = []
    ballLet = str("Ball")
    
    for item in a:
        if ballLet in item:
            ballList.append(item)
        
        numOfBall = int(len(ballList))
        i = 0
        
        for item in range(numOfBall):
            ballName = ballList[i]
            cmds.select(ballName, d=True)
            i = i + 1

def deselectGround():
    a = cmds.ls(sl=True)
    groundLet = str("Ground")
    groundList = []
    
    for item in a:
        if groundLet in item:
            groundList.append(item)
            
        numOfGround = int(len(groundList))
        i = 0
        
        for item in range(numOfGround):
            groundName = groundList[i]
            cmds.select(groundName, d = True)
            i = i + 1

def openVrayVFB():
    cmds.setAttr("defaultRenderGlobals.currentRenderer", "vray", type="string")
    cmds.vray("showVFB")

def autoAssignMat():   
    ##select every dag object (everything in outliner)
    allList = cmds.ls(dag=True)
    cmds.select(allList)
    #deselect shape node
    deselectShapeNode()
    #deselect group
    deselectGroup()
    #deselect light
    deselectLight()
    #deselect cam
    deselectCam()
    #deselect controller
    deselectCtrl()
    #deselect checker balls
    deselectCheckerBalls()
    #deselect ground plane
    deselectGround()
    sel = cmds.ls(sl=True)
    assignMatToSel()

def LoadAllFunction():
    gotoObjectmod()
    Chop()
    reverseNormal()
    normalOnOff()
    deleteHis()
    freezeTransformation()
    Centerpivot()
    JointOff()
    JointOn()
    ChildSel()
    ArmCons()
    OrientCons()
    ParentCons()
    CtrlsColor()
    Yeallow()
    Cyan()
    openHypershader()
    openNodeEditor()
    openPluinManager()
    currentSel()
    openVrayVFB()
    assignMatToSel()

def processBF():
    print "Loading all functions succeecd"