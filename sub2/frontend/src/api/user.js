import { createInstance } from "./index.js";

const instance = createInstance();


function login(member, success, fail) {
  instance.defaults.headers["access-token"] = window.localStorage.getItem(
    "access-token"
  );

  instance
    .post(`/accounts/login`, {
      username: member.username,
      password:member.password
    })
    .then(success)
    .catch(fail);
}

function join(member, success, fail) {
  const body = {
    userid: member.userid,
    userpwd: member.userpwd,
    username: member.username,
    email: member.email,
    address: member.address,
  };

  instance
    .post("/user/confirm/join", JSON.stringify(body))
    .then(success)
    .catch(fail);
}


async function findById(memberEmail, success, fail) {
  instance.defaults.headers["access-token"] = window.localStorage.getItem(
    "access-token"
  );
  await instance
    .get(`/member/info/${memberEmail}`)
    .then(success)
    .catch(fail);
}

export { login, findById };
