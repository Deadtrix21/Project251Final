import { GetterTree, ActionTree, MutationTree } from 'vuex'
import { RootState } from '~/store'
import '@nuxtjs/axios'
let heading = {
      headers: {
            'Content-Type': 'application/json',
      },
}

export const state = () => ({
      isLogin: false,
      userDetails : {
            email : "",
            password : ""
      },
      details: {
            email: '',
            password: '',
            token: '',
            uuid: '',
      },
})

export type AuthModuleState = ReturnType<typeof state>

export const getters: GetterTree<AuthModuleState, RootState> = {
      isAuthed(state) {
            return state.details !== null && state.details.token != "" && state.details.token != undefined
      },
      getUserEmail(state) {
            return state.details.email
      },
}

export const actions: ActionTree<AuthModuleState, RootState> = {
      authenticateUser(vuexContext) {
            const item1 = vuexContext.state.userDetails.email
            const item2 = vuexContext.state.userDetails.password
            if (item1 === "" || item2 === ""){return}
            console.log(2);

            var structure = ''
            if (vuexContext.state.isLogin === false) {
                  structure = `mutation{
                        SignUp(
                              account : {
                                    email: "${item1}",
                                    password : "${item2}"
                              }
                        ){
                              uuid
                              email
                              password
                              token
                        }
                  }`
                  this.$axios
                        .post(`http://${window.location.hostname}:5000/users`, {query: structure})
                        .then((data) => {
                              try {
                                    vuexContext.commit("setDetails", data.data.data.SignUp)
                                    console.log(data);

                              } catch {}
                        })
                        .catch((e) => {
                              console.log(e)
                        })
            } else {
                  structure = `
                        {
                              Login(
                                    account : {
                                          email: "${item1}",
                                          password : "${item2}"
                                    }
                              ){
                                    uuid
                                    email
                                    password
                                    token
                              }
                        }
                  `
                  this.$axios
                        .post(`http://${window.location.hostname}:5000/users`, {query: structure})
                        .then((data) => {
                              try {
                                    vuexContext.commit("setDetails", data.data.data.Login)
                              } catch {}
                        })
                        .catch((e) => {
                              console.log(e)
                        })
            }
      },
}

export const mutations: MutationTree<AuthModuleState> = {
      setDetails(state, d) {
            state.details = d
      },
      setUser(state, d) {
            state.userDetails = d
      },
      setLogin(state, d) {
            state.isLogin = d
      },
}
