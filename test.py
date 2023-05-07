from pyimagine import Imagine, Style, Ratio

if __name__ == "__main__":
    imagine = Imagine()

    img_data = imagine.sdprem(
        prompt="Woman sitting on a table, looking at the sky, seen from behind",
        style=Style.ANIME_V2,
        ratio=Ratio.RATIO_16X9
    )

    img_data = imagine.upscale(image=img_data)
    open("example.jpeg", mode="wb").write(img_data)
