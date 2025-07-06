<script>
  import { onMount } from 'svelte';
  import Chart from 'chart.js/auto';

  let chart;

  onMount(async () => {
    const res = await fetch('/api/dashboard/stats');
    const data = await res.json();
    const ctx = document.getElementById('statsChart');
    chart = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['Open', 'Triaged', 'In Progress', 'Done'],
        datasets: [{
          label: 'Issues by Status',
          data: [data.open, data.triaged, data.in_progress, data.done],
          backgroundColor: ['red', 'orange', 'blue', 'green']
        }]
      }
    });
  });
</script>

<canvas id="statsChart" width="400" height="200"></canvas>
