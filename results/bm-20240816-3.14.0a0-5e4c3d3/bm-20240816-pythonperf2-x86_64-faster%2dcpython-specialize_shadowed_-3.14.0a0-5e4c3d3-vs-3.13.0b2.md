# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: specialize_shadowed_
- machine: linux-x86_64
- commit hash: 5e4c3d3
- commit date: 2024-08-16
- overall geometric mean: 1.03x faster
- HPT reliability: 99.88%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240816-pythonperf2-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-5e4c3d3 |
|----------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 281 ms: 1.04x faster                                                                  |
| html5lib       | 74.7 ms                                                          | 72.7 ms: 1.03x faster                                                                 |
| tornado_http   | 119 ms                                                           | 116 ms: 1.03x faster                                                                  |
| Geometric mean | (ref)                                                            | 1.02x faster                                                                          |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240816-pythonperf2-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-5e4c3d3 |
|----------------------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_memoization     | 460 ms                                                           | 409 ms: 1.12x faster                                                                  |
| async_tree_io_tg           | 900 ms                                                           | 804 ms: 1.12x faster                                                                  |
| async_tree_none_tg         | 340 ms                                                           | 307 ms: 1.11x faster                                                                  |
| async_tree_none            | 365 ms                                                           | 338 ms: 1.08x faster                                                                  |
| async_tree_memoization_tg  | 421 ms                                                           | 389 ms: 1.08x faster                                                                  |
| async_tree_io              | 873 ms                                                           | 816 ms: 1.07x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 544 ms: 1.05x faster                                                                  |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 580 ms: 1.04x faster                                                                  |
| Geometric mean             | (ref)                                                            | 1.08x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240816-pythonperf2-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-5e4c3d3 |
|----------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| nbody          | 87.8 ms                                                          | 85.9 ms: 1.02x faster                                                                 |
| pidigits       | 254 ms                                                           | 253 ms: 1.00x faster                                                                  |
| Geometric mean | (ref)                                                            | 1.01x faster                                                                          |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240816-pythonperf2-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-5e4c3d3 |
|----------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                           | 139 ms: 1.03x faster                                                                  |
| regex_dna      | 249 ms                                                           | 254 ms: 1.02x slower                                                                  |
| regex_v8       | 26.0 ms                                                          | 27.1 ms: 1.04x slower                                                                 |
| regex_effbot   | 3.40 ms                                                          | 3.57 ms: 1.05x slower                                                                 |
| Geometric mean | (ref)                                                            | 1.02x slower                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240816-pythonperf2-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-5e4c3d3 |
|----------------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| tomli_loads          | 2.40 sec                                                         | 2.27 sec: 1.06x faster                                                                |
| xml_etree_iterparse  | 103 ms                                                           | 101 ms: 1.02x faster                                                                  |
| json_dumps           | 10.8 ms                                                          | 10.7 ms: 1.01x faster                                                                 |
| xml_etree_parse      | 144 ms                                                           | 143 ms: 1.01x faster                                                                  |
| xml_etree_process    | 59.7 ms                                                          | 59.4 ms: 1.01x faster                                                                 |
| json_loads           | 25.0 us                                                          | 25.4 us: 1.01x slower                                                                 |
| unpickle_pure_python | 224 us                                                           | 231 us: 1.03x slower                                                                  |
| pickle_pure_python   | 307 us                                                           | 317 us: 1.03x slower                                                                  |
| Geometric mean       | (ref)                                                            | 1.00x faster                                                                          |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240816-pythonperf2-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-5e4c3d3 |
|------------------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.3 ms: 1.00x slower                                                                 |
| python_startup_no_site | 8.85 ms                                                          | 9.00 ms: 1.02x slower                                                                 |
| Geometric mean         | (ref)                                                            | 1.01x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240816-pythonperf2-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-5e4c3d3 |
|-----------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 53.2 ms: 1.09x faster                                                                 |
| genshi_text     | 25.9 ms                                                          | 24.6 ms: 1.06x faster                                                                 |
| django_template | 39.0 ms                                                          | 39.3 ms: 1.01x slower                                                                 |
| mako            | 10.4 ms                                                          | 10.6 ms: 1.02x slower                                                                 |
| Geometric mean  | (ref)                                                            | 1.03x faster                                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240816-pythonperf2-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-5e4c3d3 |
|----------------------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| deepcopy                   | 377 us                                                           | 292 us: 1.29x faster                                                                  |
| deepcopy_memo              | 37.3 us                                                          | 29.2 us: 1.28x faster                                                                 |
| generators                 | 33.5 ms                                                          | 28.4 ms: 1.18x faster                                                                 |
| deepcopy_reduce            | 3.39 us                                                          | 2.96 us: 1.14x faster                                                                 |
| async_tree_memoization     | 460 ms                                                           | 409 ms: 1.12x faster                                                                  |
| async_tree_io_tg           | 900 ms                                                           | 804 ms: 1.12x faster                                                                  |
| async_tree_none_tg         | 340 ms                                                           | 307 ms: 1.11x faster                                                                  |
| richards_super             | 61.2 ms                                                          | 55.9 ms: 1.09x faster                                                                 |
| genshi_xml                 | 58.1 ms                                                          | 53.2 ms: 1.09x faster                                                                 |
| bench_mp_pool              | 4.91 ms                                                          | 4.54 ms: 1.08x faster                                                                 |
| async_tree_none            | 365 ms                                                           | 338 ms: 1.08x faster                                                                  |
| async_tree_memoization_tg  | 421 ms                                                           | 389 ms: 1.08x faster                                                                  |
| pathlib                    | 17.1 ms                                                          | 15.9 ms: 1.08x faster                                                                 |
| scimark_sor                | 119 ms                                                           | 110 ms: 1.07x faster                                                                  |
| async_tree_io              | 873 ms                                                           | 816 ms: 1.07x faster                                                                  |
| richards                   | 53.4 ms                                                          | 50.1 ms: 1.07x faster                                                                 |
| tomli_loads                | 2.40 sec                                                         | 2.27 sec: 1.06x faster                                                                |
| genshi_text                | 25.9 ms                                                          | 24.6 ms: 1.06x faster                                                                 |
| bench_thread_pool          | 908 us                                                           | 862 us: 1.05x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 544 ms: 1.05x faster                                                                  |
| telco                      | 8.40 ms                                                          | 8.00 ms: 1.05x faster                                                                 |
| coverage                   | 83.5 ms                                                          | 79.8 ms: 1.05x faster                                                                 |
| gc_traversal               | 4.69 ms                                                          | 4.49 ms: 1.04x faster                                                                 |
| bpe_tokeniser              | 5.14 sec                                                         | 4.93 sec: 1.04x faster                                                                |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 580 ms: 1.04x faster                                                                  |
| 2to3                       | 291 ms                                                           | 281 ms: 1.04x faster                                                                  |
| regex_compile              | 144 ms                                                           | 139 ms: 1.03x faster                                                                  |
| scimark_lu                 | 97.5 ms                                                          | 94.4 ms: 1.03x faster                                                                 |
| logging_format             | 7.11 us                                                          | 6.89 us: 1.03x faster                                                                 |
| tornado_http               | 119 ms                                                           | 116 ms: 1.03x faster                                                                  |
| html5lib                   | 74.7 ms                                                          | 72.7 ms: 1.03x faster                                                                 |
| go                         | 165 ms                                                           | 161 ms: 1.02x faster                                                                  |
| async_generators           | 363 ms                                                           | 355 ms: 1.02x faster                                                                  |
| logging_simple             | 6.40 us                                                          | 6.26 us: 1.02x faster                                                                 |
| nbody                      | 87.8 ms                                                          | 85.9 ms: 1.02x faster                                                                 |
| asyncio_websockets         | 395 ms                                                           | 387 ms: 1.02x faster                                                                  |
| xml_etree_iterparse        | 103 ms                                                           | 101 ms: 1.02x faster                                                                  |
| hexiom                     | 6.35 ms                                                          | 6.24 ms: 1.02x faster                                                                 |
| scimark_monte_carlo        | 65.5 ms                                                          | 64.4 ms: 1.02x faster                                                                 |
| meteor_contest             | 128 ms                                                           | 126 ms: 1.01x faster                                                                  |
| json_dumps                 | 10.8 ms                                                          | 10.7 ms: 1.01x faster                                                                 |
| thrift                     | 880 us                                                           | 871 us: 1.01x faster                                                                  |
| asyncio_tcp                | 378 ms                                                           | 374 ms: 1.01x faster                                                                  |
| crypto_pyaes               | 73.6 ms                                                          | 72.9 ms: 1.01x faster                                                                 |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.25 ms: 1.01x faster                                                                 |
| xml_etree_parse            | 144 ms                                                           | 143 ms: 1.01x faster                                                                  |
| xml_etree_process          | 59.7 ms                                                          | 59.4 ms: 1.01x faster                                                                 |
| deltablue                  | 3.37 ms                                                          | 3.36 ms: 1.01x faster                                                                 |
| pidigits                   | 254 ms                                                           | 253 ms: 1.00x faster                                                                  |
| spectral_norm              | 97.3 ms                                                          | 97.6 ms: 1.00x slower                                                                 |
| sqlglot_optimize           | 59.5 ms                                                          | 59.7 ms: 1.00x slower                                                                 |
| python_startup             | 13.2 ms                                                          | 13.3 ms: 1.00x slower                                                                 |
| pyflate                    | 482 ms                                                           | 484 ms: 1.01x slower                                                                  |
| sympy_integrate            | 23.2 ms                                                          | 23.3 ms: 1.01x slower                                                                 |
| sqlglot_normalize          | 120 ms                                                           | 121 ms: 1.01x slower                                                                  |
| pprint_safe_repr           | 818 ms                                                           | 824 ms: 1.01x slower                                                                  |
| django_template            | 39.0 ms                                                          | 39.3 ms: 1.01x slower                                                                 |
| comprehensions             | 17.0 us                                                          | 17.1 us: 1.01x slower                                                                 |
| json                       | 5.35 ms                                                          | 5.41 ms: 1.01x slower                                                                 |
| sqlglot_parse              | 1.39 ms                                                          | 1.41 ms: 1.01x slower                                                                 |
| fannkuch                   | 353 ms                                                           | 357 ms: 1.01x slower                                                                  |
| json_loads                 | 25.0 us                                                          | 25.4 us: 1.01x slower                                                                 |
| sqlglot_transpile          | 1.76 ms                                                          | 1.79 ms: 1.01x slower                                                                 |
| pprint_pformat             | 1.66 sec                                                         | 1.68 sec: 1.01x slower                                                                |
| python_startup_no_site     | 8.85 ms                                                          | 9.00 ms: 1.02x slower                                                                 |
| logging_silent             | 96.3 ns                                                          | 97.9 ns: 1.02x slower                                                                 |
| mako                       | 10.4 ms                                                          | 10.6 ms: 1.02x slower                                                                 |
| regex_dna                  | 249 ms                                                           | 254 ms: 1.02x slower                                                                  |
| mdp                        | 2.46 sec                                                         | 2.52 sec: 1.02x slower                                                                |
| chaos                      | 59.6 ms                                                          | 61.3 ms: 1.03x slower                                                                 |
| unpickle_pure_python       | 224 us                                                           | 231 us: 1.03x slower                                                                  |
| pickle_pure_python         | 307 us                                                           | 317 us: 1.03x slower                                                                  |
| nqueens                    | 88.4 ms                                                          | 91.8 ms: 1.04x slower                                                                 |
| regex_v8                   | 26.0 ms                                                          | 27.1 ms: 1.04x slower                                                                 |
| raytrace                   | 260 ms                                                           | 271 ms: 1.04x slower                                                                  |
| regex_effbot               | 3.40 ms                                                          | 3.57 ms: 1.05x slower                                                                 |
| Geometric mean             | (ref)                                                            | 1.03x faster                                                                          |

Benchmark hidden because not significant (13): scimark_fft, create_gc_cycles, float, sympy_str, docutils, xml_etree_generate, sympy_sum, pycparser, asyncio_tcp_ssl, sympy_expand, coroutines, typing_runtime_protocols, pylint
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.88% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x