#include <iostream>

using namespace std;

void bubbleSort();

int list[1000];

int num;

int main()
{
    cin >> num;

    for (int i = 0; i < num; ++i)
    {
        cin >> list[i];
    }

    bubbleSort();

    for (int i = 0; i < num; ++i)
    {
        cout << list[i] << " ";
    }

    return 0;
}

void bubbleSort()
{
    int counter{0};
    for (int i = 0; i < (num - 1); ++i)
    {
        if (list[i] <= list[i + 1])
        {
            ++counter;
        }
        else 
        {
            const int temp{list[i + 1]};
            list[i + 1] = list[i];
            list[i] = temp;
        }
    }

    if (counter != (num - 1))
    {
        bubbleSort();
    } 
    else
    {
        return;
    }
}
