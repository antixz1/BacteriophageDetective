import os

#assuming Phigaro and docker are installed

def runPhigaro():
    runPhigaro_command = 'sudo docker run -it phigaro'
    os.system(runPhigaro_command)

runPhigaro()

