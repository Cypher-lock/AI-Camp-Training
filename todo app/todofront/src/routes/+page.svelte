<script>
	import { onMount } from 'svelte';

	let date = (new Date()).toLocaleTimeString();

    var res = "...", prompt = "";


    const url = 'http://localhost:8000' + '/output/';
    const options = {
        method: 'GET',
    };

    let tabledata = [];
    let tasks = [];
    async function fetchdata(){
        const res = await fetch(url, options);
        const data = await res.json();
        console.log('Fetched Data:', data); 
        tabledata = data;
        tabledata = JSON.parse(tabledata);

        tasks = tabledata.map(item => ({
        task: item.fields.task,
        date_added: item.fields.date_added
        }));
        console.log('new Fetched Data:', tabledata); 
  }

  fetchdata();
  
  onMount(() => {
	    let interval = setInterval(() => {
			date = new Date().toLocaleTimeString();
		}, 1000);

		return () => {
			clearInterval(interval);
		};
	});

    function onClick(){

    }

</script>

<div class="container mx-auto max-w-3xl mt-20 px-5">
    <div>
        <h1>Current Time:</h1>
        <p>{date}</p>
    </div>
        <h2>Task List</h2>
        <table>
            <thead>
                <tr>
                    <!-- Adjust column headers based on your data -->
                    <th class="p-2 border-b">Task</th>
                    <th class="p-2 border-b">Start Date</th>
                </tr>
            </thead>
            <tbody>
                    <tr>
                        <!-- Adjust table cells based on your data structure -->
                        <table>
                       {#each tasks as els}
                       <tr></tr>
                            <td>{els.task}</td>
                            <td>{els.date_added}</td>
                            <button on:click={onClick()}>Delete</button>
                        {/each}
                        </table>
                    </tr>
            </tbody>
        </table>
</div>

