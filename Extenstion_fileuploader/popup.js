// Listen for messages from the background script
chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.action === "fileContents") {
        // Display the file contents in the input area
        document.getElementById("inputArea").value = request.contents;
    }
});
