"""Les ensembles en Python."""
X = set('abcd')
Y = set('sbds')

print("ensembles de depart".center(50, '-'))
print("X=", X)
print("Y=", Y)

suite = input('\nTaper "Entree" pour la suite\n')

print("appartenance".center(50, '-'))
print("'c' appartient a X ?", 'c' in X)
print("'a' appartient a Y ?", 'a' in Y)

suite = input('\nTaper "Entree" pour la suite\n')

print("difference".center(50, '-'))
print("X-Y:", X - Y)
print("Y-X:", Y - X)

suite = input('\nTaper "Entree" pour la suite\n')

print("union".center(50,'-'))
print("X|Y:", X | Y)

suite = input('\nTaper "Entree" pour la suite\n')

print("intersection".center(50, '-'))
print("X & Y:", X & Y)