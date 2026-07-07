import { useState } from "react"

import axios from "axios"

import { useNavigate } from "react-router-dom"
import { toast } from "react-toastify";


function Login() {

    const navigate = useNavigate()

    const [email, setEmail] = useState("")

    const [password, setPassword] = useState("")


    const handleSubmit = async (e) => {

        e.preventDefault()

        try {

            const formData = new URLSearchParams()

            formData.append("username", email)

            formData.append("password", password)

            const response = await axios.post(

                "http://127.0.0.1:8000/login",

                formData,

                {
                    headers: {
                        "Content-Type":
                            "application/x-www-form-urlencoded"
                    }
                }
            )

            const token =
                response.data.access_token

            localStorage.setItem(
                "token",
                token
            )

            toast.success("🎉 Welcome back!");

            navigate("/")

        } catch (error) {

            console.log(error)

            alert("Login Failed 😭")
        }
    }


    return (

        <div className="auth-container">

            <div className="auth-card">

                <h1>NEURAX</h1>

                <form onSubmit={handleSubmit}>

                    <input
                        type="email"
                        placeholder="Email"
                        value={email}
                        onChange={(e) =>
                            setEmail(e.target.value)
                        }
                    />

                    <input
                        type="password"
                        placeholder="Password"
                        value={password}
                        onChange={(e) =>
                            setPassword(e.target.value)
                        }
                    />

                    <button type="submit">

                        Login

                    </button>

                </form>

            </div>

        </div>
    )
}

export default Login