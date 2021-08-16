$(document).ready(function() {
    $.ajax({
        url: "IndexServlet",
        data: {
        },
        type: "POST",
        dataType:"json",
        success:function(data){
            htmlLegendsChart = document.getElementById('htmlLegendsChart1').getContext('2d');
// Chart with HTML Legends

            var gradientStroke = htmlLegendsChart.createLinearGradient(500, 0, 100, 0);
            gradientStroke.addColorStop(0, '#177dff');
            gradientStroke.addColorStop(1, '#80b6f4');

            var gradientFill = htmlLegendsChart.createLinearGradient(500, 0, 100, 0);
            gradientFill.addColorStop(0, "rgba(23, 125, 255, 0.7)");
            gradientFill.addColorStop(1, "rgba(128, 182, 244, 0.3)");

            var gradientStroke2 = htmlLegendsChart.createLinearGradient(500, 0, 100, 0);
            gradientStroke2.addColorStop(0, '#f3545d');
            gradientStroke2.addColorStop(1, '#ff8990');

            var gradientFill2 = htmlLegendsChart.createLinearGradient(500, 0, 100, 0);
            gradientFill2.addColorStop(0, "rgba(243, 84, 93, 0.7)");
            gradientFill2.addColorStop(1, "rgba(255, 137, 144, 0.3)");

            var gradientStroke3 = htmlLegendsChart.createLinearGradient(500, 0, 100, 0);
            gradientStroke3.addColorStop(0, '#fdaf4b');
            gradientStroke3.addColorStop(1, '#ffc478');

            var gradientFill3 = htmlLegendsChart.createLinearGradient(500, 0, 100, 0);
            gradientFill3.addColorStop(0, "rgba(253, 175, 75, 0.7)");
            gradientFill3.addColorStop(1, "rgba(255, 196, 120, 0.3)");

            var myHtmlLegendsChart = new Chart(htmlLegendsChart, {
                type: 'line',
                data: {
                    labels: ['2021-06/22/21-18:00:00',
                        '2021-06/22/21-19:00:00',
                        '2021-06/22/21-20:00:00',
                        '2021-06/22/21-21:00:00',
                        '2021-06/22/21-22:00:00',
                        '2021-06/22/21-23:00:00',
                        '2021-06/23/21-00:00:00',
                        '2021-06/23/21-01:00:00',
                        '2021-06/23/21-02:00:00',
                        '2021-06/23/21-03:00:00',
                        '2021-06/23/21-04:00:00',
                        '2021-06/23/21-05:00:00',
                        '2021-06/23/21-06:00:00',
                        '2021-06/23/21-07:00:00',
                        '2021-06/23/21-08:00:00',
                        '2021-06/23/21-09:00:00',
                        '2021-06/23/21-10:00:00',
                        '2021-06/23/21-11:00:00',
                        '2021-06/23/21-12:00:00',
                        '2021-06/23/21-13:00:00',
                        '2021-06/23/21-14:00:00',
                        '2021-06/23/21-15:00:00',
                        '2021-06/23/21-16:00:00',
                        '2021-06/23/21-17:00:00',
                        '2021-06/23/21-18:00:00'],
                    datasets: [{
                        label: "coverage",
                        borderColor: gradientStroke2,
                        pointBackgroundColor: gradientStroke2,
                        pointRadius: 0,
                        backgroundColor: gradientFill2,
                        legendColor: '#f3545d',
                        fill: true,
                        borderWidth: 1,
                        data: [50.62,
                            50.57,
                            50.52,
                            50.64,
                            100,
                            100,
                            70,
                            90.52,
                            50,
                            50,
                            50,
                            50,
                            50,
                            49.69,
                            49.3,
                            50,
                            50,
                            50.62,
                            50.57,
                            50.52,
                            50.64,
                            100,
                            100,
                            70,
                            90.52]
                    }, {
                        label: "rate",
                        borderColor: gradientStroke3,
                        pointBackgroundColor: gradientStroke3,
                        pointRadius: 0,
                        backgroundColor: gradientFill3,
                        legendColor: '#fdaf4b',
                        fill: true,
                        borderWidth: 1,
                        data: [94.74,
                            94.74,
                            94.73,
                            94.74,
                            70,
                            70.52,
                            92.75,
                            92.4,
                            94.68,
                            94.68,
                            94.68,
                            94.68,
                            94.67,
                            94.15,
                            94.26,
                            94.68,
                            94.68,
                            94.74,
                            94.74,
                            94.73,
                            94.74,
                            70,
                            70.52,
                            92.75,
                            92.4]
                    }, {
                        label: "successCon",
                        borderColor: gradientStroke,
                        pointBackgroundColor: gradientStroke,
                        pointRadius: 0,
                        backgroundColor: gradientFill,
                        legendColor: '#177dff',
                        fill: true,
                        borderWidth: 1,
                        data: [100,
                            100,
                            100,
                            100,
                            0,
                            2.7800000000000002,
                            100,
                            90.24,
                            100,
                            100,
                            100,
                            100,
                            100,
                            100,
                            100,
                            100,
                            100,
                            100,
                            100,
                            100,
                            100,
                            0,
                            2.7800000000000002,
                            100,
                            90.24]
                    }, {
                        label: "throughput",
                        borderColor: "#ffeeff",
                        pointBackgroundColor: "#ffeeff",
                        pointRadius: 0,
                        backgroundColor: "#ffeeff",
                        legendColor: '#ffeeff',
                        fill: true,
                        borderWidth: 1,
                        data: [100,
                            100,
                            100,
                            100,
                            100,
                            100,
                            100,
                            100,
                            100,
                            100,
                            100,
                            100,
                            100,
                            100,
                            100,
                            100,
                            100,
                            100,
                            100,
                            100,
                            100,
                            100,
                            100,
                            100,
                            100]
                    }, {
                        label: "capacity",
                        borderColor: "#ae57",
                        pointBackgroundColor: "#ae57",
                        pointRadius: 0,
                        backgroundColor: "#ae57",
                        legendColor: '#ae57',
                        fill: true,
                        borderWidth: 1,
                        data: [100,
                            100,
                            100,
                            100,
                            100,
                            100,
                            73.74,
                            77.39,
                            100,
                            100,
                            100,
                            100,
                            99.92,
                            96.65,
                            97.66,
                            100,
                            100,
                            100,
                            100,
                            100,
                            100,
                            100,
                            100,
                            73.74,
                            77.39]

                    }, {
                        borderColor: "#fff",
                        pointBackgroundColor: "#fff",
                        pointRadius: 0,
                        backgroundColor: "#fff",
                        legendColor: '#fff',
                        fill: true,
                        borderWidth: 1,
                        data: [150]
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    legend: {
                        display: false
                    },
                    tooltips: {
                        bodySpacing: 4,
                        mode: "nearest",
                        intersect: 0,
                        position: "nearest",
                        xPadding: 10,
                        yPadding: 10,
                        caretPadding: 10
                    },
                    layout: {
                        padding: { left: 15, right: 15, top: 15, bottom: 15 }
                    },
                    scales: {
                        yAxes: [{
                            ticks: {
                                fontColor: "rgba(0,0,0,0.5)",
                                fontStyle: "500",
                                beginAtZero: false,

                                padding: 20
                            },
                            gridLines: {
                                drawTicks: false,
                                display: false
                            }
                        }],
                        xAxes: [{
                            gridLines: {
                                zeroLineColor: "transparent"
                            },
                            ticks: {
                                padding: 20,
                                fontColor: "rgba(0,0,0,0.5)",
                                fontStyle: "500"
                            }
                        }]
                    },
                    legendCallback: function (chart) {
                        var text = [];
                        text.push('<ul class="' + chart.id + '-legend html-legend">');
                        for (var i = 0; i < chart.data.datasets.length; i++) {
                            text.push('<li><span style="background-color:' + chart.data.datasets[i].legendColor + '"></span>');
                            if (chart.data.datasets[i].label) {
                                text.push(chart.data.datasets[i].label);
                            }
                            text.push('</li>');
                        }
                        text.push('</ul>');
                        return text.join('');
                    }
                }
            });

            var myLegendContainer = document.getElementById("myChartLegend");

// generate HTML legend
            myLegendContainer.innerHTML = myHtmlLegendsChart.generateLegend();

// bind onClick event to all LI-tags of the legend
            var legendItems = myLegendContainer.getElementsByTagName('li');
            for (var i = 0; i < legendItems.length; i += 1) {
                legendItems[i].addEventListener("click", legendClickCallback, false);
            }

        }

    });
});
