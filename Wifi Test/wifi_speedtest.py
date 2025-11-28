import speedtest as st

def test_wifi_speed():
    try:
        wifi_test = st.Speedtest()
        wifi_test.get_best_server()
        download_speed = wifi_test.download() / 1_000_000  # Convert to Mbps
        upload_speed = wifi_test.upload() / 1_000_000      # Convert to Mbps
        ping = wifi_test.results.ping
        
        print(f"Download Speed: {download_speed:.2f} Mbps")
        print(f"Upload Speed: {upload_speed:.2f} Mbps")
        print(f"Ping: {ping} ms")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        
if __name__ == "__main__":
    test_wifi_speed()