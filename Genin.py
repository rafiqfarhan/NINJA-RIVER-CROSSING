import pygame
import sys
import os
import math
import random

# Initialize Pygame core modules and audio mixers
pygame.init()
pygame.mixer.init()

# --- CONSTANTS & CONFIGURATION ---
SCREEN_WIDTH = 950
SCREEN_HEIGHT = 650
FPS = 60

# --- CINEMATIC PALETTE & COLOR DEFINITIONS ---
COLOR_BG = (10, 14, 22)  # Dark Oceanic Slate
COLOR_CARD = (18, 22, 32)  # Deep Navy Panel
COLOR_WHITE = (245, 247, 250)  # Clean Ice White
COLOR_LIGHT_GREY = (130, 138, 155)  # Muted Steel
COLOR_BLUE = (0, 180, 255)  # Electric Cyan
COLOR_RED = (255, 60, 90)  # Crimson Ninja Red
COLOR_GREEN = (0, 230, 130)  # Deep Emerald
COLOR_GOLD = (255, 180, 0)  # Antique Gold
COLOR_PURPLE = (140, 80, 230)  # Muted Shadow Purple
COLOR_ORANGE = (255, 110, 30)  # Plasma Orange untuk Rogue Ronin

# --- PREMIUM ENVIRONMENT SHADES (FIXED NAMEERROR) ---
COLOR_SEA_DEEP = (8, 24, 48)  # Base Air Sungai Dalam (Gelap)
COLOR_FOAM = (200, 240, 255)  # Buih Ombak Putih Pekat
COLOR_CAUSTIC_SPARK = (220, 245, 255)  # Sparks
COLOR_CLIFF = (36, 28, 22)  # Warna Tebing Tanah/Gunung Gelap
COLOR_CLIFF_LIGHT = (58, 46, 36)  # Highlight Batu Tebing
COLOR_GRASS_DEEP = (12, 38, 20)  # Lumut/Pokok Tebing Sungai

# Coordinates Layout
LEFT_BANK_X = 160
RIGHT_BANK_X = 740
RAFT_LEFT_X = 340
RAFT_RIGHT_X = 520

# ==========================================
# BILINGUAL DICTIONARY
# ==========================================
LOCALIZATION = {
    'EN': {
        'title': "NINJA RIVER CROSSING", 'subtitle': "SECRET SHADOW MISSION",
        'start': "START GAME", 'instructions': "INSTRUCTIONS", 'exit': "EXIT GAME",
        'lang_toggle': "Press [L] to Swap Language  |  Tekan [L] untuk Tukar Bahasa",
        'controls_menu': "Click a button above or press [1], [2], [3] on your keyboard",
        'back_to_menu': "RETURN TO MAIN MENU",
        'level': "LEVEL", 'score': "SCORE", 'time': "TIME LEFT",
        'space_action': "[SPACE] Row Raft", 'reset_action': "[R] Reset Level",
        'menu_action': "[M] Menu", 'lang_action': "[L] Language",
        'max_capacity': "Raft is full! Maximum 2 entities allowed.",
        'opposite_side': "The raft is stationed on the opposite river bank!",
        'pilot_required': "Launch Failed: Raft requires the Ninja Master to row!",
        'embarked': "Embarked", 'disembarked': "Disembarked",
        'win_banner': "LEVEL COMPLETED!", 'victory_banner': "ALL MISSION LEVELS SECURED!",
        'game_over_banner': "MISSION CRITICAL FAILURE", 'any_key': "Click or press any key to proceed...",
        'lvl1_fail_chest': "The unattended Villager plundered the Secret Chest!",
        'lvl2_fail_ronin_chest': "The Rogue Ronin stole the Secret Scrolls!",

        'about_title': "ABOUT THE GAME",
        'about_desc1': "A strategic river-crossing puzzle game where you must guide",
        'about_desc2': "the entire ninja team safely across a turbulent river.",
        'how_title': "HOW TO PLAY",
        'how_desc1': "• Click on characters on the river bank to move them onto the wooden raft.",
        'how_desc2': "• Press [SPACEBAR] to row the raft across to the opposite bank.",
        'how_desc3': "• Click on characters on the raft to make them disembark onto the dry land.",
        'rules_title': "CRITICAL MISSION RULES",
        'rule1': "• CAPACITY: The raft can hold a maximum of 2 characters at the same time.",
        'rule2': "• PILOT: Only the Ninja Master knows how to navigate and row the raft.",
        'rule3a': "• SECURITY: Villager OR Rogue Ronin cannot be left alone with the",
        'rule3b': "  Secret Chest without the presence of the Ninja Master."
    },
    'MY': {
        'title': "MENYEBERANG SUNGAI NINJA", 'subtitle': "MISI SULIT SHADOW",
        'start': "MULA BERMAIN", 'instructions': "ARAHAN PERMAINAN", 'exit': "KELUAR GAME",
        'lang_toggle': "Tekan [L] untuk Tukar Bahasa  |  Press [L] to Swap Language",
        'controls_menu': "Klik butang di atas atau tekan [1], [2], [3] pada papan kekunci",
        'back_to_menu': "KEMBALI KE MENU UTAMA",
        'level': "TAHAP", 'score': "MARKAH", 'time': "MASA",
        'space_action': "[SPACE] Dayung", 'reset_action': "[R] Set Semula",
        'menu_action': "[M] Menu Utama", 'lang_action': "[L] Tukar Bahasa",
        'max_capacity': "Rakit penuh! Maksimum 2 entiti sahaja dibenarkan.",
        'opposite_side': "Rakit berada di tebing seberang sana sungai!",
        'pilot_required': "Gagal: Rakit memerlukan Ninja Master untuk mendayung!",
        'embarked': "Naik rakit:", 'disembarked': "Turun rakit:",
        'win_banner': "TAHAP BERJAYA!", 'victory_banner': "SEMUA TAHAP SELESAI!",
        'game_over_banner': "MISI GAGAL KATASTROFIK", 'any_key': "Klik atau tekan mana-mana butang untuk teruskan...",
        'lvl1_fail_chest': "Orang Kampung mencuri isi kandungan skrol Peti Rahsia!",
        'lvl2_fail_ronin_chest': "Rogue Ronin merompak Peti Rahsia tanpa pengawasan!",

        'about_title': "TENTANG PERMAINAN",
        'about_desc1': "Sebuah game teka-teki strategi menyeberang sungai di mana anda",
        'about_desc2': "perlu membawa semua karakter ke seberang dengan selamat.",
        'how_title': "CARA BERMAIN",
        'how_desc1': "• Klik pada karakter di tebing sungai untuk memasukkan mereka ke dalam rakit kayu.",
        'how_desc2': "• Tekan [SPACEBAR] pada papan kekunci untuk mendayung rakit ke tebing sebelah.",
        'how_desc3': "• Klik karakter di atas rakit untuk menurunkan mereka semula ke atas darat.",
        'rules_title': "PERATURAN UTAMA (RULES)",
        'rule1': "• KAPASITI: Rakit hanya boleh memuatkan maksimum 2 entiti/karakter pada satu-satu masa.",
        'rule2': "• PEMANDU: Hanya Ninja Master sahaja yang mempunyai ilmu untuk mengemudi dan mendayung rakit.",
        'rule3a': "• KESELAMATAN: Orang Kampung ATAU Rogue Ronin dilarang ditinggalkan",
        'rule3b': "  bersama Peti Rahsia tanpa pengawasan daripada Ninja Master."
    }
}


# ==========================================
# 1. GAME ENTITY CLASS
# ==========================================
class GameEntity(pygame.sprite.Sprite):
    def __init__(self, name_en, name_my, identity, start_side, img_name, color):
        super().__init__()
        self.name_en = name_en
        self.name_my = name_my
        self.identity = identity
        self.side = start_side
        self.is_in_raft = False
        self.color = color

        self.image = pygame.Surface((60, 60), pygame.SRCALPHA)

        asset_path = os.path.join("assets", "images", img_name)
        if os.path.exists(asset_path):
            try:
                loaded_img = pygame.image.load(asset_path).convert_alpha()
                self.image = pygame.transform.scale(loaded_img, (60, 60))
            except Exception as e:
                print(f"Error loading image {img_name}: {e}")
                self.draw_vector_avatar()
        else:
            self.draw_vector_avatar()

        self.rect = self.image.get_rect()

    def draw_vector_avatar(self):
        pygame.draw.circle(self.image, self.color, (30, 30), 28, width=2)
        pygame.draw.circle(self.image, (self.color[0] // 2, self.color[1] // 2, self.color[2] // 2), (30, 30), 25)

    def get_name(self, lang):
        return self.name_en if lang == 'EN' else self.name_my

    def update_position(self, target_x, target_y):
        self.rect.centerx += (target_x - self.rect.centerx) * 0.15
        self.rect.centery += (target_y - self.rect.centery) * 0.15


# ==========================================
# 2. BAMBOO RAFT CLASS
# ==========================================
class BambooRaft:
    def __init__(self):
        self.side = 'LEFT'
        self.capacity = 2
        self.passengers = []
        self.x = RAFT_LEFT_X
        self.y = 380
        self.width = 110
        self.height = 75

    def move(self, lang):
        has_pilot = any(p.identity == 'NINJA' for p in self.passengers)
        if not has_pilot:
            return False, LOCALIZATION[lang]['pilot_required']

        self.side = 'RIGHT' if self.side == 'LEFT' else 'LEFT'
        self.x = RAFT_RIGHT_X if self.side == 'RIGHT' else RAFT_LEFT_X

        for passenger in self.passengers:
            passenger.side = self.side
        return True, ""

    def draw_premium_boat(self, surface, time_ms, raft_ready):
        bobbing_y = self.y + int(math.sin(time_ms * 0.005) * 5)
        boat_rect = pygame.Rect(int(self.x), bobbing_y, self.width, self.height)

        wood_dark = (70, 42, 22) if raft_ready else (90, 52, 32)
        wood_light = (115, 74, 44) if raft_ready else (135, 84, 54)
        iron_grey = (55, 60, 70)

        pygame.draw.ellipse(surface, wood_dark, boat_rect)
        pygame.draw.ellipse(surface, wood_light, boat_rect.inflate(-6, -6))
        pygame.draw.ellipse(surface, (45, 26, 12), boat_rect.inflate(-16, -16))

        for offset in [-12, 0, 12]:
            pygame.draw.line(surface, wood_dark, (boat_rect.centerx + offset, boat_rect.top + 8),
                             (boat_rect.centerx + offset, boat_rect.bottom - 8), 2)

        pygame.draw.rect(surface, wood_dark, (boat_rect.x + 12, boat_rect.centery - 24, self.width - 24, 10),
                         border_radius=2)
        pygame.draw.rect(surface, wood_dark, (boat_rect.x + 12, boat_rect.centery + 14, self.width - 24, 10),
                         border_radius=2)

        for x_pos in [boat_rect.x + 28, boat_rect.right - 28]:
            pygame.draw.line(surface, iron_grey, (x_pos, boat_rect.top + 2), (x_pos, boat_rect.bottom - 2), 4)

        status_color = COLOR_GREEN if raft_ready else COLOR_RED
        pygame.draw.ellipse(surface, status_color, boat_rect, width=2)

        return bobbing_y


# ==========================================
# 3. GAME MANAGER CLASS
# ==========================================
class GameManager:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Ninja River Crossing: Secret Mission")
        self.clock = pygame.time.Clock()

        self.state = 'MENU'
        self.lang = 'EN'
        self.score = 0
        self.level = 1

        self.current_music = None

        # Main Menu Buttons
        self.btn_start = pygame.Rect(SCREEN_WIDTH // 2 - 180, 280, 360, 52)
        self.btn_instr = pygame.Rect(SCREEN_WIDTH // 2 - 180, 352, 360, 52)
        self.btn_exit = pygame.Rect(SCREEN_WIDTH // 2 - 180, 424, 360, 52)

        # BACK TO MENU
        self.btn_back = pygame.Rect(SCREEN_WIDTH // 2 - 180, 560, 360, 50)

        self.particles = [{'x': random.randint(0, SCREEN_WIDTH), 'y': random.randint(0, SCREEN_HEIGHT),
                           'speed': random.uniform(0.2, 0.8), 'radius': random.randint(1, 3)} for _ in range(40)]

        self.font_small = pygame.font.SysFont("Segoe UI", 16)
        self.font_mid = pygame.font.SysFont("Segoe UI", 18, bold=True)
        self.font_section = pygame.font.SysFont("Segoe UI", 21, bold=True)
        self.font_large = pygame.font.SysFont("Segoe UI", 42, bold=True)
        self.font_title = pygame.font.SysFont("Impact", 64)

        self.menu_bg = None
        bg_path = os.path.join("assets", "images", "mainmenu.png")
        if os.path.exists(bg_path):
            try:
                loaded_bg = pygame.image.load(bg_path).convert()
                self.menu_bg = pygame.transform.scale(loaded_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
            except Exception as e:
                print(f"Error loading mainmenu.png: {e}")

        self.play_music_by_state()
        self.init_level()

    def play_music_by_state(self):
        if self.state in ['MENU', 'INSTRUCTIONS']:
            target_music = os.path.join("assets", "audio", "Background music.mp3")
        else:
            target_music = os.path.join("assets", "audio", "game level sound.wav")

        if self.current_music != target_music:
            if os.path.exists(target_music):
                try:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(target_music)
                    pygame.mixer.music.play(-1)
                    pygame.mixer.music.set_volume(0.3)
                    self.current_music = target_music
                except Exception as e:
                    print(f"Audio Engine System Error: {e}")

    def init_level(self):
        self.raft = BambooRaft()
        if self.level == 1:
            self.time_remaining = 60.0
        elif self.level == 2:
            self.time_remaining = 45.0
        else:
            self.time_remaining = 35.0

        self.status_message = ""
        self.level_done = False

        self.entities = [
            GameEntity("Ninja Master", "Guru Ninja", "NINJA", "LEFT", "ninjamaster.png", COLOR_BLUE),
            GameEntity("Samurai", "Samurai", "SAMURAI", "LEFT", "samurai.png", COLOR_RED),
            GameEntity("Villager", "Orang Kampung", "VILLAGER", "LEFT", "villager.png", COLOR_PURPLE),
            GameEntity("Secret Chest", "Peti Rahsia", "CHEST", "LEFT", "secretchest.png", COLOR_GOLD)
        ]

        if self.level >= 2:
            self.entities.append(
                GameEntity("Rogue Ronin", "Ronin Liar", "RONIN", "LEFT", "ronin.png", COLOR_ORANGE)
            )

    def check_puzzle_rules(self):
        left_bank = [e.identity for e in self.entities if e.side == 'LEFT' and not e.is_in_raft]
        right_bank = [e.identity for e in self.entities if e.side == 'RIGHT' and not e.is_in_raft]

        for bank in [left_bank, right_bank]:
            if 'VILLAGER' in bank and 'CHEST' in bank and 'NINJA' not in bank:
                self.state = 'GAME_OVER'
                self.status_message = LOCALIZATION[self.lang]['lvl1_fail_chest']
                self.play_music_by_state()
                return

            if self.level >= 2:
                if 'RONIN' in bank and 'CHEST' in bank and 'NINJA' not in bank:
                    self.state = 'GAME_OVER'
                    self.status_message = LOCALIZATION[self.lang]['lvl2_fail_ronin_chest']
                    self.play_music_by_state()
                    return

        if all(e.side == 'RIGHT' and not e.is_in_raft for e in self.entities):
            level_points = 1000 + int(self.time_remaining * 15)
            self.score += level_points
            if self.level < 3:
                self.state = 'LEVEL_CLEARED'
            else:
                self.state = 'VICTORY'
            self.play_music_by_state()

    def handle_mouse_clicks(self, pos):
        if self.state == 'MENU':
            if self.btn_start.collidepoint(pos):
                self.state = 'PLAYING'
                self.status_message = ""
                self.play_music_by_state()
            elif self.btn_instr.collidepoint(pos):
                self.state = 'INSTRUCTIONS'
                self.play_music_by_state()
            elif self.btn_exit.collidepoint(pos):
                pygame.quit()
                sys.exit()
        elif self.state == 'INSTRUCTIONS':
            if self.btn_back.collidepoint(pos):
                self.state = 'MENU'
                self.play_music_by_state()
        elif self.state == 'PLAYING':
            for entity in self.entities:
                if entity.rect.collidepoint(pos):
                    if entity.is_in_raft:
                        entity.is_in_raft = False
                        self.raft.passengers.remove(entity)
                        self.status_message = f"{LOCALIZATION[self.lang]['disembarked']} {entity.get_name(self.lang)}"
                        if len(self.raft.passengers) == 0:
                            self.check_puzzle_rules()
                    else:
                        if entity.side == self.raft.side:
                            if len(self.raft.passengers) < self.raft.capacity:
                                entity.is_in_raft = True
                                self.raft.passengers.append(entity)
                                self.status_message = f"{LOCALIZATION[self.lang]['embarked']} {entity.get_name(self.lang)}"
                            else:
                                self.status_message = LOCALIZATION[self.lang]['max_capacity']
                        else:
                            self.status_message = LOCALIZATION[self.lang]['opposite_side']
                    return

    def update_ambient_particles(self):
        for p in self.particles:
            p['y'] += p['speed']
            if p['y'] > SCREEN_HEIGHT:
                p['y'] = -10
                p['x'] = random.randint(0, SCREEN_WIDTH)
            pygame.draw.circle(self.screen, (75, 85, 110), (int(p['x']), int(p['y'])), p['radius'])

    def draw_menu(self):
        if self.menu_bg:
            self.screen.blit(self.menu_bg, (0, 0))
        else:
            self.screen.fill(COLOR_BG)

        self.update_ambient_particles()

        title_surf = self.font_title.render(LOCALIZATION[self.lang]['title'], True, COLOR_WHITE)
        sub_surf = self.font_mid.render(LOCALIZATION[self.lang]['subtitle'], True, COLOR_GOLD)

        self.screen.blit(title_surf, (SCREEN_WIDTH // 2 - title_surf.get_width() // 2, 80))
        self.screen.blit(sub_surf, (SCREEN_WIDTH // 2 - sub_surf.get_width() // 2, 155))

        m_pos = pygame.mouse.get_pos()
        buttons = [
            (self.btn_start, LOCALIZATION[self.lang]['start'], COLOR_GREEN),
            (self.btn_instr, LOCALIZATION[self.lang]['instructions'], COLOR_BLUE),
            (self.btn_exit, LOCALIZATION[self.lang]['exit'], COLOR_RED)
        ]

        for rect, text, active_color in buttons:
            hover = rect.collidepoint(m_pos)
            fill_color = active_color if hover else COLOR_CARD
            text_color = COLOR_BG if hover else COLOR_WHITE

            pygame.draw.rect(self.screen, fill_color, rect, border_radius=10)
            pygame.draw.rect(self.screen, active_color, rect, width=2, border_radius=10)

            txt_surf = self.font_mid.render(text, True, text_color)
            self.screen.blit(txt_surf,
                             (rect.centerx - txt_surf.get_width() // 2, rect.centery - txt_surf.get_height() // 2))

        help_surf = self.font_small.render(LOCALIZATION[self.lang]['controls_menu'], True, COLOR_LIGHT_GREY)
        lang_surf = self.font_mid.render(LOCALIZATION[self.lang]['lang_toggle'], True, COLOR_GOLD)

        self.screen.blit(help_surf, (SCREEN_WIDTH // 2 - help_surf.get_width() // 2, 510))
        self.screen.blit(lang_surf, (SCREEN_WIDTH // 2 - lang_surf.get_width() // 2, 560))

    def draw_instructions(self):
        """FIXED: Dynamic Y-Spacing Layout Engine to eliminate overlapping text lines."""
        self.screen.fill(COLOR_BG)
        self.update_ambient_particles()

        # Outer Card Panel
        pygame.draw.rect(self.screen, COLOR_CARD, (45, 20, SCREEN_WIDTH - 90, 515), border_radius=12)
        pygame.draw.rect(self.screen, COLOR_BLUE, (45, 20, SCREEN_WIDTH - 90, 515), width=2, border_radius=12)

        # Page Header Title
        title_surf = self.font_large.render(LOCALIZATION[self.lang]['instructions'], True, COLOR_GOLD)
        self.screen.blit(title_surf, (70, 35))

        current_lang_dict = LOCALIZATION[self.lang]
        startX = 70
        startY = 105  # Initial baseline cursor position

        # Section 1: About the Game
        sect1_title = self.font_section.render(current_lang_dict['about_title'], True, COLOR_BLUE)
        self.screen.blit(sect1_title, (startX, startY))
        startY += 28  # Safe margin below section header

        desc_surf1 = self.font_small.render(current_lang_dict['about_desc1'], True, COLOR_WHITE)
        self.screen.blit(desc_surf1, (startX, startY))
        startY += 20
        desc_surf2 = self.font_small.render(current_lang_dict['about_desc2'], True, COLOR_WHITE)
        self.screen.blit(desc_surf2, (startX, startY))
        startY += 35  # Large gap between distinct blocks

        # Section 2: How to Play
        sect2_title = self.font_section.render(current_lang_dict['how_title'], True, COLOR_GREEN)
        self.screen.blit(sect2_title, (startX, startY))
        startY += 28

        h1 = self.font_small.render(current_lang_dict['how_desc1'], True, COLOR_WHITE)
        self.screen.blit(h1, (startX, startY))
        startY += 22
        h2 = self.font_small.render(current_lang_dict['how_desc2'], True, COLOR_WHITE)
        self.screen.blit(h2, (startX, startY))
        startY += 22
        h3 = self.font_small.render(current_lang_dict['how_desc3'], True, COLOR_WHITE)
        self.screen.blit(h3, (startX, startY))
        startY += 35

        # Section 3: Critical Mission Rules
        sect3_title = self.font_section.render(current_lang_dict['rules_title'], True, COLOR_RED)
        self.screen.blit(sect3_title, (startX, startY))
        startY += 28

        r1 = self.font_small.render(current_lang_dict['rule1'], True, COLOR_WHITE)
        self.screen.blit(r1, (startX, startY))
        startY += 22
        r2 = self.font_small.render(current_lang_dict['rule2'], True, COLOR_WHITE)
        self.screen.blit(r2, (startX, startY))
        startY += 22
        r3a = self.font_small.render(current_lang_dict['rule3a'], True, COLOR_LIGHT_GREY)
        self.screen.blit(r3a, (startX, startY))
        startY += 20
        r3b = self.font_small.render(current_lang_dict['rule3b'], True, COLOR_LIGHT_GREY)
        self.screen.blit(r3b, (startX, startY))

        # Language Swap Hint Footer Label
        lang_hint = self.font_small.render(LOCALIZATION[self.lang]['lang_toggle'], True, COLOR_GOLD)
        self.screen.blit(lang_hint, (SCREEN_WIDTH // 2 - lang_hint.get_width() // 2, 495))

        # Bottom Menu Return Button Controls
        m_pos = pygame.mouse.get_pos()
        hover = self.btn_back.collidepoint(m_pos)
        fill_color = COLOR_BLUE if hover else COLOR_CARD
        text_color = COLOR_BG if hover else COLOR_WHITE

        pygame.draw.rect(self.screen, fill_color, self.btn_back, border_radius=10)
        pygame.draw.rect(self.screen, COLOR_BLUE, self.btn_back, width=2, border_radius=10)

        back_surf = self.font_mid.render(LOCALIZATION[self.lang]['back_to_menu'], True, text_color)
        self.screen.blit(back_surf, (self.btn_back.centerx - back_surf.get_width() // 2,
                                     self.btn_back.centery - back_surf.get_height() // 2))

    def draw_gameplay(self):
        self.screen.fill(COLOR_BG)
        time_ms = pygame.time.get_ticks()

        # Base River Background (Deep Water Core)
        river_rect = pygame.Rect(320, 0, 310, SCREEN_HEIGHT)
        pygame.draw.rect(self.screen, COLOR_SEA_DEEP, river_rect)

        # --- HORIZONTAL WATER FLOWING SECTIONS (UP TO DOWN) ---
        flow_speed = 0.22
        for i in range(14):
            base_y = (i * 55) + int(time_ms * flow_speed)
            y_coord = base_y % (SCREEN_HEIGHT + 60) - 30

            points_left_to_right = []
            for x_coord in range(river_rect.left, river_rect.right + 20, 15):
                wave_ripple = math.sin((time_ms * 0.005) + (x_coord * 0.025) + (i * 1.1)) * 14
                points_left_to_right.append((x_coord, y_coord + wave_ripple))

            if len(points_left_to_right) > 1:
                b_color = (12, 60 + (i % 3) * 20, 120 + (i % 4) * 25)
                pygame.draw.lines(self.screen, b_color, False, points_left_to_right, 2)

                if i % 2 == 0:
                    pygame.draw.lines(self.screen, COLOR_FOAM, False, points_left_to_right[1:-1], 1)

        # Ambient Water Flotsam / Sparkling Caustic Particles (Flowing Downwards)
        random.seed(777)
        for i in range(30):
            p_flow = 0.2 + (i % 3) * 0.08
            spark_y = (random.randint(0, SCREEN_HEIGHT) + int(time_ms * p_flow)) % SCREEN_HEIGHT

            sway_x = math.sin((time_ms * 0.003) + (spark_y * 0.015)) * 16
            spark_x = river_rect.left + random.randint(20, 290) + int(sway_x)

            if river_rect.left < spark_x < river_rect.right:
                alpha = abs(math.sin(time_ms * 0.004 + i))
                p_radius = 3 if alpha > 0.6 else 2
                pygame.draw.circle(self.screen, COLOR_CAUSTIC_SPARK, (spark_x, spark_y), p_radius)
        random.seed()

        # --- RENDER ORGANIC RUGGED MOUNTAIN CLIFFS (TEBING ZIGZAG) ---
        pygame.draw.rect(self.screen, COLOR_CLIFF, (0, 0, 320, SCREEN_HEIGHT))
        pygame.draw.rect(self.screen, COLOR_CLIFF, (630, 0, 320, SCREEN_HEIGHT))

        for y_sec in range(0, SCREEN_HEIGHT + 30, 30):
            cliff_sway = math.sin((time_ms * 0.0012) + y_sec * 0.03) * 5

            # Left Rocky Extensions
            pygame.draw.polygon(self.screen, COLOR_CLIFF_LIGHT, [
                (305 + cliff_sway, y_sec), (325 + cliff_sway, y_sec + 15),
                (310 + cliff_sway, y_sec + 30), (275, y_sec + 15)
            ])
            # Right Rocky Extensions
            pygame.draw.polygon(self.screen, COLOR_CLIFF_LIGHT, [
                (645 - cliff_sway, y_sec), (625 - cliff_sway, y_sec + 15),
                (640 - cliff_sway, y_sec + 30), (675, y_sec + 15)
            ])

        # Outer thick moss framing
        pygame.draw.rect(self.screen, COLOR_GRASS_DEEP, (0, 0, 270, SCREEN_HEIGHT), width=18)
        pygame.draw.rect(self.screen, COLOR_GRASS_DEEP, (680, 0, 270, SCREEN_HEIGHT), width=18)
        pygame.draw.rect(self.screen, COLOR_BG, (318, 0, 4, SCREEN_HEIGHT))
        pygame.draw.rect(self.screen, COLOR_BG, (628, 0, 4, SCREEN_HEIGHT))

        # --- DRAW RAFT BOAT & CHARACTERS ---
        raft_ready = any(p.identity == 'NINJA' for p in self.raft.passengers)
        current_boat_y = self.raft.draw_premium_boat(self.screen, time_ms, raft_ready)

        for entity in self.entities:
            self.screen.blit(entity.image, entity.rect)
            if entity.is_in_raft:
                pygame.draw.circle(self.screen, COLOR_GREEN, (entity.rect.centerx, entity.rect.bottom + 5), 4)
            lbl = self.font_small.render(entity.get_name(self.lang), True, COLOR_WHITE)
            self.screen.blit(lbl, (entity.rect.centerx - lbl.get_width() // 2, entity.rect.y - 25))

        # Top HUD Banner Panel
        pygame.draw.rect(self.screen, COLOR_CARD, (0, 0, SCREEN_WIDTH, 65))
        pygame.draw.line(self.screen, COLOR_BLUE, (0, 65), (SCREEN_WIDTH, 65), 2)

        lvl_surf = self.font_mid.render(f"{LOCALIZATION[self.lang]['level']}: {self.level}", True, COLOR_WHITE)
        score_surf = self.font_mid.render(f"{LOCALIZATION[self.lang]['score']}: {self.score}", True, COLOR_GOLD)
        t_color = COLOR_RED if self.time_remaining < 15 else COLOR_GREEN
        time_surf = self.font_mid.render(f"{LOCALIZATION[self.lang]['time']}: {int(self.time_remaining)}s", True,
                                         t_color)

        self.screen.blit(lvl_surf, (40, 18))
        self.screen.blit(score_surf, (220, 18))
        self.screen.blit(time_surf, (SCREEN_WIDTH - 200, 18))

        # Bottom Navigation Control Frame
        pygame.draw.rect(self.screen, COLOR_CARD, (0, SCREEN_HEIGHT - 75, SCREEN_WIDTH, 75))
        pygame.draw.line(self.screen, COLOR_BLUE, (0, SCREEN_HEIGHT - 75), (SCREEN_WIDTH, SCREEN_HEIGHT - 75), 2)

        action_str = f"{LOCALIZATION[self.lang]['space_action']}    |    {LOCALIZATION[self.lang]['reset_action']}    |    {LOCALIZATION[self.lang]['menu_action']}    |    {LOCALIZATION[self.lang]['lang_action']}"
        actions_surf = self.font_small.render(action_str, True, COLOR_LIGHT_GREY)
        self.screen.blit(actions_surf, (40, SCREEN_HEIGHT - 62))

        if self.status_message:
            msg_surf = self.font_small.render(self.status_message, True, COLOR_GOLD)
            self.screen.blit(msg_surf, (40, SCREEN_HEIGHT - 34))

        return current_boat_y

    def draw_overlays(self):
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((8, 10, 16, 240))
        self.screen.blit(overlay, (0, 0))

        if self.state == 'LEVEL_CLEARED':
            banner = LOCALIZATION[self.lang]['win_banner']
            color = COLOR_GREEN
        elif self.state == 'VICTORY':
            banner = LOCALIZATION[self.lang]['victory_banner']
            color = COLOR_GOLD
        else:
            banner = LOCALIZATION[self.lang]['game_over_banner']
            color = COLOR_RED

        title_surf = self.font_large.render(banner, True, color)
        self.screen.blit(title_surf, (SCREEN_WIDTH // 2 - title_surf.get_width() // 2, SCREEN_HEIGHT // 2 - 100))

        if self.status_message:
            msg_surf = self.font_mid.render(self.status_message, True, COLOR_WHITE)
            self.screen.blit(msg_surf, (SCREEN_WIDTH // 2 - msg_surf.get_width() // 2, SCREEN_HEIGHT // 2 - 20))

        cont_surf = self.font_small.render(LOCALIZATION[self.lang]['any_key'], True, COLOR_LIGHT_GREY)
        self.screen.blit(cont_surf, (SCREEN_WIDTH // 2 - cont_surf.get_width() // 2, SCREEN_HEIGHT // 2 + 60))

    def run(self):
        while True:
            dt = self.clock.tick(FPS) / 1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.state in ['MENU', 'INSTRUCTIONS']:
                        self.handle_mouse_clicks(event.pos)
                    elif self.state == 'PLAYING':
                        self.handle_mouse_clicks(event.pos)
                    elif self.state in ['LEVEL_CLEARED', 'GAME_OVER', 'VICTORY']:
                        if self.state == 'LEVEL_CLEARED':
                            self.level += 1
                            self.state = 'PLAYING'
                            self.init_level()
                            self.play_music_by_state()
                        else:
                            self.state = 'MENU'
                            self.level = 1
                            self.score = 0
                            self.init_level()
                            self.play_music_by_state()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_l:
                        self.lang = 'MY' if self.lang == 'EN' else 'EN'
                        if self.state == 'PLAYING':
                            self.status_message = LOCALIZATION[self.lang]['lang_action']

                    elif event.key == pygame.K_m:
                        self.state = 'MENU'
                        self.level = 1
                        self.score = 0
                        self.init_level()
                        self.play_music_by_state()

                    elif self.state == 'MENU':
                        if event.key in [pygame.K_1, pygame.K_KP1]:
                            self.state = 'PLAYING'
                            self.status_message = ""
                            self.play_music_by_state()
                        elif event.key in [pygame.K_2, pygame.K_KP2]:
                            self.state = 'INSTRUCTIONS'
                            self.play_music_by_state()
                        elif event.key in [pygame.K_3, pygame.K_KP3]:
                            pygame.quit()
                            sys.exit()

                    elif self.state == 'INSTRUCTIONS':
                        if event.key != pygame.K_l:
                            self.state = 'MENU'
                            self.play_music_by_state()

                    elif self.state == 'PLAYING':
                        if event.key == pygame.K_SPACE:
                            success, msg = self.raft.move(self.lang)
                            if not success:
                                self.status_message = msg
                            else:
                                self.status_message = ""
                                self.check_puzzle_rules()
                        elif event.key == pygame.K_r:
                            self.score = max(0, self.score - 100)
                            self.init_level()

                    elif self.state in ['LEVEL_CLEARED', 'GAME_OVER', 'VICTORY']:
                        if self.state == 'LEVEL_CLEARED':
                            self.level += 1
                            self.state = 'PLAYING'
                            self.init_level()
                            self.play_music_by_state()
                        else:
                            self.state = 'MENU'
                            self.level = 1
                            self.score = 0
                            self.init_level()
                            self.play_music_by_state()

            if self.state == 'PLAYING':
                self.time_remaining -= dt
                if self.time_remaining <= 0:
                    self.time_remaining = 0
                    self.state = 'GAME_OVER'
                    self.status_message = "TIME EXPIRED: Enemy guards spotted your location!"
                    self.play_music_by_state()

            if self.state in ['PLAYING', 'LEVEL_CLEARED', 'GAME_OVER', 'VICTORY']:
                target_raft_x = RAFT_RIGHT_X if self.raft.side == 'RIGHT' else RAFT_LEFT_X
                self.raft.x += (target_raft_x - self.raft.x) * 0.15

                current_boat_y = self.raft.y + int(math.sin(pygame.time.get_ticks() * 0.005) * 4)

                l_idx, r_idx = 0, 0
                for entity in self.entities:
                    if entity.is_in_raft:
                        offset = self.raft.passengers.index(entity)
                        entity.update_position(int(self.raft.x) + (offset * 48) + 32, current_boat_y + 38)
                    else:
                        if entity.side == 'LEFT':
                            entity.update_position(LEFT_BANK_X, 160 + (l_idx * 78))
                            l_idx += 1
                        else:
                            entity.update_position(RIGHT_BANK_X, 160 + (r_idx * 78))
                            r_idx += 1

            if self.state == 'MENU':
                self.draw_menu()
            elif self.state == 'INSTRUCTIONS':
                self.draw_instructions()
            else:
                self.draw_gameplay()
                if self.state in ['LEVEL_CLEARED', 'GAME_OVER', 'VICTORY']:
                    self.draw_overlays()

            pygame.display.flip()


if __name__ == "__main__":
    game = GameManager()
    game.run()