/* Javascript for JennytreeXBlock. */
function JennytreeXBlock(runtime, element) {
    #����jstreeĿ¼��
    function jstreeGen(result) {
        $('#jstree',element).jstree({
            'core' : {
                'data' :result

            },
            "themes" : {
                "theme" : "classic",
                "dots" : true,
                "icons" : true
            },
            "plugins" : [
                "themes","json_data", "ui","types","dnd"
            ]
        })
            .on('changed.jstree', function (e, data) {
                path=base+data.instance.get_path(data.selected[0],"/",0);
                document.getElementById('choosenfilename').value=data.instance.get_node(data.selected[0]).text;
            });
    }

    var handlerUrl = runtime.handlerUrl(element, 'getJson');
   
    #ѡ����lab�󣬰�lab����·����ΪPOST��data������jennytree.py���jetJson����������json����
    $('.selectLab', element).click(function(eventObject) {
        var input = document.getElementById("selectLab");
        var lab = input.options[input.selectedIndex].innerHTML;
        var path="/edx/var/edxapp/staticfiles/ucore/0f28b5d49b3020afeecd95b4009adf4c/ucore_lab/labcodes/"+lab
        $.ajax({
            type: "POST",
            url: handlerUrl,
            data: JSON.stringify({"path":path}),
            success: jstreeGen
        });
    });

    $(function ($) {
        /* Here's where you'd do things on page load. */
    })
}


    
       
       

    function ReadFile(){
        alert(path)
    }

