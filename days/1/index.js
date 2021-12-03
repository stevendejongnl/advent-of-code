import data from './input.json'

const measurements = data.input

function partOne(measurements) {
    let previousMeasurement = null
    let totalLarger = 0
    measurements.forEach(measurement => {
        if (parseInt(measurement) > previousMeasurement) {
            totalLarger++
        }

        previousMeasurement = parseInt(measurement)
    })

    return totalLarger
}

function partTwo(measurements) {
    let totalLarger = 0
    let newMeasurements = []
    measurements
      .map(measurement => parseInt(measurement))
      .forEach((measurement, index, array) => {
        if (array[index - 1] && array[index] && array[index + 1]) {
          let sum = array[index - 1] + array[index] + array[index + 1]
            newMeasurements.push(sum)
            return sum
        }
      })

    newMeasurements
      .reduce((previous, current) => {
        if (previous < current) {
          totalLarger++
        }
        return current
      })

    return totalLarger
}

function Parts(one, two) {
    this.partOne = one
    this.partTwo = two
}

const partOneResult = partOne(measurements)
const partTwoResult = partTwo(measurements)
const parts = new Parts(partOneResult, partTwoResult)

console.table(parts)
