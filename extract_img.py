import re
import os
from PIL import Image

# 创建输出目录
output_dir = os.path.join(os.path.dirname(__file__), 'output_images')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 打开源图片
src_img = Image.open('INGAMEPNG.png')
s = """
INGAME_$PNG.ROBOTO_REGULAR_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1781,650,164,164),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.UBUNTU_REG_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(923,1,418,418),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.APPSTORE_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(384,1200,185,56),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.ARM_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1256,1264,33,49),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.ARROW_DOWN_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1692,1314,65,38),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.ARROWS_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1077,1050,167,82),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.AVATAR_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1855,1,117,245),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.AVATAR2_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1936,478,76,170),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BACK_FOOT_WHITE_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(283,1386,51,27),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BACK_SHOE_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(704,1386,51,27),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BACK_SHOELACES_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(652,1386,51,27),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BACK_SOCK_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(728,1274,33,45),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BACK_UPPERLEG_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(496,1312,21,42),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BALL_WHITE_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1316,965,82,81),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BBROS_BIG_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(487,1,435,434),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BLANK_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1053,1352,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BOSTON_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(199,1323,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BRO01_HEAD_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(113,818,108,141),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BRO02_HEAD_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1896,815,120,144),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BRO03_HEAD_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1174,817,114,141),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BRO04_HEAD_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(848,952,108,138),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BRO05_HEAD_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(164,655,117,162),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BRO06_HEAD_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1,818,111,141),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BRO07_HEAD_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1413,814,117,147),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BRO08_HEAD_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1781,815,114,147),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BRO09_HEAD_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1408,657,105,156),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BRO10_HEAD_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(282,817,120,141),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BRO11_HEAD_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1174,657,120,159),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BRO12_HEAD_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(744,629,192,168),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BRO13_HEAD_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(282,655,135,161),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BRO14_HEAD_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1643,816,112,143),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BRO15_HEAD_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(593,806,113,152),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BRO16_HEAD_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1531,816,111,144),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BRO17_HEAD_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1051,657,122,160),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BRO18_HEAD_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(969,818,109,139),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BRO19_HEAD_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1514,657,103,152),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BRO20_HEAD_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(723,798,124,155),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BRO21_HEAD_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1295,814,117,150),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BRO22_HEAD_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(418,808,145,152),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BRO23_HEAD_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(744,436,136,174),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BRO24_HEAD_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1624,650,156,165),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BRO25_HEAD_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(337,484,113,168),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BRO26_HEAD_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(937,629,113,168),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BRO27_HEAD_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1295,657,112,156),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BRO28_HEAD_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(848,798,120,153),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BRO29_HEAD_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(923,420,187,208),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BRO30_HEAD_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1803,478,132,171),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BRO31_HEAD_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1670,478,132,171),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BRO32_HEAD_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(593,641,129,164),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BRO33_HEAD_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(451,641,141,166),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BU_2PLAYER_HOVER_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(570,1219,342,54),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BU_2PLAYER_UP_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1633,1204,342,54),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BU_ARROW_UP_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1992,1041,42,75),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BU_AUDIO_DOWN2_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(931,1148,62,62),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BU_AUDIO_HOVER_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1,1063,81,81),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BU_AUDIO_UP_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1910,1051,81,81),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BU_AUDIO_UP2_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(321,1145,62,62),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BU_CUSTOMIZATION_COURT_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1758,1314,52,38),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BU_CUSTOMIZATION_JERSEY_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1245,1050,42,71),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BU_CUSTOMIZATION_PANTS_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1290,1264,41,47),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BU_CUSTOMIZATION_SELECTED_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1896,960,75,90),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BU_CUSTOMIZATION_SHOES_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1465,1314,62,40),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BU_CUSTOMIZATION_SOCKS_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(812,1161,38,56),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BU_CUSTOMIZATION_STATS_SELECTED_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1155,959,75,90),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BU_CUSTOMIZATION_STATS_UNSELECTED_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1079,909,75,90),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BU_CUSTOMIZATION_UNSELECTED_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1079,818,75,90),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BU_DISCORD_HOVER_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(83,1063,81,81),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BU_DISCORD_SPEECH_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1398,1064,295,70),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BU_DISCORD_UP_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(165,1063,81,81),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BU_FULLSCREENOFF_DOWN2_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1572,1135,62,62),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BU_FULLSCREENOFF_UP2_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1509,1135,62,62),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BU_FULLSCREEN_DOWN2_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(481,1137,62,62),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BU_FULLSCREEN_HOVER_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1316,1047,81,81),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BU_FULLSCREEN_UP_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(247,1063,81,81),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BU_FULLSCREEN_UP2_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(418,1137,62,62),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BU_PLAY_HOVER_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1,960,342,102),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BU_PLAY_UP_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(344,961,342,102),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BU_PRIVATE_HOVER_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(519,1274,174,54),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BU_PRIVATE_UP_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(344,1257,174,54),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BU_RESET_HOVER_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1,1213,342,54),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BU_RESET_UP_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1337,1259,342,54),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BU_SETTINGS_DOWN_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(544,1137,62,62),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BU_SETTINGS_HOVER_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1828,1051,81,81),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BU_SETTINGS_UP_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(258,1145,62,62),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BU_SINGLEPLAYER_HOVER_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1680,1259,342,54),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BU_SINGLEPLAYER_UP_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(913,1264,342,54),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.BUBBLE_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1342,258,327,223),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.CATWALK_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1,1145,256,67),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.CHAT_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1111,482,512,174),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.CHAT2_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1342,1,512,256),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.CHICAGO_MENU_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(784,1386,32,26),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.COIN_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1019,1386,15,7),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.DALAS_MENU_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1086,1352,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.DARK_BACK_ARM_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(440,1312,27,42),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.DARK_BACK_HAND_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1465,1355,36,30),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.DARK_BACK_LOWERLEG_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(762,1274,33,45),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.DARK_BACK_SHOULDER_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1290,1312,27,42),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.DARK_BACK_UPPERLEG_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1399,1314,21,42),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.DARK_FRONT_ARM_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1644,1314,15,39),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.DARK_FRONT_HAND_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(280,1317,30,33),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.DARK_FRONT_HAND2_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(898,1319,30,33),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.DARK_FRONT_LOWERLEG_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(694,1274,33,45),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.DARK_FRONT_SHOULDER_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1927,1314,36,36),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.DARK_FRONT_UPPERLEG_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(2023,1187,24,42),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.DARK_STOMACH_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1157,1133,39,69),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.FLASH_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1,655,162,162),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.FRONT_FOOT_WHITE_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(335,1386,51,27),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.FRONT_SHOE_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1824,1385,51,27),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.FRONT_SHOELACES_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1410,1385,51,27),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.FRONT_SOCK_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(864,1274,33,45),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.FRONT_UPPERLEG_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(2023,1230,24,42),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.GLIMMER_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1660,1354,31,31),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.GOOGLEPLAY_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1445,1199,187,57),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.HIPS_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1876,1385,39,27),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.HOT_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(707,954,128,128),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.INPUTFIELD_NAME_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(994,1203,342,60),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.ITALIC_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1,1,485,482),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO01_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1405,1135,39,69),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO02_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1365,1135,39,69),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO03_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1774,1134,39,69),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO04_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1734,1134,39,69),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO05_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1694,1134,39,69),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO06_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(651,1134,39,69),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO07_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(611,1134,39,69),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO08_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1934,1133,39,69),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO09_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1894,1133,39,69),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO10_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1854,1133,39,69),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO11_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1814,1133,39,69),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO12_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1197,1133,39,69),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO13_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1117,1133,39,69),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO14_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1077,1133,39,69),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO15_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1325,1129,39,69),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO16_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1245,1122,39,69),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO17_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1992,1117,39,69),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO18_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(891,1091,39,69),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO19_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(851,1091,39,69),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO20_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(811,1091,39,69),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO21_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(771,1083,39,69),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO22_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(731,1083,39,69),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO23_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(691,1083,39,69),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO24_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1037,1078,39,69),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO25_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(611,1064,39,69),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO26_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(997,1078,39,69),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO27_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(957,1078,39,69),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO28_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1774,1064,39,69),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO29_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1734,1064,39,69),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO_MENU01_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(166,1323,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO_MENU02_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(100,1323,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO_MENU03_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(34,1323,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO_MENU04_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1,1323,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO_MENU05_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(826,1320,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO_MENU06_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(694,1320,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO_MENU07_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1218,1319,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO_MENU08_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1185,1319,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO_MENU09_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1119,1319,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO_MENU10_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1086,1319,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO_MENU11_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(760,1320,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO_MENU12_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1053,1319,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO_MENU13_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(914,1353,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO_MENU14_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(232,1323,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO_MENU15_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(265,1351,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO_MENU16_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1927,1351,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO_MENU17_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(782,1353,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO_MENU18_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(749,1353,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO_MENU19_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(716,1353,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO_MENU20_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1884,1352,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO_MENU21_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1185,1352,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO_MENU22_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(298,1351,28,28),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO_MENU23_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1119,1352,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO_MENU24_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(650,1329,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO_MENU25_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(584,1329,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO_MENU26_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(551,1329,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO_MENU27_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(518,1329,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO_MENU28_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(859,1320,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_LOGO_MENU29_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(793,1320,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.JERSEY_WHITE_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(651,1064,39,69),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.LA_MENU_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(727,1320,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.LEFT_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1568,1314,37,39),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.LEG_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1635,1135,20,60),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.LIGHT_BACK_ARM_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1346,1314,27,42),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.LIGHT_BACK_HAND_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(38,1356,36,30),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.LIGHT_BACK_LOWERLEG_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(363,1312,33,45),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.LIGHT_BACK_SHOULDER_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1318,1314,27,42),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.LIGHT_BACK_UPPERLEG_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1443,1314,21,42),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.LIGHT_FRONT_ARM_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1676,1314,15,39),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.LIGHT_FRONT_HAND_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1022,1319,30,33),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.LIGHT_FRONT_HAND2_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(991,1319,30,33),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.LIGHT_FRONT_LOWERLEG_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(329,1312,33,45),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.LIGHT_FRONT_SHOULDER_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(2001,1316,36,36),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.LIGHT_FRONT_UPPERLEG_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(2023,1273,24,42),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.LIGHT_STOMACH_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1694,1064,39,69),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.LOSE_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(817,1386,175,25),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.MEDIUM_BACK_ARM_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1256,1314,27,42),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.MEDIUM_BACK_HAND_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1,1356,36,30),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.MEDIUM_BACK_LOWERLEG_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(830,1274,33,45),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.MEDIUM_BACK_SHOULDER_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(468,1312,27,42),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.MEDIUM_BACK_UPPERLEG_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1421,1314,21,42),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.MEDIUM_FRONT_ARM_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1660,1314,15,39),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.MEDIUM_FRONT_HAND_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(960,1319,30,33),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.MEDIUM_FRONT_HAND2_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(929,1319,30,33),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.MEDIUM_FRONT_LOWERLEG_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(796,1274,33,45),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.MEDIUM_FRONT_SHOULDER_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1964,1314,36,36),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.MEDIUM_FRONT_UPPERLEG_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1374,1314,24,42),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.MEDIUM_STOMACH_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1285,1129,39,69),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.NET_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(387,1388,92,10),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.NET1_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(329,1064,88,80),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.PIXELBALL_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(397,1312,42,42),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.PLACKARD_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1,1268,278,54),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.PUNCH_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1889,1314,37,37),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.RAY_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1413,963,414,100),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.RECT_CORNER_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(993,1386,25,25),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.RECT_SIDES_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(2038,1316,8,8),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.RIGHT_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1606,1314,37,39),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SANFRAN_MENU_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(683,1353,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SCOREBOARD_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1,484,335,170),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SELECTION_COLOR_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1811,1314,39,38),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SELECTION_LOGO_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(280,1268,48,48),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SHADING_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(815,1353,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SHADOW_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1969,1386,75,7),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SHOE_LOGO01_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1306,1385,51,27),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SHOE_LOGO02_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1358,1385,51,27),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SHOE_LOGO03_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1254,1385,51,27),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SHOE_LOGO04_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1202,1385,51,27),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SHOE_LOGO05_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1150,1385,51,27),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SHOE_LOGO06_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1098,1385,51,27),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SHOE_LOGO07_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1046,1385,51,27),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SHOE_LOGO08_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1917,1384,51,27),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SHOE_LOGO09_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(231,1384,51,27),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SHOE_LOGO10_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(179,1384,51,27),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SHOE_LOGO11_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(127,1384,51,27),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SHOE_LOGO12_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(75,1384,51,27),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SHOE_LOGO13_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(600,1362,51,27),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SHOE_LOGO14_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(548,1362,51,27),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SHOE_LOGO15_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(496,1362,51,27),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SHOE_LOGO16_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(327,1358,51,27),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SHOE_LOGO17_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1407,1357,51,27),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SHOE_LOGO18_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1355,1357,51,27),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SHOE_LOGO19_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1303,1357,51,27),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SHOE_LOGO20_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1251,1357,51,27),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SHOE_LOGO21_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(179,1356,51,27),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SHOE_LOGO22_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(127,1356,51,27),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SHOE_LOGO23_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(75,1356,51,27),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SHOE_LOGO_MENU01_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1152,1319,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SHOE_LOGO_MENU02_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(133,1323,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SHOE_LOGO_MENU03_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(617,1329,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SHOE_LOGO_MENU04_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1152,1352,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SHOE_LOGO_MENU05_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1218,1352,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SHOE_LOGO_MENU06_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(463,1355,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SHOE_LOGO_MENU07_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(430,1355,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SHOE_LOGO_MENU08_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(397,1355,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SHOE_LOGO_MENU09_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1627,1354,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SHOE_LOGO_MENU10_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1594,1354,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SHOE_LOGO_MENU11_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1561,1354,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SHOE_LOGO_MENU12_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1528,1354,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SHOE_LOGO_MENU13_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1993,1353,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SHOE_LOGO_MENU14_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1791,1353,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SHOE_LOGO_MENU15_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1758,1353,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SHOE_LOGO_MENU16_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1725,1353,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SHOE_LOGO_MENU17_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1692,1353,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SHOE_LOGO_MENU18_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1013,1353,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SHOE_LOGO_MENU19_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(980,1353,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SHOE_LOGO_MENU20_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(947,1353,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SHOE_LOGO_MENU21_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(881,1353,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SHOE_LOGO_MENU22_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(848,1353,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SHOE_LOGO_MENU23_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1851,1352,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SPARK_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(2045,1328,2,2),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SPARK__TILE_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(2045,1325,2,2),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SPARKLE01_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(691,1153,59,59),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SPARKLE02_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1231,965,84,84),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.SPARKLE03_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(957,958,119,119),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.STAR_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(751,1161,60,57),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.STATBAR_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1660,1386,105,15),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.STATSPANEL_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1670,258,342,219),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.TOOLTIP_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1960,1351,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.TORSO_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1992,960,40,80),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.TRAIL_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1445,1135,63,63),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.UI_BKND_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(487,436,256,204),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.UP_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1851,1314,37,37),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.WASD_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(418,1064,192,72),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.WHITE_PARTICLE_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(67,1323,32,32),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.WHITE_STAR_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(756,1386,27,27),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.WIN_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1462,1387,166,25),
    INGAME_$PNG.Get()
}
,
INGAME_$PNG.X_PNG = function() {
    return BundlerData.rect = new openfl_geom_Rectangle(1528,1314,39,39),
    INGAME_$PNG.Get()
}
;
"""
regex = r"INGAME_\$PNG\..*?_PNG \= function\(\) \{.*?\}"

for i in re.findall(regex, s, re.M | re.S):
    name_reg = r"[^.]*?_PNG"
    name = re.findall(name_reg, i)[0]
    pos_reg = r"\(([\d,]+)\)"
    pos_tuple = re.findall(pos_reg, i)[0].split(',')
    x, y, w, h = map(int, pos_tuple)
    
    # 裁剪图片
    cropped = src_img.crop((x, y, x + w, y + h))
    
    # 保存图片
    output_path = os.path.join(output_dir, f"{name}.png")
    cropped.save(output_path)
    print(f"Saved: {output_path}")