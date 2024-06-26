import React, { useEffect, useState } from 'react'
import { Routes, Route, useNavigate } from 'react-router-dom'
import MainPage from './routes/MainPage'
import LoginPage from './routes/LoginPage'
import SignUpPage from './routes/SignUpPage'

const App = () => {

  const [selectedVynil, setSelectedVynil] = useState([])
  const [likedVynils, setLikedVynils] = useState([])
  const [isLikedVynil, setIsLikedVynil] = useState([])
  const [aggregation, setAggregation] = useState([])
  const [filter, setFilter] = useState("")

  const viewVynil = (vinyl) => {
    setSelectedVynil(vinyl)
  }

  useEffect(() => {
    console.log(aggregation)
  }, [aggregation])

  useEffect(() => {
    if (likedVynils.includes(selectedVynil._id)) {
      setIsLikedVynil(true)
    } else {
      setIsLikedVynil(false)
    }
  }, [selectedVynil])

  useEffect(() => {
  
    if (likedVynils.includes(selectedVynil._id)) {
      setIsLikedVynil(true)
    } else {
      setIsLikedVynil(false)
    }
  }, [likedVynils])

  const handleFavorites = (favorites) => {
    setLikedVynils(favorites)
  }

  const embeds = [
    { src: "https://charts.mongodb.com/charts-project-0-dfebe/embed/charts?id=63ea97f5-f7c5-4555-8409-fda2c81b9f45&maxDataAge=3600&theme=light&autoRefresh=true" },
    { src: "https://charts.mongodb.com/charts-project-0-dfebe/embed/charts?id=63ea9605-1d7c-4be3-8bbc-780c6cf8efc1&maxDataAge=3600&theme=light&autoRefresh=true" },
    { src: "https://charts.mongodb.com/charts-project-0-dfebe/embed/charts?id=63ea9436-28ca-41b6-8f4b-1430585e7ce6&maxDataAge=3600&theme=light&autoRefresh=true" }
  ];

   // hacer la busqueda d evinilos al entrar
  useEffect(() => {
    setFilter("nothing")
  }, [])

  
  return (<Routes>
    <Route path="/" element={<LoginPage handleFavorites={handleFavorites}/>} />
    <Route path="/main" element={<MainPage viewVinil={viewVynil} setAggregation={setAggregation} filter={filter} setFilter={setFilter} />} />
    <Route path="/login" element={<LoginPage handleFavorites={handleFavorites} />} />
    <Route path="/sign-up" element={<SignUpPage />} />

  </Routes>)
}

export default App
