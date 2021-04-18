import cv2

if __name__ == "__main__":
    with open("map.h", "w+") as f:
        f.write(
            "#pragma once\n"
            "#include <string>\n"
            "#include <vector>\n"
            "#include <ccomplex>\n"
            "std::vector<std::vector<std::vector<char>>> map = {\n"
        )
        map = cv2.imread("data/map.png")
        for i in range(map.shape[0]):
            f.write("\t{\n")
            for j in range(map.shape[1]):
                f.write("\t\t{ ")
                for k in range(map.shape[2]):
                    if k == map.shape[2] - 1:
                        f.write(str(map[i, j, k]) + " ")
                    else:
                        f.write(str(map[i, j, k]) + ", ")
                if j == map.shape[1] - 1:
                    f.write("}\n")
                else:
                    f.write("},\n")
            if i == map.shape[0] - 1:
                f.write("\t}\n")
            else:
                f.write("\t},\n")
        f.write("};\n")
        f.close()
