from BanditOpt import ConfigSpace, ConditionalSpace, NominalSpace, OrdinalSpace, ContinuousSpace, Forbidden
from BanditOpt.BO4ML import BO4ML
import numpy as np

search_space = ConfigSpace()
con = ConditionalSpace("test")

p1= NominalSpace(['none', 'weighting'],'p1',default='none')
search_space._add_singleparameter(p1)
p2= NominalSpace(['adaboost', 'bernoulli_nb', 'decision_tree', 'extra_trees', 'gaussian_nb', 'gradient_boosting', 'k_nearest_neighbors', 'lda', 'liblinear_svc', 'libsvm_svc', 'multinomial_nb', 'passive_aggressive', 'qda', 'random_forest', 'sgd'],'p2',default='random_forest')
search_space._add_singleparameter(p2)
p3= NominalSpace(['no_encoding', 'one_hot_encoding'],'p3',default='one_hot_encoding')
search_space._add_singleparameter(p3)
p4= NominalSpace(['minority_coalescer', 'no_coalescense'],'p4',default='minority_coalescer')
search_space._add_singleparameter(p4)
p5= NominalSpace(['mean', 'median', 'most_frequent'],'p5',default='mean')
search_space._add_singleparameter(p5)
p6= NominalSpace(['minmax', 'none', 'normalize', 'quantile_transformer', 'robust_scaler', 'standardize'],'p6',default='standardize')
search_space._add_singleparameter(p6)
p7= NominalSpace(['extra_trees_preproc_for_classification', 'fast_ica', 'feature_agglomeration', 'kernel_pca', 'kitchen_sinks', 'liblinear_svc_preprocessor', 'no_preprocessing', 'nystroem_sampler', 'pca', 'polynomial', 'random_trees_embedding', 'select_percentile_classification', 'select_rates'],'p7',default='no_preprocessing')
search_space._add_singleparameter(p7)
p8= NominalSpace(['SAMME.R', 'SAMME'],'p8',default='SAMME.R')
search_space._add_singleparameter(p8)
p9= ContinuousSpace([0.01, 2.0],'p9',default=0.1)
search_space._add_singleparameter(p9)
p10= OrdinalSpace([1, 10],'p10',default=1)
search_space._add_singleparameter(p10)
p11= OrdinalSpace([50, 500],'p11',default=50)
search_space._add_singleparameter(p11)
p12= ContinuousSpace([0.01, 100.0],'p12',default=1.0)
search_space._add_singleparameter(p12)
p13= NominalSpace(['True', 'False'],'p13',default='True')
search_space._add_singleparameter(p13)
p14= NominalSpace(['gini', 'entropy'],'p14',default='gini')
search_space._add_singleparameter(p14)
p15= ContinuousSpace([0.0, 2.0],'p15',default=0.5)
search_space._add_singleparameter(p15)
p16= NominalSpace([1.0],'p16',default=1.0)
search_space._add_singleparameter(p16)
p17= NominalSpace(['None'],'p17',default='None')
search_space._add_singleparameter(p17)
p18= NominalSpace([0.0],'p18',default=0.0)
search_space._add_singleparameter(p18)
p19= OrdinalSpace([1, 20],'p19',default=1)
search_space._add_singleparameter(p19)
p20= OrdinalSpace([2, 20],'p20',default=2)
search_space._add_singleparameter(p20)
p21= NominalSpace([0.0],'p21',default=0.0)
search_space._add_singleparameter(p21)
p22= NominalSpace(['True', 'False'],'p22',default='False')
search_space._add_singleparameter(p22)
p23= NominalSpace(['gini', 'entropy'],'p23',default='gini')
search_space._add_singleparameter(p23)
p24= NominalSpace(['None'],'p24',default='None')
search_space._add_singleparameter(p24)
p25= ContinuousSpace([0.0, 1.0],'p25',default=0.5)
search_space._add_singleparameter(p25)
p26= NominalSpace(['None'],'p26',default='None')
search_space._add_singleparameter(p26)
p27= NominalSpace([0.0],'p27',default=0.0)
search_space._add_singleparameter(p27)
p28= OrdinalSpace([1, 20],'p28',default=1)
search_space._add_singleparameter(p28)
p29= OrdinalSpace([2, 20],'p29',default=2)
search_space._add_singleparameter(p29)
p30= NominalSpace([0.0],'p30',default=0.0)
search_space._add_singleparameter(p30)
p31= NominalSpace(['off', 'train', 'valid'],'p31',default='off')
search_space._add_singleparameter(p31)
p32= ContinuousSpace([1e-10, 1.0],'p32',default=1e-10)
search_space._add_singleparameter(p32)
p33= ContinuousSpace([0.01, 1.0],'p33',default=0.1)
search_space._add_singleparameter(p33)
p34= NominalSpace(['auto'],'p34',default='auto')
search_space._add_singleparameter(p34)
p35= NominalSpace([255],'p35',default=255)
search_space._add_singleparameter(p35)
p36= NominalSpace(['None'],'p36',default='None')
search_space._add_singleparameter(p36)
p37= OrdinalSpace([3, 2047],'p37',default=31)
search_space._add_singleparameter(p37)
p38= OrdinalSpace([1, 200],'p38',default=20)
search_space._add_singleparameter(p38)
p39= NominalSpace(['loss'],'p39',default='loss')
search_space._add_singleparameter(p39)
p40= NominalSpace([1e-07],'p40',default=1e-07)
search_space._add_singleparameter(p40)
p41= OrdinalSpace([1, 100],'p41',default=1)
search_space._add_singleparameter(p41)
p42= NominalSpace([1, 2],'p42',default='2')
search_space._add_singleparameter(p42)
p43= NominalSpace(['uniform', 'distance'],'p43',default='uniform')
search_space._add_singleparameter(p43)
p44= OrdinalSpace([1, 250],'p44',default=10)
search_space._add_singleparameter(p44)
p45= NominalSpace(['None', 'auto', 'manual'],'p45',default='None')
search_space._add_singleparameter(p45)
p46= ContinuousSpace([1e-05, 0.1],'p46',default=0.0001)
search_space._add_singleparameter(p46)
p47= ContinuousSpace([0.03125, 32768.0],'p47',default=1.0)
search_space._add_singleparameter(p47)
p48= NominalSpace(['False'],'p48',default='False')
search_space._add_singleparameter(p48)
p49= NominalSpace(['True'],'p49',default='True')
search_space._add_singleparameter(p49)
p50= NominalSpace([1],'p50',default=1)
search_space._add_singleparameter(p50)
p51= NominalSpace(['hinge', 'squared_hinge'],'p51',default='squared_hinge')
search_space._add_singleparameter(p51)
p52= NominalSpace(['ovr'],'p52',default='ovr')
search_space._add_singleparameter(p52)
p53= NominalSpace(['l1', 'l2'],'p53',default='l2')
search_space._add_singleparameter(p53)
p54= ContinuousSpace([1e-05, 0.1],'p54',default=0.0001)
search_space._add_singleparameter(p54)
p55= ContinuousSpace([0.03125, 32768.0],'p55',default=1.0)
search_space._add_singleparameter(p55)
p56= ContinuousSpace([3.0517578125e-05, 8.0],'p56',default=0.1)
search_space._add_singleparameter(p56)
p57= NominalSpace(['rbf', 'poly', 'sigmoid'],'p57',default='rbf')
search_space._add_singleparameter(p57)
p58= NominalSpace([-1],'p58',default=-1)
search_space._add_singleparameter(p58)
p59= NominalSpace(['True', 'False'],'p59',default='True')
search_space._add_singleparameter(p59)
p60= ContinuousSpace([1e-05, 0.1],'p60',default=0.001)
search_space._add_singleparameter(p60)
p61= ContinuousSpace([0.01, 100.0],'p61',default=1.0)
search_space._add_singleparameter(p61)
p62= NominalSpace(['True', 'False'],'p62',default='True')
search_space._add_singleparameter(p62)
p63= ContinuousSpace([1e-05, 10.0],'p63',default=1.0)
search_space._add_singleparameter(p63)
p64= NominalSpace(['False', 'True'],'p64',default='False')
search_space._add_singleparameter(p64)
p65= NominalSpace(['True'],'p65',default='True')
search_space._add_singleparameter(p65)
p66= NominalSpace(['hinge', 'squared_hinge'],'p66',default='hinge')
search_space._add_singleparameter(p66)
p67= ContinuousSpace([1e-05, 0.1],'p67',default=0.0001)
search_space._add_singleparameter(p67)
p68= ContinuousSpace([0.0, 1.0],'p68',default=0.0)
search_space._add_singleparameter(p68)
p69= NominalSpace(['True', 'False'],'p69',default='True')
search_space._add_singleparameter(p69)
p70= NominalSpace(['gini', 'entropy'],'p70',default='gini')
search_space._add_singleparameter(p70)
p71= NominalSpace(['None'],'p71',default='None')
search_space._add_singleparameter(p71)
p72= ContinuousSpace([0.0, 1.0],'p72',default=0.5)
search_space._add_singleparameter(p72)
p73= NominalSpace(['None'],'p73',default='None')
search_space._add_singleparameter(p73)
p74= NominalSpace([0.0],'p74',default=0.0)
search_space._add_singleparameter(p74)
p75= OrdinalSpace([1, 20],'p75',default=1)
search_space._add_singleparameter(p75)
p76= OrdinalSpace([2, 20],'p76',default=2)
search_space._add_singleparameter(p76)
p77= NominalSpace([0.0],'p77',default=0.0)
search_space._add_singleparameter(p77)
p78= ContinuousSpace([1e-07, 0.1],'p78',default=0.0001)
search_space._add_singleparameter(p78)
p79= NominalSpace(['False', 'True'],'p79',default='False')
search_space._add_singleparameter(p79)
p80= NominalSpace(['True'],'p80',default='True')
search_space._add_singleparameter(p80)
p81= NominalSpace(['optimal', 'invscaling', 'constant'],'p81',default='invscaling')
search_space._add_singleparameter(p81)
p82= NominalSpace(['hinge', 'log', 'modified_huber', 'squared_hinge', 'perceptron'],'p82',default='log')
search_space._add_singleparameter(p82)
p83= NominalSpace(['l1', 'l2', 'elasticnet'],'p83',default='l2')
search_space._add_singleparameter(p83)
p84= ContinuousSpace([1e-05, 0.1],'p84',default=0.0001)
search_space._add_singleparameter(p84)
p85= ContinuousSpace([0.0001, 0.5],'p85',default=0.01)
search_space._add_singleparameter(p85)
p86= OrdinalSpace([10, 2000],'p86',default=1000)
search_space._add_singleparameter(p86)
p87= NominalSpace(['uniform', 'normal'],'p87',default='uniform')
search_space._add_singleparameter(p87)
p88= ContinuousSpace([0.7, 0.999],'p88',default=0.75)
search_space._add_singleparameter(p88)
p89= ContinuousSpace([0.001, 0.3],'p89',default=0.25)
search_space._add_singleparameter(p89)
p90= NominalSpace(['True', 'False'],'p90',default='False')
search_space._add_singleparameter(p90)
p91= NominalSpace(['gini', 'entropy'],'p91',default='gini')
search_space._add_singleparameter(p91)
p92= NominalSpace(['None'],'p92',default='None')
search_space._add_singleparameter(p92)
p93= ContinuousSpace([0.0, 1.0],'p93',default=0.5)
search_space._add_singleparameter(p93)
p94= NominalSpace(['None'],'p94',default='None')
search_space._add_singleparameter(p94)
p95= NominalSpace([0.0],'p95',default=0.0)
search_space._add_singleparameter(p95)
p96= OrdinalSpace([1, 20],'p96',default=1)
search_space._add_singleparameter(p96)
p97= OrdinalSpace([2, 20],'p97',default=2)
search_space._add_singleparameter(p97)
p98= NominalSpace([0.0],'p98',default=0.0)
search_space._add_singleparameter(p98)
p99= NominalSpace([100],'p99',default=100)
search_space._add_singleparameter(p99)
p100= NominalSpace(['parallel', 'deflation'],'p100',default='parallel')
search_space._add_singleparameter(p100)
p101= NominalSpace(['logcosh', 'exp', 'cube'],'p101',default='logcosh')
search_space._add_singleparameter(p101)
p102= NominalSpace(['False', 'True'],'p102',default='False')
search_space._add_singleparameter(p102)
p103= NominalSpace(['euclidean', 'manhattan', 'cosine'],'p103',default='euclidean')
search_space._add_singleparameter(p103)
p104= NominalSpace(['ward', 'complete', 'average'],'p104',default='ward')
search_space._add_singleparameter(p104)
p105= OrdinalSpace([2, 400],'p105',default=25)
search_space._add_singleparameter(p105)
p106= NominalSpace(['mean', 'median', 'max'],'p106',default='mean')
search_space._add_singleparameter(p106)
p107= NominalSpace(['poly', 'rbf', 'sigmoid', 'cosine'],'p107',default='rbf')
search_space._add_singleparameter(p107)
p108= OrdinalSpace([10, 2000],'p108',default=100)
search_space._add_singleparameter(p108)
p109= ContinuousSpace([3.0517578125e-05, 8.0],'p109',default=1.0)
search_space._add_singleparameter(p109)
p110= OrdinalSpace([50, 10000],'p110',default=100)
search_space._add_singleparameter(p110)
p111= ContinuousSpace([0.03125, 32768.0],'p111',default=1.0)
search_space._add_singleparameter(p111)
p112= NominalSpace(['False'],'p112',default='False')
search_space._add_singleparameter(p112)
p113= NominalSpace(['True'],'p113',default='True')
search_space._add_singleparameter(p113)
p114= NominalSpace([1],'p114',default=1)
search_space._add_singleparameter(p114)
p115= NominalSpace(['hinge', 'squared_hinge'],'p115',default='squared_hinge')
search_space._add_singleparameter(p115)
p116= NominalSpace(['ovr'],'p116',default='ovr')
search_space._add_singleparameter(p116)
p117= NominalSpace(['l1'],'p117',default='l1')
search_space._add_singleparameter(p117)
p118= ContinuousSpace([1e-05, 0.1],'p118',default=0.0001)
search_space._add_singleparameter(p118)
p119= NominalSpace(['poly', 'rbf', 'sigmoid', 'cosine'],'p119',default='rbf')
search_space._add_singleparameter(p119)
p120= OrdinalSpace([50, 10000],'p120',default=100)
search_space._add_singleparameter(p120)
p121= ContinuousSpace([0.5, 0.9999],'p121',default=0.9999)
search_space._add_singleparameter(p121)
p122= NominalSpace(['False', 'True'],'p122',default='False')
search_space._add_singleparameter(p122)
p123= OrdinalSpace([2, 3],'p123',default=2)
search_space._add_singleparameter(p123)
p124= NominalSpace(['True', 'False'],'p124',default='True')
search_space._add_singleparameter(p124)
p125= NominalSpace(['False', 'True'],'p125',default='False')
search_space._add_singleparameter(p125)
p126= NominalSpace(['True', 'False'],'p126',default='True')
search_space._add_singleparameter(p126)
p127= OrdinalSpace([2, 10],'p127',default=5)
search_space._add_singleparameter(p127)
p128= NominalSpace(['None'],'p128',default='None')
search_space._add_singleparameter(p128)
p129= OrdinalSpace([1, 20],'p129',default=1)
search_space._add_singleparameter(p129)
p130= OrdinalSpace([2, 20],'p130',default=2)
search_space._add_singleparameter(p130)
p131= NominalSpace([1.0],'p131',default=1.0)
search_space._add_singleparameter(p131)
p132= OrdinalSpace([10, 100],'p132',default=10)
search_space._add_singleparameter(p132)
p133= ContinuousSpace([1.0, 99.0],'p133',default=50.0)
search_space._add_singleparameter(p133)
p134= NominalSpace(['chi2', 'f_classif', 'mutual_info'],'p134',default='chi2')
search_space._add_singleparameter(p134)
p135= ContinuousSpace([0.01, 0.5],'p135',default=0.1)
search_space._add_singleparameter(p135)
p136= NominalSpace(['fpr', 'fdr', 'fwe'],'p136',default='fpr')
search_space._add_singleparameter(p136)
p137= NominalSpace(['chi2', 'f_classif'],'p137',default='chi2')
search_space._add_singleparameter(p137)
p138= OrdinalSpace([1, 20],'p138',default=10)
search_space._add_singleparameter(p138)
p139= ContinuousSpace([0.01, 0.4],'p139',default=0.1)
search_space._add_singleparameter(p139)
p140= ContinuousSpace([0.0, 1.0],'p140',default=0.5)
search_space._add_singleparameter(p140)
p141= ContinuousSpace([-1.0, 1.0],'p141',default=0.0)
search_space._add_singleparameter(p141)
p142= OrdinalSpace([2, 5],'p142',default=3)
search_space._add_singleparameter(p142)
p143= ContinuousSpace([1e-05, 0.1],'p143',default=0.0001)
search_space._add_singleparameter(p143)
p144= ContinuousSpace([1e-07, 0.1],'p144',default=0.01)
search_space._add_singleparameter(p144)
p145= ContinuousSpace([1e-09, 1.0],'p145',default=0.15)
search_space._add_singleparameter(p145)
p146= ContinuousSpace([1e-05, 1.0],'p146',default=0.5)
search_space._add_singleparameter(p146)
p147= OrdinalSpace([10, 2000],'p147',default=100)
search_space._add_singleparameter(p147)
p148= ContinuousSpace([-1.0, 1.0],'p148',default=0.0)
search_space._add_singleparameter(p148)
p149= OrdinalSpace([2, 5],'p149',default=3)
search_space._add_singleparameter(p149)
p150= ContinuousSpace([3.0517578125e-05, 8.0],'p150',default=1.0)
search_space._add_singleparameter(p150)
p151= ContinuousSpace([-1.0, 1.0],'p151',default=0.0)
search_space._add_singleparameter(p151)
p152= OrdinalSpace([2, 5],'p152',default=3)
search_space._add_singleparameter(p152)
p153= ContinuousSpace([3.0517578125e-05, 8.0],'p153',default=0.1)
search_space._add_singleparameter(p153)
con.addConditional(p8,p2,['adaboost'])
con.addConditional(p9,p2,['adaboost'])
con.addConditional(p10,p2,['adaboost'])
con.addConditional(p11,p2,['adaboost'])
con.addConditional(p12,p2,['bernoulli_nb'])
con.addConditional(p13,p2,['bernoulli_nb'])
con.addConditional(p14,p2,['decision_tree'])
con.addConditional(p15,p2,['decision_tree'])
con.addConditional(p16,p2,['decision_tree'])
con.addConditional(p17,p2,['decision_tree'])
con.addConditional(p18,p2,['decision_tree'])
con.addConditional(p19,p2,['decision_tree'])
con.addConditional(p20,p2,['decision_tree'])
con.addConditional(p21,p2,['decision_tree'])
con.addConditional(p22,p2,['extra_trees'])
con.addConditional(p23,p2,['extra_trees'])
con.addConditional(p24,p2,['extra_trees'])
con.addConditional(p25,p2,['extra_trees'])
con.addConditional(p26,p2,['extra_trees'])
con.addConditional(p27,p2,['extra_trees'])
con.addConditional(p28,p2,['extra_trees'])
con.addConditional(p29,p2,['extra_trees'])
con.addConditional(p30,p2,['extra_trees'])
con.addConditional(p31,p2,['gradient_boosting'])
con.addConditional(p32,p2,['gradient_boosting'])
con.addConditional(p33,p2,['gradient_boosting'])
con.addConditional(p34,p2,['gradient_boosting'])
con.addConditional(p35,p2,['gradient_boosting'])
con.addConditional(p36,p2,['gradient_boosting'])
con.addConditional(p37,p2,['gradient_boosting'])
con.addConditional(p38,p2,['gradient_boosting'])
con.addConditional(p39,p2,['gradient_boosting'])
con.addConditional(p40,p2,['gradient_boosting'])
con.addConditional(p41,p2,['k_nearest_neighbors'])
con.addConditional(p42,p2,['k_nearest_neighbors'])
con.addConditional(p43,p2,['k_nearest_neighbors'])
con.addConditional(p44,p2,['lda'])
con.addConditional(p45,p2,['lda'])
con.addConditional(p46,p2,['lda'])
con.addConditional(p47,p2,['liblinear_svc'])
con.addConditional(p48,p2,['liblinear_svc'])
con.addConditional(p49,p2,['liblinear_svc'])
con.addConditional(p50,p2,['liblinear_svc'])
con.addConditional(p51,p2,['liblinear_svc'])
con.addConditional(p52,p2,['liblinear_svc'])
con.addConditional(p53,p2,['liblinear_svc'])
con.addConditional(p54,p2,['liblinear_svc'])
con.addConditional(p55,p2,['libsvm_svc'])
con.addConditional(p56,p2,['libsvm_svc'])
con.addConditional(p57,p2,['libsvm_svc'])
con.addConditional(p58,p2,['libsvm_svc'])
con.addConditional(p59,p2,['libsvm_svc'])
con.addConditional(p60,p2,['libsvm_svc'])
con.addConditional(p61,p2,['multinomial_nb'])
con.addConditional(p62,p2,['multinomial_nb'])
con.addConditional(p63,p2,['passive_aggressive'])
con.addConditional(p64,p2,['passive_aggressive'])
con.addConditional(p65,p2,['passive_aggressive'])
con.addConditional(p66,p2,['passive_aggressive'])
con.addConditional(p67,p2,['passive_aggressive'])
con.addConditional(p68,p2,['qda'])
con.addConditional(p69,p2,['random_forest'])
con.addConditional(p70,p2,['random_forest'])
con.addConditional(p71,p2,['random_forest'])
con.addConditional(p72,p2,['random_forest'])
con.addConditional(p73,p2,['random_forest'])
con.addConditional(p74,p2,['random_forest'])
con.addConditional(p75,p2,['random_forest'])
con.addConditional(p76,p2,['random_forest'])
con.addConditional(p77,p2,['random_forest'])
con.addConditional(p78,p2,['sgd'])
con.addConditional(p79,p2,['sgd'])
con.addConditional(p80,p2,['sgd'])
con.addConditional(p81,p2,['sgd'])
con.addConditional(p82,p2,['sgd'])
con.addConditional(p83,p2,['sgd'])
con.addConditional(p84,p2,['sgd'])
con.addConditional(p85,p4,['minority_coalescer'])
con.addConditional(p86,p6,['quantile_transformer'])
con.addConditional(p87,p6,['quantile_transformer'])
con.addConditional(p88,p6,['robust_scaler'])
con.addConditional(p89,p6,['robust_scaler'])
con.addConditional(p90,p7,['extra_trees_preproc_for_classification'])
con.addConditional(p91,p7,['extra_trees_preproc_for_classification'])
con.addConditional(p92,p7,['extra_trees_preproc_for_classification'])
con.addConditional(p93,p7,['extra_trees_preproc_for_classification'])
con.addConditional(p94,p7,['extra_trees_preproc_for_classification'])
con.addConditional(p95,p7,['extra_trees_preproc_for_classification'])
con.addConditional(p96,p7,['extra_trees_preproc_for_classification'])
con.addConditional(p97,p7,['extra_trees_preproc_for_classification'])
con.addConditional(p98,p7,['extra_trees_preproc_for_classification'])
con.addConditional(p99,p7,['extra_trees_preproc_for_classification'])
con.addConditional(p100,p7,['fast_ica'])
con.addConditional(p101,p7,['fast_ica'])
con.addConditional(p102,p7,['fast_ica'])
con.addConditional(p103,p7,['feature_agglomeration'])
con.addConditional(p104,p7,['feature_agglomeration'])
con.addConditional(p105,p7,['feature_agglomeration'])
con.addConditional(p106,p7,['feature_agglomeration'])
con.addConditional(p107,p7,['kernel_pca'])
con.addConditional(p108,p7,['kernel_pca'])
con.addConditional(p109,p7,['kitchen_sinks'])
con.addConditional(p110,p7,['kitchen_sinks'])
con.addConditional(p111,p7,['liblinear_svc_preprocessor'])
con.addConditional(p112,p7,['liblinear_svc_preprocessor'])
con.addConditional(p113,p7,['liblinear_svc_preprocessor'])
con.addConditional(p114,p7,['liblinear_svc_preprocessor'])
con.addConditional(p115,p7,['liblinear_svc_preprocessor'])
con.addConditional(p116,p7,['liblinear_svc_preprocessor'])
con.addConditional(p117,p7,['liblinear_svc_preprocessor'])
con.addConditional(p118,p7,['liblinear_svc_preprocessor'])
con.addConditional(p119,p7,['nystroem_sampler'])
con.addConditional(p120,p7,['nystroem_sampler'])
con.addConditional(p121,p7,['pca'])
con.addConditional(p122,p7,['pca'])
con.addConditional(p123,p7,['polynomial'])
con.addConditional(p124,p7,['polynomial'])
con.addConditional(p125,p7,['polynomial'])
con.addConditional(p126,p7,['random_trees_embedding'])
con.addConditional(p127,p7,['random_trees_embedding'])
con.addConditional(p128,p7,['random_trees_embedding'])
con.addConditional(p129,p7,['random_trees_embedding'])
con.addConditional(p130,p7,['random_trees_embedding'])
con.addConditional(p131,p7,['random_trees_embedding'])
con.addConditional(p132,p7,['random_trees_embedding'])
con.addConditional(p133,p7,['select_percentile_classification'])
con.addConditional(p134,p7,['select_percentile_classification'])
con.addConditional(p135,p7,['select_rates'])
con.addConditional(p136,p7,['select_rates'])
con.addConditional(p137,p7,['select_rates'])
con.addConditional(p138,p31,['valid', 'train'])
con.addConditional(p139,p31,['valid'])
con.addConditional(p140,p45,['manual'])
con.addConditional(p141,p57,['poly', 'sigmoid'])
con.addConditional(p142,p57,['poly'])
con.addConditional(p144,p81,['invscaling', 'constant'])
con.addConditional(p146,p81,['invscaling'])
con.addConditional(p143,p82,['modified_huber'])
con.addConditional(p145,p83,['elasticnet'])
con.addConditional(p147,p102,['True'])
con.addConditional(p148,p107,['poly', 'sigmoid'])
con.addConditional(p149,p107,['poly'])
con.addConditional(p150,p107,['poly', 'rbf'])
con.addConditional(p151,p119,['poly', 'sigmoid'])
con.addConditional(p152,p119,['poly'])
con.addConditional(p153,p119,['poly', 'rbf', 'sigmoid'])
myforb = Forbidden()
myforb.addForbidden(p103,["cosine", "manhattan"],p104,"ward")
myforb.addForbidden(p117,"l1",p115,"hinge")
myforb.addForbidden(p53,"l1",p51,"hinge")
myforb.addForbidden(p48,"False",p53,"l2",p51,"hinge")
myforb.addForbidden(p48,"False",p53,"l1")
myforb.addForbidden(p7,"extra_trees_preproc_for_classification",p2,"multinomial_nb")
myforb.addForbidden(p7,"fast_ica",p2,"multinomial_nb")
myforb.addForbidden(p7,"feature_agglomeration",p2,"multinomial_nb")
myforb.addForbidden(p7,"kernel_pca",p2,"multinomial_nb")
myforb.addForbidden(p7,"kitchen_sinks",p2,"multinomial_nb")
myforb.addForbidden(p7,"liblinear_svc_preprocessor",p2,"multinomial_nb")
myforb.addForbidden(p7,"no_preprocessing",p2,"multinomial_nb")
myforb.addForbidden(p7,"nystroem_sampler",p2,"multinomial_nb")
myforb.addForbidden(p7,"pca",p2,"multinomial_nb")
myforb.addForbidden(p7,"polynomial",p2,"multinomial_nb")
myforb.addForbidden(p7,"random_trees_embedding",p2,"gaussian_nb")
myforb.addForbidden(p7,"random_trees_embedding",p2,"gradient_boosting")
myforb.addForbidden(p7,"random_trees_embedding",p2,"lda")
myforb.addForbidden(p7,"random_trees_embedding",p2,"qda")
myforb.addForbidden(p7,"select_percentile_classification",p2,"multinomial_nb")
myforb.addForbidden(p7,"select_rates",p2,"multinomial_nb")
myforb.addForbidden(p2,"adaboost",p7,"kitchen_sinks")
myforb.addForbidden(p2,"adaboost",p7,"kernel_pca")
myforb.addForbidden(p2,"adaboost",p7,"nystroem_sampler")
myforb.addForbidden(p2,"decision_tree",p7,"kitchen_sinks")
myforb.addForbidden(p2,"decision_tree",p7,"kernel_pca")
myforb.addForbidden(p2,"decision_tree",p7,"nystroem_sampler")
myforb.addForbidden(p2,"extra_trees",p7,"kitchen_sinks")
myforb.addForbidden(p2,"extra_trees",p7,"kernel_pca")
myforb.addForbidden(p2,"extra_trees",p7,"nystroem_sampler")
myforb.addForbidden(p2,"gradient_boosting",p7,"kitchen_sinks")
myforb.addForbidden(p2,"gradient_boosting",p7,"kernel_pca")
myforb.addForbidden(p2,"gradient_boosting",p7,"nystroem_sampler")
myforb.addForbidden(p2,"k_nearest_neighbors",p7,"kitchen_sinks")
myforb.addForbidden(p2,"k_nearest_neighbors",p7,"kernel_pca")
myforb.addForbidden(p2,"k_nearest_neighbors",p7,"nystroem_sampler")
myforb.addForbidden(p2,"libsvm_svc",p7,"kitchen_sinks")
myforb.addForbidden(p2,"libsvm_svc",p7,"kernel_pca")
myforb.addForbidden(p2,"libsvm_svc",p7,"nystroem_sampler")
myforb.addForbidden(p2,"random_forest",p7,"kitchen_sinks")
myforb.addForbidden(p2,"random_forest",p7,"kernel_pca")
myforb.addForbidden(p2,"random_forest",p7,"nystroem_sampler")
myforb.addForbidden(p2,"gaussian_nb",p7,"kitchen_sinks")
myforb.addForbidden(p2,"gaussian_nb",p7,"kernel_pca")
myforb.addForbidden(p2,"gaussian_nb",p7,"nystroem_sampler")
myforb.addForbidden(p2,"decision_tree",p7,"kitchen_sinks")
myforb.addForbidden(p2,"decision_tree",p7,"kernel_pca")
myforb.addForbidden(p2,"decision_tree",p7,"nystroem_sampler")
myforb.addForbidden(p7,"kitchen_sinks",p2,"multinomial_nb")
myforb.addForbidden(p7,"pca",p2,"multinomial_nb")
myforb.addForbidden(p7,"fast_ica",p2,"multinomial_nb")
myforb.addForbidden(p7,"kernel_pca",p2,"multinomial_nb")
myforb.addForbidden(p7,"nystroem_sampler",p2,"multinomial_nb")


def new_obj(params):
    print(params)
    return (np.random.uniform(0, 1))
opt = BO4ML(search_space, new_obj,forbidden=myforb,conditional=con,SearchType="BO",
            max_eval=2300, verbose=True, n_job=1, n_point=3,n_init_sample=5)
xopt, fopt, _, eval_count = opt.run()
print(fopt)