var updateBtns = document.getElementsByClassName('update-cart')

// add an event handler to each button
for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('ProductId: ', productId, 'Action: ', action)
        console.log('USER: ', user)
        if (user === 'AnonymousUser') {
            // 'AnonymousUser' is how Django renders anonymous user
            console.log('User not logged in')
        }
        else {
            updateUserOrder(productId, action)
        }
    }
    )
}

function updateUserOrder(productId, action) {
    console.log('User is authenticated, sending data...')
    var url = '/update_item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken' : csrftoken
        },
        body: JSON.stringify({'productId': productId, 'action': action})
    })
        // to return a promise to fetch
        // first, response value turned into json value
        .then((response) => {
            return response.json();
        })

        // we console out that data
        .then((data) => {
            console.log('data: ', data);  //"Item was added"
            location.reload();
        })

}