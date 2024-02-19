let timerInterval;
let totalSeconds = 0;
let timeRemaining = totalSeconds;
let timerRunning = false;

function startTimer(hours, minutes, seconds) {
    timerRunning = true;
    totalSeconds = (parseInt(hours) * 3600) + (parseInt(minutes) * 60) + parseInt(seconds);
    timeRemaining = totalSeconds;
    updateTimer();
    timerInterval = setInterval(updateTimer, 1000);
}

function stopTimer() {
    timerRunning = false;
    clearInterval(timerInterval);
}

function updateTimer() {
    timeRemaining--;
    if (timeRemaining <= 0) {
        stopTimer();
        playNotificationSound();
    }
    // Send message to update timer display in popup (if open)
    chrome.runtime.sendMessage({ type: 'updateTimerDisplay', timeRemaining });
}

function playNotificationSound() {
    const notificationSound = new Audio('WCSC5KW-message-notification.mp3'); // Path to your notification sound file
    notificationSound.play();
}

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.type === 'startTimer') {
        const { hours, minutes, seconds } = message;
        startTimer(hours, minutes, seconds);
    } else if (message.type === 'stopTimer') {
        stopTimer();
    }
});
