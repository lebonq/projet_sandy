import numpy as np;
import matplotlib.pyplot as plt
import random

#Liste de string possible pour le spectre
liste_matrix_ref = ["PET","PVC","Ink Cartridge","PLA","PELD","PP", "sable"]

#liste_matrix_plastique = ["orange_pp","white_peld","blue_pp","bottle","white_polyester","pvc","polystyrene"]
liste_matrix_plastique = ["PET","PVC","Ink Cartridge","PLA","PELD","PP"]

# PET
liste_longeur_onde_pet = []
liste_data_pet = [-14,-176.6,-195.7,138.2,-357.7,-245.9,163.7,-259.2,-140.3,-365.6,96.5,-390.7,-188.6,-404.9,-14.1,129.4,17.7,38.9,64.5,-430.9,-250,-456.3,-245.1,-77.8,-434.6,36.7,-233,145.8,-230,-90.3,-612.9,-611.8,25.6,-294.3,-445.6,-77.9,-193.2,-154,162.3,-237.5,-22.3,-373.4,-36.3,380.5,-213.3,-198,-215.5,-437.1,-213.9,-264.2,312.7,-236,-265.1,-105.5,-227.9,-393.7,-383.2,-29.8,-286.9,-202,-164.3,-312.2,-78.9,25.8,505.4,-281.2,58.6,-350.4,-299.6,13.5,76.8,185,899,1370.4,1518.2,1733.4,1699,1425.1,1573,1511.4,1766.8,1593.9,1568,1693.2,1629.4,1268,1651.6,1519.8,1667.5,1807,1551.4,1409.4,1409.1,1473.3,1512.4,1681.6,1744,1545.5,1330,1389.3,1742.5,2069,1815.6,2178,1770.7,1722.3,1451.7,1331.4,1200.3,1323.4,1446.4,1297.5,1393.5,1172.4,1592.3,1426.6,1407.7,1436,1092.4,1394.5,957,1429.8,1238.4,1356.6,1217.5,1254.3,1322.7,1533,857.6,1142.4,1718.4,1044.8,1155.9,1715.8,1221.2,1491.8,822.2,1307.5,1440.2,814.6,1137.9,1212.7,958.4,960.8,1387.5,1157.7,994.6,1026.2,1155.8,665.8,1173.8,1337.9,1357.5,1331.6,881.5,1155.8,931.1,921.9,1189.1,1320.6,1298.6,1230.5,1491.7,1192.5,1158.1,457.5,1142.5,1023.1,980.1,914.1,962.4,1155,1062.6,946.1,958.1,1150.1,1113.7,1111,837.7,1089.6,910.1,1185.3,805,974.2,755.8,792.9,961.6,1184.7,1292.2,1072.4,973,944.2,855.9,699.2,512.7,789.4,932.5,1003.1,858.2,1045.5,738.5,1161.2,1130.8,1072.9,885.5,886.3,1051.3,978.4,1096.7,1029.6,513.6,728.4,620.6,495.5,841.8,644.2,871.4,731.8,689.7,1014.8,611.6,791.5,827.7,865.4,892.5,909.9,842,917.2,897.7,731.2,889.4,748.6,944.2,971.2,1029.4,1280.2,2707.6,3897.8,3667.6,2063.3,1520.5,1311.9,1248.7,1556.4,1305.8,1359.4,1250.7,735.6,946.1,1119.6,1104.3,1114.6,1795.3,3126.6,4524.6,4308.1,2701.6,1395.2,1282.5,1124.9,982.8,1078.9,871.9,771,1270.6,986,895.2,1094.7,856.9,949.2,666.6,765.6,571.5,847.8,992.9,552.6,632.9,772.8,742,829.8,497.7,862.6,475.4,565.1,1130.1,781.2,284.5,736.8,739.9,281.1,793.5,1192.4,689.3,866.9,690.2,942.9,1353.4,2537.8,4016,4274.9,2543,1376.5,1288.7,965.6,816.1,504.1,871.2,646.2,610.9,705.7,821.8,351.6,664.4,363.8,649.5,1042.2,520.8,401.7,837,691.4,982.9,667.2,825.7,428.7,634.5,61.7,702.8,432,689.5,393.3,1140,1234.7,1730.6,2284,1342.7,1301.9,1873.2,1637.1,2351.2,3182.2,3162.9,2518.4,2307.4,2024.8,1715.2,1609.2,2092.6,1922.5,1257.1,976.6,1070.3,796.5,302.4,527.1,359.9,593.4,578,312.2,729.6,621.2,348.6,110.8,411.6,143.6,144.2,414.5,341.7,223.9,426.8,353.4,346.6,708.8,539.3,561.9,370,459.8,162.1,196.5,181.8,652.6,188.3,487.8,281.5,326.4,340.9,330.8,222,356.7,300.3,180.7,408.2,-3.1,436.3,342,110.7,83.3,347.2,134.9,72.8,643.8,201.2,460.8,94.4,253.9,15.1,135.8,333.9,163,295.4,245,-76.3,31.6,388.7,152.4,323.6,122.5,790.1,277.9,453,257.9,141.8,226.4,167.2,269.3,176.2,-206.1,-23.9,148.6,-105.6,521.9,39.5,27.6,-157.6,-73.7,-181.5,20,414.5,120.6,242.4,158.2,4.2,238,227.4,7.8,158.7,207.2,212.5,97.4,128.6,344.1,-94.8,100.2,394.2,-14.6,158,79.1,148.9,80.7,-105.4,-263,-263.9,137,59.8,-46,91.3,9.3,-231.3,398.8,240.1,-246.1,193.3,108.7,-173.1,421.1,70.8,189.1,322.8,68.8,-17.3,-39.5,533.2,-143.5,-97.7,71.4,245.9,157.2,-45,218.6,-57.5,-257.5,262.9,58.4,179.4,91.2,26.1,-4.2,-27.8,26.8,339.1,-18,89.4,69.4,773,4.8,26.3,8.6,296,8.4,93.7,-58.4,123.1,565.6]

# PVC
liste_longeur_onde_pvc = []
liste_data_pvc = intensity_PVC= [452.105,445.858,439.611,435.863,431.49,425.66,421.704,416.081,411.707,408.167,403.378,398.588,395.465,392.549,388.801,384.22,379.847,371.935,367.979,364.023,357.984,352.986,349.654,345.281,340.492,337.159,333.619,329.663,322.791,316.335,311.129,307.172,303.841,301.758,296.76,293.221,290.097,285.932,283.641,279.892,276.144,273.229,268.023,260.526,255.944,251.572,247.823,244.283,239.494,236.162,232.83,229.29,226.583,223.251,220.336,217.004,213.255,210.548,208.049,204.301,202.01,199.303,196.387,193.68,190.139,188.057,184.725,182.435,179.102,176.187,173.272,169.107,164.318,161.403,158.488,155.781,152.241,147.035,144.327,141.62,138.705,135.581,131.625,128.501,125.794,123.295,120.171,117.465,114.758,110.176,107.47,104.763,102.056,98.9321,95.6004,92.4778,89.1459,86.0224,82.2739,78.5249,74.9863,62.4943,66.6575,64.5757,60.2048,58.7486,55.8341,53.1272,50.4206,46.6726,42.7159,40.0092,36.8861,33.7624,28.5565,25.8494,23.9762,20.8536,18.7717,9.40351,6.69726,5.03319,8.16259,11.292,13.1679,14.0022,15.6697,18.5869,22.1278,25.2517,34.2069,39.6217,41.7062,43.3747,46.0836,48.5839,57.1229,62.5373,67.1191,71.7015,77.1159,81.4892,84.4049,88.1539,91.2793,86.699,82.5343,79.4102,74.2044,69.2067,64.4172,60.0444,54.839,49.0085,45.6772,42.7627,39.4317,33.6015,27.9804,22.9871,21.3226,18.825,16.9525,13.4142,10.7093,11.1309,12.5913,16.3447,19.2622,22.1794,24.2641,26.5573,29.0583,32.1838,36.9744,40.5149,45.5136,50.0954,53.6365,59.2594,64.6738,70.2966,74.6694,91.9546,80.9172,84.0411,87.7895,94.6616,98.4097,102.367,106.949,110.905,114.446,119.027,121.526,125.066,127.981,130.689,133.604,199.832,143.393,147.975,157.553,160.469,164.843,174.424,178.173,182.338,188.377,192.75,195.25,204.413,208.786,213.368,218.158,223.155,227.946,232.319,239.399,236.9,235.652,230.655,226.073,220.659,215.661,211.704,207.54,202.958,199.835,197.128,191.714,187.132,183.592,179.635,175.678,171.722,166.933,162.352,160.061,155.896,147.983,143.401,141.527,139.236,136.946,134.447,131.74,129.866,127.991,125.701,123.827,122.577,120.911,118.204,114.247,112.373,109.667,106.543,103.003,101.337,98.8378,95.0899,91.1332,88.8421,85.5102,82.1786,79.6805,77.5997,81.5568,84.6805,87.8043,90.72,93.8437,98.0088,100.716,105.297,108.63,113.42,117.168,121.125,127.165,133.829,138.41,142.576,146.116,150.489,154.238,157.778,162.36,166.527,161.113,156.532,152.575,148.41,145.287,140.706,136.332,131.127,124.463,123.422,119.881,115.717,111.552,105.514,104.472,101.765,98.8494,96.5589,93.0189,90.1038,85.9392,81.1494,78.2341,75.1104,72.1954,70.1129,67.1975,63.8659,61.1587,58.2429,54.2862,51.5794,48.4561,45.5408,43.2503,40.7519,38.0449,35.5459,32.6307,30.3407,23.0527,18.6795,15.9731,12.8503,8.8944,5.56379,3.89896,1.40248,-0.470218,-1.71779,-4.42138,-2.33607,1.62175,5.37095,10.3696,13.9108,12.0381,11.207,9.54329,8.08766,6.2161,3.92768,2.26456,6.43158,8.30884,10.6014,13.5184,16.6436,19.769,18.3138,13.7335,10.4021,7.48992,8.32709,9.37175,12.0829,15.4177,18.9596,23.751,32.5002,36.8743,31.0451,26.6727,24.5912,20.6355,16.2637,11.8916,7.10272,4.18784,1.48273,3.5671,6.48331,9.39875,14.813,19.8114,38.3476,27.0999,30.8489,34.3891,36.8924,32.7284,29.8139,25.2329,23.9842,22.3182,20.862,16.6973,14.6158,11.4932,21.9116,18.5787,24.6209,27.329,24.8316,21.0843,19.4208,22.7539,42.9561,31.293,35.8751,37.9578,39.832,57.7452,50.6623,53.5785,56.7081,37.5516,49.6285,46.5052,43.7982,41.0914,33.1788,30.2633,27.7655,24.8521,21.7298,18.3988,16.11,13.4043,10.2825,15.2821,18.8231,66.5126,26.1111,28.4024,29.6519,33.4005,35.6912,42.1472,43.8136,46.9373,49.6445,61.9312,66.5126,71.0939,73.8011,76.9253,78.383,87.3382,84.8389,90.254,92.9612,95.0437,97.7509,102.124,104.833,100.669,96.7121,91.5062,87.1334,81.0946,73.5978,70.2662,65.8932,62.5613,58.1879,54.8562,51.5246,47.7762,45.2774,40.9042,37.364,34.2402,31.5331,28.2018,24.8696,20.7049,17.7897,14.6669,12.3775,9.87972,7.38457,6.37452,7.18279,7.60251,6.77295,6.77542,6.36235,6.57383,6.3711,4.12756,7.21397,6.80205,7.22101,5.97344,5.35136,5.35421,4.94628,3.90809,4.12052,3.7065,3.91874,0.0539158,3.09241,2.88645,2.88911,1.85035,2.06069,1.44375,1.65484,0.622932,0.626926]

# INK CARTRIDGE
liste_longeur_onde_inkCatridge = []
liste_data_inkCartridge = [249.62,143.02,272.4,395.48,355.76,132.96,294.5,246,186.22,416.78,252.9,170.4,475.72,190.36,104.66,303.34,121.68,197.52,271.84,365.96,296.46,257.44,376.22,156.78,293.66,202.72,287.22,194.56,104.62,271.86,335.94,368.86,273.44,310.22,186.38,128.3,142.14,315.3,362.52,257.62,466,280.7,249.62,296.78,156.16,335.6,185.72,186.64,269.14,290.32,102.1,337.4,346.04,344.52,305.52,329.72,234.9,391.94,249.58,159.92,310.54,412.9,347.58,322.9,241.52,361.82,166.42,334.82,321.64,982.84,2520.82,5974.4,10569.96,14903.74,16459.2,17085.12,17194.22,17399.6,17883.88,18358.26,18633.36,18961.46,18389.9,18829.72,18878.78,18785.52,18547.42,18491.1,18460.56,18225.66,18275.5,18621.94,18709.72,18291.82,18572.84,18518.96,18326.84,18164.78,18212.14,18051.96,17864.92,17822.96,17693.66,17885.6,17766.86,18041.12,17817.48,17498.28,17430.6,17651.8,18017.86,17883.7,17777.72,17518.46,17471.14,17519.5,17634.2,17352.58,17327.32,17486.5,17146.24,17141.22,17176.6,17075.98,16991.46,16997.58,16938.56,17074.78,16410.4,16860.28,16803.08,16938.84,16667.4,16773.42,16912.24,16890.92,16612.92,16527.58,16490.34,16240.06,16490.2,16391.8,16031.26,15948.16,15874.56,16087.02,15767.86,15899.94,15789.04,15852.9,15725.34,15708.12,15462.96,15602.32,15922.6,15569.28,15750.04,15580.98,15692.78,15451.4,15204.06,15251.22,15213.3,14899.88,14828.82,14706.68,14582.76,14445.78,14192.72,14244.16,14275.64,14066.22,13989.26,13774.6,13663.94,13779.24,13575.86,13522.34,13575.44,13504.7,13623.3,13590.4,13246.96,13198.38,13172.34,12878.24,12850.1,12861.7,12744.52,12876.88,12852.04,12845.24,12804.2,12781.98,12682.82,12362.08,12283.22,11937.64,11981.42,11987.16,11785.16,11703.34,11782.92,11792.38,11779.32,11707.84,11699.48,11487.4,11480.72,11476.92,11471.44,11450.88,11476.44,11440.54,11358.7,11220.5,11337.18,11267.26,11336.08,11219.1,11342.96,11131.56,11207.36,11171.22,11073.8,10995.12,10884.44,10890.84,10747.88,10740.6,10753.64,10331.86,10418.74,10385.34,10431.58,10823.3,11730.8,12529,12213.32,11380.72,10846.5,10659.24,10532.24,10457.62,10284.58,10030.54,9791.98,9714.06,9621.1,9530.06,9555.98,9768.8,10232.8,11374.84,12070,11260.24,10717.3,10034.78,9720.92,9453.96,9239.9,9185.62,9139.86,9495.3,9342.14,9339.64,9220.52,8961.04,8875.46,8751.64,8573.56,8535.06,8376.66,8419.22,8296.8,8268.74,8164.68,8283.24,8090.44,7958.04,7942,7916.98,7946.3,7798.44,7762.78,7881.58,7654,7685.88,7643.56,7868.96,7759.4,7903.96,7761.16,7942.32,7783.32,7597.08,8208.88,9298.54,10611.14,10127.94,9013.94,8303.06,7955.04,7507.88,7443.28,7455.12,7113.58,6930.16,6793.46,6684.04,6775.38,6680.74,6552.58,6736.12,6536.08,6307.44,6611.26,6655.82,6714.6,6752.52,6641.32,6630.14,6610.28,6267.72,6300.5,6473.48,6345.24,6229.96,6153.32,6419.64,6321.08,6523.64,6913.02,7030.82,7049.58,7000.4,7140.5,7640.2,8789.04,9130.48,8889.24,8059.7,7948.58,7773.72,7673.06,7570.2,7523.4,7075.66,6838.22,6423.34,6082.4,5804.12,5671.98,5463.7,5504.1,5288.1,5369.58,5252.24,5085.02,5117.04,5111.6,5010.68,5017.88,4952.82,4869.2,4767.82,4821.42,4851.02,4865.58,4694.9,4796.68,4684.6,4628.72,4763.18,4797.5,4711.52,4655.7,4503.32,4483.36,4602.28,4483.72,4358.98,4519.32,4673.16,4530.28,4508.48,4503.3,4340.44,4372.08,4463.96,4155.08,4413.14,4196.76,4392.12,4055.04,4278.66,4050.3,4182.98,4071.32,3971.92,4101.3,3972.26,3912.24,3911.9,3708.96,3694.58,3591.3,3856.06,3846.06,3731,3699.32,3562.92,3623.98,3545.78,3675.9,3647.96,3535.96,3586.16,3462.88,3368.92,3531.66,3446.96,3322.42,3320.88,3309.94,3428.12,3167.14,3329.18,3281.28,3189.66,3408.9,3081.2,3034.34,3190.92,3161.18,2980.24,3143.04,3221.98,3121.5,3092.14,3103.14,2972.28,2954.4,2969.66,2997,2817.88,2954.34,2652.48,2680.72,2839.64,2891.08,2799.26,2685.94,2833.02,2680.8,2684.42,2578.86,2743.24,2752.38,2487.36,2830.56,2617.14,2651.1,2524.86,2536.94,2685.6,2556.52,2509.42,2681.22,2465.34,2597.16,2491.6,2544.82,2372.02,2451.24,2430.04,2418.04,2625.6,2536.94,2376,2447.92,2345.12,2363.06,2457,2468.18,2377.42,2398.9,2306.24,2278.18,2301.9,2212.66,2309.26,2253.7,2173.76,2145.2,2213.3,2190.28,2063.56,2272.46,2269.76,2186.16,2158.1,2072.36,2161.48,2085.14,2003.58,2041.4,1870.78,2122.02,1977.06,2059.5,2072]

# PLA
liste_longeur_onde_pla = []
liste_data_pla = [316.06,292.84,347.14,419.46,239.22,317.08,433.46,372.92,148.58,335.18,267.34,334.68,233.94,169.02,350.94,206.02,461.68,201.16,324.12,165.72,299.74,145.26,230.86,277.82,130.6,326.42,77.48,303.04,292.36,404.26,32.06,320.54,306.22,290.44,341.26,283.22,137.14,315.36,200.8,315.18,295.84,156.86,270.12,214.1,211.78,380.34,168.08,268.78,319.24,171.5,235.28,291.34,297.54,259.28,273.24,141.84,364.48,259.04,237.76,440.58,266.78,342.44,314.7,279.1,177.84,274.74,198.7,332.76,372.1,578.82,993.18,1772.58,3241.9,4423.62,4814.04,4996.4,5019.38,4931.8,5268,5347.82,5749.24,5586.28,5819.44,5739.64,5742.36,5698.78,5644.02,5900.3,5867.96,5930,5939.86,5845.6,5873.96,5773.94,5705.02,5740.9,5555.48,5248.6,5325.56,5186.7,5185.84,5184.82,5248.74,5095.02,5140.32,5090.96,4934.48,4952.46,5170.96,4901.54,5019.56,5054.82,4985.66,5172.86,5125.36,4965.72,5075.38,4753.14,4918.2,4767.16,4778.06,4780.92,4775.46,4817.14,4798.12,4673.9,4753.48,4792.32,4807.22,4893.2,4742.36,4740.56,4595.12,4702.76,4616.66,4773.44,4635.14,4506.8,4484,4428.48,4568.72,4417.92,4418.28,4154.66,4289.72,4294.76,4271.44,4340.74,4172.5,4297.44,4111.28,4327.1,4268.34,4294.5,4336.56,4384,4210.54,4128.66,4009.2,4115.64,4061.46,4039.58,4047.68,4124.06,4074.6,4107.72,3898.64,3958.98,3809.36,3826.48,3722.72,3940.66,3832.92,3628.14,3648.9,3741.84,3643.8,3576.32,3577.9,3507.3,3711.32,3493.64,3528.82,3543.44,3539.88,3610.74,3465.88,3763.92,3905.96,3929.02,4514.06,4760.52,4857.28,4585.78,4027.14,3767.44,3586.2,3423.08,3171.48,3399.24,3181,3139.68,3146.56,3122.38,3178.4,3158.98,3232.02,3122.78,3218.96,3137.82,3051.8,3272.3,3046.92,3246.42,3100.08,2952.04,3032.24,2974.2,3012.2,3143.36,2936.14,2910.52,3063.02,3147.12,2898.18,2979.32,2880.24,2926.76,3092.98,3003.52,2935.68,2987.46,3001.74,3222.48,3051.7,2924.66,2886.14,2908.68,2934.66,2667.8,2785.64,2705.4,2963.68,3089.04,2728.88,2858.72,2822.58,2805.78,2927,2939.52,2726.74,2971.52,3147.08,2998.16,2886.12,2840.94,2779.54,2810.48,2738.48,2861.86,2552.34,2576.78,2578.48,2747.3,2606.26,2620.16,2511.62,2681.74,2592.3,2702.04,2529.8,2448.7,2380.58,2506.2,2375.84,2527.84,2385.76,2596.26,2360.26,2429.94,2332.18,2352.9,2206.12,2283.06,2363.84,2309.72,2209.76,2363.92,2203.52,2384.44,2254.9,2383.96,2323.68,2445.34,2320.36,2268.6,2365.24,2349.5,2402.9,2185.24,2290.16,2342.64,2337.24,2241.64,2287.28,2246.48,2167.06,2086.8,2296.82,2327.36,2186.14,1975.14,2211.48,2135.78,2020.16,2278.46,2082.24,2357.96,2132.16,2123.84,2117.26,2050.9,2166.16,2129.7,2035.52,2118.16,2182.28,2129.02,1805.8,1797.3,1927.5,1966.82,1898.88,1882.12,1979.58,1850.26,1893.88,1867.74,1751.8,1833.56,1930.02,2096.88,2135.42,2129.98,2012.1,2117.9,1952.2,1898.82,1914.78,1807.04,1695.86,1749.74,1654.38,1776.22,1617.32,1792.58,1694.98,1621.82,1637.36,1630.86,1529.7,1711.06,1537.9,1546.94,1499.9,1614.14,1406.16,1710.22,1527.12,1485.38,1532.68,1364.42,1485.28,1514.92,1376.98,1445.5,1353.68,1480.62,1496.96,1564.4,1338.2,1557.02,1266.2,1482.36,1458.1,1404,1319.72,1328.42,1398.42,1399.18,1319.36,1466.62,1321.58,1445.44,1401.14,1155.4,1217.56,1228.26,1286.94,1330.54,1101.7,1096.12,1225.92,1379.02,1256.98,1116.6,1238.74,1072.22,1134.36,1259.96,1058.02,1241.34,1056.4,1296.34,1248.1,1259.56,1222.76,1099.48,1048.18,1012.88,1205.84,1014.04,947.84,1009.34,1031.78,979.02,1034.36,1082.78,1027.64,1000.86,1113.98,1079.72,1002.32,1006.82,1046.1,1193.88,1052.18,1066.02,1169.94,997.96,1117.38,1077.54,1188.04,1128.5,1146.76,1110.38,1164.8,1008.36,1028.64,841.76,912.74,798.18,821.74,871.66,884.64,957.44,784.92,794.22,865.18,776.74,727.26,864.8,816.5,892.74,687.48,834.88,845.52,856.52,818.16,673.36,891.78,861.96,855.94,701.22,694.54,787.28,649.56,748.1,871.32,802.36,762.88,831.18,738.7,793.5,608.04,732.44,648.04,735.36,852.64,691.84,793.74,695.14,724.44,803.68,707.9,610.84,772.68,749.26,691.72,634.34,747.52,652.02,576.74,721.56,730.72,668.46,671.8,545.54,584.82,776.52,679.56,698.66]

# PELD
liste_longeur_onde_petd = []
liste_data_peld = [292.68,438.32,354.52,366.1,208.6,328.28,229.04,540.26,262.34,226.54,298.4,354.4,411.78,280.88,249.04,291.26,229.32,145.58,209.42,378.18,445.54,356.36,230.46,323.36,321.68,410.32,173.86,174.42,262.08,408.92,364.62,241.44,324.5,133.76,224.84,131.76,167.66,233.1,222.8,344.24,88.62,165.36,214.88,214.94,100.14,242.14,240.06,358.64,333.32,285.7,262.58,289.36,320.32,281.72,112.84,126.48,317.16,170.56,93.18,104.98,138.66,87.28,99.72,206.14,255.24,458,327.78,256.52,269.94,417.5,594.6,978.36,1428.64,1913.58,2345.3,2299.6,2339.96,2400.82,2445.2,2732.36,2722.48,2743.46,2723.18,2537.94,2560.8,2701.08,2679.66,2578.28,2632.04,2678.22,2597.56,2536.6,2741.92,2596.28,2554.82,2557.98,2508.84,2544.96,2400.36,2595.18,2371.02,2465.02,2762.32,2681.86,2310.04,2439.88,2291.16,2370.46,2265.36,2313.14,2308.42,2395.82,2423.64,2410.94,2218.8,2244.56,2152.76,2236.6,2325.3,2262.08,2139.3,2183.88,2236.78,2068.5,1940.5,2131.22,2117.82,2065.32,2208.72,2167.92,2168.86,2151.58,2162.92,2061.38,2012.48,2326.58,2154.84,2138.58,2137.58,2046.24,2117.32,1991.52,1995.24,2018.32,1984.44,1959.82,1892.64,2054.36,1945.7,1977.46,2032.48,1985.22,2023.54,2056.9,1903.44,1838.9,2127.26,1844.32,2008.54,2048.2,1911.02,1913.9,1871.84,1919.76,1914.4,1958.7,1802.66,1773.08,1766.48,1949.68,1781.32,1680.2,1729.78,1867.6,1889.08,1996.94,1696.14,1968.04,1916.68,1796.98,1886.98,1907.18,1860.72,1843.92,1702.22,1814.24,1820.72,1787.78,1849.62,1781,1882.46,1908.26,1890.84,1903.94,1929.56,1860.9,1858.1,1931.64,1814.16,1796.34,1725.52,1698.18,1677.06,1699.8,1718.98,1675.38,1649.4,1682.72,1775.4,1631.4,1626.42,1682.28,1756,1608.06,1703.94,1556.24,1808.8,1628.86,1724.64,1844.5,1952.7,1648.5,1898.74,1838.82,1603.18,1710.36,1669.5,1714.82,1766.88,1848.12,1709.26,1747.76,1815.78,1852.84,1864,2267.48,3515.04,4700.06,4056.96,3071.54,2457.34,2304.62,2119.44,2139.76,1980.08,2031.38,1857.32,2016.52,1884.16,1924.42,2153.18,2226.72,2641.1,4094.66,5269.46,4778.4,3349.6,2221.7,1994.1,1907.3,1875.7,1725.58,1777.28,1761.14,1996.58,2139.42,1898.18,1839.44,1718.32,1781.6,1557.84,1545.56,1559.08,1583.98,1526.98,1635.2,1629.76,1637.98,1508.98,1629.42,1563.74,1577.74,1678.64,1676.78,1492.38,1557.24,1605.36,1725.74,1562.82,1548.86,1684.7,1708.28,1686.2,1725.12,1810.62,1950.86,2330.14,3644.5,5309.38,4763.84,3294.82,2293.06,2084.72,1798.16,1865.04,1553.24,1577.52,1467,1404.62,1441.84,1473.04,1416.34,1388.12,1390.48,1476.96,1278.5,1169.34,1499.28,1549.18,1700.4,1596.16,1464.38,1314.16,1379.08,1422.2,1431.44,1487.18,1295.78,1358.76,1565.66,1500.4,2079,2603.94,2659.04,2275.58,2362.18,2281.78,2535.26,3410.4,4000.56,3850.3,3242.6,2865.32,2665,2759.9,2742.04,2845.22,2482.36,2311.28,1803.34,1710.96,1579.14,1454.6,1237.4,1288.52,1302.68,1362.68,1143.54,1055.9,1137.28,993.42,1075.44,1081.96,1231.14,1026.12,979.42,1137.48,1020.74,1028.08,1152.04,974.04,995.22,991.86,1039.06,1170.1,843.7,875.94,840.14,986.08,1059.8,1016.66,995.3,1073.42,886.54,975.68,861.02,949.92,912.96,1038,1042.62,879.02,880.82,904.82,735.3,872.96,838.66,889.72,955.74,854.58,842.6,1011.38,862.7,810.56,694.34,839.1,950.78,881.48,824.68,779.68,822.86,802.72,824.3,992.12,768.26,899.82,818.5,807.12,863.64,748.02,671.84,694.98,755.54,679.74,606.2,722.18,701.04,635.74,944.1,741.1,753.42,565.7,769.3,716.9,679.32,741.38,641.04,657.94,766.54,749.06,651.32,733.3,709.78,547.04,573.94,748.96,690.36,620.16,741.22,652.78,669.86,548.06,605.96,622.42,623.72,581.32,622.26,519.3,725.48,636.6,566.68,648.92,603.82,588.9,667.9,468.26,511.04,343.6,625.94,792.16,628.06,570.76,600.92,595.58,510.02,608.2,496.56,521.28,554.72,504,526.22,598.72,593.82,534.26,454.18,390.82,542.6,525.52,696.56,348.54,560.5,512.4,376.88,440.52,457.98,545.42,503.64,582.8,372.74,434.98,444.48,534.22,521.24,483.28,440.26,482.3,562.24,430.2,576.9,535.92,436.44,509.72,527.82]

#PP
liste_longeur_onde_pp = []
liste_data_pp = [204.716,204.716,204.716,204.716,204.161,204.161,204.161,204.716,205.825,202.497,195.839,189.182,183.079,178.641,188.072,194.73,200.832,206.935,205.825,204.161,204.716,208.044,205.825,207.49,206.935,209.709,203.606,208.044,214.702,216.366,211.373,205.27,193.62,190.846,206.935,211.928,215.257,216.366,223.578,223.578,225.243,227.462,234.674,241.886,247.434,255.201,260.194,264.078,265.187,261.304,257.42,259.085,269.071,274.064,326.214,334.535,346.186,373.37,381.137,392.788,412.76,423.856,499.307,454.369,461.581,477.67,509.847,520.388,529.265,539.806,549.237,557.004,567.545,579.75,593.065,620.804,628.017,639.667,650.763,662.968,680.166,692.372,712.899,723.44,735.09,746.741,762.829,775.589,792.788,818.863,828.849,846.602,854.369,883.773,894.313,910.957,995.284,926.491,948.128,959.223,968.655,984.743,1006.93,1077.39,1039.11,1026.35,1057.42,1189.46,1100.14,1115.67,1140.08,1152.84,1168.38,1180.03,1203.33,1275.45,1239.39,1252.15,1263.25,1290.43,1307.07,1339.81,1327.05,1350.9,1362,1371.43,1385.85,1401.94,1413.59,1425.8,1462.41,1444.66,1493.48,1466.85,1408.04,1389.74,1376.42,1351.46,1288.77,1334.26,1319.28,1297.64,1170.6,1268.24,1247.71,1236.06,1226.63,1214.42,1206.1,1192.23,1180.03,1117.89,1150.07,1125.66,1104.02,1093.48,1084.05,1071.84,1060.19,1049.1,1040.22,1027.46,1016.92,1006.38,994.175,981.969,970.874,959.223,942.58,923.162,912.621,804.438,890.985,872.122,859.362,836.061,823.856,765.049,783.911,773.37,748.96,739.528,728.433,715.673,697.92,685.714,676.283,661.304,652.982,637.448,627.462,615.257,593.065,581.969,568.1,557.004,548.682,538.696,527.046,515.395,504.3,483.773,472.677,455.479,443.273,431.623,419.972,408.877,389.459,404.438,380.028,367.268,355.062,351.734,343.967,350.069,361.165,372.816,382.247,390.569,400.555,418.308,427.184,443.273,451.595,458.252,467.684,476.56,486.546,535.368,556.449,588.072,638.003,615.811,623.578,649.653,660.749,671.29,680.166,687.379,695.7,702.913,713.454,721.775,729.542,742.857,757.836,792.788,903.19,814.979,826.075,836.616,847.157,858.807,871.013,880.999,893.204,939.806,927.601,953.675,971.429,990.291,1018.59,1035.78,1047.99,1070.74,1043.55,1013.59,830.513,954.23,942.58,930.374,918.724,908.738,895.978,878.225,868.239,856.588,842.718,818.863,786.685,796.671,773.37,757.282,742.302,717.892,705.687,696.81,686.269,672.399,661.304,650.208,640.222,627.462,618.031,609.709,586.408,527.601,565.881,552.011,537.587,514.286,502.635,489.875,479.889,450.485,422.191,412.205,398.89,386.13,375.035,359.501,340.083,323.994,297.92,306.241,287.933,280.166,294.591,309.015,264.078,238.003,228.017,224.688,196.949,205.825,215.257,208.599,220.804,221.914,188.627,206.935,214.702,206.38,193.62,221.914,203.606,223.024,189.736,200.277,223.024,235.229,244.66,260.749,275.173,288.488,301.248,308.46,314.008,290.153,280.166,267.406,252.427,251.872,234.119,220.25,214.147,204.716,183.634,193.62,184.743,170.874,175.867,188.072,208.044,179.75,195.284,206.935,231.345,224.133,216.921,234.119,261.859,274.064,286.824,295.146,302.913,312.344,325.104,338.419,332.316,319.001,307.351,294.591,258.53,248.544,235.229,234.674,220.25,206.935,205.825,214.147,210.264,220.25,210.264,225.243,230.791,184.189,240.777,230.236,252.982,285.16,295.7,307.351,317.892,329.542,346.741,356.172,367.822,446.047,427.739,436.061,463.245,478.779,517.614,500.416,532.594,548.682,611.928,588.627,601.942,625.797,632.455,574.203,560.333,542.025,521.498,504.3,489.32,473.786,459.917,418.308,380.583,366.713,341.748,326.214,309.015,294.591,280.166,262.413,245.215,230.791,219.14,208.599,198.058,192.51,176.422,199.168,207.49,214.147,233.564,242.996,256.311,286.824,299.584,315.673,326.768,338.974,361.165,379.473,398.336,411.096,390.569,347.85,335.645,318.447,305.132,271.845,241.331,225.798,191.956,186.963,179.196,165.326,188.627,199.168,176.976,187.517,193.065,193.065,166.99,179.75,210.818,226.907,222.469,244.66,259.085,275.173,292.926,319.001,336.2,348.405,371.151,363.939,330.097,310.125,310.68,323.44,337.864,316.227,296.81,282.386,265.187,246.879,215.257,201.942,189.736,175.312,166.436,172.538,179.196,158.114]

# SABLE
liste_longeur_onde_sable = []
liste_data_sable = [47.7,-70.3,206.4,127.4,441.1,303.2,131.9,297,572.7,240.5,357.8,124.5,182.4,598.4,238.8,169.6,-246.6,205,171.5,78.9,211.4,55.4,-69.3,372.9,-123,40.9,110.6,307.6,250.8,208.9,264.5,135.2,23.2,114.4,107.7,233.5,236.2,150.4,171.8,264.4,487.5,-18.8,298.6,336.8,389.1,515.2,118.9,574.1,-173.6,273.2,100.4,212.3,205.5,398.3,169.3,420.6,328.5,471.3,141.9,386.6,120.6,247.7,670.3,257.7,54.9,272.7,542.6,416.1,593.7,1146.3,2066.5,5275.9,8612.5,11880.1,13749,13857.2,14533.9,14671.3,15453.5,15526.9,15767.8,16187.4,16687.7,16015.6,16058.7,16122.4,15934,15731,16022.7,15602.4,15796.7,16206.1,15734.3,15840.1,15649.6,15357.4,15557.7,15288.1,15380.3,15618.5,15885.6,16063.6,17856.7,18247.5,16881,15427.3,14534.6,14854.6,14568.3,14379.3,14847.8,14333.9,14544.2,14391.2,14318.9,14270.9,13921,13820.8,13801.7,13419,13671.2,13358.7,13204.9,13467.3,13518,13102.7,12969.5,13024.9,13164.4,12834.1,12873.1,12946.8,13134.3,13037.3,12511.1,12621.9,12126.6,12231,12395.7,12081.3,11899.3,11993.4,11968.3,11756.4,11681.9,11401,11452.2,11622.2,11430.6,11524.4,11535.9,11596.4,11357.4,11623,11535.8,11240.8,10792.7,11322,10719.7,11149.1,10574,10738.9,10566.9,10758,10748.9,10484.4,10073.8,10187.4,10072.7,10254.6,9834.3,9979.1,9711,10039.1,9728.9,9792.2,9640.2,9479.7,9312.3,9479.3,9398.5,9197.1,8929.7,9128.8,9077,8574.5,8740.9,8455.2,8680.2,8420.2,8580,8461,8362.2,8532.3,8583.8,8317.9,8451.1,8346.7,8011,8189.6,8069.6,8364.2,8048,8130.7,8249.9,7985.6,8263.2,7776.6,8262.9,8117.8,8141.3,8015,8003.1,8274.7,7852.4,8031.5,7550.5,7997.7,7771.7,7993.1,8043.7,7856,8043.7,7772.5,7784,7605.3,7675.8,7390.4,7436.9,7438.7,7494.7,7445.2,7527.3,7109.6,7175.7,6910.6,6607.2,6658,6947.2,6858.2,7031,6725.1,7155.7,6831,6880.2,6940.6,6768,6923.6,6515.6,6762.6,6391.5,6918.2,6778.2,6859.7,6551.9,6360.2,6605.3,7203.5,6622,6805.2,6716,6639.3,6604.5,6760.4,6515.9,6790.5,6307.1,6353.8,6387.4,6221.3,5845.9,5848.1,5898.1,6110.2,5906.2,6239.6,5601,5869.6,5931.9,5943.6,6181,6421.2,5747.8,5418.5,5666.1,5701.1,5983.2,5664.1,5841.7,5973.6,5967.6,5574.5,5840.2,5728.9,5308.8,5764.3,5388,5729.4,5660.2,5287.4,5240.4,5210.7,5091,4913.8,4982.8,5096.9,5248.5,4803.5,4896.8,5350.4,5055.5,5009.1,5059.2,5038.5,4692.2,5002.8,4904,4778.4,4545.3,5023.9,4795.9,4579.8,4559.3,4846.3,4847,4721.7,4693.2,4648.4,4891.7,4768.3,4903.1,4957,4566,4747,4813.3,4569.5,4580.5,4346.2,4509.6,4433.3,4302.4,4428.2,4338.7,4092.1,4255.7,4218.9,4328,4260.6,4164.2,4153.2,4144.5,4212.4,4510.4,3811.5,4118.9,4102.1,3951.9,3926.6,3399.1,3748.7,4097.3,3981.5,3880.8,3435.9,3583.3,3652.1,3898.3,3458.2,3699.9,3870.2,3488.3,3955.7,3807.1,3606.3,3400.1,3230.2,3662.9,3413,3698.3,4032.3,3585.2,3299.8,3451,3607.2,3105,3239.9,3736.7,3358.9,3198.6,3173.7,2987.6,3312.2,3452.3,3120.7,3138.4,3108.7,3110.3,3097.2,2794.1,3048,2868.8,2591.3,3204.8,3067.2,2726.8,3023.6,2851.6,2725.1,2984.1,2790.6,2548.5,2495,2406.3,2780.7,2715.3,2575.5,2370,2558.5,2751.9,2697.2,2455.4,2457.2,2554.5,2358.2,2713.8,2492.7,2325.6,2294.9,2637.8,2938.4,2526.7,2681.8,2640.7,2579.7,2249,2178,2436.4,2230.4,2115,2342.5,2134.8,2410.9,2498.1,1919.6,2219.5,2616,2233.6,2080.1,1933.1,2129.6,2140.9,1872.3,2040.1,2021.6,1949.9,2295.2,1990.7,1770.3,2003.9,1974.4,2027.1,2126.5,2320.1,1750.2,2081.9,1882,1913.5,1986.6,1860.9,1746.7,1732.9,1968.2,2171.1,1976.2,2226,1598.8,1940.4,2145.6,1879.5,1789.8,2138.6,1905.9,1853,1654,1432.2,1672.8,1522.8,1453.8,1791.2,1558.4,1925.4,1885.9,1619.4,1953,1384.9,1683.5,1497,1342.6,1356,1439.4,1639.8,1270.7,1105,1857.2,1205.2,1678.4,1659.4,1524.7,1772.5,1546,1692.9,1084.8]

#Classe spectre qui permet de simuler un spectrometre
class Spectre: 

    def __init__(self, plastique,resolution,petit_bruit,grand_bruit):
        self.plastique = plastique #boolean permet de savoir si le spectre est plastique ou non
        self.borne_inf = -80 #Int
        self.borne_sup = 1968 #Int
        self.resolution = resolution #resolution de la courbe
        self.petit_bruit = petit_bruit # une valeur float comme par exemple 0.0005
        self.type_plastique = self.plastique_aleatoire() #string avec le nom du plastique (cf)
        self.grand_bruit = grand_bruit*5 #0 si pas de bruit, 1 si bruit
        self.reflectance = [] #Tableau qui contient la reflectance pour chaque longeur d'onde de plage_longeur_donde
        self.plage_longueur_d_onde = [] #tableai qui contient toute les longeurs d'ondes
        self.creer_spectre()

    # retourne l'attribut isPlastic de la classe
    def est_plastique(self):
        return self.plastique

    #retoure un type de plastique aléatoire
    def plastique_aleatoire(self):
        if self.plastique==True:
            return random.choice(liste_matrix_plastique)
        else:
            return "sable"

    #peut etre appeler pour recreer le spectre selon vos besoins
    def creer_spectre(self):
        liste_data = []

        if(self.plastique == True):
            if(self.type_plastique == "PET"):
                liste_data = liste_data_pet
            elif(self.type_plastique == "Ink Cartridge"):
                liste_data = liste_data_inkCartridge
            elif(self.type_plastique == "PLA"):
                liste_data = liste_data_pla
            elif(self.type_plastique == "PELD"):
                liste_data = liste_data_peld
            elif(self.type_plastique == "PVC"):
                liste_data = liste_data_pvc
            elif(self.type_plastique == "PP"):
                liste_data = liste_data_pp

            else:
                print("Erreur type plastique")
                print(self.type_plastique)
                return
        else:
            liste_data = liste_data_sable



        list_wavelength = []   

        list_wavelength.append([-80.0,-76.0])
        for i in range (1,512):
            list_wavelength.append([list_wavelength[i-1][1],list_wavelength[i-1][1]+4.0])
        
        data1 = np.zeros(512)
        data2 = np.zeros(512)

        for i in range (512):
            data1[i] = liste_data[i]

        for i in range (511):
            data2[i] = liste_data[i+1]

        data2[511] = data1[511]

        data1 = np.reshape(data1,(512,1))
        data2 = np.reshape(data2,(512,1))
        matrix_data = np.append(data1,data2,axis=1)

        longeur_donde_spectre_type = list_wavelength
        reflectance_donde_spectre_type = matrix_data

        self.plage_longueur_d_onde = np.linspace(self.borne_inf,self.borne_sup, int((1/self.resolution)*(self.borne_sup-self.borne_inf)))
        self.reflectance = []

        for nb in range(len(longeur_donde_spectre_type)):
            nb_valeur = int((1/self.resolution)*(longeur_donde_spectre_type[nb][1]-longeur_donde_spectre_type[nb][0]))
            pas = (reflectance_donde_spectre_type[nb][1] - reflectance_donde_spectre_type[nb][0])/nb_valeur
            for i in range(nb_valeur):
                self.reflectance.append((reflectance_donde_spectre_type[nb][0]+pas*i)+random.uniform(-self.petit_bruit,self.petit_bruit))#Pour le petit bruit

        self.reflectance =  np.sin(self.plage_longueur_d_onde*random.uniform(0.3,0.5))*random.uniform(0.5,1.2)*self.grand_bruit + np.sin(self.plage_longueur_d_onde*random.uniform(0.3,0.5))*random.uniform(1.5,2.2)*self.grand_bruit + np.sin(self.plage_longueur_d_onde*random.uniform(0.08,0.12))*random.uniform(0.5,1.2)*self.grand_bruit + np.sin(self.plage_longueur_d_onde*random.uniform(0.05,0.08))*random.uniform(0.5,1.2)*self.grand_bruit + self.reflectance #+ self.reflectance   ##Pour le bruit

    def afficher(self):# affiche le spectre dans une fenetre numpy
        
        plt.plot(self.plage_longueur_d_onde, self.reflectance)
        plt.show()
    
    def get_reflectance(self):#permet de recupere le tableau avec toute la valeur des reflectances selon la resolution donnee
        return self.reflectance
    
    def get_longeur_donde(self):
        return self.plage_longueur_d_onde
    
    def get_resolution(self):
        return self.resolution