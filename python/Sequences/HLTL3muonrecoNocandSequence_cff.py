import FWCore.ParameterSet.Config as cms

from HLTrigger.PhaseII.Sequences.HLTIterL3muonTkCandidateSequence_cff import *
from HLTrigger.PhaseII.Producers.hltIterL3MuonMerged_cfi import *
from HLTrigger.PhaseII.Producers.hltIterL3MuonAndMuonFromL1Merged_cfi import *
from HLTrigger.PhaseII.Producers.hltIterL3GlbMuon_cfi import *
from HLTrigger.PhaseII.Producers.hltIterL3MuonsNoID_cfi import *
from HLTrigger.PhaseII.Producers.hltIterL3Muons_cfi import *
from HLTrigger.PhaseII.Producers.hltL3MuonsIterL3Links_cfi import *
from HLTrigger.PhaseII.Producers.hltIterL3MuonTracks_cfi import *

HLTL3muonrecoNocandSequence = cms.Sequence(HLTIterL3muonTkCandidateSequence+hltIterL3MuonMerged+hltIterL3MuonAndMuonFromL1Merged+hltIterL3GlbMuon+hltIterL3MuonsNoID+hltIterL3Muons+hltL3MuonsIterL3Links+hltIterL3MuonTracks)
