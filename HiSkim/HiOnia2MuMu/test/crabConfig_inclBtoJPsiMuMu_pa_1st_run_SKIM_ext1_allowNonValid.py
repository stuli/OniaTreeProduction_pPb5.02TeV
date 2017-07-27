from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.section_('General')
config.General.requestName = 'inclBtoJPsiMuMu_pa_1st_run_SKIM_STARTHI53_V27_ext1_v1'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'inclBtoJPsiMuMu_pa_1st_run_SKIM_STARTHI53_V27_cfg.py'
config.JobType.outputFiles = ['inclBtoJPsiMuMu_pa_1st_run_SKIM_STARTHI53_V27_ext1.root']

config.section_('Data')
config.Data.allowNonValidInputDataset= True # When status=PRODUCTION
config.Data.inputDataset = '/inclBtoJPsiMuMu_5TeV02/pAWinter13DR53X-pa_1st_run_STARTHI53_V27_ext1-v1/GEN-SIM-RECO'
config.Data.inputDBS = 'global'
config.Data.unitsPerJob = 1
#NJOBS = 10  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
#config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.splitting = 'FileBased'
#config.Data.outLFNDirBase = '/store/user/%s/pAWinter13/%s' % (getUsernameFromSiteDB(), config.General.requestName)
config.Data.outLFNDirBase = '/store/user/%s/pAWinter13ext1' % (getUsernameFromSiteDB())
#config.Data.publication = False
config.Data.publication = True
config.Data.outputDatasetTag =  config.General.requestName

config.section_('Site')
#config.Site.whitelist = ['T2_KR_KNU']
config.Site.storageSite = 'T2_KR_KNU'

# If your site is blacklisted by crab, use:
# config.Data.ignoreLocality = True
# config.Site.whitelist = ["T2_FR*"]
