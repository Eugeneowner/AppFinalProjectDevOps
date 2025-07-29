// Автотема на основе времени суток
window.onload = function () {
  const hour = new Date().getHours();
  const body = document.body;
  if (hour < 6 || hour > 18) {
    body.classList.remove('light');
    body.classList.add('dark');
  } else {
    body.classList.remove('dark');
    body.classList.add('light');
  }
};

// Переключатель темы вручную
function toggleTheme() {
  const body = document.body;
  body.classList.toggle('dark');
  body.classList.toggle('light');
}