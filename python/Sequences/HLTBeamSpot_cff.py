import FWCore.ParameterSet.Config as cms

from HLTrigger.PhaseII.Producers.hltScalersRawToDigi_cfi import *
from HLTrigger.PhaseII.Producers.hltOnlineBeamSpot_cfi import *

HLTBeamSpot = cms.Sequence(hltScalersRawToDigi+hltOnlineBeamSpot)
