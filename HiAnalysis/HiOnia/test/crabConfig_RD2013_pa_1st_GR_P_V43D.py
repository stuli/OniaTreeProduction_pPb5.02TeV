from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.section_('General')
config.General.requestName = 'RD2013_pa_1st_GR_P_V43D_v4'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'myeffanalyzer_RD2013_pa_1st_run_210676-211256_GR_P_V43D_nocut_cfg.py'
config.JobType.outputFiles = ['RD2013_pa_1st_run_210676-211256_GR_P_V43D_nocut.root']

config.section_('Data')
config.Data.inputDataset = '/PAMuon/kyolee-pPbData_1st_SKIM_PromptReco-v1_GR_P_V43D_pileupRej-f8e1476788d2eda648cb01596b343346/USER' 
config.Data.inputDBS = 'phys03'
config.Data.runRange = '210676-211256'
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

