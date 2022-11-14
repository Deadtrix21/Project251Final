import { GetterTree, ActionTree, MutationTree } from 'vuex'
import { RootState } from '~/store'

export const state = () => ({
      pages: [
            { name: 'Home',         path: '/',              mdi: 'mdi-home' },
            { name: 'Client',       path: '/Client',        mdi: 'mdi-account' },
            { name: 'Admin',        path: '/Admin',         mdi: 'mdi-home' },
            { name: 'About',        path: '/About',         mdi: 'mdi-contacts' },
            { name: 'Settings',     path: '/Settings',      mdi: 'mdi-cog-outline' },
      ],
      admin : [

            { name: 'Add Device',         path: '/Admin/',         mdi: 'mdi-source-branch-plus' },
            { name: 'Remove Device',      path: '/Admin/',         mdi: 'mdi-source-branch-minus' },

      ]
})

export type NavModuleState = ReturnType<typeof state>

export const getters: GetterTree<NavModuleState, RootState> = {
      pager(state) {
            return state.pages
      },
      adminpager(state) {
            return state.admin
      },
}

export const actions: ActionTree<NavModuleState, RootState> = {}
export const mutations: MutationTree<NavModuleState> = {}
