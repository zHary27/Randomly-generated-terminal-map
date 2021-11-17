import os
import keyboard
import time
import random

chão = ' '
pedra = '#'
boneco = 'O'
chegadasimbolo = 'A'
spawnposparacriarmapa = 'B'
    
def checarlados(mapa, pos, jaforam):
    ladospossiveis = []

    try:
        if mapa[pos[0]][pos[1]+1] != pedra and (pos[0], pos[1]+1) not in jaforam:
            ladospossiveis.append((pos[0], pos[1]+1))
    except:
        pass
    
    try:
        if mapa[pos[0]][pos[1]-1] != pedra and pos[1]-1 >= 0 and (pos[0], pos[1]-1) not in jaforam:
            ladospossiveis.append((pos[0], pos[1]-1))
    except:
        pass
    
    try:
        if mapa[pos[0]+1][pos[1]] != pedra and (pos[0]+1, pos[1]) not in jaforam:
            ladospossiveis.append((pos[0]+1, pos[1]))
    except:
        pass
    
    try:
        if mapa[pos[0]-1][pos[1]] != pedra and pos[0]-1 >= 0 and (pos[0]-1, pos[1]) not in jaforam:
            ladospossiveis.append((pos[0]-1, pos[1]))
    except:
        pass
    
    return ladospossiveis

def criarmapabfs(altura, largura, porcentagem):
    
    global chão
    global pedra
    global boneco
    global chegadasimbolo
    global spawnposparacriarmapa
    
    porcento = []
    
    for i in range(0, porcentagem): porcento.append(i)
    
    mapa = []
    parachecar = []
    jaforam = [(0, 0)]

    spawnpos = (random.randint(0, altura-1), random.randint(0, largura-1))
    
    while spawnpos == (0, 0):
        spawnpos = (random.randint(0, altura-1), random.randint(0, largura-1))
    
    for i in range(0, altura):
        mapa.append([])
    
    for linha in mapa:
        for i in range(0, largura):
            linha.append(chão)
            
    for linha in mapa:
        for i in range(0, largura):
            if random.randint(0,100) in porcento and (mapa.index(linha), i) != spawnpos:
                linha[i] = pedra
  
    chegada = random.choice([(0, 0), (0, largura-1), (altura-1, 0), (altura-1, largura-1)])
    mapa[spawnpos[0]][spawnpos[1]] = spawnposparacriarmapa
    mapa[chegada[0]][chegada[1]] = chegadasimbolo
    apos = chegada
    
    while True:
        
        os.system('cls')
        for i in mapa: print(i)
        print('Generating map...')
        
        for linha in mapa:
            for i in linha:
                if i == chegadasimbolo:
                    apos = mapa.index(linha), linha.index(i)
        
        for i in checarlados(mapa, apos, jaforam):
            if i not in parachecar:
                parachecar.append(i)
    
        if parachecar == []:
            os.system('cls')
            
            if spawnpos not in jaforam:
                for i in mapa: print(i)
                print('Impossible')
                return 'no'
            else:
                mapa[chegada[0]][chegada[1]] = chegadasimbolo
                break
            
        if apos == spawnpos or spawnpos in jaforam:
            os.system('cls')
        
            mapa[chegada[0]][chegada[1]] = chegadasimbolo
            for i in mapa: print(i)
            print('Found')
            break
        
        else:
            if mapa[parachecar[0][0]][parachecar[0][1]] == pedra:
                if (parachecar[0][0], parachecar[0][1]) not in jaforam:
                    jaforam.append((parachecar[0][0], parachecar[0][1]))
                parachecar.pop(0)
            else:
                if (parachecar[0][0], parachecar[0][1]) not in jaforam:
                    jaforam.append((parachecar[0][0], parachecar[0][1]))
                    mapa[apos[0]][apos[1]] = chão
                    mapa[parachecar[0][0]][parachecar[0][1]] = chegadasimbolo
                parachecar.pop(0)

    return mapa, spawnpos

def criarmapadfs(altura, largura, porcentagem):
    
    global chão
    global pedra
    global boneco
    global chegadasimbolo
    global spawnposparacriarmapa
    
    porcento = []
    
    for i in range(0, porcentagem): porcento.append(i)
    
    mapa = []
    parachecar = []
    jaforam = [(0, 0)]

    chegada = random.choice([(0, 0), (0, largura-1), (altura-1, 0), (altura-1, largura-1)])
    spawnpos = (random.randint(0, altura-1), random.randint(0, largura-1))
    
    while spawnpos == chegada:
        spawnpos = (random.randint(0, altura-1), random.randint(0, largura-1))
    
    for i in range(0, altura):
        mapa.append([])
    
    for linha in mapa:
        for i in range(0, largura):
            linha.append(chão)
            
    for linha in mapa:
        for i in range(0, largura):
            if random.randint(0,100) in porcento and (mapa.index(linha), i) != spawnpos:
                linha[i] = pedra
  
    mapa[spawnpos[0]][spawnpos[1]] = spawnposparacriarmapa
    mapa[chegada[0]][chegada[1]] = chegadasimbolo
    apos = chegada
    
    while True:
        
        os.system('cls')
        for i in mapa: print(i)
        print('Generating map...')
        
        for linha in mapa:
            for i in linha:
                if i == chegadasimbolo:
                    apos = mapa.index(linha), linha.index(i)
        
        for i in checarlados(mapa, apos, jaforam):
            if i not in parachecar:
                parachecar.append(i)
    
        if parachecar == []:
            os.system('cls')
            
            if spawnpos not in jaforam:
                for i in mapa: print(i)
                print('Impossible')
                return 'no'
            else:
                mapa[chegada[0]][chegada[1]] = chegadasimbolo
                break
            
        if apos == spawnpos or spawnpos in jaforam:
            os.system('cls')
        
            mapa[chegada[0]][chegada[1]] = chegadasimbolo
            for i in mapa: print(i)
            print('Found')
            break
        
        else:
            if mapa[parachecar[-1][0]][parachecar[-1][1]] == pedra:
                if (parachecar[-1][0], parachecar[-1][1]) not in jaforam:
                    jaforam.append((parachecar[-1][0], parachecar[-1][1]))
                parachecar.pop()
            else:
                if (parachecar[-1][0], parachecar[-1][1]) not in jaforam:
                    jaforam.append((parachecar[-1][0], parachecar[-1][1]))
                    mapa[apos[0]][apos[1]] = chão
                    mapa[parachecar[-1][0]][parachecar[-1][1]] = chegadasimbolo
                parachecar.pop()

    return mapa, spawnpos

def pegarposição(mapa):
    
    global boneco
    
    for i in mapa:
        for b in i:
            if b == boneco:
                return (mapa.index(i), i.index(b))

def iniciarjogo(altura, largura, porcentagem, bfsdfs):
    
    while True:
        if bfsdfs == 'bfs':
            criandomapa = criarmapabfs(altura, largura, porcentagem)
        
        elif bfsdfs == 'dfs':
            criandomapa = criarmapadfs(altura, largura, porcentagem)
            
        if criandomapa != 'no':

            global chão
            global pedra
            global boneco
            global chegada
            
            mapa = criandomapa[0]
            mapa[criandomapa[1][0]][criandomapa[1][1]] = boneco

            for linha in mapa:
                for i in linha:
                    if i == chegadasimbolo:
                        chegada = mapa.index(linha), linha.index(i)

            while True:
                os.system('cls')
                
                for i in mapa: print(i)
                print(f'Current position: ({pegarposição(mapa)[0]+1}, {pegarposição(mapa)[1]})')
                print(f'Objective: ({chegada[0]+1}, {chegada[1]+1})')

                bonecoestaem = (pegarposição(mapa)[0], pegarposição(mapa)[1])

                if bonecoestaem == chegada:
                    break

                time.sleep(0.2)
                andar = keyboard.read_key()

                if andar.upper() == 'D':
                    try:
                        if mapa[bonecoestaem[0]][bonecoestaem[1]+1] != pedra:
                            mapa[bonecoestaem[0]][bonecoestaem[1]+1] = boneco
                            mapa[bonecoestaem[0]][bonecoestaem[1]] = chão
                        else:
                            pass
                    except:
                        pass
                elif andar.upper() == 'A':
                    try:
                        if mapa[bonecoestaem[0]][bonecoestaem[1]-1] != pedra and bonecoestaem[1]-1 >= 0:
                            mapa[bonecoestaem[0]][bonecoestaem[1]-1] = boneco
                            mapa[bonecoestaem[0]][bonecoestaem[1]] = chão
                        else:
                            pass
                    except:
                        pass
                elif andar.upper() == 'W':
                    try:
                        if mapa[bonecoestaem[0]-1][bonecoestaem[1]] != pedra and bonecoestaem[0]-1 >= 0:
                            mapa[bonecoestaem[0]-1][bonecoestaem[1]] = boneco
                            mapa[bonecoestaem[0]][bonecoestaem[1]] = chão
                        else:
                            pass
                    except:
                        pass
                elif andar.upper() == 'S':
                    try:
                        if mapa[bonecoestaem[0]+1][bonecoestaem[1]] != pedra:
                            mapa[bonecoestaem[0]+1][bonecoestaem[1]] = boneco
                            mapa[bonecoestaem[0]][bonecoestaem[1]] = chão
                        else:
                            pass
                    except:
                        pass
        else:
            pass

while True:

    try:
        
        os.system('cls')
        
        bfsoudfs = input('BFS or DFS: ').lower()
        if bfsoudfs not in 'bfsdfs':
            print('Invalid value, try again.')
            break
        
        iniciarjogo(int(input('Height: ')), int(input('Width: ')), int(input('Rocks rate (40 recommended): ')), bfsoudfs)

    except ValueError:
        print('Invalid value detected, try again.')
