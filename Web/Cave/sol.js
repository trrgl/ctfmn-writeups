// browseriinha console deer ajluulah
(async () => {
  for (let i = 0; i < 5000; i++) {
    try {
      const res = await fetch(`/chest-${i}`, { method: 'POST' }); // chest burluu POST huselt yvuulna
      if (res.status === 200) { // response coden 200 baivl heddeh chest gdgin hevleed olood ongoilgono
        console.log(i);
        break;
      }
    } catch (err) {
      console.error(err);
    }
  }
})();

// flag : HZU18{HUH_Y0U_G0T_A_HIDDEN_ITEM}