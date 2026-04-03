<script>
  import Map from './Map.svelte';

  let geojson = null;
  let loading = false;
  let error = null;

  async function runDemo() {
    loading = true;
    error = null;
    try {
      const res = await fetch("http://127.0.0.1:8000/demo");
      if (!res.ok) throw new Error("Server error");
      const data = await res.json();
      geojson = JSON.parse(data);
    } catch (e) {
      error = e.message;
    } finally {
      loading = false;
    }
  }
</script>

<h1>Redistricting Validator Demo</h1>
<button on:click={runDemo} disabled={loading}>
  {loading ? "Loading..." : "Run Demo"}
</button>

{#if error}
  <p style="color:red">{error}</p>
{/if}

{#if geojson}
  <Map {geojson} />
{/if}