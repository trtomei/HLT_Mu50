# PhaseII

Repository for CMS HLT studies for Phase-II

## Current contents
   * HLT_Mu50_v13 path, as it stood at the end of Run 2

## Instructions

```
cmsrel CMSSW_10_4_0_mtd5
cd CMSSW_10_4_0_mtd5
cmsenv
mkdir HLTrigger
cd HLTrigger
git clone git@github.com:trtomei/PhaseII.git
cd PhaseII
scram b
```

Grab a path from ConfDB, for instance `HLT_Mu50_v13`: from Thiago's area:

```
hltGetConfiguration /users/tomei/Phase2/Run2Menu/HLT/V2 \
--input file:file.roott --offline --mc --unprescale --no-output \
--process TEST --globaltag auto:run2_mc_GRun --setup /dev/CMSSW_10_1_0/GRun &> hlt.py
```

and dump it with python to make it easier. Do `python -i hlt.py` and inside python:

```python
x = process.dumpPython()
f = open("dumpedHLT.py","w")
f.write(x)
f.close()
```

To split the path and organize the modules and sequences in their folders, edit and run `organizePath.py`.
