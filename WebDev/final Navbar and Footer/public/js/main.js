const  menuBtn = document.querySelector('.hamburger')
const dropDownMenu = document.querySelector('.dropdown-menu')
let menuOpen = false;


menuBtn.addEventListener('click', () => {
    if(!menuOpen){
        menuBtn.classList.add('open')
        dropDownMenu.classList.add('open')
        menuOpen = true;
    }else{
        menuBtn.classList.remove('open')
        dropDownMenu.classList.remove('open')
        menuOpen = false;
    }
})


// Drop down click event----------------------------------------------------------------------------------------------

    // Home Drop ---------------------------------------------------------------------------
        const homeDrop = document.querySelector('.home-drop p')
        const homeMenu = document.querySelector('.home-menu')

        homeDrop.addEventListener('click', () => {
            homeMenu.classList.toggle('open')
        })
    // ------------------------------------------------------------------------------------

    //About Us Drop--------------------------------------------------------------------------
        const aboutUsDrop = document.querySelector('.aboutUs-drop p')
        const aboutUsMenu = document.querySelector('.aboutUs-menu')
        aboutUsDrop.addEventListener('click', () => {
            aboutUsMenu.classList.toggle('open')
            aboutUsDrop.classList.toggle('open')
        })
    // -------------------------------------------------------------------------------------

    //Products Drop-------------------------------------------------------------------------
        const productsDrop = document.querySelector('.products-drop p')
        const productsMenu = document.querySelector('.products-menu')
        productsDrop.addEventListener('click', () => {
            productsMenu.classList.toggle('open')
            productsDrop.classList.toggle('open')
        })

        // PV Module drop
            const pvModuleDrop = document.querySelector('.pvModule-drop p')
            const pvModuleMenu = document.querySelector('.pvModule-menu')

            pvModuleDrop.addEventListener('click', () => {
                pvModuleMenu.classList.toggle('open')
                // pvModuleDrop.classList.toggle('open')
            })
        

            // Poly Crystaline
                const polyCrystalineDrop = document.querySelector('.polyCrystaline-drop p')
                const polyCrystalineMenu = document.querySelector('.polyCrystaline-menu')

                polyCrystalineDrop.addEventListener('click', () => {
                    polyCrystalineMenu.classList.toggle('open')
                    // pvModuleDrop.classList.toggle('open')
                })

            // Mono Perc
                const monoPercDrop = document.querySelector('.monoPerc-drop p')
                const monoPercMenu = document.querySelector('.monoPerc-menu')

                monoPercDrop.addEventListener('click', () => {
                    monoPercMenu.classList.toggle('open')
                    // pvModuleDrop.classList.toggle('open')
                })

            // Bifacial
                const bifacialDrop = document.querySelector('.bifacial-drop p')
                const bifacialMenu = document.querySelector('.bifacial-menu')

                bifacialDrop.addEventListener('click', () => {
                    bifacialMenu.classList.toggle('open')
                    // pvModuleDrop.classList.toggle('open')
                })

            // DCR
                const dcrDrop = document.querySelector('.dcr-drop p')
                const dcrMenu = document.querySelector('.dcr-menu')

                dcrDrop.addEventListener('click', () => {
                    dcrMenu.classList.toggle('open')
                    // pvModuleDrop.classList.toggle('open')
                })
        
        // Solar Home Lightening System 
            const solarHomeLighteningDrop = document.querySelector('.solarHomeLightening-drop p')
            const solarHomeLighteningMenu = document.querySelector('.solarHomeLightening-menu')

            solarHomeLighteningDrop.addEventListener('click', () => {
                solarHomeLighteningMenu.classList.toggle('open')
            })

            //Traffic Signal Drop 
                const trafficSignalDrop = document.querySelector('.trafficSignal-drop p')
                const trafficSignalMenu = document.querySelector('.trafficSignal-menu')

                trafficSignalDrop.addEventListener('click', () => {
                    trafficSignalMenu.classList.toggle('open')
                })

    // ------------------------------------------------------------------------------------------------
    

    // Solutions Drop ---------------------------------------------------------------------------------

        const solutionsDrop = document.querySelector('.solutions-drop p')
        const solutionsMenu = document.querySelector('.solutions-menu')

        solutionsDrop.addEventListener('click', () => {
            solutionsMenu.classList.toggle('open')
        })


        // Products Below 20 KW
            const productsBelow20KwDrop = document.querySelector('.productsBelow20Kw-drop p')
            const productsBelow20KwMenu = document.querySelector('.productsBelow20Kw-menu')

            productsBelow20KwDrop.addEventListener('click', () => {
                productsBelow20KwMenu.classList.toggle('open')
            })
        // --------------------

        // Products Above 20 KW
            const productsAbove20KwDrop = document.querySelector('.productsAbove20Kw-drop p')
            const productsAbove20KwMenu = document.querySelector('.productsAbove20Kw-menu')

            productsAbove20KwDrop.addEventListener('click', () => {
                productsAbove20KwMenu.classList.toggle('open')
            })
        // --------------------

        // Operation and Maintainance
            const operationAndMaintainanceDrop = document.querySelector('.operationAndMaintainance-drop p')
            const operationAndMaintainanceMenu = document.querySelector('.operationAndMaintainance-menu')

            operationAndMaintainanceDrop.addEventListener('click', () => {
                operationAndMaintainanceMenu.classList.toggle('open')
            })


            // AMC--------
                const amcDrop = document.querySelector('.amc-drop p')
                const amcMenu = document.querySelector('.amc-menu')

                amcDrop.addEventListener('click', () => {
                    amcMenu.classList.toggle('open')
                })
            // -----------
        // --------------------

    
    // ------------------------------------------------------------------------------------------------

    // Downloads Drop --------------------------------------------------------------------------------

        const downloadsDrop = document.querySelector('.downloads-drop p')
        const downloadsMenu = document.querySelector('.downloads-menu')

        downloadsDrop.addEventListener('click', () => {
            downloadsMenu.classList.toggle('open')
        })

    // ----------------------------------------------------------------------------------------------


    // Achievements Drop --------------------------------------------------------------------------------

    const achievementsDrop = document.querySelector('.achievements-drop p')
    const achievementsMenu = document.querySelector('.achievements-menu')

    achievementsDrop.addEventListener('click', () => {
        achievementsMenu.classList.toggle('open')
    })

// ----------------------------------------------------------------------------------------------






// ----------------------------------------------------------------------------------------------------------------
