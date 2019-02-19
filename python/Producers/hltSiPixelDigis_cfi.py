import FWCore.ParameterSet.Config as cms

hltSiPixelDigis = cms.EDProducer("SiPixelRawToDigi",
    CablingMapLabel = cms.string(''),
    ErrorList = cms.vint32(29),
    IncludeErrors = cms.bool(True),
    InputLabel = cms.InputTag("rawDataCollector"),
    Regions = cms.PSet(

    ),
    Timing = cms.untracked.bool(False),
    UsePhase1 = cms.bool(True),
    UsePilotBlade = cms.bool(False),
    UseQualityInfo = cms.bool(False),
    UserErrorList = cms.vint32()
)
