package DS.Java.Array;

public class _Array {
    int [] array;
    int passed_index;
    public _Array(int size){
        this.array = new int[size];
        this.passed_index = -1;
    }
    
    boolean isFull(){
        return this.passed_index == this.array.length - 1;
    }

    boolean isEmpty(){
        return this.passed_index == -1;
    }

    void insertFront(int data){
        if(this.isFull()){
            System.err.println("Overflow");
        }
        else{
            int i = this.passed_index;
            while(i > -1){
                this.array[i + 1] = this.array[i];
                i -= 1;
            }
            this.array[0] = data;
            this.passed_index += 1;
        }
    }

    void insertEnd(int data){
        if(this.isFull()){
            System.err.println("Overflow");
        }
        else{
            this.passed_index += 1;
            this.array[this.passed_index] = data;
        }
    }

    void insertAt(int index , int data){
        if(this.isFull()){
            System.out.println("Overfllow");
        }
        else if(index < 0 || index > this.passed_index + 1){
            System.err.println("Invalid position");
        }
        else if(index == 0){
            this.insertFront(data);
        }
        else if(index == this.passed_index + 1){
            this.insertEnd(data);
        }
        else{
            int i = this.passed_index;
            int target = index;
            while(i >= target){
                this.array[i + 1] = this.array[i];
                i -= 1;
            }
            this.array[target] = data;
            this.passed_index += 1;

        }
    }

    void delFront(){
        if(this.isEmpty()){
            System.out.println("Underflow");
        }
        else{
            int i = 0;
            while(i < this.passed_index){
                this.array[i] = this.array[i + 1];
                i += 1;
            }
            this.array[this.passed_index] = 0;
            this.passed_index -= 1;

        }
    }

    void delEnd(){
        if(this.isEmpty()){
            System.out.println("Underflow");
        }
        else{
            this.array[this.passed_index] = 0;
            this.passed_index -= 1;
        }
    }

    void delAt(int index){
        if(this.isEmpty()){
            System.out.println("Underflow");
        }
        else if(index < 0 || index > this.passed_index){
            System.err.println("Invalid position");
        }
        else if(index == 0){
            this.delFront();
        }
        else if(index == this.passed_index){
            this.delEnd();
        }
        else{
            int i = index;
            while(i <= this.passed_index){
                this.array[i] = this.array[i + 1];
                i += 1;
            }
            this.array[this.passed_index] = 0;
            this.passed_index -= 1;
        }
    }

    void reverse(){
        if(this.isEmpty()){
            System.err.println("The Array is empty");
        }
        else{
            int low = 0;
            int high = this.passed_index;
            while(low < high){
                int temp = this.array[low];
                this.array[low] = this.array[high];
                this.array[high] = temp;
                low += 1;
                high -= 1;
            }
        }
    }

    void search(int data){
        if(this.isEmpty()){
            System.err.println("The Array is empty");
        }
        else{
            boolean found = false;
            int index = -1;
            for(int i = 0 ; i <= this.passed_index ; i++){
                if(this.array[i] == data){
                    found = true;
                    index = i;
                    break;
                }
            }
            if(found == true){
                System.err.println("Data found at:"+index+"\'th index");
            }
            else{
                System.out.println("Data not found");
            }
        }
    }

    void display(){
        if(this.isEmpty()){
            System.err.println("The Array is empty");
        }
        else{
            for(int i = 0 ; i <= this.passed_index ; i++){
                System.out.print(this.array[i]+" ");
            }
        }
    }
    public static void main(String[] args){
        _Array my_array = new _Array(10);

        /*insertFront() method */
        for(int i = 0 ; i < 9 ; i++){
            my_array.insertFront(i);
        }

        /*insertEnd() method */

        my_array.insertEnd(10);

        /*delFront() method */
        for(int i = 0 ; i < 5 ; i++){
            my_array.delFront();
        }
        my_array.delEnd();

        /*insertAt() method */
        my_array.insertAt(3, 4);
        my_array.insertAt(0, 5);
        my_array.insertAt(1, 4);

        /*delAt() method */
        my_array.delAt(5);
        my_array.display();
        System.err.println("\nReversed Array:");
        my_array.reverse();
        my_array.display();
        System.err.println("\nPassed Index:"+my_array.passed_index);

        System.out.println("Searching....");
        my_array.search(5);
        my_array.search(10);

        _Array new_arrray = new _Array(20);
        for(int i = 19 ; i >= 0 ; i--){
            new_arrray.insertEnd(i);
        }
        new_arrray.display();

    }
}
