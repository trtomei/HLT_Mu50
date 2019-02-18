import FWCore.ParameterSet.Config as cms

process.load('HLTrigger.PhaseII.Producers.hltSiPixelDigis_cfi')
process.load('HLTrigger.PhaseII.Producers.hltSiPixelClusters_cfi')
process.load('HLTrigger.PhaseII.Producers.hltSiPixelClustersCache_cfi')
process.load('HLTrigger.PhaseII.Producers.hltSiPixelRecHits_cfi')

HLTDoLocalPixelSequence = cms.Sequence(process.hltSiPixelDigis+process.hltSiPixelClusters+process.hltSiPixelClustersCache+process.hltSiPixelRecHits)
