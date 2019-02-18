import FWCore.ParameterSet.Config as cms

process.load('HLTrigger.PhaseII.Sequences.HLTDoLocalPixelSequence_cff')
process.load('HLTrigger.PhaseII.Sequences.HLTDoLocalStripSequence_cff')
process.load('HLTrigger.PhaseII.Sequences.HLTIterL3OIAndIOFromL2muonTkCandidateSequence_cff')
process.load('HLTrigger.PhaseII.Producers.hltL1MuonsPt0_cfi')
process.load('HLTrigger.PhaseII.Sequences.HLTIterL3IOmuonFromL1TkCandidateSequence_cff')

HLTIterL3muonTkCandidateSequence = cms.Sequence(process.HLTDoLocalPixelSequence+process.HLTDoLocalStripSequence+process.HLTIterL3OIAndIOFromL2muonTkCandidateSequence+process.hltL1MuonsPt0+process.HLTIterL3IOmuonFromL1TkCandidateSequence)
