import pygame
import sys
import os
import math
import random

# Initialize pygame siap-siap
pygame.init()
pygame.mixer.init()

# Setup screen size dengan FPS
SCREEN_WIDTH = 950
SCREEN_HEIGHT = 650
FPS = 60

# Senarai kod warna RGB (guna nama simple)
WARNA_BG = (10, 14, 22)
WARNA_KOTAK = (18, 22, 32)
WARNA_PUTIH = (245, 247, 250)
WARNA_KELABU = (130, 138, 155)
WARNA_BIRU = (0, 180, 255)
WARNA_MERAH = (255, 60, 90)
WARNA_HIJAU = (0, 230, 130)
WARNA_EMAS = (255, 180, 0)
WARNA_UNGU = (140, 80, 230)
WARNA_OREN = (255, 110, 30)

# Warna untuk map/sungai
WARNA_SUNGAI = (8, 24, 48)
WARNA_BUIH = (200, 240, 255)
WARNA_SPARK = (220, 245, 255)
WARNA_TEBING = (36, 28, 22)
WARNA_TEBING_LIGHT = (58, 46, 36)
WARNA_RUMPUT = (12, 38, 20)

# Set koordinat paksi-X tebing dan rakit
TEBING_KIRI_X = 160
TEBING_KANAN_X = 740
RAKIT_KIRI_X = 340
RAKIT_KANAN_X = 520

# Data translation (English & Melayu)
teks_bahasa = {
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


# Kelas untuk karakter/objek game
class GameEntity(pygame.sprite.Sprite):
    def __init__(self, name_en, name_my, identity, start_side, img_name, warna):
        super().__init__()
        self.name_en = name_en
        self.name_my = name_my
        self.identity = identity
        self.side = start_side
        self.is_in_raft = False
        self.color = warna

        self.image = pygame.Surface((60, 60), pygame.SRCALPHA)

        # Try load gambar, kalau tak jumpa buat bulatan biasa biar tak crash
        asset_path = os.path.join("assets", "images", img_name)
        if os.path.exists(asset_path):
            try:
                loaded_img = pygame.image.load(asset_path).convert_alpha()
                self.image = pygame.transform.scale(loaded_img, (60, 60))
            except:
                self.lukis_bulatan_ganti()
        else:
            self.lukis_bulatan_ganti()

        self.rect = self.image.get_rect()

    def lukis_bulatan_ganti(self):
        pygame.draw.circle(self.image, self.color, (30, 30), 28, width=2)
        pygame.draw.circle(self.image, (self.color[0] // 2, self.color[1] // 2, self.color[2] // 2), (30, 30), 25)

    def dapatkan_nama(self, bahasa):
        if bahasa == 'EN':
            return self.name_en
        return self.name_my

    def update_posisi(self, target_x, target_y):
        # Bagi nampak smooth sikit masa slide gerak
        self.rect.centerx += (target_x - self.rect.centerx) * 0.15
        self.rect.centery += (target_y - self.rect.centery) * 0.15


# Kelas untuk rakit
class BambooRaft:
    def __init__(self):
        self.side = 'LEFT'
        self.capacity = 2
        self.passengers = []
        self.x = RAKIT_KIRI_X
        self.y = 380
        self.width = 110
        self.height = 75

    def gerak_seberang(self, bahasa):
        # Jangan bagi gerak kalau ninja takde dalam list penumpang
        ada_ninja = any(p.identity == 'NINJA' for p in self.passengers)
        if not ada_ninja:
            return False, teks_bahasa[bahasa]['pilot_required']

        if self.side == 'LEFT':
            self.side = 'RIGHT'
            self.x = RAKIT_KANAN_X
        else:
            self.side = 'LEFT'
            self.x = RAKIT_KIRI_X

        for p in self.passengers:
            p.side = self.side
        return True, ""

    def lukis_rakit(self, surface, masa_ms, rakit_sedia):
        # Buat animasi rakit beralun naik turun sikit
        ombak_y = self.y + int(math.sin(masa_ms * 0.005) * 5)
        raft_rect = pygame.Rect(int(self.x), ombak_y, self.width, self.height)

        warna_kayu_gelap = (70, 42, 22) if rakit_sedia else (90, 52, 32)
        warna_kayu_cerah = (115, 74, 44) if rakit_sedia else (135, 84, 54)

        pygame.draw.ellipse(surface, warna_kayu_gelap, raft_rect)
        pygame.draw.ellipse(surface, warna_kayu_cerah, raft_rect.inflate(-6, -6))
        pygame.draw.ellipse(surface, (45, 26, 12), raft_rect.inflate(-16, -16))

        for j in [-12, 0, 12]:
            pygame.draw.line(surface, warna_kayu_gelap, (raft_rect.centerx + j, raft_rect.top + 8),
                             (raft_rect.centerx + j, raft_rect.bottom - 8), 2)

        warna_lampu = WARNA_HIJAU if rakit_sedia else WARNA_MERAH
        pygame.draw.ellipse(surface, warna_lampu, raft_rect, width=2)

        return ombak_y


# Kelas utama pengurus skrin dan loop game
class GameManager:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Ninja River Crossing")
        self.clock = pygame.time.Clock()

        self.state = 'MENU'
        self.bahasa = 'EN'
        self.score = 0
        self.level = 1
        self.lagu_sekarang = None

        # Koordinat butang menu utama
        self.btn_start = pygame.Rect(SCREEN_WIDTH // 2 - 180, 280, 360, 52)
        self.btn_instr = pygame.Rect(SCREEN_WIDTH // 2 - 180, 352, 360, 52)
        self.btn_exit = pygame.Rect(SCREEN_WIDTH // 2 - 180, 424, 360, 52)
        self.btn_back = pygame.Rect(SCREEN_WIDTH // 2 - 180, 560, 360, 50)

        # Habuk/partikel terbang kat background
        self.habuk_list = [{'x': random.randint(0, SCREEN_WIDTH), 'y': random.randint(0, SCREEN_HEIGHT),
                            'speed': random.uniform(0.2, 0.8), 'radius': random.randint(1, 3)} for _ in range(40)]

        # Set font tulisan
        self.font_kecik = pygame.font.SysFont("Segoe UI", 16)
        self.font_sedang = pygame.font.SysFont("Segoe UI", 18, bold=True)
        self.font_seksyen = pygame.font.SysFont("Segoe UI", 21, bold=True)
        self.font_besar = pygame.font.SysFont("Segoe UI", 42, bold=True)
        self.font_tajuk = pygame.font.SysFont("Impact", 64)

        self.menu_bg = None
        bg_path = os.path.join("assets", "images", "mainmenu.png")
        if os.path.exists(bg_path):
            try:
                loaded_bg = pygame.image.load(bg_path).convert()
                self.menu_bg = pygame.transform.scale(loaded_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
            except:
                pass

        self.tukar_lagu_bg()
        self.init_level_baru()

    def tukar_lagu_bg(self):
        # Sini aku dah kemaskan path audio baru ke .mp3 ikut folder kau
        if self.state in ['MENU', 'INSTRUCTIONS']:
            path_lagu = os.path.join("assets", "audio", "Background music.mp3")
        else:
            path_lagu = os.path.join("assets", "audio", "game level sound.mp3")

        if self.lagu_sekarang != path_lagu:
            if os.path.exists(path_lagu):
                try:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(path_lagu)
                    pygame.mixer.music.play(-1)
                    pygame.mixer.music.set_volume(0.3)
                    self.lagu_sekarang = path_lagu
                except:
                    print("Audio failed to load")

    def init_level_baru(self):
        self.raft = BambooRaft()
        if self.level == 1:
            self.masa_tinggal = 60.0
        elif self.level == 2:
            self.masa_tinggal = 45.0
        else:
            self.masa_tinggal = 35.0

        self.mesej_status = ""

        self.entities = [
            GameEntity("Ninja Master", "Guru Ninja", "NINJA", "LEFT", "ninjamaster.png", WARNA_BIRU),
            GameEntity("Samurai", "Samurai", "SAMURAI", "LEFT", "samurai.png", WARNA_MERAH),
            GameEntity("Villager", "Orang Kampung", "VILLAGER", "LEFT", "villager.png", WARNA_UNGU),
            GameEntity("Secret Chest", "Peti Rahsia", "CHEST", "LEFT", "secretchest.png", WARNA_EMAS)
        ]

        # Tambah ronin kalau level 2 ke atas
        if self.level >= 2:
            self.entities.append(
                GameEntity("Rogue Ronin", "Ronin Liar", "RONIN", "LEFT", "ronin.png", WARNA_OREN)
            )

    def semak_peraturan_game(self):
        tebing_kiri = [e.identity for e in self.entities if e.side == 'LEFT' and not e.is_in_raft]
        tebing_kanan = [e.identity for e in self.entities if e.side == 'RIGHT' and not e.is_in_raft]

        # Check rule teka-teki kalah/menang
        for tebing in [tebing_kiri, tebing_kanan]:
            if 'VILLAGER' in tebing and 'CHEST' in tebing and 'NINJA' not in tebing:
                self.state = 'GAME_OVER'
                self.mesej_status = teks_bahasa[self.bahasa]['lvl1_fail_chest']
                self.tukar_lagu_bg()
                return

            if self.level >= 2:
                if 'RONIN' in tebing and 'CHEST' in tebing and 'NINJA' not in tebing:
                    self.state = 'GAME_OVER'
                    self.mesej_status = teks_bahasa[self.bahasa]['lvl2_fail_ronin_chest']
                    self.tukar_lagu_bg()
                    return

        # Check kalau semua dah selamat sampai seberang kanan
        if all(e.side == 'RIGHT' and not e.is_in_raft for e in self.entities):
            kira_markah = 1000 + int(self.masa_tinggal * 15)
            self.score += kira_markah
            if self.level < 3:
                self.state = 'LEVEL_CLEARED'
            else:
                self.state = 'VICTORY'
            self.tukar_lagu_bg()

    def klik_tetikus(self, pos):
        if self.state == 'MENU':
            if self.btn_start.collidepoint(pos):
                self.state = 'PLAYING'
                self.mesej_status = ""
                self.tukar_lagu_bg()
            elif self.btn_instr.collidepoint(pos):
                self.state = 'INSTRUCTIONS'
                self.tukar_lagu_bg()
            elif self.btn_exit.collidepoint(pos):
                pygame.quit()
                sys.exit()
        elif self.state == 'INSTRUCTIONS':
            if self.btn_back.collidepoint(pos):
                self.state = 'MENU'
                self.tukar_lagu_bg()
        elif self.state == 'PLAYING':
            for entity in self.entities:
                if entity.rect.collidepoint(pos):
                    if entity.is_in_raft:
                        entity.is_in_raft = False
                        self.raft.passengers.remove(entity)
                        self.mesej_status = f"{teks_bahasa[self.bahasa]['disembarked']} {entity.dapatkan_nama(self.bahasa)}"
                        if len(self.raft.passengers) == 0:
                            self.semak_peraturan_game()
                    else:
                        if entity.side == self.raft.side:
                            if len(self.raft.passengers) < self.raft.capacity:
                                entity.is_in_raft = True
                                self.raft.passengers.append(entity)
                                self.mesej_status = f"{teks_bahasa[self.bahasa]['embarked']} {entity.dapatkan_nama(self.bahasa)}"
                            else:
                                self.mesej_status = teks_bahasa[self.bahasa]['max_capacity']
                        else:
                            self.mesej_status = teks_bahasa[self.bahasa]['opposite_side']
                    return

    def update_animasi_habuk(self):
        for p in self.habuk_list:
            p['y'] += p['speed']
            if p['y'] > SCREEN_HEIGHT:
                p['y'] = -10
                p['x'] = random.randint(0, SCREEN_WIDTH)
            pygame.draw.circle(self.screen, (75, 85, 110), (int(p['x']), int(p['y'])), p['radius'])

    def lukis_menu_utama(self):
        if self.menu_bg:
            self.screen.blit(self.menu_bg, (0, 0))
        else:
            self.screen.fill(WARNA_BG)

        self.update_animasi_habuk()

        title_surf = self.font_tajuk.render(teks_bahasa[self.bahasa]['title'], True, WARNA_PUTIH)
        sub_surf = self.font_sedang.render(teks_bahasa[self.bahasa]['subtitle'], True, WARNA_EMAS)

        self.screen.blit(title_surf, (SCREEN_WIDTH // 2 - title_surf.get_width() // 2, 80))
        self.screen.blit(sub_surf, (SCREEN_WIDTH // 2 - sub_surf.get_width() // 2, 155))

        m_pos = pygame.mouse.get_pos()
        buttons = [
            (self.btn_start, teks_bahasa[self.bahasa]['start'], WARNA_HIJAU),
            (self.btn_instr, teks_bahasa[self.bahasa]['instructions'], WARNA_BIRU),
            (self.btn_exit, teks_bahasa[self.bahasa]['exit'], WARNA_MERAH)
        ]

        for rect, teks, warna_aktif in buttons:
            hover = rect.collidepoint(m_pos)
            warna_isi = warna_aktif if hover else WARNA_KOTAK
            warna_teks = WARNA_BG if hover else WARNA_PUTIH

            pygame.draw.rect(self.screen, warna_isi, rect, border_radius=10)
            pygame.draw.rect(self.screen, warna_aktif, rect, width=2, border_radius=10)

            txt_surf = self.font_sedang.render(teks, True, warna_teks)
            self.screen.blit(txt_surf,
                             (rect.centerx - txt_surf.get_width() // 2, rect.centery - txt_surf.get_height() // 2))

        help_surf = self.font_kecik.render(teks_bahasa[self.bahasa]['controls_menu'], True, WARNA_KELABU)
        lang_surf = self.font_sedang.render(teks_bahasa[self.bahasa]['lang_toggle'], True, WARNA_EMAS)

        self.screen.blit(help_surf, (SCREEN_WIDTH // 2 - help_surf.get_width() // 2, 510))
        self.screen.blit(lang_surf, (SCREEN_WIDTH // 2 - lang_surf.get_width() // 2, 560))

    def lukis_skrin_arahan(self):
        self.screen.fill(WARNA_BG)
        self.update_animasi_habuk()

        pygame.draw.rect(self.screen, WARNA_KOTAK, (45, 20, SCREEN_WIDTH - 90, 515), border_radius=12)
        pygame.draw.rect(self.screen, WARNA_BIRU, (45, 20, SCREEN_WIDTH - 90, 515), width=2, border_radius=12)

        title_surf = self.font_besar.render(teks_bahasa[self.bahasa]['instructions'], True, WARNA_EMAS)
        self.screen.blit(title_surf, (70, 35))

        dict_skrg = teks_bahasa[self.bahasa]
        startX = 70
        startY = 105

        # Buat manual jarak Y biar tulisan tak bertindih hancur
        t_sec1 = self.font_seksyen.render(dict_skrg['about_title'], True, WARNA_BIRU)
        self.screen.blit(t_sec1, (startX, startY))
        startY += 28

        d1 = self.font_kecik.render(dict_skrg['about_desc1'], True, WARNA_PUTIH)
        self.screen.blit(d1, (startX, startY))
        startY += 20
        d2 = self.font_kecik.render(dict_skrg['about_desc2'], True, WARNA_PUTIH)
        self.screen.blit(d2, (startX, startY))
        startY += 35

        t_sec2 = self.font_seksyen.render(dict_skrg['how_title'], True, WARNA_HIJAU)
        self.screen.blit(t_sec2, (startX, startY))
        startY += 28

        h1 = self.font_kecik.render(dict_skrg['how_desc1'], True, WARNA_PUTIH)
        self.screen.blit(h1, (startX, startY))
        startY += 22
        h2 = self.font_kecik.render(dict_skrg['how_desc2'], True, WARNA_PUTIH)
        self.screen.blit(h2, (startX, startY))
        startY += 22
        h3 = self.font_kecik.render(dict_skrg['how_desc3'], True, WARNA_PUTIH)
        self.screen.blit(h3, (startX, startY))
        startY += 35

        t_sec3 = self.font_seksyen.render(dict_skrg['rules_title'], True, WARNA_MERAH)
        self.screen.blit(t_sec3, (startX, startY))
        startY += 28

        r1 = self.font_kecik.render(dict_skrg['rule1'], True, WARNA_PUTIH)
        self.screen.blit(r1, (startX, startY))
        startY += 22
        r2 = self.font_kecik.render(dict_skrg['rule2'], True, WARNA_PUTIH)
        self.screen.blit(r2, (startX, startY))
        startY += 22
        r3a = self.font_kecik.render(dict_skrg['rule3a'], True, WARNA_KELABU)
        self.screen.blit(r3a, (startX, startY))
        startY += 20
        r3b = self.font_kecik.render(dict_skrg['rule3b'], True, WARNA_KELABU)
        self.screen.blit(r3b, (startX, startY))

        hint_tukar = self.font_kecik.render(teks_bahasa[self.bahasa]['lang_toggle'], True, WARNA_EMAS)
        self.screen.blit(hint_tukar, (SCREEN_WIDTH // 2 - hint_tukar.get_width() // 2, 495))

        m_pos = pygame.mouse.get_pos()
        hover = self.btn_back.collidepoint(m_pos)
        warna_back = WARNA_BIRU if hover else WARNA_KOTAK
        warna_teks_back = WARNA_BG if hover else WARNA_PUTIH

        pygame.draw.rect(self.screen, warna_back, self.btn_back, border_radius=10)
        pygame.draw.rect(self.screen, WARNA_BIRU, self.btn_back, width=2, border_radius=10)

        back_surf = self.font_sedang.render(teks_bahasa[self.bahasa]['back_to_menu'], True, warna_teks_back)
        self.screen.blit(back_surf, (self.btn_back.centerx - back_surf.get_width() // 2,
                                     self.btn_back.centery - back_surf.get_height() // 2))

    def lukis_gameplay(self):
        self.screen.fill(WARNA_BG)
        masa_tick = pygame.time.get_ticks()

        # Lukis petak sungai kat tengah-tengah
        sungai_rect = pygame.Rect(320, 0, 310, SCREEN_HEIGHT)
        pygame.draw.rect(self.screen, WARNA_SUNGAI, sungai_rect)

        # Loop guna math.sin buat ombak air bergerak
        laju_air = 0.22
        for i in range(14):
            kira_y = (i * 55) + int(masa_tick * laju_air)
            y_final = kira_y % (SCREEN_HEIGHT + 60) - 30

            list_point_ombak = []
            for x_koor in range(sungai_rect.left, sungai_rect.right + 20, 15):
                ombak_sin = math.sin((masa_tick * 0.005) + (x_koor * 0.025) + (i * 1.1)) * 14
                list_point_ombak.append((x_koor, y_final + ombak_sin))

            if len(list_point_ombak) > 1:
                warna_air_line = (12, 60 + (i % 3) * 20, 120 + (i % 4) * 25)
                pygame.draw.lines(self.screen, warna_air_line, False, list_point_ombak, 2)
                if i % 2 == 0:
                    pygame.draw.lines(self.screen, WARNA_BUIH, False, list_point_ombak[1:-1], 1)

        # Sparkles dalam air sungai
        random.seed(777)
        for i in range(30):
            laju_spark = 0.2 + (i % 3) * 0.08
            spark_y = (random.randint(0, SCREEN_HEIGHT) + int(masa_tick * laju_spark)) % SCREEN_HEIGHT
            goyang_x = math.sin((masa_tick * 0.003) + (spark_y * 0.015)) * 16
            spark_x = sungai_rect.left + random.randint(20, 290) + int(goyang_x)

            if sungai_rect.left < spark_x < sungai_rect.right:
                saiz_spark = 3 if abs(math.sin(masa_tick * 0.004 + i)) > 0.6 else 2
                pygame.draw.circle(self.screen, WARNA_SPARK, (spark_x, spark_y), saiz_spark)
        random.seed()

        # Lukis daratan kiri kanan
        pygame.draw.rect(self.screen, WARNA_TEBING, (0, 0, 320, SCREEN_HEIGHT))
        pygame.draw.rect(self.screen, WARNA_TEBING, (630, 0, 320, SCREEN_HEIGHT))

        # Hiasan tepi tebing batu
        for ys in range(0, SCREEN_HEIGHT + 30, 30):
            goyang_batu = math.sin((masa_tick * 0.0012) + ys * 0.03) * 5
            pygame.draw.polygon(self.screen, WARNA_TEBING_LIGHT,
                                [(305 + goyang_batu, ys), (325 + goyang_batu, ys + 15), (310 + goyang_batu, ys + 30),
                                 (275, ys + 15)])
            pygame.draw.polygon(self.screen, WARNA_TEBING_LIGHT,
                                [(645 - goyang_batu, ys), (625 - goyang_batu, ys + 15), (640 - goyang_batu, ys + 30),
                                 (675, ys + 15)])

        pygame.draw.rect(self.screen, WARNA_RUMPUT, (0, 0, 270, SCREEN_HEIGHT), width=18)
        pygame.draw.rect(self.screen, WARNA_RUMPUT, (680, 0, 270, SCREEN_HEIGHT), width=18)
        pygame.draw.rect(self.screen, WARNA_BG, (318, 0, 4, SCREEN_HEIGHT))
        pygame.draw.rect(self.screen, WARNA_BG, (628, 0, 4, SCREEN_HEIGHT))

        # Lukis bot rakit dan karakter
        ninja_ready = any(p.identity == 'NINJA' for p in self.raft.passengers)
        y_bot_skrg = self.raft.lukis_rakit(self.screen, masa_tick, ninja_ready)

        for entity in self.entities:
            self.screen.blit(entity.image, entity.rect)
            if entity.is_in_raft:
                pygame.draw.circle(self.screen, WARNA_HIJAU, (entity.rect.centerx, entity.rect.bottom + 5), 4)
            lbl = self.font_kecik.render(entity.dapatkan_nama(self.bahasa), True, WARNA_PUTIH)
            self.screen.blit(lbl, (entity.rect.centerx - lbl.get_width() // 2, entity.rect.y - 25))

        # UI Top Bar (Level, Score, Time)
        pygame.draw.rect(self.screen, WARNA_KOTAK, (0, 0, SCREEN_WIDTH, 65))
        pygame.draw.line(self.screen, WARNA_BIRU, (0, 65), (SCREEN_WIDTH, 65), 2)

        lvl_s = self.font_sedang.render(f"{teks_bahasa[self.bahasa]['level']}: {self.level}", True, WARNA_PUTIH)
        scr_s = self.font_sedang.render(f"{teks_bahasa[self.bahasa]['score']}: {self.score}", True, WARNA_EMAS)
        warna_masa = WARNA_MERAH if self.masa_tinggal < 15 else WARNA_HIJAU
        tim_s = self.font_sedang.render(f"{teks_bahasa[self.bahasa]['time']}: {int(self.masa_tinggal)}s", True,
                                        warna_masa)

        self.screen.blit(lvl_s, (40, 18))
        self.screen.blit(scr_s, (220, 18))
        self.screen.blit(tim_s, (SCREEN_WIDTH - 200, 18))

        # UI Bottom Bar (Bantuan Butang)
        pygame.draw.rect(self.screen, WARNA_KOTAK, (0, SCREEN_HEIGHT - 75, SCREEN_WIDTH, 75))
        pygame.draw.line(self.screen, WARNA_BIRU, (0, SCREEN_HEIGHT - 75), (SCREEN_WIDTH, SCREEN_HEIGHT - 75), 2)

        str_tindakan = f"{teks_bahasa[self.bahasa]['space_action']}    |    {teks_bahasa[self.bahasa]['reset_action']}    |    {teks_bahasa[self.bahasa]['menu_action']}    |    {teks_bahasa[self.bahasa]['lang_action']}"
        act_s = self.font_kecik.render(str_tindakan, True, WARNA_KELABU)
        self.screen.blit(act_s, (40, SCREEN_HEIGHT - 62))

        if self.mesej_status:
            msg_s = self.font_kecik.render(self.mesej_status, True, WARNA_EMAS)
            self.screen.blit(msg_s, (40, SCREEN_HEIGHT - 34))

        return y_bot_skrg

    def lukis_skrin_overlay(self):
        fail_screen = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        fail_screen.fill((8, 10, 16, 240))
        self.screen.blit(fail_screen, (0, 0))

        if self.state == 'LEVEL_CLEARED':
            banner = teks_bahasa[self.bahasa]['win_banner']
            warna_banner = WARNA_HIJAU
        elif self.state == 'VICTORY':
            banner = teks_bahasa[self.bahasa]['victory_banner']
            warna_banner = WARNA_EMAS
        else:
            banner = teks_bahasa[self.bahasa]['game_over_banner']
            warna_banner = WARNA_MERAH

        t_surf = self.font_besar.render(banner, True, warna_banner)
        self.screen.blit(t_surf, (SCREEN_WIDTH // 2 - t_surf.get_width() // 2, SCREEN_HEIGHT // 2 - 100))

        if self.mesej_status:
            msg_s = self.font_sedang.render(self.mesej_status, True, WARNA_PUTIH)
            self.screen.blit(msg_s, (SCREEN_WIDTH // 2 - msg_s.get_width() // 2, SCREEN_HEIGHT // 2 - 20))

        c_surf = self.font_kecik.render(teks_bahasa[self.bahasa]['any_key'], True, WARNA_KELABU)
        self.screen.blit(c_surf, (SCREEN_WIDTH // 2 - c_surf.get_width() // 2, SCREEN_HEIGHT // 2 + 60))

    def run(self):
        while True:
            kadar_masa = self.clock.tick(FPS) / 1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.state in ['MENU', 'INSTRUCTIONS', 'PLAYING']:
                        self.klik_tetikus(event.pos)
                    elif self.state in ['LEVEL_CLEARED', 'GAME_OVER', 'VICTORY']:
                        if self.state == 'LEVEL_CLEARED':
                            self.level += 1
                            self.state = 'PLAYING'
                            self.init_level_baru()
                            self.tukar_lagu_bg()
                        else:
                            self.state = 'MENU'
                            self.level = 1
                            self.score = 0
                            self.init_level_baru()
                            self.tukar_lagu_bg()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_l:
                        self.bahasa = 'MY' if self.bahasa == 'EN' else 'EN'
                        if self.state == 'PLAYING':
                            self.mesej_status = teks_bahasa[self.bahasa]['lang_action']

                    elif event.key == pygame.K_m:
                        self.state = 'MENU'
                        self.level = 1
                        self.score = 0
                        self.init_level_baru()
                        self.tukar_lagu_bg()

                    elif self.state == 'MENU':
                        if event.key in [pygame.K_1, pygame.K_KP1]:
                            self.state = 'PLAYING'
                            self.mesej_status = ""
                            self.tukar_lagu_bg()
                        elif event.key in [pygame.K_2, pygame.K_KP2]:
                            self.state = 'INSTRUCTIONS'
                            self.tukar_lagu_bg()
                        elif event.key in [pygame.K_3, pygame.K_KP3]:
                            pygame.quit()
                            sys.exit()

                    elif self.state == 'INSTRUCTIONS':
                        if event.key != pygame.K_l:
                            self.state = 'MENU'
                            self.tukar_lagu_bg()

                    elif self.state == 'PLAYING':
                        if event.key == pygame.K_SPACE:
                            berjaya, ralat = self.raft.gerak_seberang(self.bahasa)
                            if not berjaya:
                                self.mesej_status = ralat
                            else:
                                self.mesej_status = ""
                                self.semak_peraturan_game()
                        elif event.key == pygame.K_r:
                            self.score = max(0, self.score - 100)  # Tolak markah denda kalau reset
                            self.init_level_baru()

                    elif self.state in ['LEVEL_CLEARED', 'GAME_OVER', 'VICTORY']:
                        if self.state == 'LEVEL_CLEARED':
                            self.level += 1
                            self.state = 'PLAYING'
                            self.init_level_baru()
                            self.tukar_lagu_bg()
                        else:
                            self.state = 'MENU'
                            self.level = 1
                            self.score = 0
                            self.init_level_baru()
                            self.tukar_lagu_bg()

            # Tolak masa timer kalau tengah main
            if self.state == 'PLAYING':
                self.masa_tinggal -= kadar_masa
                if self.masa_tinggal <= 0:
                    self.masa_tinggal = 0
                    self.state = 'GAME_OVER'
                    self.mesej_status = "TIME EXPIRED: Enemy guards spotted your location!"
                    self.tukar_lagu_bg()

            # Update pergerakan koordinat entiti/karakter
            if self.state in ['PLAYING', 'LEVEL_CLEARED', 'GAME_OVER', 'VICTORY']:
                x_target_rakit = RAKIT_KANAN_X if self.raft.side == 'RIGHT' else RAKIT_KIRI_X
                self.raft.x += (x_target_rakit - self.raft.x) * 0.15

                y_rakit_skrg = self.raft.y + int(math.sin(pygame.time.get_ticks() * 0.005) * 4)

                kiri_count, kanan_count = 0, 0
                for entity in self.entities:
                    if entity.is_in_raft:
                        kedudukan = self.raft.passengers.index(entity)
                        entity.update_posisi(int(self.raft.x) + (kedudukan * 48) + 32, y_rakit_skrg + 38)
                    else:
                        if entity.side == 'LEFT':
                            entity.update_posisi(TEBING_KIRI_X, 160 + (kiri_count * 78))
                            kiri_count += 1
                        else:
                            entity.update_posisi(TEBING_KANAN_X, 160 + (kanan_count * 78))
                            kanan_count += 1

            # Render skrin ikut status state sekarang
            if self.state == 'MENU':
                self.lukis_menu_utama()
            elif self.state == 'INSTRUCTIONS':
                self.lukis_skrin_arahan()
            else:
                self.lukis_gameplay()
                if self.state in ['LEVEL_CLEARED', 'GAME_OVER', 'VICTORY']:
                    self.lukis_skrin_overlay()

            pygame.display.flip()


if __name__ == "__main__":
    game = GameManager()
    game.run()