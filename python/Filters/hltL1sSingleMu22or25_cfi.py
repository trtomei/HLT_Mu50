import FWCore.ParameterSet.Config as cms

hltL1sSingleMu22or25 = cms.EDFilter("HLTL1TSeed",
    L1EGammaInputTag = cms.InputTag("hltGtStage2Digis","EGamma"),
    L1EtSumInputTag = cms.InputTag("hltGtStage2Digis","EtSum"),
    L1GlobalInputTag = cms.InputTag("hltGtStage2Digis"),
    L1JetInputTag = cms.InputTag("hltGtStage2Digis","Jet"),
    L1MuonInputTag = cms.InputTag("hltGtStage2Digis","Muon"),
    L1ObjectMapInputTag = cms.InputTag("hltGtStage2ObjectMap"),
    L1SeedsLogicalExpression = cms.string('L1_SingleMu22 OR L1_SingleMu25'),
    L1TauInputTag = cms.InputTag("hltGtStage2Digis","Tau"),
    saveTags = cms.bool(True)
)
