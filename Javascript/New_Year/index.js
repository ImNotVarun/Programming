// Set the target date for the countdown (e.g., January 1, 2025)
const targetDate = new Date("April 19, 2024 18:47").getTime();

// Function to update the countdown
function updateCountdown() {
    // Get the current date and time
    const now = new Date().getTime();

    // Calculate the remaining time
    const distance = targetDate - now;

    // Calculate days, hours, minutes, seconds, and milliseconds remaining
    const daysRemaining = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hoursRemaining = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutesRemaining = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const secondsRemaining = Math.floor((distance % (1000 * 60)) / 1000);

    // Update the countdown display
    days.textContent = daysRemaining;
    hours.textContent = hoursRemaining;
    minutes.textContent = minutesRemaining;
    seconds.textContent = secondsRemaining;


    // If the countdown is over, display the "Happy New Year" message
    if (distance < 0) {
        document.getElementById("Happy_newYear").textContent = "Happy New Year!";
    }

    // Request the next frame
    requestAnimationFrame(updateCountdown);
}

// Start the countdown
updateCountdown();


