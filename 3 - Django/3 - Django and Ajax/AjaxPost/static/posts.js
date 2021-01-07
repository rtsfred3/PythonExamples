function appendPosts(data){
  $('#posts').append('<div class="post-box">' + data['fields']['post'] + '</div>');
}

function modifyPosts(data){
  $('#posts').html("");
  for(var i = 0; i < data.length; i++){
    appendPosts(data[i]);
  }
}

function getPosts(){
  $.ajax({
    url: 'all_json',
    method: 'get',
    success: function(serverResponse) {
      modifyPosts(serverResponse);
    }
  });
}

$(document).ready(function() {
  getPosts();
});

$('#post_form').submit(function(e){
        e.preventDefault();
        console.log('Sending Ajax request to', $(this).attr('action'));
        console.log('Submitting the following data', $(this).serialize());
        $.ajax({
          url: $(this).attr('action'),
          method: 'post',
          data: $(this).serialize(),
          success: function(serverResponse) {
            appendPosts(serverResponse[serverResponse.length - 1]);
            $('#post_location').val("");
          }
        })
      });
