package DS.Java.LL;
public class DLL {
    Node head;
    Node tail;
    public DLL(){
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
            this.head.prev = node;
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
            node.prev = this.tail;
            this.tail.next = node;
            this.tail = node;
        }
    }

    void insertAt(int pos , int data){
        int length = this.length();
        if(pos < 1 || pos > length + 1){
            System.out.println("Invalid position");
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
            Node node = new Node(data);
            Node temp = this.head;

            while(current < prev){
                current += 1;
                temp = temp.next;

            }
            node.next = temp.next;
            node.prev = temp;

            temp.next.prev = node;
            temp.next = node;


        }
    }

    void delFront(){
        if(this.isEmpty()){
            System.out.println("The DLL is empty");
        }
        else if(this.head == this.tail){
            this.head = null;
            this.tail = null;
        }
        else{
            Node target = this.head;
            this.head = target.next;
            this.head.prev = null;
        }
    }

    void delEnd(){
        if(this.isEmpty()){
            System.out.println("The DLL is empty");
        }
        else if(this.head == this.tail){
            this.head = null;
            this.tail = null;
        }
        else{
            Node target = this.tail;
            this.tail = target.prev;
            this.tail.next = null;
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
            int current = 1;
            int prev = pos - 1;
            Node temp = this.head;

            while(current < prev){
                current += 1;
                temp = temp.next;
            }

            Node target = temp.next;

            temp.next = target.next;
            target.next.prev = temp;

            target = null;
        }
    }

    String search(Node temp , int data){
        if(temp == null){
            return "Data not found";
        }
        else if(temp.data == data){
            return "Data found";
        }
        else{
            return search(temp.next , data);
        }
    }
    void forDisplay(){
        if(this.isEmpty()){
            System.out.println("The DLL is empty");
        }
        else{
            Node temp = this.head;
            while(temp.next != null){
                System.out.print(temp.data+"<->");
                temp = temp.next;
            }
            System.out.print(temp.data);
        }
    }

    void backDisplay(){
        if(this.isEmpty()){
            System.out.println("The DLL is empty");
        }
        else{
            Node temp = this.tail;
            while(temp.prev != null){
                System.out.print(temp.data+"<->");
                temp = temp.prev;
            }
            System.out.print(temp.data);
        }
    }

    void headTail(){
        if(this.isEmpty()){
            System.out.println("The DLL is empty");
        }
        else{
            System.out.print("\nHead:"+this.head.data+"\nTail:"+this.tail.data);
        }
    }

    public static void main(String[] args){
        DLL dll = new DLL();
        for(int i = 0 ; i < 10 ; i++){
            dll.insertFront(i);
        }
        for(int i = 0 ; i < 10 ; i++){
            dll.insertEnd(i);
        }
        dll.insertAt(11 , 10);
        for(int i = 0 ; i < 5 ; i++){
            dll.delFront();
        }
        for(int i = 0 ; i < 5 ; i++){
            dll.delEnd();
        }
        dll.delAt(6);
        dll.delAt(1);
        dll.delAt(9);
        System.out.println("\nForward Display");
        dll.forDisplay();

        System.out.println("\nBackward Display");
        dll.backDisplay();
        dll.headTail();
        System.out.println("\nLength:"+dll.length());
        System.out.println(dll.search(dll.head, 10));
        System.out.println(dll.search(dll.head, 1));
    }
}

class Node{
    int data;
    Node prev;
    Node next;
    public Node(int data){
        this.data = data;
        this.prev = null;
        this.next = null;
    }
}
