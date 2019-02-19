import FWCore.ParameterSet.Config as cms

process.load('HLTrigger.PhaseII.Sequences.HLTIterL3muonTkCandidateSequence_cff')
process.load('HLTrigger.PhaseII.Producers.hltIterL3MuonMerged_cfi')
process.load('HLTrigger.PhaseII.Producers.hltIterL3MuonAndMuonFromL1Merged_cfi')
process.load('HLTrigger.PhaseII.Producers.hltIterL3GlbMuon_cfi')
process.load('HLTrigger.PhaseII.Producers.hltIterL3MuonsNoID_cfi')
process.load('HLTrigger.PhaseII.Producers.hltIterL3Muons_cfi')
process.load('HLTrigger.PhaseII.Producers.hltL3MuonsIterL3Links_cfi')
process.load('HLTrigger.PhaseII.Producers.hltIterL3MuonTracks_cfi')

HLTL3muonrecoNocandSequence = cms.Sequence(process.HLTIterL3muonTkCandidateSequence+process.hltIterL3MuonMerged+process.hltIterL3MuonAndMuonFromL1Merged+process.hltIterL3GlbMuon+process.hltIterL3MuonsNoID+process.hltIterL3Muons+process.hltL3MuonsIterL3Links+process.hltIterL3MuonTracks)
