

export default function (context) {
      const authed = context.store.getters['authModule/isAuthed']
      if (!authed) { context.redirect("/Login") }
}