import FWCore.ParameterSet.Config as cms

hltIter3IterL3MuonTrackSelectionHighPurity = cms.EDProducer("TrackCollectionFilterCloner",
    copyExtras = cms.untracked.bool(True),
    copyTrajectories = cms.untracked.bool(False),
    minQuality = cms.string('highPurity'),
    originalMVAVals = cms.InputTag("hltIter3IterL3MuonTrackCutClassifier","MVAValues"),
    originalQualVals = cms.InputTag("hltIter3IterL3MuonTrackCutClassifier","QualityMasks"),
    originalSource = cms.InputTag("hltIter3IterL3MuonCtfWithMaterialTracks")
)
