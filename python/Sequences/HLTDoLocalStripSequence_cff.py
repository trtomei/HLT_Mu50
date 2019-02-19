import FWCore.ParameterSet.Config as cms

from HLTrigger.PhaseII.Producers.hltSiStripExcludedFEDListProducer_cfi import *
from HLTrigger.PhaseII.Producers.hltSiStripRawToClustersFacility_cfi import *
from HLTrigger.PhaseII.Producers.hltSiStripClusters_cfi import *

HLTDoLocalStripSequence = cms.Sequence(hltSiStripExcludedFEDListProducer+hltSiStripRawToClustersFacility+hltSiStripClusters)
