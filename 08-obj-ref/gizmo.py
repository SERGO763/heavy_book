class Gizmo:
    def __init__(self):
        print('Gizmo id: %d' % id(self))

x = Gizmo()
print(x)
y = Gizmo() * 10
print(y)
