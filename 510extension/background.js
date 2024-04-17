chrome.runtime.onMessage.addListener(function(message, sender, sendResponse) {
    if (message.type === "processData") {
      // Simulate an API response
      setTimeout(() => { // Use setTimeout to mimic network delay
        let simulatedResponse = { folderName: "Automobile" }; // Simulated response data
        let folderName = simulatedResponse.folderName;
  
        chrome.bookmarks.create({ title: folderName }, function(newFolder) {
          chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
            chrome.bookmarks.create({
              parentId: newFolder.id,
              title: tabs[0].title,
              url: tabs[0].url
            });
          });
        });
      }, 1000); // Simulate a network delay of 1 second
    }
  });
  