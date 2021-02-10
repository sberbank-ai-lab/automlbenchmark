import report.config as config
import os

config.renamed_frameworks = dict(
    constantpredictor_enc='constantpredictor'
)
config.excluded_frameworks = []

# config.impute_missing_with = 'constantpredictor'

RESULTS_PATH = '/home/rinchin/PycharmProjects/automlbenchmark/results'

all_results_files = {    
    '1h':map(
        lambda x: os.path.join(RESULTS_PATH, x, 'scores/results.csv'), 
        [
            # ============================ constantpredictor ============================
            'constantpredictor_small_1h8c_docker_20201011T144418', # small            
            'constantpredictor_medium_1h8c_docker_20201017T235950', # medium
        
            # ============================ RF ============================ 
            'randomforest_small_1h8c_docker_20201015T231526', # small
            'randomforest_medium_1h8c_docker_20201017T235935', # medium
            'randomforest_168329_1h8c_local_20201215T120753', # helena
            
            # ============================ lightautoml 0.2.8 ============================
            # SMALL
            'lightautoml_146818_1h8c_docker_20201218T110454', # Australian 146818

#             'lightautoml_10101_1h8c_docker_20201218T113400', # blood-transfusion 10101
            'lightautoml_10101_1h8c_docker_20201220T211915',
            'lightautoml_10101_1h8c_docker_20201220T210955',
            'lightautoml_10101_1h8c_docker_20201220T210959',
            'lightautoml_10101_1h8c_docker_20201220T211430',
            'lightautoml_10101_1h8c_docker_20201220T210757',
            'lightautoml_10101_1h8c_docker_20201220T202613',
            'lightautoml_10101_1h8c_docker_20201220T202603',
            'lightautoml_10101_1h8c_docker_20201220T202623',
            'lightautoml_10101_1h8c_docker_20201220T202618',
            'lightautoml_10101_1h8c_docker_20201220T202608',
            
            'lightautoml_146821_1h8c_docker_20201218T110533', # car 146821
            'lightautoml_168908_1h8c_docker_20201218T113054', # christine 168908
            'lightautoml_9981_1h8c_docker_20201218T113114', # cnae-9 9981
            'lightautoml_31_1h8c_docker_20201218T113459', # credit-g 31
            'lightautoml_168909_1h8c_docker_20201218T113539', # dilbert 168909
            'lightautoml_168910_1h8c_docker_20201212T223246', # fabert 168910
            'lightautoml_168911_1h8c_docker_20201212T223224', # jasmine 168911

#             'lightautoml_3917_1h8c_docker_20201211T235411', # kc1 3917
            'lightautoml_3917_1h8c_docker_20201220T212650',
            'lightautoml_3917_1h8c_docker_20201220T212712',
            'lightautoml_3917_1h8c_docker_20201220T212510',
            'lightautoml_3917_1h8c_docker_20201220T212436',
            'lightautoml_3917_1h8c_docker_20201220T212419',
            'lightautoml_3917_1h8c_docker_20201220T202728',
            'lightautoml_3917_1h8c_docker_20201220T202733',
            'lightautoml_3917_1h8c_docker_20201220T202723',
            'lightautoml_3917_1h8c_docker_20201220T202719',            
            
            'lightautoml_3_1h8c_docker_20201211T235334', # kr-vs-kp 3
            'lightautoml_12_1h8c_docker_20201211T235356', # mfeat-factors 12
            'lightautoml_9952_1h8c_docker_20201212T223200', # phoneme 9952
            'lightautoml_146822_1h8c_docker_20201211T235434', # segment 146822
            'lightautoml_168912_1h8c_docker_20201218T023055', # sylvine 168912
            'lightautoml_53_1h8c_docker_20201218T112614', # vehicle 53

            # MEDIUM
#             'lightautoml_7592_1h8c_docker_20201218T112558', # adult 7592
            'lightautoml_7592_1h8c_docker_20201220T212124',
            'lightautoml_7592_1h8c_docker_20201220T212114',
            'lightautoml_7592_1h8c_docker_20201220T212129',
            'lightautoml_7592_1h8c_docker_20201220T212044',
            'lightautoml_7592_1h8c_docker_20201220T212019',
            'lightautoml_7592_1h8c_docker_20201220T202442',
            'lightautoml_7592_1h8c_docker_20201220T202447',
            'lightautoml_7592_1h8c_docker_20201220T202432',
            'lightautoml_7592_1h8c_docker_20201220T202452',
            'lightautoml_7592_1h8c_docker_20201220T202437',

            'lightautoml_34539_1h8c_docker_20201218T112536', # Amazon_employee_access 34539
            'lightautoml_168868_1h8c_docker_20201218T022317', # APSFailure 168868
            'lightautoml_14965_1h8c_docker_20201218T023006', # bank-marketing 14965
            'lightautoml_146195_1h8c_docker_20201218T113711', # connect-4 146195
            
#             'lightautoml_146825_1h8c_docker_20201218T114010', # Fashion-MNIST 146825
            'lightautoml_146825_1h8c_docker_20201220T202548',
            'lightautoml_146825_1h8c_docker_20201220T202538',
            'lightautoml_146825_1h8c_docker_20201220T202543',
            'lightautoml_146825_1h8c_docker_20201220T202528',
            'lightautoml_146825_1h8c_docker_20201220T202533',
            'lightautoml_146825_1h8c_docker_20201220T210140',
            'lightautoml_146825_1h8c_docker_20201220T210105',
            'lightautoml_146825_1h8c_docker_20201220T210151',
            'lightautoml_146825_1h8c_docker_20201220T205934',
            'lightautoml_146825_1h8c_docker_20201220T210027',            
            
            'lightautoml_168337_1h8c_docker_20201218T113635', # guillermo 168337
            'lightautoml_168329_1h8c_docker_20201218T022944', # Helena 168329
            'lightautoml_146606_1h8c_docker_20201218T022933', # higgs 146606
            'lightautoml_168330_1h8c_docker_20201218T022913', # Jannis 168330
            'lightautoml_167119_1h8c_docker_20201218T113855', # jungle_chess_2pcs_raw_endgame_complete 167119
            'lightautoml_3945_1h8c_docker_20201218T131641', # KDDCup09_appetency 3945
            'lightautoml_168335_1h8c_docker_20201218T022755', # MiniBooNE 168335
            'lightautoml_9977_1h8c_docker_20201218T022726', # nomao 9977
            'lightautoml_167120_1h8c_docker_20201218T022711', # numerai28.6 | 167120
            'lightautoml_168338_1h8c_docker_20201212T223341', # riccardo 168338
            'lightautoml_168332_1h8c_docker_20201218T022640', # Robert 168332
            'lightautoml_146212_1h8c_docker_20201218T022304', # Shuttle 146212
            'lightautoml_168331_1h8c_docker_20201218T022602', # Volkert 168331
            
            # LARGE
            # 189354
            'lightautoml_189354_1h8c_docker_20210202T112310',
            'lightautoml_189354_1h8c_docker_20210202T112330',
            'lightautoml_189354_1h8c_docker_20210202T112345',
            'lightautoml_189354_1h8c_docker_20210202T112340',
            'lightautoml_189354_1h8c_docker_20210202T112320',
            'lightautoml_189354_1h8c_docker_20210202T112335',
            'lightautoml_189354_1h8c_docker_20210202T112350',
            'lightautoml_189354_1h8c_docker_20210202T112315',
            'lightautoml_189354_1h8c_docker_20210202T112325',
            'lightautoml_189354_1h8c_docker_20210202T112305',

            # Albert 189356
            'lightautoml_189356_1h8c_docker_20210208T100407',
            'lightautoml_189356_1h8c_docker_20210208T104422',
            'lightautoml_189356_1h8c_docker_20210208T104113',
            'lightautoml_189356_1h8c_docker_20210208T104126',
            'lightautoml_189356_1h8c_docker_20210208T105436',
#             '',
            'lightautoml_189356_1h8c_docker_20210208T113529',
            'lightautoml_189356_1h8c_docker_20210208T113434',
            'lightautoml_189356_1h8c_docker_20210208T113553',
            
            # Covertype 7593
            'lightautoml_7593_1h8c_docker_20210203T105337',
            'lightautoml_7593_1h8c_docker_20210203T105332',
            'lightautoml_7593_1h8c_docker_20210203T105317',
            'lightautoml_7593_1h8c_docker_20210203T105322',
            'lightautoml_7593_1h8c_docker_20210203T105402',
            'lightautoml_7593_1h8c_docker_20210203T105347',
            'lightautoml_7593_1h8c_docker_20210203T105357',
            'lightautoml_7593_1h8c_docker_20210203T105352',
            'lightautoml_7593_1h8c_docker_20210203T105342',
            'lightautoml_7593_1h8c_docker_20210203T105327',

            # Dionis 189355
            'lightautoml_189355_1h8c_docker_20210203T115349', # TIMEOUT
            'lightautoml_189355_1h8c_docker_20210203T115329', # TIMEOUT
            'lightautoml_189355_1h8c_docker_20210203T115354',
            'lightautoml_189355_1h8c_docker_20210203T115359', #FAIL
#             'lightautoml_189355_1h8c_docker_20210203T115344',
#             'lightautoml_189355_1h8c_docker_20210203T115339',
#             'lightautoml_189355_1h8c_docker_20210203T115334',
#             'lightautoml_189355_1h8c_docker_20210203T115324',
#             'lightautoml_189355_1h8c_docker_20210203T115319',
#             'lightautoml_189355_1h8c_docker_20210203T115314',

            # ============================ H2OAutoML Zermelo ============================
            # SMALL
            'h2oautoml_146818_1h8c_docker_20201104T120258', # Australian 146818
            'h2oautoml_10101_1h8c_docker_20201104T120310', # blood-transfusion 10101
            'h2oautoml_146821_1h8c_docker_20201104T120323', # car 146821
            'h2oautoml_168908_1h8c_docker_20201104T120348', # christine 168908
            'h2oautoml_9981_1h8c_docker_20201104T120400', # cnae-9 9981
            'h2oautoml_31_1h8c_docker_20201104T120419', # credit-g 31
            'h2oautoml_168909_1h8c_docker_20201104T120445', # dilbert 168909
            'h2oautoml_168910_1h8c_docker_20201104T120523', # fabert 168910
            'h2oautoml_168911_1h8c_docker_20201104T120535', # jasmine 168911
            'h2oautoml_3917_1h8c_docker_20201104T120546', # kc1 3917
            'h2oautoml_3_1h8c_docker_20201104T215254', # kr-vs-kp 3
            'h2oautoml_12_1h8c_docker_20201104T215302', # mfeat-factors 12
            'h2oautoml_9952_1h8c_docker_20201104T215244', # phoneme 9952
            'h2oautoml_146822_1h8c_docker_20201103T223614', # segment 146822
            'h2oautoml_168912_1h8c_docker_20201103T223555', # sylvine 168912
            'h2oautoml_53_1h8c_docker_20201103T223534', # vehicle 53
            # MEDIUM
            'h2oautoml_7592_1h8c_docker_20201104T120049', # adult 7592
            'h2oautoml_34539_1h8c_docker_20201101T230455', # Amazon_employee_access 34539
            'h2oautoml_168868_1h8c_docker_20201102T100906', # APSFailure 168868 # 
            'h2oautoml_14965_1h8c_docker_20201103T222804',# bank-marketing 14965
            'h2oautoml_146195_1h8c_docker_20201103T222848', # connect-4 146195
            'h2oautoml_146825_1h8c_docker_20201104T120146', # Fashion-MNIST 146825
            'h2oautoml_168337_1h8c_docker_20201101T230610', # guillermo 168337
            'h2oautoml_168329_1h8c_docker_20201102T100923', # Helena 168329
            'h2oautoml_146606_1h8c_docker_20201102T204732', # higgs 146606
            'h2oautoml_168330_1h8c_docker_20201102T204810', # Jannis 168330
            'h2oautoml_167119_1h8c_docker_20201103T222905', # jungle_chess_2pcs_raw_endgame_complete 167119
            'h2oautoml_3945_1h8c_docker_20201104T120204', # KDDCup09_appetency 3945
            'h2oautoml_168335_1h8c_docker_20201104T120235', # MiniBooNE 168335
            'h2oautoml_9977_1h8c_docker_20201103T223012', # nomao 9977
            'h2oautoml_167120_1h8c_docker_20201103T223034', # numerai28.6 167120
            'h2oautoml_168338_1h8c_docker_20201103T223057', # riccardo 168338
            'h2oautoml_168332_1h8c_docker_20201103T223133', # Robert 168332
            'h2oautoml_146212_1h8c_docker_20201103T223151', # Shuttle 146212
            'h2oautoml_168331_1h8c_docker_20201103T223305', # Volkert 168331            
           # LARGE
            'h2oautoml_189354_1h8c_docker_20210203T205130', # 189354
            'h2oautoml_189356_1h8c_docker_20210203T205203', # Albert 189356
#         #     'h2oautoml_7593_1h8c_docker_20210203T205229', # Covertype 7593 FAILED TIME
#         #     'h2oautoml_189355_1h8c_docker_20210203T205250', # Dionis 189355 MEMORY

            # ============================ AutoGluon 0.0.12 ============================
            'autogluon_small_1h8c_docker_20201011T142300', # small
            'autogluon_10101_1h8c_docker_20201109T121303', # blood-transfusion 10101
            'autogluon_146821_1h8c_docker_20201109T085205', # car 146821
            # MEDIUM
            'autogluon_7592_1h8c_docker_20201016T180226', # adult 7592
            'autogluon_34539_1h8c_docker_20201018T000539', # Amazon_employee_access 34539
            'autogluon_168868_1h8c_docker_20201018T000607', # APSFailure 168868
            'autogluon_14965_1h8c_docker_20201018T000633', # bank-marketing 14965
            'autogluon_146195_1h8c_docker_20201018T000721',# connect-4 146195
            'autogluon_146825_4h8c_docker_20201014T225129', # Fashion-MNIST 146825
            'autogluon_medium_4h8c_docker_20201012T222352', # guillermo    

            # Helena 168329
            'autogluon_168329_1h8c_docker_20201110T054147',
            'autogluon_168329_1h8c_docker_20201110T033954',
            'autogluon_168329_1h8c_docker_20201110T034623',
            'autogluon_168329_1h8c_docker_20201110T034106',
            'autogluon_168329_1h8c_docker_20201110T013407',
            'autogluon_168329_1h8c_docker_20201110T013339',
            'autogluon_168329_1h8c_docker_20201110T013310',
            'autogluon_167120_1h8c_docker_20201109T232506',
            'autogluon_167120_1h8c_docker_20201109T232536',
            'autogluon_168329_1h8c_docker_20201109T232641',
            'autogluon_168329_1h8c_docker_20201109T232636',
            'autogluon_168329_1h8c_docker_20201109T232631',

            'autogluon_146606_1h8c_docker_20201020T222850', # higgs 146606
            'autogluon_168330_1h8c_docker_20201020T222950', # Jannis 168330
            'autogluon_167119_1h8c_docker_20201020T223039', # jungle_chess_2pcs_raw_endgame_complete 167119
            'autogluon_3945_1h8c_docker_20201020T223113', # KDDCup09_appetency 3945
            'autogluon_168335_1h8c_docker_20201020T223147', # MiniBooNE 168335
            'autogluon_9977_1h8c_docker_20201020T223247', # nomao 9977
            'autogluon_167120_1h8c_docker_20201116T232345', # numerai28.6 167120
            'autogluon_168338_1h8c_docker_20201020T223422', # riccardo 168338
            'autogluon_168332_1h8c_docker_20201020T223456', # Robert 168332
            'autogluon_146212_1h8c_docker_20201020T223643', # Shuttle 146212
            'autogluon_168331_1h8c_docker_20201020T223753', # Volkert 168331
            #LARGE ALL FAILED TIME
#             'autogluon_189356_1h8c_docker_20210207T193038',
#             'autogluon_189355_1h8c_docker_20210207T192934',
#             'autogluon_7593_1h8c_docker_20210207T192837',
#             'autogluon_189354_1h8c_docker_20210207T192848',

            # ============================ oboe ============================
            # SMALL
            'oboe_146818_1h8c_local_20201110T222003', # Australian 146818
            'oboe_10101_1h8c_local_20201110T222005', # blood-transfusion 10101
            'oboe_146821_1h8c_local_20201110T222052', # car 146821
            'oboe_168908_1h8c_local_20201110T222052', # christine 168908 FAILED
            'oboe_9981_1h8c_local_20201110T222007', # cnae-9 9981
            'oboe_31_1h8c_local_20201110T222050', # credit-g 31
            'oboe_168909_1h8c_local_20201110T222006', # dilbert 168909
            'oboe_168910_1h8c_local_20201110T222050', # fabert 168910
            'oboe_168911_1h8c_local_20201110T222050', # jasmine 168911
            'oboe_3917_1h8c_local_20201110T222050', # kc1 3917
            'oboe_3_1h8c_local_20201110T222015', # kr-vs-kp 3
            'oboe_12_1h8c_local_20201110T222013', # mfeat-factors 12
            'oboe_9952_1h8c_local_20201110T222014', # phoneme 9952
            'oboe_146822_1h8c_local_20201110T222050', # segment 146822
            'oboe_168912_1h8c_local_20201110T222016', # sylvine 168912
            'oboe_53_1h8c_local_20201110T213834', # vehicle 53
            #MEDIUM
            'oboe_7592_1h8c_docker_20201027T221901', # adult 7592
            'oboe_34539_1h8c_docker_20201028T174551', # Amazon_employee_access 34539
            'oboe_168868_1h8c_docker_20201028T174608', # APSFailure 168868
            'oboe_14965_1h8c_docker_20201028T174621', # bank-marketing 14965
            'oboe_146195_1h8c_docker_20201027T221901', # connect-4 146195
            'oboe_146825_1h8c_docker_20201028T174731', # Fashion-MNIST 146825
            'oboe_168337_1h8c_docker_20201028T174757', # guillermo 168337
            'oboe_168329_1h8c_docker_20201028T174813', # Helena 168329
            'oboe_146606_1h8c_docker_20201028T174849', # higgs 146606
            'oboe_168330_1h8c_docker_20201028T174929', # Jannis 168330
            'oboe_167119_1h8c_docker_20201027T221856', # jungle_chess_2pcs_raw_endgame_complete 167119
            'oboe_3945_1h8c_docker_20201028T175106', # KDDCup09_appetency 3945
            'oboe_168335_1h8c_docker_20201103T222941', # MiniBooNE 168335
            'oboe_9977_1h8c_docker_20201028T235208', # nomao 9977
            'oboe_167120_1h8c_docker_20201028T235238', # numerai28.6 | 167120
            'oboe_168338_1h8c_docker_20201028T235300', # riccardo 168338
            'oboe_168332_1h8c_docker_20201028T235325', # Robert 168332
            'oboe_146212_1h8c_docker_20201028T235402', # Shuttle 146212
            'oboe_168331_1h8c_docker_20201028T235423', # Volkert 168331
            # LARGE
            'oboe_189354_1h8c_docker_20201027T221856', # 189354
            'oboe_189356_1h8c_docker_20201027T221817', # Albert 189356
            'oboe_7593_1h8c_docker_20201027T221750', # Covertype 7593
            'oboe_189355_1h8c_docker_20201027T221856', # Dionis 189355
            

            # ============================ TPOT ============================
            'tpot_small_1h8c_docker_20201011T143500', # small
            'tpot_168909_1h8c_docker_20201116T112034', # dilbert 168909
            # MEDIUM
            'tpot_7592_1h8c_docker_20201018T001228', # adult 7592
            'tpot_34539_1h8c_docker_20201020T223856', # Amazon_employee_access 34539
            'tpot_168868_1h8c_docker_20201020T223954', # APSFailure 168868
            'tpot_14965_1h8c_docker_20201020T224042', # bank-marketing 14965
            'tpot_146195_1h8c_docker_20201020T224246', # connect-4 146195
            'tpot_146825_1h8c_docker_20201020T224359', # Fashion-MNIST 146825
            'tpot_168337_1h8c_docker_20201021T101713', # guillermo 168337
            'tpot_168329_1h8c_docker_20201116T215638', # Helena 168329
            'tpot_146606_1h8c_docker_20201021T131349', # higgs 146606
            'tpot_168330_1h8c_docker_20201021T131419', # Jannis 168330
            'tpot_167119_1h8c_docker_20201021T131456', # jungle_chess_2pcs_raw_endgame_complete 167119 FAILED some folds
            'tpot_3945_1h8c_docker_20201021T131526', # KDDCup09_appetency 3945
            'tpot_168335_1h8c_docker_20201021T131601', # MiniBooNE 168335
            'tpot_9977_1h8c_docker_20201021T131621', # nomao 9977 FAILED some folds
            'tpot_167120_1h8c_docker_20201021T131651', # numerai28.6 | 167120
            'tpot_168338_1h8c_docker_20201109T085614', # riccardo 168338 FAILED some folds
            'tpot_168332_1h8c_docker_20201021T131807', # Robert 168332 # FAILED 1 fold
            'tpot_146212_1h8c_docker_20201021T131837', # Shuttle 146212
            'tpot_168331_1h8c_docker_20201021T131909', # Volkert 168331
            # LARGE
            'tpot_189354_1h8c_docker_20210203T205336', # 189354
#             'tpot_189356_1h8c_docker_20210203T205415', # Albert 189356 FAILED
            'tpot_7593_1h8c_docker_20210203T205444', # Covertype 7593
#             'tpot_189355_1h8c_docker_20210203T205553', # Dionis 189355 FAILED


            # ============================ AutoWEKA ============================
            # SMALL    
            'autoweka_146818_1h8c_docker_20201115T142333', # Australian 146818 
            'autoweka_10101_1h8c_docker_20201114T235213', # blood-transfusion 10101
            'autoweka_146821_1h8c_docker_20201114T235327', # car 146821
            'autoweka_168908_1h8c_docker_20201114T235025', # christine 168908 FAILED 1 Fold
            'autoweka_9981_1h8c_docker_20201112T115531', # cnae-9 9981
            'autoweka_31_1h8c_docker_20201112T115627', # credit-g 31
            'autoweka_168909_1h8c_docker_20201115T142302', # dilbert 168909
            'autoweka_168910_1h8c_docker_20201115T142246', # fabert 168910
            'autoweka_168911_1h8c_docker_20201115T142227', # jasmine 168911
            'autoweka_3917_1h8c_docker_20201115T142215', # kc1 3917
            'autoweka_3_1h8c_docker_20201114T235437', # kr-vs-kp 3
            'autoweka_12_1h8c_docker_20201114T234935', # mfeat-factors 12
            'autoweka_9952_1h8c_docker_20201109T091706', # phoneme 9952
            'autoweka_146822_1h8c_docker_20201114T234846', # segment 146822
            'autoweka_168912_1h8c_docker_20201114T234650', # sylvine 168912
            'autoweka_53_1h8c_docker_20201112T120331', # vehicle 53
            # MEDIUM
            'autoweka_7592_1h8c_docker_20201016T180348', # adult 7592
            'autoweka_34539_1h8c_docker_20201018T001537', # Amazon_employee_access 34539
            'autoweka_168868_1h8c_docker_20201018T001632', # APSFailure 168868
            'autoweka_14965_1h8c_docker_20201018T002121', # bank-marketing 14965
            'autoweka_146195_1h8c_docker_20201021T132015', # connect-4 146195
            'autoweka_146825_1h8c_docker_20201021T132033', # Fashion-MNIST 146825
            'autoweka_168337_1h8c_docker_20201021T132127', # guillermo 168337 # FAILED some folds
            'autoweka_168329_1h8c_docker_20201021T132155', # Helena 168329 # FAILED some folds
            'autoweka_146606_1h8c_docker_20201021T132243', # higgs 146606
            'autoweka_168330_1h8c_docker_20201114T151639', # Jannis 168330
            'autoweka_167119_1h8c_docker_20201028T133857', # jungle_chess_2pcs_raw_endgame_complete 167119
            # 'autoweka_3945_1h8c_docker_20201116T092615', # KDDCup09_appetency 3945
            'autoweka_168335_1h8c_docker_20201022T105746', # MiniBooNE 168335
            'autoweka_9977_1h8c_docker_20201022T105817', # nomao 9977
            'autoweka_167120_1h8c_docker_20201022T105839', # numerai28.6 | 167120
            'autoweka_168338_1h8c_docker_20201112T234054', # riccardo 168338
            # 'autoweka_168332_1h8c_docker_20201116T092552', # Robert 168332
            'autoweka_146212_1h8c_docker_20201022T110147', # Shuttle 146212
            'autoweka_168331_1h8c_docker_20201022T110215', # Volkert 168331
            #LARGE
            'autoweka_189355_1h8c_docker_20210203T231829', 
            'autoweka_189354_1h8c_docker_20210203T232202',
            'autoweka_189356_1h8c_docker_20210203T232101', 
            'autoweka_189355_1h8c_docker_20210203T231829',

            # ============================ GAMA ============================
            # SMALL
            'gama_146818_1h8c_docker_20201105T113105', # Australian 146818
            'gama_10101_1h8c_docker_20201108T233150', # blood-transfusion 10101
            'gama_146821_1h8c_docker_20201106T081435', # car 146821
            'gama_168908_1h8c_docker_20201114T152425', # christine 168908
            'gama_9981_1h8c_docker_20201106T081627', # cnae-9 9981
            'gama_31_1h8c_docker_20201105T115508', # credit-g 31
            'gama_168909_1h8c_docker_20201105T115515', # dilbert 168909
            'gama_168910_1h8c_docker_20201105T115520', # fabert 168910
            'gama_168911_1h8c_docker_20201105T115524', # jasmine 168911
            'gama_3917_1h8c_docker_20201105T222413', # kc1 3917
            'gama_3_1h8c_docker_20201105T222120', # kr-vs-kp 3
            'gama_12_1h8c_docker_20201105T222127', # mfeat-factors 12
            'gama_9952_1h8c_docker_20201105T222136', # phoneme 9952
            'gama_146822_1h8c_docker_20201105T222153', # segment 146822
            'gama_168912_1h8c_docker_20201105T222221', # sylvine 168912
            'gama_53_1h8c_docker_20201105T222300', # vehicle 53

            # MEDIUM
            'gama_7592_1h8c_docker_20201105T222244', # adult 7592
            'gama_34539_1h8c_docker_20201105T222345', # Amazon_employee_access 34539
            'gama_168868_1h8c_docker_20201105T222407', # APSFailure 168868
            'gama_14965_1h8c_docker_20201105T222431', # bank-marketing 14965
            'gama_146195_1h8c_docker_20201108T232106', # connect-4 146195
            'gama_146825_1h8c_docker_20201111T203154', # Fashion-MNIST 146825 lastest
            'gama_168337_1h8c_docker_20201112T234350', # guillermo 168337 FAILED
            'gama_168329_1h8c_docker_20201112T115240', # Helena 168329
            'gama_146606_1h8c_docker_20201106T081637', # higgs 146606
            'gama_168330_1h8c_docker_20201106T081658', # Jannis 168330
            'gama_167119_1h8c_docker_20201106T081714', # jungle_chess_2pcs_raw_endgame_complete 167119
            'gama_3945_1h8c_docker_20201106T081729', # KDDCup09_appetency 3945
            'gama_168335_1h8c_docker_20201114T152135', # MiniBooNE 168335
            'gama_9977_1h8c_docker_20201106T115717', # nomao 9977
            'gama_167120_1h8c_docker_20201106T115730', # numerai28.6 | 167120
            'gama_168338_1h8c_docker_20201115T060056', # riccardo 168338 
            'gama_168332_1h8c_docker_20201106T115809', # Robert 168332
            'gama_146212_1h8c_docker_20201107T230925', # Shuttle 146212
            'gama_168331_1h8c_docker_20201114T152251', # Volkert 168331

#             LARGE
            'gama_189354_1h8c_docker_20210208T093442',
            'gama_189354_1h8c_docker_20210208T093526',
            'gama_189354_1h8c_docker_20210208T093445',
            'gama_189354_1h8c_docker_20210208T093556',
            'gama_189354_1h8c_docker_20210208T093437',
            'gama_189354_1h8c_docker_20210208T083934',
            'gama_189354_1h8c_docker_20210208T083938',
            'gama_189354_1h8c_docker_20210208T083930',
            'gama_189354_1h8c_docker_20210208T083925',
            'gama_189354_1h8c_docker_20210208T083920',
            
            # Albert 189356
            'gama_189356_1h8c_docker_20210208T095218',
            'gama_189356_1h8c_docker_20210208T123838',
            'gama_189356_1h8c_docker_20210208T115601',
            'gama_189356_1h8c_docker_20210208T115901',
            'gama_189356_1h8c_docker_20210208T142012',
            'gama_189356_1h8c_docker_20210208T130606',
            'gama_189356_1h8c_docker_20210208T141755',
            'gama_189356_1h8c_docker_20210208T142229',
            'gama_189356_1h8c_docker_20210208T142224',

            # Covertype 7593
            'gama_7593_1h8c_docker_20210208T153733',
#             'gama_7593_1h8c_docker_20210208T095401',
            'gama_7593_1h8c_docker_20210208T105125',
            'gama_7593_1h8c_docker_20210208T105152',
            'gama_7593_1h8c_docker_20210208T115645',
            'gama_7593_1h8c_docker_20210208T115415',
            'gama_7593_1h8c_docker_20210208T130620',
            'gama_7593_1h8c_docker_20210208T141145',
            'gama_7593_1h8c_docker_20210208T141220',
            'gama_7593_1h8c_docker_20210208T141236',
            'gama_7593_1h8c_docker_20210208T131721',
            'gama_7593_1h8c_docker_20210208T153733',

            # Dionis 189355
#             '',
            'gama_189355_1h8c_docker_20210208T094921',
            'gama_189355_1h8c_docker_20210208T105134',
            'gama_189355_1h8c_docker_20210208T115456',
            'gama_189355_1h8c_docker_20210208T152910',
            'gama_189355_1h8c_docker_20210208T145120',
            'gama_189355_1h8c_docker_20210208T152939',
            'gama_189355_1h8c_docker_20210208T141642',
            'gama_189355_1h8c_docker_20210208T153010',
            'gama_189355_1h8c_docker_20210208T130658',
            'gama_189355_1h8c_docker_20210208T170328',

            # ============================ autosklearn ============================
            # SMALL
            'autosklearn_146818_1h8c_docker_20201126T224632', # Australian 146818
            'autosklearn_10101_1h8c_docker_20201126T231834', # blood-transfusion 10101
            'autosklearn_146821_1h8c_docker_20201126T231645', # car 146821
            'autosklearn_168908_1h8c_docker_20201126T231743', # christine 168908
            'autosklearn_9981_1h8c_docker_20201216T113310', # cnae-9 9981
            'autosklearn_31_1h8c_docker_20201215T112848', # credit-g 31
            'autosklearn_168909_1h8c_docker_20201126T224746', # dilbert 168909
            'autosklearn_168910_1h8c_docker_20201215T101943', # fabert 168910
            'autosklearn_168911_1h8c_docker_20201126T231500', # jasmine 168911
            'autosklearn_3917_1h8c_docker_20201126T231412', # kc1 3917
            'autosklearn_3_1h8c_docker_20201214T214303', # kr-vs-kp 3
            'autosklearn_12_1h8c_docker_20201215T112922', # mfeat-factors 12
            'autosklearn_9952_1h8c_docker_20201215T112909', # phoneme 9952
            'autosklearn_146822_1h8c_docker_20201126T231328', # segment 146822
            'autosklearn_168912_1h8c_docker_20201215T214037', # sylvine 168912
            'autosklearn_53_1h8c_docker_20201126T231105', # vehicle 53

#             # MEDIUM
            'autosklearn_7592_1h8c_docker_20201215T214002', # adult 7592
            'autosklearn_34539_1h8c_docker_20201215T213945', # Amazon_employee_access 34539
            'autosklearn_168868_1h8c_docker_20201215T113005', # APSFailure 168868
            'autosklearn_14965_1h8c_docker_20201215T112953', # bank-marketing 14965

            # connect-4 146195
            'autosklearn_146195_1h8c_docker_20201215T101750',
            'autosklearn_146195_1h8c_docker_20201215T101745',
            'autosklearn_146195_1h8c_docker_20201215T101730',
            'autosklearn_146195_1h8c_docker_20201215T101735',
            'autosklearn_146195_1h8c_docker_20201215T101740',
            'autosklearn_146195_1h8c_docker_20201215T101720',
            'autosklearn_146195_1h8c_docker_20201215T101725',
            'autosklearn_146195_1h8c_docker_20201215T101704',
            'autosklearn_146195_1h8c_docker_20201215T101709',
            'autosklearn_146195_1h8c_docker_20201215T101714',
            
            'autosklearn_146825_1h8c_docker_20201214T214354', # Fashion-MNIST 146825
            'autosklearn_168337_1h8c_docker_20201214T214336', # guillermo 168337
            'autosklearn_168329_1h8c_docker_20201214T214325', # Helena 168329
            
            'autosklearn_146606_1h8c_docker_20201127T095410', # higgs 146606
            'autosklearn_146606_1h8c_docker_20201127T095405',
            'autosklearn_146606_1h8c_docker_20201127T095400',
            'autosklearn_146606_1h8c_docker_20201127T095350',
            'autosklearn_146606_1h8c_docker_20201127T095355',
            'autosklearn_146606_1h8c_docker_20201127T095335',
            'autosklearn_146606_1h8c_docker_20201127T095340',
            'autosklearn_146606_1h8c_docker_20201127T095345',
            'autosklearn_146606_1h8c_docker_20201127T095330',
            'autosklearn_146606_1h8c_docker_20201127T095326',

            'autosklearn_168330_1h8c_docker_20201216T113205', # Jannis 168330
            'autosklearn_167119_1h8c_docker_20201215T214242', # jungle_chess_2pcs_raw_endgame_complete 167119
            'autosklearn_3945_1h8c_docker_20201126T232029', # KDDCup09_appetency 3945
            'autosklearn_168335_1h8c_docker_20201126T225012', # MiniBooNE 168335
            'autosklearn_9977_1h8c_docker_20201116T103207', # nomao 9977
            'autosklearn_167120_1h8c_docker_20201215T214405', # numerai28.6 | 167120
            'autosklearn_168338_1h8c_docker_20201126T224659', # riccardo 168338
            'autosklearn_168332_1h8c_docker_20201215T214521', # Robert 168332
            'autosklearn_146212_1h8c_docker_20201115T060204', # Shuttle 146212
            'autosklearn_168331_1h8c_docker_20201126T224857', # Volkert 168331

# #             # LARGE
            'autosklearn_189354_1h8c_docker_20201126T231932', # 189354
            'autosklearn_189356_1h8c_docker_20210204T125247', # Albert 189356
# #         #     'autosklearn_7593', # Covertype 7593
            'autosklearn_189355_1h8c_docker_20210204T125242', # Dionis 189355

          ]
    ),
}

config.results_group = '1h'
config.results_files = all_results_files[config.results_group]
config.tasks_sort_by = 'nrows'


