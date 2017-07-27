from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.section_('General')
config.General.requestName = 'MCinclBtoJPsiMuMu_pa_1st_run_ext1_v2'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'myeffanalyzer_MCinclBtoJPsiMuMu_pa_1st_run_STARTHI53_V27_ext1_nocut_cfg.py'
config.JobType.outputFiles = ['MCinclBtoJPsiMuMu_pa_1st_run_STARTHI53_V27_ext1_nocut.root']

config.section_('Data')
config.Data.inputDataset = '/inclBtoJPsiMuMu_5TeV02/kyolee-inclBtoJPsiMuMu_pa_1st_run_SKIM_STARTHI53_V27_ext1_v1-146ccb073f655aee96fcd8c006c87b7c/USER'
#config.Data.inputDBS = 'global'
config.Data.inputDBS = 'phys03'
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
config.Site.whitelist = ['T2_KR_KNU']
config.Site.storageSite = 'T2_KR_KNU'

