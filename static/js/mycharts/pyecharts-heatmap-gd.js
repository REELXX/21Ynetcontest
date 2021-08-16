
var chart_6a7c753f18d04e8585e1827c1af1bb60 = echarts.init(
    document.getElementById('6a7c753f18d04e8585e1827c1af1bb60'), 'light', { renderer: 'canvas' });
var option_6a7c753f18d04e8585e1827c1af1bb60 = {
    "animation": true,
    "animationThreshold": 2000,
    "animationDuration": 1000,
    "animationEasing": "cubicOut",
    "animationDelay": 0,
    "animationDurationUpdate": 300,
    "animationEasingUpdate": "cubicOut",
    "animationDelayUpdate": 0,
    "series": [
        {
            "type": "effectScatter",
            "coordinateSystem": "geo",
            "showEffectOn": "render",
            "rippleEffect": {
                "show": true,
                "brushType": "stroke",
                "scale": 2.5,
                "period": 4
            },
            "symbolSize": 12,
            "data": [
                {
                    "name": "\u6df1\u5733",
                    "value": [
                        114.07,
                        22.62,
                        348
                    ]
                }
            ],
            "label": {
                "show": false,
                "position": "top",
                "margin": 8
            }
        }
    ],
    "legend": [
        {
            "data": [
                ""
            ],
            "selected": {
                "": true
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
        "formatter": function (params) { return params.name + ' : ' + params.value[2]; },
        "textStyle": {
            "fontSize": 14
        },
        "borderWidth": 0,
        "padding": 5
    },
    // "title": [
    //     {
    //         "text": "\u533a\u57df\u8bbe\u5907\u6570\u91cf",
    //         "subtext": "\u66f4\u65b0\u65e5\u671f:2021-4-5",
    //         "sublink": "http://tianqi.2345.com/air-rank.html",
    //         "left": "center",
    //         "padding": 5,
    //         "itemGap": 10
    //     }
    // ],
    "visualMap": {
        "show": true,
        "type": "piecewise",
        "min": 0,
        "max": 1000,
        "text": [
            "\u8bbe\u5907\u6570\u91cf",
            ""
        ],
        "inRange": {
            "color": [
                "#50a3ba",
                "#eac763",
                "#d94e5d"
            ]
        },
        "calculable": true,
        "inverse": false,
        "splitNumber": 4,
        "orient": "vertical",
        "left": "20%",
        "top": "70%",
        "showLabel": true,
        "itemWidth": 20,
        "itemHeight": 14,
        "borderWidth": 0,
        "pieces": [
            {
                "min": 500,
                "max": 1000,
                "color": "#ec5858",
                "label": "500\u4ee5\u4e0a"
            },
            {
                "min": 300,
                "max": 500,
                "color": "#fd8c04",
                "label": "300~500"
            },
            {
                "min": 100,
                "max": 300,
                "color": "#b8de6f",
                "label": "100~300"
            },
            {
                "min": 0,
                "max": 100,
                "color": "#32e0c4",
                "label": "100\u4ee5\u4e0b"
            }
        ]
    },
    "geo": {
        "map": "\u5e7f\u4e1c",
        "roam": true,
        "aspectScale": 0.75,
        "nameProperty": "name",
        "selectedMode": false,
        "itemStyle": {
            "color": "#fff",
            "borderColor": "#9ba4b4"
        },
        "emphasis": {}
    }
};
chart_6a7c753f18d04e8585e1827c1af1bb60.setOption(option_6a7c753f18d04e8585e1827c1af1bb60);