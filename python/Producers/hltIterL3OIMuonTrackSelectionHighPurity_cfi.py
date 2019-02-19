import FWCore.ParameterSet.Config as cms

hltIterL3OIMuonTrackSelectionHighPurity = cms.EDProducer("TrackCollectionFilterCloner",
    copyExtras = cms.untracked.bool(True),
    copyTrajectories = cms.untracked.bool(False),
    minQuality = cms.string('highPurity'),
    originalMVAVals = cms.InputTag("hltIterL3OIMuonTrackCutClassifier","MVAValues"),
    originalQualVals = cms.InputTag("hltIterL3OIMuonTrackCutClassifier","QualityMasks"),
    originalSource = cms.InputTag("hltIterL3OIMuCtfWithMaterialTracks")
)
