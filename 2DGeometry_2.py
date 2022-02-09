#Finding intersection points between two lines L1 and L2

def PointIntersect(L1, L2):
    delX = (L1[0][0] - L1[1][0], L2[0][0] - L2[1][0])
    delY = (L1[0][1] - L1[1][1], L2[0][1] - L2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(delX, delY)
    if div == 0:
        raise Exception('lines do not intersect')

    d = (det(*L1), det(*L2))
    x = det(d, delX) / div
    y = det(d, delY) / div
    return x, y

# Test code
if __name__ == '__main__':
    P=(2,4); Q=(6,9); R=(-4,2); S=(9,-3)
    print(PointIntersect((P, Q), (R, S)))

