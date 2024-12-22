// http://api.weatherapi.com/v1/current.json?key=0802315908c3488e96b82027240610&q=Amritsar&aqi=no


let traget ='Amritsar'

const feathResults =async (targetlocation) => {
    let url='http://api.weatherapi.com/v1/current.json?key=0802315908c3488e96b82027240610&q=$(targetlocation)&aqi=no'

    const res = await fetch(url)
    const data = await res.json()

    console.log(res)

}

feathResults(traget)