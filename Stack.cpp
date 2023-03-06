#include <iostream>
#include <vector>
#include <string>
#include <typeinfo>

using namespace std;

template <typename T>
class Stack
{
private:
    vector<T> theStack;
    int theSize;
    int top;
public:
    Stack(int size);
    // ~Stack();
    void push(T val);
    T pop();
    T getTop();
    bool isEmpty();
    void toString();
};

template <typename T>
Stack<T>::Stack(int size)
{
    theSize = size;
    top = -1;
}

template <typename T>
void Stack<T>::push(T val)
{
    top++;
    theStack.push_back(val);
}

template <typename T>
T Stack<T>::pop()
{
    top--;
    T temp = theStack.back();
    theStack.pop_back();
    return temp;
}

template <typename T>
T Stack<T>::getTop()
{
    return theStack.at(top);
}

template <typename T>
bool Stack<T>::isEmpty()
{
    return theStack.empty();
}

template <typename T>
void Stack<T>::toString()
{
    string str = "Current Stack:\n";
    for (int i = top; i >= 0; i--) {
        // if (typeid(theStack.at(i) ).name() == "string")
        str += to_string(theStack.at(i));
        str += "\n";
    }
    cout << str << endl;
}

int main(int argc, char const *argv[])
{
    Stack<int> testStack(10);
    cout << testStack.isEmpty() << endl;
    testStack.push(1);
    cout << testStack.isEmpty() << endl;
    testStack.push(12);
    testStack.push(14);
    cout << testStack.getTop() << endl;
    int temp = testStack.pop();
    cout << temp << endl;
    cout << testStack.getTop() << endl;
    testStack.push(25);
    testStack.push(104);
    testStack.toString();

    Stack<bool> testStack2(10);
    cout << testStack2.isEmpty() << endl;
    testStack2.push(true);
    cout << testStack.isEmpty() << endl;
    testStack2.push(false);
    testStack2.push(true);
    cout << testStack2.getTop() << endl;
    bool temp2 = testStack2.pop();
    cout << temp2 << endl;
    cout << testStack2.getTop() << endl;
    testStack2.push(false);
    testStack2.push(false);

    testStack2.toString();

    return 0;
}
