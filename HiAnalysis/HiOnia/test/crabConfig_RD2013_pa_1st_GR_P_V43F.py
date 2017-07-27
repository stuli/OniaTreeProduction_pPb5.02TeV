from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.section_('General')
config.General.requestName = 'RD2013_pa_1st_GR_P_V43F_v1'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'myeffanalyzer_RD2013_pa_1st_run_210498-210658_GR_P_V43F_nocut_cfg.py'
config.JobType.outputFiles = ['RD2013_pa_1st_run_210498-210658_GR_P_V43F_nocut.root']

config.section_('Data')
config.Data.inputDataset = '/PAMuon/kyolee-pPbData_1st_SKIM_ReprocessedReco-v1_GR_P_V43F_pileupRej-v4-3fb37d130463b80cc67787287cb18f76/USER'
config.Data.inputDBS = 'phys03'
config.Data.runRange = '210498-210658'
config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions13/pPb/Prompt/Cert_210498-211631_HI_PromptReco_Collisions13_JSON_MuonPhys_v2.txt'
#config.Data.unitsPerJob = 100
#config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 2
config.Data.splitting = 'FileBased'
#NJOBS = 10  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
#config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
#config.Data.outLFNDirBase = '/store/user/%s/pAWinter13' % (getUsernameFromSiteDB())
config.Data.outLFNDirBase = '/store/user/%s/PAMuon' % (getUsernameFromSiteDB())

config.Data.publication = False
#config.Data.publication = True
#config.Data.outputDatasetTag =  config.General.requestName

config.section_('Site')
config.Site.whitelist = ['T2_KR_KNU']
config.Site.storageSite = 'T2_KR_KNU'

