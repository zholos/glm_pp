#include <iostream>
#define GLM_FORCE_RADIANS
#include <glm/glm.hpp>
#include <glm/gtc/matrix_integer.hpp>
#include <glm/gtx/string_cast.hpp>

using std::cout;
using namespace glm;

dvec3 f(int x) {
    return dvec3(x, -x, 1./x);
}

int main() {
    bvec2 v1(true, false);
    ivec3 v2(5, 6, 7);
    dvec4 v3(5, 6, 7.5, 1);

    imat3x2 m1(1, 2, 3, 4, 5, 6);
    imat2x3 m2(7, 8, 9, 10, 11, 12);
    dmat4x4 m3(1.5, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 0, 5, 6, 7.5, 1);

    cout << to_string(v1) << '\n';
    cout << to_string(v2) << '\n';
    cout << to_string(v3) << '\n';
    cout << to_string(mat3x2(m1)) << '\n'; // no to_string for imat
    cout << to_string(mat2x3(m2)) << '\n';
    cout << to_string(m3) << '\n';
    cout << to_string(f(8)) << '\n';

    flush(cout);

breakpoint:;

    return 0;
}
