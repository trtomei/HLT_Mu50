import FWCore.ParameterSet.Config as cms

process.load('HLTrigger.PhaseII.Producers.hltScalersRawToDigi_cfi')
process.load('HLTrigger.PhaseII.Producers.hltOnlineBeamSpot_cfi')

HLTBeamSpot = cms.Sequence(process.hltScalersRawToDigi+process.hltOnlineBeamSpot)
