def compare_versions(version1: str, version2: str) -> int:
    v1 = version1.split('.')
    v2 = version2.split('.')

    len_v1 = len(v1)
    len_v2 = len(v2)

    for i in range(max(len_v1, len_v2)):
        i1 = int(v1[i]) if i < len_v1 else 0
        i2 = int(v2[i]) if i < len_v2 else 0

        if i1 != i2:
            return 1 if i1 > i2 else -1
    return 0


if __name__ == '__main__':
    print(compare_versions('1.2.2', '1.2.2'))
    print(compare_versions('1.2.2', '1.2.1'))
    print(compare_versions('1.2.1', '1.2.2'))
