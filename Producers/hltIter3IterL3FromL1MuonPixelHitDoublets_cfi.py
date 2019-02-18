import FWCore.ParameterSet.Config as cms

hltIter3IterL3FromL1MuonPixelHitDoublets = cms.EDProducer("HitPairEDProducer",
    clusterCheck = cms.InputTag("hltIter3IterL3FromL1MuonPixelClusterCheck"),
    layerPairs = cms.vuint32(0),
    maxElement = cms.uint32(0),
    produceIntermediateHitDoublets = cms.bool(False),
    produceSeedingHitSets = cms.bool(True),
    seedingLayers = cms.InputTag("hltIter3IterL3FromL1MuonPixelLayerPairs"),
    trackingRegions = cms.InputTag("hltIter3IterL3FromL1MuonTrackingRegions"),
    trackingRegionsSeedingLayers = cms.InputTag("")
)
