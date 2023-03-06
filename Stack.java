// A generic stack implementation by using an ArrayList

import java.util.*;

public class Stack<T> {
    List<T> stack = new ArrayList<T>();
    int top = -1;
    int size;

    //constructor
    Stack(int size) {
        this.size = size;
        this.stack = new ArrayList<T>(size);
    }

    boolean isEmpty() {
        return top == -1;
    }

    public T top() {
        if (isEmpty()) {
            System.out.println("Stack is empty!");
            return null;
        }
        return (T)stack.get(top);
    }

    public void push(T val) {
        if (top + 1 == size) {
            System.out.println("Stack is full!");
            return;
        } else {
            stack.add(val);
            top++;
        }
    }

    public T pop() {
        if (isEmpty()) {
            System.out.println("Stack is empty!");
            return null;
        }
        T temp = (T)stack.get(top);
        stack.remove(top);
        top--;
        return temp;
    }

    public String toString() {
        String str = "Current Stack:\n";
        for (int i = top; i >= 0; i--) {
            str += String.valueOf(stack.get(i));
            str += "\n";
        }
        return str;
    }
    public static void main(String[] args) {
        Stack<Integer> s = new Stack<Integer>(10);
        System.out.println(s.isEmpty());
        System.out.println(s.toString());
        System.out.println(s.top());
        s.push(1);
        System.out.println(s.isEmpty());
        System.out.println(s.top());
        System.out.println(s.toString());
        s.push(2);
        s.push(3);
        s.push(4);
        System.out.println(s.isEmpty());
        System.out.println(s.top());
        System.out.println(s.toString());
        int temp = s.pop();
        System.out.println(temp);
        System.out.println(s.toString());
        s.push(5);
        s.push(6);
        s.pop();
        s.pop();
        s.pop();
        s.push(7);
        System.out.println(s.toString());
        s.pop();
        s.pop();
        s.pop();
        System.out.println(s.toString());
        System.out.println(s.isEmpty());
        Stack<Integer> s2 = new Stack<Integer>(5);

        s2.push(1);
        System.out.println(s.size);
        System.out.println(s2.size);
        System.out.println(s.top);
        System.out.println(s2.top);


        Stack<String> s3 = new Stack<String>(10);
        s3.push("hello");
        s3.push("hi");
        s3.push("hey");
        System.out.println(s3.size);
        System.out.println(s3.top());
        System.out.println(s3.toString());
        s3.pop();
        System.out.println(s3.toString());

    }
}
