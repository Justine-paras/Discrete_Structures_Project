const startSelect = document.getElementById('start');
const endSelect = document.getElementById('end');
const computeBtn = document.getElementById('compute');
const routeDisplay = document.getElementById('route');
const distanceDisplay = document.getElementById('distance');

computeBtn.addEventListener('click', async () => {
  const start = startSelect.value;
  const end = endSelect.value;

  if (!start || !end || start === end) {
    routeDisplay.textContent = "Please select two different locations.";
    routeDisplay.style.color = "#cc0000";
    distanceDisplay.textContent = "N/A";
    return;
  }

  // Show loading state
  routeDisplay.textContent = "Calculating route...";
  routeDisplay.style.color = "#333";
  distanceDisplay.textContent = "⏳";

  try {
    const result = await window.pywebview.api.get_shortest_path(start, end);

    if (result.error) {
      routeDisplay.textContent = result.error;
      routeDisplay.style.color = "#cc0000";
      distanceDisplay.textContent = "N/A";
    } else {
      routeDisplay.textContent = result.path_string;
      routeDisplay.style.color = "#2c5e2e";
      distanceDisplay.textContent = `${result.distance} meters`;
    }
  } catch (err) {
    routeDisplay.textContent = "Error connecting to backend.";
    routeDisplay.style.color = "#cc0000";
    distanceDisplay.textContent = "N/A";
    console.error(err);
  }
});