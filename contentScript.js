// Function to extract text content from the current page
function getPageContent() {
    // Simple example: extracts text from body element
    let content = document.body.innerText;
    console.log("Extracted page content:", content);  // Log the extracted content
    return content;
}

// Function to send page content to an API and get a category label
function fetchCategoryLabel(pageContent) {
    const serverURL = 'http://127.0.0.1:5001/process'; // Replace with your actual API URL

    // Log the content being sent
    console.log("Sending the following content to the local server:", pageContent);

    // Setting up the API request with the page content
    fetch(serverURL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
            // 'Authorization': 'Bearer YOUR_API_TOKEN' // If your API requires an auth token
        },
        body: JSON.stringify({ content: pageContent })
    })
    .then(response => response.json())
    .then(data => {
        console.log("API response:", data.label);  // Log the API response
        console.log("API response:", data);
        displayLabel(data); // Assuming the API returns an object with a 'label' property
    })
    .catch(error => {
        console.error('Error fetching category label:', error);
        displayLabel('Error fetching label');
    });
    
}

// Function to display the category label in the suggested-category span
function displayLabel(labelObj) {
    console.log("Attempting to display label object:", labelObj);

    const suggestedCategoryElement = document.getElementById('suggested-category');
    const textBox = document.getElementById('search'); // Get the textbox where the folder name is entered

    // Extract the label from the object
    const label_final = labelObj.label; // Assuming the object structure is {label: 'Your Label'}
    console.log("Extracted label:", label_final);

    if (suggestedCategoryElement) {
        suggestedCategoryElement.textContent = label_final;
    }

    // Set the textbox value to the AI suggested category
    if (textBox) {
        textBox.value = label_final;
        console.log("Label set in search textbox:", label_final);

        // Simulate a space character using KeyboardEvent
        const spaceEvent = new KeyboardEvent('keydown', {
            bubbles: true,
            cancelable: true,
            charCode: 0,
            keyCode: 32,
            key: ' ',
            shiftKey: false,
            code: 'Space'
        });

        // Dispatch the space event
        textBox.dispatchEvent(spaceEvent);

        // To ensure it triggers input, we follow it with an 'input' event
        textBox.value += ' '; // Add a space for visual change
        const inputEvent = new Event('input', {
            bubbles: true,
            cancelable: true
        });
        textBox.dispatchEvent(inputEvent);
    }
}

// Main function to run the process
function main() {
    const pageContent = getPageContent();
    fetchCategoryLabel(pageContent);
}

// Run the main function when the content script is loaded
main();
