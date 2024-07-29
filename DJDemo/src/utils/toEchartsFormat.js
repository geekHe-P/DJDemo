// 转换 JSON 数据为 ECharts 需要的格式

function echartsFormat(json) {
    // 使用 for 循环遍历 json 对象的键
    const echartsFormat = Object.entries(json).map(([name, value]) => ({
        value,
        name
    }));

    // 按照 value 升序排序
    echartsFormat.sort((a, b) => a.value - b.value);
    // console.log(echartsFormat)
    return echartsFormat
}

export default echartsFormat
