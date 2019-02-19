import FWCore.ParameterSet.Config as cms

process.load('HLTrigger.PhaseII.Producers.hltMuonDTDigis_cfi')
process.load('HLTrigger.PhaseII.Producers.hltDt1DRecHits_cfi')
process.load('HLTrigger.PhaseII.Producers.hltDt4DSegments_cfi')
process.load('HLTrigger.PhaseII.Producers.hltMuonCSCDigis_cfi')
process.load('HLTrigger.PhaseII.Producers.hltCsc2DRecHits_cfi')
process.load('HLTrigger.PhaseII.Producers.hltCscSegments_cfi')
process.load('HLTrigger.PhaseII.Producers.hltMuonRPCDigis_cfi')
process.load('HLTrigger.PhaseII.Producers.hltRpcRecHits_cfi')

HLTMuonLocalRecoSequence = cms.Sequence(process.hltMuonDTDigis+process.hltDt1DRecHits+process.hltDt4DSegments+process.hltMuonCSCDigis+process.hltCsc2DRecHits+process.hltCscSegments+process.hltMuonRPCDigis+process.hltRpcRecHits)
