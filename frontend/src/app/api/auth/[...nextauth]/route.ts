import NextAuth from "next-auth"
import CredentialsProvider from "next-auth/providers/credentials"
import axios from 'axios'

export default NextAuth({
  providers: [
    CredentialsProvider({
      id: 'django-allauth',
      name: 'Django Allauth',
      async authorize(credentials, req) {
        const { provider, access_token } = credentials as { provider: string; access_token: string }
        
        try {
          const res = await axios.post(`${process.env.NEXT_PUBLIC_BACKEND_URL}/auth/${provider}/`, {
            access_token: access_token
          })

          if (res.data.key) {
            return { id: res.data.user.pk, name: res.data.user.username, email: res.data.user.email, token: res.data.key }
          }
          return null
        } catch (error) {
          console.error('Authentication error:', error)
          return null
        }
      }
    }),
  ],
  callbacks: {
    async jwt({ token, user }) {
      if (user) {
        token.accessToken = user.token
      }
      return token
    },
    async session({ session, token }) {
      session.accessToken = token.accessToken
      return session
    }
  },
  pages: {
    signIn: '/login',
  }
})