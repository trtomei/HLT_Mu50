import FWCore.ParameterSet.Config as cms

from HLTrigger.PhaseII.Producers.hltSiPixelDigis_cfi import *
from HLTrigger.PhaseII.Producers.hltSiPixelClusters_cfi import *
from HLTrigger.PhaseII.Producers.hltSiPixelClustersCache_cfi import *
from HLTrigger.PhaseII.Producers.hltSiPixelRecHits_cfi import *

HLTDoLocalPixelSequence = cms.Sequence(hltSiPixelDigis+hltSiPixelClusters+hltSiPixelClustersCache+hltSiPixelRecHits)
