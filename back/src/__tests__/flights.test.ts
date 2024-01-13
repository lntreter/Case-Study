import exp from "constants"
import type * as t from "../index"

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

describe("Status OK kontrolü getStatus()", () => {
    it("½s", async () => {
        const result = await getStatus({} as any, {} as any)
        expect(result).toEqual({status: 200})
    })
})

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

describe("Header kontrolü getHeaderType()", () => {
    it("½s", async () => {
        const result = await getHeaderType({} as any, {} as any)
        console.log(result.headers.get("content-type"))
        expect(result.status).toBe(200)
        expect(result.headers.get("content-type")).toBe("application/json")
    })
})


