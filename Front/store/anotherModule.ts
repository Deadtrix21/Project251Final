import { GetterTree, ActionTree } from 'vuex'
import { RootState } from '~/store'

export const state = () => ({
      more: 3,
})

export type AnotherModuleState = ReturnType<typeof state>

export const getters: GetterTree<AnotherModuleState, RootState> = {
      evenMore: (state) => state.more + 5,
      nameAndMore: (state, getters, rootState) =>
            `${rootState.name}: ${state.more}`,
}

export const actions: ActionTree<AnotherModuleState, RootState> = {
      printRootState({ rootState }) {
            console.log('accessing rootState:', rootState.name)
      },
}
