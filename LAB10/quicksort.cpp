#include <iostream>
using namespace std;

void quicksort(float arr[], int left, int right);

int main() {
    int arr_size;

    cout << "Podaj wielkosc tablicy:\n";
    cin >> arr_size;

    if (arr_size > 1) {
        int last_arr = arr_size - 1;
        float arr[1000];

        cout << "Podaj zawartosc tablicy:\n";
        for (int i = 0; i < arr_size; i++)
            cin >> arr[i];

        for (int y = 0; y < arr_size; y++)
            quicksort(arr, 0, last_arr);

        cout << "Posortowana tablica = [ ";
        for (int j = 0; j < arr_size; j++)
            cout << arr[j] << " ";
        cout << "]\n";
    }

    else
        cout << "Wrong Input!\n";

    return 0;
}

void quicksort(float arr[], int left, int right) {
    int i, j, last;
    float bufor;

    last = right;
    i = left - 1;
    j = left;

    while (j < last) {
        if (arr[j] < arr[last]) {
            i++;

            bufor = arr[i];
            arr[i] = arr[j];
            arr[j] = bufor;
        }

        j++;
    }
    i++;

    bufor = arr[i];
    arr[i] = arr[last];
    arr[last] = bufor;

    if (i < right - 1)
        quicksort(arr, i + 1, right);

    if (i > left + 1)
        quicksort(arr, left, i - 1);
}
