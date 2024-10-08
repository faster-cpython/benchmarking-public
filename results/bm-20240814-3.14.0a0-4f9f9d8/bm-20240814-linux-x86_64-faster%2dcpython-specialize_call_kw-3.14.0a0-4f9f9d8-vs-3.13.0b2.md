# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: specialize_call_kw
- machine: linux-x86_64
- commit hash: 4f9f9d8
- commit date: 2024-08-14
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240814-linux-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-4f9f9d8 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 262 ms: 1.05x faster                                                          |
| docutils       | 2.83 sec                                                   | 2.73 sec: 1.04x faster                                                        |
| html5lib       | 67.2 ms                                                    | 64.2 ms: 1.05x faster                                                         |
| tornado_http   | 94.6 ms                                                    | 90.4 ms: 1.05x faster                                                         |
| Geometric mean | (ref)                                                      | 1.04x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240814-linux-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-4f9f9d8 |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 323 ms: 1.17x faster                                                          |
| async_tree_memoization_tg  | 444 ms                                                     | 392 ms: 1.13x faster                                                          |
| async_tree_none_tg         | 336 ms                                                     | 299 ms: 1.13x faster                                                          |
| async_tree_memoization     | 463 ms                                                     | 413 ms: 1.12x faster                                                          |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 533 ms: 1.10x faster                                                          |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 565 ms: 1.08x faster                                                          |
| async_tree_io_tg           | 936 ms                                                     | 889 ms: 1.05x faster                                                          |
| async_tree_io              | 939 ms                                                     | 898 ms: 1.05x faster                                                          |
| Geometric mean             | (ref)                                                      | 1.10x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240814-linux-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-4f9f9d8 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 187 ms: 1.03x faster                                                          |
| nbody          | 88.3 ms                                                    | 86.8 ms: 1.02x faster                                                         |
| float          | 78.9 ms                                                    | 78.3 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                      | 1.02x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240814-linux-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-4f9f9d8 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 130 ms: 1.05x faster                                                          |
| regex_dna      | 221 ms                                                     | 223 ms: 1.01x slower                                                          |
| regex_effbot   | 3.67 ms                                                    | 3.80 ms: 1.04x slower                                                         |
| regex_v8       | 25.1 ms                                                    | 26.2 ms: 1.05x slower                                                         |
| Geometric mean | (ref)                                                      | 1.01x slower                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240814-linux-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-4f9f9d8 |
|----------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 155 ms: 1.05x faster                                                          |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                         |
| tomli_loads          | 2.12 sec                                                   | 2.05 sec: 1.03x faster                                                        |
| xml_etree_iterparse  | 107 ms                                                     | 105 ms: 1.03x faster                                                          |
| unpickle_pure_python | 218 us                                                     | 212 us: 1.03x faster                                                          |
| xml_etree_process    | 61.2 ms                                                    | 60.1 ms: 1.02x faster                                                         |
| json_loads           | 28.9 us                                                    | 28.4 us: 1.02x faster                                                         |
| pickle_pure_python   | 305 us                                                     | 301 us: 1.01x faster                                                          |
| xml_etree_generate   | 87.4 ms                                                    | 86.8 ms: 1.01x faster                                                         |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240814-linux-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-4f9f9d8 |
|------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.03x faster                                                         |
| python_startup_no_site | 7.11 ms                                                    | 7.03 ms: 1.01x faster                                                         |
| Geometric mean         | (ref)                                                      | 1.02x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240814-linux-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-4f9f9d8 |
|-----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| django_template | 34.8 ms                                                    | 33.7 ms: 1.03x faster                                                         |
| genshi_text     | 23.7 ms                                                    | 23.3 ms: 1.01x faster                                                         |
| genshi_xml      | 51.6 ms                                                    | 51.2 ms: 1.01x faster                                                         |
| Geometric mean  | (ref)                                                      | 1.01x faster                                                                  |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240814-linux-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-4f9f9d8 |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 260 us: 1.41x faster                                                          |
| deepcopy_memo              | 39.7 us                                                    | 29.7 us: 1.34x faster                                                         |
| deepcopy_reduce            | 3.35 us                                                    | 2.66 us: 1.26x faster                                                         |
| async_tree_none            | 378 ms                                                     | 323 ms: 1.17x faster                                                          |
| async_tree_memoization_tg  | 444 ms                                                     | 392 ms: 1.13x faster                                                          |
| async_tree_none_tg         | 336 ms                                                     | 299 ms: 1.13x faster                                                          |
| async_tree_memoization     | 463 ms                                                     | 413 ms: 1.12x faster                                                          |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.74 ms: 1.11x faster                                                         |
| coverage                   | 93.1 ms                                                    | 83.8 ms: 1.11x faster                                                         |
| richards                   | 50.9 ms                                                    | 45.8 ms: 1.11x faster                                                         |
| richards_super             | 57.4 ms                                                    | 51.7 ms: 1.11x faster                                                         |
| pathlib                    | 17.3 ms                                                    | 15.7 ms: 1.11x faster                                                         |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 533 ms: 1.10x faster                                                          |
| mdp                        | 2.79 sec                                                   | 2.53 sec: 1.10x faster                                                        |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 565 ms: 1.08x faster                                                          |
| logging_silent             | 105 ns                                                     | 97.0 ns: 1.08x faster                                                         |
| scimark_lu                 | 122 ms                                                     | 113 ms: 1.08x faster                                                          |
| scimark_fft                | 392 ms                                                     | 364 ms: 1.08x faster                                                          |
| logging_format             | 6.47 us                                                    | 6.05 us: 1.07x faster                                                         |
| asyncio_tcp                | 508 ms                                                     | 478 ms: 1.06x faster                                                          |
| bench_thread_pool          | 834 us                                                     | 785 us: 1.06x faster                                                          |
| gc_traversal               | 3.98 ms                                                    | 3.75 ms: 1.06x faster                                                         |
| logging_simple             | 5.74 us                                                    | 5.42 us: 1.06x faster                                                         |
| crypto_pyaes               | 77.5 ms                                                    | 73.1 ms: 1.06x faster                                                         |
| thrift                     | 823 us                                                     | 781 us: 1.05x faster                                                          |
| async_tree_io_tg           | 936 ms                                                     | 889 ms: 1.05x faster                                                          |
| regex_compile              | 137 ms                                                     | 130 ms: 1.05x faster                                                          |
| raytrace                   | 267 ms                                                     | 254 ms: 1.05x faster                                                          |
| tornado_http               | 94.6 ms                                                    | 90.4 ms: 1.05x faster                                                         |
| html5lib                   | 67.2 ms                                                    | 64.2 ms: 1.05x faster                                                         |
| 2to3                       | 274 ms                                                     | 262 ms: 1.05x faster                                                          |
| async_tree_io              | 939 ms                                                     | 898 ms: 1.05x faster                                                          |
| hexiom                     | 6.30 ms                                                    | 6.02 ms: 1.05x faster                                                         |
| xml_etree_parse            | 162 ms                                                     | 155 ms: 1.05x faster                                                          |
| chaos                      | 61.3 ms                                                    | 58.7 ms: 1.05x faster                                                         |
| create_gc_cycles           | 1.82 ms                                                    | 1.74 ms: 1.04x faster                                                         |
| bpe_tokeniser              | 5.02 sec                                                   | 4.83 sec: 1.04x faster                                                        |
| generators                 | 29.6 ms                                                    | 28.5 ms: 1.04x faster                                                         |
| spectral_norm              | 116 ms                                                     | 112 ms: 1.04x faster                                                          |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.78 sec: 1.04x faster                                                        |
| sympy_str                  | 282 ms                                                     | 272 ms: 1.04x faster                                                          |
| sqlglot_optimize           | 55.5 ms                                                    | 53.6 ms: 1.04x faster                                                         |
| sympy_sum                  | 156 ms                                                     | 150 ms: 1.04x faster                                                          |
| nqueens                    | 81.4 ms                                                    | 78.6 ms: 1.04x faster                                                         |
| scimark_sor                | 127 ms                                                     | 123 ms: 1.04x faster                                                          |
| sqlglot_parse              | 1.32 ms                                                    | 1.28 ms: 1.04x faster                                                         |
| deltablue                  | 3.25 ms                                                    | 3.14 ms: 1.04x faster                                                         |
| docutils                   | 2.83 sec                                                   | 2.73 sec: 1.04x faster                                                        |
| sympy_integrate            | 20.5 ms                                                    | 19.8 ms: 1.03x faster                                                         |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                         |
| django_template            | 34.8 ms                                                    | 33.7 ms: 1.03x faster                                                         |
| tomli_loads                | 2.12 sec                                                   | 2.05 sec: 1.03x faster                                                        |
| telco                      | 8.41 ms                                                    | 8.16 ms: 1.03x faster                                                         |
| sqlglot_transpile          | 1.63 ms                                                    | 1.59 ms: 1.03x faster                                                         |
| pyflate                    | 484 ms                                                     | 470 ms: 1.03x faster                                                          |
| go                         | 145 ms                                                     | 141 ms: 1.03x faster                                                          |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.03x faster                                                         |
| xml_etree_iterparse        | 107 ms                                                     | 105 ms: 1.03x faster                                                          |
| unpickle_pure_python       | 218 us                                                     | 212 us: 1.03x faster                                                          |
| sympy_expand               | 473 ms                                                     | 461 ms: 1.03x faster                                                          |
| pidigits                   | 191 ms                                                     | 187 ms: 1.03x faster                                                          |
| scimark_monte_carlo        | 69.2 ms                                                    | 67.5 ms: 1.02x faster                                                         |
| pprint_pformat             | 1.56 sec                                                   | 1.52 sec: 1.02x faster                                                        |
| sqlglot_normalize          | 110 ms                                                     | 108 ms: 1.02x faster                                                          |
| pprint_safe_repr           | 758 ms                                                     | 742 ms: 1.02x faster                                                          |
| meteor_contest             | 110 ms                                                     | 108 ms: 1.02x faster                                                          |
| xml_etree_process          | 61.2 ms                                                    | 60.1 ms: 1.02x faster                                                         |
| async_generators           | 442 ms                                                     | 434 ms: 1.02x faster                                                          |
| nbody                      | 88.3 ms                                                    | 86.8 ms: 1.02x faster                                                         |
| asyncio_websockets         | 567 ms                                                     | 557 ms: 1.02x faster                                                          |
| json_loads                 | 28.9 us                                                    | 28.4 us: 1.02x faster                                                         |
| genshi_text                | 23.7 ms                                                    | 23.3 ms: 1.01x faster                                                         |
| pickle_pure_python         | 305 us                                                     | 301 us: 1.01x faster                                                          |
| json                       | 5.31 ms                                                    | 5.24 ms: 1.01x faster                                                         |
| python_startup_no_site     | 7.11 ms                                                    | 7.03 ms: 1.01x faster                                                         |
| coroutines                 | 23.2 ms                                                    | 22.9 ms: 1.01x faster                                                         |
| fannkuch                   | 402 ms                                                     | 398 ms: 1.01x faster                                                          |
| genshi_xml                 | 51.6 ms                                                    | 51.2 ms: 1.01x faster                                                         |
| typing_runtime_protocols   | 165 us                                                     | 163 us: 1.01x faster                                                          |
| xml_etree_generate         | 87.4 ms                                                    | 86.8 ms: 1.01x faster                                                         |
| float                      | 78.9 ms                                                    | 78.3 ms: 1.01x faster                                                         |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                         |
| regex_dna                  | 221 ms                                                     | 223 ms: 1.01x slower                                                          |
| pycparser                  | 1.16 sec                                                   | 1.18 sec: 1.02x slower                                                        |
| regex_effbot               | 3.67 ms                                                    | 3.80 ms: 1.04x slower                                                         |
| regex_v8                   | 25.1 ms                                                    | 26.2 ms: 1.05x slower                                                         |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                                  |

Benchmark hidden because not significant (3): pylint, mako, comprehensions
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.01x