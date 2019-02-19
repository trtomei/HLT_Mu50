import FWCore.ParameterSet.Config as cms

from HLTrigger.PhaseII.Filters.hltBoolEnd_cfi import *

HLTEndSequence = cms.Sequence(hltBoolEnd)
