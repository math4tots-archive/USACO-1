"""
ID: math4to3
LANG: PYTHON3
TASK: transform
"""
class Pattern:
    def __init__(self, rows):
        # rows : List[str]
        self.rows = tuple(rows)

    def __eq__(self, other):
        return (
            type(self) is type(other) and
            self.rows == other.rows
        )

    def __str__(self):
        return '\n'.join(
            row for row in self.rows
        )

    def rotate90(self):
        "clockwise 90 degree rotation"
        rows = self.rows
        R = len(rows)
        C = len(rows[0])
        return Pattern([
            ''.join(
                rows[R - 1 - r][c]
                for r in range(R)
            )
            for c in range(C)
        ])

    def rotate(self, n):
        ret = self
        for _ in range(n):
            ret = ret.rotate90()
        return ret

    def reflect(self):
        return Pattern([
            ''.join(reversed(row))
            for row in self.rows
        ])

def solve(original, new) -> int:
    if new == original.rotate90():
        return 1
    if new == original.rotate(2):
        return 2
    if new == original.rotate(3):
        return 3
    if new == original.reflect():
        return 4
    for i in range(4):
        if new == original.reflect().rotate(i):
            return 5
    if new == original:
        return 6
    return 7


def read():
    with open('transform.in') as f:
        N = int(f.readline())

        rows = []
        for _ in range(N):
            rows.append(f.readline().strip())
        original = Pattern(rows)

        rows = []
        for _ in range(N):
            rows.append(f.readline().strip())
        new = Pattern(rows)

    return original, new


def main():
    original, new = read()
    answer = solve(original, new)
    with open('transform.out', 'w') as f:
        f.write(f'{answer}\n')


if __name__ == '__main__':
    main()
