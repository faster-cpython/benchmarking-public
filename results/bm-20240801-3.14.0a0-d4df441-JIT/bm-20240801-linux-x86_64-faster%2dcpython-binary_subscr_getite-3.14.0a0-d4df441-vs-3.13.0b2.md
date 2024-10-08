# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: binary_subscr_getite
- machine: linux-x86_64
- commit hash: d4df441
- commit date: 2024-08-01
- overall geometric mean: 1.05x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-d4df441 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 273 ms: 1.00x faster                                                            |
| docutils       | 2.83 sec                                                   | 2.91 sec: 1.03x slower                                                          |
| html5lib       | 67.2 ms                                                    | 63.8 ms: 1.05x faster                                                           |
| tornado_http   | 94.6 ms                                                    | 92.3 ms: 1.03x faster                                                           |
| Geometric mean | (ref)                                                      | 1.01x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-d4df441 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 327 ms: 1.16x faster                                                            |
| async_tree_memoization_tg  | 444 ms                                                     | 393 ms: 1.13x faster                                                            |
| async_tree_none_tg         | 336 ms                                                     | 302 ms: 1.11x faster                                                            |
| async_tree_memoization     | 463 ms                                                     | 422 ms: 1.10x faster                                                            |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 537 ms: 1.09x faster                                                            |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 566 ms: 1.08x faster                                                            |
| async_tree_io_tg           | 936 ms                                                     | 872 ms: 1.07x faster                                                            |
| async_tree_io              | 939 ms                                                     | 908 ms: 1.03x faster                                                            |
| Geometric mean             | (ref)                                                      | 1.10x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-d4df441 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 69.8 ms: 1.13x faster                                                           |
| nbody          | 88.3 ms                                                    | 79.6 ms: 1.11x faster                                                           |
| pidigits       | 191 ms                                                     | 185 ms: 1.03x faster                                                            |
| Geometric mean | (ref)                                                      | 1.09x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-d4df441 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 133 ms: 1.03x faster                                                            |
| regex_dna      | 221 ms                                                     | 230 ms: 1.04x slower                                                            |
| regex_effbot   | 3.67 ms                                                    | 3.89 ms: 1.06x slower                                                           |
| Geometric mean | (ref)                                                      | 1.02x slower                                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-d4df441 |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.91 sec: 1.11x faster                                                          |
| xml_etree_parse      | 162 ms                                                     | 146 ms: 1.11x faster                                                            |
| xml_etree_generate   | 87.4 ms                                                    | 79.3 ms: 1.10x faster                                                           |
| xml_etree_process    | 61.2 ms                                                    | 55.5 ms: 1.10x faster                                                           |
| xml_etree_iterparse  | 107 ms                                                     | 99.3 ms: 1.08x faster                                                           |
| json_dumps           | 10.7 ms                                                    | 10.2 ms: 1.05x faster                                                           |
| json_loads           | 28.9 us                                                    | 28.0 us: 1.03x faster                                                           |
| unpickle_pure_python | 218 us                                                     | 213 us: 1.02x faster                                                            |
| pickle_pure_python   | 305 us                                                     | 300 us: 1.02x faster                                                            |
| Geometric mean       | (ref)                                                      | 1.07x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-d4df441 |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                           |
| python_startup_no_site | 7.11 ms                                                    | 7.17 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                      | 1.00x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-d4df441 |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.92 ms: 1.13x faster                                                           |
| genshi_text     | 23.7 ms                                                    | 24.1 ms: 1.02x slower                                                           |
| genshi_xml      | 51.6 ms                                                    | 52.7 ms: 1.02x slower                                                           |
| django_template | 34.8 ms                                                    | 35.6 ms: 1.02x slower                                                           |
| Geometric mean  | (ref)                                                      | 1.02x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-d4df441 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 28.5 us: 1.39x faster                                                           |
| deepcopy                   | 367 us                                                     | 271 us: 1.35x faster                                                            |
| scimark_fft                | 392 ms                                                     | 306 ms: 1.28x faster                                                            |
| richards                   | 50.9 ms                                                    | 39.9 ms: 1.27x faster                                                           |
| deepcopy_reduce            | 3.35 us                                                    | 2.73 us: 1.22x faster                                                           |
| richards_super             | 57.4 ms                                                    | 46.9 ms: 1.22x faster                                                           |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.38 ms: 1.20x faster                                                           |
| async_tree_none            | 378 ms                                                     | 327 ms: 1.16x faster                                                            |
| scimark_monte_carlo        | 69.2 ms                                                    | 60.1 ms: 1.15x faster                                                           |
| crypto_pyaes               | 77.5 ms                                                    | 67.5 ms: 1.15x faster                                                           |
| mako                       | 11.2 ms                                                    | 9.92 ms: 1.13x faster                                                           |
| spectral_norm              | 116 ms                                                     | 103 ms: 1.13x faster                                                            |
| async_tree_memoization_tg  | 444 ms                                                     | 393 ms: 1.13x faster                                                            |
| float                      | 78.9 ms                                                    | 69.8 ms: 1.13x faster                                                           |
| scimark_lu                 | 122 ms                                                     | 109 ms: 1.11x faster                                                            |
| bpe_tokeniser              | 5.02 sec                                                   | 4.51 sec: 1.11x faster                                                          |
| scimark_sor                | 127 ms                                                     | 114 ms: 1.11x faster                                                            |
| tomli_loads                | 2.12 sec                                                   | 1.91 sec: 1.11x faster                                                          |
| pyflate                    | 484 ms                                                     | 435 ms: 1.11x faster                                                            |
| async_tree_none_tg         | 336 ms                                                     | 302 ms: 1.11x faster                                                            |
| nbody                      | 88.3 ms                                                    | 79.6 ms: 1.11x faster                                                           |
| xml_etree_parse            | 162 ms                                                     | 146 ms: 1.11x faster                                                            |
| xml_etree_generate         | 87.4 ms                                                    | 79.3 ms: 1.10x faster                                                           |
| xml_etree_process          | 61.2 ms                                                    | 55.5 ms: 1.10x faster                                                           |
| async_tree_memoization     | 463 ms                                                     | 422 ms: 1.10x faster                                                            |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 537 ms: 1.09x faster                                                            |
| xml_etree_iterparse        | 107 ms                                                     | 99.3 ms: 1.08x faster                                                           |
| gc_traversal               | 3.98 ms                                                    | 3.68 ms: 1.08x faster                                                           |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 566 ms: 1.08x faster                                                            |
| fannkuch                   | 402 ms                                                     | 372 ms: 1.08x faster                                                            |
| async_tree_io_tg           | 936 ms                                                     | 872 ms: 1.07x faster                                                            |
| pathlib                    | 17.3 ms                                                    | 16.2 ms: 1.07x faster                                                           |
| chaos                      | 61.3 ms                                                    | 57.4 ms: 1.07x faster                                                           |
| logging_format             | 6.47 us                                                    | 6.06 us: 1.07x faster                                                           |
| pprint_safe_repr           | 758 ms                                                     | 717 ms: 1.06x faster                                                            |
| telco                      | 8.41 ms                                                    | 7.97 ms: 1.06x faster                                                           |
| html5lib                   | 67.2 ms                                                    | 63.8 ms: 1.05x faster                                                           |
| pprint_pformat             | 1.56 sec                                                   | 1.48 sec: 1.05x faster                                                          |
| logging_simple             | 5.74 us                                                    | 5.46 us: 1.05x faster                                                           |
| json_dumps                 | 10.7 ms                                                    | 10.2 ms: 1.05x faster                                                           |
| thrift                     | 823 us                                                     | 788 us: 1.04x faster                                                            |
| logging_silent             | 105 ns                                                     | 101 ns: 1.04x faster                                                            |
| async_tree_io              | 939 ms                                                     | 908 ms: 1.03x faster                                                            |
| json_loads                 | 28.9 us                                                    | 28.0 us: 1.03x faster                                                           |
| create_gc_cycles           | 1.82 ms                                                    | 1.76 ms: 1.03x faster                                                           |
| pidigits                   | 191 ms                                                     | 185 ms: 1.03x faster                                                            |
| mdp                        | 2.79 sec                                                   | 2.70 sec: 1.03x faster                                                          |
| regex_compile              | 137 ms                                                     | 133 ms: 1.03x faster                                                            |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.03x faster                                                            |
| tornado_http               | 94.6 ms                                                    | 92.3 ms: 1.03x faster                                                           |
| coverage                   | 93.1 ms                                                    | 90.9 ms: 1.02x faster                                                           |
| unpickle_pure_python       | 218 us                                                     | 213 us: 1.02x faster                                                            |
| bench_thread_pool          | 834 us                                                     | 815 us: 1.02x faster                                                            |
| sqlglot_parse              | 1.32 ms                                                    | 1.29 ms: 1.02x faster                                                           |
| comprehensions             | 16.6 us                                                    | 16.3 us: 1.02x faster                                                           |
| asyncio_websockets         | 567 ms                                                     | 556 ms: 1.02x faster                                                            |
| raytrace                   | 267 ms                                                     | 262 ms: 1.02x faster                                                            |
| pickle_pure_python         | 305 us                                                     | 300 us: 1.02x faster                                                            |
| asyncio_tcp                | 508 ms                                                     | 499 ms: 1.02x faster                                                            |
| coroutines                 | 23.2 ms                                                    | 22.8 ms: 1.02x faster                                                           |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                                          |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                           |
| dask                       | 369 ms                                                     | 363 ms: 1.02x faster                                                            |
| sqlglot_transpile          | 1.63 ms                                                    | 1.62 ms: 1.01x faster                                                           |
| 2to3                       | 274 ms                                                     | 273 ms: 1.00x faster                                                            |
| sqlglot_optimize           | 55.5 ms                                                    | 55.4 ms: 1.00x faster                                                           |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                           |
| python_startup_no_site     | 7.11 ms                                                    | 7.17 ms: 1.01x slower                                                           |
| go                         | 145 ms                                                     | 146 ms: 1.01x slower                                                            |
| pycparser                  | 1.16 sec                                                   | 1.17 sec: 1.01x slower                                                          |
| genshi_text                | 23.7 ms                                                    | 24.1 ms: 1.02x slower                                                           |
| sqlglot_normalize          | 110 ms                                                     | 112 ms: 1.02x slower                                                            |
| genshi_xml                 | 51.6 ms                                                    | 52.7 ms: 1.02x slower                                                           |
| django_template            | 34.8 ms                                                    | 35.6 ms: 1.02x slower                                                           |
| docutils                   | 2.83 sec                                                   | 2.91 sec: 1.03x slower                                                          |
| regex_dna                  | 221 ms                                                     | 230 ms: 1.04x slower                                                            |
| nqueens                    | 81.4 ms                                                    | 84.6 ms: 1.04x slower                                                           |
| typing_runtime_protocols   | 165 us                                                     | 172 us: 1.04x slower                                                            |
| async_generators           | 442 ms                                                     | 463 ms: 1.05x slower                                                            |
| sympy_str                  | 282 ms                                                     | 299 ms: 1.06x slower                                                            |
| regex_effbot               | 3.67 ms                                                    | 3.89 ms: 1.06x slower                                                           |
| hexiom                     | 6.30 ms                                                    | 6.70 ms: 1.06x slower                                                           |
| sympy_expand               | 473 ms                                                     | 503 ms: 1.06x slower                                                            |
| deltablue                  | 3.25 ms                                                    | 3.49 ms: 1.07x slower                                                           |
| sympy_sum                  | 156 ms                                                     | 170 ms: 1.09x slower                                                            |
| sympy_integrate            | 20.5 ms                                                    | 22.4 ms: 1.09x slower                                                           |
| generators                 | 29.6 ms                                                    | 32.8 ms: 1.11x slower                                                           |
| pylint                     | 317 ms                                                     | 354 ms: 1.12x slower                                                            |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                                    |

Benchmark hidden because not significant (2): json, regex_v8
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.07x