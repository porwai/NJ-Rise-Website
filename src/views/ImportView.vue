<template>
    <div class="card">
        <div class="card-body d-flex flex-column" style="overflow-y: auto;">
			<h2>Import CSV Data</h2>
            <p>Upload CSV file into Master Database</p>
			<label>
				<input type="file" @change="handleFileUpload( $event )"/>
			</label>
			<br>
            <div class="button">
                <button class="btn btn-primary" v-on:click="submitFile()">Submit</button>
            </div>
		</div>
		<div v-if="fileUploaded" class="card-footer">
          <h3 class="card-title">File has been uploaded</h3>
      </div>
	</div>
</template>

<script>
	import axios from 'axios';
	export default {
		data(){
			return {
				file: '',
				fileUploaded: false
			}
		},
		
		methods: {
			handleFileUpload( event ){
				this.file = event.target.files[0];
			},
			submitFile(){
				let formData = new FormData();
				formData.append('file', this.file);
				axios.post( '/api/importcsv', formData,
					{
						headers: {
								'Content-Type': 'multipart/form-data'
						}
					}
				).then(response =>{
					const output = response.data;
					if (output[0] !== true){
						alert(output[1]);
					}
					else {
						this.fileUploaded = true
					}
				})
				.catch((error) => {
                    console.error(error);
                    // Consider adding user-facing error handling here
                });
			}
		}
	}
</script>