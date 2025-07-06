<script lang="ts">
  import { onMount } from 'svelte';
  import Chart from 'chart.js/auto';
  let chartDiv;
  onMount(async () => {
    const res = await fetch('/api/stats/open_severity');
    const data = await res.json();
    const ctx = chartDiv.getContext('2d');
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: data.labels,
        datasets: [{
          label: 'Open Issues by Severity',
          data: data.counts,
        }]
      }
    });
  });
</script>
<canvas bind:this={chartDiv}></canvas>
