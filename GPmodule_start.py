def psource(module):
    import sys
	
    import os


    file = os.path.basename(module)
    os.path.basename(module)
    
    toks = file.split('.')
    modname = toks[0]
    
    #check if dirrectory is really a directory
    
    if(os.path.exists(dir)):
        
    #check if the file directory already exists in the sys.path array
    
        paths = sys.path
        pathfound = 0
        for path in paths:
            if(dir == path):
                pathfound = 1
    
    #if the dirrectory is not part of sys.path add it
        if not pathfound:
            sys.path.append(dir)
            
    #exec works like MEL's eval but you need to add in globals()
    #at the end to make sure the file is imported into the global
    #nameespace else it wil only be in the scope of this function
    
    exec ('import' + modname) in globals()
    
    #reload the file to make sure its up to date
    exec ('reload('+modname+')') in globals()
    
    #this returns the namespace of the file imported
    return modname
    
#when you import a file you must give it the full path
def callbuttonsFunction():
	psource(r'C/Users/panda/Documents/maya/2016/scripts/GPbuttonsFuction.py')

def winUI():
	psource(r'C/Users/panda/Documents/maya/2016/scripts/GPwindowUI.py')

def GPmodule_start():
	callbuttonsFunction()