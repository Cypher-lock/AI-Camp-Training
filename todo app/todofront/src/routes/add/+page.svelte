<script>
	var res = "...", prompt = "";

    async function doPost () {
		const res = await fetch('http://localhost:8000' + '/input/', {
			method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
			body: JSON.stringify({
				"newItem":prompt
			})
		})
		
		const json = await res.json()
	}

    function onSubmit() {
        event.preventDefault();
		doPost();
    };
</script>

<div class="container mx-auto max-w-3xl mt-20 px-5">
	<form on:submit={onSubmit} class="mb-10">
		<label for="prompt" class="block text-2xl font-bold mb-3">
			Enter new task
		</label>
		<input 
			type="text" 
			name="prompt" 
			id="prompt" 
			placeholder="..."
			bind:value={prompt}
			class="w-full mb-5 rounded bg-slate-200 p-2"
			on:change={e => prompt = e.target.value}
		/>
		<button 
			class="px-5 py-3 rounded bg-slate-600 text-white block ml-auto"               
		>
			Submit!
		</button>
	</form>
</div>