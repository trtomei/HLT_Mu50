import FWCore.ParameterSet.Config as cms

process.load('HLTrigger.PhaseII.Filters.hltTriggerType_cfi')
process.load('HLTrigger.PhaseII.Sequences.HLTL1UnpackerSequence_cff')
process.load('HLTrigger.PhaseII.Sequences.HLTBeamSpot_cff')

HLTBeginSequence = cms.Sequence(process.hltTriggerType+process.HLTL1UnpackerSequence+process.HLTBeamSpot)
