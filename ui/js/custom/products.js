
var productListApiUrl = "http://localhost:5000/getProducts"
var addToCartApiUrl = "http://127.0.0.1:5000/addToCart"
document.addEventListener('DOMContentLoaded', async function () {
    // JSON data by API call
    const url = new URL(window.location.href)
    const id = url.searchParams.get("id")
    console.log(id)
    const data = await fetch(productListApiUrl)
    const response = await data.json()
    console.log(response)
    document.getElementById('category-name').textContent = id;
    const filteredData = response.filter((product) => {
        return product.category.toLowerCase() == id.toLowerCase()
    })

    console.log(filteredData)
    const productContainer = document.getElementById('product-container');

    filteredData.forEach((product) => {
        const productCard = document.createElement('div');
        productCard.classList.add('product-card');
debugger
        productCard.innerHTML = `
        <span class="product_img"><img src="${product.image_url}" alt="${product.name}" class="product-image"></span>
        <div class="product-info">
            <h3>${product.name}</h3>
            <p>Price: ₹<span id="price-${product.product_id}">${product.price_per_unit}</span></p>
            <input type="number" id="quantity-${product.product_id}" name="quantity" min="1" value="1" class="quantity-input">
            <button class="addToCartBtn" data-product-id="${product.product_id}">Add To cart</button>
        </div>
    `;

        productContainer.appendChild(productCard);
    });

    const addToCartButton = document.querySelectorAll('.addToCartBtn');
    addToCartButton.forEach(button => {
        button.addEventListener('click', async function (e) {
            debugger
            const productId = e.target.getAttribute('data-product-id');
            const quantityInput = document.getElementById(`quantity-${productId}`).value;
            const price = document.getElementById(`price-${productId}`).innerText;
            console.log(price)
            const costInput = price * quantityInput;
            const token = JSON.parse(localStorage.getItem('userData'))
            console.log(costInput)
                        // API call to add product to cart
                        try {
                            const addToCartResponse = await fetch(addToCartApiUrl, {
                                method: 'POST',
                                headers: {
                                    'Content-Type': 'application/json',
                                    'Authorization': `Bearer ${token.access_token}`
                                },
                                body: JSON.stringify({ product_id: productId, quantity: quantityInput, cost:costInput})
                            });
            
                            if (addToCartResponse.ok) {
                                console.log('Product added to cart successfully');
                                // You can add more UI feedback here like showing a success message
                            } else {
                                console.log('Failed to add product to cart');
                                // Handle errors here
                            }
                        } catch (error) {
                            console.error('Error adding product to cart:', error);
                        }
            
        });
    });

});
