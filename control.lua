require "util"

script.on_event(defines.events.on_built_entity, function(event)
    position = event.created_entity.bounding_box
    position = {x = (position.right_bottom.x + position.left_top.x) / 2 , y = (position.right_bottom.y + position.left_top.y) / 2}
    if event.created_entity.is_registered_for_construction() then
        item = event.created_entity.ghost_name
    else
        item = event.created_entity.name
    end
    facing = event.created_entity.direction
    game.print("placed " .. serpent.line(item) .. " at " .. serpent.line(position) .. " facing " .. facing)
    game.write_file("tasks.txt", "{\"build\", {x=" .. position.x .. ", y=" .. position.y .. "}, \"" .. item .. "\", " .. facing .. "}\n", true)
end)

script.on_event(defines.events.on_player_mined_entity, function(event)
    position = event.entity.bounding_box
    position = {x = (position.right_bottom.x + position.left_top.x) / 2 , y = (position.right_bottom.y + position.left_top.y) / 2}
    game.print("mined at " .. serpent.line(position))
    game.write_file("tasks.txt", "{\"mine\", {x=" .. position.x .. ", y=" .. position.y .. "}}\n", true)
end)
