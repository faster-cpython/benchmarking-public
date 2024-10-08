# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: specialize_shadowed_
- machine: linux-x86_64
- commit hash: b0f4953
- commit date: 2024-08-16
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240816-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-b0f4953 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 254 ms: 1.08x faster                                                            |
| docutils       | 2.83 sec                                                   | 2.71 sec: 1.04x faster                                                          |
| html5lib       | 67.2 ms                                                    | 63.8 ms: 1.05x faster                                                           |
| tornado_http   | 94.6 ms                                                    | 90.3 ms: 1.05x faster                                                           |
| Geometric mean | (ref)                                                      | 1.06x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240816-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-b0f4953 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 323 ms: 1.17x faster                                                            |
| async_tree_memoization_tg  | 444 ms                                                     | 393 ms: 1.13x faster                                                            |
| async_tree_none_tg         | 336 ms                                                     | 301 ms: 1.12x faster                                                            |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 527 ms: 1.11x faster                                                            |
| async_tree_memoization     | 463 ms                                                     | 422 ms: 1.10x faster                                                            |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 560 ms: 1.09x faster                                                            |
| async_tree_io_tg           | 936 ms                                                     | 886 ms: 1.06x faster                                                            |
| async_tree_io              | 939 ms                                                     | 897 ms: 1.05x faster                                                            |
| Geometric mean             | (ref)                                                      | 1.10x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240816-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-b0f4953 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                            |
| nbody          | 88.3 ms                                                    | 88.1 ms: 1.00x faster                                                           |
| Geometric mean | (ref)                                                      | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240816-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-b0f4953 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 129 ms: 1.06x faster                                                            |
| regex_v8       | 25.1 ms                                                    | 25.0 ms: 1.00x faster                                                           |
| regex_effbot   | 3.67 ms                                                    | 3.68 ms: 1.00x slower                                                           |
| regex_dna      | 221 ms                                                     | 223 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                      | 1.01x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240816-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-b0f4953 |
|---------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_process   | 61.2 ms                                                    | 58.9 ms: 1.04x faster                                                           |
| xml_etree_parse     | 162 ms                                                     | 156 ms: 1.04x faster                                                            |
| json_dumps          | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                           |
| xml_etree_iterparse | 107 ms                                                     | 105 ms: 1.03x faster                                                            |
| xml_etree_generate  | 87.4 ms                                                    | 85.7 ms: 1.02x faster                                                           |
| json_loads          | 28.9 us                                                    | 28.5 us: 1.02x faster                                                           |
| pickle_pure_python  | 305 us                                                     | 302 us: 1.01x faster                                                            |
| tomli_loads         | 2.12 sec                                                   | 2.10 sec: 1.01x faster                                                          |
| Geometric mean      | (ref)                                                      | 1.02x faster                                                                    |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240816-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-b0f4953 |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                           |
| python_startup_no_site | 7.11 ms                                                    | 7.07 ms: 1.01x faster                                                           |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240816-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-b0f4953 |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 22.2 ms: 1.06x faster                                                           |
| genshi_xml      | 51.6 ms                                                    | 49.3 ms: 1.05x faster                                                           |
| django_template | 34.8 ms                                                    | 34.2 ms: 1.02x faster                                                           |
| mako            | 11.2 ms                                                    | 11.3 ms: 1.01x slower                                                           |
| Geometric mean  | (ref)                                                      | 1.03x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240816-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-b0f4953 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 260 us: 1.41x faster                                                            |
| deepcopy_memo              | 39.7 us                                                    | 30.1 us: 1.32x faster                                                           |
| deepcopy_reduce            | 3.35 us                                                    | 2.70 us: 1.24x faster                                                           |
| async_tree_none            | 378 ms                                                     | 323 ms: 1.17x faster                                                            |
| async_tree_memoization_tg  | 444 ms                                                     | 393 ms: 1.13x faster                                                            |
| async_tree_none_tg         | 336 ms                                                     | 301 ms: 1.12x faster                                                            |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.72 ms: 1.12x faster                                                           |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 527 ms: 1.11x faster                                                            |
| pathlib                    | 17.3 ms                                                    | 15.6 ms: 1.11x faster                                                           |
| coverage                   | 93.1 ms                                                    | 84.4 ms: 1.10x faster                                                           |
| async_tree_memoization     | 463 ms                                                     | 422 ms: 1.10x faster                                                            |
| richards                   | 50.9 ms                                                    | 46.5 ms: 1.09x faster                                                           |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 560 ms: 1.09x faster                                                            |
| richards_super             | 57.4 ms                                                    | 52.8 ms: 1.09x faster                                                           |
| scimark_fft                | 392 ms                                                     | 361 ms: 1.09x faster                                                            |
| crypto_pyaes               | 77.5 ms                                                    | 71.5 ms: 1.08x faster                                                           |
| 2to3                       | 274 ms                                                     | 254 ms: 1.08x faster                                                            |
| thrift                     | 823 us                                                     | 766 us: 1.07x faster                                                            |
| gc_traversal               | 3.98 ms                                                    | 3.71 ms: 1.07x faster                                                           |
| regex_compile              | 137 ms                                                     | 129 ms: 1.06x faster                                                            |
| genshi_text                | 23.7 ms                                                    | 22.2 ms: 1.06x faster                                                           |
| bench_thread_pool          | 834 us                                                     | 784 us: 1.06x faster                                                            |
| generators                 | 29.6 ms                                                    | 28.0 ms: 1.06x faster                                                           |
| async_tree_io_tg           | 936 ms                                                     | 886 ms: 1.06x faster                                                            |
| scimark_lu                 | 122 ms                                                     | 115 ms: 1.06x faster                                                            |
| asyncio_tcp                | 508 ms                                                     | 481 ms: 1.06x faster                                                            |
| html5lib                   | 67.2 ms                                                    | 63.8 ms: 1.05x faster                                                           |
| create_gc_cycles           | 1.82 ms                                                    | 1.73 ms: 1.05x faster                                                           |
| tornado_http               | 94.6 ms                                                    | 90.3 ms: 1.05x faster                                                           |
| genshi_xml                 | 51.6 ms                                                    | 49.3 ms: 1.05x faster                                                           |
| pprint_safe_repr           | 758 ms                                                     | 724 ms: 1.05x faster                                                            |
| logging_format             | 6.47 us                                                    | 6.18 us: 1.05x faster                                                           |
| chaos                      | 61.3 ms                                                    | 58.6 ms: 1.05x faster                                                           |
| async_tree_io              | 939 ms                                                     | 897 ms: 1.05x faster                                                            |
| pprint_pformat             | 1.56 sec                                                   | 1.49 sec: 1.05x faster                                                          |
| docutils                   | 2.83 sec                                                   | 2.71 sec: 1.04x faster                                                          |
| sympy_str                  | 282 ms                                                     | 271 ms: 1.04x faster                                                            |
| xml_etree_process          | 61.2 ms                                                    | 58.9 ms: 1.04x faster                                                           |
| bpe_tokeniser              | 5.02 sec                                                   | 4.84 sec: 1.04x faster                                                          |
| sympy_integrate            | 20.5 ms                                                    | 19.8 ms: 1.04x faster                                                           |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.04x faster                                                            |
| xml_etree_parse            | 162 ms                                                     | 156 ms: 1.04x faster                                                            |
| typing_runtime_protocols   | 165 us                                                     | 159 us: 1.04x faster                                                            |
| sqlglot_optimize           | 55.5 ms                                                    | 53.6 ms: 1.04x faster                                                           |
| logging_simple             | 5.74 us                                                    | 5.55 us: 1.04x faster                                                           |
| sympy_expand               | 473 ms                                                     | 457 ms: 1.03x faster                                                            |
| sympy_sum                  | 156 ms                                                     | 151 ms: 1.03x faster                                                            |
| spectral_norm              | 116 ms                                                     | 113 ms: 1.03x faster                                                            |
| sqlglot_transpile          | 1.63 ms                                                    | 1.59 ms: 1.03x faster                                                           |
| pyflate                    | 484 ms                                                     | 469 ms: 1.03x faster                                                            |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.79 sec: 1.03x faster                                                          |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                           |
| xml_etree_iterparse        | 107 ms                                                     | 105 ms: 1.03x faster                                                            |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                            |
| raytrace                   | 267 ms                                                     | 260 ms: 1.03x faster                                                            |
| pycparser                  | 1.16 sec                                                   | 1.13 sec: 1.03x faster                                                          |
| mdp                        | 2.79 sec                                                   | 2.72 sec: 1.02x faster                                                          |
| nqueens                    | 81.4 ms                                                    | 79.5 ms: 1.02x faster                                                           |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                           |
| sqlglot_parse              | 1.32 ms                                                    | 1.29 ms: 1.02x faster                                                           |
| xml_etree_generate         | 87.4 ms                                                    | 85.7 ms: 1.02x faster                                                           |
| async_generators           | 442 ms                                                     | 434 ms: 1.02x faster                                                            |
| go                         | 145 ms                                                     | 142 ms: 1.02x faster                                                            |
| django_template            | 34.8 ms                                                    | 34.2 ms: 1.02x faster                                                           |
| asyncio_websockets         | 567 ms                                                     | 558 ms: 1.02x faster                                                            |
| json_loads                 | 28.9 us                                                    | 28.5 us: 1.02x faster                                                           |
| sqlglot_normalize          | 110 ms                                                     | 109 ms: 1.02x faster                                                            |
| scimark_monte_carlo        | 69.2 ms                                                    | 68.3 ms: 1.01x faster                                                           |
| pickle_pure_python         | 305 us                                                     | 302 us: 1.01x faster                                                            |
| tomli_loads                | 2.12 sec                                                   | 2.10 sec: 1.01x faster                                                          |
| telco                      | 8.41 ms                                                    | 8.33 ms: 1.01x faster                                                           |
| deltablue                  | 3.25 ms                                                    | 3.22 ms: 1.01x faster                                                           |
| hexiom                     | 6.30 ms                                                    | 6.24 ms: 1.01x faster                                                           |
| python_startup_no_site     | 7.11 ms                                                    | 7.07 ms: 1.01x faster                                                           |
| regex_v8                   | 25.1 ms                                                    | 25.0 ms: 1.00x faster                                                           |
| nbody                      | 88.3 ms                                                    | 88.1 ms: 1.00x faster                                                           |
| regex_effbot               | 3.67 ms                                                    | 3.68 ms: 1.00x slower                                                           |
| fannkuch                   | 402 ms                                                     | 404 ms: 1.00x slower                                                            |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                           |
| regex_dna                  | 221 ms                                                     | 223 ms: 1.01x slower                                                            |
| mako                       | 11.2 ms                                                    | 11.3 ms: 1.01x slower                                                           |
| comprehensions             | 16.6 us                                                    | 16.7 us: 1.01x slower                                                           |
| scimark_sor                | 127 ms                                                     | 129 ms: 1.01x slower                                                            |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                                    |

Benchmark hidden because not significant (6): coroutines, pylint, unpickle_pure_python, float, json, logging_silent
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.01x