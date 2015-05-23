/* Javascript for JennytreeXBlock. */
function JennytreeXBlock(runtime, element) {

    function updateCount(result) {
        $('.count', element).text(result.count);
    }

    var handlerUrl = runtime.handlerUrl(element, 'increment_count');

    $('p', element).click(function(eventObject) {
        $.ajax({
            type: "POST",
            url: handlerUrl,
            data: JSON.stringify({"hello": "world"}),
            success: updateCount
        });
    });

    $(function ($) {
        /* Here's where you'd do things on page load. */
    })
}


    function selectLab() {
        base="";
        path="";
        var input = document.getElementById("selectLab");
        var lab = input.options[input.selectedIndex].innerHTML;
        base+=lab;
        base+="/";
        var jsonstr=[{"attributes":{"id":"0"},"parent":"0","state":{"opened":false},"text":"id","children":[{"attributes":{"id":"1"},"parent":"0","state":{"opened":false},"text":"lab1","children":[]},{"attributes":{"id":"2"},"parent":"1","state":{"opened":false},"text":"lab2","children":[]}]},{"attributes":{"id":"3"},"parent":"2","state":{"opened":false},"text":"jstree","children":[{"attributes":{"id":"4"},"parent":"3","state":{"opened":false},"text":"dist","children":[]},{"attributes":{"id":"5"},"parent":"4","state":{"opened":false},"text":"leaf.png","type":"leaf"},{"attributes":{"id":"6"},"parent":"4","state":{"opened":false},"text":"root.json","type":"leaf"}]},{"attributes":{"id":"7"},"parent":"4","state":{"opened":false},"text":"jstree.html","type":"leaf"},{"attributes":{"id":"8"},"parent":"4","state":{"opened":false},"text":"jstree.js","type":"leaf"}];
        //  create an instance when the DOM is readyp
        $('#jstree',element).jstree({
            'core' : {
                'data' :jsonstr

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
    function ReadFile(){
        alert(path)
    }

