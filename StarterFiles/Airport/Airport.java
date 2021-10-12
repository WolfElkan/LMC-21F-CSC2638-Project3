/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package StudentProjects.P3_Queues.StarterFiles.Airport;
import StudentProjects.P3_Queues.StarterFiles.ArrayQueue;
import StudentProjects.P3_Queues.StarterFiles.QueueInterface;

/**
 *
 * Simulate a small airport runway as realistically as you can:
 *	Airplanes randomly generated to take off join a queue on the ground (use your queue implementation). 
 *	Airplanes randomly generated to land (less frequently then those generated to takeoff)  join a queue in the air. 
 *	Only one airplane can use the runway at a time. 
 *	All airplanes in the air must land before any airplane can takeoff. 
 *	Run the simulation for duration length that you can vary.
 * @author KarinaAssiter
 */
public class Airport {

    // Declare instance variables arrivalQueue and departureQueue of type QueueInterface<Plane>
    private QueueInterface<Plane> arrivalQueue;
    private QueueInterface<Plane> departureQueue;

    // *************************************************************************
    // Constructor 
    //   Create the arrivalQueue and departureQueue objects (i.,e. both of type
    //   ArrayQueue<Plane>
    // *************************************************************************
    public Airport() {
        
        System.out.println("STUB Airport constructor : replace with your code");
        
    }

    // *************************************************************************
    // simulate 
    // 
    //    loop duration number of times
    //         if a generated random number (i.e., Math.random()) is less than arrival probability
    //            Generate a plane object and add it to the arrivalQueue
    //         if a generated random number is less than departure probability
    //            Generate a plane object and add it to the departureQueue
    //
    //         if a plane is waiting to land (arrival queue not empty)
    //            let it land
    //         otherwise if a plane is waiting to take off (departure queue not empty)
    //            let it takeoff
    // 
    
    public void simulate(int duration, double arrivalProbability, double departureProbability) {
       
        System.out.println("STUB simulate method : replace with your code");
    }

    public static void main(String[] args) {
        Airport airport = new Airport();
        airport.simulate(100, .3, .5);
    }
}
