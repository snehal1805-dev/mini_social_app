import { useEffect } from "react"

import { useState } from "react"

import axios from "axios"
import { toast } from "react-toastify";

function Dashboard() {

    const [posts, setPosts] = useState([])

    const [content, setContent] = useState("")


    const token = localStorage.getItem(
        "token"
    )


    const fetchPosts = async () => {

        try {

            const response = await axios.get(

                "http://127.0.0.1:8000/posts/"
            )

            setPosts(response.data)

        } catch (error) {

            console.log(error)
        }
    }


    useEffect(() => {

        fetchPosts()

    }, [])


    const createPost = async () => {

        try {

            await axios.post(

                "http://127.0.0.1:8000/posts/",

                {
                    content: content
                },

                {
                    headers: {
                        Authorization:
                            `Bearer ${token}`
                    }
                }
            )

            toast.success("🚀 Post created successfully!");

            setContent("")

            fetchPosts()

        } catch (error) {

            console.log(error)

            alert("Post Failed 😭")
        }
    }

    const deletePost = async (id) => {

        try {

            await axios.delete(

                `http://127.0.0.1:8000/posts/${id}`,

                {
                    headers: {
                        Authorization:
                            `Bearer ${token}`
                    }
                }
            )

            fetchPosts()
            setPosts(posts.filter((post) => post.id !== id));

            toast.success("🗑️ Post deleted successfully!");

        } catch (error) {

            console.log(error)
        }
    }


    return (

        <div>

            <div className="navbar">

                <h1 className="logo">

                    NEURAX

                </h1>

                <button
                    className="logout-btn"
                    onClick={() => {

                        localStorage.removeItem(
                            "token"

                        
                        )
                        

                        window.location.href =
                            "/login"

                        
                    }}
                    
                >

                    Logout

                </button>

            </div>

            <div className="dashboard">

                <div className="create-post">

                    <input
                        type="text"
                        placeholder=
                        "Transmit your thoughts..."
                        value={content}
                        onChange={(e) =>
                            setContent(e.target.value)
                        }
                    />

                    <button onClick={createPost}>

                        Create Post

                    </button>

                </div>

                {
                    posts.length === 0 ? (

                        <div className="empty-posts">

                            No neural transmissions yet 🚀

                        </div>

                    ) : (

                        posts.map((post) => (

                            <div
                                className="post-card"
                                key={post.id}
                            >

                                <h3>

                                    {post.content}

                                </h3>

                                <p>

                                    Neural User :
                                    @{post.username}

                                </p>

                                <button
                                    className="delete-btn"
                                    onClick={() =>
                                        deletePost(post.id)
                                    }
                                >

                                    Delete

                                </button>

                            </div>
                        ))
                    )
                }

            </div>

        </div>
    )
}

export default Dashboard