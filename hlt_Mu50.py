import FWCore.ParameterSet.Config as cms

process.load('HLTrigger.PhaseII.Sequences.HLTBeginSequence_cff')
process.load('HLTrigger.PhaseII.Filters.hltL1sSingleMu22or25_cfi')
process.load('HLTrigger.PhaseII.Filters.hltPreMu50_cfi')
process.load('HLTrigger.PhaseII.Filters.hltL1fL1sMu22or25L1Filtered0_cfi')
process.load('HLTrigger.PhaseII.Sequences.HLTL2muonrecoSequence_cff')
process.load('HLTrigger.PhaseII.Filters.hltL2fL1sMu22or25L1f0L2Filtered10Q_cfi')
process.load('HLTrigger.PhaseII.Sequences.HLTL3muonrecoSequence_cff')
process.load('HLTrigger.PhaseII.Filters.hltL1fForIterL3L1fL1sMu22or25L1Filtered0_cfi')
process.load('HLTrigger.PhaseII.Filters.hltL3fL1sMu22Or25L1f0L2f10QL3Filtered50Q_cfi')
process.load('HLTrigger.PhaseII.Sequences.HLTEndSequence_cff')

process.HLT_Mu50_v13 = cms.Path(process.HLTBeginSequence+process.hltL1sSingleMu22or25+process.hltPreMu50+process.hltL1fL1sMu22or25L1Filtered0+process.HLTL2muonrecoSequence+cms.ignore(process.hltL2fL1sMu22or25L1f0L2Filtered10Q)+process.HLTL3muonrecoSequence+cms.ignore(process.hltL1fForIterL3L1fL1sMu22or25L1Filtered0)+process.hltL3fL1sMu22Or25L1f0L2f10QL3Filtered50Q+process.HLTEndSequence)
