import type * as t from "../index" // t modülü içerisindeki fonksiyonları kullanmak için import ediyoruz


// typescript ile yazılan fonksiyonları jest ile test edebilmek için jest.requireActual kullanıyoruz
// getStatus, getFlights ve getHeaderType fonksiyonlarını jest.requireActual ile import ediyoruz
const {getStatus, getFlights, getHeaderType} = jest.requireActual<typeof t>("../index") 

interface Flight {

    data: [
        {
            id: number,
            from: string,
            to: string,
            date: string,
        }
    ]
} 

// Get status kontrolü getStatus() fonksiyonu status olarak 200 döndürüyor ise test başarılı

describe("Status OK kontrolü getStatus()", () => {
    it("½s", async () => {
        const result = await getStatus({} as any, {} as any)
        expect(result).toEqual({status: 200})
    })
})

// Get flights kontrolü getFlights() fonksiyonu status olarak 200 döndürüyor ise ve 
// body içerisinde data arrayi ve bu array içerisinde id, from, to ve date keyleri var ise test başarılı

describe("Gelen cevap kontrolü getFlights()", () => {
    it ("½s", async () => {
        const result = await getFlights({} as any, {} as any)
        //console.log(result.body.data)
        expect(result.status).toBe(200)
        expect(result.body.data).toEqual(
            expect.arrayContaining([
                expect.objectContaining({
                    id: expect.any(Number),
                    from: expect.any(String),
                    to: expect.any(String),
                    date: expect.any(String)
                })
            ]) as unknown as Flight["data"]
        )
    })
})

// Get header kontrolü getHeaderType() fonksiyonu status olarak 200 döndürüyor ise ve
// headers içerisinde content-type keyi application/json ise test başarılı

describe("Header kontrolü getHeaderType()", () => {
    it("½s", async () => {
        const result = await getHeaderType({} as any, {} as any)
        console.log(result.headers.get("content-type"))
        expect(result.status).toBe(200)
        expect(result.headers.get("content-type")).toBe("application/json")
    })
})


