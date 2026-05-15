import customtkinter as ctk
import os
from PIL import Image

pasta_do_script = os.path.dirname(os.path.abspath(__file__))
pasta_das_fontes = os.path.join(pasta_do_script, "fontes")
pasta_imagens = os.path.join(pasta_do_script, "imagens")

caminho_fnt_hollow = os.path.join(pasta_das_fontes, "Pokemon Hollow.ttf")
caminho_fnt_solid = os.path.join(pasta_das_fontes, "Pokemon Solid.ttf")
caminho_fnt_emeraldpro = os.path.join(pasta_das_fontes, "pokemon-emerald-pro.otf")
caminho_img_fundo = os.path.join(pasta_imagens, "paterndarkmod.png")

def calcular():
    try:
        vitalidade = int(hpe.get())
        ataque_fisico = int(atke.get())
        defesa_fisica = int(dfse.get())
        ataque_especial = int(spae.get())
        defesa_especial = int(spee.get())
        velocidade = int(spde.get())

        IVs = [vitalidade, ataque_fisico, defesa_fisica, defesa_especial, ataque_especial, velocidade]

        if any(valor < 0 or valor > 31 for valor in IVs):
            for valor in IVs:
                if valor > 31:
                    log_text.configure(text="Erro: Apenas números até 31", font=font_log_text, text_color="#870000")
                elif valor < 0:
                    log_text.configure(text="Erro: Apenas números maiores que 0", font=font_log_text, text_color="#870000")
        else:
            somatorio = sum(IVs)
            porcentagem = (somatorio/186)*100

            hp.configure(text=f"    HP: {vitalidade}    ")
            atk.configure(text=f"   ATK: {ataque_fisico}   ")
            dfe.configure(text=f"   DEF: {defesa_fisica}   ")
            sp_atk.configure(text=f"SP.ATK: {ataque_especial}")
            sp_def.configure(text=f"SP.DEF: {defesa_especial}")
            speed.configure(text=f"SPEED: {velocidade}")

            if somatorio >= 0 and somatorio <= 90 and porcentagem >= 0 and porcentagem <=48.8:
                if somatorio >= 0 and somatorio <= 6:
                    log_text.configure(text=f"TOTAL IVs: {somatorio} | PORCENTAGEM IVs: {porcentagem:.1f}% | AVALIAÇÃO: RUIM", font=font_labels, text_color="#E76F51")
                else:
                    log_text.configure(text=f"TOTAL IVs: {somatorio} | PORCENTAGEM IVs: {porcentagem:.1f}% | AVALIAÇÃO: OK", font=font_labels, text_color="#F4A261")

            elif somatorio >= 91 and somatorio <= 120 and porcentagem >= 48.9 and porcentagem <=65:
                log_text.configure(text=f"TOTAL IVs: {somatorio} | PORCENTAGEM IVs: {porcentagem:.1f}% | AVALIAÇÃO: BOM", font=font_labels, text_color="#FFD166")

            elif somatorio >= 121 and somatorio <= 150 and porcentagem >= 65.1 and porcentagem <= 81.1:
                log_text.configure(text=f"TOTAL IVs: {somatorio} | PORCENTAGEM IVs: {porcentagem:.1f}% | AVALIAÇÃO: MUITO BOM", font=font_labels, text_color="#427e3a")

            elif somatorio >= 151 and somatorio <= 186 and porcentagem >= 81.2 and porcentagem <=100:
                if all(valores == 31 for valores in IVs):

                    log_text.configure(text=f"TOTAL IVs: {somatorio} | PORCENTAGEM IVs: {porcentagem:.1f}% | AVALIAÇÃO: 6 IVS PERFEITOS", font=font_labels, text_color="#00B4D8")
                else:
                    log_text.configure(text=f"TOTAL IVs: {somatorio} | PORCENTAGEM IVs: {porcentagem:.1f}% | AVALIAÇÃO: EXCELENTE", font=font_labels, text_color="#57CC99")
    except ValueError:
        log_text.configure(text="Erro: insira apenas números", font=font_log_text, text_color="#870000")

#* CRIAÇÃO DA JANELA
janela = ctk.CTk()
janela.geometry("1080x900")
janela.title("Calculo IVS")
janela.configure(fg_color="#2B2D42")
# janela.overrideredirect(True)
# janela.iconbitmap()

ctk.FontManager.load_font(caminho_fnt_hollow)
ctk.FontManager.load_font(caminho_fnt_solid)
ctk.FontManager.load_font(caminho_fnt_emeraldpro)
imagem_pil = Image.open(caminho_img_fundo)
imagem_pil = imagem_pil.resize((1080, 900))
imagem_fundo = ctk.CTkImage(light_image=imagem_pil,dark_image=imagem_pil, size=(1080, 900))

label_fundo = ctk.CTkLabel(janela, image=imagem_fundo, text="")
label_fundo.place(x=0, y=0, relwidth=1, relheight=1)

font_title1 = ctk.CTkFont(family="Pokemon Hollow", size=40)
font_title2 = ctk.CTkFont(family="Pokemon Solid", size=40)
font_labels = ctk.CTkFont(family="Pokémon Emerald Pro", size=22)
font_log_text = ctk.CTkFont(family="Pokémon Emerald Pro", size=36)
font_botao = ctk.CTkFont(family="Pokémon Emerald Pro", size=30, weight="bold")

#! FRAME DO TÍTULO
frame_pack_titulo1 = ctk.CTkFrame(janela, fg_color="#2B2D42")
frame_pack_titulo1.pack(padx=10, pady=(25,10))
titulo1 = ctk.CTkLabel(frame_pack_titulo1, text="Calcular IVs", font=font_title1, fg_color="#2B2D42")
titulo1.pack(pady=10, padx=5)

#! FRAME DO PRIMEIRO CONTAINER
frame_pack_container = ctk.CTkFrame(janela, fg_color="#8D99AE")
frame_pack_container.pack(ipadx=20, ipady=20)
frame_pack_subcontainer = ctk.CTkFrame(frame_pack_container, fg_color="#13304a", corner_radius=10, border_color="#000", border_width=2)
frame_pack_subcontainer.pack(pady=(20, 10))

#! FRAME DA ESQUERDA
frame_grid_esquerda = ctk.CTkFrame(frame_pack_subcontainer, fg_color="#003566", corner_radius=10, border_color="#000", border_width=2)
frame_grid_esquerda.pack(side="left", padx=(20, 5), pady=20)

#? ENTRADA DOS 3 PRIMEIROS ATRIBUTOS
ctk.CTkLabel(frame_grid_esquerda, text="HP", font=font_labels, text_color="#EDF2F4").grid(row=0, column=0, padx=10, pady=10)
hpe = ctk.CTkEntry(frame_grid_esquerda, font=font_labels, fg_color="transparent", border_color="#EDF2F4")
hpe.grid(row=0, column=1, padx=10, pady=10)

ctk.CTkLabel(frame_grid_esquerda, text="ATK", font=font_labels, text_color="#EDF2F4").grid(row=1, column=0, padx=10, pady=10)
atke = ctk.CTkEntry(frame_grid_esquerda, font=font_labels, fg_color="transparent", border_color="#EDF2F4")
atke.grid(row=1, column=1, padx=10, pady=10)

ctk.CTkLabel(frame_grid_esquerda, text="DEF", font=font_labels, text_color="#EDF2F4").grid(row=2, column=0, padx=10, pady=10)
dfse = ctk.CTkEntry(frame_grid_esquerda, font=font_labels, fg_color="transparent", border_color="#EDF2F4")
dfse.grid(row=2, column=1, padx=10, pady=10)

#! FRAME DA DIREITA
frame_grid_direita = ctk.CTkFrame(frame_pack_subcontainer, fg_color="#003566", corner_radius=10, border_color="#000", border_width=2)
frame_grid_direita.pack(side="left", padx=(5, 20), pady=20)

#? ENTRADA DOS 3 ÚLTIMOS ATRIBUTOS
ctk.CTkLabel(frame_grid_direita, text="SP.ATK", font=font_labels, text_color="#EDF2F4").grid(row=0, column=0, padx=10, pady=10)
spae = ctk.CTkEntry(frame_grid_direita, font=font_labels, fg_color="transparent", border_color="#EDF2F4")
spae.grid(row=0, column=1, padx=10, pady=10)

ctk.CTkLabel(frame_grid_direita, text="SP.DEF", font=font_labels, text_color="#EDF2F4").grid(row=1, column=0, padx=10, pady=10)
spee = ctk.CTkEntry(frame_grid_direita, font=font_labels, fg_color="transparent", border_color="#EDF2F4")
spee.grid(row=1, column=1, padx=10, pady=10)

ctk.CTkLabel(frame_grid_direita, text="SPEED", font=font_labels, text_color="#EDF2F4").grid(row=2, column=0, padx=10, pady=10)
spde = ctk.CTkEntry(frame_grid_direita, font=font_labels, fg_color="transparent", border_color="#EDF2F4")
spde.grid(row=2, column=1, padx=10, pady=10)

#! FRAME DO BOTÃO QUE CHAMA A FUNÇÃO
botao = ctk.CTkButton(frame_pack_container,
text="CALCULAR", 
command=calcular,
width=150,
height=40,
font=font_botao,
anchor="center",
corner_radius=10,
fg_color="#E63946",
hover_color="#457B9D"
)
botao.pack(pady=(10, 20))

#! FRAME DO TÍTULO DOS RESULTADOS
frame_pack_titulo2 = ctk.CTkFrame(janela, fg_color="#2B2D42")
titulo2 = ctk.CTkLabel(frame_pack_titulo2, text="Resultados IVs", font=font_title2, fg_color="#2B2D42")
titulo2.pack(pady=10, padx=5)
frame_pack_titulo2.pack(pady=(25, 10))

#! FRAME DO SEGUNDO CONTAINER
frame_pack_container2 = ctk.CTkFrame(janela)
frame_pack_container2.pack(ipadx=20, ipady=20)
frame_pack_subcontainer2 = ctk.CTkFrame(frame_pack_container2)
frame_pack_subcontainer2.pack(pady=20)

frame_label_esquerda = ctk.CTkFrame(frame_pack_subcontainer2)
frame_label_esquerda.pack(side="left", padx=(20, 5), pady=20)

hp = ctk.CTkLabel(frame_label_esquerda, text="HP:", font=font_labels)
hp.grid(row=0, column=0, padx=10, pady=10)

atk = ctk.CTkLabel(frame_label_esquerda, text="ATK:", font=font_labels)
atk.grid(row=1, column=0, padx=10, pady=10)

dfe = ctk.CTkLabel(frame_label_esquerda, text="DEF:", font=font_labels)
dfe.grid(row=2, column=0, padx=10, pady=10)

frame_label_direita = ctk.CTkFrame(frame_pack_subcontainer2)
frame_label_direita.pack(side="left", padx=(5, 20) , pady=20)

sp_atk = ctk.CTkLabel(frame_label_direita, text="SP.ATK:", font=font_labels)
sp_atk.grid(row=0, column=0, padx=10, pady=10)

sp_def = ctk.CTkLabel(frame_label_direita, text="SP.DEF:", font=font_labels)
sp_def.grid(row=1, column=0, padx=10, pady=10)

speed = ctk.CTkLabel(frame_label_direita, text="SPEED:", font=font_labels)
speed.grid(row=2, column=0, padx=10, pady=10)

log = ctk.CTkFrame(frame_pack_container2)
log.pack(fill="x", padx=20)
log_text = ctk.CTkLabel(log, text="...")
log_text.pack(padx=10, pady=10)

janela.mainloop()