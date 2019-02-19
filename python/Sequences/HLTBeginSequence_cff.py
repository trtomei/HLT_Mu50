import FWCore.ParameterSet.Config as cms

from HLTrigger.PhaseII.Filters.hltTriggerType_cfi import *
from HLTrigger.PhaseII.Sequences.HLTL1UnpackerSequence_cff import *
from HLTrigger.PhaseII.Sequences.HLTBeamSpot_cff import *

HLTBeginSequence = cms.Sequence(hltTriggerType+HLTL1UnpackerSequence+HLTBeamSpot)
