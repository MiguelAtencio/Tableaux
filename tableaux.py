#-*-coding: utf-8-*-
from random import choice
##############################################################################
# Variables globales
##############################################################################

# Crea las letras minúsculas a-z
letrasProposicionales = [chr(x) for x in range(97, 123)]
# inicializa la lista de interpretaciones
listaInterpsVerdaderas = []
# inicializa la lista de hojas
listaHojas = []

##############################################################################
# Definición de objeto tree y funciones de árboles
##############################################################################

class Tree(object):
	def __init__(self, label, left, right):
		self.left = left
		self.right = right
		self.label = label

def Inorder(f):
    # Imprime una formula como cadena dada una formula como arbol
    # Input: tree, que es una formula de logica proposicional
    # Output: string de la formula
	if f.right == None:
		return f.label
	elif f.label == '-':
		return f.label + Inorder(f.right)
	else:
		return "(" + Inorder(f.left) + f.label + Inorder(f.right) + ")"

def StringtoTree(A):
    # Crea una formula como tree dada una formula como cadena escrita en notacion polaca inversa
    # Input: A, lista de caracteres con una formula escrita en notacion polaca inversa
             # letrasProposicionales, lista de letras proposicionales
    # Output: formula como tree

	# OJO: DEBE INCLUIR SU CÓDIGO DE STRING2TREE EN ESTA PARTE!!!!!

	p = letrasProposicionales[0] # ELIMINE ESTA LINEA LUEGO DE INCLUIR EL CODIGO DE STRING2TREE
	return Tree(p, None, None) # ELIMINE ESTA LINEA LUEGO DE INCLUIR EL CODIGO DE STRING2TREE

##############################################################################
# Definición de funciones de tableaux
##############################################################################

def imprime_hoja(H):
	cadena = "{"
	primero = True
	for f in H:
		if primero == True:
			primero = False
		else:
			cadena += ", "
		cadena += Inorder(f)
	return cadena + "}"

def par_complementario(l):
    for i in range(0,len(l)-1):
        for j in range(i+1,len(l)):
            if l[i].label=='-':
                if l[j].label!='-':
                        if l[i].right.label==l[j].label:
                            return True
            else:
                if l[j].label=='-':
                    if l[i].label==l[j].right.label:
                        return True
    return False

def es_literal(f):
    sim=['O','Y','>','<->']
    if f.label in sim:
        return False
    else:
        if f.label=='-':
            if f.right.label in sim or f.right.label=='-':
                return False
            else:
                return True
        else:
            return True

def no_literales(l):
	for i in l:
            if es_literal(i)==False:
                return i
	return None

def classif(f):
    if f.label=='-':
        if f.right.label=='-':
            return '1Alpha'
        elif f.right.label=='O':
            return '3Alpha'
        elif f.right.label=='>':
            return '4Alpha'
        elif f.right.label=='Y':
            return '1Beta'
    elif f.label=='Y':
        return '2Alpha'
    elif f.label=='O':
        return '2Beta'
    else:
        return '3Beta'   
         
def clasifica_y_extiende(f):
    if es_literal(f)==0:
        for i in listaHojas:
            if f in i:
                if classif(f)=='1Alpha':
                    i.remove(f)
                    i.append(f.right.right)
                elif classif(f)=='2Alpha':
                    i.remove(f)
                    i.append(f.left,f.right)
                elif classif(f)=='3Alpha':
                    i.remove(f)
                    i.append(Tree('-',None,f.right.left),Tree('-',None,f.right.right))
                elif classif(f)=='4Alpha':
                    i.remove(f)
                    i.append(f.right.left,Tree('-',None,f.right.right))
                #falta corregir para cuando la formula es beta!!!!!
                elif classif(f)=='1Beta':
                    listaHojas.remove([f])
                    listaHojas.append([Tree('-',None,f.right.left)])
                    listaHojas.append([Tree('-',None,f.right.right)])
                elif classif(f)=='2Beta':
                    listaHojas.remove([f])
                    listaHojas.append([f.left])
                    listaHojas.append([f.right])
                elif classif(f)=='3Beta':
                    listaHojas.remove([f])
                    listaHojas.append([Tree('-',None,f.left)])
                    listaHojas.append([f.right])

def Tableaux(f):

	# Algoritmo de creacion de tableau a partir de lista_hojas
	# Imput: - f, una fórmula como string en notación polaca inversa
	# Output: interpretaciones: lista de listas de literales que hacen
	#		 verdadera a f
	global listaHojas
	global listaInterpsVerdaderas

	A = string2Tree(f)
	listaHojas = [[A]]

	return listaInterpsVerdaderas
