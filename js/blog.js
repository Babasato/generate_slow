// Updated blog.js - paste this exactly
document.addEventListener('DOMContentLoaded', function() {
  fetch('/blog/index.json')
    .then(response => response.json())
    .then(posts => {
      const container = document.getElementById('blog-posts');
      posts.slice(0, 3).forEach(post => {
        container.innerHTML += `
          <article class="glass-card rounded-xl overflow-hidden blog-card">
            <img src="${post.image}" alt="${post.title}" class="w-full h-48 object-cover">
            <div class="p-6">
              <h3 class="text-xl font-bold mb-2">${post.title}</h3>
              <p class="text-gray-600 mb-4">${post.excerpt}</p>
              <a href="/blog/${post.slug}" class="text-purple-600 font-medium">Read More →</a>
            </div>
          </article>
        `;
      });
    })
    .catch(error => console.log('Error loading posts:', error));
});
