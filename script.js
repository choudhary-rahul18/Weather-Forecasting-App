// Constants
const API_BASE_URL = "http://127.0.0.1:8000";

// DOM Elements
const cityInput = document.getElementById('cityInput');
const searchBtn = document.getElementById('searchBtn');
const skeleton = document.getElementById('skeleton'); // Ensure this ID matches your HTML
const display = document.getElementById('weatherDisplay');
const errorBox = document.getElementById('errorBox');
const errorText = document.getElementById('errorText');

// Event Listener
searchBtn.addEventListener('click', () => getWeather(cityInput.value.trim()));

async function getWeather(city) {
    if (!city) return;

    // Reset UI for new search
    errorBox.classList.add('hidden');
    display.classList.add('hidden');
    skeleton.classList.remove('hidden');

    try {
        const response = await fetch(`${API_BASE_URL}/weather/${city}`);
        
        // 🧱 Logic: Check status codes before parsing JSON
        if (!response.ok) {
            if (response.status === 401 || response.status === 403) {
                throw new Error("Our weather station authentication failed. We're on it!");
            }
            if (response.status === 429) {
                throw new Error("Whoa! You're searching too fast. Wait a minute.");
            }
            if (response.status >= 500) {
                throw new Error("The weather station is taking a nap. Try again in 5 minutes.");
            }
            
            // Try to get detail from backend, fallback to generic error
            const errorData = await response.json();
            throw new Error(errorData.detail || "Something went wrong.");
        }

        const data = await response.json();
        updateUI(data);

    } catch (err) {
        showError(err.message);
    } finally {
        skeleton.classList.add('hidden');
    }
}

function updateUI(data) {
    document.getElementById('cityName').innerText = data.city;
    document.getElementById('temp').innerText = `${Math.round(data.temp)}°C`;
    document.getElementById('condition').innerText = data.condition;
    document.getElementById('wind').innerText = `${data.wind_kph} kph`;
    document.getElementById('humidity').innerText = `${data.humidity}%`;
    document.getElementById('weatherIcon').src = data.icon;
    display.classList.remove('hidden');
}

// 🧱 Logic: showError should only handle the UI display
function showError(message) {
    errorText.innerText = message;
    errorBox.classList.remove('hidden');
}