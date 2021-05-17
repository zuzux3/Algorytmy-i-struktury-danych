#include <iostream>
#include <string>
using namespace std;

int main() {
    unsigned int height = 3;
    int posit, a, b;
    string sentence;

    cout << "Podaj zdanie do zaszyfrowania:\n";
    getline(cin, sentence);

    cout << "Zaszyfrowane zdanie:\n";
    for (int i = 0; i < height; i++) {
        cout << sentence[i];

        posit = i;
        a = 2 * (height - 1) - 2 * i;
        b = 2 * i;

        while ((posit + a) < sentence.size() || (posit + b) < sentence.size()) {
            if (a > 0 && (posit + a) < sentence.size())
                cout << sentence[posit + a];

            if (a > 0)
                posit += a;

            if (b > 0 && (posit + b) < sentence.size())
                cout << sentence[posit + a];

            if (b > 0)
                posit += b;
        }
    }
    cout << "\n";

    return 0;
}
