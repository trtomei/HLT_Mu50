import FWCore.ParameterSet.Config as cms

process.load('HLTrigger.PhaseII.Filters.hltBoolEnd_cfi')

HLTEndSequence = cms.Sequence(process.hltBoolEnd)
