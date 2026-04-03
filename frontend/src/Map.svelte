<script>
  import { onMount } from 'svelte';
  export let geojson;

  let mapEl;

  onMount(async () => {
    const L = await import('leaflet');
    await import('leaflet/dist/leaflet.css');

    const map = L.map(mapEl).setView([40.0, -77.5], 7);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    function getColor(status) {
      if (status === 'good')    return '#22c55e';
      if (status === 'warning') return '#f59e0b';
      return '#ef4444'; // bad
    }

    L.geoJSON(geojson, {
      style: (feature) => ({
        fillColor: getColor(feature.properties.status),
        fillOpacity: 0.6,
        color: '#333',
        weight: 0.5
      }),
      onEachFeature: (feature, layer) => {
        const p = feature.properties;
        layer.bindPopup(`
          <b>${p.NAMELSAD20 ?? 'Precinct'}</b><br>
          Matched: ${p.matched_name}<br>
          Status: ${p.status}
        `);
      }
    }).addTo(map);
  });
</script>

<div bind:this={mapEl} style="height: 600px; width: 100%;"></div>