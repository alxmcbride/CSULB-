package lab1;

/**
 * This class is used as a stopwatch to calculate elapsed time
 */

public class Stopwatch {

    private long start;
    private long now;

    /**
     * Initializes a new stopwatch.
     */
    public Stopwatch() {
        start = 0;
        now = 0;
    }

    /**
     * Starts the stopwatch
     */
    public void start() {
        start = System.nanoTime();
    }

    /**
     * Stops the stopwatch
     */
    public void stop() {
        now = System.nanoTime();
    }

    /**
     * Returns the elapsed CPU time (in seconds) since the stopwatch was created.
     * @return elapsed CPU time (in seconds) since the stopwatch was created
     */
    public double elapsedTime() {

        return (now - start) / 1000000000.0;
    }

}
