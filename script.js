function date() {
    var startDate = new Date(2025, 0, 14); // 起始日期（2025年1月14日，月份从0开始）
    var currentDate = new Date(); // 当前日期
    var diff = currentDate - startDate; // 时间差（单位：毫秒）

    var days = Math.floor(diff / (1000 * 60 * 60 * 24)); // 计算天数差
    var years = Math.floor(days / 365); // 计算年数
    days -= years * 365; // 剩余天数

    var months = Math.floor(days / 30); // 计算月数（假设每月30天）
    days -= months * 30; // 剩余天数

    var text = '网站已运行' + years + '年' + months + '月' + days + '天';
    return text;
}