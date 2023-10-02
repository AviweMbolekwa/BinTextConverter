document.getElementById('copy-btn').addEventListener('click', () => copy())
document.getElementById('bulbs').addEventListener('change', (e) => convertOutput(e))
document.getElementById('nums').addEventListener('change', (e) => convertOutput(e))

function copy() {
    const binary = document.getElementById('binary-message').innerText;
    navigator.clipboard.writeText(binary)
    document.getElementById('copy-btn').innerText = "COPIED!"
}

function convertOutput(e) {
    const outputType = e.target.value
    const outputValue = document.getElementById('binary-message').innerText

    if (outputType === "nums") {
        document.getElementById('binary-message').innerText = outputValue.replaceAll('⚫', '0').replaceAll('🟡', '1')
    }

    if (outputType === "bulbs") {
        document.getElementById('binary-message').innerText = outputValue.replaceAll('0', '⚫').replaceAll('1', '🟡')
    }
}