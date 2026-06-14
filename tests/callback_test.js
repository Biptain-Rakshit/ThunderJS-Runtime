function greet(name, callback) {
    callback(name);
}

greet("Biptain", (name) => {
    console.log("Hello " + name);
});