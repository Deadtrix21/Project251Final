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
      userDetails: {
            email: '',
            password: '',
      },
      details: {
            email: '',
            password: '',
            token: '',
            uuid: '',
      },
      aliases: {
            alias: '',
            obj: {},
      },
      fulldataset: [],
      fulldeviceSet: [],
      AdminDetails : {
            isAdmin : false,
            details : {
                  uuid : "",
                  token : ""
            }
      },
      deleteAccountEmail: "",
      devices : {
            link : '',
            name : ""
      }
})

export type AuthModuleState = ReturnType<typeof state>


export const getters: GetterTree<AuthModuleState, RootState> = {
      isAuthed(state) {
            return (
                  state.details !== null &&
                  state.details.token != '' &&
                  state.details.token != undefined
            )
      },
      isAdmin(state){
            return state.AdminDetails
      },
      getUserEmail(state) {
            return state.details.email
      },
      getAll(state) {
            return state.details
      },
      getAllUser(state) {
            return state.fulldataset
      },
      getAllDevices(state) {
            return state.fulldeviceSet
      },
}


export const actions: ActionTree<AuthModuleState, RootState> = {
      authenticateUser(vuexContext) {
            const item1 = vuexContext.state.userDetails.email
            const item2 = vuexContext.state.userDetails.password
            if (item1 === '' || item2 === '') {
                  return
            }
            console.log(2)

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
                        .post(`http://${window.location.hostname}:5000/users`, {
                              query: structure,
                        })
                        .then((data) => {
                              try {
                                    vuexContext.commit(
                                          'setDetails',
                                          data.data.data.SignUp
                                    )
                                    console.log(data)
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
                                    _id
                                    uuid
                                    email
                                    token
                              }
                        }
                  `
                  this.$axios
                        .post(`http://${window.location.hostname}:5000/users`, {
                              query: structure,
                        })
                        .then((data) => {
                              try {
                                    vuexContext.commit(
                                          'setDetails',
                                          data.data.data.Login
                                    )
                              } catch {}
                        })
                        .catch((e) => {
                              console.log(e)
                        })
            }
      },
      uploadAlias(vuexContext) {
            let obj = vuexContext.state.aliases.obj
            let alias = vuexContext.state.aliases.alias
            console.log(vuexContext.state.aliases)

            let structure = `
                  mutation{
                        sectionAlias(
                              name:"${obj.name}",
                              uuid:"${obj.uuid}",
                              alias:"${alias}"
                        )
                  }
            `
            this.$axios.post(
                  `http://${window.location.hostname}:5000/devices`,
                  { query: structure }
            )
      },
      getAllUsers(vuexContext) {
            let structure = `
            {
                  Users{
                        _id
                        uuid
                        email
                        password
                        token
                  }
            }
            `
            this.$axios
                  .post(`http://${window.location.hostname}:5000/admins`, {
                        query: structure,
                  })
                  .then((res) => {
                        vuexContext.commit(
                              'setDataset',
                               res.data.data.Users
                        )
                  })
      },
      getAllDevice(vuexContext) {
            let structure = `
            {
                  deviceGetAll{
                        alias
                        name
                        uuid
                  }
            }
            `
            this.$axios
                  .post(`http://${window.location.hostname}:5000/devices`, {
                        query: structure,
                  })
                  .then((res) => {
                        vuexContext.commit(
                              'setDevices',
                               res.data.data.deviceGetAll
                        )
                  })
      },
      getAdminUser(vuexContext){
            const item1 = vuexContext.state.userDetails.email
            const item2 = vuexContext.state.userDetails.password
            let structure = `
            {
                  Login(
                        account: {
                              email : "${item1}",
                              password : "${item2}"
                        }
                  ){
                        token
                        uuid
                  }
            }
            `
            this.$axios
                  .post(`http://${window.location.hostname}:5000/admins`, {
                        query: structure,
                  })
                  .then((res) => {
                        let obj = ""
                        if (res.data.data.Login == null){
                              obj = {
                                    isAdmin : false,
                                    details : null
                              }
                        }
                        else{
                              obj = {
                                    isAdmin : true,
                                    details : {
                                          uuid : res.data.data.Login.uuid,
                                          token : res.data.data.Login.token
                                    }
                              }
                        }

                        vuexContext.commit(
                              'setAdmin',
                              obj
                        )
                  })
      },
      deleteUserAccount(vuexContext){
            const item1 = vuexContext.state.deleteAccountEmail
            let structure = `
            {
                  DelUsers(
                        email:"${item1}"
                        )
            }
            `
            this.$axios
                  .post(`http://${window.location.hostname}:5000/admins`, {
                        query: structure,
                  })
                  .then((res) => {
                        return res.data.data.DelUsers
                  })
      },
      deleteDeviceAccount(vuexContext){
            const item1 = vuexContext.state.devices.name
            console.log(item1);

            let structure = `
            mutation{
                  deviceDelete(
                        word:"${item1}"
                  )
            }
            `
            this.$axios
                  .post(`http://${window.location.hostname}:5000/devices`, {
                        query: structure,
                  })
      },
      linkDeviceAccount(vuexContext){
            const item1 = vuexContext.state.devices.link
            const item2 = vuexContext.state.devices.name
            let structure = `
            mutation{
                  deviceLink(
                        name:"${item2}",
                        uuid:"${item1}"
                  )
            }
            `
            this.$axios
                  .post(`http://${window.location.hostname}:5000/devices`, {
                        query: structure,
                  })
      }
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
      setAlias(state, obj) {
            state.aliases = obj
      },
      setDataset(state, obj) {
            state.fulldataset = obj
      },
      setAdmin(state, obj) {
            state.AdminDetails = obj
      },
      setDeleteAccount(state, obj) {
            state.deleteAccountEmail = obj
      },
      setDevices(state, obj){
            state.fulldeviceSet = obj
      },
      setLinkDevice(state, obj){
            state.devices = obj
      },
      setDeleteDevice(state, obj){
            state.devices.name = obj
      }
}
