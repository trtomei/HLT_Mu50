import FWCore.ParameterSet.Config as cms

process.load('HLTrigger.PhaseII.Sequences.HLTIterL3OImuonTkCandidateSequence_cff')
process.load('HLTrigger.PhaseII.Producers.hltIterL3OIL3MuonsLinksCombination_cfi')
process.load('HLTrigger.PhaseII.Producers.hltIterL3OIL3Muons_cfi')
process.load('HLTrigger.PhaseII.Producers.hltIterL3OIL3MuonCandidates_cfi')
process.load('HLTrigger.PhaseII.Producers.hltL2SelectorForL3IO_cfi')
process.load('HLTrigger.PhaseII.Sequences.HLTIterL3IOmuonTkCandidateSequence_cff')
process.load('HLTrigger.PhaseII.Producers.hltIterL3MuonsFromL2LinksCombination_cfi')

HLTIterL3OIAndIOFromL2muonTkCandidateSequence = cms.Sequence(process.HLTIterL3OImuonTkCandidateSequence+process.hltIterL3OIL3MuonsLinksCombination+process.hltIterL3OIL3Muons+process.hltIterL3OIL3MuonCandidates+process.hltL2SelectorForL3IO+process.HLTIterL3IOmuonTkCandidateSequence+process.hltIterL3MuonsFromL2LinksCombination)