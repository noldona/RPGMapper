db.createUser(
    {
        user: "mapper",
        pwd: "password",
        roles: [
            {
                role: "readWrite",
                db: "mapper"
            }
        ]
    }
)
