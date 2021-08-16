//用户满意度占比
var chart_4b1609a1e9104d049e0acd026a8e1643 = echarts.init(
    document.getElementById('yonghu'), 'white', { renderer: 'canvas' });
var option_4b1609a1e9104d049e0acd026a8e1643 = {
    "animation": true,
    "animationThreshold": 2000,
    "animationDuration": 1000,
    "animationEasing": "cubicOut",
    "animationDelay": 0,
    "animationDurationUpdate": 300,
    "animationEasingUpdate": "cubicOut",
    "animationDelayUpdate": 0,
    "color": [
        "#2f4554",
        "#ffffff",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
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
            "type": "pie",
            "name": "用户数",
            "clockwise": true,
            "data": [
                {
                    "name": "用户数",
                    "value": 478
                },
                {
                    "name": "",
                    "value": 22
                }
            ],
            "radius": [
                "60%",
                "90%"
            ],
            "center": [
                "50%",
                "50%"
            ],
            "label": {
                "show": true,
                "position": "center",
                "margin": 8,
                "formatter": "478",
                textStyle: {
                    fontSize:50,
                    color: "#2f4554"
                }
            }
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
    }
};
chart_4b1609a1e9104d049e0acd026a8e1643.setOption(option_4b1609a1e9104d049e0acd026a8e1643);

