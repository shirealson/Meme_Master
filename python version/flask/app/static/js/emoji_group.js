function create_emojiGroup(group_id){
    var new_Object = {
        group_id : group_id,
        group_loaded_group : 0,
        group_loaded_index : 0,
        eachUpdateNum : 10,
        change_group : function(){
            this.group_loaded_group = 0;
            this.group_loaded_index = 0;
            $.ajax({
                type:'GET',
                url:'localhost:7777/' + this.group_id + "/" + (this.group_loaded_group + 1) * this.eachUpdateNum,
                dataType:'jsonp',//改成了jsonp格式，解决了跨域访问的问题
                success:function(data){
                    return [1,data];
                },
                error:function(jqXHR){
                    return [-1,jqXHR.status];
                }
            })

        },
        get_more_group : function(){
            var request = new XMLHttpRequest();
	        request.open("GET", "localhost:7777/" + this.group_id + "/" + (this.group_loaded_group + 1) * this.eachUpdateNum);
	        request.send();
	        request.onreadystatechange = function() {
		    if (request.readyState===4) {
                if (request.status===200) { 
				    data = request.responseText;
                    dataJSON = JSON.parse(data);
                    group_loaded_group += 1;//已经加载了的组+1

                    return dataJSON;//返回json结果
                        
                } 
                else return -1;//错误代码
                }
            }
        },
    }
    return new_Object;
}
