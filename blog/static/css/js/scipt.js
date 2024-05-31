function getBlogPosts() {
    fetch('/get_posts/')  // Blog gönderilerini almak için bir GET isteği yap
    .then(response => response.json())
    .then(data => {
        // Ana sayfadaki uygun bir HTML elementine (div, ul gibi) gönderileri ekle
        const postsContainer = document.getElementById('posts-container');
        data.posts.forEach(post => {
            const postElement = document.createElement('div');
            postElement.innerHTML = `
                <h3>${post.title}</h3>
                <p>${post.content}</p>
                <small>Author: ${post.author}</small>
                <br>
                <small>Created at: ${post.created_at}</small>
                <hr>
            `;
            postsContainer.appendChild(postElement);
        });
    })
    .catch(error => console.error('Error fetching blog posts:', error));
}

document.addEventListener('DOMContentLoaded', function() {
    getBlogPosts();  // Sayfa yüklendiğinde blog gönderilerini al
});
