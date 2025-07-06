<script lang="ts">
  import { onMount } from 'svelte';
  let issues = [];
  let ws;
  onMount(() => {
    fetch('/api/issues').then(res => res.json()).then(data => issues = data);
    ws = new WebSocket('ws://localhost:8000/ws/issues');
    ws.onmessage = (event) => {
      // update issues list on message
      fetch('/api/issues').then(res => res.json()).then(data => issues = data);
    };
    return () => ws && ws.close();
  });
</script>

<h1>Issues</h1>
<ul>
  {#each issues as issue}
    <li>{issue.title} ({issue.status})</li>
  {/each}
</ul>
