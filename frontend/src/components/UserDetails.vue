<!-- UserDetails.vue -->

<template>
    <div class = "container-fluid">
        <h1>John Doe</h1>
        <h2>123456789</h2>
        <div class = "table-responsive" style="max-height: 300px; overflow-y: scroll;">

<!-- very inefficient - vue is not good with tables with column headers -->
<b-table class = "table table-striped">
    <tbody>
        <tr v-for="detail in details" :key="detail.clientid">
            <td><b> phone </b></td>
            <td> {{detail.phone}} </td>
        </tr>
        <tr v-for="detail in details" :key="detail.clientid">
            <td><b> dependents </b></td>
            <td> {{detail.dependents}} </td>
        </tr>
    </tbody>
</b-table>
</div>

<h2>Visitation Log</h2>
        <div class = "table-responsive" style="max-height: 300px; overflow-y: scroll;">

        <b-table class ="table table-striped">
            <thead>
                <tr>
                    <th>Date/Time</th>
                    <th>Weekday</th>
                    <th>Food Bags</th>
                    <th>Baby Supplies</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="client in clients" :key="client.clientid">
                    <td> {{ client.date }}</td>
                    <td> {{ client.weekday }}</td>
                    <td> {{ client.foodbags }}</td>
                </tr>
            </tbody>
        </b-table>
    </div>
    </div>
</template>

<script>
    export default {
        name: 'userdetails',
        data() {
            return {
                details: [
                    {phone: '019283', dependents: 'wed'}
                ],
                clients: [
                    {date: '019283', weekday: 'wed', foodbags: '5'},
                    {date: '019283', weekday: 'wed', foodbags: '5'},
                    {date: '019283', weekday: 'wed', foodbags: '5'}
                ],
            };
        },
    }
</script>