// Sample data for star systems and their resource requirements
const starSystems = {
  Earth: {
    resourcesRequired: { fuel: 10, food: 5, minerals: 2, research: 1 },
    description: "The home planet of humanity.",
  },
  Mars: {
    resourcesRequired: { fuel: 20, food: 10, minerals: 5, research: 2 },
    description: "The red planet, a potential colony.",
  },
  Jupiter: {
    resourcesRequired: { fuel: 30, food: 15, minerals: 8, research: 4 },
    description: "A gas giant with rich resources.",
  },
  Saturn: {
    resourcesRequired: { fuel: 40, food: 20, minerals: 12, research: 6 },
    description: "Known for its stunning rings.",
  },
  Uranus: {
    resourcesRequired: { fuel: 50, food: 25, minerals: 15, research: 8 },
    description: "An ice giant in the outer solar system.",
  },
  Neptune: {
    resourcesRequired: { fuel: 60, food: 30, minerals: 20, research: 10 },
    description: "A distant ice giant with strong winds.",
  },
};

// Player object with separate resource quantities
const player = {
  name: "Player Name",
  currentPlanet: "Earth",
  resources: {
    fuel: 100,
    food: 50,
    minerals: 10,
    research: 5,
  },
};

// Function to update player information on the UI
function updateUI() {
  document.getElementById(
    "player-name"
  ).innerText = `Player Name: ${player.name}`;
  document.getElementById(
    "current-planet"
  ).innerText = `Current Planet: ${player.currentPlanet}`;
  document.getElementById(
    "fuel-resources"
  ).innerText = `Fuel: ${player.resources.fuel}`;
  document.getElementById(
    "food-resources"
  ).innerText = `Food: ${player.resources.food}`;
  document.getElementById(
    "mineral-resources"
  ).innerText = `Minerals: ${player.resources.minerals}`;
  document.getElementById(
    "research-resources"
  ).innerText = `Research: ${player.resources.research}`;
}

// Ensure the log always scrolls to the latest entry
function scrollToLatestEntry() {
  const logContainer = document.getElementById("log-container");
  logContainer.scrollTop = logContainer.scrollHeight;
}

// Function to log messages in the game log
function log(message) {
  const logList = document.getElementById("log-list");
  const listItem = document.createElement("li");
  listItem.innerText = message;
  logList.appendChild(listItem);

  scrollToLatestEntry(); // Scroll to the latest log entry
}

// Function to draw the map
function drawMap() {
  const canvas = document.getElementById("map");
  const ctx = canvas.getContext("2d");
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // Draw star systems on the map
  Object.keys(starSystems).forEach((system, index) => {
    const x = 50 + index * 100;
    const y = 200;
    ctx.beginPath();
    ctx.arc(x, y, 10, 0, 2 * Math.PI);
    ctx.fillStyle = "yellow";
    ctx.fill();
    ctx.stroke();
    ctx.fillStyle = "black";
    ctx.textAlign = "center";
    ctx.fillText(system, x, y + 30);
  });
}

// Function to select a star system on the map
function selectSystem(event) {
  const canvas = document.getElementById("map");
  const rect = canvas.getBoundingClientRect();
  const x = event.clientX - rect.left;
  const y = event.clientY - rect.top;

  // Check if a star system is clicked
  Object.keys(starSystems).forEach((system, index) => {
    const systemX = 50 + index * 100;
    const systemY = 200;
    const distance = Math.sqrt((x - systemX) ** 2 + (y - systemY) ** 2);

    if (distance <= 10) {
      displaySystemInfo(system);
      return;
    }
  });
}

// Function to simulate traveling to a random planet
function travel() {
  const randomPlanet = getRandomPlanet();
  player.currentPlanet = randomPlanet;
  log(`Traveled to ${randomPlanet}`);
  updateUI();
}

// Function to simulate exploring a planet
function explore() {
  const explorationResult = Math.floor(Math.random() * 20) + 1;
  // Simulate finding resources during exploration
  player.resources.fuel += explorationResult;
  player.resources.food += explorationResult / 2;
  player.resources.minerals += explorationResult / 4;
  player.resources.research += explorationResult / 5;
  log(
    `Explored and found ${explorationResult} fuel, ${
      explorationResult / 2
    } food, ${explorationResult / 4} minerals, and ${
      explorationResult / 5
    } research resources`
  );
  updateUI();
}

// Function to simulate harvesting resources on the current planet
function harvest() {
  const harvestAmount = Math.floor(Math.random() * 10) + 1;
  // Simulate harvesting resources
  player.resources.fuel += harvestAmount;
  player.resources.food += harvestAmount / 2;
  player.resources.minerals += harvestAmount / 4;
  player.resources.research += harvestAmount / 5;
  log(
    `Harvested ${harvestAmount} fuel, ${harvestAmount / 2} food, ${
      harvestAmount / 4
    } minerals, and ${harvestAmount / 5} research resources`
  );
  updateUI();
}

// Function to simulate trading resources with other ships
function trade() {
  const tradeAmount = Math.floor(Math.random() * 10) + 1;
  // Simulate trading resources
  if (
    player.resources.fuel >= tradeAmount &&
    player.resources.food >= tradeAmount / 2
  ) {
    player.resources.fuel -= tradeAmount;
    player.resources.food -= tradeAmount / 2;
    player.resources.minerals += tradeAmount / 4;
    player.resources.research += tradeAmount / 5;
    log(
      `Traded ${tradeAmount} fuel and ${tradeAmount / 2} food resources for ${
        tradeAmount / 4
      } minerals and ${tradeAmount / 5} research`
    );
    updateUI();
  } else {
    log("Not enough resources to trade");
  }
}

// Function to display information about a selected star system
function displaySystemInfo(system) {
  const systemInfo = starSystems[system];
  const requiredResources = systemInfo.resourcesRequired;
  const description = systemInfo.description;

  log(`Selected star system: ${system}`);
  log(`Description: ${description}`);
  log(
    `Resources required: Fuel - ${requiredResources.fuel}, Food - ${requiredResources.food}, Minerals - ${requiredResources.minerals}, Research - ${requiredResources.research}`
  );
}

// Function to get a random planet for travel
function getRandomPlanet() {
  const planetsArray = Object.keys(starSystems);
  const randomIndex = Math.floor(Math.random() * planetsArray.length);
  return planetsArray[randomIndex];
}

// Initial UI update and map rendering
updateUI();
drawMap();
