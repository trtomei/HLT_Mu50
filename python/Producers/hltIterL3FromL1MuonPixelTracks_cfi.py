import FWCore.ParameterSet.Config as cms

hltIterL3FromL1MuonPixelTracks = cms.EDProducer("PixelTrackProducer",
    Cleaner = cms.string('hltPixelTracksCleanerBySharedHits'),
    Filter = cms.InputTag("hltIterL3MuonPixelTracksFilter"),
    Fitter = cms.InputTag("hltIterL3MuonPixelTracksFitter"),
    SeedingHitSets = cms.InputTag("hltIterL3FromL1MuonPixelTracksHitQuadruplets"),
    passLabel = cms.string('')
)
