# find the height of binary tree
# input example: (5, (3, (20, None, None), (21, None, None)), (10, (1, None, None), None))
class Tree:
    x: int = 0
    l: "Tree" = None  # noqa: E741
    r: "Tree" = None


def solutions(T):
    if T.l is None and T.r is None:
        return 0
    elif T.l is None:
        return 1 + solutions(T.r)
    elif T.r is None:
        return 1 + solutions(T.l)
    else:
        return 1 + max(solutions(T.r), solutions(T.l))


def test_solution():
    root = Tree()
    root.x = 1

    left = Tree()
    left.x = 2

    right = Tree()
    right.x = 3

    right_left = Tree()
    right_left.x = 4

    right_right = Tree()
    right_right.x = 5

    # 建構二元樹
    root.r = right
    root.l = left

    right.r = right_right
    right.l = right_left

    expected_depth = 2
    calculated_depth = solutions(root)

    print(f"預期深度: {expected_depth}, 計算得出的深度: {calculated_depth}")


test_solution()
