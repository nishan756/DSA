package DS.Java.LL;

public class SLL {
    Node head;
    Node tail;
    public SLL(){
        this.head = null;
        this.tail = null;
    }

    boolean isEmpty(){
        return this.head == null;
    }

    int length(){
        int count = 0;
        Node temp = this.head;
        while(temp != null){
            count += 1;
            temp = temp.next;
        }
        return count;
    }

    void insertFront(int data){
        Node node = new Node(data);
        if(this.isEmpty()){
            this.head = node;
            this.tail = node;
        }
        else{
            node.next = this.head;
            this.head = node;
        }
    }

    void insertEnd(int data){
        Node node = new Node(data);
        if(this.isEmpty()){
            this.head = node;
            this.tail = node;
        }
        else{
            this.tail.next = node;
            this.tail = node;
        }
    }

    void insertAt(int pos , int data){
        int length = this.length();
        if(pos < 1 || pos > length + 1){
            System.out.println("Invalid Position");
        }
        else if(pos == 1){
            this.insertFront(data);
        }
        else if(pos == length + 1){
            this.insertEnd(data);
        }
        else{
            int current = 1;
            int prev = pos - 1;
            Node temp = this.head;
            Node node = new Node(data);

            while(current < prev){
                temp = temp.next;
                current += 1;
            }
            node.next = temp.next;
            temp.next = node;
        }
    }

    void delFront(){
        if(this.isEmpty()){
            System.out.println("The SLL is empty");
        }
        else if(this.head == this.tail){
            this.head = null;
            this.tail = null;
        }
        else{
            Node target = this.head;
            this.head = target.next;
            target = null;
        }
    }

    void delEnd(){
        if(this.isEmpty()){
            System.out.println("The SLL is empty");
        }
        else if(this.head == this.tail){
            this.head = null;
            this.tail = null;
        }
        else{
            Node temp = this.head;

            while(temp.next != this.tail){
                temp = temp.next;
            }
            temp.next = null;
            this.tail = temp;

        }
    }

    void delAt(int pos){
        int length = this.length();
        if(pos < 1 || pos > length){
            System.out.println("Invalid Position");
        }
        else if(pos == 1){
            this.delFront();
        }
        else if(pos == length){
            this.delEnd();
        }
        else{
            Node temp = this.head;
            int current = 1;
            int prev = pos - 1;
            while(current < prev){
                temp = temp.next;
                current += 1;
            }
            Node target = temp.next;
            temp.next = target.next;
            target = null;

        }
    }

    void display(){
        if(this.isEmpty()){
            System.out.println("The SLL is empty");
        }
        else{
            Node temp = this.head;
            while(temp.next != null){
                System.out.print(temp.data+"->");
                temp = temp.next;
            }
            System.out.print(temp.data);
        }
    }

    void headTail(){
        if(this.isEmpty()){
            System.out.println("The SLL is empty");
        }
        else{
            System.out.println("\nHead:"+this.head.data+"\nTail:"+this.tail.data);
        }
    }

    public static void main(String[] args){
        SLL sll = new SLL();

        /* Insertion*/
        for(int i = 0 ; i < 10 ; i++){
            sll.insertFront(i);
        }
        for(int i = 0 ; i < 10 ; i++){
            sll.insertEnd(i);
        }
        sll.insertAt(11, 10);

        /* Deletion*/
        for(int i = 0 ; i < 5 ; i++){
            sll.delFront();
        }
        for(int i = 0 ; i < 5 ; i++){
            sll.delEnd();
        }
        sll.delAt(6);
        sll.display();
        sll.headTail();
        System.out.println("Length:"+sll.length());
    }
}

class Node{
    int data;
    Node next;
    public Node(int data){
        this.data = data;
        this.next = null;
    }
}
