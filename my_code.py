def dist(point_1, point_2, manhattan):
    """
    This function calculate the euclidean or manhattan
    distance from point_1 to point_2 in 2D space
    """
    (x1, y1), (x2, y2) = point_1, point_2

    if manhattan:
        return abs(x1-x2) + abs(y1-y2)

    return ((x1-x2)**2 + (y1-y2)**2)**0.5


def main():
    print(f"{dist((0, 0), (1, 1), manhattan=True):.3f}")


if __name__=="__main__":
    main()
