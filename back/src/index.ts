// Staus kodunu döndüren fonksiyon

export const getStatus = async (req: Request, res: Response) => {
    res = await fetch('https://flights-api.buraky.workers.dev/');
    const data = await res.json();
    return {
        status: res.status,
    };
};

// Status kodunu ve body içerisindeki datayı döndüren fonksiyon

export const getFlights = async (req: Request, res: Response) => {
    res = await fetch('https://flights-api.buraky.workers.dev/');
    const data = await res.json();
    return {
        status: res.status,
        body : data,
    };
}

// Status kodunu ve headers içeriğini döndüren fonksiyon

export const getHeaderType = async (req: Request, res: Response) => {
    res = await fetch('https://flights-api.buraky.workers.dev/');
    return {
        status: res.status,
        headers: res.headers,
    };
}
