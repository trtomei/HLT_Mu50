import FWCore.ParameterSet.Config as cms

process.load('HLTrigger.PhaseII.Producers.hltIterL3OISeedsFromL2Muons_cfi')
process.load('HLTrigger.PhaseII.Producers.hltIterL3OITrackCandidates_cfi')
process.load('HLTrigger.PhaseII.Producers.hltIterL3OIMuCtfWithMaterialTracks_cfi')
process.load('HLTrigger.PhaseII.Producers.hltIterL3OIMuonTrackCutClassifier_cfi')
process.load('HLTrigger.PhaseII.Producers.hltIterL3OIMuonTrackSelectionHighPurity_cfi')
process.load('HLTrigger.PhaseII.Producers.hltL3MuonsIterL3OI_cfi')

HLTIterL3OImuonTkCandidateSequence = cms.Sequence(process.hltIterL3OISeedsFromL2Muons+process.hltIterL3OITrackCandidates+process.hltIterL3OIMuCtfWithMaterialTracks+process.hltIterL3OIMuonTrackCutClassifier+process.hltIterL3OIMuonTrackSelectionHighPurity+process.hltL3MuonsIterL3OI)
