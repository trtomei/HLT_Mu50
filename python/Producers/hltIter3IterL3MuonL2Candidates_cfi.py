import FWCore.ParameterSet.Config as cms

hltIter3IterL3MuonL2Candidates = cms.EDProducer("ConcreteChargedCandidateProducer",
    particleType = cms.string('mu+'),
    src = cms.InputTag("hltL2SelectorForL3IO")
)
