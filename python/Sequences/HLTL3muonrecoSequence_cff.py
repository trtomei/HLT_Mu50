import FWCore.ParameterSet.Config as cms

process.load('HLTrigger.PhaseII.Sequences.HLTL3muonrecoNocandSequence_cff')
process.load('HLTrigger.PhaseII.Producers.hltIterL3MuonCandidates_cfi')

HLTL3muonrecoSequence = cms.Sequence(process.HLTL3muonrecoNocandSequence+process.hltIterL3MuonCandidates)
