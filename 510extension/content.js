// chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
//     if (request.action === "scrape") {
//       let data = document.body.innerText; // Simple example: scrape all text
//       chrome.runtime.sendMessage({type: "processData", data: data});
//     }
//   });

chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.action === "scrape") {
      let data = document.body.innerText;  // Or any other logic to scrape data
      console.log("Scraped Data:", data);  // Log the data to the console
      chrome.runtime.sendMessage({type: "processData", data: data});
      sendResponse({status: "Data sent to background script"});
    }
    return true;  // Keep the messaging channel open for async response
  });
  