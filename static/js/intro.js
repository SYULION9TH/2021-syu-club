const count     = 220;
const blurCount = 60;

const stage = document.querySelector(".stage");

for (let i = 0; i < count; i++) {
    setTimeout(() => {
        makeLight(i);
    }, 10 * i);
}

const timer = setInterval(() => {
    for (let i = 0; i < count; i++) {
        setTimeout(() => {
        const removespan = document.querySelector("span");
        removespan.parentNode.removeChild(removespan);
        makeLight(i);
        }, 10 * i);
    }
}, 5000);

function makeLight(i) {

    let span = document.createElement("span");
    if (i < blurCount) {
        span.classList.add("blur");
    }
    stage.appendChild(span);

    gsap.set(span, {
        left: gsap.utils.random(0, stage.offsetWidth),
        top: gsap.utils.random(0, stage.offsetHeight),
        scale: gsap.utils.random(0.2, 1.2, 0.1),
        opacity: 0
    });

    let tl = gsap.timeline({
        paused: true,
        onComplate: () => {
        span.remove();
        makeLight(i);
        }
    })

    if (i < blurCount) {
        tl.to(span, {
        opacity: gsap.utils.random(0.1, 0),
        duration: .8
        })

        tl.to(span, {
        y: gsap.utils.random(-20, 20),
        x: gsap.utils.random(-20, 20),
        duration: gsap.utils.random(4, 2, 2),
        ease: Power0.easeNone
        }, -0.3)

        tl.to(span, {
        opacity:   0.2,
        duration: .4
        }, ">-0.8")
        
        tl.play();

    } else {
        tl.to(span, {
        opacity: gsap.utils.random(1, 1),
        duration: .2
        })

        tl.to(span, {
        x: gsap.utils.random(-20, 20),
        y: gsap.utils.random(-20, 20),
        duration: gsap.utils.random(4, 2, 5),
        ease: Power0.easeNone
        }, -0.3)

        tl.to(span, {
        opacity:  .3,
        duration: .3
        }, ">-0.3")

        tl.play();
    }
}