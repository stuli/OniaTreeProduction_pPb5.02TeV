from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.section_('General')
config.General.requestName = 'MCPsi2SWithFSR_pa_1st_run_GENOLNY_v1'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'myaccanalyzer_MCPsi2SWithFSR_pa_1st_run_STARTHI53_V27_cfg.py'
config.JobType.outputFiles = ['MCPsi2SWithFSR_pa_1st_run_STARTHI53_V27_GENONLY.root']

config.section_('Data')
config.Data.inputDataset = '/Psi2SWithFSR_tuneD6T_5TeV02_nofilter/pAWinter13-1stRunGENOnly_STARTHI53_V27-v2/GEN'
config.Data.inputDBS = 'global'
#config.Data.inputDBS = 'phys03'
#config.Data.unitsPerJob = 100
config.Data.unitsPerJob = 1
config.Data.splitting = 'FileBased'
#NJOBS = 10  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
#config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
#config.Data.outLFNDirBase = '/store/user/%s/pAWinter13/%s' % (getUsernameFromSiteDB(), config.General.requestName)
config.Data.outLFNDirBase = '/store/user/%s/pAWinter13ext1' % (getUsernameFromSiteDB())

config.Data.publication = False
#config.Data.publication = True
#config.Data.outputDatasetTag =  config.General.requestName

config.section_('Site')
#config.Site.whitelist = ['T2_KR_KNU']
config.Site.storageSite = 'T2_KR_KNU'

