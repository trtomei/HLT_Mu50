import FWCore.ParameterSet.Config as cms

from HLTrigger.PhaseII.Sequences.HLTL2muonrecoNocandSequence_cff import *
from HLTrigger.PhaseII.Producers.hltL2MuonCandidates_cfi import *

HLTL2muonrecoSequence = cms.Sequence(HLTL2muonrecoNocandSequence+hltL2MuonCandidates)
