package DS.Java.Tree;

public class BST {
    Node root;
    public BST(){
        this.root = null;
    }

    Node insert(Node root , int data){
        if(root == null){
            Node node = new Node(data);
            return node;
        }
        else if(data > root.data){
            root.right = this.insert(root.right, data);
        }
        else if(data < root.data){
            root.left = this.insert(root.left, data);
        }
        return root;
    }

    void inOrder(Node root){
        if(root == null){   
            return;
        }
        else{
            this.inOrder(root.left);
            System.out.print(root.data+"->");
            this.inOrder(root.right);
        }
    }

    void preOrder(Node root){
        if(root == null){   
            return;
        }
        else{
            System.out.print(root.data+"->");
            this.preOrder(root.left);
            this.preOrder(root.right);
        }
    }

    void postOrder(Node root){
        if(root == null){   
            return;
        }
        else{
            this.postOrder(root.left);
            this.postOrder(root.right);
            System.out.print(root.data+"->");
        }
    }

    void search(Node root , int data){
        if(root == null){
            System.out.println("\nNot Found");
        }
        else if(root.data == data){
            System.out.println("\nData Found");
            return;
        }
        else if(data > root.data){
            this.search(root.right, data);
        }
        else if(data < root.data){
            this.search(root.left, data);
        }
    }

    public static void main(String[] args){
        BST bst = new BST();
        bst.root = bst.insert(bst.root, 10);
        for(int i = 0 ; i < 10 ; i++){
            bst.insert(bst.root, i);
        }
        System.out.println("\nInorder Traversal");
        bst.inOrder(bst.root);

        System.out.println("\nPreorder Traversal");
        bst.preOrder(bst.root);

        System.out.println("\nPostorder Traversal");
        bst.postOrder(bst.root);

        bst.search(bst.root, 10);
        bst.search(bst.root, 11);

    }
}

class Node{
    int data;
    Node left;
    Node right;
    public Node(int data){
        this.data = data;
        this.left = null;
        this.right = null;
    }
}
