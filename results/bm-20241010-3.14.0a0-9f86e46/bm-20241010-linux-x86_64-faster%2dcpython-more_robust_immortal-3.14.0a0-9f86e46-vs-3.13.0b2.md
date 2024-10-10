# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: more_robust_immortal
- machine: linux-x86_64
- commit hash: 9f86e46
- commit date: 2024-10-10
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241010-linux-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-9f86e46 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 254 ms: 1.08x faster                                                            |
| docutils       | 2.83 sec                                                   | 2.62 sec: 1.08x faster                                                          |
| html5lib       | 67.2 ms                                                    | 61.7 ms: 1.09x faster                                                           |
| tornado_http   | 94.6 ms                                                    | 90.4 ms: 1.05x faster                                                           |
| Geometric mean | (ref)                                                      | 1.07x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241010-linux-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-9f86e46 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization     | 463 ms                                                     | 396 ms: 1.17x faster                                                            |
| async_tree_none            | 378 ms                                                     | 325 ms: 1.16x faster                                                            |
| async_tree_memoization_tg  | 444 ms                                                     | 404 ms: 1.10x faster                                                            |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 559 ms: 1.09x faster                                                            |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 542 ms: 1.08x faster                                                            |
| async_tree_none_tg         | 336 ms                                                     | 312 ms: 1.08x faster                                                            |
| Geometric mean             | (ref)                                                      | 1.09x faster                                                                    |

Benchmark hidden because not significant (2): async_tree_io_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241010-linux-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-9f86e46 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 188 ms: 1.02x faster                                                            |
| nbody          | 88.3 ms                                                    | 92.7 ms: 1.05x slower                                                           |
| Geometric mean | (ref)                                                      | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241010-linux-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-9f86e46 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 129 ms: 1.06x faster                                                            |
| regex_v8       | 25.1 ms                                                    | 24.3 ms: 1.03x faster                                                           |
| regex_effbot   | 3.67 ms                                                    | 3.62 ms: 1.01x faster                                                           |
| regex_dna      | 221 ms                                                     | 222 ms: 1.00x slower                                                            |
| Geometric mean | (ref)                                                      | 1.03x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241010-linux-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-9f86e46 |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_loads           | 28.9 us                                                    | 26.3 us: 1.10x faster                                                           |
| xml_etree_parse      | 162 ms                                                     | 155 ms: 1.04x faster                                                            |
| unpickle_list        | 5.34 us                                                    | 5.19 us: 1.03x faster                                                           |
| xml_etree_iterparse  | 107 ms                                                     | 105 ms: 1.03x faster                                                            |
| xml_etree_process    | 61.2 ms                                                    | 59.6 ms: 1.03x faster                                                           |
| tomli_loads          | 2.12 sec                                                   | 2.08 sec: 1.02x faster                                                          |
| pickle_dict          | 34.8 us                                                    | 34.2 us: 1.02x faster                                                           |
| json_dumps           | 10.7 ms                                                    | 10.6 ms: 1.01x faster                                                           |
| xml_etree_generate   | 87.4 ms                                                    | 87.0 ms: 1.00x faster                                                           |
| pickle               | 11.5 us                                                    | 11.4 us: 1.00x faster                                                           |
| unpickle_pure_python | 218 us                                                     | 220 us: 1.01x slower                                                            |
| pickle_pure_python   | 305 us                                                     | 309 us: 1.01x slower                                                            |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                                    |

Benchmark hidden because not significant (2): unpickle, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241010-linux-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-9f86e46 |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                           |
| python_startup_no_site | 7.11 ms                                                    | 7.05 ms: 1.01x faster                                                           |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241010-linux-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-9f86e46 |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 51.6 ms                                                    | 49.1 ms: 1.05x faster                                                           |
| genshi_text     | 23.7 ms                                                    | 22.8 ms: 1.04x faster                                                           |
| django_template | 34.8 ms                                                    | 34.2 ms: 1.02x faster                                                           |
| mako            | 11.2 ms                                                    | 11.6 ms: 1.03x slower                                                           |
| Geometric mean  | (ref)                                                      | 1.02x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241010-linux-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-9f86e46 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 260 us: 1.41x faster                                                            |
| deepcopy_memo              | 39.7 us                                                    | 31.3 us: 1.27x faster                                                           |
| deepcopy_reduce            | 3.35 us                                                    | 2.66 us: 1.26x faster                                                           |
| go                         | 145 ms                                                     | 121 ms: 1.19x faster                                                            |
| async_tree_memoization     | 463 ms                                                     | 396 ms: 1.17x faster                                                            |
| async_tree_none            | 378 ms                                                     | 325 ms: 1.16x faster                                                            |
| mdp                        | 2.79 sec                                                   | 2.51 sec: 1.11x faster                                                          |
| coverage                   | 93.1 ms                                                    | 84.1 ms: 1.11x faster                                                           |
| generators                 | 29.6 ms                                                    | 26.9 ms: 1.10x faster                                                           |
| async_tree_memoization_tg  | 444 ms                                                     | 404 ms: 1.10x faster                                                            |
| json_loads                 | 28.9 us                                                    | 26.3 us: 1.10x faster                                                           |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.80 ms: 1.10x faster                                                           |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 559 ms: 1.09x faster                                                            |
| html5lib                   | 67.2 ms                                                    | 61.7 ms: 1.09x faster                                                           |
| richards                   | 50.9 ms                                                    | 46.8 ms: 1.09x faster                                                           |
| pathlib                    | 17.3 ms                                                    | 16.0 ms: 1.09x faster                                                           |
| richards_super             | 57.4 ms                                                    | 52.9 ms: 1.08x faster                                                           |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 542 ms: 1.08x faster                                                            |
| 2to3                       | 274 ms                                                     | 254 ms: 1.08x faster                                                            |
| docutils                   | 2.83 sec                                                   | 2.62 sec: 1.08x faster                                                          |
| async_tree_none_tg         | 336 ms                                                     | 312 ms: 1.08x faster                                                            |
| json                       | 5.31 ms                                                    | 4.93 ms: 1.08x faster                                                           |
| bpe_tokeniser              | 5.02 sec                                                   | 4.70 sec: 1.07x faster                                                          |
| asyncio_tcp                | 508 ms                                                     | 477 ms: 1.07x faster                                                            |
| regex_compile              | 137 ms                                                     | 129 ms: 1.06x faster                                                            |
| pyflate                    | 484 ms                                                     | 457 ms: 1.06x faster                                                            |
| crypto_pyaes               | 77.5 ms                                                    | 73.3 ms: 1.06x faster                                                           |
| thrift                     | 823 us                                                     | 780 us: 1.06x faster                                                            |
| sympy_sum                  | 156 ms                                                     | 148 ms: 1.05x faster                                                            |
| scimark_fft                | 392 ms                                                     | 373 ms: 1.05x faster                                                            |
| sympy_str                  | 282 ms                                                     | 268 ms: 1.05x faster                                                            |
| genshi_xml                 | 51.6 ms                                                    | 49.1 ms: 1.05x faster                                                           |
| telco                      | 8.41 ms                                                    | 8.01 ms: 1.05x faster                                                           |
| sqlite_synth               | 2.99 us                                                    | 2.85 us: 1.05x faster                                                           |
| scimark_lu                 | 122 ms                                                     | 116 ms: 1.05x faster                                                            |
| logging_format             | 6.47 us                                                    | 6.18 us: 1.05x faster                                                           |
| tornado_http               | 94.6 ms                                                    | 90.4 ms: 1.05x faster                                                           |
| pprint_safe_repr           | 758 ms                                                     | 725 ms: 1.05x faster                                                            |
| dulwich_log                | 67.2 ms                                                    | 64.3 ms: 1.04x faster                                                           |
| xml_etree_parse            | 162 ms                                                     | 155 ms: 1.04x faster                                                            |
| pprint_pformat             | 1.56 sec                                                   | 1.50 sec: 1.04x faster                                                          |
| genshi_text                | 23.7 ms                                                    | 22.8 ms: 1.04x faster                                                           |
| sqlglot_optimize           | 55.5 ms                                                    | 53.6 ms: 1.04x faster                                                           |
| typing_runtime_protocols   | 165 us                                                     | 159 us: 1.04x faster                                                            |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.78 sec: 1.03x faster                                                          |
| regex_v8                   | 25.1 ms                                                    | 24.3 ms: 1.03x faster                                                           |
| sqlglot_normalize          | 110 ms                                                     | 107 ms: 1.03x faster                                                            |
| sympy_integrate            | 20.5 ms                                                    | 19.9 ms: 1.03x faster                                                           |
| sympy_expand               | 473 ms                                                     | 458 ms: 1.03x faster                                                            |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.03x faster                                                            |
| unpickle_list              | 5.34 us                                                    | 5.19 us: 1.03x faster                                                           |
| xml_etree_iterparse        | 107 ms                                                     | 105 ms: 1.03x faster                                                            |
| logging_simple             | 5.74 us                                                    | 5.60 us: 1.03x faster                                                           |
| xml_etree_process          | 61.2 ms                                                    | 59.6 ms: 1.03x faster                                                           |
| sqlglot_transpile          | 1.63 ms                                                    | 1.60 ms: 1.02x faster                                                           |
| asyncio_websockets         | 567 ms                                                     | 555 ms: 1.02x faster                                                            |
| pidigits                   | 191 ms                                                     | 188 ms: 1.02x faster                                                            |
| create_gc_cycles           | 1.82 ms                                                    | 1.78 ms: 1.02x faster                                                           |
| tomli_loads                | 2.12 sec                                                   | 2.08 sec: 1.02x faster                                                          |
| chaos                      | 61.3 ms                                                    | 60.2 ms: 1.02x faster                                                           |
| pickle_dict                | 34.8 us                                                    | 34.2 us: 1.02x faster                                                           |
| django_template            | 34.8 ms                                                    | 34.2 ms: 1.02x faster                                                           |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                           |
| json_dumps                 | 10.7 ms                                                    | 10.6 ms: 1.01x faster                                                           |
| scimark_sor                | 127 ms                                                     | 126 ms: 1.01x faster                                                            |
| regex_effbot               | 3.67 ms                                                    | 3.62 ms: 1.01x faster                                                           |
| sqlglot_parse              | 1.32 ms                                                    | 1.30 ms: 1.01x faster                                                           |
| async_generators           | 442 ms                                                     | 437 ms: 1.01x faster                                                            |
| scimark_monte_carlo        | 69.2 ms                                                    | 68.5 ms: 1.01x faster                                                           |
| python_startup_no_site     | 7.11 ms                                                    | 7.05 ms: 1.01x faster                                                           |
| nqueens                    | 81.4 ms                                                    | 80.7 ms: 1.01x faster                                                           |
| spectral_norm              | 116 ms                                                     | 116 ms: 1.00x faster                                                            |
| xml_etree_generate         | 87.4 ms                                                    | 87.0 ms: 1.00x faster                                                           |
| pickle                     | 11.5 us                                                    | 11.4 us: 1.00x faster                                                           |
| gc_traversal               | 3.98 ms                                                    | 3.99 ms: 1.00x slower                                                           |
| fannkuch                   | 402 ms                                                     | 403 ms: 1.00x slower                                                            |
| regex_dna                  | 221 ms                                                     | 222 ms: 1.00x slower                                                            |
| unpickle_pure_python       | 218 us                                                     | 220 us: 1.01x slower                                                            |
| raytrace                   | 267 ms                                                     | 269 ms: 1.01x slower                                                            |
| pickle_pure_python         | 305 us                                                     | 309 us: 1.01x slower                                                            |
| comprehensions             | 16.6 us                                                    | 16.9 us: 1.02x slower                                                           |
| bench_thread_pool          | 834 us                                                     | 849 us: 1.02x slower                                                            |
| deltablue                  | 3.25 ms                                                    | 3.32 ms: 1.02x slower                                                           |
| coroutines                 | 23.2 ms                                                    | 23.8 ms: 1.03x slower                                                           |
| logging_silent             | 105 ns                                                     | 108 ns: 1.03x slower                                                            |
| mako                       | 11.2 ms                                                    | 11.6 ms: 1.03x slower                                                           |
| nbody                      | 88.3 ms                                                    | 92.7 ms: 1.05x slower                                                           |
| bench_mp_pool              | 23.9 ms                                                    | 56.3 ms: 2.36x slower                                                           |
| Geometric mean             | (ref)                                                      | 1.03x faster                                                                    |

Benchmark hidden because not significant (8): async_tree_io_tg, async_tree_io, float, hexiom, unpickle, pickle_list, pylint, pycparser
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241010-3.14.0a0-9f86e46/bm-20241010-linux-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-9f86e46.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.00x