import FWCore.ParameterSet.Config as cms

process = cms.Process("HIOnia")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('root://cms-xrd-global.cern.ch//store/group/phys_heavyions/stuli/MCpPb5TeV02/PYTHIA6_Upsilon3S_tuneD6T_5TeV02/Ups3S_tuneD6T_5TeV02/170815_222027/0000/Upsilon3S_pa_1st_run_SKIM_STARTHI53_V27-v1_102.root')
)
process.hltDblMu0 = cms.EDFilter("HLTHighLevel",
    eventSetupPathsKey = cms.string(''),
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    HLTPaths = cms.vstring('HLT_PAL1DoubleMu0_HighQ_v*'),
    throw = cms.bool(False),
    andOr = cms.bool(True)
)


process.hltDblMu3 = cms.EDFilter("HLTHighLevel",
    eventSetupPathsKey = cms.string(''),
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    HLTPaths = cms.vstring('HLT_PAL2DoubleMu3_v*'),
    throw = cms.bool(False),
    andOr = cms.bool(True)
)


process.hltDblMuOpen = cms.EDFilter("HLTHighLevel",
    eventSetupPathsKey = cms.string(''),
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    HLTPaths = cms.vstring('HLT_PAL1DoubleMuOpen_v*'),
    throw = cms.bool(False),
    andOr = cms.bool(True)
)


process.hltMu12 = cms.EDFilter("HLTHighLevel",
    eventSetupPathsKey = cms.string(''),
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    HLTPaths = cms.vstring('HLT_PAMu12_v*'),
    throw = cms.bool(False),
    andOr = cms.bool(True)
)


process.hltMu3 = cms.EDFilter("HLTHighLevel",
    eventSetupPathsKey = cms.string(''),
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    HLTPaths = cms.vstring('HLT_PAMu3_v*'),
    throw = cms.bool(False),
    andOr = cms.bool(True)
)


process.hltMu7 = cms.EDFilter("HLTHighLevel",
    eventSetupPathsKey = cms.string(''),
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    HLTPaths = cms.vstring('HLT_PAMu7_v*'),
    throw = cms.bool(False),
    andOr = cms.bool(True)
)


process.hltMult100DblMu3 = cms.EDFilter("HLTHighLevel",
    eventSetupPathsKey = cms.string(''),
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    HLTPaths = cms.vstring('HLT_PAPixelTrackMultiplicity100_L2DoubleMu3_v*'),
    throw = cms.bool(False),
    andOr = cms.bool(True)
)


process.hionia = cms.EDAnalyzer("HiOniaAnalyzer",
    fillRecoTracks = cms.bool(True),
    sglTriggerFilterNames = cms.vstring('hltL3fL2sMu3L3Filtered3', 
        'hltL3fL2sMu7L3Filtered7', 
        'hltL3fL2sMu12L3Filtered12'),
    dataSetName = cms.string('Ups3S_DataSet.root'),
    centralityRanges = cms.vdouble(20, 40, 100),
    histFileName = cms.string('Upsilon3S_tuneD6T_5TeV02.root'),
    srcTracks = cms.InputTag("generalTracks"),
    applyCuts = cms.bool(True),
    etaBinRanges = cms.vdouble(0.0, 2.5),
    minimumFlag = cms.bool(False),
    fillTree = cms.bool(True),
    isPA = cms.untracked.bool(True),
    srcMuon = cms.InputTag("patMuonsWithTrigger"),
    triggerResultsLabel = cms.InputTag("TriggerResults","","HLT"),
    removeSignalEvents = cms.untracked.bool(False),
    sglTriggerPathNames = cms.vstring('HLT_PAMu3_v1', 
        'HLT_PAMu7_v1', 
        'HLT_PAMu12_v1'),
    useRapidity = cms.bool(True),
    srcMuonNoTrig = cms.InputTag("patMuonsWithoutTrigger"),
    srcCentrality = cms.InputTag("pACentrality"),
    maxAbsZ = cms.double(24.0),
    dblTriggerPathNames = cms.vstring('HLT_PAL1DoubleMuOpen_v1', 
        'HLT_PAL1DoubleMu0_HighQ_v1', 
        'HLT_PAL2DoubleMu3_v1', 
        'HLT_PAPixelTrackMultiplicity100_L2DoubleMu3_v1'),
    storeEfficiency = cms.bool(False),
    isHI = cms.untracked.bool(False),
    combineCategories = cms.bool(False),
    storeSameSign = cms.untracked.bool(True),
    primaryVertexTag = cms.InputTag("offlinePrimaryVertices"),
    dblTriggerFilterNames = cms.vstring('hltL1fL1sPAL1DoubleMuOpenL1Filtered0', 
        'hltL1fL1sPAL1DoubleMu0HighQL1FilteredHighQ', 
        'hltL2fL1sPAL2DoubleMu3L2Filtered3', 
        'hltL2fL1sPAL2DoubleMu3L2Filtered3'),
    fillHistos = cms.bool(False),
    oniaPDG = cms.int32(200553),
    fillRooDataSet = cms.bool(False),
    genParticles = cms.InputTag("genParticles"),
    pTBinRanges = cms.vdouble(0.0, 6.0, 8.0, 9.0, 10.0, 
        12.0, 15.0, 40.0),
    fillSingleMuons = cms.bool(True),
    src = cms.InputTag("onia2MuMuPatTrkTrk"),
    isPromptMC = cms.untracked.bool(True),
    useBeamSpot = cms.bool(False),
    removeTrueMuons = cms.untracked.bool(False),
    isMC = cms.untracked.bool(True),
    muonLessPV = cms.bool(True),
    onlyTheBest = cms.bool(False)
)


process.p = cms.Path(process.hionia)


process.MessageLogger = cms.Service("MessageLogger",
    suppressInfo = cms.untracked.vstring(),
    debugs = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    suppressDebug = cms.untracked.vstring(),
    cout = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    cerr_stats = cms.untracked.PSet(
        threshold = cms.untracked.string('WARNING'),
        output = cms.untracked.string('cerr'),
        optionalPSet = cms.untracked.bool(True)
    ),
    warnings = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    default = cms.untracked.PSet(

    ),
    statistics = cms.untracked.vstring('cerr_stats'),
    cerr = cms.untracked.PSet(
        INFO = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        noTimeStamps = cms.untracked.bool(False),
        FwkReport = cms.untracked.PSet(
            reportEvery = cms.untracked.int32(100),
            optionalPSet = cms.untracked.bool(True),
            limit = cms.untracked.int32(10000000)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000)
        ),
        Root_NoDictionary = cms.untracked.PSet(
            optionalPSet = cms.untracked.bool(True),
            limit = cms.untracked.int32(0)
        ),
        threshold = cms.untracked.string('INFO'),
        FwkJob = cms.untracked.PSet(
            optionalPSet = cms.untracked.bool(True),
            limit = cms.untracked.int32(0)
        ),
        FwkSummary = cms.untracked.PSet(
            reportEvery = cms.untracked.int32(1),
            optionalPSet = cms.untracked.bool(True),
            limit = cms.untracked.int32(10000000)
        ),
        optionalPSet = cms.untracked.bool(True)
    ),
    FrameworkJobReport = cms.untracked.PSet(
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        optionalPSet = cms.untracked.bool(True),
        FwkJob = cms.untracked.PSet(
            optionalPSet = cms.untracked.bool(True),
            limit = cms.untracked.int32(10000000)
        )
    ),
    suppressWarning = cms.untracked.vstring(),
    errors = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    destinations = cms.untracked.vstring('cout', 
        'cerr'),
    debugModules = cms.untracked.vstring(),
    infos = cms.untracked.PSet(
        optionalPSet = cms.untracked.bool(True),
        Root_NoDictionary = cms.untracked.PSet(
            optionalPSet = cms.untracked.bool(True),
            limit = cms.untracked.int32(0)
        ),
        placeholder = cms.untracked.bool(True)
    ),
    categories = cms.untracked.vstring('FwkJob', 
        'FwkReport', 
        'FwkSummary', 
        'Root_NoDictionary'),
    fwkJobReports = cms.untracked.vstring('FrameworkJobReport')
)


process.CastorDbProducer = cms.ESProducer("CastorDbProducer")


process.EcalLaserCorrectionService = cms.ESProducer("EcalLaserCorrectionService")


process.SiStripRecHitMatcherESProducer = cms.ESProducer("SiStripRecHitMatcherESProducer",
    ComponentName = cms.string('StandardMatcher'),
    NSigmaInside = cms.double(3.0)
)


process.StripCPEfromTrackAngleESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('StripCPEfromTrackAngle')
)


process.hcal_db_producer = cms.ESProducer("HcalDbProducer",
    file = cms.untracked.string(''),
    dump = cms.untracked.vstring('')
)


process.siPixelQualityESProducer = cms.ESProducer("SiPixelQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(cms.PSet(
        record = cms.string('SiPixelQualityFromDbRcd'),
        tag = cms.string('')
    ), 
        cms.PSet(
            record = cms.string('SiPixelDetVOffRcd'),
            tag = cms.string('')
        ))
)


process.siStripGainESProducer = cms.ESProducer("SiStripGainESProducer",
    printDebug = cms.untracked.bool(False),
    appendToDataLabel = cms.string(''),
    APVGain = cms.VPSet(cms.PSet(
        Record = cms.string('SiStripApvGainRcd'),
        NormalizationFactor = cms.untracked.double(1.0),
        Label = cms.untracked.string('')
    ), 
        cms.PSet(
            Record = cms.string('SiStripApvGain2Rcd'),
            NormalizationFactor = cms.untracked.double(1.0),
            Label = cms.untracked.string('')
        )),
    AutomaticNormalization = cms.bool(False)
)


process.siStripLorentzAngleDepESProducer = cms.ESProducer("SiStripLorentzAngleDepESProducer",
    LatencyRecord = cms.PSet(
        record = cms.string('SiStripLatencyRcd'),
        label = cms.untracked.string('')
    ),
    LorentzAngleDeconvMode = cms.PSet(
        record = cms.string('SiStripLorentzAngleRcd'),
        label = cms.untracked.string('deconvolution')
    ),
    LorentzAnglePeakMode = cms.PSet(
        record = cms.string('SiStripLorentzAngleRcd'),
        label = cms.untracked.string('peak')
    )
)


process.siStripQualityESProducer = cms.ESProducer("SiStripQualityESProducer",
    appendToDataLabel = cms.string(''),
    PrintDebugOutput = cms.bool(False),
    ThresholdForReducedGranularity = cms.double(0.3),
    UseEmptyRunInfo = cms.bool(False),
    ReduceGranularity = cms.bool(False),
    ListOfRecordToMerge = cms.VPSet(cms.PSet(
        record = cms.string('SiStripDetVOffRcd'),
        tag = cms.string('')
    ), 
        cms.PSet(
            record = cms.string('SiStripDetCablingRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('RunInfoRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadChannelRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadFiberRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadModuleRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadStripRcd'),
            tag = cms.string('')
        ))
)


process.sistripconn = cms.ESProducer("SiStripConnectivity")


process.GlobalTag = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        enableReadOnlySessionOnUpdateConnection = cms.untracked.bool(False),
        idleConnectionCleanupPeriod = cms.untracked.int32(10),
        messageLevel = cms.untracked.int32(0),
        enablePoolAutomaticCleanUp = cms.untracked.bool(False),
        enableConnectionSharing = cms.untracked.bool(True),
        connectionRetrialTimeOut = cms.untracked.int32(60),
        connectionTimeOut = cms.untracked.int32(60),
        authenticationSystem = cms.untracked.int32(0),
        connectionRetrialPeriod = cms.untracked.int32(10)
    ),
    BlobStreamerName = cms.untracked.string('TBufferBlobStreamingService'),
    toGet = cms.VPSet(cms.PSet(
        record = cms.string('HeavyIonRcd'),
        tag = cms.string('CentralityTable_HFhits40_AMPTOrgan_v0_offline'),
        connect = cms.untracked.string('frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS'),
        label = cms.untracked.string('HFhitsAMPT_Organ')
    ), 
        cms.PSet(
            record = cms.string('HeavyIonRcd'),
            tag = cms.string('CentralityTable_PixelHits40_AMPTOrgan_v0_offline'),
            connect = cms.untracked.string('frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS'),
            label = cms.untracked.string('PixelHitsAMPT_Organ')
        ), 
        cms.PSet(
            record = cms.string('HeavyIonRcd'),
            tag = cms.string('CentralityTable_HFhits40_HydjetBass_vv44x04_mc'),
            connect = cms.untracked.string('frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS'),
            label = cms.untracked.string('HFhitsHydjet_Bass')
        ), 
        cms.PSet(
            record = cms.string('HeavyIonRcd'),
            tag = cms.string('CentralityTable_PixelHits40_HydjetBass_vv44x04_mc'),
            connect = cms.untracked.string('frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS'),
            label = cms.untracked.string('PixelHitsHydjet_Bass')
        ), 
        cms.PSet(
            record = cms.string('HeavyIonRcd'),
            tag = cms.string('CentralityTable_Tracks40_HydjetBass_vv44x04_mc'),
            connect = cms.untracked.string('frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS'),
            label = cms.untracked.string('TracksHydjet_Bass')
        ), 
        cms.PSet(
            record = cms.string('HeavyIonRcd'),
            tag = cms.string('CentralityTable_PixelTracks40_HydjetBass_vv44x04_mc'),
            connect = cms.untracked.string('frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS'),
            label = cms.untracked.string('PixelTracksHydjet_Bass')
        ), 
        cms.PSet(
            record = cms.string('HeavyIonRcd'),
            tag = cms.string('CentralityTable_HFtowers40_HydjetBass_vv44x04_mc'),
            connect = cms.untracked.string('frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS'),
            label = cms.untracked.string('HFtowersHydjet_Bass')
        ), 
        cms.PSet(
            record = cms.string('HeavyIonRcd'),
            tag = cms.string('CentralityTable_HFhits40_HydjetDrum_vv44x05_mc'),
            connect = cms.untracked.string('frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS'),
            label = cms.untracked.string('HFhitsHydjet_Drum')
        ), 
        cms.PSet(
            record = cms.string('HeavyIonRcd'),
            tag = cms.string('CentralityTable_PixelHits40_HydjetDrum_vv44x05_mc'),
            connect = cms.untracked.string('frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS'),
            label = cms.untracked.string('PixelHitsHydjet_Drum')
        ), 
        cms.PSet(
            record = cms.string('HeavyIonRcd'),
            tag = cms.string('CentralityTable_Tracks40_HydjetDrum_vv44x05_mc'),
            connect = cms.untracked.string('frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS'),
            label = cms.untracked.string('TracksHydjet_Drum')
        ), 
        cms.PSet(
            record = cms.string('HeavyIonRcd'),
            tag = cms.string('CentralityTable_PixelTracks40_HydjetDrum_vv44x05_mc'),
            connect = cms.untracked.string('frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS'),
            label = cms.untracked.string('PixelTracksHydjet_Drum')
        ), 
        cms.PSet(
            record = cms.string('HeavyIonRcd'),
            tag = cms.string('CentralityTable_HFtowers40_HydjetDrum_vv44x05_mc'),
            connect = cms.untracked.string('frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS'),
            label = cms.untracked.string('HFtowersHydjet_Drum')
        ), 
        cms.PSet(
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_AK1PFTowers_hiIterativeTracks_HI_2760GeV_v3_offline'),
            connect = cms.untracked.string('frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS'),
            label = cms.untracked.string('AK1PF_hiIterativeTracks')
        ), 
        cms.PSet(
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_AK2PFTowers_hiIterativeTracks_HI_2760GeV_v3_offline'),
            connect = cms.untracked.string('frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS'),
            label = cms.untracked.string('AK2PF_hiIterativeTracks')
        ), 
        cms.PSet(
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_AK3PFTowers_hiIterativeTracks_HI_2760GeV_v3_offline'),
            connect = cms.untracked.string('frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS'),
            label = cms.untracked.string('AK3PF_hiIterativeTracks')
        ), 
        cms.PSet(
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_AK4PFTowers_hiIterativeTracks_HI_2760GeV_v3_offline'),
            connect = cms.untracked.string('frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS'),
            label = cms.untracked.string('AK4PF_hiIterativeTracks')
        ), 
        cms.PSet(
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_AK5PFTowers_hiIterativeTracks_HI_2760GeV_v3_offline'),
            connect = cms.untracked.string('frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS'),
            label = cms.untracked.string('AK5PF_hiIterativeTracks')
        ), 
        cms.PSet(
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_AK6PFTowers_hiIterativeTracks_HI_2760GeV_v3_offline'),
            connect = cms.untracked.string('frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS'),
            label = cms.untracked.string('AK6PF_hiIterativeTracks')
        ), 
        cms.PSet(
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_HI_PythiaZ2_5TeV_538_v03_AK1Calo_offline'),
            connect = cms.untracked.string('frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS'),
            label = cms.untracked.string('AK1Calo_HI')
        ), 
        cms.PSet(
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_HI_PythiaZ2_5TeV_538_v04_AK2Calo_offline'),
            connect = cms.untracked.string('frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS'),
            label = cms.untracked.string('AK2Calo_HI')
        ), 
        cms.PSet(
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_HI_PythiaZ2_5TeV_538_v05_AK3Calo_offline'),
            connect = cms.untracked.string('frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS'),
            label = cms.untracked.string('AK3Calo_HI')
        ), 
        cms.PSet(
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_HI_PythiaZ2_5TeV_538_v05_AK4Calo_offline'),
            connect = cms.untracked.string('frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS'),
            label = cms.untracked.string('AK4Calo_HI')
        ), 
        cms.PSet(
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_HI_PythiaZ2_5TeV_538_v05_AK5Calo_offline'),
            connect = cms.untracked.string('frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS'),
            label = cms.untracked.string('AK5Calo_HI')
        ), 
        cms.PSet(
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_HI_PythiaZ2_5TeV_538_v04_AK6Calo_offline'),
            connect = cms.untracked.string('frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS'),
            label = cms.untracked.string('AK6Calo_HI')
        ), 
        cms.PSet(
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_5TeV_538_v02_AK2PF_offline'),
            connect = cms.untracked.string('frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS'),
            label = cms.untracked.string('AK1PF_generalTracks')
        ), 
        cms.PSet(
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_5TeV_538_v04_AK2PF_offline'),
            connect = cms.untracked.string('frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS'),
            label = cms.untracked.string('AK2PF_generalTracks')
        ), 
        cms.PSet(
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_5TeV_538_v05_AK3PF_offline'),
            connect = cms.untracked.string('frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS'),
            label = cms.untracked.string('AK3PF_generalTracks')
        ), 
        cms.PSet(
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_5TeV_538_v05_AK4PF_offline'),
            connect = cms.untracked.string('frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS'),
            label = cms.untracked.string('AK4PF_generalTracks')
        ), 
        cms.PSet(
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_5TeV_538_v05_AK5PF_offline'),
            connect = cms.untracked.string('frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS'),
            label = cms.untracked.string('AK5PF_generalTracks')
        ), 
        cms.PSet(
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_HI_PFTowers_generalTracks_PythiaZ2_5TeV_538_v04_AK6PF_offline'),
            connect = cms.untracked.string('frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS'),
            label = cms.untracked.string('AK6PF_generalTracks')
        ), 
        cms.PSet(
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_Fall12_V5_DATA_AK7PF'),
            connect = cms.untracked.string('frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS'),
            label = cms.untracked.string('AK7PF_generalTracks')
        ), 
        cms.PSet(
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_IC5Calo_2760GeV_v0_offline'),
            connect = cms.untracked.string('frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS'),
            label = cms.untracked.string('IC5Calo_2760GeV')
        ), 
        cms.PSet(
            record = cms.string('HeavyIonRcd'),
            tag = cms.string('CentralityTable_HFplus100_PA2012B_v533x01_offline'),
            connect = cms.untracked.string('frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS'),
            label = cms.untracked.string('HFtowersPlusTrunc')
        ), 
        cms.PSet(
            record = cms.string('HeavyIonRcd'),
            tag = cms.string('CentralityTable_Tracks100_HijingPA_v538x02_mc'),
            connect = cms.untracked.string('frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS'),
            label = cms.untracked.string('TracksHijing')
        ), 
        cms.PSet(
            record = cms.string('HeavyIonRcd'),
            tag = cms.string('CentralityTable_HFplus100_HijingPA_v538x02_mc'),
            connect = cms.untracked.string('frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS'),
            label = cms.untracked.string('HFtowersPlusTruncHijing')
        )),
    connect = cms.string('frontier://FrontierProd/CMS_COND_31X_GLOBALTAG'),
    globaltag = cms.string('STARTHI53_V27::All')
)


process.es_hardcode = cms.ESSource("HcalHardcodeCalibrations",
    toGet = cms.untracked.vstring('GainWidths')
)


process.CondDBSetup = cms.PSet(
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        enableReadOnlySessionOnUpdateConnection = cms.untracked.bool(False),
        idleConnectionCleanupPeriod = cms.untracked.int32(10),
        messageLevel = cms.untracked.int32(0),
        enablePoolAutomaticCleanUp = cms.untracked.bool(False),
        enableConnectionSharing = cms.untracked.bool(True),
        connectionRetrialTimeOut = cms.untracked.int32(60),
        connectionTimeOut = cms.untracked.int32(60),
        authenticationSystem = cms.untracked.int32(0),
        connectionRetrialPeriod = cms.untracked.int32(10)
    )
)

process.HeavyIonGlobalParameters = cms.PSet(
    centralityVariable = cms.string('HFtowersPlusTrunc'),
    centralitySrc = cms.InputTag("pACentrality"),
    pPbRunFlip = cms.untracked.uint32(211313),
    nonDefaultGlauberModel = cms.string('')
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.options = cms.untracked.PSet(
    SkipEvent = cms.untracked.vstring('ProductNotFound')
)

