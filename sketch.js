  
var train = true;

function setup() {
    createCanvas(500, 500);
    background(0);

    nn = new RedeNeural(2, 3, 1);

    // XOR Problem
    dataset = {
        inputs:
            [[1, 1],
            [1, 0],
            [0, 1],
            [0, 0]],
        outputs:
            [[0],
            [1],
            [1],
            [0]]
    }
}

function draw() {
    if (train) {
        for (var i = 0; i < 10000; i++) {
            var index = floor(random(4));
            nn.train(dataset.inputs[index], dataset.outputs[index]);
        }
        var valor1 = nn.predict([0, 1]);
        var valor2 = nn.predict([1, 0]);
        if (valor1 < 0.04 &&  valor2 > 0.98) {
            console.log(valor1);
            console.log(valor2);
            train = false;
            console.log("terminou");
        }
    }
}
