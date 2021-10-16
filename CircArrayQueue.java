public class CircArrayQueue <T> {
	private T t;
	private T[] array;
	CircArrayQueue(Class<T> clazz, int initialCapacity) {
		array = (T[]) Array.newInstance(clazz, initialCapacity);
	}
	void enqueue() {}
	T dequeue() {
		return t;
	} 
	T getFront() {
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
		System.out.println(test);
	}
}