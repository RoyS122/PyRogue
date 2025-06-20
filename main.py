from rogue_engine.game import Game
from rogue_engine.camera import Camera

import pyglet
from pyglet import gl
import ctypes

from pyglet.window import key

from pyglet.gl import (
    GL_NEAREST,
    glTexParameteri,
    GL_TEXTURE_2D,
    GL_TEXTURE_MIN_FILTER,
    GL_TEXTURE_MAG_FILTER
    )
# === Initialisation du jeu ===
game = Game(60, 30)
cam = Camera(game.player.x, 20, game.player.y, 20)
window = pyglet.window.Window(1200, 720, "PyRogue")

game.player.init_sprite()

glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

# === Shader GLSL ===
fragment_shader_source = """
#version 120
uniform sampler2D texture;
uniform vec2 resolution;

void main() {
    vec2 uv = gl_TexCoord[0].xy;
    vec4 base_color = texture2D(texture, uv);

    // Calcul de la luminosité du pixel
    float brightness = dot(base_color.rgb, vec3(0.299, 0.587, 0.114));
    float glow_threshold = 0.3; // Plus bas = plus de pixels brillent

    vec4 glow = vec4(0.0);
    float offset = 1.0 / 256.0; // Plus large = glow plus diffus

    // Appliquer un flou autour des pixels lumineux
    if (brightness > glow_threshold) {
        for (int x = -2; x <= 2; x++) {
            for (int y = -2; y <= 2; y++) {
                vec2 sample_uv = uv + vec2(x, y) * offset;
                glow += texture2D(texture, sample_uv);
            }
        }
        glow /= 25.0;
    }

    // Mélange entre la couleur de base et le glow
    vec4 final_color = mix(base_color, glow, 0.7); // Plus haut = glow plus intense

    gl_FragColor = final_color;
}

"""

# === Compilation du shader ===
def create_shader(source):
    shader = gl.glCreateShader(gl.GL_FRAGMENT_SHADER)
    src_buffer = ctypes.create_string_buffer(source.encode('utf-8'))
    buf_pointer = ctypes.cast(ctypes.pointer(ctypes.pointer(src_buffer)), ctypes.POINTER(ctypes.POINTER(gl.GLchar)))
    length = ctypes.c_int(len(source))
    gl.glShaderSource(shader, 1, buf_pointer, ctypes.byref(length))
    gl.glCompileShader(shader)

    # Vérification de la compilation
    compile_status = ctypes.c_int()
    gl.glGetShaderiv(shader, gl.GL_COMPILE_STATUS, ctypes.byref(compile_status))
    if not compile_status.value:
        log_length = ctypes.c_int()
        gl.glGetShaderiv(shader, gl.GL_INFO_LOG_LENGTH, ctypes.byref(log_length))
        log = ctypes.create_string_buffer(log_length.value)
        gl.glGetShaderInfoLog(shader, log_length, None, log)
        print("Shader compilation failed:\n", log.value.decode())
        raise RuntimeError("Shader compilation failed")

    return shader

# === Création et activation du programme shader ===
shader = create_shader(fragment_shader_source)
program = gl.glCreateProgram()
gl.glAttachShader(program, shader)
gl.glLinkProgram(program)

# === Rendu avec shader ===
@window.event
def on_draw():
    window.clear()
    gl.glUseProgram(program)

    # Uniforms
    res_loc = gl.glGetUniformLocation(program, b"resolution")
    gl.glUniform2f(res_loc, window.width, window.height)

    # Dessin du jeu
    game.player.draw(window.height, tile_size=game.tile_size, camera=cam)
    game.map.draw(window.height, cam)

    gl.glUseProgram(0)

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.ESCAPE:
        print("Touche Échap pressée")

@window.event
def on_key_release(symbol, modifiers):
    game.on_key_release(symbol)
    cam.x = game.player.x - cam.x_offset // 2
    cam.y = game.player.y - cam.y_offset // 2
   


pyglet.app.run()
