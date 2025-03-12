import store from './store';

async function fetchHelper(url, options = {}) {
  try {
    let res = await fetch(url, options);
    // if status code is 200-299
    if (res.ok) {
      let data = await res.json();
      return data;
    }
    // else status code is 3xx/4xx/5xx (but fetch was successful)
    throw Error('response not ok');
  } catch (err) {
    store.errorFlag = true; // show error alert in App.vue
    console.error('💥 failure in fetchHelper:', err);
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
