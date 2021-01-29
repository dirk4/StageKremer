export class Prediction {
    prediction;
    time;
    avg;
    inc;
    dec;
    part;


    constructor(prediction, time, avg, inc, dec, part) {
        this.prediction = prediction;
        this.time = time
        this.avg = avg;
        this.inc = inc;
        this.dec = dec;
        this.part=part;
    }
}
