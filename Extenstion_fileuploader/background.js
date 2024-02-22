// Listen for messages from the popup
chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.action === "uploadFiles") {
        // Handle file upload action
        uploadFiles(request.files);
    }
});

// Function to upload files
function uploadFiles(files) {
    // Loop through each file
    files.forEach(function(file) {
        // Read the file contents
        readFileContents(file, function(contents) {
            // Send file contents to popup
            chrome.runtime.sendMessage({ action: "fileContents", contents: contents });
        });
    });
}

// Function to read file contents
function readFileContents(file, callback) {
    var reader = new FileReader();
    reader.onload = function(event) {
        // Once the file is loaded, call the callback with the file contents
        callback(event.target.result);
    };
    // Read the file as text
    reader.readAsText(file);
}
