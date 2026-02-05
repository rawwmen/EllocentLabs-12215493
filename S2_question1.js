// Question 1: API Data Processing (Async/Await + Array Methods)                                                              (Time: 1 hour)
// Fetch users from: https://jsonplaceholder.typicode.com/users
// Requirements:
// Write an async function that:
//   Fetches the data
//   Filters users by a given city name
//   Sorts users alphabetically by name
//   Returns only: { name, email }
// Expected Output Example: [ { name: "Leanne Graham", email: "leanne@gmail.com" }]



async function getUsersByCity(city) {
  const response = await fetch("https://jsonplaceholder.typicode.com/users")
  const users = await response.json()

  return users
    .filter(user => user.address.city.toLowerCase() === city.toLowerCase())
    .sort((a, b) => a.name.localeCompare(b.name))
    .map(user => ({
      name: user.name,
      email: user.email
    }))
}

// Test
getUsersByCity("Gwenborough").then(console.log)

// I’m using an async function with await to fetch the data and convert it into JSON. 
// After that, I filter the users based on the given city, sort them alphabetically using localeCompare, 
// and finally map the result to return only the name and email fields.
