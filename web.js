// Aktivizo kamerën
fetch('/activate', { method: 'POST' })
  .then(response => response.text())
  .then(message => console.log(message));

// Çaktivizo kamerën
fetch('/deactivate', { method: 'POST' })
  .then(response => response.text())
  .then(message => console.log(message));

// Regjistro audio
fetch('/record', { method: 'POST' })
  .then(response => response.text())
  .then(message => console.log(message));
