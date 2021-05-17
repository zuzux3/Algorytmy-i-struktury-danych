#include <iostream>
#include <string>
using namespace std;

int main() {
    string sentence;
    unsigned int strLength;

    cout << "Podaj zdanie do zaszyfrowania:\n";
    getline (cin, sentence);
    strLength = sentence.length();

    cout << "\nZaszyfrowane zdanie:\n";
    for (int i = 0; i < strLength; i += 2)
        swap(sentence[i], sentence [i + 1]);

    cout << sentence << "\n";

    return 0;
}
