import FWCore.ParameterSet.Config as cms

from HLTrigger.PhaseII.Sequences.HLTL3muonrecoNocandSequence_cff import *
from HLTrigger.PhaseII.Producers.hltIterL3MuonCandidates_cfi import *

HLTL3muonrecoSequence = cms.Sequence(HLTL3muonrecoNocandSequence+hltIterL3MuonCandidates)
