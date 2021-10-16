## Was this the best application of a queue? Why or why not?

A real-life airport will *usually* follow the FIFO paradigm, however exceptions will occasionally have to be made, moving certain aircraft to the front of the queue in an emergency.  The queue, as it currently exists, does not support such exceptions, and could cause problems were it implemented by an active airport.

One issue I encountered was that if planes have an opportunity to take off, land, or join either queue at each time increment, then a backlog never really builds up.  At most, one plane will join the queue at a time, and that plane immediately can take off or land.  To solve this, I prevented closed the runway any time a plane joined either queue.  This meant each plane had to wait a minimum of 1 time increment (5 minutes in this case) before taking off or landing.  

## Describe other types of problems for which you think it would be appropriate to apply a queue. 

Any problem where elements need to be retrieved from a list in the same order that they were inserted can usually be solved with a Queue.  One that comes to mind is phone calls coming into a call center.  Rather than being simulated by a queue, this application would actually *implement* one, as the software to manage the calls would have to keep track of which ones needed to be sent to agents to answer.

As I mentioned in [CBA 1](https://landmark.instructure.com/courses/3993/assignments/97844/submissions/4514), other examples include:

* Documents spooled to a printer
* People waiting in line to buy tickets, checkout groceries, or any number of things
* Songs on a playlist if only the "Play Later" button is used