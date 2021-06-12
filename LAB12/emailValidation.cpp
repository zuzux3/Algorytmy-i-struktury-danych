#include <iostream>
using namespace std;

int main() {
    int at = 0;
    int dot = 0;
    int chars;
    bool isEmail = true;
    char email[255];

    cout << "Podaj ilosc znakow swojego adresu e-mail: ";
    cin >> chars;
    cout << "Podaj swoj adres e-mail: ";

    for (int i = 0; i < chars; i++) {
        cin >> email[i];
    }

    if ((email[0] < 'A') || ((email[0] < 'a') && (email[0] > 'Z')) || (email[0] > 'z'))
        isEmail = false;

    if (chars > 255)
        isEmail = false;

    for (int i = 0; email[i] != '@'; i++)
        at++;

    if ((at < 2) || (at > chars - 3))
        isEmail = false;

    for (int i = at + 1; i < chars; i++) {
        if (email[i] == '.') {
            dot = 1;
            break;
        }
    }

    if ((dot == 0) || (email[at + 1] == '.') || (email[chars - 1] == '.'))
        isEmail = false;

    if (isEmail)
        cout << "Wpisany email jest poprawny!\n";

    else
        cout << "Wpisany email jest niepoprawny!\n";

    return 0;

}
