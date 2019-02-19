import FWCore.ParameterSet.Config as cms

process = cms.Process('TEST')

process.load("setup_dev_CMSSW_10_1_0_GRun_cff")

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

process.load('HLTrigger.PhaseII.Sequences.HLTBeginSequence_cff')
process.load('HLTrigger.PhaseII.Filters.hltL1sSingleMu22or25_cfi')
process.load('HLTrigger.PhaseII.Filters.hltPreMu50_cfi')
process.load('HLTrigger.PhaseII.Filters.hltL1fL1sMu22or25L1Filtered0_cfi')
process.load('HLTrigger.PhaseII.Sequences.HLTL2muonrecoSequence_cff')
process.load('HLTrigger.PhaseII.Filters.hltL2fL1sMu22or25L1f0L2Filtered10Q_cfi')
process.load('HLTrigger.PhaseII.Sequences.HLTL3muonrecoSequence_cff')
process.load('HLTrigger.PhaseII.Filters.hltL1fForIterL3L1fL1sMu22or25L1Filtered0_cfi')
process.load('HLTrigger.PhaseII.Filters.hltL3fL1sMu22Or25L1f0L2f10QL3Filtered50Q_cfi')
process.load('HLTrigger.PhaseII.Sequences.HLTEndSequence_cff')

process.HLT_Mu50_v13 = cms.Path(process.HLTBeginSequence+process.hltL1sSingleMu22or25+process.hltPreMu50+process.hltL1fL1sMu22or25L1Filtered0+process.HLTL2muonrecoSequence+cms.ignore(process.hltL2fL1sMu22or25L1f0L2Filtered10Q)+process.HLTL3muonrecoSequence+cms.ignore(process.hltL1fForIterL3L1fL1sMu22or25L1Filtered0)+process.hltL3fL1sMu22Or25L1f0L2f10QL3Filtered50Q+process.HLTEndSequence)
