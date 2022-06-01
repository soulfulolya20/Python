def zero(items, left, middle, right):
    if items[0] == 2011:
        return left
    if items[0] == 2018:
        return middle
    if items[0] == 1960:
        return right


def four(items, left, middle, right):
    if items[4] == 'JSX':
        return left
    if items[4] == 'GOLO':
        return middle
    if items[4] == 'NIM':
        return right


def three(items, left, right):
    if items[3] == 'COBOL':
        return left
    if items[3] == 'P4':
        return right


def two(items, left, middle, right):
    if items[2] == 'EC':
        return left
    if items[2] == 'VUE':
        return middle
    if items[2] == 'STATA':
        return right


def one(items, left, right):
    if items[1] == 'CLEAN':
        return left
    if items[1] == 'YAML':
        return right


def main(items):
    return three(
        items,
        two(items, one(items, 0, four(items, 1, 2, 3)),
            zero(items, one(items, 4, 5),
                 four(items, 6, 7, 8), 9), 10),
        11
    )


print(main([2011, 'YAML', 'EC', 'P4', 'JSX']))
