import FWCore.ParameterSet.Config as cms

from HLTrigger.PhaseII.Producers.hltMuonDTDigis_cfi import *
from HLTrigger.PhaseII.Producers.hltDt1DRecHits_cfi import *
from HLTrigger.PhaseII.Producers.hltDt4DSegments_cfi import *
from HLTrigger.PhaseII.Producers.hltMuonCSCDigis_cfi import *
from HLTrigger.PhaseII.Producers.hltCsc2DRecHits_cfi import *
from HLTrigger.PhaseII.Producers.hltCscSegments_cfi import *
from HLTrigger.PhaseII.Producers.hltMuonRPCDigis_cfi import *
from HLTrigger.PhaseII.Producers.hltRpcRecHits_cfi import *

HLTMuonLocalRecoSequence = cms.Sequence(hltMuonDTDigis+hltDt1DRecHits+hltDt4DSegments+hltMuonCSCDigis+hltCsc2DRecHits+hltCscSegments+hltMuonRPCDigis+hltRpcRecHits)
