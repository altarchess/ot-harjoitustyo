import pygame, defs, math, random

class Sudoku:
    def __init__(self, x, y):
        self.ruudukko = defs.TYHJA_RUUDUKKO
        self.ratkaisu = defs.TYHJA_RUUDUKKO
        self.cursor_x = x
        self.cursor_y = y
        self.cursor_active = False


    #piiretaan sudoku
    def draw(self, screen):
        #piirra 9x9 ruudukko
        self.drawMesh(screen, defs.X_ALKU, defs.Y_ALKU, defs.RUUTUJA_SIVUTTAIN, 50, 2, defs.HARMAA)
        #piira voimakkaampi 3x3
        self.drawMesh(screen, defs.X_ALKU, defs.Y_ALKU, 3, 150, 4, defs.HARMAA)
        #tarkista onko aktivoitua ruutua
        if self.cursor_active:
            #piira aktivoitu ruutu jos ruutu on aktivoitu
            self.drawMesh(screen, defs.X_ALKU+self.cursor_x*defs.RUUTU_KOKO, defs.Y_ALKU+self.cursor_y*defs.RUUTU_KOKO, 1, defs.RUUTU_KOKO, 4, defs.MUSTA)
        #Piirra voiko ratkaista
        self.drawSolvable(screen)
        #Piirra tyhjien ruutujen maara
        self.drawEmpty(screen)
        #Piira numerot
        self.drawNumbers(screen, defs.X_ALKU, defs.Y_ALKU, defs.RUUTUJA_SIVUTTAIN, 50, 4, defs.HARMAA)


    #piirra numerot
    def drawNumbers(self, screen, x, y, size, cell_width, line_width, color):
        for iX in range(size):
            for iY in range(size):
                if self.ruudukko[iX][iY] != 0:
                    #luodaan teksti
                    text = defs.SUDOKU_FONT.render(str(self.ruudukko[iX][iY]), True, color) 
                    #piirretaan teksti
                    screen.blit(text,(x+iX*cell_width+15, y+iY*cell_width+10))  


    #piirra ruudukko annetulla koolla ja viivan paksuudella, voidaan kayttaa mm sudokun ruudukon piirtamiseen
    def drawMesh(self, screen, x, y, size, cell_width, line_width, color):
        for i in range (size+1):
            #piirra vaakasuora viiva
            pygame.draw.line(screen, color, (x, y + i* cell_width), (x + size * cell_width, y + i * cell_width), line_width)
            #piirra pystysuora viiva
            pygame.draw.line(screen, color, (x + i * cell_width, y), (x + i * cell_width, y + size * cell_width), line_width)

    #ratkaisujen maaran piirto
    def drawSolvable(self, screen):
        #voiko ratkaista vastausteksti
        solvable = defs.SUDOKULLA_EI_RATK
        if self.findSolution():
            solvable = defs.SUDOKULLA_RATK

        #luodaan teksti
        text = defs.BUTTON_FONT.render(defs.SUDOKU_MAHDOLLINEN + solvable, True, defs.HARMAA) 
        #piirretaan teksti
        screen.blit(text, (defs.X_ALKU, defs.SUDOKU_SOULTION_Y)) 

    #Tyhjien ruutujen maaran piirto
    def drawEmpty(self, screen):
        #kuinka monta tyhjaa
        count = 0
        for x in range(defs.RUUTUJA_SIVUTTAIN):
            for y in range(defs.RUUTUJA_SIVUTTAIN):
                if self.ruudukko[x][y] == 0:
                    count += 1

        #luodaan teksti
        text = defs.BUTTON_FONT.render(defs.SUDOKULLA_TYHJIA + str(count), True, defs.HARMAA) 
        #piirretaan teksti
        screen.blit(text, (defs.X_ALKU, defs.SUDOKU_TYHJAT_Y)) 

    #aktivoidaan ruutu sudokun kordinaatin mukaan
    def activate(self, kordinaatti):
        self.cursor_active = True
        self.cursor_x = kordinaatti[0]
        self.cursor_y = kordinaatti[1]


    #deaktivoidaan ruutu
    def deactivate(self):
        self.cursor_active = False


    #asetetaan ruutun numero jos tyhja
    def insert(self, number):
        if self.cursor_active and self.ruudukko[self.cursor_x][self.cursor_y] == 0:
            self.ruudukko[self.cursor_x][self.cursor_y] = number


    #pakotetaan ruutuun numero
    def forceInsert(self, number):
        if self.cursor_active:
            self.ruudukko[self.cursor_x][self.cursor_y] = number


    #Annetaan ikkunan kordinaatit, saadan sudokuruudukon
    def getPressedSquare(self, x, y):
        #tarkistetaan onko ruudukolla, jos ei, palautetaan None
        if x < defs.X_ALKU or y < defs.Y_ALKU or x > defs.X_ALKU + defs.RUUTUJA_SIVUTTAIN * defs.RUUTU_KOKO or y > defs.Y_ALKU + defs.RUUTUJA_SIVUTTAIN * defs.RUUTU_KOKO:
            return None
        #muuten lasketaan ruutu ja palautetaan se
        return [(int)((x-defs.X_ALKU)/defs.RUUTU_KOKO), (int)((y-defs.Y_ALKU)/defs.RUUTU_KOKO)]


    #numeron laillisuus ruudussa
    def checkLegalityNumberOnSquare(self, x, y, number, ruudukko):
        #jos luku on nolla palauta aina tosi
        if number == 0: 
            return True
        #Vaakasuora laillisuus
        for i in range(defs.RUUTUJA_SIVUTTAIN):
            if i != x and ruudukko[i][y] == number:
                return False

        #Pystysuora laillisuus
        for i in range(defs.RUUTUJA_SIVUTTAIN):
            if i != y and ruudukko[x][i] == number:
                return False

        #3x3 ruudun laillisuus
        baseX = (int)(x/3)
        baseY = (int)(y/3)

        for iX in range(3):
            for iY in range(3):              
                if baseX  * 3 + iX != x or baseY * 3 + iY != y:
                    if ruudukko[baseX  * 3 + iX][baseY * 3 + iY] == number:
                        return False

        #Jos ei riko laillisuusehtoja, palauta Tosi
        return True

    #sudokun ratkaisia
    def findSolution(self):
        if not self.laillisuus():
            return False
        #kopioidaan nayton sudoku ratkaisua varten kaytettavaan
        ratkaistava = [row[:] for row in self.ruudukko]
        if self.solveNode(ratkaistava):
            return True
        return False
        
    
    def solveNode(self, ratkaistava):
        empty_x, empty_y = self.findEmptyCell(ratkaistava)
        if empty_x == -1:
            self.ratkaisu = [row[:] for row in ratkaistava]
            return True
        else:
            for i in range(defs.RUUTUJA_SIVUTTAIN):
                if self.checkLegalityNumberOnSquare(empty_x, empty_y, i+1, ratkaistava):
                    ratkaistava[empty_x][empty_y] = i+1
                    if self.solveNode(ratkaistava):
                        return True
                ratkaistava[empty_x][empty_y] = 0
        return False 
        
    
    def solveUniqueNess(self, ratkaistava, target):
        empty_x, empty_y = self.findEmptyCell(ratkaistava)
        if empty_x == -1:
            return target - 1
        else:
            for i in range(defs.RUUTUJA_SIVUTTAIN):
                if target <= 0:
                    return target
                if self.checkLegalityNumberOnSquare(empty_x, empty_y, i+1, ratkaistava):
                    ratkaistava[empty_x][empty_y] = i+1
                    target = self.solveUniqueNess(ratkaistava, target)
                ratkaistava[empty_x][empty_y] = 0
                
        return target 


    #talla funktiolla loydetaan tyhja ruutu ratkaistavasta sudokusta
    def findEmptyCell(self, ratkaistava):
        for x in range(defs.RUUTUJA_SIVUTTAIN):
            for y in range(defs.RUUTUJA_SIVUTTAIN):
                if ratkaistava[x][y] == 0:
                    return x, y
        return -1, -1

    #voidaan kayttaa sudokun printtaamiseen komentoriville
    def printRuudukko(self, ruudukko):
        for y in range(defs.RUUTUJA_SIVUTTAIN):
            rivi = "|"
            for x in range (defs.RUUTUJA_SIVUTTAIN):
                rivi += str(ruudukko[x][y])+"|"
            print(rivi)

    #tarkistetaan tamanhetkinen laillisuus
    def laillisuus(self):
        for x in range (defs.RUUTUJA_SIVUTTAIN):
            for y in range(defs.RUUTUJA_SIVUTTAIN):
                if not self.checkLegalityNumberOnSquare(x, y, self.ruudukko[x][y], self.ruudukko):
                    return False
        return True


    #Sudokun ratkaisujen maara tulee olla 1
    def uniqueSolution(self):
        #oletetamme etta on ratkaisu
        ratkaistava = [row[:] for row in self.ruudukko]
        if self.solveUniqueNess(ratkaistava, 2) <= 0:
            return False
        return True

    #Generoi sudoku. On huomattava etta sudokussa voi vain olla yksi ratkaisu
    def generate(self):
        while (True):
            self.ruudukko = [row[:] for row in defs.TYHJA_RUUDUKKO]
            #luodaan satunnaisuutta sudokuun
            for i in range(2):
                self.ruudukko[0][i] = random.randint(1, 9)
            self.ruudukko[random.randint(3,5)][random.randint(3,5)] = 9
            #loydetaan ratkaisu sudokulle, jos ei loydy yritetaan uudestaan
            if self.findSolution():
                self.ruudukko = [row[:] for row in self.ratkaisu]
                break

        for i in range(70):
            x = random.randint(0, 8)
            y = random.randint(0, 8)
            luku = self.ruudukko[x][y]
            self.ruudukko[x][y] = 0
            if not self.uniqueSolution():
                self.ruudukko[x][y] = luku
        