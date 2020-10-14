class Color:
    def __init__(self, id, name, rgba):
        self.id = id
        self.name = name
        self.rgba = rgba
        
# https://minecraft.gamepedia.com/Map_item_format#Map_colors
NONE = Color(0, "NONE", (0, 0, 0, 0))
GRASS = Color(1, "GRASS", (127, 178, 56, 255))
SAND = Color(2, "SAND", (247, 233, 163, 255))
WOOL = Color(3, "WOOL", (199, 199, 199, 255))
FIRE = Color(4, "FIRE", (255, 0, 0, 255))
ICE = Color(5, "ICE", (160, 160, 255, 255))
METAL = Color(6, "METAL", (167, 167, 167, 255))
PLANT = Color(7, "PLANT", (0, 124, 0, 255))
SNOW = Color(8, "SNOW", (255, 255, 255, 255))
CLAY = Color(9, "CLAY", (164, 168, 184, 255))
DIRT = Color(10, "DIRT", (151, 109, 77, 255))
STONE = Color(11, "STONE", (112, 112, 112, 255))
WATER = Color(12, "WATER", (64, 64, 255, 255))
WOOD = Color(13, "WOOD", (143, 119, 72, 255))
QUARTZ = Color(14, "QUARTZ", (255, 252, 245, 255))
ORANGE = Color(15, "ORANGE", (216, 127, 51, 255))
MAGENTA = Color(16, "MAGENTA", (178, 76, 216, 255))
LIGHT_BLUE = Color(17, "LIGHT_BLUE", (102, 153, 216, 255))
YELLOW = Color(18, "YELLOW", (229, 229, 51, 255))
LIGHT_GREEN = Color(19, "LIGHT_GREEN", (127, 204, 25, 255))
PINK = Color(20, "PINK", (242, 127, 165, 255))
GRAY = Color(21, "GRAY", (76, 76, 76, 255))
LIGHT_GRAY = Color(22, "LIGHT_GRAY", (153, 153, 153, 255))
CYAN = Color(23, "CYAN", (76, 127, 153, 255))
PURPLE = Color(24, "PURPLE", (127, 63, 178, 255))
BLUE = Color(25, "BLUE", (51, 76, 178, 255))
BROWN = Color(26, "BROWN", (102, 76, 51, 255))
GREEN = Color(27, "GREEN", (102, 127, 51, 255))
RED = Color(28, "RED", (153, 51, 51, 255))
BLACK = Color(29, "BLACK", (25, 25, 25, 255))
GOLD = Color(30, "GOLD", (250, 238, 77, 255))
DIAMOND = Color(31, "DIAMOND", (92, 219, 213, 255))
LAPIS = Color(32, "LAPIS", (74, 128, 255, 255))
EMERALD = Color(33, "EMERALD", (0, 217, 58, 255))
PODZOL = Color(34, "PODZOL", (129, 86, 49, 255))
NETHER = Color(35, "NETHER", (112, 2, 0, 255))
TERRACOTTA_WHITE = Color(36, "TERRACOTTA_WHITE", (209, 177, 161, 255))
TERRACOTTA_ORANGE = Color(37, "TERRACOTTA_ORANGE", (159, 82, 36, 255))
TERRACOTTA_MAGENTA = Color(38, "TERRACOTTA_MAGENTA", (149, 87, 108, 255))
TERRACOTTA_LIGHT_BLUE = Color(39, "TERRACOTTA_LIGHT_BLUE", (112, 108, 138, 255))
TERRACOTTA_YELLOW = Color(40, "TERRACOTTA_YELLOW", (186, 133, 36, 255))
TERRACOTTA_LIGHT_GREEN = Color(41, "TERRACOTTA_LIGHT_GREEN", (103, 117, 53, 255))
TERRACOTTA_PINK = Color(42, "TERRACOTTA_PINK", (160, 77, 78, 255))
TERRACOTTA_GRAY = Color(43, "TERRACOTTA_GRAY", (57, 41, 35, 255))
TERRACOTTA_LIGHT_GRAY = Color(44, "TERRACOTTA_LIGHT_GRAY", (135, 107, 98, 255))
TERRACOTTA_CYAN = Color(45, "TERRACOTTA_CYAN", (87, 92, 92, 255))
TERRACOTTA_PURPLE = Color(46, "TERRACOTTA_PURPLE", (122, 73, 88, 255))
TERRACOTTA_BLUE = Color(47, "TERRACOTTA_BLUE", (76, 62, 92, 255))
TERRACOTTA_BROWN = Color(48, "TERRACOTTA_BROWN", (76, 50, 35, 255))
TERRACOTTA_GREEN = Color(49, "TERRACOTTA_GREEN", (76, 82, 42, 255))
TERRACOTTA_RED = Color(50, "TERRACOTTA_RED", (142, 60, 46, 255))
TERRACOTTA_BLACK = Color(51, "TERRACOTTA_BLACK", (37, 22, 16, 255))
CRIMSON_NYLIUM = Color(52, "CRIMSON_NYLIUM", (189, 48, 49, 255))
CRIMSON_STEM = Color(53, "CRIMSON_STEM", (148, 63, 97, 255))
CRIMSON_HYPHAE = Color(54, "CRIMSON_HYPHAE", (92, 25, 29, 255))
WARPED_NYLIUM = Color(55, "WARPED_NYLIUM", (22, 126, 134, 255))
WARPED_STEM = Color(56, "WARPED_STEM", (58, 142, 140, 255))
WARPED_HYPHAE = Color(57, "WARPED_HYPHAE", (86, 44, 62, 255))
WARPED_WART_BLOCK = Color(58, "WARPED_WART_BLOCK", (20, 180, 133, 255))