# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: use_attributes_to_gu
- machine: linux-x86_64
- commit hash: 3d7e23f
- commit date: 2024-08-05
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240805-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-3d7e23f |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 263 ms: 1.04x faster                                                            |
| docutils       | 2.83 sec                                                   | 2.74 sec: 1.03x faster                                                          |
| html5lib       | 67.2 ms                                                    | 66.0 ms: 1.02x faster                                                           |
| tornado_http   | 94.6 ms                                                    | 89.7 ms: 1.05x faster                                                           |
| Geometric mean | (ref)                                                      | 1.04x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240805-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-3d7e23f |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 323 ms: 1.17x faster                                                            |
| async_tree_memoization_tg  | 444 ms                                                     | 392 ms: 1.13x faster                                                            |
| async_tree_none_tg         | 336 ms                                                     | 300 ms: 1.12x faster                                                            |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 526 ms: 1.12x faster                                                            |
| async_tree_memoization     | 463 ms                                                     | 417 ms: 1.11x faster                                                            |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 558 ms: 1.09x faster                                                            |
| async_tree_io_tg           | 936 ms                                                     | 866 ms: 1.08x faster                                                            |
| async_tree_io              | 939 ms                                                     | 899 ms: 1.04x faster                                                            |
| Geometric mean             | (ref)                                                      | 1.11x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240805-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-3d7e23f |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 86.2 ms: 1.02x faster                                                           |
| pidigits       | 191 ms                                                     | 187 ms: 1.02x faster                                                            |
| float          | 78.9 ms                                                    | 77.8 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                      | 1.02x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240805-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-3d7e23f |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 132 ms: 1.04x faster                                                            |
| regex_v8       | 25.1 ms                                                    | 25.8 ms: 1.03x slower                                                           |
| regex_dna      | 221 ms                                                     | 229 ms: 1.04x slower                                                            |
| regex_effbot   | 3.67 ms                                                    | 3.87 ms: 1.06x slower                                                           |
| Geometric mean | (ref)                                                      | 1.02x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240805-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-3d7e23f |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 2.03 sec: 1.05x faster                                                          |
| json_loads           | 28.9 us                                                    | 27.8 us: 1.04x faster                                                           |
| xml_etree_parse      | 162 ms                                                     | 156 ms: 1.04x faster                                                            |
| unpickle_pure_python | 218 us                                                     | 211 us: 1.03x faster                                                            |
| xml_etree_process    | 61.2 ms                                                    | 59.4 ms: 1.03x faster                                                           |
| xml_etree_iterparse  | 107 ms                                                     | 105 ms: 1.03x faster                                                            |
| xml_etree_generate   | 87.4 ms                                                    | 85.5 ms: 1.02x faster                                                           |
| pickle_pure_python   | 305 us                                                     | 302 us: 1.01x faster                                                            |
| json_dumps           | 10.7 ms                                                    | 10.7 ms: 1.01x faster                                                           |
| Geometric mean       | (ref)                                                      | 1.03x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240805-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-3d7e23f |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                           |
| python_startup_no_site | 7.11 ms                                                    | 7.07 ms: 1.00x faster                                                           |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240805-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-3d7e23f |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 23.1 ms: 1.03x faster                                                           |
| django_template | 34.8 ms                                                    | 34.3 ms: 1.01x faster                                                           |
| genshi_xml      | 51.6 ms                                                    | 52.5 ms: 1.02x slower                                                           |
| Geometric mean  | (ref)                                                      | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240805-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-3d7e23f |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 263 us: 1.39x faster                                                            |
| deepcopy_memo              | 39.7 us                                                    | 28.6 us: 1.39x faster                                                           |
| go                         | 145 ms                                                     | 117 ms: 1.24x faster                                                            |
| deepcopy_reduce            | 3.35 us                                                    | 2.71 us: 1.23x faster                                                           |
| async_tree_none            | 378 ms                                                     | 323 ms: 1.17x faster                                                            |
| async_tree_memoization_tg  | 444 ms                                                     | 392 ms: 1.13x faster                                                            |
| async_tree_none_tg         | 336 ms                                                     | 300 ms: 1.12x faster                                                            |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 526 ms: 1.12x faster                                                            |
| richards_super             | 57.4 ms                                                    | 51.6 ms: 1.11x faster                                                           |
| async_tree_memoization     | 463 ms                                                     | 417 ms: 1.11x faster                                                            |
| richards                   | 50.9 ms                                                    | 45.9 ms: 1.11x faster                                                           |
| pathlib                    | 17.3 ms                                                    | 15.7 ms: 1.10x faster                                                           |
| scimark_fft                | 392 ms                                                     | 358 ms: 1.10x faster                                                            |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.81 ms: 1.10x faster                                                           |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 558 ms: 1.09x faster                                                            |
| async_tree_io_tg           | 936 ms                                                     | 866 ms: 1.08x faster                                                            |
| scimark_lu                 | 122 ms                                                     | 113 ms: 1.08x faster                                                            |
| crypto_pyaes               | 77.5 ms                                                    | 72.2 ms: 1.07x faster                                                           |
| logging_silent             | 105 ns                                                     | 98.0 ns: 1.07x faster                                                           |
| generators                 | 29.6 ms                                                    | 27.8 ms: 1.06x faster                                                           |
| bench_thread_pool          | 834 us                                                     | 785 us: 1.06x faster                                                            |
| chaos                      | 61.3 ms                                                    | 57.7 ms: 1.06x faster                                                           |
| gc_traversal               | 3.98 ms                                                    | 3.75 ms: 1.06x faster                                                           |
| tornado_http               | 94.6 ms                                                    | 89.7 ms: 1.05x faster                                                           |
| thrift                     | 823 us                                                     | 781 us: 1.05x faster                                                            |
| logging_format             | 6.47 us                                                    | 6.14 us: 1.05x faster                                                           |
| bpe_tokeniser              | 5.02 sec                                                   | 4.78 sec: 1.05x faster                                                          |
| sympy_integrate            | 20.5 ms                                                    | 19.5 ms: 1.05x faster                                                           |
| asyncio_tcp                | 508 ms                                                     | 485 ms: 1.05x faster                                                            |
| sqlglot_optimize           | 55.5 ms                                                    | 53.1 ms: 1.05x faster                                                           |
| sqlglot_transpile          | 1.63 ms                                                    | 1.56 ms: 1.05x faster                                                           |
| tomli_loads                | 2.12 sec                                                   | 2.03 sec: 1.05x faster                                                          |
| dask                       | 369 ms                                                     | 353 ms: 1.05x faster                                                            |
| async_tree_io              | 939 ms                                                     | 899 ms: 1.04x faster                                                            |
| 2to3                       | 274 ms                                                     | 263 ms: 1.04x faster                                                            |
| sympy_str                  | 282 ms                                                     | 271 ms: 1.04x faster                                                            |
| sqlglot_parse              | 1.32 ms                                                    | 1.27 ms: 1.04x faster                                                           |
| logging_simple             | 5.74 us                                                    | 5.51 us: 1.04x faster                                                           |
| sympy_sum                  | 156 ms                                                     | 150 ms: 1.04x faster                                                            |
| json_loads                 | 28.9 us                                                    | 27.8 us: 1.04x faster                                                           |
| create_gc_cycles           | 1.82 ms                                                    | 1.75 ms: 1.04x faster                                                           |
| raytrace                   | 267 ms                                                     | 257 ms: 1.04x faster                                                            |
| xml_etree_parse            | 162 ms                                                     | 156 ms: 1.04x faster                                                            |
| regex_compile              | 137 ms                                                     | 132 ms: 1.04x faster                                                            |
| sqlglot_normalize          | 110 ms                                                     | 106 ms: 1.04x faster                                                            |
| mdp                        | 2.79 sec                                                   | 2.69 sec: 1.04x faster                                                          |
| telco                      | 8.41 ms                                                    | 8.12 ms: 1.04x faster                                                           |
| sympy_expand               | 473 ms                                                     | 456 ms: 1.04x faster                                                            |
| pprint_pformat             | 1.56 sec                                                   | 1.50 sec: 1.04x faster                                                          |
| scimark_monte_carlo        | 69.2 ms                                                    | 66.8 ms: 1.04x faster                                                           |
| spectral_norm              | 116 ms                                                     | 112 ms: 1.03x faster                                                            |
| unpickle_pure_python       | 218 us                                                     | 211 us: 1.03x faster                                                            |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.79 sec: 1.03x faster                                                          |
| coverage                   | 93.1 ms                                                    | 90.3 ms: 1.03x faster                                                           |
| docutils                   | 2.83 sec                                                   | 2.74 sec: 1.03x faster                                                          |
| xml_etree_process          | 61.2 ms                                                    | 59.4 ms: 1.03x faster                                                           |
| pprint_safe_repr           | 758 ms                                                     | 737 ms: 1.03x faster                                                            |
| json                       | 5.31 ms                                                    | 5.16 ms: 1.03x faster                                                           |
| xml_etree_iterparse        | 107 ms                                                     | 105 ms: 1.03x faster                                                            |
| nqueens                    | 81.4 ms                                                    | 79.3 ms: 1.03x faster                                                           |
| genshi_text                | 23.7 ms                                                    | 23.1 ms: 1.03x faster                                                           |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                           |
| nbody                      | 88.3 ms                                                    | 86.2 ms: 1.02x faster                                                           |
| pyflate                    | 484 ms                                                     | 473 ms: 1.02x faster                                                            |
| xml_etree_generate         | 87.4 ms                                                    | 85.5 ms: 1.02x faster                                                           |
| pidigits                   | 191 ms                                                     | 187 ms: 1.02x faster                                                            |
| deltablue                  | 3.25 ms                                                    | 3.19 ms: 1.02x faster                                                           |
| hexiom                     | 6.30 ms                                                    | 6.18 ms: 1.02x faster                                                           |
| scimark_sor                | 127 ms                                                     | 125 ms: 1.02x faster                                                            |
| html5lib                   | 67.2 ms                                                    | 66.0 ms: 1.02x faster                                                           |
| meteor_contest             | 110 ms                                                     | 108 ms: 1.02x faster                                                            |
| async_generators           | 442 ms                                                     | 435 ms: 1.02x faster                                                            |
| django_template            | 34.8 ms                                                    | 34.3 ms: 1.01x faster                                                           |
| float                      | 78.9 ms                                                    | 77.8 ms: 1.01x faster                                                           |
| pickle_pure_python         | 305 us                                                     | 302 us: 1.01x faster                                                            |
| asyncio_websockets         | 567 ms                                                     | 560 ms: 1.01x faster                                                            |
| typing_runtime_protocols   | 165 us                                                     | 163 us: 1.01x faster                                                            |
| json_dumps                 | 10.7 ms                                                    | 10.7 ms: 1.01x faster                                                           |
| python_startup_no_site     | 7.11 ms                                                    | 7.07 ms: 1.00x faster                                                           |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.00x slower                                                           |
| fannkuch                   | 402 ms                                                     | 408 ms: 1.01x slower                                                            |
| genshi_xml                 | 51.6 ms                                                    | 52.5 ms: 1.02x slower                                                           |
| regex_v8                   | 25.1 ms                                                    | 25.8 ms: 1.03x slower                                                           |
| regex_dna                  | 221 ms                                                     | 229 ms: 1.04x slower                                                            |
| regex_effbot               | 3.67 ms                                                    | 3.87 ms: 1.06x slower                                                           |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                                    |

Benchmark hidden because not significant (5): pycparser, pylint, comprehensions, mako, coroutines
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.01x