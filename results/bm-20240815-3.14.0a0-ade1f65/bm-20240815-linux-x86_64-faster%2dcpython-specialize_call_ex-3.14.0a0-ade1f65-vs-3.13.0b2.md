# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: specialize_call_ex
- machine: linux-x86_64
- commit hash: ade1f65
- commit date: 2024-08-15
- overall geometric mean: 1.04x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-linux-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-ade1f65 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 262 ms: 1.05x faster                                                          |
| docutils       | 2.83 sec                                                   | 2.72 sec: 1.04x faster                                                        |
| html5lib       | 67.2 ms                                                    | 65.4 ms: 1.03x faster                                                         |
| tornado_http   | 94.6 ms                                                    | 90.1 ms: 1.05x faster                                                         |
| Geometric mean | (ref)                                                      | 1.04x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-linux-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-ade1f65 |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 327 ms: 1.16x faster                                                          |
| async_tree_memoization_tg  | 444 ms                                                     | 395 ms: 1.12x faster                                                          |
| async_tree_none_tg         | 336 ms                                                     | 301 ms: 1.12x faster                                                          |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 537 ms: 1.09x faster                                                          |
| async_tree_memoization     | 463 ms                                                     | 425 ms: 1.09x faster                                                          |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 570 ms: 1.07x faster                                                          |
| async_tree_io_tg           | 936 ms                                                     | 897 ms: 1.04x faster                                                          |
| async_tree_io              | 939 ms                                                     | 908 ms: 1.03x faster                                                          |
| Geometric mean             | (ref)                                                      | 1.09x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-linux-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-ade1f65 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 187 ms: 1.03x faster                                                          |
| nbody          | 88.3 ms                                                    | 86.9 ms: 1.02x faster                                                         |
| float          | 78.9 ms                                                    | 79.8 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                      | 1.01x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-linux-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-ade1f65 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 131 ms: 1.04x faster                                                          |
| regex_effbot   | 3.67 ms                                                    | 3.61 ms: 1.02x faster                                                         |
| regex_dna      | 221 ms                                                     | 222 ms: 1.01x slower                                                          |
| regex_v8       | 25.1 ms                                                    | 26.1 ms: 1.04x slower                                                         |
| Geometric mean | (ref)                                                      | 1.00x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-linux-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-ade1f65 |
|----------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 156 ms: 1.04x faster                                                          |
| xml_etree_process    | 61.2 ms                                                    | 59.2 ms: 1.03x faster                                                         |
| xml_etree_iterparse  | 107 ms                                                     | 104 ms: 1.03x faster                                                          |
| json_dumps           | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                                         |
| xml_etree_generate   | 87.4 ms                                                    | 86.2 ms: 1.01x faster                                                         |
| tomli_loads          | 2.12 sec                                                   | 2.09 sec: 1.01x faster                                                        |
| unpickle_pure_python | 218 us                                                     | 217 us: 1.01x faster                                                          |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                                  |

Benchmark hidden because not significant (2): json_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-linux-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-ade1f65 |
|------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.4 ms: 1.03x faster                                                         |
| python_startup_no_site | 7.11 ms                                                    | 7.03 ms: 1.01x faster                                                         |
| Geometric mean         | (ref)                                                      | 1.02x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-linux-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-ade1f65 |
|-----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_xml      | 51.6 ms                                                    | 50.5 ms: 1.02x faster                                                         |
| genshi_text     | 23.7 ms                                                    | 23.2 ms: 1.02x faster                                                         |
| django_template | 34.8 ms                                                    | 34.2 ms: 1.02x faster                                                         |
| mako            | 11.2 ms                                                    | 11.3 ms: 1.00x slower                                                         |
| Geometric mean  | (ref)                                                      | 1.01x faster                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-linux-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-ade1f65 |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 267 us: 1.37x faster                                                          |
| deepcopy_memo              | 39.7 us                                                    | 30.9 us: 1.28x faster                                                         |
| deepcopy_reduce            | 3.35 us                                                    | 2.70 us: 1.24x faster                                                         |
| async_tree_none            | 378 ms                                                     | 327 ms: 1.16x faster                                                          |
| async_tree_memoization_tg  | 444 ms                                                     | 395 ms: 1.12x faster                                                          |
| async_tree_none_tg         | 336 ms                                                     | 301 ms: 1.12x faster                                                          |
| mdp                        | 2.79 sec                                                   | 2.54 sec: 1.10x faster                                                        |
| coverage                   | 93.1 ms                                                    | 84.7 ms: 1.10x faster                                                         |
| richards                   | 50.9 ms                                                    | 46.4 ms: 1.10x faster                                                         |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 537 ms: 1.09x faster                                                          |
| pathlib                    | 17.3 ms                                                    | 15.9 ms: 1.09x faster                                                         |
| async_tree_memoization     | 463 ms                                                     | 425 ms: 1.09x faster                                                          |
| richards_super             | 57.4 ms                                                    | 52.8 ms: 1.09x faster                                                         |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 570 ms: 1.07x faster                                                          |
| scimark_lu                 | 122 ms                                                     | 114 ms: 1.07x faster                                                          |
| logging_format             | 6.47 us                                                    | 6.09 us: 1.06x faster                                                         |
| bench_thread_pool          | 834 us                                                     | 785 us: 1.06x faster                                                          |
| asyncio_tcp                | 508 ms                                                     | 479 ms: 1.06x faster                                                          |
| spectral_norm              | 116 ms                                                     | 109 ms: 1.06x faster                                                          |
| crypto_pyaes               | 77.5 ms                                                    | 73.1 ms: 1.06x faster                                                         |
| thrift                     | 823 us                                                     | 783 us: 1.05x faster                                                          |
| tornado_http               | 94.6 ms                                                    | 90.1 ms: 1.05x faster                                                         |
| scimark_fft                | 392 ms                                                     | 374 ms: 1.05x faster                                                          |
| pyflate                    | 484 ms                                                     | 462 ms: 1.05x faster                                                          |
| chaos                      | 61.3 ms                                                    | 58.5 ms: 1.05x faster                                                         |
| 2to3                       | 274 ms                                                     | 262 ms: 1.05x faster                                                          |
| regex_compile              | 137 ms                                                     | 131 ms: 1.04x faster                                                          |
| async_tree_io_tg           | 936 ms                                                     | 897 ms: 1.04x faster                                                          |
| bpe_tokeniser              | 5.02 sec                                                   | 4.83 sec: 1.04x faster                                                        |
| create_gc_cycles           | 1.82 ms                                                    | 1.75 ms: 1.04x faster                                                         |
| logging_simple             | 5.74 us                                                    | 5.52 us: 1.04x faster                                                         |
| gc_traversal               | 3.98 ms                                                    | 3.82 ms: 1.04x faster                                                         |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 5.07 ms: 1.04x faster                                                         |
| docutils                   | 2.83 sec                                                   | 2.72 sec: 1.04x faster                                                        |
| sympy_integrate            | 20.5 ms                                                    | 19.8 ms: 1.04x faster                                                         |
| generators                 | 29.6 ms                                                    | 28.6 ms: 1.04x faster                                                         |
| xml_etree_parse            | 162 ms                                                     | 156 ms: 1.04x faster                                                          |
| async_tree_io              | 939 ms                                                     | 908 ms: 1.03x faster                                                          |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.78 sec: 1.03x faster                                                        |
| xml_etree_process          | 61.2 ms                                                    | 59.2 ms: 1.03x faster                                                         |
| sqlglot_optimize           | 55.5 ms                                                    | 53.8 ms: 1.03x faster                                                         |
| sympy_sum                  | 156 ms                                                     | 151 ms: 1.03x faster                                                          |
| sqlglot_transpile          | 1.63 ms                                                    | 1.58 ms: 1.03x faster                                                         |
| telco                      | 8.41 ms                                                    | 8.16 ms: 1.03x faster                                                         |
| xml_etree_iterparse        | 107 ms                                                     | 104 ms: 1.03x faster                                                          |
| sympy_str                  | 282 ms                                                     | 274 ms: 1.03x faster                                                          |
| python_startup             | 10.8 ms                                                    | 10.4 ms: 1.03x faster                                                         |
| nqueens                    | 81.4 ms                                                    | 79.2 ms: 1.03x faster                                                         |
| raytrace                   | 267 ms                                                     | 259 ms: 1.03x faster                                                          |
| html5lib                   | 67.2 ms                                                    | 65.4 ms: 1.03x faster                                                         |
| sqlglot_parse              | 1.32 ms                                                    | 1.29 ms: 1.03x faster                                                         |
| pidigits                   | 191 ms                                                     | 187 ms: 1.03x faster                                                          |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.02x faster                                                          |
| sqlglot_normalize          | 110 ms                                                     | 108 ms: 1.02x faster                                                          |
| json_dumps                 | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                                         |
| genshi_xml                 | 51.6 ms                                                    | 50.5 ms: 1.02x faster                                                         |
| genshi_text                | 23.7 ms                                                    | 23.2 ms: 1.02x faster                                                         |
| hexiom                     | 6.30 ms                                                    | 6.17 ms: 1.02x faster                                                         |
| go                         | 145 ms                                                     | 142 ms: 1.02x faster                                                          |
| django_template            | 34.8 ms                                                    | 34.2 ms: 1.02x faster                                                         |
| regex_effbot               | 3.67 ms                                                    | 3.61 ms: 1.02x faster                                                         |
| sympy_expand               | 473 ms                                                     | 465 ms: 1.02x faster                                                          |
| nbody                      | 88.3 ms                                                    | 86.9 ms: 1.02x faster                                                         |
| fannkuch                   | 402 ms                                                     | 396 ms: 1.01x faster                                                          |
| xml_etree_generate         | 87.4 ms                                                    | 86.2 ms: 1.01x faster                                                         |
| tomli_loads                | 2.12 sec                                                   | 2.09 sec: 1.01x faster                                                        |
| python_startup_no_site     | 7.11 ms                                                    | 7.03 ms: 1.01x faster                                                         |
| asyncio_websockets         | 567 ms                                                     | 561 ms: 1.01x faster                                                          |
| scimark_monte_carlo        | 69.2 ms                                                    | 68.6 ms: 1.01x faster                                                         |
| pprint_pformat             | 1.56 sec                                                   | 1.54 sec: 1.01x faster                                                        |
| unpickle_pure_python       | 218 us                                                     | 217 us: 1.01x faster                                                          |
| pprint_safe_repr           | 758 ms                                                     | 754 ms: 1.01x faster                                                          |
| mako                       | 11.2 ms                                                    | 11.3 ms: 1.00x slower                                                         |
| async_generators           | 442 ms                                                     | 444 ms: 1.00x slower                                                          |
| regex_dna                  | 221 ms                                                     | 222 ms: 1.01x slower                                                          |
| comprehensions             | 16.6 us                                                    | 16.7 us: 1.01x slower                                                         |
| scimark_sor                | 127 ms                                                     | 129 ms: 1.01x slower                                                          |
| float                      | 78.9 ms                                                    | 79.8 ms: 1.01x slower                                                         |
| pycparser                  | 1.16 sec                                                   | 1.19 sec: 1.03x slower                                                        |
| regex_v8                   | 25.1 ms                                                    | 26.1 ms: 1.04x slower                                                         |
| Geometric mean             | (ref)                                                      | 1.04x faster                                                                  |

Benchmark hidden because not significant (9): json_loads, json, typing_runtime_protocols, pylint, deltablue, pickle_pure_python, coroutines, bench_mp_pool, logging_silent
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.01x