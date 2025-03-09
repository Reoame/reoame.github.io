var posts=["2025/03/08/hello-world/","2025/03/09/2/","2025/03/09/关于GitHub无法访问的解决办法/","2025/03/09/post/"];function toRandomPost(){
    pjax.loadUrl('/'+posts[Math.floor(Math.random() * posts.length)]);
  };