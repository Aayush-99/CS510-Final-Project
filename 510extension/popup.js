document.getElementById('scrape').addEventListener('click', function() {
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
      chrome.tabs.sendMessage(tabs[0].id, {action: "scrape"});
    });
    window.close(); // Close the popup when the user clicks the button
  });
  