import FWCore.ParameterSet.Config as cms

process.load('HLTrigger.PhaseII.Sequences.HLTMuonLocalRecoSequence_cff')
process.load('HLTrigger.PhaseII.Producers.hltL2OfflineMuonSeeds_cfi')
process.load('HLTrigger.PhaseII.Producers.hltL2MuonSeeds_cfi')
process.load('HLTrigger.PhaseII.Producers.hltL2Muons_cfi')

HLTL2muonrecoNocandSequence = cms.Sequence(process.HLTMuonLocalRecoSequence+process.hltL2OfflineMuonSeeds+process.hltL2MuonSeeds+process.hltL2Muons)
