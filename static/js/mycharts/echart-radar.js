//健康度综合指标雷达图
$(document).ready(function() {
	$.ajax({
		url: "IndexServlet",
		data: {
		},
		type: "POST",
		dataType:"json",
		success:function(data){
			var dom = document.getElementById("radar");
			var myChart = echarts.init(dom);
			var app = {};

			var option;


// Schema:

			var dataNJ = [
				[100.0, 100.0, 320.0, 100.0, 100.0]
			];

			var dataShenZ = [
				[63.94, 64.95, 317.0, 100.0, 96.61]
			];

			var dataSH = [
				[50.0, 100.0, 320.0, 100.0, 100.0],
			];

			var dataSuZ = [
				[93.27, 100.0, 320.0, 100.0, 100.0]
			];

			var lineStyle = {
				normal: {
					width: 1,
					opacity: 0.7
				}
			};

			option = {
				backgroundColor: '#fff',
				title: {
					text: 'AQI - 雷达图',
					left: 'center',
					textStyle: {
						color: '#333'
					}
				},
				legend: {
					bottom: 5,
					data: ['南京', '深圳', '上海', '苏州'],
					itemGap: 20,
					textStyle: {
						color: '#333',
						fontSize: 14
					},
					selectedMode: 'single'
				},
				// visualMap: {
				// 	show: true,
				// 	min: 0,
				// 	max: 20,
				// 	dimension: 6,
				// 	inRange: {
				// 		colorLightness: [0.5, 0.8]
				// 	}
				// },
				radar: {
					indicator: [
						{ name: '信号与干扰(coverage)', max: 100 },
						{ name: '接入成功率（successCon）', max: 100 },
						{ name: '接入耗时（timeCon）', max: 1000 },
						{ name: '吞吐达标率（throughput）', max: 100 },
						{ name: '容量健康度（capacity）', max: 100 },
					],
					shape: 'circle',
					splitNumber: 5,
					name: {
						textStyle: {
							color: '666'
						}
					},
					splitLine: {
						lineStyle: {
							color: [
								'rgba(238, 197, 102, 0.9)', 'rgba(238, 197, 102, 1)',
								'rgba(238, 197, 102, 0.3)', 'rgba(238, 197, 102, 1)',
								'rgba(238, 197, 102, 0.8)', 'rgba(238, 197, 102, 1)'
							].reverse()
						}
					},
					splitArea: {
						show: false
					},
					axisLine: {
						lineStyle: {
							color: 'rgba(228, 197, 102, 0.7)'
						}
					}
				},
				series: [
					{
						name: '南京',
						type: 'radar',
						lineStyle: lineStyle,
						data: dataNJ,
						symbol: 'none',
						itemStyle: {
							color: '#F9713C'
						},
						areaStyle: {
							opacity: 0.1
						}
					},
					{
						name: '上海',
						type: 'radar',
						lineStyle: lineStyle,
						data: dataSH,
						symbol: 'none',
						itemStyle: {
							color: '#B3E4A1'
						},
						areaStyle: {
							opacity: 0.1
						}
					},
					{
						name: '深圳',
						type: 'radar',
						lineStyle: lineStyle,
						data: dataShenZ,
						symbol: 'none',
						itemStyle: {
							color: 'rgb(238, 197, 102)'
						},
						areaStyle: {
							opacity: 0.1
						}
					},
					{
						name: '苏州',
						type: 'radar',
						lineStyle: lineStyle,
						data: dataSuZ,
						symbol: 'none',
						itemStyle: {
							color: 'rgb(238, 52, 12)'
						},
						areaStyle: {
							opacity: 0.1
						}
					}
				]
			};

			if (option && typeof option === 'object') {
				myChart.setOption(option);
			}

		}

	});
});
