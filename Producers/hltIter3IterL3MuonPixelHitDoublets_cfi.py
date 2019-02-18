import FWCore.ParameterSet.Config as cms

hltIter3IterL3MuonPixelHitDoublets = cms.EDProducer("HitPairEDProducer",
    clusterCheck = cms.InputTag("hltIter3IterL3MuonPixelClusterCheck"),
    layerPairs = cms.vuint32(0),
    maxElement = cms.uint32(0),
    produceIntermediateHitDoublets = cms.bool(False),
    produceSeedingHitSets = cms.bool(True),
    seedingLayers = cms.InputTag("hltIter3IterL3MuonPixelLayerPairs"),
    trackingRegions = cms.InputTag("hltIter3IterL3MuonTrackingRegions"),
    trackingRegionsSeedingLayers = cms.InputTag("")
)
