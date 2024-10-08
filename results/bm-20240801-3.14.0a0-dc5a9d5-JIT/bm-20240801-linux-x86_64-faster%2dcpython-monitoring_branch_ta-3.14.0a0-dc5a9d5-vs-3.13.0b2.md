# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: monitoring_branch_ta
- machine: linux-x86_64
- commit hash: dc5a9d5
- commit date: 2024-08-01
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-linux-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 273 ms: 1.00x faster                                                            |
| docutils       | 2.83 sec                                                   | 2.90 sec: 1.03x slower                                                          |
| html5lib       | 67.2 ms                                                    | 64.2 ms: 1.05x faster                                                           |
| tornado_http   | 94.6 ms                                                    | 92.1 ms: 1.03x faster                                                           |
| Geometric mean | (ref)                                                      | 1.01x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-linux-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 326 ms: 1.16x faster                                                            |
| async_tree_memoization_tg  | 444 ms                                                     | 390 ms: 1.14x faster                                                            |
| async_tree_memoization     | 463 ms                                                     | 410 ms: 1.13x faster                                                            |
| async_tree_none_tg         | 336 ms                                                     | 299 ms: 1.12x faster                                                            |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 531 ms: 1.11x faster                                                            |
| async_tree_io_tg           | 936 ms                                                     | 860 ms: 1.09x faster                                                            |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 563 ms: 1.09x faster                                                            |
| async_tree_io              | 939 ms                                                     | 903 ms: 1.04x faster                                                            |
| Geometric mean             | (ref)                                                      | 1.11x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-linux-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.4 ms: 1.12x faster                                                           |
| nbody          | 88.3 ms                                                    | 79.4 ms: 1.11x faster                                                           |
| pidigits       | 191 ms                                                     | 185 ms: 1.03x faster                                                            |
| Geometric mean | (ref)                                                      | 1.09x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-linux-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 134 ms: 1.02x faster                                                            |
| regex_v8       | 25.1 ms                                                    | 24.8 ms: 1.01x faster                                                           |
| regex_effbot   | 3.67 ms                                                    | 3.70 ms: 1.01x slower                                                           |
| regex_dna      | 221 ms                                                     | 227 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                      | 1.00x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-linux-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 146 ms: 1.11x faster                                                            |
| xml_etree_process    | 61.2 ms                                                    | 55.3 ms: 1.11x faster                                                           |
| xml_etree_generate   | 87.4 ms                                                    | 79.2 ms: 1.10x faster                                                           |
| tomli_loads          | 2.12 sec                                                   | 1.92 sec: 1.10x faster                                                          |
| xml_etree_iterparse  | 107 ms                                                     | 99.2 ms: 1.08x faster                                                           |
| json_dumps           | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                           |
| json_loads           | 28.9 us                                                    | 27.8 us: 1.04x faster                                                           |
| pickle_pure_python   | 305 us                                                     | 295 us: 1.04x faster                                                            |
| unpickle_pure_python | 218 us                                                     | 216 us: 1.01x faster                                                            |
| Geometric mean       | (ref)                                                      | 1.07x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-linux-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                           |
| python_startup_no_site | 7.11 ms                                                    | 7.16 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-linux-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.92 ms: 1.13x faster                                                           |
| genshi_text     | 23.7 ms                                                    | 24.2 ms: 1.02x slower                                                           |
| django_template | 34.8 ms                                                    | 35.9 ms: 1.03x slower                                                           |
| genshi_xml      | 51.6 ms                                                    | 53.9 ms: 1.05x slower                                                           |
| Geometric mean  | (ref)                                                      | 1.01x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-linux-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 28.8 us: 1.38x faster                                                           |
| deepcopy                   | 367 us                                                     | 273 us: 1.35x faster                                                            |
| scimark_fft                | 392 ms                                                     | 308 ms: 1.28x faster                                                            |
| richards                   | 50.9 ms                                                    | 40.4 ms: 1.26x faster                                                           |
| richards_super             | 57.4 ms                                                    | 46.5 ms: 1.23x faster                                                           |
| deepcopy_reduce            | 3.35 us                                                    | 2.77 us: 1.21x faster                                                           |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.39 ms: 1.20x faster                                                           |
| async_tree_none            | 378 ms                                                     | 326 ms: 1.16x faster                                                            |
| scimark_monte_carlo        | 69.2 ms                                                    | 59.9 ms: 1.15x faster                                                           |
| crypto_pyaes               | 77.5 ms                                                    | 67.9 ms: 1.14x faster                                                           |
| spectral_norm              | 116 ms                                                     | 102 ms: 1.14x faster                                                            |
| async_tree_memoization_tg  | 444 ms                                                     | 390 ms: 1.14x faster                                                            |
| pyflate                    | 484 ms                                                     | 427 ms: 1.13x faster                                                            |
| mako                       | 11.2 ms                                                    | 9.92 ms: 1.13x faster                                                           |
| async_tree_memoization     | 463 ms                                                     | 410 ms: 1.13x faster                                                            |
| async_tree_none_tg         | 336 ms                                                     | 299 ms: 1.12x faster                                                            |
| float                      | 78.9 ms                                                    | 70.4 ms: 1.12x faster                                                           |
| bpe_tokeniser              | 5.02 sec                                                   | 4.51 sec: 1.11x faster                                                          |
| nbody                      | 88.3 ms                                                    | 79.4 ms: 1.11x faster                                                           |
| xml_etree_parse            | 162 ms                                                     | 146 ms: 1.11x faster                                                            |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 531 ms: 1.11x faster                                                            |
| xml_etree_process          | 61.2 ms                                                    | 55.3 ms: 1.11x faster                                                           |
| fannkuch                   | 402 ms                                                     | 364 ms: 1.10x faster                                                            |
| xml_etree_generate         | 87.4 ms                                                    | 79.2 ms: 1.10x faster                                                           |
| tomli_loads                | 2.12 sec                                                   | 1.92 sec: 1.10x faster                                                          |
| mdp                        | 2.79 sec                                                   | 2.55 sec: 1.09x faster                                                          |
| async_tree_io_tg           | 936 ms                                                     | 860 ms: 1.09x faster                                                            |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 563 ms: 1.09x faster                                                            |
| pathlib                    | 17.3 ms                                                    | 16.0 ms: 1.08x faster                                                           |
| xml_etree_iterparse        | 107 ms                                                     | 99.2 ms: 1.08x faster                                                           |
| logging_format             | 6.47 us                                                    | 6.00 us: 1.08x faster                                                           |
| chaos                      | 61.3 ms                                                    | 57.6 ms: 1.06x faster                                                           |
| logging_simple             | 5.74 us                                                    | 5.47 us: 1.05x faster                                                           |
| meteor_contest             | 110 ms                                                     | 105 ms: 1.05x faster                                                            |
| html5lib                   | 67.2 ms                                                    | 64.2 ms: 1.05x faster                                                           |
| gc_traversal               | 3.98 ms                                                    | 3.81 ms: 1.04x faster                                                           |
| telco                      | 8.41 ms                                                    | 8.07 ms: 1.04x faster                                                           |
| json_dumps                 | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                           |
| json_loads                 | 28.9 us                                                    | 27.8 us: 1.04x faster                                                           |
| async_tree_io              | 939 ms                                                     | 903 ms: 1.04x faster                                                            |
| pprint_pformat             | 1.56 sec                                                   | 1.50 sec: 1.04x faster                                                          |
| pickle_pure_python         | 305 us                                                     | 295 us: 1.04x faster                                                            |
| thrift                     | 823 us                                                     | 796 us: 1.03x faster                                                            |
| pprint_safe_repr           | 758 ms                                                     | 733 ms: 1.03x faster                                                            |
| pidigits                   | 191 ms                                                     | 185 ms: 1.03x faster                                                            |
| comprehensions             | 16.6 us                                                    | 16.1 us: 1.03x faster                                                           |
| create_gc_cycles           | 1.82 ms                                                    | 1.77 ms: 1.03x faster                                                           |
| tornado_http               | 94.6 ms                                                    | 92.1 ms: 1.03x faster                                                           |
| pycparser                  | 1.16 sec                                                   | 1.13 sec: 1.03x faster                                                          |
| regex_compile              | 137 ms                                                     | 134 ms: 1.02x faster                                                            |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.02x faster                                                          |
| sqlglot_parse              | 1.32 ms                                                    | 1.29 ms: 1.02x faster                                                           |
| go                         | 145 ms                                                     | 142 ms: 1.02x faster                                                            |
| coroutines                 | 23.2 ms                                                    | 22.8 ms: 1.02x faster                                                           |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                           |
| asyncio_tcp                | 508 ms                                                     | 499 ms: 1.02x faster                                                            |
| asyncio_websockets         | 567 ms                                                     | 557 ms: 1.02x faster                                                            |
| json                       | 5.31 ms                                                    | 5.22 ms: 1.02x faster                                                           |
| bench_thread_pool          | 834 us                                                     | 821 us: 1.02x faster                                                            |
| coverage                   | 93.1 ms                                                    | 91.7 ms: 1.01x faster                                                           |
| dask                       | 369 ms                                                     | 365 ms: 1.01x faster                                                            |
| sqlglot_transpile          | 1.63 ms                                                    | 1.61 ms: 1.01x faster                                                           |
| regex_v8                   | 25.1 ms                                                    | 24.8 ms: 1.01x faster                                                           |
| unpickle_pure_python       | 218 us                                                     | 216 us: 1.01x faster                                                            |
| scimark_sor                | 127 ms                                                     | 127 ms: 1.01x faster                                                            |
| 2to3                       | 274 ms                                                     | 273 ms: 1.00x faster                                                            |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                           |
| sqlglot_optimize           | 55.5 ms                                                    | 55.9 ms: 1.01x slower                                                           |
| python_startup_no_site     | 7.11 ms                                                    | 7.16 ms: 1.01x slower                                                           |
| regex_effbot               | 3.67 ms                                                    | 3.70 ms: 1.01x slower                                                           |
| logging_silent             | 105 ns                                                     | 106 ns: 1.01x slower                                                            |
| sqlglot_normalize          | 110 ms                                                     | 112 ms: 1.02x slower                                                            |
| genshi_text                | 23.7 ms                                                    | 24.2 ms: 1.02x slower                                                           |
| scimark_lu                 | 122 ms                                                     | 125 ms: 1.02x slower                                                            |
| docutils                   | 2.83 sec                                                   | 2.90 sec: 1.03x slower                                                          |
| regex_dna                  | 221 ms                                                     | 227 ms: 1.03x slower                                                            |
| typing_runtime_protocols   | 165 us                                                     | 170 us: 1.03x slower                                                            |
| async_generators           | 442 ms                                                     | 456 ms: 1.03x slower                                                            |
| django_template            | 34.8 ms                                                    | 35.9 ms: 1.03x slower                                                           |
| genshi_xml                 | 51.6 ms                                                    | 53.9 ms: 1.05x slower                                                           |
| nqueens                    | 81.4 ms                                                    | 85.2 ms: 1.05x slower                                                           |
| sympy_str                  | 282 ms                                                     | 298 ms: 1.06x slower                                                            |
| hexiom                     | 6.30 ms                                                    | 6.67 ms: 1.06x slower                                                           |
| sympy_expand               | 473 ms                                                     | 503 ms: 1.06x slower                                                            |
| deltablue                  | 3.25 ms                                                    | 3.52 ms: 1.08x slower                                                           |
| sympy_sum                  | 156 ms                                                     | 170 ms: 1.09x slower                                                            |
| sympy_integrate            | 20.5 ms                                                    | 22.6 ms: 1.10x slower                                                           |
| pylint                     | 317 ms                                                     | 355 ms: 1.12x slower                                                            |
| generators                 | 29.6 ms                                                    | 33.3 ms: 1.12x slower                                                           |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                                    |

Benchmark hidden because not significant (1): raytrace
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.08x