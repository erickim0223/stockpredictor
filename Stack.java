import java.util.*;

public class Stack {
    List<Integer> stack = new ArrayList<Integer>();
    int size = 0;

    boolean isEmpty() {
        return size == 0;
    }

    public int top() {
        if (isEmpty()) {
            return -1;
        }
        return (int)stack.get(size - 1);
    }

    public void push(int val) {
        stack.add(val);
        size++;
    }

    public int pop() {
        if (isEmpty()) {
            return -1;
        }
        int temp = (int)stack.get(size - 1);
        stack.remove(size - 1);
        size--;
        return temp;
    }

    public String toString() {
        String str = "Current Stack:\n";
        for (int i = size; i > 0; i--) {
            str += Integer.toString(stack.get(i - 1));
            str += "\n";
        }
        return str;
    }
    public static void main(String[] args) {
        Stack s = new Stack();
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
        Stack s2 = new Stack();
        
        s2.push(1);
        System.out.println(s.size);
        System.out.println(s2.size);

    }
}
