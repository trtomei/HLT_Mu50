import FWCore.ParameterSet.Config as cms

process.load('HLTrigger.PhaseII.Producers.hltGtStage2Digis_cfi')
process.load('HLTrigger.PhaseII.Producers.hltGtStage2ObjectMap_cfi')

HLTL1UnpackerSequence = cms.Sequence(process.hltGtStage2Digis+process.hltGtStage2ObjectMap)
