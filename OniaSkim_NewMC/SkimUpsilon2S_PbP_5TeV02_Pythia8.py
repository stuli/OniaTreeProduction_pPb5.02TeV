# for the list of used tags please see:
# https://twiki.cern.ch/twiki/bin/view/CMS/Onia2MuMuSamples

import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

# set up process
process = cms.Process("Onia2MuMuPAT")

# setup 'analysis'  options
options = VarParsing.VarParsing ('analysis')

# setup any defaults you want
options.outputFile = 'Upsilon2S_pa_PbP_SKIM_STARTHI53_V27-v1.root' # 2015 : 2M
#options.outputFile = 'Upsilon2S_PbP_SKIM_5TeV02_Pythia8.root' # 2015 : 2M
#options.inputFile = 'root://cms-xrd-global.cern.ch//store/himc/HiWinter13/PYTHIA6_Upsilon1SWithFSR_tuneD6T_5TeV02/GEN-SIM-RECO/pa_STARTHI53_V27-v1/00000/0074FA10-CB57-E311-9C9C-00A0D1EE8F64.root'
options.inputFiles = 'root://cms-xrd-global.cern.ch//store/himc/pAWinter13DR53X/Upsilon2S_PbP_5p02-Pythia8/GEN-SIM-RECO/pa_PbP_STARTHI53_V27-v1/50000/04269711-87E4-E711-B3FF-0CC47A703326.root'


options.maxEvents = -1 # -1 means all events

# get and parse the command line arguments
options.parseArguments()

process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load("Configuration.StandardSequences.Reconstruction_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
#process.GlobalTag.globaltag = 'STARTHI53_V17::All'
process.GlobalTag.globaltag = 'STARTHI53_V27::All'

# Common offline event selection
process.load("HeavyIonsAnalysis.Configuration.collisionEventSelection_cff")

# pile up rejection
process.load('Appeltel.RpPbAnalysis.PAPileUpVertexFilter_cff')

# Centrality for pPb
process.load('RecoHI.HiCentralityAlgos.HiCentrality_cfi')

# HLT dimuon trigger
import HLTrigger.HLTfilters.hltHighLevel_cfi
process.hltOniaHI = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltOniaHI.HLTPaths = ["HLT_PAL1DoubleMuOpen_v*",
                              "HLT_PAL1DoubleMu0_HighQ_v*",
                              "HLT_PAL2DoubleMu3_v*",
                              "HLT_PAMu3_v*",
                              "HLT_PAMu7_v*",
                              "HLT_PAMu12_v*",
#Santona
                              "HLT_PAPixelTrackMultiplicity100_L2DoubleMu3_v*"
                              ]
process.hltOniaHI.throw = False
process.hltOniaHI.andOr = True
process.hltOniaHI.TriggerResultsTag = cms.InputTag("TriggerResults","","HLT")


from HiSkim.HiOnia2MuMu.onia2MuMuPAT_cff import *
onia2MuMuPAT(process, GlobalTag=process.GlobalTag.globaltag, MC=True, HLT="HLT", Filter=False)
process.onia2MuMuPatTrkTrk.dimuonMassMin = cms.double(6.0)
process.onia2MuMuPatTrkTrk.dimuonMassMax = cms.double(20.0)

#process.onia2MuMuPatTrkTrk.addMuonlessPrimaryVertex = False
#process.onia2MuMuPatTrkTrk.resolvePileUpAmbiguity = False

## don't filter on good vertex here, do it in the skimming step on the PV closest to onia in Delta Z
#process.PAcollisionEventSelection = cms.Sequence(process.hfCoincFilter *
#                                                 #process.PAprimaryVertexFilter *
#                                                 process.NoScraping
#                                                 )

process.patMuonSequence = cms.Sequence(
#    process.hltOniaHI *
    process.PAcollisionEventSelection *
    process.pileupVertexFilterCutGplus * 
    process.pACentrality_step *
    process.genMuons *
    process.patMuonsWithTriggerSequence
    )

process.source.duplicateCheckMode = cms.untracked.string('noDuplicateCheck')
process.source.fileNames = cms.untracked.vstring(
    options.inputFiles
    )

# filter on lumisections
#from HiSkim.HiOnia2MuMu.goodLumiSectionListHI_cfi import *
#process.source.lumisToProcess = goodLumisToProcess

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(options.maxEvents) )
process.outOnia2MuMu.fileName = cms.untracked.string( options.outputFile )

process.e = cms.EndPath(process.outOnia2MuMu)

process.schedule = cms.Schedule(process.Onia2MuMuPAT,process.e)

