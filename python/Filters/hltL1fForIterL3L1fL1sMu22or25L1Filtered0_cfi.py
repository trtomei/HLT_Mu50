import FWCore.ParameterSet.Config as cms

hltL1fForIterL3L1fL1sMu22or25L1Filtered0 = cms.EDFilter("HLTMuonL1TFilter",
    CandTag = cms.InputTag("hltL1MuonsPt0"),
    CentralBxOnly = cms.bool(True),
    MaxEta = cms.double(2.5),
    MinN = cms.int32(1),
    MinPt = cms.double(0.0),
    PreviousCandTag = cms.InputTag("hltL1fL1sMu22or25L1Filtered0"),
    SelectQualities = cms.vint32(),
    saveTags = cms.bool(True)
)
