v2v_host_type: openstack
v2v_transport_method: ssh
v2v_max_concurrent_conversions: 20
v2v_vddk_install_dir: /opt
v2v_ca_bundle: |
  -----BEGIN TRUSTED CERTIFICATE-----
  MIIDNzCCAh8CAQEwDQYJKoZIhvcNAQELBQAwYjELMAkGA1UEBhMCVVMxCzAJBgNV
  BAgMAk5DMRAwDgYDVQQHDAdSYWxlaWdoMRAwDgYDVQQKDAdSZWQgSEF0MQswCQYD
  VQQLDAJRRTEVMBMGA1UEAwwMMTkyLjE2OC4yNC4yMB4XDTE4MTEwODIyMzg0MVoX
  DTE5MTEwODIyMzg0MVowYTELMAkGA1UEBhMCVVMxCzAJBgNVBAgMAk5DMRAwDgYD
  VQQHDAdSYWxlaWdoMRAwDgYDVQQKDAdSZWQgSEF0MQswCQYDVQQLDAJRRTEUMBIG
  A1UEAwwLMTAuOC4xOTcuODQwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIB
  AQDCh0IIszxUjiR5YiBZDzYWFKircfiKXgw2o9K5V6J5Aqflnm2tUHl1jtucAwsk
  EoDIgc9Cf8UVS8gw5KBIFxJKnILhu1HGud/jrNtNZuBOq1WeMa8suSKSOg1tvH+k
  ltbzLMBFBz1x/AnzUkadpQQeaw58pP8kQIT/MTkw9i+yEwq2tjwer+806tWMpm0e
  eG27UbCVpel/ex6WTR5sUe0lmoRoVwpBkC0WQsip9Ly8aY0ZeHgnWIeNvf52olwW
  hEl7LhpRMUH0E24uEAo7+ChiNp7q640L0QWcEDfTYEwTyS+zy1/n0S0EWohWLyxR
  B7GDr+4z+dgztGCjKtKmTN2fAgMBAAEwDQYJKoZIhvcNAQELBQADggEBAIBMl35D
  onOMr1ZuKFMnl/x3LhJihRL5c1XZ2VTPx7P6fOeEoWwocuqW40BE+HLMXX9K4dUI
  fYEi/vRSh/8Obcirvobztl2KPripo1PXOLx82a8eTpQFubELqBKVVSUQkIIKpyIW
  Itbf/+4I08j9hXG1XGZtla05SEx9je5ntZI9DwsNRIe3ZNWeEoTZnG5cpXKoTuiv
  ZSBZV5uygZ6yGv7hnoqVRNXZP4OKE0ZdVt1TxbO0dBPjav6NdTpi7e9ZmVGKv9Xi
  drf/14FoGeDsU2zXLQ/UAqlzaAqx1NAtp99wnX3yI2dXJzGpVXdl0SJU6Hi5M+32
  PFjCzC1Et4Yl6sUwDQwLMTAuOC4xOTcuODQ=
  -----END TRUSTED CERTIFICATE-----
  -----BEGIN TRUSTED CERTIFICATE-----
  MIIDlzCCAn+gAwIBAgIJAOP7AaT7dsLYMA0GCSqGSIb3DQEBCwUAMGIxCzAJBgNV
  BAYTAlVTMQswCQYDVQQIDAJOQzEQMA4GA1UEBwwHUmFsZWlnaDEQMA4GA1UECgwH
  UmVkIEhBdDELMAkGA1UECwwCUUUxFTATBgNVBAMMDDE5Mi4xNjguMjQuMjAeFw0x
  ODExMDUyMTE3NTFaFw0xOTExMDUyMTE3NTFaMGIxCzAJBgNVBAYTAlVTMQswCQYD
  VQQIDAJOQzEQMA4GA1UEBwwHUmFsZWlnaDEQMA4GA1UECgwHUmVkIEhBdDELMAkG
  A1UECwwCUUUxFTATBgNVBAMMDDE5Mi4xNjguMjQuMjCCASIwDQYJKoZIhvcNAQEB
  BQADggEPADCCAQoCggEBAODRYemzQhGx2+8t0Peru6BEv2EFpxGKbav5p+6NzFXb
  50ccUIXA59+5vEEUr8EF8aCJuizBjAskPXwAT89qlbrsxKfN/r/xFOGvMkQ3xA2S
  ucnZCZXaVGkk/KC3VzPrd3atmPHWmAjTb37m4b1vKBRC9zh1F1l2CEyb31Eku4br
  gi4PwqoUQWIwiXPhD88YLuRKxdc079j7NRICBfJN68tzK81TW9cCQiOR7PdMuPzm
  h9nyNfYDeuGOuIFbpmL+8cLCofdMlyKtz/v+Y8s5bTtEf0ETG3qLYXskWM5nYYK+
  AkdKV3yZDrBha1X9Qo8wRcNZUas0kycXtZOXspPQ9AkCAwEAAaNQME4wHQYDVR0O
  BBYEFJzqK4CnpGbnQJIsN2te/jndZk2yMB8GA1UdIwQYMBaAFJzqK4CnpGbnQJIs
  N2te/jndZk2yMAwGA1UdEwQFMAMBAf8wDQYJKoZIhvcNAQELBQADggEBAJs+irLk
  osXnAqN8HwCp8NFGo2armdb/HE7v+qUanHRFfxDJJ70KhTM2gEi732u19oxhpgJP
  LNj40fC6U6A17oeNzGk+U75cOnbHY0Wovdo/2E8n508zsg0f+h8170QCKwf1qqd+
  o+AbxDIH6C262pF4AGjYQxK302Xj4Te+XckQa6nIX4xk1xJeHEzlxfBcV3h6BQH8
  sVqekffwgMFam9A66Ovcx8QgzZ2HpVnuq/CMY/sUxp0dK5PsnpKbUm6UCqaXigY7
  hgpqdqIdwkeR+c+fbYZKXBOBotCcmEXoHuIlZ9GhIti7gwSBSRWEjkPEL2j8R/zK
  k2ikyNbbVRx/13AwDgwMMTkyLjE2OC4yNC4y
  -----END TRUSTED CERTIFICATE-----
