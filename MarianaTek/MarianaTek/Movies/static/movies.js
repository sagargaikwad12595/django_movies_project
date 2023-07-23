function mySearch() {
    var input = $("#searchMovie").val()
    $.ajax(
        {
            type:"GET",
            url: "/getMatchMovie",
            data:{
                     searchInput: input
            },
            success: function( data ) 
            {
                var data = JSON.parse(data)

                $("#movie_list").find("tr:gt(0)").remove();

                for (let i = 0; i < data.length; i++) {
                    var tr = '<tr><td>'+ data[i].title +'</td><td><img src='+ data[i].poster + ' width="20%" alt="'+ data[i].title +'"></img></td><td> '+ data[i].genre +'</td><td>' + data[i].rating + '</td><td> '+ data[i].year_release + '</td><td> ' + data[i].metacritic_rating +'</td><td>'+ data[i].runtime +'</td></tr>'
                    $('#movie_list').append(tr);
                  }
            }
         })
}

function filterMovie() { 
    var filter_text = $('#filter_genre :selected').text();
    
    $.ajax(
        {
            type:"GET",
            url: "/getMoviesByGenre",
            data:{
                filter_text: filter_text
            },
            success: function( data ) 
            {
                var data = JSON.parse(data)

                $("#movie_list").find("tr:gt(0)").remove();

                for (let i = 0; i < data.length; i++) {
                    var tr = '<tr><td>'+ data[i].title +'</td><td><img src='+ data[i].poster + ' width="20%" alt="'+ data[i].title +'"></img></td><td> '+ data[i].genre +'</td><td>' + data[i].rating + '</td><td> '+ data[i].year_release + '</td><td> ' + data[i].metacritic_rating +'</td><td>'+ data[i].runtime +'</td></tr>'
                    $('#movie_list').append(tr);
                  }
            }
         })
 }