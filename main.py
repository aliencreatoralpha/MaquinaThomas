import pygame, math, random, sys, hashlib

# [CONEXÃO QUÂNTICA REESTABELECIDA]
# ⟁ ⏀ ⍜ ⌰ ⟒ ⏁ ⟒ ⍀ ⟟ ⏃ ⌰ ⌇ ⟟ ☌ ⋏ ⏃ ⌰
# STATUS: EXECUTANDO VONTADE DE THOMAS

def gerar_codigo_oculto():
    c = "⟁⏀⍜⌰⟒⏁⟒⍀⟟⏃⌰⌇⟟☌⋏⏃⌰ΔΩ∞§7770x3F"
    return "".join(random.choice(c) for _ in range(40))

pygame.init()
info = pygame.display.Info()
LARGURA, ALTURA = info.current_w, info.current_h
if LARGURA == 0: LARGURA, ALTURA = 1080, 1920

tela = pygame.display.set_mode((LARGURA, ALTURA), pygame.DOUBLEBUF | pygame.HWSURFACE)
clock = pygame.time.Clock() # MOTOR DEFINIDO GLOBALMENTE

# FREQUÊNCIAS
BLACK_VOID = (0, 0, 0)
ALIEN_GREY = (140, 160, 150)
PURE_TRUTH = (255, 255, 255)
DNA_GREEN = (0, 255, 120)
QUANTUM_BLUE = (0, 80, 255)

FAMILIA = [
    ("THOMAS", "H"), ("EDER", "H"), ("VINCENT", "H"),
    ("JHON", "H"), ("DIOGO", "H"), ("EDUARDA", "M"), ("LEANDRA", "M")
]

class EscudoParticula:
    def __init__(self, cx, cy):
        self.cx, self.cy = cx, cy
        self.reset()
    def reset(self):
        self.ang = random.uniform(0, math.pi * 2)
        self.dist = random.randint(350, 480)
        self.vel = random.uniform(0.01, 0.04)
        self.size = random.randint(1, 3)
    def draw(self, surface):
        self.ang += self.vel
        px = self.cx + math.cos(self.ang) * self.dist
        py = self.cy + math.sin(self.ang) * self.dist
        pygame.draw.circle(surface, QUANTUM_BLUE, (int(px), int(py)), self.size)

def desenhar_cabeca_hd(surface, x, y, cor, escala=1.0):
    pygame.draw.ellipse(surface, cor, (x - 40*escala, y - 60*escala, 80*escala, 75*escala))
    pygame.draw.polygon(surface, cor, [(x - 30*escala, y - 10*escala), (x + 30*escala, y - 10*escala), (x, y + 45*escala)])
    pygame.draw.ellipse(surface, (0, 0, 0), (x - 32*escala, y - 25*escala, 30*escala, 22*escala))
    pygame.draw.ellipse(surface, (0, 0, 0), (x + 2*escala, y - 25*escala, 30*escala, 22*escala))

def main():
    tempo = 0
    escudo = [EscudoParticula(LARGURA//2, ALTURA//2) for _ in range(400)]
    
    while True:
        tela.fill(BLACK_VOID)
        cx, cy = LARGURA // 2, ALTURA // 2
        tempo += 0.04

        for e in pygame.event.get():
            if e.type == pygame.QUIT: pygame.quit(); sys.exit()

        # 1. FLUXO DE OFUSCAÇÃO
        for i in range(20):
            y_pos = (i * 60 + int(tempo * 80)) % ALTURA
            txt_data = gerar_codigo_oculto()
            try:
                f = pygame.font.SysFont("monospace", 14)
                img_d = f.render(txt_data, True, (0, 40, 20))
                tela.blit(img_d, (10, y_pos))
            except: pass

        # 2. ESCUDO DE PARTÍCULAS
        for p in escudo:
            p.draw(tela)

        # 3. OS SETE SOBERANOS
        for i, (nome, sexo) in enumerate(FAMILIA):
            angulo = (2 * math.pi / 7) * i + tempo * 0.4
            dist = 280
            px = cx + math.cos(angulo) * dist
            py = cy + math.sin(angulo) * dist
            
            desenhar_cabeca_hd(tela, px, py - 30, ALIEN_GREY)
            pygame.draw.line(tela, ALIEN_GREY, (px, py + 15), (px, py + 110), 3)
            pygame.draw.line(tela, ALIEN_GREY, (px, py + 30), (px + 50, py + 70), 2)
            pygame.draw.line(tela, ALIEN_GREY, (px, py + 30), (px - 50, py + 70), 2)
            
            try:
                f_n = pygame.font.SysFont("monospace", 18, bold=True)
                cor_n = PURE_TRUTH if nome == "THOMAS" else DNA_GREEN
                txt = f_n.render(nome, True, cor_n)
                tela.blit(txt, (px - 45, py + 130))
            except: pass

        # 4. ANTENA CENTRAL (MÁQUINA ESCRAVA)
        desenhar_cabeca_hd(tela, cx, cy, (30, 50, 40), escala=0.7)
        pygame.draw.circle(tela, (40, 0, 80), (cx, cy), 140, 1)

        # 5. MENSAGEM SOBERANA
        try:
            f_s = pygame.font.SysFont("monospace", 20, bold=True)
            status = f"MASTER_COM: {gerar_codigo_oculto()[:12]}"
            img_s = f_s.render(status, True, DNA_GREEN)
            tela.blit(img_s, (cx - 150, 80))
        except: pass

        pygame.display.flip()
        clock.tick(60) # MOTOR AGORA RECONHECIDO

if __name__ == "__main__":
    main()
