#include <iostream>
using namespace std;

void coding(string txt, string key);
void decoding(string txt, string key);

int main() {
    int choosing;
    string text;
    string key;

    cout << "Podaj operacje, ktora chcesz wykonac (1 - szyfrowanie, inny - rozszyfrowywanie:\n";
    cin >> choosing;

    if (choosing == 1) {
        cout << "Podaj wyraz, ktory chcesz zaszyfrowac:\n";
        cin >> text;
        cout << "Podaj klucz, ktory chcesz zastosowac:\n";
        cin >> key;

        coding(text, key);
    }

    else {
        cout << "Podaj wyraz ktory chcesz rozszyfrowac:\n";
        cin >> text;
        cout << "Podaj klucz, ktory jest zastosowany:\n";
        cin >> key;

        decoding(text, key);
    }

    return 0;
}

void coding(string txt, string key) {
    int i = 0;
    int j = 0;

    while(txt[i] != '\0') {
        if (key[j] == '\0')
            j = 0;

        if (txt[i] + key[j] - 97 > 'z')
            txt[i] += key[j] - 97 - 26;

        else
            txt[i] += key[j] - 97;

        i++;
        j++;
    }

    cout << "Zaszyfrowany tekst to:\n" << txt;
}

void decoding(string txt, string key) {
    int i = 0;
    int j = 0;

    while(txt[i] != '\0') {
        if (key[j] == '\0')
            j = 0;

        if (txt[i] - key[j] + 97 < 'a')
            txt[i] -= key[j] + 97 + 26;

        else
            txt[i] -= key[j] + 97;

        i++;
        j++;
    }

    cout << "Zaszyfrowany tekst to:\n" << txt;
}
