# Results vs. 3.12.0

- fork: faster-cpython
- ref: monitoring_branch_ta
- machine: linux-x86_64
- commit hash: dc5a9d5
- commit date: 2024-08-01
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-linux-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 273 ms: 1.00x faster                                                            |
| docutils       | 2.77 sec                                               | 2.90 sec: 1.05x slower                                                          |
| tornado_http   | 103 ms                                                 | 92.1 ms: 1.11x faster                                                           |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-linux-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 299 ms: 1.50x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 390 ms: 1.47x faster                                                            |
| async_tree_none            | 472 ms                                                 | 326 ms: 1.45x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 410 ms: 1.41x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 860 ms: 1.37x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 531 ms: 1.37x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 563 ms: 1.29x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 903 ms: 1.28x faster                                                            |
| Geometric mean             | (ref)                                                  | 1.39x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-linux-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 79.4 ms: 1.22x faster                                                           |
| float          | 84.7 ms                                                | 70.4 ms: 1.20x faster                                                           |
| pidigits       | 187 ms                                                 | 185 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                  | 1.14x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-linux-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 134 ms: 1.11x faster                                                            |
| regex_effbot   | 3.61 ms                                                | 3.70 ms: 1.03x slower                                                           |
| regex_dna      | 212 ms                                                 | 227 ms: 1.07x slower                                                            |
| regex_v8       | 23.1 ms                                                | 24.8 ms: 1.07x slower                                                           |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-linux-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.92 sec: 1.21x faster                                                          |
| xml_etree_generate   | 89.2 ms                                                | 79.2 ms: 1.13x faster                                                           |
| xml_etree_process    | 61.7 ms                                                | 55.3 ms: 1.12x faster                                                           |
| pickle_pure_python   | 324 us                                                 | 295 us: 1.10x faster                                                            |
| xml_etree_parse      | 159 ms                                                 | 146 ms: 1.09x faster                                                            |
| xml_etree_iterparse  | 107 ms                                                 | 99.2 ms: 1.08x faster                                                           |
| unpickle_pure_python | 230 us                                                 | 216 us: 1.07x faster                                                            |
| json_loads           | 28.5 us                                                | 27.8 us: 1.03x faster                                                           |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                           |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-linux-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.16 ms: 1.03x slower                                                           |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-linux-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.92 ms: 1.20x faster                                                           |
| django_template | 34.6 ms                                                | 35.9 ms: 1.04x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-linux-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 299 ms: 1.50x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 390 ms: 1.47x faster                                                            |
| async_tree_none            | 472 ms                                                 | 326 ms: 1.45x faster                                                            |
| deepcopy_memo              | 40.7 us                                                | 28.8 us: 1.41x faster                                                           |
| async_tree_memoization     | 578 ms                                                 | 410 ms: 1.41x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 860 ms: 1.37x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 531 ms: 1.37x faster                                                            |
| deepcopy                   | 371 us                                                 | 273 us: 1.36x faster                                                            |
| comprehensions             | 21.8 us                                                | 16.1 us: 1.35x faster                                                           |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 563 ms: 1.29x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 903 ms: 1.28x faster                                                            |
| scimark_monte_carlo        | 75.1 ms                                                | 59.9 ms: 1.25x faster                                                           |
| scimark_fft                | 382 ms                                                 | 308 ms: 1.24x faster                                                            |
| nbody                      | 97.0 ms                                                | 79.4 ms: 1.22x faster                                                           |
| tomli_loads                | 2.33 sec                                               | 1.92 sec: 1.21x faster                                                          |
| pathlib                    | 19.3 ms                                                | 16.0 ms: 1.21x faster                                                           |
| deepcopy_reduce            | 3.35 us                                                | 2.77 us: 1.21x faster                                                           |
| crypto_pyaes               | 81.9 ms                                                | 67.9 ms: 1.21x faster                                                           |
| logging_format             | 7.23 us                                                | 6.00 us: 1.21x faster                                                           |
| float                      | 84.7 ms                                                | 70.4 ms: 1.20x faster                                                           |
| mako                       | 11.9 ms                                                | 9.92 ms: 1.20x faster                                                           |
| logging_simple             | 6.46 us                                                | 5.47 us: 1.18x faster                                                           |
| raytrace                   | 312 ms                                                 | 266 ms: 1.17x faster                                                            |
| chaos                      | 67.0 ms                                                | 57.6 ms: 1.16x faster                                                           |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.39 ms: 1.15x faster                                                           |
| fannkuch                   | 417 ms                                                 | 364 ms: 1.15x faster                                                            |
| richards                   | 45.8 ms                                                | 40.4 ms: 1.14x faster                                                           |
| pyflate                    | 482 ms                                                 | 427 ms: 1.13x faster                                                            |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.13x faster                                                            |
| xml_etree_generate         | 89.2 ms                                                | 79.2 ms: 1.13x faster                                                           |
| xml_etree_process          | 61.7 ms                                                | 55.3 ms: 1.12x faster                                                           |
| tornado_http               | 103 ms                                                 | 92.1 ms: 1.11x faster                                                           |
| regex_compile              | 148 ms                                                 | 134 ms: 1.11x faster                                                            |
| richards_super             | 51.5 ms                                                | 46.5 ms: 1.11x faster                                                           |
| pickle_pure_python         | 324 us                                                 | 295 us: 1.10x faster                                                            |
| xml_etree_parse            | 159 ms                                                 | 146 ms: 1.09x faster                                                            |
| xml_etree_iterparse        | 107 ms                                                 | 99.2 ms: 1.08x faster                                                           |
| meteor_contest             | 112 ms                                                 | 105 ms: 1.07x faster                                                            |
| unpickle_pure_python       | 230 us                                                 | 216 us: 1.07x faster                                                            |
| pprint_safe_repr           | 776 ms                                                 | 733 ms: 1.06x faster                                                            |
| deltablue                  | 3.72 ms                                                | 3.52 ms: 1.06x faster                                                           |
| sqlglot_parse              | 1.36 ms                                                | 1.29 ms: 1.05x faster                                                           |
| pprint_pformat             | 1.57 sec                                               | 1.50 sec: 1.05x faster                                                          |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.04x faster                                                          |
| sqlglot_transpile          | 1.68 ms                                                | 1.61 ms: 1.04x faster                                                           |
| mdp                        | 2.63 sec                                               | 2.55 sec: 1.03x faster                                                          |
| bench_thread_pool          | 842 us                                                 | 821 us: 1.03x faster                                                            |
| json_loads                 | 28.5 us                                                | 27.8 us: 1.03x faster                                                           |
| dask                       | 372 ms                                                 | 365 ms: 1.02x faster                                                            |
| scimark_sor                | 129 ms                                                 | 127 ms: 1.02x faster                                                            |
| coroutines                 | 23.2 ms                                                | 22.8 ms: 1.02x faster                                                           |
| async_generators           | 463 ms                                                 | 456 ms: 1.02x faster                                                            |
| pidigits                   | 187 ms                                                 | 185 ms: 1.01x faster                                                            |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                           |
| sympy_str                  | 300 ms                                                 | 298 ms: 1.01x faster                                                            |
| 2to3                       | 274 ms                                                 | 273 ms: 1.00x faster                                                            |
| sympy_sum                  | 169 ms                                                 | 170 ms: 1.00x slower                                                            |
| gc_traversal               | 3.79 ms                                                | 3.81 ms: 1.00x slower                                                           |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                          |
| asyncio_websockets         | 551 ms                                                 | 557 ms: 1.01x slower                                                            |
| logging_silent             | 104 ns                                                 | 106 ns: 1.02x slower                                                            |
| go                         | 139 ms                                                 | 142 ms: 1.02x slower                                                            |
| asyncio_tcp                | 491 ms                                                 | 499 ms: 1.02x slower                                                            |
| sqlglot_normalize          | 110 ms                                                 | 112 ms: 1.02x slower                                                            |
| sqlglot_optimize           | 54.8 ms                                                | 55.9 ms: 1.02x slower                                                           |
| nqueens                    | 83.3 ms                                                | 85.2 ms: 1.02x slower                                                           |
| regex_effbot               | 3.61 ms                                                | 3.70 ms: 1.03x slower                                                           |
| python_startup_no_site     | 6.94 ms                                                | 7.16 ms: 1.03x slower                                                           |
| django_template            | 34.6 ms                                                | 35.9 ms: 1.04x slower                                                           |
| hexiom                     | 6.41 ms                                                | 6.67 ms: 1.04x slower                                                           |
| docutils                   | 2.77 sec                                               | 2.90 sec: 1.05x slower                                                          |
| sympy_expand               | 478 ms                                                 | 503 ms: 1.05x slower                                                            |
| sympy_integrate            | 21.4 ms                                                | 22.6 ms: 1.05x slower                                                           |
| scimark_lu                 | 118 ms                                                 | 125 ms: 1.06x slower                                                            |
| generators                 | 31.2 ms                                                | 33.3 ms: 1.07x slower                                                           |
| regex_dna                  | 212 ms                                                 | 227 ms: 1.07x slower                                                            |
| regex_v8                   | 23.1 ms                                                | 24.8 ms: 1.07x slower                                                           |
| typing_runtime_protocols   | 158 us                                                 | 170 us: 1.08x slower                                                            |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                           |
| telco                      | 7.10 ms                                                | 8.07 ms: 1.14x slower                                                           |
| create_gc_cycles           | 1.48 ms                                                | 1.77 ms: 1.20x slower                                                           |
| coverage                   | 72.7 ms                                                | 91.7 ms: 1.26x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                                    |

Benchmark hidden because not significant (2): json, bench_mp_pool
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240801-3.14.0a0-dc5a9d5-JIT/bm-20240801-linux-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.05x