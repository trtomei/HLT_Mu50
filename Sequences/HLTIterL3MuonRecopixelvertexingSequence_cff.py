import FWCore.ParameterSet.Config as cms

process.load('HLTrigger.PhaseII.Sequences.HLTIterL3MuonRecoPixelTracksSequence_cff')
process.load('HLTrigger.PhaseII.Producers.hltIterL3MuonPixelVertices_cfi')
process.load('HLTrigger.PhaseII.Producers.hltIterL3MuonTrimmedPixelVertices_cfi')

HLTIterL3MuonRecopixelvertexingSequence = cms.Sequence(process.HLTIterL3MuonRecoPixelTracksSequence+process.hltIterL3MuonPixelVertices+process.hltIterL3MuonTrimmedPixelVertices)
