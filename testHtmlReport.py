#encoding=gbk
class TestHtmlReport:
    HTMLSCRIPt = """
function show(obj){
    var ele_log = document.getElementsByName('log');
    var ele_detail = document.getElementsByName("detail");
    var i = ele_log.length;
    while (i--) {
        if (ele_detail[i] ==obj) {
            break
        }
    }
    if (ele_log[i].hasAttribute("hidden")){
          ele_log[i].removeAttribute("hidden");
          ele_detail[i].innerHTML="����";
    }else {
          ele_detail[i].innerHTML="��ϸ";
          ele_log[i].setAttribute("hidden","true");
    }
}
function show_pass() {
    if (document.getElementById("pass").checked) {
        var eles = document.getElementsByName("rpass")
        var len = eles.length
        var index = 0
        for (index; index < len; index++) {
           eles[index].removeAttribute("hidden")
        }
    }
    else {
        var eles = document.getElementsByName("rpass")
        var len = eles.length
        var index = 0
        for (index; index < len; index++) {
            eles[index].setAttribute("hidden", "true")
        }
    }
}
function show_unpass() {
    if (document.getElementById("unpass").checked) {
        var eles = document.getElementsByName("runpass")
        var len = eles.length
        var index = 0
        for (index; index < len; index++) {
           eles[index].removeAttribute("hidden")
        }
    }
    else {
        var eles = document.getElementsByName("runpass")
        var len = eles.length
        var index = 0
        for (index; index < len; index++) {
            eles[index].setAttribute("hidden", "true")
        }
    }
}
function show_error() {
    if (document.getElementById("error").checked) {
        var eles = document.getElementsByName("rerror")
        var len = eles.length
        var index = 0
        for (index; index < len; index++) {
           eles[index].removeAttribute("hidden")
        }
    }
    else {
        var eles = document.getElementsByName("rerror")
        var len = eles.length
        var index = 0
        for (index; index < len; index++) {
            eles[index].setAttribute("hidden", "true")
        }
    }
}
    """
    HTMLHEAD = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>���Ա���</title>
    <script language="javascript">
{}
</script>
</head>
<body>
 <h1>�Զ������Ա���</h1>
 <p class ="attribute"><strong>�����������{}</strong></p>
 <p class ="attribute"><strong>���Ե�ַ��{}</strong></p>
 <p class ="attribute"><strong>������ʼִ��ʱ�䣺{}</strong></p>
 <p class ="attribute"><strong>�ܼƺ�ʱ��{}</strong></p>
 <p class ="attribute"><strong>���Խ����{}</strong></p>
 <p class ="attribute"><strong>����ִ�������</strong></p>
 <label style="background-color: green;"><input id="pass" checked onclick="show_pass()" type="checkbox" value="" />����ͨ�� : {}&nbsp&nbsp&nbsp </label>
 <label style="background-color: yellow;"><input id="unpass" checked onclick="show_unpass()" type="checkbox" value="" />������ͨ�� : {}&nbsp&nbsp </label>
 <label style="background-color: red;"><input id="error" checked onclick="show_error()" type="checkbox" value="" />�����쳣 : {}&nbsp&nbsp&nbsp </label>
 <table id="result_table" style="text-align: center" width="100%" border="1" cellpadding="2" cellspacing="1">
     <colgroup>
         <col align="left">
         <col align="right">
         <col align="right">
         <col align="right">
         <col align="right">
     </colgroup>
     <tr id ="header_row" style="font-weight: bold;font-size: 16px;">
         <td>����ģ��</td>
         <td>��������</td>
         <td>��־��¼</td>
         <td>�ķ�ʱ��</td>
         <td>���</td>
     </tr>
    """
    HTMLROWPASS="""
     <tr name="rpass">
         <td>{}</td>
         <td>{}</td>
         <td><a href="javascript:void(0)" onclick="show(this)" style="text-align: center" name="detail">��ϸ</a>
             <pre name="log" style="text-align: left" hidden="true">
{}
         </pre>
         </td>
         <td>{}</td>
         <td style="background-color: green">{}</td>
     </tr>
     """
    HTMLROWUNPASS="""
<tr name="runpass">
         <td>{}</td>
         <td>{}</td>
         <td><a href="javascript:void(0)" onclick="show(this)" style="text-align: center" name="detail">��ϸ</a>
             <pre name="log" style="text-align: left" hidden="true">
{}
         </pre>
         </td>
         <td>{}</td>
         <td style="background-color: yellow">{}</td>
     </tr>
    """
    HTMLROWERROR="""
<tr name="rerror">
         <td>{}</td>
         <td>{}</td>
         <td><a href="javascript:void(0)" onclick="show(this)" style="text-align: center" name="detail">��ϸ</a>
             <pre name="log" style="text-align: left" hidden="true">
{}
         </pre>
         </td>
         <td>{}</td>
         <td style="background-color: red">{}</td>
     </tr>
    """
    HTMLEND="""
 </table>
</body>
</html>
    """
