import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/00764D7D-7806-E411-BD7C-0025905A6094.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/04FEC3A5-7A06-E411-8128-0025905A60CE.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/0600887E-7A06-E411-9B50-003048FF9AA6.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/062FC08F-7A06-E411-A483-0026189438BC.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/08942ED8-7A06-E411-A327-00261894398A.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/08A0D662-7806-E411-A0D3-00261894393F.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/0C5F46E7-7A06-E411-84B6-0025905A612E.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/0C6704AE-7A06-E411-BD98-0025905B85AE.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/0CC1DF7F-7806-E411-A9DA-002590593902.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/0CE75C8F-7A06-E411-A156-002590593878.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/24FE6674-7A06-E411-A8EC-003048D15E40.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/2AC31A78-7A06-E411-A4C4-002590596486.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/2C0346E7-7A06-E411-B8FE-0025905A612E.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/2CA5DF79-7A06-E411-96C9-003048FF86CA.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/2E3C01A1-7A06-E411-BBA8-0025905A6090.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/3023EFA8-7806-E411-8DCB-0025905A6092.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/30D4A539-7B06-E411-BA33-0025905A607E.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/32219477-7806-E411-A846-0025905A60B6.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/3235E986-7806-E411-BC5D-003048FFCC2C.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/36FF2778-7A06-E411-96D0-0025905A60B8.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/3A9ECCA8-7A06-E411-9EAC-003048FFCBA8.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/3EEFE0A0-7806-E411-9472-0025905A48F2.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/4424A7AC-7A06-E411-B208-0025905A60CA.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/44847A7B-7806-E411-B482-0025905A48BA.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/46399683-7A06-E411-8444-002618FDA259.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/50BD26F6-7A06-E411-8178-002618943857.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/5A5246E7-7A06-E411-8259-0025905A612E.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/622271F8-7A06-E411-9A96-00261894398B.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/663545C7-7A06-E411-8AC8-0025905A60FE.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/6691F97A-7A06-E411-AD1A-0026189437EC.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/68B30889-7A06-E411-9B84-002354EF3BE2.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/6EAB9E79-7806-E411-A36A-0025905A6066.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/728E7E74-7A06-E411-AC9C-00261894389E.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/74469D7F-7806-E411-970B-0025905A609E.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/78909A78-7A06-E411-AA79-00261894387C.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/863009D9-7A06-E411-A2F4-002618943934.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/8879DE9C-7806-E411-8241-0025905A497A.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/88CD448B-7A06-E411-98B9-00259059642E.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/8AF2BAED-7A06-E411-9FAC-002618943807.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/8C2089E5-7A06-E411-A725-0025905A605E.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/8C43D37F-7806-E411-A29B-003048FFCB84.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/8CAC1974-7A06-E411-A25E-0025905A609E.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/947AC1A7-7806-E411-BBE7-0025905A4964.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/96EBD881-7806-E411-98BB-0025905A6082.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/9A6C00A1-7A06-E411-BB4A-0025905A6090.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/9EF3CFE1-7A06-E411-8C68-003048FFCBA8.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/A0154599-7A06-E411-97FC-0025905A6088.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/A812BF6C-7806-E411-9AA0-0025905A606A.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/A8948D83-7A06-E411-A608-0025905B85E8.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/ACB44F86-7806-E411-8C60-0025905A60D6.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/B8B03EB5-7A06-E411-8EC9-0025905A6088.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/BC15A876-7806-E411-AF03-003048FFCB6A.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/BE2EC1A4-7A06-E411-977F-0025905A608C.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/CE763691-7A06-E411-9B8D-0025905A6066.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/D6D97BC4-7806-E411-8E2A-002590596490.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/D6F94D7D-7806-E411-99AB-0025905A6094.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/DEEA1F67-7806-E411-9D5C-00261894393A.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/ECE8E595-7C06-E411-AE40-003048FFD75C.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/F4061171-7806-E411-80E6-002618FDA28E.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/F4C5C2D7-7806-E411-894D-0025905AA9F0.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/F6A13133-7B06-E411-A9BC-0025905A60F8.root',
       '/store/mc/Spring14miniaod/QCD_Pt-170to300_Tune4C_13TeV_pythia8/MINIAODSIM/castor_PU20bx25_POSTLS170_V5-v1/00000/FCFEE5A0-7806-E411-808B-0025905A48F2.root' ] );


secFiles.extend( [
               ] )


