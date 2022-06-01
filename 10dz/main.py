import re


def transpose(table):
    response = []
    for i in range(len(table[0])):
        response.append([])
        for j in range(len(table)):
            response[i].append(table[j][i])
    return response


def delete_empty_rows(table):
    return [row for row in table if row[0] is not None]


def delete_empty_columns(table):
    table = transpose(table)
    table = [row for row in table if row[0] is not None]
    return transpose(table)


def transformer(i, value):
    if i == 0:
        digit_str = value.replace('%', '')
        digit = float(digit_str) / 100
        return f'{digit:.4f}'
    if i == 2:
        p = r"\d\d\-\d\d-\d\d"
        matches = re.search(pattern=p, string=value).group()
        return matches.replace('-', '.')
    if i == 1:
        return '1' if value == "Y" else '0'


def transform(table):
    for i in range(len(table)):
        for j in range(len(table[i])):
            table[i][j] = transformer(j, table[i][j])
    return table


def main(table):
    return transform(
        delete_empty_columns(
            delete_empty_rows(table)
        )
    )

'''
tab = (
    (None, None, None, None, None),
    ("71%", None, "Y", None, "2000-10-13"),
    ("47%", None, "Y", None, "2001-09-05"),
    ("74%", None, "N", None, "2004-01-14"),
    (None, None, None, None, None),
    ("43%", None, "Y", None, "1999-05-17"),
)'''
tab = (
    (None, None, None, None, None),
    ("34%", None, "Y", None, "2004-03-27"),
    ("94%", None, "N", None, "2000-01-20"),
    (None, None, None, None, None),
    ("46%", None, "Y", None, "1999-09-07"),
)
print(main(tab))
