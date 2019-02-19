from __future__ import print_function

# organizePath.py
# Purpose: organize an HLT path
# into sequences and modules
# Author: Thiago Tomei
# Date: 2019-02-19

import sys
import os
import fnmatch

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

HLTMenuName = "dumpedHLT.py"
mother_path_name = "HLT_Mu50_v13"
output_name = "hlt_Mu50.py"
cms_line = "import FWCore.ParameterSet.Config as cms\n\n"
system_subsystem = "HLTrigger.PhaseII."

# Parse the HLT menu
### Usually, blindly executing an external file is a security hazard... 
execfile(HLTMenuName)

print (process.process)
pathnames = process.paths.viewkeys()
sequencenames = set(process.sequences.viewkeys())

boilerPlate='''process.load("setup_dev_CMSSW_10_1_0_GRun_cff")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/mc/PhaseIIMTDTDRAutumn18DR/DYToLL_M-50_14TeV_TuneCP5_pythia8/FEVT/PU200_103X_upgrade2023_realistic_v2-v2/910000/F37B1F94-AD89-DF40-8D40-3EE87E8339A1.root'),
    inputCommands = cms.untracked.vstring('keep *')
)

# DQMStore service
# load the DQMStore and DQMRootOutputModule
process.load( "DQMServices.Core.DQMStore_cfi" )
process.DQMStore.enableMultiThread = True

# enable TrigReport, TimeReport and MultiThreading
process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool( True ),
    numberOfThreads = cms.untracked.uint32( 4 ),
    numberOfStreams = cms.untracked.uint32( 0 ),
    sizeOfStackForThreadsInKB = cms.untracked.uint32( 10*1024 )
)

process.GlobalTag.globaltag = cms.string('103X_upgrade2018_realistic_v8')
process.GlobalTag.toGet = cms.VPSet(
    cms.PSet(
        connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
        record = cms.string('L1TUtmTriggerMenuRcd'),
        snapshotTime = cms.string('2018-08-14 11:03:08.000'),
        tag = cms.string('L1Menu_Collisions2018_v2_1_0-d1_xml')
        ),
)

'''

### Define function to fix name of components in sequences
def name_fixer(name):
    # Fix the name
    if "(" in name:
        name = name.split("(")[1]
    if ")" in name:
        name = name.split(")")[0]
    if "process." in name:
        name = name.split(".")[1]
    return name

### Define function to get fully qualified name of component
def full_namer(name, process):
    entity = getattr(process,name)
    if type(entity).__name__ is "Sequence":
       return_name = "Sequences."+name+"_cff" 
    if type(entity).__name__ is "EDProducer":
       return_name = "Producers."+name+"_cfi" 
    if type(entity).__name__ is "EDFilter":
       return_name = "Filters."+name+"_cfi" 
    return return_name

def split_and_make_files(thePath, process, output_name, add_cms_line):

    # First get the python string, and split it into components
    python_string = thePath.dumpPython()
    split_python_string = python_string.split("+") ### FIXME: what if there are other dividers?
    
    if type(thePath).__name__ is "Path":
        name = thePath.label()
        print(name)
        with open(output_name,"w") as f:
            x = thePath.dumpPython()
            if (add_cms_line == True):
                f.write(cms_line)
            f.write("process = cms.Process('TEST')\n\n")
            f.write(boilerPlate)
            for component in split_python_string:
                component = name_fixer(component)
                component = full_namer(component, process)
                f.write("process.load('"+system_subsystem+component+"')\n")
            f.write("\n")
            f.write("process."+name+" = ")
            f.write(python_string)

    if type(thePath).__name__ is "Sequence":
        name = thePath.label()
        with open("python/Sequences/"+name+"_cff.py","w") as f:
            x = thePath.dumpPython()
            f.write(cms_line)
            for component in split_python_string:
                component = name_fixer(component)
                component = full_namer(component, process)
                f.write("from "+system_subsystem+component+" import *\n")
            f.write("\n")
            f.write(name+" = ")
            f.write(python_string.replace("process.",""))

    for name in split_python_string:
        name = name_fixer(name)
        entity = getattr(process,name)
        # Is this module or a sequence? If it is a sequence, recurse
        if type(entity).__name__ is "Sequence":
            split_and_make_files(entity,process,output_name,False)
        if type(entity).__name__ is "EDProducer":
            with open("python/Producers/"+name+"_cfi.py","w") as f:
                x = entity.dumpPython()
                f.write(cms_line)
                f.write(name+" = ")
                f.write(x)
        if type(entity).__name__ is "EDFilter":
            with open("python/Filters/"+name+"_cfi.py","w") as f:
                x = entity.dumpPython()
                f.write(cms_line)
                f.write(name+" = ")
                f.write(x)

### Okay, now we should parse the paths
print("\n"+"="*16+"\n")
thePath = getattr(process,mother_path_name)
#hlt_trigger_first_path = getattr(process,"HLTriggerFirstPath")
#split_and_make_files(hlt_trigger_first_path, process, output_name, True)
split_and_make_files(thePath, process, output_name, True)
