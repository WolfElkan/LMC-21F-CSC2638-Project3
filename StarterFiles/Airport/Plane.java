/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package StudentProjects.P3_Queues.StarterFiles.Airport;

/**
 *
 * @author KarinaAssiter
 */
public class Plane {
    private int id;
    static int nextId = 1;
    
    public Plane() {
        id = nextId;
        nextId = (nextId+1)%10000; // eventually re-use numbers
        
    }
    public int getId() {
        return id;
    }
    
    public String toString() { 
        return "Plane " + id;
    }
    
    public static void main(String[] args) {
        Plane p = new Plane();
        System.out.println(p);
    }
    
}
