import { useState } from "react"

import axios from "axios"
import { toast } from "react-toastify";


function Register() {

    const [username, setUsername] = useState("")

    const [email, setEmail] = useState("")

    const [password, setPassword] = useState("")


    const handleSubmit = async (e) => {

        e.preventDefault()

        try {

            const response = await axios.post(

                "http://127.0.0.1:8000/register",

                {
                    username,
                    email,
                    password
                }
            )

            toast.success("🎊 Account created!");

            console.log(response.data)

        } catch (error) {

            console.log(error)

            toast.error("❌ Something went wrong!");
        }
    }


    return (

        <div className="auth-container">

            <div className="auth-card">

                <h1>NEURAX</h1>

                <form onSubmit={handleSubmit}>

                    <input
                        type="text"
                        placeholder="Username"
                        value={username}
                        onChange={(e) =>
                            setUsername(e.target.value)
                        }
                    />

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

                        Register

                    </button>

                </form>

            </div>

        </div>
    )
}

export default Register