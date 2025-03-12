export async function post(apiPath, payload) {
  let res = await fetch(`http://127.0.0.1:5000${apiPath}`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(payload),
  });
  let data = await res.json();
  return data;
}
