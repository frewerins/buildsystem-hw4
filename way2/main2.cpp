#include "map.h"

#include <opencv2/core.hpp>
#include <string>
#include <opencv2/imgcodecs.hpp>

int main() {
    auto file = cv::imread("../../data/file.jpg");
    for (size_t i = 0; i < file.rows; ++i) {
        for (size_t j = 0; j < file.cols; ++j) {
            auto& item = file.at<cv::Vec3b>(i, j);
            for (int k = 0; k < file.channels(); ++k) {
                auto result = map[abs(file.channels() - (k + 1))][item[k]];
                item[k] = result[k];
            }
        }
    }
    cv::imwrite("../../data/result2.png", file);
    return 0;
}
