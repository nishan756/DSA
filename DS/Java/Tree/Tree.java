package DS.Java.Tree;
import java.util.Scanner;
public class Tree {
    Node root;
    public Tree(){
        this.root = null;
    }

    Node insert(){
        Scanner input = new Scanner(System.in);
        System.out.print("Enter data:");
        int data = input.nextInt();
        if(data == -1){
            return null;
        }
        Node node = new Node(data);
        System.out.println("Enter left child of "+data);
        node.left = insert();

        System.out.println("Enter right child of "+data);
        node.right = insert();
        return node;
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

    public static void main(String[] args) {
        Tree tree = new Tree();
        tree.root = tree.insert();

        System.out.println("Inorder Traversal");
        tree.inOrder(tree.root);

        System.out.println("\nPreorder Traversal");
        tree.preOrder(tree.root);

        System.out.println("\nPostorder Traversal");
        tree.postOrder(tree.root);
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