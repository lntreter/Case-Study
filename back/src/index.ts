export const getStatus = async (req: Request, res: Response) => {
    res = await fetch('https://flights-api.buraky.workers.dev/');
    const data = await res.json();
    return {
        status: res.status,
    };
};

export const getFlights = async (req: Request, res: Response) => {
    res = await fetch('https://flights-api.buraky.workers.dev/');
    const data = await res.json();
    return {
        status: res.status,
        body : data,
    };
}

export const getHeaderType = async (req: Request, res: Response) => {
    res = await fetch('https://flights-api.buraky.workers.dev/');
    return {
        status: res.status,
        headers: res.headers,
    };
}
