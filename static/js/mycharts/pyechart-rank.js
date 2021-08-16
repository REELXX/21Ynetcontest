//站点健康度排名
$(document).ready(function() {
    $.ajax({
        url: "IndexServlet",
        data: {
        },
        type: "POST",
        dataType:"json",
        success:function(data){
            var chart_9ad4f64b0b0c45638b323bef661ad98e = echarts.init(
                document.getElementById('9ad4f64b0b0c45638b323bef661ad98e'), 'white', { renderer: 'canvas' });
            var option_9ad4f64b0b0c45638b323bef661ad98e = {
                "animation": true,
                "animationThreshold": 2000,
                "animationDuration": 1000,
                "animationEasing": "cubicOut",
                "animationDelay": 0,
                "animationDurationUpdate": 300,
                "animationEasingUpdate": "cubicOut",
                "animationDelayUpdate": 0,
                "color": [
                    // "#c23531",
                    // "#2f4554",
                    // "#61a0a8",
                    // "#d48265",
                    // "#749f83",
                    // "#ca8622",
                    // "#bda29a",
                    // "#6e7074",
                    // "#546570",
                    // "#c4ccd3",
                    // "#f05b72",
                    // "#ef5b9c",
                    // "#f47920",
                    // "#905a3d",
                    "#fab27b",
                    "#2a5caa",
                    "#444693",
                    "#726930",
                    "#b2d235",
                    "#6d8346",
                    "#ac6767",
                    "#1d953f",
                    "#6950a1",
                    "#918597"
                ],
                "series": [
                    {
                        "type": "bar",
                        "name": "\u5065\u5eb7\u5ea6\u603b\u6307\u6807",
                        "legendHoverLink": true,
                        "data": [
                            65.32,
                            100.0,
                            100.0,
                            100.0
                        ],
                        "showBackground": false,
                        "barMinHeight": 0,
                        "barCategoryGap": "50%",
                        "barGap": "0%",
                        "large": false,
                        "largeThreshold": 1,
                        "seriesLayoutBy": "column",
                        "datasetIndex": 0,
                        "clip": true,
                        "zlevel": 0,
                        "z": 2,
                        "label": {
                            "show": true,
                            "position": "right",
                            "margin": 8
                        },
                        "rippleEffect": {
                            "show": true,
                            "brushType": "stroke",
                            "scale": 2.5,
                            "period": 4
                        }
                    },
                    // {
                    //     "type": "bar",
                    //     "name": "association",
                    //     "legendHoverLink": true,
                    //     "data": [
                    //         99.57,
                    //         92.57,
                    //         99.57,
                    //         99.57
                    //     ],
                    //     "showBackground": false,
                    //     "barMinHeight": 0,
                    //     "barCategoryGap": "20%",
                    //     "barGap": "30%",
                    //     "large": false,
                    //     "largeThreshold": 400,
                    //     "seriesLayoutBy": "column",
                    //     "datasetIndex": 0,
                    //     "clip": true,
                    //     "zlevel": 0,
                    //     "z": 2,
                    //     "label": {
                    //         "show": true,
                    //         "position": "right",
                    //         "margin": 8
                    //     },
                    //     "rippleEffect": {
                    //         "show": true,
                    //         "brushType": "stroke",
                    //         "scale": 2.5,
                    //         "period": 4
                    //     }
                    // },
                    // {
                    //     "type": "bar",
                    //     "name": "authentication",
                    //     "legendHoverLink": true,
                    //     "data": [
                    //         48.54,
                    //         98.54,
                    //         98.54,
                    //         98.54
                    //     ],
                    //     "showBackground": false,
                    //     "barMinHeight": 0,
                    //     "barCategoryGap": "20%",
                    //     "barGap": "30%",
                    //     "large": false,
                    //     "largeThreshold": 400,
                    //     "seriesLayoutBy": "column",
                    //     "datasetIndex": 0,
                    //     "clip": true,
                    //     "zlevel": 0,
                    //     "z": 2,
                    //     "label": {
                    //         "show": true,
                    //         "position": "right",
                    //         "margin": 8
                    //     },
                    //     "rippleEffect": {
                    //         "show": true,
                    //         "brushType": "stroke",
                    //         "scale": 2.5,
                    //         "period": 4
                    //     }
                    // }
                ],
                "legend": [
                    {
                        "data": [
                            "\u5065\u5eb7\u5ea6\u603b\u6307\u6807",
                            // "association",
                            // "authentication"
                        ],
                        "selected": {
                            "\u5065\u5eb7\u5ea6\u603b\u6307\u6807": true,
                            // "association": true,
                            // "authentication": true
                        },
                        "show": true,
                        "padding": 5,
                        "itemGap": 10,
                        "itemWidth": 25,
                        "itemHeight": 14
                    }
                ],
                "tooltip": {
                    "show": true,
                    "trigger": "item",
                    "triggerOn": "mousemove|click",
                    "axisPointer": {
                        "type": "line"
                    },
                    "showContent": true,
                    "alwaysShowContent": false,
                    "showDelay": 0,
                    "hideDelay": 100,
                    "textStyle": {
                        "fontSize": 14
                    },
                    "borderWidth": 0,
                    "padding": 5
                },
                "xAxis": [
                    {
                        "show": false,
                        "scale": false,
                        "nameLocation": "end",
                        "nameGap": 15,
                        "gridIndex": 0,
                        "inverse": false,
                        "offset": 0,
                        "splitNumber": 10,
                        "minInterval": 0,
                        "splitLine": {
                            "show": false,
                            "lineStyle": {
                                "show": true,
                                "width": 1,
                                "opacity": 1,
                                "curveness": 0,
                                "type": "solid"
                            }
                        }
                    }
                ],
                "yAxis": [
                    {
                        "show": true,
                        "scale": false,
                        "nameLocation": "end",
                        "nameGap": 15,
                        "gridIndex": 0,
                        "inverse": false,
                        "offset": 0,
                        "splitNumber": 5,
                        "minInterval": 0,
                        "splitLine": {
                            "show": false,
                            "lineStyle": {
                                "show": true,
                                "width": 1,
                                "opacity": 1,
                                "curveness": 0,
                                "type": "solid"
                            }
                        },
                        "data": [

                            "\u6df1\u5733",
                            "\u5357\u4eac",
                            "\u82cf\u5dde",
                            "\u4e0a\u6d77"
                        ]
                    }
                ],
                // "title": [
                // 	{
                // 		"text": "\u533a\u57df\u7f51\u7edc\u5065\u5eb7\u5ea6\u6392\u540d",
                // 		"padding": 5,
                // 		"itemGap": 10
                // 	}
                // ]
            };
            chart_9ad4f64b0b0c45638b323bef661ad98e.setOption(option_9ad4f64b0b0c45638b323bef661ad98e);

        }

    });
});
