import FWCore.ParameterSet.Config as cms

process.load('HLTrigger.PhaseII.Sequences.HLTIterL3MuonRecopixelvertexingSequence_cff')
process.load('HLTrigger.PhaseII.Sequences.HLTIterativeTrackingIter023ForIterL3Muon_cff')
process.load('HLTrigger.PhaseII.Producers.hltL3MuonsIterL3IO_cfi')

HLTIterL3IOmuonTkCandidateSequence = cms.Sequence(process.HLTIterL3MuonRecopixelvertexingSequence+process.HLTIterativeTrackingIter023ForIterL3Muon+process.hltL3MuonsIterL3IO)
