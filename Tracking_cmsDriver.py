# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step3 --conditions auto:phase2_realistic -n 10 --era Phase2 --eventcontent RECOSIM,DQM --runUnscheduled -s RAW2DIGI,RECO:reconstruction_trackingOnly,VALIDATION:@trackingOnlyValidation,DQM:@trackingOnlyDQM --datatier GEN-SIM-RECO,DQMIO --geometry Extended2023D21 --filein file:step2.root --fileout file:step3.root
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('RECOHLT',eras.Phase2)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2023D21Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.Validation_cff')
process.load('DQMOffline.Configuration.DQMOfflineMC_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
#    input = cms.untracked.int32(1000)
    input = cms.untracked.int32(100)
)

process.MessageLogger = cms.Service( "MessageLogger",
    suppressInfo = cms.untracked.vstring(  ),
    debugs = cms.untracked.PSet( 
      threshold = cms.untracked.string( "INFO" ),
      placeholder = cms.untracked.bool( True ),
      suppressInfo = cms.untracked.vstring(  ),
      suppressWarning = cms.untracked.vstring(  ),
      suppressDebug = cms.untracked.vstring(  ),
      suppressError = cms.untracked.vstring(  )
    ),
    suppressDebug = cms.untracked.vstring(  ),
    cout = cms.untracked.PSet(  placeholder = cms.untracked.bool( True ) ),
    cerr_stats = cms.untracked.PSet( 
      threshold = cms.untracked.string( "WARNING" ),
      output = cms.untracked.string( "cerr" ),
      optionalPSet = cms.untracked.bool( True )
    ),
    warnings = cms.untracked.PSet( 
      threshold = cms.untracked.string( "INFO" ),
      placeholder = cms.untracked.bool( True ),
      suppressInfo = cms.untracked.vstring(  ),
      suppressWarning = cms.untracked.vstring(  ),
      suppressDebug = cms.untracked.vstring(  ),
      suppressError = cms.untracked.vstring(  )
    ),
    statistics = cms.untracked.vstring( 'cerr' ),
    cerr = cms.untracked.PSet( 
      INFO = cms.untracked.PSet(  limit = cms.untracked.int32( 0 ) ),
      noTimeStamps = cms.untracked.bool( False ),
      FwkReport = cms.untracked.PSet( 
        reportEvery = cms.untracked.int32( 1 ),
        limit = cms.untracked.int32( 0 )
      ),
      default = cms.untracked.PSet(  limit = cms.untracked.int32( 10000000 ) ),
      Root_NoDictionary = cms.untracked.PSet(  limit = cms.untracked.int32( 0 ) ),
      FwkJob = cms.untracked.PSet(  limit = cms.untracked.int32( 0 ) ),
      FwkSummary = cms.untracked.PSet( 
        reportEvery = cms.untracked.int32( 1 ),
        limit = cms.untracked.int32( 10000000 )
      ),
      threshold = cms.untracked.string( "INFO" ),
      suppressInfo = cms.untracked.vstring(  ),
      suppressWarning = cms.untracked.vstring(  ),
      suppressDebug = cms.untracked.vstring(  ),
      suppressError = cms.untracked.vstring(  )
    ),
    FrameworkJobReport = cms.untracked.PSet( 
      default = cms.untracked.PSet(  limit = cms.untracked.int32( 0 ) ),
      FwkJob = cms.untracked.PSet(  limit = cms.untracked.int32( 10000000 ) )
    ),
    suppressWarning = cms.untracked.vstring( 'hltOnlineBeamSpot',
      'hltCtf3HitL1SeededWithMaterialTracks',
      'hltL3MuonsOIState',
      'hltPixelTracksForHighMult',
      'hltHITPixelTracksHE',
      'hltHITPixelTracksHB',
      'hltCtfL1SeededWithMaterialTracks',
      'hltRegionalTracksForL3MuonIsolation',
      'hltSiPixelClusters',
      'hltActivityStartUpElectronPixelSeeds',
      'hltLightPFTracks',
      'hltPixelVertices3DbbPhi',
      'hltL3MuonsIOHit',
      'hltPixelTracks',
      'hltSiPixelDigis',
      'hltL3MuonsOIHit',
      'hltL1SeededElectronGsfTracks',
      'hltL1SeededStartUpElectronPixelSeeds',
      'hltBLifetimeRegionalCtfWithMaterialTracksbbPhiL1FastJetFastPV',
      'hltCtfActivityWithMaterialTracks' ),
    errors = cms.untracked.PSet( 
      threshold = cms.untracked.string( "INFO" ),
      placeholder = cms.untracked.bool( True ),
      suppressInfo = cms.untracked.vstring(  ),
      suppressWarning = cms.untracked.vstring(  ),
      suppressDebug = cms.untracked.vstring(  ),
      suppressError = cms.untracked.vstring(  )
    ),
    fwkJobReports = cms.untracked.vstring( 'FrameworkJobReport' ),
    debugModules = cms.untracked.vstring(  ),
    infos = cms.untracked.PSet( 
      threshold = cms.untracked.string( "INFO" ),
      Root_NoDictionary = cms.untracked.PSet(  limit = cms.untracked.int32( 0 ) ),
      placeholder = cms.untracked.bool( True ),
      suppressInfo = cms.untracked.vstring(  ),
      suppressWarning = cms.untracked.vstring(  ),
      suppressDebug = cms.untracked.vstring(  ),
      suppressError = cms.untracked.vstring(  )
    ),
    categories = cms.untracked.vstring( 'FwkJob',
      'FwkReport',
      'FwkSummary',
      'Root_NoDictionary' ),
    destinations = cms.untracked.vstring( 'warnings',
      'errors',
      'infos',
      'debugs',
      'cout',
      'cerr' ),
    threshold = cms.untracked.string( "INFO" ),
    suppressError = cms.untracked.vstring( 'hltOnlineBeamSpot',
      'hltL3MuonCandidates',
      'hltL3TkTracksFromL2OIState',
      'hltPFJetCtfWithMaterialTracks',
      'hltL3TkTracksFromL2IOHit',
      'hltL3TkTracksFromL2OIHit' )
)
if 'MessageLogger' in process.__dict__:
    process.MessageLogger.categories.append('TriggerSummaryProducerAOD')
    process.MessageLogger.categories.append('L1GtTrigReport')
    process.MessageLogger.categories.append('L1TGlobalSummary')
    process.MessageLogger.categories.append('HLTrigReport')
    process.MessageLogger.categories.append('FastReport')



# enable the TrigReport and TimeReport
process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool( True )
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
"/store/mc/PhaseIIMTDTDRAutumn18DR/TTbar_14TeV_TuneCP5_Pythia8/FEVT/PU200_103X_upgrade2023_realistic_v2-v1/80000/9F184E96-958D-774B-8242-CEB1F61F7505.root",
"/store/mc/PhaseIIMTDTDRAutumn18DR/TTbar_14TeV_TuneCP5_Pythia8/FEVT/PU200_103X_upgrade2023_realistic_v2-v1/80000/A56961F4-A999-F041-87EC-B0B3AE7BC451.root",
"/store/mc/PhaseIIMTDTDRAutumn18DR/TTbar_14TeV_TuneCP5_Pythia8/FEVT/PU200_103X_upgrade2023_realistic_v2-v1/80000/1A45B5C4-5E39-2C40-878A-4954D178D762.root",
"/store/mc/PhaseIIMTDTDRAutumn18DR/TTbar_14TeV_TuneCP5_Pythia8/FEVT/PU200_103X_upgrade2023_realistic_v2-v1/80000/362E2A03-9819-7B4B-9AD1-0F1544A6B16D.root",
"/store/mc/PhaseIIMTDTDRAutumn18DR/TTbar_14TeV_TuneCP5_Pythia8/FEVT/PU200_103X_upgrade2023_realistic_v2-v1/80000/061E6A7D-DAFA-EA45-86DD-C8504E7C3A24.root",
"/store/mc/PhaseIIMTDTDRAutumn18DR/TTbar_14TeV_TuneCP5_Pythia8/FEVT/PU200_103X_upgrade2023_realistic_v2-v1/80000/32AEB5C3-B03C-E942-A28B-458834BE9E94.root",
"/store/mc/PhaseIIMTDTDRAutumn18DR/TTbar_14TeV_TuneCP5_Pythia8/FEVT/PU200_103X_upgrade2023_realistic_v2-v1/80000/981A067C-A5E7-5841-B181-3F9FB6BE2669.root",
"/store/mc/PhaseIIMTDTDRAutumn18DR/TTbar_14TeV_TuneCP5_Pythia8/FEVT/PU200_103X_upgrade2023_realistic_v2-v1/80000/8E79E006-C866-8F47-835A-E9F0B542CB05.root",
"/store/mc/PhaseIIMTDTDRAutumn18DR/TTbar_14TeV_TuneCP5_Pythia8/FEVT/PU200_103X_upgrade2023_realistic_v2-v1/80000/44384221-A552-864B-96DB-839C3E21C364.root",
"/store/mc/PhaseIIMTDTDRAutumn18DR/TTbar_14TeV_TuneCP5_Pythia8/FEVT/PU200_103X_upgrade2023_realistic_v2-v1/80000/0D298922-5C0F-2C4F-92E8-551996C83542.root",
"/store/mc/PhaseIIMTDTDRAutumn18DR/TTbar_14TeV_TuneCP5_Pythia8/FEVT/PU200_103X_upgrade2023_realistic_v2-v1/80000/A6BF9985-734E-8C42-A3AC-5A1618D2D22B.root",
"/store/mc/PhaseIIMTDTDRAutumn18DR/TTbar_14TeV_TuneCP5_Pythia8/FEVT/PU200_103X_upgrade2023_realistic_v2-v1/80000/39DD6BEE-A61F-F146-89C1-C6FC0768D9DA.root",
"/store/mc/PhaseIIMTDTDRAutumn18DR/TTbar_14TeV_TuneCP5_Pythia8/FEVT/PU200_103X_upgrade2023_realistic_v2-v1/80000/1E659E87-3DEE-6F4E-9C2F-B3CCDA1175BA.root",
"/store/mc/PhaseIIMTDTDRAutumn18DR/TTbar_14TeV_TuneCP5_Pythia8/FEVT/PU200_103X_upgrade2023_realistic_v2-v1/80000/8026FE38-21CF-524C-9637-30A7ED936BA4.root",
"/store/mc/PhaseIIMTDTDRAutumn18DR/TTbar_14TeV_TuneCP5_Pythia8/FEVT/PU200_103X_upgrade2023_realistic_v2-v1/80000/5879A635-DC63-7F40-85C3-748C55C2D917.root",
"/store/mc/PhaseIIMTDTDRAutumn18DR/TTbar_14TeV_TuneCP5_Pythia8/FEVT/PU200_103X_upgrade2023_realistic_v2-v1/80000/9C05CC03-62F6-C141-8BEF-5D2D7A3671F0.root",
"/store/mc/PhaseIIMTDTDRAutumn18DR/TTbar_14TeV_TuneCP5_Pythia8/FEVT/PU200_103X_upgrade2023_realistic_v2-v1/80000/275C4478-D59A-2143-BC3F-734AED7FD085.root",
"/store/mc/PhaseIIMTDTDRAutumn18DR/TTbar_14TeV_TuneCP5_Pythia8/FEVT/PU200_103X_upgrade2023_realistic_v2-v1/80000/C4A1A7F5-55FA-E143-9258-781785307922.root",

#"/store/mc/PhaseIIMTDTDRAutumn18DR/TTbar_TuneCP5_14TeV_pythia8/FEVT/NoPU_103X_upgrade2023_realistic_v2-v1/120000/95A036AE-8749-AA4A-9A66-317E93BDE806.root",
#"/store/mc/PhaseIIMTDTDRAutumn18DR/TTbar_TuneCP5_14TeV_pythia8/FEVT/NoPU_103X_upgrade2023_realistic_v2-v1/120000/C35175A9-E2B7-9C4B-BE1D-F6AD194BA88A.root",
#"/store/mc/PhaseIIMTDTDRAutumn18DR/TTbar_TuneCP5_14TeV_pythia8/FEVT/NoPU_103X_upgrade2023_realistic_v2-v1/120000/7EEA54C7-B5C6-7A4B-A1F4-33DD7AE52C2E.root",
    ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step3 nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RECO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:step3.root'),
    outputCommands = process.RECOSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

process.DQMoutput = cms.OutputModule("DQMRootOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('DQMIO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:step3_inDQM.root'),
    outputCommands = process.DQMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.mix.playback = True
process.mix.digitizers = cms.PSet()
for a in process.aliases: delattr(process, a)
process.RandomNumberGeneratorService.restoreStateLabel=cms.untracked.string("randomEngineStateProducer")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic', '')
print process.GlobalTag.globaltag

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.reconstruction_step = cms.Path(process.reconstruction_trackingOnly)

#process.reconstruction_step = cms.Path(cms.Task(process.HGCalRecHit, process.HGCalUncalibRecHit, process.MeasurementTrackerEventPreSplitting, process.bunchSpacingProducer, process.csc2DRecHits, process.cscSegments, process.ctppsDiamondLocalTracks, process.ctppsDiamondRecHits, process.ctppsLocalTrackLiteProducer, process.ctppsPixelClusters, process.ctppsPixelLocalTracks, process.ctppsPixelRecHits, process.dt1DCosmicRecHits, process.dt1DRecHits, process.dt4DCosmicSegments, process.dt4DSegments, process.ecalCompactTrigPrim, process.ecalDetIdToBeRecovered, process.ecalMultiFitUncalibRecHit, process.ecalPreshowerRecHit, process.ecalRecHit, process.ecalTPSkim, process.gemRecHits, process.gemSegments, process.hbhereco, process.hfprereco, process.hfreco, process.hgcalLayerClusters, process.hgcalMultiClusters, process.horeco, process.me0RecHits, process.me0Segments, process.offlineBeamSpot, process.particleFlowClusterHGCal, process.particleFlowClusterHGCalFromMultiCl, process.particleFlowRecHitHGC, process.rpcNewRecHits, process.rpcRecHits, process.siPixelClusterShapeCachePreSplitting, process.totemRPClusterProducer, process.totemRPLocalTrackFitter, process.totemRPRecHitProducer, process.totemRPUVPatternFinder, process.totemTimingRecHits, process.trackExtrapolator, process.zdcreco), cms.Task(process.MeasurementTrackerEvent, process.ak4CaloJetsForTrk, process.ancientMuonSeed, process.caloTowerForTrk, process.clusterSummaryProducer, process.convClusters, process.convLayerPairs, process.convStepSelector, process.convStepTracks, process.convTrackCandidates, process.conversionStepTracks, process.dedxHarmonic2, process.dedxHitInfo, process.dedxPixelAndStripHarmonic2T085, process.dedxPixelHarmonic2, process.dedxTruncated40, process.detachedQuadStep, process.detachedQuadStepClusters, process.detachedQuadStepHitDoublets, process.detachedQuadStepHitQuadruplets, process.detachedQuadStepSeedLayers, process.detachedQuadStepSeeds, process.detachedQuadStepSelector, process.detachedQuadStepTrackCandidates, process.detachedQuadStepTrackingRegions, process.detachedQuadStepTracks, process.displacedMuonSeeds, process.displacedStandAloneMuons, process.duplicateTrackCandidates, process.duplicateTrackClassifier, process.earlyGeneralTracks, process.earlyMuons, process.firstStepPrimaryVertices, process.firstStepPrimaryVerticesUnsorted, process.generalTracks, process.generalV0Candidates, process.highPtTripletStepClusters, process.highPtTripletStepHitDoublets, process.highPtTripletStepHitTriplets, process.highPtTripletStepSeedClusterMask, process.highPtTripletStepSeedLayers, process.highPtTripletStepSeeds, process.highPtTripletStepSelector, process.highPtTripletStepTrackCandidates, process.highPtTripletStepTrackingRegions, process.highPtTripletStepTracks, process.inclusiveSecondaryVertices, process.inclusiveVertexFinder, process.initialStepHitDoublets, process.initialStepHitQuadruplets, process.initialStepSeedClusterMask, process.initialStepSeedLayers, process.initialStepSeeds, process.initialStepSelector, process.initialStepTrackCandidates, process.initialStepTrackRefsForJets, process.initialStepTrackingRegions, process.initialStepTracks, process.lowPtQuadStepClusters, process.lowPtQuadStepHitDoublets, process.lowPtQuadStepHitQuadruplets, process.lowPtQuadStepSeedLayers, process.lowPtQuadStepSeeds, process.lowPtQuadStepSelector, process.lowPtQuadStepTrackCandidates, process.lowPtQuadStepTrackingRegions, process.lowPtQuadStepTracks, process.lowPtTripletStepClusters, process.lowPtTripletStepHitDoublets, process.lowPtTripletStepHitTriplets, process.lowPtTripletStepSeedLayers, process.lowPtTripletStepSeeds, process.lowPtTripletStepSelector, process.lowPtTripletStepTrackCandidates, process.lowPtTripletStepTrackingRegions, process.lowPtTripletStepTracks, process.mergedDuplicateTracks, process.muonSeededSeedsInOut, process.muonSeededSeedsOutIn, process.muonSeededTrackCandidatesInOut, process.muonSeededTrackCandidatesOutIn, process.muonSeededTracksInOut, process.muonSeededTracksInOutSelector, process.muonSeededTracksOutIn, process.muonSeededTracksOutInSelector, process.newCombinedSeeds, process.offlinePrimaryVertices, process.offlinePrimaryVerticesWithBS, process.photonConvTrajSeedFromSingleLeg, process.pixelPairStepClusters, process.pixelPairStepHitDoublets, process.pixelPairStepSeedClusterMask, process.pixelPairStepSeedLayers, process.pixelPairStepSeeds, process.pixelPairStepSelector, process.pixelPairStepTrackCandidates, process.pixelPairStepTrackingRegions, process.pixelPairStepTracks, process.preDuplicateMergingGeneralTracks, process.refittedStandAloneMuons, process.siPhase2Clusters, process.siPixelClusterShapeCache, process.siPixelClusters, process.siPixelClustersPreSplitting, process.siPixelRecHits, process.siPixelRecHitsPreSplitting, process.standAloneMuons, process.trackRefsForJetsBeforeSorting, process.trackVertexArbitrator, process.trackWithVertexRefSelectorBeforeSorting, process.trackerClusterCheck, process.tripletElectronHitDoublets, process.tripletElectronHitTriplets, process.tripletElectronSeedLayers, process.tripletElectronSeeds, process.tripletElectronTrackingRegions, process.unsortedOfflinePrimaryVertices, process.vertexMerger))

process.reconstruction_step = cms.Path(cms.Task(process.MeasurementTrackerEvent, process.ak4CaloJetsForTrk, process.ancientMuonSeed, process.caloTowerForTrk, process.clusterSummaryProducer, process.convClusters, process.convLayerPairs, process.convStepSelector, process.convStepTracks, process.convTrackCandidates, process.conversionStepTracks, process.dedxHarmonic2, process.dedxHitInfo, process.dedxPixelAndStripHarmonic2T085, process.dedxPixelHarmonic2, process.dedxTruncated40, process.detachedQuadStep, process.detachedQuadStepClusters, process.detachedQuadStepHitDoublets, process.detachedQuadStepHitQuadruplets, process.detachedQuadStepSeedLayers, process.detachedQuadStepSeeds, process.detachedQuadStepSelector, process.detachedQuadStepTrackCandidates, process.detachedQuadStepTrackingRegions, process.detachedQuadStepTracks, process.displacedMuonSeeds, process.displacedStandAloneMuons, process.duplicateTrackCandidates, process.duplicateTrackClassifier, process.earlyGeneralTracks, process.earlyMuons, process.firstStepPrimaryVertices, process.firstStepPrimaryVerticesUnsorted, process.generalTracks, process.generalV0Candidates, process.highPtTripletStepClusters, process.highPtTripletStepHitDoublets, process.highPtTripletStepHitTriplets, process.highPtTripletStepSeedClusterMask, process.highPtTripletStepSeedLayers, process.highPtTripletStepSeeds, process.highPtTripletStepSelector, process.highPtTripletStepTrackCandidates, process.highPtTripletStepTrackingRegions, process.highPtTripletStepTracks, process.inclusiveSecondaryVertices, process.inclusiveVertexFinder, process.initialStepHitDoublets, process.initialStepHitQuadruplets, process.initialStepSeedClusterMask, process.initialStepSeedLayers, process.initialStepSeeds, process.initialStepSelector, process.initialStepTrackCandidates, process.initialStepTrackRefsForJets, process.initialStepTrackingRegions, process.initialStepTracks, process.lowPtQuadStepClusters, process.lowPtQuadStepHitDoublets, process.lowPtQuadStepHitQuadruplets, process.lowPtQuadStepSeedLayers, process.lowPtQuadStepSeeds, process.lowPtQuadStepSelector, process.lowPtQuadStepTrackCandidates, process.lowPtQuadStepTrackingRegions, process.lowPtQuadStepTracks, process.lowPtTripletStepClusters, process.lowPtTripletStepHitDoublets, process.lowPtTripletStepHitTriplets, process.lowPtTripletStepSeedLayers, process.lowPtTripletStepSeeds, process.lowPtTripletStepSelector, process.lowPtTripletStepTrackCandidates, process.lowPtTripletStepTrackingRegions, process.lowPtTripletStepTracks, process.mergedDuplicateTracks, process.muonSeededSeedsInOut, process.muonSeededSeedsOutIn, process.muonSeededTrackCandidatesInOut, process.muonSeededTrackCandidatesOutIn, process.muonSeededTracksInOut, process.muonSeededTracksInOutSelector, process.muonSeededTracksOutIn, process.muonSeededTracksOutInSelector, process.newCombinedSeeds, process.offlinePrimaryVertices, process.offlinePrimaryVerticesWithBS, process.photonConvTrajSeedFromSingleLeg, process.pixelPairStepClusters, process.pixelPairStepHitDoublets, process.pixelPairStepSeedClusterMask, process.pixelPairStepSeedLayers, process.pixelPairStepSeeds, process.pixelPairStepSelector, process.pixelPairStepTrackCandidates, process.pixelPairStepTrackingRegions, process.pixelPairStepTracks, process.preDuplicateMergingGeneralTracks, process.refittedStandAloneMuons, process.siPhase2Clusters, process.siPixelClusterShapeCache, process.siPixelClusters, process.siPixelClustersPreSplitting, process.siPixelRecHits, process.siPixelRecHitsPreSplitting, process.standAloneMuons, process.trackRefsForJetsBeforeSorting, process.trackVertexArbitrator, process.trackWithVertexRefSelectorBeforeSorting, process.trackerClusterCheck, process.tripletElectronHitDoublets, process.tripletElectronHitTriplets, process.tripletElectronSeedLayers, process.tripletElectronSeeds, process.tripletElectronTrackingRegions, process.unsortedOfflinePrimaryVertices, process.vertexMerger))

process.prevalidation_step = cms.Path(process.globalPrevalidationTrackingOnly)
process.validation_step = cms.EndPath(process.globalValidationTrackingOnly)
process.dqmoffline_step = cms.EndPath(process.DQMOfflineTracking)
process.dqmofflineOnPAT_step = cms.EndPath(process.PostDQMOffline)
process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)
process.DQMoutput_step = cms.EndPath(process.DQMoutput)


process.hltTrigReport = cms.EDAnalyzer( "HLTrigReport",
    ReferencePath = cms.untracked.string( "HLTriggerFinalPath" ),
    ReferenceRate = cms.untracked.double( 100.0 ),
    serviceBy = cms.untracked.string( "never" ),
    resetBy = cms.untracked.string( "never" ),
    reportBy = cms.untracked.string( "job" ),
    HLTriggerResults = cms.InputTag( 'TriggerResults','','RECOHLT' )
)
process.hltTriggerSummaryAOD = cms.EDProducer( "TriggerSummaryProducerAOD",
    processName = cms.string( "@" )
)
process.hltTriggerSummaryRAW = cms.EDProducer( "TriggerSummaryProducerRAW",
    processName = cms.string( "@" )
)
process.hltBoolFalse = cms.EDFilter( "HLTBool",
    result = cms.bool( False )
)
process.HLTriggerFinalPath = cms.Path( process.hltTriggerSummaryAOD + process.hltTriggerSummaryRAW + process.hltBoolFalse )
process.HLTAnalyzerEndpath = cms.EndPath( process.hltTrigReport )


process.dqmoffline_step.remove(process.KshortWlxy16)
process.dqmoffline_step.remove(process.KshortWlxy16MonitoringCommon)
process.dqmoffline_step.remove(process.LambdaWlxy16)
process.dqmoffline_step.remove(process.LambdaWlxy16MonitoringCommon)
process.dqmoffline_step.remove(process.TrackSplitMonitor)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.reconstruction_step,process.prevalidation_step,process.validation_step,process.dqmoffline_step,process.HLTriggerFinalPath,process.DQMoutput_step,process.HLTAnalyzerEndpath)
#process.schedule = cms.Schedule(process.raw2digi_step,process.reconstruction_step,process.prevalidation_step,process.validation_step,process.dqmoffline_step,process.dqmofflineOnPAT_step,process.RECOSIMoutput_step,process.DQMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from SimGeneral.MixingModule.fullMixCustomize_cff
from SimGeneral.MixingModule.fullMixCustomize_cff import setCrossingFrameOn 

#call to customisation function setCrossingFrameOn imported from SimGeneral.MixingModule.fullMixCustomize_cff
process = setCrossingFrameOn(process)

# End of customisation functions
#do not add changes to your config after this point (unless you know what you are doing)
from FWCore.ParameterSet.Utilities import convertToUnscheduled
process=convertToUnscheduled(process)


# Customisation from command line

#Have logErrorHarvester wait for the same EDProducers to finish as those providing data for the OutputModule
from FWCore.Modules.logErrorHarvester_cff import customiseLogErrorHarvesterUsingOutputCommands
process = customiseLogErrorHarvesterUsingOutputCommands(process)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion


#print getattr(process,"AK8PFHT750_TrimMass50_Mjjmonitoring")
#
#from HLTrigger.Configuration.common import *
#print producers_by_type(process,"HTMonitor")



