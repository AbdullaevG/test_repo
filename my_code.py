def dist(point_1, point_2):
    """
    This function calculate the euclidean
    distance from point_1 to point_2 in 2D space
    """
    (x1, y1), (x2, y2) = point_1, point_2
    return ((x1-x2)**2 + (y1-y2)**2)**0.5


def main():
    print(f"{dist((0, 0), (1, 1)):.3f}")


if __name__=="__main__":
    main()
