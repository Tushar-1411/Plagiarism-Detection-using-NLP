
const plagiarismCheckerForm = document.querySelector('#query-form')

// Update table with data from Flask route results
function updateTable(results) {

  // Get table body element
  var tableBody = document.getElementById("similar-articles-table").getElementsByTagName("tbody")[0];
  
  // Clear existing table rows
  tableBody.innerHTML = "";

  // Loop through results dictionary
  for (var i = 0; i < 10; i++) {
    var tr = document.createElement('tr');

    var td1 = document.createElement('td');
    var td2 = document.createElement('td');
    var td3 = document.createElement('td');
    var td4 = document.createElement('td');

    td1.innerHTML = results['Titles'][i]
    td2.innerHTML = results['Publications'][i]
    td3.innerHTML = results['Authors'][i]
    td4.innerHTML = results['Scores'][i]

    tr.appendChild(td1);
    tr.appendChild(td2);
    tr.appendChild(td3);
    tr.appendChild(td4);

    tableBody.appendChild(tr);
  }
}



// Function to handle form submission
function handleSubmit(event) {
  event.preventDefault(); // Prevent default form submission behavior

  // var textarea = document.getElementById("text");
  // var inputText = textarea.value;
  
  fetch('/query', {
    method: 'POST',
    body: new FormData(plagiarismCheckerForm),
    // method: 'POST',
    // body: inputText, // Send input text as request body
    // headers: {
    //     'Content-Type': 'text/plain' // Set content type to plain text
    // }
}).then(function(response) {
  // Check if response is plain text or JSON
  // console.log(response.json())
  return response.json()
})
.then(function(results) {
  updateTable(results); // Update DOM with results
  // console.log(results['Authors'][0])
})
.catch(function(error) {
    console.log(error); // Log any errors to the console
});
}


// Add event listener for form submission
document.getElementById("query-form").addEventListener("submit", handleSubmit);
