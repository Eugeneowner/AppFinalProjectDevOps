window.onload = function () {
  const hour = new Date().getHours();
  const isNight = hour < 6 || hour > 18;

  if (isNight) {
    document.body.classList.add('night');
  }
};