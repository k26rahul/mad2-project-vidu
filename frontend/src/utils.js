import store from './store';

async function fetchHelper(url, options = {}) {
  try {
    let res = await fetch(url, {
      ...options,
      credentials: 'include',
    });
    let data = await res.json();
    return data;
  } catch {
    store.errorFlag = true; // show error alert in App.vue
  }
}

export async function get(apiPath) {
  return await fetchHelper(`http://127.0.0.1:5000${apiPath}`);
}

export async function post(apiPath, payload = {}) {
  return await fetchHelper(`http://127.0.0.1:5000${apiPath}`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(payload),
  });
}
