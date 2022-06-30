let follow_buttons = document.getElementsByClassName('add-unadd')

for (let i = 0; i < follow_buttons.length; i++){
    follow_buttons[i].addEventListener('click', function(){
        let item_id = this.dataset.id
        let action = this.dataset.action

        addToWishList(item_id, action)
    })
}

function addToWishList(item_id, action){
    let url = '/add_to_wishlist/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'item_id': item_id, 'action': action})
    })
        .then((response)=> {
            return response.json()
        })
        .then((data)=> {
            console.log('data:', data)
            location.reload()
        })

}
