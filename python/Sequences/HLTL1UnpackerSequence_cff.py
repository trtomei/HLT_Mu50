import FWCore.ParameterSet.Config as cms

from HLTrigger.PhaseII.Producers.hltGtStage2Digis_cfi import *
from HLTrigger.PhaseII.Producers.hltGtStage2ObjectMap_cfi import *

HLTL1UnpackerSequence = cms.Sequence(hltGtStage2Digis+hltGtStage2ObjectMap)
