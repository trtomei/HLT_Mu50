import FWCore.ParameterSet.Config as cms

from HLTrigger.PhaseII.Sequences.HLTMuonLocalRecoSequence_cff import *
from HLTrigger.PhaseII.Producers.hltL2OfflineMuonSeeds_cfi import *
from HLTrigger.PhaseII.Producers.hltL2MuonSeeds_cfi import *
from HLTrigger.PhaseII.Producers.hltL2Muons_cfi import *

HLTL2muonrecoNocandSequence = cms.Sequence(HLTMuonLocalRecoSequence+hltL2OfflineMuonSeeds+hltL2MuonSeeds+hltL2Muons)
