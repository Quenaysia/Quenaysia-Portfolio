/*This file contains ALL the JavaScript*/


function loadVehicleImage(baseName) {
  const img = document.getElementById('vehicleImg');
  const caption = document.getElementById('imgCaption');

  
  img.onerror = function () {
    if (img.src.endsWith('.png')) {
      img.onerror = null; // prevent loop
      img.src = `images/${baseName}.jpg`;
    }
  };

  img.src = `images/${baseName}.png`;
  caption.textContent = baseName.replace('_', ' ').replace('_', ' ');
}

function buyVehicle() {
  // Read input 
  const rawVehicle = document.getElementById('vehicle').value.trim().toLowerCase();
  const rawColor   = document.getElementById('color').value.trim().toLowerCase();

  const output = document.getElementById('finalOutput');

  // === IF/ELSE to validate vehicle  ===
  let vehicle;
  if (rawVehicle === 'car' || rawVehicle === 'truck') {
    vehicle = rawVehicle;
  } else {
    alert('Invalid vehicle. Please enter "car" or "truck".'); // warning 
    output.textContent = ''; 
    document.getElementById('vehicleImg').removeAttribute('src');
    document.getElementById('imgCaption').textContent = '';
    return;
  }

  // === SWITCH to evaluate color  ===
  let colorMessage = '';
  let color;
  switch (rawColor) {
    case 'black':
    case 'blue':
    case 'red':
    case 'white':
      color = rawColor;
      colorMessage = `You chose a ${color} ${vehicle}.`;
      break;

    default:
      alert('Sorry, that color is not available. Choose black, blue, red, or white.'); // warning 
      output.textContent = '';
      document.getElementById('vehicleImg').removeAttribute('src');
      document.getElementById('imgCaption').textContent = '';
      return;
  }

 
  output.textContent = colorMessage;

  // === Show the correct image ===
  const baseName = `${color}_${vehicle}`;
  loadVehicleImage(baseName);
}
