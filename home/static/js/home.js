const animate = document.querySelectorAll('.animate')

const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.3, // Adjust this value to your preference (e.g., 0.2 means 20% visibility is enough)
};

const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        entry.target.classList.toggle('show', entry.isIntersecting)
        if(entry.isIntersecting) observer.unobserve(entry.target)
    })
},observerOptions)

animate.forEach(element => {
    observer.observe(element)
    console.log(element);
})


