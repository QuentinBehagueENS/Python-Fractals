import pygame
pygame.init()


#________________________________________________________________________/ Variables Globales :

ITERATION = 80
abcisseMIN, abcisseMAX, ordonneeMIN, ordonneeMAX = -1.75, 1.75, -1.75, 1.75 
LARGEUR, HAUTEUR = 400,400

#________________________________________________________________________/ Création de la fenêtre :


fenetre = pygame.display.set_mode((LARGEUR,HAUTEUR))
pygame.display.set_caption("Ensemble de Julia")

#________________________________________________________________________/ Coloration pixel par pixel :

# On produit un ensemble de Julia en classant les points par divergence/convergence de la suite x^2+c

for y in range(HAUTEUR):
    pygame.display.flip()
    for x in range(LARGEUR):
        xn = (x * (abcisseMAX - abcisseMIN) / LARGEUR + abcisseMIN)
        yn = (y * (ordonneeMIN - ordonneeMAX) / HAUTEUR + ordonneeMAX)
        '''Réglage de la suite (Zn) où Zn = (Zn-1)**2 + c'''
        cx = 0.3  # Re(c)
        cy = 0.5  # Im(c)
        n = 0

        while (xn * xn + yn * yn) < 4 and n < ITERATION:
            xn, yn = xn*xn - yn*yn +cx , 2*xn*yn+cy
            n += 1
        if n == ITERATION:
            fenetre.set_at((x, y), (0,0,0))
        else:
            fenetre.set_at((x, y),((5* n+10) % 256, (20 * n) % 256, (2 * n+90) % 256))
            
#________________________________________________________________________/ Boucle de fermeture :
            
pygame.display.flip()
ouvert= True
while ouvert:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      ouvert = False
pygame.quit()


#________________________________________________________________________/ Quelques graines intéressantes:

#(0.285; 0.013 )
#(-0.8; 0.156)
# (0.3; 0.5)
# (-0.4;0.6)
# (0.32 ; 0.56)
