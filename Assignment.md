## Queue Implementation
1. Use a **circular array**, as described in Segments 8.8 and 8.9 of the text to implement a **Queue** class with the standard behaviors (`enqueue`, `dequeue`, `getFront()`, `isEmpty()`, `isFull()`). Count entries to ascertain whether the queue is empty or full *(otherwise you will not be able to tell)*. 
2. Test all methods before you proceed to use your class in the application *(below)*.
## Queue Application
**Simulate** a small airport **runway** as realistically as you can:
* Airplanes randomly generated to **take off** join a **queue on the ground** (use your **queue** implementation). 
* Airplanes randomly generated to **land** (less frequently then those generated to takeoff) join a **queue in the air**. 
* **Only one** airplane can use the runway at a time. 
* All airplanes in the **air** must **land before** any airplane can **takeoff**. 
* **Run** the simulation for duration length that you can vary.