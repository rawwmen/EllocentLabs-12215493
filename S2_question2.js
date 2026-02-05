// Question 2: Rate Limiter (Closures + Timing) 
// Create a utility: const limitedFn = rateLimit(fn, delay); 
// Behavior: The function should execute only once within the given delay. 
// Extra calls during the delay should be ignored. Example: 
// limitedFn(); // runs 
// limitedFn(); // ignored 
// Notes: Must use closures. Use setTimeout or similar timing logic.


function rateLimit(fn, delay) {
  let canRun = true

  return function () {
    if (!canRun) return

    canRun = false
    fn()

    setTimeout(() => {
      canRun = true
    }, delay)
  }
}

const limitedFn = rateLimit(() => {
  console.log("function executed")
}, 2000)

limitedFn()
limitedFn()

//I’m using a closure to store a flag that controls execution and resetting it after the delay using setTimeout.
