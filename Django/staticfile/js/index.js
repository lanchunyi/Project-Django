var echarts_wg = echarts.init(document.getElementById('myechart'))
echarts_wg.showLoading();
var option = {
    title: {
        text: "我的工作量统计"
    },
    legend: {
        data: ['具体工作数量']
    },
    xAxis: {
        data: ['1','2','3','4','5']
    },
    yAxis: {

    },
    series: [{
        name: '工作量',
        type: 'bar',
        data: [10,20,30,15,5]
    }]
};
echarts_wg.hideLoading();
echarts_wg.setOption(option);