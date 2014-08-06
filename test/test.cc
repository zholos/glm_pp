#include <iostream>
#define GLM_FORCE_RADIANS
#include <glm/glm.hpp>
#include <glm/gtc/matrix_integer.hpp>
#include <glm/gtx/string_cast.hpp>

using namespace std;
using namespace glm;

int main() {
    glm::bvec2 v1(true, false);
    glm::ivec3 v2(5, 6, 7);
    glm::dvec4 v3(5, 6, 7.5, 1);

    glm::imat3x2 m1(1, 2, 3, 4, 5, 6);
    glm::imat2x3 m2(7, 8, 9, 10, 11, 12);
    glm::dmat4x4 m3(1.5, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 0, 5, 6, 7.5, 1);

    cout << to_string(v1) << '\n';
    cout << to_string(v2) << '\n';
    cout << to_string(v3) << '\n';
    cout << to_string(mat3x2(m1)) << '\n'; // no to_string for imat
    cout << to_string(mat2x3(m2)) << '\n';
    cout << to_string(m3) << '\n';

breakpoint:
    return 0;
}
