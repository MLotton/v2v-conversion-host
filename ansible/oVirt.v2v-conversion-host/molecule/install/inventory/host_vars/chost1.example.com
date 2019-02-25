v2v_host_type: openstack
v2v_transport_methods:
  # - vddk
  - ssh
v2v_max_concurrent_conversions: 20
#manageiq_provider_name: Shiny RHV
