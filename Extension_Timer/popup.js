document.addEventListener('DOMContentLoaded', function() {
    const startButton = document.getElementById('startButton');
    const stopButton = document.getElementById('stopButton');
    const resetButton = document.getElementById('resetButton');
    const hoursInput = document.getElementById('hoursInput');
    const minutesInput = document.getElementById('minutesInput');
    const secondsInput = document.getElementById('secondsInput');
    const timerDisplay = document.getElementById('timerDisplay');
    const container = document.querySelector('.container');

    let timerInterval;
    let totalSeconds = 0;
    let timeRemaining = totalSeconds;
    let timerRunning = false;

    // Function to generate a random hex color
    function getRandomColor() {
        return '#' + Math.floor(Math.random()*16777215).toString(16);
    }

    // Function to set background gradient color
    function setBackgroundGradient() {
        const color1 = getRandomColor();
        const color2 = getRandomColor();
        container.style.background = `linear-gradient(to bottom right, ${color1}, ${color2})`;
    }

    // Set initial background gradient color
    setBackgroundGradient();

    function startTimer() {
        timerRunning = true;
        startButton.disabled = true;
        stopButton.disabled = false;
        resetButton.disabled = true;

        totalSeconds = (parseInt(hoursInput.value) * 3600) + (parseInt(minutesInput.value) * 60) + parseInt(secondsInput.value);
        timeRemaining = totalSeconds;
        updateTimerDisplay();

        timerInterval = setInterval(updateTimer, 1000);
    }

    function stopTimer() {
        timerRunning = false;
        clearInterval(timerInterval);
        startButton.disabled = false;
        stopButton.disabled = true;
        resetButton.disabled = false;
    }

    function resetTimer() {
        timerRunning = false;
        clearInterval(timerInterval);
        totalSeconds = 0;
        timeRemaining = totalSeconds;
        updateTimerDisplay();
        startButton.disabled = false;
        stopButton.disabled = true;
        resetButton.disabled = true;
    }

    function updateTimer() {
        timeRemaining--;
        updateTimerDisplay();

        if (timeRemaining <= 0) {
            stopTimer();
            playNotificationSound();
        }
    }

    function updateTimerDisplay() {
        const hours = Math.floor(timeRemaining / 3600);
        const minutes = Math.floor((timeRemaining % 3600) / 60);
        const seconds = timeRemaining % 60;
        timerDisplay.textContent = `${padZero(hours)}:${padZero(minutes)}:${padZero(seconds)}`;
    }

    function padZero(num) {
        return (num < 10 ? '0' : '') + num;
    }

    function playNotificationSound() {
        const notificationSound = new Audio('WCSC5KW-message-notification.mp3'); // Path to your notification sound file
        notificationSound.play();
    }

    startButton.addEventListener('click', startTimer);
    stopButton.addEventListener('click', stopTimer);
    resetButton.addEventListener('click', resetTimer);

    // Send message to background script to start the timer
    startButton.addEventListener('click', function() {
        chrome.runtime.sendMessage({
            type: 'startTimer',
            hours: hoursInput.value,
            minutes: minutesInput.value,
            seconds: secondsInput.value
        });
    });

    // Send message to background script to stop the timer
    stopButton.addEventListener('click', function() {
        chrome.runtime.sendMessage({ type: 'stopTimer' });
    });

    // Listen for updates to the timer display
    chrome.runtime.onMessage.addListener(function(message, sender, sendResponse) {
        if (message.type === 'updateTimerDisplay') {
            updateTimerDisplay(message.timeRemaining);
        }
    });
});
