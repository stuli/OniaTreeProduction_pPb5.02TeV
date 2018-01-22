from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.section_('General')
config.General.requestName = 'Analyzer_Ups3S_PbP_5TeV02'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'hioniaanalyzer3S_PbP_cfg.py'
config.JobType.outputFiles = ['Upsilon3S_PbP_5TeV02.root']   # match with primary output file in crabCofig

config.section_('Data')
config.Data.inputDataset = '/Upsilon3S_PbP_5p02-Pythia8/stuli-SKIM_Upsilon3S_PbP_5TeV02-c33dc9ac7d7d0e1f5eed45ebf52f99b5/USER'
#config.Data.inputDataset = '/Upsilon3S_PbP_5p02-Pythia8/stuli-Upsilon3S_PbP_5TeV02-c33dc9ac7d7d0e1f5eed45ebf52f99b5/USER'  # Get dataset name from skim crab output
config.Data.inputDBS = 'phys03'   # from DAS dbs instance:   prod/
config.Data.unitsPerJob = 1
#NJOBS = 10  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
#config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.splitting = 'FileBased'
#config.Data.outLFNDirBase = '/store/user/%s/pAWinter13/%s' % (getUsernameFromSiteDB(), config.General.requestName)
config.Data.outLFNDirBase = '/store/group/phys_heavyions/stuli/MCpPb5TeV02'
#'/store/user/%s/pAWinter13ext1' % (getUsernameFromSiteDB())
#config.Data.publication = False
config.Data.publication = False   # False for Analyser
#config.Data.outputDatasetTag =  config.General.requestName

config.section_('Site')
#config.Site.whitelist = ['T2_KR_KNU']
config.Site.storageSite = 'T2_CH_CERN'

# If your site is blacklisted by crab, use:
# config.Data.ignoreLocality = True
# config.Site.whitelist = ["T2_FR*"]
