---
title: Accumulo Fotovoltaico
subtitle: Piccola analisi sull'opportunità di utilizzare un accumulo fotovoltaico
layout: page
---

# {{page.title}}

Utilizzando i dati di circa 3 anni di funzionamento dei miei pannelli solari (3kW di picco), registrati ogni 15 minuti, ho simulato l'effetto ottenibile dall'inserimento nell'impianto di un accumulo di energia
con capacità via via crescente, fino a dimensioni non praticabili fisicamente con le tecnologie attuali.
Come si può notare, già intorno ai 5kWh di accumulo si ottiene un dimezzamento della quantità di energia totale comprata o venduta. Oltre questo valore, si ha un ulteriore diminuzione al crescere della
capacità, finché a 2621.44kWh di accumulo si ottiene che l'energia non viene più venduta, ma allo stesso tempo resta una quantità non abbattibile di energia da acquistare dal gestore per
rispondere alla domanda dell'impianto.

<div markdown="0">
<canvas id="myChart" width="400" height="400"></canvas>
<script>
var ctx = document.getElementById("myChart");
var myChart = new Chart(ctx, {
type: 'line',

data: {
labels: [
{% for member in site.data.results %}
{{member.capacity}},
{% endfor %}
],


datasets: [{
label: 'Sold',
data: [
{% for member in site.data.results %}
{{member.sold_with}},
{% endfor %}
],
backgroundColor: [
'rgba(255, 99, 132, 0.2)',
],
        borderColor: [
                'rgba(255,99,132,1)',
        ],
        borderWidth: 1
        },
{
label: 'Bought',
       data: [
       {% for member in site.data.results %}
       {{member.bought_with}},
               {% endfor %}
       ],
       backgroundColor: [
               'rgba(54, 162, 235, 1)',
       ],
       borderColor: [
               'rgba(54, 162, 235, 1)',
       ],
       borderWidth: 1
}
]
},
options: {
title: {
display: true,
         text: 'Bought/Sold vs Capacity'
       },
scales: {
yAxes: [{
ticks: {
beginAtZero:true
       }
       }],
xAxes: [{
scaleLabel: {
display: true,
         labelString: 'Capacity [kWh]'
            }
       }]
        }
         }
});
</script>
</div>


Lo script usato per l'analisi e i dati si possono trovare sul [repo Github](https://github.com/mfortini/AccumuloFotovoltaico). I dati sono rilasciati con licenza ODBL.
