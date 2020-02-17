a = int(input())
s = [" _oO^____", "(._,     \\", "   \  _\ /\\", "    || ||", "~~~~~~~~~~~~~"]

if a > 0:
    s.insert(0, "  \\")
    if a > 1:
        s.insert(0, " \\")
        if a > 2:
            s.insert(0, "\\")
            if a > 4:
                s.insert(0, "\\")


print(*s, sep="\n")
