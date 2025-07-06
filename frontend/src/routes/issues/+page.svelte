<script>
  import { onMount } from 'svelte';
  import { browser } from '$app/environment';

  let issues = [];
  let ws;

  async function fetchIssues() {
    const res = await fetch('/api/issues');
    issues = await res.json();
  }

  onMount(() => {
    fetchIssues();

    if (browser) {
      ws = new WebSocket('ws://localhost:8000/ws/issues');
      ws.onmessage = (event) => {
        if (event.data === 'refresh') {
          fetchIssues();
        }
      };
    }
  });
</script>

<h1 class="text-xl font-bold">Issue List</h1>
<ul>
  {#each issues as issue}
    <li class="p-2 border-b">{issue.title} - {issue.status}</li>
  {/each}
</ul>
