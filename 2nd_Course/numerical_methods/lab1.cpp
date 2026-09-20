#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

struct Variant {
    double a, b, c, exact1, exact2;
};

template <typename T>
void solve(T a, T b, T c, double exact1, double exact2, const char* type) {
    T D = b * b - 4 * a * c;

    if (D < 0){
        cout << "D < 0. Корені комплексні.\n";
        return;
    }

    T sqrtD = sqrt(D);

    // Класичний метод
    T x1Classic = (-b + sqrtD) / (2 * a);
    T x2Classic = (-b - sqrtD) / (2 * a);

    // Модифікований метод
    T sign = (b >= 0) ? 1 : -1;

    T q = static_cast<T>(-0.5) * (b + sign * sqrtD);

    T x1Modified = q / a;
    T x2Modified = c / q;

    auto printResult = [&](const char* method, T x1, T x2){
        double X1 = x1;
        double X2 = x2;

        double absError1 = fabs(X1 - exact1);
        double absError2 = fabs(X2 - exact2);

        double relError1 = (exact1 != 0) ? absError1 / fabs(exact1) : 0;
        double relError2 = (exact2 != 0) ? absError2 / fabs(exact2) : 0;

        cout << "\nMethod: " << method << '\n';
        cout << "Type:   " << type << '\n';

        cout << "x1 = " << X1 << '\n';
        cout << "x2 = " << X2 << '\n';

        cout << "Absolute error x1 = " << absError1 << '\n';
        cout << "Relative error x1 = " << relError1 << '\n';

        cout << "Absolute error x2 = " << absError2 << '\n';
        cout << "Relative error x2 = " << relError2 << '\n';
    };

    printResult("Classic", x1Classic, x2Classic);
    printResult("Modified", x1Modified, x2Modified);
}

int main() {
    Variant variants[30] = {
        {1, -100000, 1, 99999.99999, 1e-5},
        {1, -1000000, 1, 999999.999999, 1e-6},
        {1, -10000000, 1, 1e7, 1e-7},
        {1, -500000, 2, 499999.999996, 4e-6},
        {1, -200000, 1, 199999.999995, 5e-6},
        {1, -2000000, 2, 1999999.999999, 1e-6},
        {1, -300000, 3, 299999.99999, 1e-5},
        {1, -1e6, 0.001, 999999.999999, 1e-9},
        {1, -1e5, 0.001, 99999.99999, 1e-8},
        {1, -1e7, 0.001, 9999999.999999, 1e-10},
        {1, -123456, 1, 123455.999992, 8.1e-6},
        {1, -654321, 1, 654320.999998, 1.5e-6},
        {1, -999999, 2, 999998.999999, 2e-6},
        {1, -888888, 1, 888887.999999, 1.1e-6},
        {1, -777777, 1, 777776.999999, 1.3e-6},
        {1, -333333, 1, 333332.999997, 3e-6},
        {1, -250000, 1, 249999.999996, 4e-6},
        {1, -1e8, 1, 1e8, 1e-8},
        {1, -5e6, 1, 4999999.999999, 2e-7},
        {1, -2e6, 2, 1999999.999999, 1e-6},
        {1, -3e5, 1, 299999.999997, 3e-6},
        {1, -7e5, 1, 699999.999999, 1.4e-6},
        {1, -9e5, 2, 899999.999999, 2.2e-6},
        {1, -4e5, 1, 399999.999998, 2.5e-6},
        {1, -6e5, 3, 599999.999999, 5e-6},
        {1, -8e5, 4, 799999.999999, 5e-6},
        {1, -1.2e6, 2, 1199999.999999, 1.7e-6},
        {1, -1.5e6, 3, 1499999.999999, 2e-6},
        {1, -2.5e6, 5, 2499999.999999, 2e-6},
        {1, -5e6, 10, 4999999.999999, 2e-6}
    };

    int number;
    cout << "Введіть номер варіанту (1-30): ";
    cin >> number;

    if (number < 1 || number > 30) {
        cout << "Ви ввели не вірний номер" << endl;;
        return 1;
    }

    Variant v = variants[number - 1];

    cout << fixed << setprecision(15);

    cout << "\na = " << v.a;
    cout << "\nb = " << v.b;
    cout << "\nc = " << v.c;

    cout << "\n\nExact x1 = " << v.exact1;
    cout << "\nExact x2 = " << v.exact2 << '\n';

    solve<float>(v.a, v.b, v.c, v.exact1, v.exact2, "float");
    solve<double>( v.a, v.b, v.c, v.exact1, v.exact2, "double");

    return 0;
}
