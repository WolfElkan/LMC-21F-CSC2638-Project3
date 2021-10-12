public class CircArrayQueue <T> {
	CircArrayQueue(int initialCapacity) {

	}
	void enqueue() {}
	T dequeue() {
		T t = new T();
		return t;
	} 
	T getFront() {
		T t = new T();
		return t;
	}
	boolean isEmpty() {
		return true;
	} 
	boolean isFull() {
		return false;
	}
	public static void main(String[] args) {
		CircArrayQueue<String> test = new CircArrayQueue<>(4);
		System.out.println("Hello World");
	}
}