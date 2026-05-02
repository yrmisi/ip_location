let currentCoords = { lat: null, lon: null };

// Элементы DOM
const ipInput = document.getElementById('ipInput');
const searchBtn = document.getElementById('searchBtn');
const wrapper = document.getElementById('resultWrapper');
const resultsDiv = document.getElementById('results');
const errorBox = document.getElementById('errorBox');
const viewMapBtn = document.getElementById('viewMapBtn');

// Функция запроса данных
async function fetchIPInfo() {
    const ip = ipInput.value.trim();
    if (!ip) return;

    // Сброс UI перед поиском
    searchBtn.disabled = true;
    searchBtn.innerText = 'Searching...';
    errorBox.classList.add('hidden');
    wrapper.classList.add('hidden');
    currentCoords = { lat: null, lon: null };

    try {
        const response = await fetch('/api/ip_info', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ ip_address: ip })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || 'Failed to fetch data');
        }

        currentCoords.lat = data.lat;
        currentCoords.lon = data.lon;

        // Рендер карточек с данными
        resultsDiv.innerHTML = Object.entries(data)
            .map(([key, value]) => `
                <div class="bg-gray-700/50 p-3 rounded border border-gray-600">
                    <p class="text-xs text-gray-400 uppercase font-semibold">${key}</p>
                    <p class="text-white truncate" title="${value || 'N/A'}">${value || 'N/A'}</p>
                </div>
            `).join('');

        wrapper.classList.remove('hidden');

    } catch (err) {
        errorBox.innerText = err.message;
        errorBox.classList.remove('hidden');
    } finally {
        searchBtn.disabled = false;
        searchBtn.innerText = 'Lookup IP';
    }
}

// Функция открытия карты
function viewMap() {
    const ip = ipInput.value.trim();
    if (ip) {
        window.open(`/api/map?ip=${ip}`, '_blank');
    }
}

// Слушатели событий
searchBtn.addEventListener('click', fetchIPInfo);
viewMapBtn.addEventListener('click', viewMap);

// Поиск по нажатию Enter
ipInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        fetchIPInfo();
    }
});
