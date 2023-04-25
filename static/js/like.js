function like(project_id) {
    var heart = document.getElementById('heart')
    var count = document.getElementById('count')
    $.get(`/gallery/like/${project_id}`).then(response => {
        if (response['response'] === 'liked') {
            count.innerText = Number(count.innerText) + 1;
            heart.className = 'fa fa-heart';
        } else {
            count.innerText = Number(count.innerText) - 1;
            heart.className = 'fa fa-heart-o';

        }

    })
}