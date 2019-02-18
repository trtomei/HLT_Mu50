import FWCore.ParameterSet.Config as cms

process.load('HLTrigger.PhaseII.Producers.hltSiStripExcludedFEDListProducer_cfi')
process.load('HLTrigger.PhaseII.Producers.hltSiStripRawToClustersFacility_cfi')
process.load('HLTrigger.PhaseII.Producers.hltSiStripClusters_cfi')

HLTDoLocalStripSequence = cms.Sequence(process.hltSiStripExcludedFEDListProducer+process.hltSiStripRawToClustersFacility+process.hltSiStripClusters)
