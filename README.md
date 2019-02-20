# PhaseII

Repository for CMS HLT studies for Phase-II

## Current contents
   * HLT_Mu50_v13 path, as it stood at the end of Run 2, with technical changes to run in Phase-II samples

## Instructions

```
cmsrel CMSSW_10_4_0_mtd5
cd CMSSW_10_4_0_mtd5/src
cmsenv
mkdir HLTrigger
cd HLTrigger
git clone git@github.com:trtomei/PhaseII.git
cd PhaseII
scram b
```

### To add a new path (but read the notice below)

Grab a path from ConfDB, for instance `HLT_Mu50_v13`: from Thiago's area:

```
hltGetConfiguration /users/tomei/Phase2/Run2Menu/HLT/V2 \
--input file:file.root --offline --mc --unprescale --no-output \
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

*Notice that your newly added path may not run because of Phase II-related changes in the modules!* Part of the job is indeed to understand the changes needed for Phase-II reconstruction, and make the HLT code compliant with it. For instance, if you actually execute the steps above for `HLT_Mu50_v13`, it will *not* run because of changes in `hltSiPixelClusters` and `hltSiStripRawToClustersFacility`. Thiago has already changed those two modules in the current master of the repository.
