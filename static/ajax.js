/**
 * Created by zhangjun on 15/6/19.
 */

//修改
function mModel(ip,n_ip,status) {
    $('#mModal').modal();
    $('#mip').val(ip);
    $('#mn_ip').val(n_ip);
    //$('#mstatus').val(status);
}

function modModel() {
    var ip = $('#mip').val();
    //var status = $('#mstatus').val();
    var status = $('#xx option:selected').val();
    if (status == '') {
        alert("请选择机器状态 或者 取消当前操作！！！");
    }
    if (status != '') {
        window.location.href = "/mod?ip=" + ip + "&status=" + status;
    }
}

//添加
function aModel() {
    $('#addModal').modal();
}

function addModel() {
    var ip = $('#ip').val();
    var n_ip = $('#n_ip').val();
    var c_room = $('#c_room').val();
    var operator = $('#operator').val();
    var status = $('#status').val();
    if (ip == '') {
        alert("IP 不能为空！！！")

    }
    if (ip != '') {
        window.location.href = "/add?ip=" + ip + "&n_ip=" + n_ip + "&c_room=" + c_room + "&operator=" + operator + "&status=" + status;
    }
}

//删除
function dModel(ip) {
    $('#delModal').modal(); //打开模态框
    $('#info').val(ip);
}

function delModel() {
    var ip = $('#info').val(); //根据id获取模态框中的值
    window.location.href="/delete_ip?ip=" + ip;
}

//搜索
function sModel() {
    var content = $('#s_ip').val();
    if (content == '') {
        window.location.href = "/";
    }
    if (content != '') {
        window.location.href = "/search_ip?ip=" + content;
    }
}