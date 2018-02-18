import sys
import os
import re

def changePortDir(portsInfo):
    testPortsInfo = []
    for ports in portsInfo:
        #ports.lower()
        #print ports
        if ports.find("sc_in<")==0:
            #print ports
            ports = ports.replace("sc_in<", "sc_out<")
        elif ports.find("sc_out<")==0:
            ports.replace("sc_out<", "sc_in<")
        testPortsInfo.append(ports)
    print testPortsInfo
    return testPortsInfo 

def stripPortDecl(modelFile):
    portsInfo = []
    portFormat = re.compile(("sc_in|sc_out|sc_inout")+".*")
    for lines in modelFile:
        lines = lines.strip()
        if portFormat.match(lines):
            #lines.rstrip(';')
            portsInfo.append(lines)
    #print portsInfo
    return portsInfo


def validateFileName(modelFiles):
    fileNameFormat = re.compile(".*\.cpp");
    if fileNameFormat.match(modelFiles):
        return 0
    else:
        return 1


def main():
    portsInfo = []
    testPortsInfo = []
    os.chdir(sys.argv[1])
    for modelFiles in os.listdir("."):
        ignoreFile = validateFileName(modelFiles)
        if ignoreFile == 0:
            with open(modelFiles) as modelFile:
                #populate the ports
                #print modelFile.name
                portsInfo = stripPortDecl(modelFile)
                #print portsInfo
                testPortsInfo = changePortDir(portsInfo)



if __name__ == "__main__":
    #check for arguments
    if len(sys.argv) < 2:
        print """Too few arguments
        Usage <script_name.py><path of model file>
        """
    main()
    exit()
