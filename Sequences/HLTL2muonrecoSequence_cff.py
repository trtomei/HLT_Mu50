import FWCore.ParameterSet.Config as cms

process.load('HLTrigger.PhaseII.Sequences.HLTL2muonrecoNocandSequence_cff')
process.load('HLTrigger.PhaseII.Producers.hltL2MuonCandidates_cfi')

HLTL2muonrecoSequence = cms.Sequence(process.HLTL2muonrecoNocandSequence+process.hltL2MuonCandidates)
