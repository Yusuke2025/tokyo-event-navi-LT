// main.js
async function loadEvents() {
  const res = await fetch('data/events.json');
  const events = await res.json();
  const container = document.getElementById('events');
  const filter = document.getElementById('genreFilter');

  function render(filtered) {
    container.innerHTML = '';
    filtered.forEach(event => {
      container.innerHTML += `
        <div class="p-4 bg-white rounded shadow">
          <h2 class="text-xl font-bold">${event.title}</h2>
          <p>${event.genre}｜${event.date}｜${event.location}</p>
          <a href="${event.url}" target="_blank" class="text-blue-500">詳細を見る</a>
        </div>`;
    });
  }

  filter.addEventListener('change', () => {
    const genre = filter.value;
    const filtered = genre === 'all' ? events : events.filter(e => e.genre === genre);
    render(filtered);
  });

  render(events);
}
loadEvents();
