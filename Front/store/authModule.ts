import { GetterTree, ActionTree, MutationTree } from 'vuex'
import { RootState } from '~/store'

export const state = () => ({
      token: null,
      isEmail : null,
      isLogin: true,
      SignUp: {
            email: '',
            password: '',
            confirmPassword: '',
            birthDate: '',
            registerDate: '',
      },
      Login: {
            email: '',
            password: '',
      },
})

export type AuthModuleState = ReturnType<typeof state>

export const getters: GetterTree<AuthModuleState, RootState> = {
      isAuthed(state) {
            return state.token != null
      },
      emailAuthed(state) {
            if (state.Login.email !== ''){
                  return state.Login.email
            }else{
                  return state.SignUp.email
            }

      },
}

export const actions: ActionTree<AuthModuleState, RootState> = {
      authenticateUser(vuexContext) {
            let authData = {email : "", password: ""}
            let authUrl =  ""
            if (vuexContext.state.isLogin == false) {
                  authData = vuexContext.state.SignUp
                  authUrl =
                        'https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=AIzaSyAVnJ2m4lb6DQcFD8iQgHVaKxjpvLfDNA0'
                  this.$axios
                        .get(
                              'http://localhost:8001/editcreate/?email=' +
                                    authData.email
                        )
                        .then()
                        .catch((e) => {
                              console.log('oops')
                        })
            } else {
                  authData = vuexContext.state.Login

                  authUrl =
                        'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyAVnJ2m4lb6DQcFD8iQgHVaKxjpvLfDNA0'
            }
            vuexContext.commit('setEmail', authData.email)
            localStorage.setItem("isEmail", authData.email)
            return this.$axios
                  .post(authUrl, {
                        email: authData.email,
                        password: authData.password,
                        returnSecureToken: true,
                  })
                  .then((res) => {
                        vuexContext.commit('setToken', res.data.idToken)

                        localStorage.setItem("token", res.data.idToken)
                        const exp = new Date().getTime() + (res.data.expiresIn * 1000)
                        localStorage.setItem("tokenExp", exp)
                        vuexContext.dispatch('setLogout', res.data.expiresIn * 1000)
                  })
                  .catch((e) => {
                        console.log(e)
                  })
      },
      setLogout(vuexContext, duration) {
            setTimeout(() => {
                  vuexContext.commit('clearToken')
            }, duration)
      },
      initAuth(vuexContext){

            const token = localStorage.getItem("token")
            const email = localStorage.getItem("isEmail")
            const exp = localStorage.getItem("tokenExp")

            if (token != null){
                  if (new Date().getTime() > new Date(exp).getTime()){return};
                  console.log(new Date().getTime() >= new Date(exp));


            }
            vuexContext.commit("setToken", token)
            vuexContext.commit("setEmail", email)
      }
}
export const mutations: MutationTree<AuthModuleState> = {
      setSignDetails(state, details: any) {
            state.SignUp = details
      },
      setLoginDetails(state, details: any) {
            state.Login = details
      },
      setToken(state, token) {
            state.token = token
      },
      setEmail(state, email) {
            state.isEmail = email

      },
      clearToken(state) {
            state.token = null
      },
      toggleLogin(state, toggle){
            state.isLogin = toggle
      }
}
