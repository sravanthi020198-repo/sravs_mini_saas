<script>
  import { onMount } from 'svelte';
  let issues = [];
  onMount(async () => {
    const res = await fetch('/api/issues');
    issues = await res.json();
  });
</script>

<h1 class="text-xl font-bold">Issue List</h1>
<ul>
  {#each issues as issue}
    <li class="p-2 border-b">{issue.title} - {issue.status}</li>
  {/each}
</ul>
