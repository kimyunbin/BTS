import axios from "axios";

function createInstance() {
  const instance = axios.create({
    baseURL: "http://j5c203.p.ssafy.io/api",

    headers: {
      "Content-Type": "application/json"
    },
  });
  return instance;
}
function createInstance2() {
  const token =  localStorage.getItem('token')
  const instance = axios.create({
    baseURL: "http://j5c203.p.ssafy.io/api",

    headers: {
      Authorization: `JWT ${token}`
    },
  });
  return instance;
}


function imageInstance() {
  const instance = axios.create({
    baseURL: "https://dapi.kakao.com/v2",

    headers: {
      "Authorization": "KakaoAK " + "81c18060700638a5bd2763e645639108",
      //"Content-Type": "application/json"
    },
  });
  return instance;
}


function createInstance3() {
  const instance = axios.create({
    baseURL: "http://j5c203.p.ssafy.io/api",

  });
  return instance;
}

export { createInstance };
export { createInstance2 };
export { createInstance3 };
export { imageInstance};
