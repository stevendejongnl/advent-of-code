import data from './input.json'

const input = data.input

let previousMeasurement = null
let totalLarger = 0
input.forEach(measurement => {
    if (measurement > previousMeasurement) {
        totalLarger++
    }

    previousMeasurement = measurement
})

console.info('Result part one')
console.log(totalLarger)

