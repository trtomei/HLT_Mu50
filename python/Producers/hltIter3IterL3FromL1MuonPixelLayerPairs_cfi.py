import FWCore.ParameterSet.Config as cms

hltIter3IterL3FromL1MuonPixelLayerPairs = cms.EDProducer("SeedingLayersEDProducer",
    BPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        hitErrorRPhi = cms.double(0.0027),
        hitErrorRZ = cms.double(0.006),
        skipClusters = cms.InputTag("hltIter3IterL3FromL1MuonClustersRefRemoval"),
        useErrorsFromParam = cms.bool(True)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        hitErrorRPhi = cms.double(0.0051),
        hitErrorRZ = cms.double(0.0036),
        skipClusters = cms.InputTag("hltIter3IterL3FromL1MuonClustersRefRemoval"),
        useErrorsFromParam = cms.bool(True)
    ),
    MTEC = cms.PSet(

    ),
    MTIB = cms.PSet(

    ),
    MTID = cms.PSet(

    ),
    MTOB = cms.PSet(

    ),
    TEC = cms.PSet(

    ),
    TIB = cms.PSet(

    ),
    TID = cms.PSet(

    ),
    TOB = cms.PSet(

    ),
    layerList = cms.vstring(
        'BPix1+BPix2', 
        'BPix1+BPix3', 
        'BPix1+BPix4', 
        'BPix2+BPix3', 
        'BPix2+BPix4', 
        'BPix3+BPix4', 
        'BPix1+FPix1_pos', 
        'BPix1+FPix1_neg', 
        'BPix1+FPix2_pos', 
        'BPix1+FPix2_neg', 
        'BPix1+FPix3_pos', 
        'BPix1+FPix3_neg', 
        'BPix2+FPix1_pos', 
        'BPix2+FPix1_neg', 
        'BPix2+FPix2_pos', 
        'BPix2+FPix2_neg', 
        'BPix3+FPix1_pos', 
        'BPix3+FPix1_neg', 
        'FPix1_pos+FPix2_pos', 
        'FPix1_neg+FPix2_neg', 
        'FPix1_pos+FPix3_pos', 
        'FPix1_neg+FPix3_neg', 
        'FPix2_pos+FPix3_pos', 
        'FPix2_neg+FPix3_neg'
    )
)
