# C:\lib\Python\Python36 python.exe
# -*- coding:utf-8 -*-
"""
@file       731_My_Calendar_II.py
@project    LeetCode
--------------------------------------
@author     hjw
@date       2018-08-21 10:50
@version    0.0.1.20180821
--------------------------------------
Implement a MyCalendarTwo class to store your events. A new event can be added
    if adding the event will not cause a triple booking.

Your class will have one method, book(int start, int end). Formally,
    this represents a booking on the half open interval [start, end),
    the range of real numbers x such that start <= x < end.

A triple booking happens when three events have some non-empty intersection
    (ie., there is some time that is common to all 3 events.)

For each call to the method MyCalendar.book,
    return true if the event can be added to the calendar successfully without causing a triple booking.
    Otherwise, return false and do not add the event to the calendar.

Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)
"""

import sys


class MyCalendarTwo:
    
    def __init__(self):
        self.booked = []
        self.overlaps = []
        self.calendar = []
    
    
    ## out of time limit
    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        
        intersections = []
        
        for interval in self.booked:
            booked_interval = self.intersection(interval, [start, end])
            
            if not booked_interval:
                pass
            else:
                for inter_interval in intersections:
                    if self.intersection(booked_interval, inter_interval):
                        return False
                
                ## if there is no intersection between every two intervals, add it into list
                intersections.append(booked_interval)
        
        self.booked.append([start, end])
        return True
    
    
    def intersection(self, interval1, interval2):
        start1, end1 = interval1[0], interval1[1]
        start2, end2 = interval2[0], interval2[1]
        
        start_new = max(start1, start2)
        end_new = min(end1, end2)
        
        if start_new >= end_new:
            return []
        else:
            return [start_new, end_new]
    
    
    ## passed
    def book2(self, start, end):
        for i, j in self.overlaps:
            if start < j and end > i:
                return False
        for i, j in self.calendar:
            if start < j and end > i:
                self.overlaps.append((max(start, i), min(end, j)))
        self.calendar.append((start, end))
        return True


if __name__ == "__main__":
    obj = MyCalendarTwo()
    l1 = [[38115, 42136], [958404, 966280], [843000, 850441], [419867, 425511], [737800, 744230], [513787, 519408],
          [408938, 413517], [143881, 149835], [140857, 148801], [37665, 44486], [263519, 269131], [904640, 910087],
          [574705, 579510], [722387, 729157], [834002, 838105], [394555, 398606], [399830, 407030], [837124, 843094],
          [794874, 801773], [383305, 387366], [490598, 498193], [132690, 137344], [941531, 947919], [606101, 613674],
          [262693, 269135], [516481, 524337], [996011, 1000000], [152493, 157071], [295535, 303408], [33541, 39014],
          [395328, 400086], [410084, 414159], [797985, 803038], [516619, 523116], [253508, 261221], [645119, 650049],
          [477374, 483834], [500074, 505454], [30837, 37723], [814231, 820873], [172845, 179510], [205981, 213882],
          [787030, 792875], [61920, 69883], [150496, 157505], [384357, 391167], [721369, 725590], [534369, 539516],
          [280045, 284263], [210280, 217278], [537114, 543785], [466714, 472275], [718128, 722688], [987800, 994261],
          [403558, 407893], [296350, 303196], [831814, 836824], [237903, 243507], [935549, 942779], [445224, 450667],
          [915618, 920265], [740325, 746863], [463324, 468759], [27223, 32773], [235532, 239678], [484348, 488574],
          [167439, 174149], [852607, 860111], [793227, 798884], [351458, 357905], [815256, 821302], [343417, 350313],
          [933092, 938145], [433338, 440515], [631264, 637911], [80855, 88571], [853413, 858820], [79018, 86947],
          [172155, 179154], [430418, 436564], [895501, 902174], [865775, 871764], [137738, 145700], [260248, 267031],
          [243117, 248720], [589323, 593522], [925712, 931467], [737971, 742599], [300575, 306348], [708311, 712679],
          [825011, 832594], [891275, 898658], [430816, 435017], [383892, 390670], [521952, 526686], [111249, 118725],
          [970493, 976603], [840423, 844439], [222873, 229740], [378625, 382648], [69349, 74754], [405874, 413208],
          [319662, 326856], [157125, 161893], [903154, 909030], [223760, 229050], [432737, 438015], [857337, 865266],
          [302015, 309497], [474626, 479474], [902751, 907120], [472790, 478058], [838371, 842477], [568291, 572851],
          [861025, 868835], [57284, 63032], [429522, 436795], [44967, 52944], [547448, 554477], [475430, 481877],
          [605571, 612392], [544438, 550192], [990528, 996760], [55017, 59976], [837404, 844423], [991045, 998944],
          [311358, 318315], [950638, 957808], [867222, 874924], [844444, 851107], [287054, 294864], [799374, 805776],
          [863904, 871740], [105491, 110401], [716934, 723594], [155104, 161948], [379876, 386373], [765526, 772872],
          [191934, 196719], [102866, 109505], [790004, 794066], [751334, 757170], [583846, 591317], [503328, 509042],
          [166649, 172292], [8698, 15047], [256513, 263640], [648162, 653780], [233769, 239518], [523589, 528481],
          [731350, 735533], [672532, 678708], [576431, 582209], [755656, 759692], [974807, 979402], [995348, 999631],
          [492392, 498752], [948816, 956133], [26559, 32230], [19690, 23991], [531641, 537510], [597060, 602481],
          [79990, 86760], [341363, 346096], [469098, 474407], [220829, 226740], [972936, 980408], [313607, 320729],
          [598707, 604952], [618054, 622342], [521745, 526224], [28198, 34529], [203082, 208967], [756102, 760212],
          [992091, 998506], [227305, 232445], [236077, 243952], [393811, 400856], [578122, 582782], [201286, 209275],
          [136968, 142955], [420557, 426345], [994351, 998734], [634621, 640368], [519742, 525643], [670284, 677772],
          [473967, 478201], [632205, 639653], [147083, 154613], [75938, 80263], [272508, 277639], [752402, 756449],
          [490729, 498411], [926727, 932072], [692723, 698141], [587755, 594466], [664900, 669584], [54930, 59371],
          [961550, 967124], [501867, 507518], [603909, 610459], [574220, 579676], [428017, 435627], [587095, 592646],
          [657624, 661802], [320479, 325807], [939720, 946056], [253754, 260276], [1417, 6497], [594629, 600018],
          [528820, 534861], [850134, 857002], [486250, 491745], [558442, 562771], [577895, 585468], [52568, 58177],
          [843178, 850984], [904127, 908396], [676130, 682096], [579515, 586608], [79212, 84546], [202370, 209885],
          [29555, 37017], [695502, 700963], [296003, 302598], [397491, 405206], [212513, 216826], [741217, 745507],
          [175541, 179575], [916115, 922846], [342050, 346158], [107334, 111472], [340795, 348431], [440923, 447843],
          [717089, 721720], [520327, 525613], [973680, 980795], [990497, 994978], [239228, 243847], [547345, 551728],
          [456776, 464333], [793256, 798825], [750591, 756326], [340761, 347427], [78836, 83939], [273218, 280452],
          [606596, 614042], [342896, 348516], [617167, 624306], [46446, 52414], [688095, 693591], [723617, 729075],
          [815208, 822917], [540404, 547924], [676730, 683063], [256974, 263019], [651977, 658505], [905598, 913525],
          [863131, 869581], [862935, 868033], [726199, 732065], [251311, 257734], [68586, 75847], [928509, 936029],
          [836470, 844456], [890655, 897064], [153848, 158415], [678339, 685417], [762921, 767971], [666454, 671985],
          [934292, 940927], [257821, 264608], [689120, 695405], [79124, 84263], [421436, 425759], [577079, 582213],
          [358015, 364507], [554989, 559394], [541515, 545682], [761539, 766319], [936149, 943260], [58936, 63250],
          [218479, 225436], [934204, 939420], [528948, 535226], [244508, 250415], [841498, 847774], [504454, 511520],
          [303976, 311325], [173124, 177521], [293575, 299515], [717691, 723645], [43574, 50720], [221503, 226601],
          [642137, 648038], [168556, 174293], [144435, 149936], [925261, 929567], [828307, 832441], [641483, 647381],
          [999547, 1000000], [208965, 215952], [538588, 543481], [649849, 656248], [169449, 175404], [941118, 946005],
          [640166, 645490], [904044, 909104], [797075, 802508], [180994, 185267], [801605, 808464], [841946, 847449],
          [890595, 897276], [519712, 526494], [607017, 614472], [998916, 1000000], [284238, 290479], [94883, 99146],
          [125053, 131866], [636199, 641443], [778577, 785438], [347627, 355015], [154895, 161186], [696677, 703319],
          [677563, 685440], [968518, 975516], [989152, 995070], [599851, 606687], [857212, 862328], [967896, 973979],
          [447556, 452921], [337502, 342859], [220535, 224639], [388862, 393535], [667830, 673231], [331741, 337543],
          [802492, 808630], [464735, 470141], [147861, 152599], [86003, 92271], [433512, 438866], [165237, 171517],
          [919990, 925706], [21621, 28794], [613399, 620633], [285995, 292185], [377504, 385166], [378467, 384946],
          [109655, 114679], [503463, 508601], [525151, 529376], [594018, 601315], [121351, 128754], [403040, 407116],
          [834511, 839658], [333513, 337937], [468938, 476691], [378971, 383769], [382612, 386657], [268535, 274190],
          [634992, 640392], [956948, 964099], [959381, 965592], [290196, 296126], [877298, 882241], [816863, 823474],
          [651841, 658171], [56861, 64386], [931927, 938309], [774670, 781124], [680856, 686635], [23121, 27121],
          [757063, 764599], [343431, 348933], [466726, 471244], [78025, 84393], [178042, 182878], [741630, 749443],
          [726319, 732471], [524326, 530107], [223594, 229238], [592955, 600139], [19907, 25380], [431196, 438834],
          [648191, 654266], [254976, 262567], [987159, 994785], [157709, 162664], [986222, 992732], [486803, 494401],
          [124972, 129778], [680329, 686553], [782674, 787594], [586301, 593659], [136114, 142693], [77362, 83729],
          [134947, 140777], [585496, 591789], [53367, 57914], [76453, 83426], [145643, 152047], [315065, 320163],
          [832621, 839774], [92880, 99507], [98121, 104788], [863892, 870641], [81751, 87461], [609529, 616592],
          [213853, 218160], [64306, 69999], [842027, 846948], [121066, 125143], [981472, 987077], [468809, 472937],
          [258484, 265469], [415208, 419527], [471222, 476578], [946311, 951067], [22775, 28132], [956733, 964067],
          [294531, 300990], [663019, 669483], [416610, 421873], [317545, 322105], [520967, 527589], [75369, 82351],
          [692324, 699911], [929231, 936291], [394351, 399254], [790325, 794915], [197815, 202143], [485717, 490875],
          [139140, 144368], [96916, 103169], [591735, 597675], [589667, 596267], [82308, 88426], [273729, 277790],
          [954096, 958209], [133212, 140625], [161307, 169290], [906623, 911398], [11458, 18848], [820122, 824469],
          [306801, 313018], [473635, 481347], [496147, 501267], [372705, 378721], [450219, 456820], [450336, 456663],
          [988168, 994057], [499829, 504387], [867184, 874452], [593096, 598581], [936789, 943146], [278299, 284127],
          [599529, 607120], [676878, 684116], [268190, 273301], [212616, 218295], [573658, 578377], [903814, 909762],
          [150544, 156786], [21211, 28731], [527042, 531913], [36733, 41343], [741406, 746152], [671778, 679553],
          [457231, 463647], [123146, 127818], [827930, 835703], [103941, 109023], [249853, 255622], [402338, 409317],
          [197154, 204825], [713436, 718087], [907991, 914496], [520874, 528765], [71385, 77655], [472576, 477739],
          [630845, 636678], [81582, 89321], [321706, 327867], [103915, 108578], [149356, 154131], [191819, 197308],
          [114617, 121482], [119817, 124718], [199898, 207305], [891544, 896972], [773598, 779895], [175479, 181283],
          [939469, 943505], [183393, 188838], [370643, 375735], [422240, 430197], [752292, 758603], [313994, 320876],
          [130972, 135573], [189158, 193194], [67608, 72757], [731993, 737529], [426409, 432994], [538739, 543753],
          [779086, 785739], [132691, 137436], [98437, 104350], [841153, 847369], [404959, 410299], [436240, 442459],
          [20941, 26763], [759531, 763940], [159366, 164158], [440432, 446274], [382977, 389096], [375606, 380061],
          [670507, 677064], [212270, 216817], [267592, 272920], [135149, 140837], [754933, 761369], [865879, 870773],
          [346797, 354093], [676855, 681532], [788404, 795835], [344952, 349005], [616284, 623138], [71972, 76396],
          [323471, 328416], [747180, 752677], [937076, 941893], [822928, 828369], [511639, 515888], [158996, 164272],
          [32696, 39216], [45122, 50854], [500235, 506025], [912252, 918389], [695500, 702625], [44339, 50424],
          [307660, 313700], [397053, 401892], [409563, 414632], [20814, 27346], [949810, 954393], [333494, 339207],
          [488004, 492298], [674076, 679235], [871965, 878749], [237513, 243774], [302173, 307760], [498490, 505244],
          [120696, 124958], [686342, 690577], [546344, 552888], [46168, 54054], [19743, 25451], [136036, 140830],
          [799657, 804956], [456006, 460728], [142931, 150892], [292988, 298730], [481611, 486793], [981253, 986783],
          [519751, 524885], [657987, 665072], [835828, 842561], [314700, 320744], [114142, 120638], [38439, 44014],
          [904564, 910979], [495966, 500713], [289979, 297700], [455311, 460768], [292445, 298634], [386784, 391440],
          [63118, 67162], [648047, 655105], [487691, 491710], [899118, 906236], [639892, 647111], [440045, 446175],
          [839565, 844857], [583735, 589596], [677663, 682329], [147435, 151685], [996021, 1000000], [579924, 586268],
          [780200, 787417], [368165, 375897], [906513, 911126], [119892, 124724], [98849, 106681], [483542, 489454],
          [292592, 298327], [677810, 684373], [918376, 922414], [564722, 569340], [60618, 67628], [268976, 276008],
          [534947, 539554], [876051, 882077], [949460, 953493], [620647, 625837], [36979, 43228], [496864, 504475],
          [895085, 900535], [127582, 132237], [13751, 21563], [639692, 646169], [69777, 77242], [332100, 339045],
          [600288, 607899], [916765, 923245], [126091, 131265], [500350, 506635], [145553, 151084], [72722, 79029],
          [97976, 103043], [771195, 776583], [637592, 644760], [621356, 626510], [482548, 487109], [769833, 774367],
          [60224, 64590], [517132, 521878], [586715, 591294], [75993, 83642], [571950, 576824], [211612, 217637],
          [953920, 961768], [301486, 308633], [286509, 291738], [300325, 308251], [674942, 679670], [458238, 462524],
          [283584, 289602], [379705, 386252], [435290, 439895], [215371, 222077], [606754, 613048], [311871, 316401],
          [855243, 862377], [328124, 335482], [344696, 349167], [935773, 939918], [687581, 693133], [523149, 529257],
          [757010, 763890], [168061, 172984], [279731, 286953], [238731, 246017], [332560, 338006], [214895, 220954],
          [323668, 327972], [141319, 148330], [271089, 276695], [8147, 15322], [646137, 653912], [860701, 866836],
          [106586, 110701], [969608, 976913], [856830, 861688], [671801, 677559], [128142, 134998], [288526, 296201],
          [711477, 719468], [550026, 557769], [870618, 877137], [393621, 399973], [832752, 836955], [378197, 382264],
          [107384, 112171], [464180, 471968], [909598, 917272], [445979, 451903], [650623, 654813], [601074, 609003],
          [107928, 113973], [374470, 378550], [392254, 399510], [98584, 102599], [497141, 501595], [371540, 378303],
          [83436, 90443], [366778, 373547], [319830, 327615], [939883, 944088], [831494, 836390], [376930, 384116],
          [722349, 729598], [62355, 68141], [967929, 974639], [217094, 225055], [48865, 56538], [919053, 925616],
          [762033, 766351], [288422, 292940], [784915, 792309], [802408, 806518], [614720, 621540], [119212, 126639],
          [273305, 278967], [600124, 607015], [994944, 1000000], [377287, 385120], [315100, 320742], [794565, 798892],
          [792214, 798821], [108872, 115319], [67488, 72413], [914568, 920374], [23661, 28672], [187112, 194722],
          [424493, 430624], [507900, 512561], [169418, 177364], [941356, 947530], [525187, 530020], [851607, 859067],
          [94120, 99985], [194601, 201319], [637636, 641929], [327180, 331551], [402729, 409482], [785320, 790089],
          [943251, 950050], [429474, 434211], [339730, 346638], [870762, 876017], [456474, 461407], [435296, 439975],
          [376782, 383277], [899056, 904481], [420701, 426329], [861652, 868002], [77813, 85791], [719864, 725663],
          [811226, 819045], [898933, 904653], [786639, 792463], [582677, 589614], [204771, 209424], [467263, 472327],
          [588918, 593191], [307190, 315086], [967545, 972583], [691687, 697967], [304446, 311088], [733163, 740260],
          [230031, 235495], [936076, 942646], [960646, 968397], [926257, 931694], [96838, 103039], [578976, 586137],
          [666898, 672096], [171606, 176811], [658789, 665697], [255614, 262571], [241087, 246573], [888121, 893096],
          [638806, 642887], [459762, 467077], [788907, 793933], [960335, 964743], [690372, 696608], [837259, 841870],
          [802171, 808296], [693507, 699190], [812628, 817330], [586993, 593965], [113738, 120737], [666547, 671279],
          [179222, 183571], [7674, 15082], [488643, 495364], [77121, 82814], [12846, 18164], [939927, 946233],
          [432501, 439866], [189951, 197008], [134511, 138853], [344982, 351341], [179738, 185051], [250386, 255178],
          [212156, 218886], [800307, 807911], [980432, 987591], [472316, 479379], [9435, 15959], [795857, 802590],
          [240224, 246972], [516683, 522221], [4464, 8472], [156698, 163528], [861629, 869233], [537963, 545707],
          [229949, 237896], [952228, 959528], [8230, 12668], [135157, 139530], [405970, 412939], [272306, 277569],
          [982762, 989845], [619703, 623803], [433360, 440348], [49466, 53467], [727864, 732585], [526293, 533264],
          [574627, 579550], [483993, 490989], [518470, 524752], [215345, 221087], [649690, 657297], [996842, 1000000],
          [203077, 208934], [425514, 430200], [40556, 47150], [443908, 451592], [798272, 806221], [19853, 25036],
          [76893, 81886], [812787, 819358], [298991, 305901], [507296, 513933], [556079, 560635], [575833, 581968],
          [69453, 75852], [575355, 583034], [893742, 900710], [3167, 10352], [608380, 615597], [629602, 634625],
          [566022, 573080], [837746, 844512], [105504, 111948], [560350, 564810], [382509, 389767], [199579, 207034],
          [805013, 811361], [926567, 931331], [791438, 797653], [210614, 214985], [853576, 858174], [849001, 854890],
          [949740, 954162], [830312, 838218], [856176, 862194], [57975, 61988], [254453, 261455], [987285, 994058],
          [579714, 584417], [541897, 548449], [509648, 517070], [771425, 776093], [458552, 464437], [325333, 330066],
          [701470, 707624], [851612, 858756], [211231, 218959], [183594, 189250], [299961, 306020], [292973, 300006],
          [309072, 313750], [662755, 668454], [699240, 703454], [261660, 268067], [70344, 75068], [359129, 363190],
          [395997, 400223], [584293, 591409], [706853, 712589], [86323, 90886], [750881, 755609], [134735, 141667],
          [14075, 18562], [872139, 876929], [417934, 424874], [195813, 202753], [986153, 991545], [574353, 581074],
          [979454, 983454], [147883, 155003], [530289, 534831], [548257, 552569], [436291, 442013], [808460, 815532],
          [177752, 184445], [533510, 538595], [282802, 288281], [304351, 312174], [417714, 424647], [726909, 734337],
          [7248, 14401], [72155, 79428], [799971, 804508], [901284, 906019], [176386, 182460], [405915, 412703],
          [965930, 972166], [890970, 895597], [807082, 812201], [745256, 750350], [901167, 905429], [592416, 597860],
          [309518, 314769], [114983, 121086], [319517, 325708], [776382, 780642], [257251, 262266], [378659, 386031],
          [210869, 217497], [204462, 211852], [805442, 813095], [665802, 670482], [71306, 77463], [967872, 973302],
          [10896, 15493], [461441, 465975], [485505, 493170], [859497, 864185], [403989, 410898], [709772, 716229],
          [214551, 220120], [831227, 836411], [139395, 145920], [135645, 143016], [691406, 697488], [939634, 943761],
          [185467, 189949], [873628, 881177], [962805, 969963], [71838, 78329], [108862, 114102], [291043, 298342],
          [291356, 295480], [326517, 331536], [786045, 791198], [978940, 984264], [684335, 688699], [633727, 638781],
          [603865, 610608], [677752, 682299], [995395, 1000000], [823358, 827833], [607545, 614330], [388747, 393574],
          [860940, 868353], [304273, 309321], [162891, 169217], [653326, 658862], [249408, 254892], [991796, 999357],
          [214338, 220071], [555239, 561669], [974093, 980854], [389621, 396586], [530054, 537569], [72768, 78683],
          [384161, 389055], [341340, 345376], [858999, 864479], [458446, 464334], [637532, 643987], [930091, 934729],
          [139529, 143792], [65410, 70857], [808177, 816169], [641875, 648607], [936862, 944131], [75904, 82999],
          [474511, 480787], [815604, 823336], [68161, 74838], [917925, 922987], [61415, 67150], [601574, 605869],
          [605183, 610885], [634700, 641626], [22736, 29236], [455290, 459300], [608096, 615964], [21257, 27840],
          [473013, 480371], [502368, 508460], [909537, 916124], [716230, 721817], [532521, 538052], [420869, 427294],
          [832066, 837753], [446020, 450237], [482574, 487313], [478429, 485139], [16036, 22859], [11615, 17393],
          [532812, 539319], [790108, 797267], [582467, 586544], [938518, 945997]]
    
    for ll in l1:
        aa = obj.book(ll[0], ll[1])
        print(aa)
    
    print(obj.booked)


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)