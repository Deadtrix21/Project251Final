import { GetterTree, ActionTree, MutationTree } from 'vuex'

function dataPost(): Array<Object> {
      const post = [
            {
                  id: '0',
                  title: 'Hello',
                  lastupdate: new Date().toUTCString(),
                  preview: 'I am a ttyutyutyjfgfxfhsrg itle ',
                  author: 'Deadtrix21',
                  thumbnail:
                        'https://media.istockphoto.com/photos/data-scientists-male-programmer-using-laptop-analyzing-and-developing-picture-id1295900106?k=20&m=1295900106&s=612x612&w=0&h=hDkQP1a9dUo4Esv8iMyVlEnP4nfN2mwM5LdtPW9M8zo=',
            },
            {
                  id: '1',
                  author: 'Deadtrix21',
                  lastupdate: new Date().toUTCString(),
                  title: 'Hello',
                  preview: 'I am ajghgkhjkjhktytyu title ',
                  thumbnail:
                        'https://media.istockphoto.com/photos/data-scientists-male-programmer-using-laptop-analyzing-and-developing-picture-id1295900106?k=20&m=1295900106&s=612x612&w=0&h=hDkQP1a9dUo4Esv8iMyVlEnP4nfN2mwM5LdtPW9M8zo=',
            },
            {
                  id: '2',
                  title: 'Hello',
                  lastupdate: new Date().toUTCString(),
                  author: 'Deadtrix21',
                  preview: 'I am assafdfgfgha title ',
                  thumbnail:
                        'https://media.istockphoto.com/photos/data-scientists-male-programmer-using-laptop-analyzing-and-developing-picture-id1295900106?k=20&m=1295900106&s=612x612&w=0&h=hDkQP1a9dUo4Esv8iMyVlEnP4nfN2mwM5LdtPW9M8zo=',
            },
            {
                  id: '3',
                  author: 'Deadtrix21',
                  lastupdate: new Date().toUTCString(),
                  title: 'Hello',
                  preview: 'I am aasasd title ',
                  thumbnail:
                        'https://media.istockphoto.com/photos/data-scientists-male-programmer-using-laptop-analyzing-and-developing-picture-id1295900106?k=20&m=1295900106&s=612x612&w=0&h=hDkQP1a9dUo4Esv8iMyVlEnP4nfN2mwM5LdtPW9M8zo=',
            },
      ]
      return post
}

export const state = () => ({
      BlogPosts: dataPost() as Array<Object>[],
      name: 'Deadtrix' as String,
})

export type RootState = ReturnType<typeof state>

export const getters: GetterTree<RootState, RootState> = {
      loadPosts: (state) => {
            return state.BlogPosts
      },
}

export const mutations: MutationTree<RootState> = {
      setPosts: (state, posts: any) => (state.BlogPosts = posts),
}

export const actions: ActionTree<RootState, RootState> = {
      async fetchThings({ commit }) {
            const things = await this.$axios.$get('/things')
            console.log(things)
            commit('CHANGE_NAME', 'New name')
      },
      setPosts(vuexContext, posts) {
            vuexContext.commit('setPosts', posts)
      },
}
