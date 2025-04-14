# Results vs. 3.12.0

- fork: brandtbucher
- ref: hack_night
- machine: linux-x86_64
- commit hash: b856d47
- commit date: 2025-02-22
- overall geometric mean: 1.033x faster
- HPT reliability: 99.14%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf2-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 291 ms: 1.02x slower                                                    |
| docutils       | 2.87 sec                                                     | 2.96 sec: 1.03x slower                                                  |
| Geometric mean | (ref)                                                        | 1.03x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf2-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 643 ms: 1.64x faster                                                    |
| async_tree_io              | 1.04 sec                                                     | 640 ms: 1.63x faster                                                    |
| async_tree_memoization_tg  | 540 ms                                                       | 338 ms: 1.60x faster                                                    |
| async_tree_none            | 452 ms                                                       | 291 ms: 1.55x faster                                                    |
| async_tree_memoization     | 544 ms                                                       | 353 ms: 1.54x faster                                                    |
| async_tree_none_tg         | 431 ms                                                       | 280 ms: 1.54x faster                                                    |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 511 ms: 1.36x faster                                                    |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 524 ms: 1.33x faster                                                    |
| Geometric mean             | (ref)                                                        | 1.52x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf2-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 69.5 ms: 1.10x faster                                                   |
| pidigits       | 265 ms                                                       | 253 ms: 1.05x faster                                                    |
| nbody          | 88.0 ms                                                      | 100.0 ms: 1.14x slower                                                  |
| Geometric mean | (ref)                                                        | 1.00x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf2-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.13 ms: 1.14x faster                                                   |
| regex_compile  | 144 ms                                                       | 136 ms: 1.06x faster                                                    |
| regex_dna      | 239 ms                                                       | 238 ms: 1.00x faster                                                    |
| regex_v8       | 23.6 ms                                                      | 25.5 ms: 1.08x slower                                                   |
| Geometric mean | (ref)                                                        | 1.03x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf2-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 79.8 ms: 1.08x faster                                                   |
| tomli_loads          | 2.16 sec                                                     | 2.02 sec: 1.07x faster                                                  |
| xml_etree_iterparse  | 103 ms                                                       | 96.6 ms: 1.06x faster                                                   |
| xml_etree_parse      | 144 ms                                                       | 137 ms: 1.05x faster                                                    |
| xml_etree_process    | 58.4 ms                                                      | 55.9 ms: 1.05x faster                                                   |
| unpickle_pure_python | 210 us                                                       | 206 us: 1.02x faster                                                    |
| pickle_pure_python   | 318 us                                                       | 337 us: 1.06x slower                                                    |
| json_loads           | 24.4 us                                                      | 26.6 us: 1.09x slower                                                   |
| json_dumps           | 10.2 ms                                                      | 11.8 ms: 1.15x slower                                                   |
| Geometric mean       | (ref)                                                        | 1.00x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf2-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.03 ms: 1.05x slower                                                   |
| python_startup         | 11.6 ms                                                      | 16.0 ms: 1.38x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf2-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 36.3 ms: 1.05x faster                                                   |
| mako            | 10.0 ms                                                      | 9.61 ms: 1.04x faster                                                   |
| Geometric mean  | (ref)                                                        | 1.05x faster                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf2-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 643 ms: 1.64x faster                                                    |
| async_tree_io              | 1.04 sec                                                     | 640 ms: 1.63x faster                                                    |
| async_tree_memoization_tg  | 540 ms                                                       | 338 ms: 1.60x faster                                                    |
| async_tree_none            | 452 ms                                                       | 291 ms: 1.55x faster                                                    |
| async_tree_memoization     | 544 ms                                                       | 353 ms: 1.54x faster                                                    |
| async_tree_none_tg         | 431 ms                                                       | 280 ms: 1.54x faster                                                    |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 511 ms: 1.36x faster                                                    |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 524 ms: 1.33x faster                                                    |
| deepcopy                   | 368 us                                                       | 280 us: 1.31x faster                                                    |
| generators                 | 37.4 ms                                                      | 28.9 ms: 1.29x faster                                                   |
| deepcopy_memo              | 36.8 us                                                      | 28.9 us: 1.27x faster                                                   |
| comprehensions             | 21.9 us                                                      | 19.0 us: 1.15x faster                                                   |
| deepcopy_reduce            | 3.37 us                                                      | 2.93 us: 1.15x faster                                                   |
| regex_effbot               | 3.57 ms                                                      | 3.13 ms: 1.14x faster                                                   |
| pathlib                    | 18.9 ms                                                      | 16.6 ms: 1.14x faster                                                   |
| scimark_monte_carlo        | 69.0 ms                                                      | 61.1 ms: 1.13x faster                                                   |
| spectral_norm              | 91.6 ms                                                      | 82.4 ms: 1.11x faster                                                   |
| float                      | 76.6 ms                                                      | 69.5 ms: 1.10x faster                                                   |
| sqlalchemy_declarative     | 159 ms                                                       | 146 ms: 1.09x faster                                                    |
| coroutines                 | 23.0 ms                                                      | 21.1 ms: 1.09x faster                                                   |
| logging_format             | 7.48 us                                                      | 6.91 us: 1.08x faster                                                   |
| xml_etree_generate         | 86.1 ms                                                      | 79.8 ms: 1.08x faster                                                   |
| tomli_loads                | 2.16 sec                                                     | 2.02 sec: 1.07x faster                                                  |
| xml_etree_iterparse        | 103 ms                                                       | 96.6 ms: 1.06x faster                                                   |
| regex_compile              | 144 ms                                                       | 136 ms: 1.06x faster                                                    |
| logging_simple             | 6.71 us                                                      | 6.37 us: 1.05x faster                                                   |
| django_template            | 38.2 ms                                                      | 36.3 ms: 1.05x faster                                                   |
| xml_etree_parse            | 144 ms                                                       | 137 ms: 1.05x faster                                                    |
| crypto_pyaes               | 80.3 ms                                                      | 76.7 ms: 1.05x faster                                                   |
| pidigits                   | 265 ms                                                       | 253 ms: 1.05x faster                                                    |
| xml_etree_process          | 58.4 ms                                                      | 55.9 ms: 1.05x faster                                                   |
| mako                       | 10.0 ms                                                      | 9.61 ms: 1.04x faster                                                   |
| sqlalchemy_imperative      | 18.7 ms                                                      | 18.1 ms: 1.04x faster                                                   |
| sympy_sum                  | 162 ms                                                       | 157 ms: 1.04x faster                                                    |
| pyflate                    | 439 ms                                                       | 425 ms: 1.03x faster                                                    |
| chaos                      | 64.0 ms                                                      | 62.1 ms: 1.03x faster                                                   |
| scimark_sor                | 109 ms                                                       | 107 ms: 1.02x faster                                                    |
| scimark_fft                | 301 ms                                                       | 295 ms: 1.02x faster                                                    |
| unpickle_pure_python       | 210 us                                                       | 206 us: 1.02x faster                                                    |
| richards                   | 45.7 ms                                                      | 45.1 ms: 1.02x faster                                                   |
| scimark_lu                 | 98.8 ms                                                      | 97.7 ms: 1.01x faster                                                   |
| sympy_integrate            | 23.9 ms                                                      | 23.7 ms: 1.01x faster                                                   |
| raytrace                   | 298 ms                                                       | 295 ms: 1.01x faster                                                    |
| richards_super             | 51.3 ms                                                      | 51.0 ms: 1.01x faster                                                   |
| sympy_str                  | 302 ms                                                       | 300 ms: 1.01x faster                                                    |
| go                         | 150 ms                                                       | 149 ms: 1.01x faster                                                    |
| regex_dna                  | 239 ms                                                       | 238 ms: 1.00x faster                                                    |
| sqlglot_parse              | 1.38 ms                                                      | 1.38 ms: 1.00x slower                                                   |
| pprint_safe_repr           | 807 ms                                                       | 813 ms: 1.01x slower                                                    |
| 2to3                       | 285 ms                                                       | 291 ms: 1.02x slower                                                    |
| pycparser                  | 1.23 sec                                                     | 1.26 sec: 1.02x slower                                                  |
| logging_silent             | 94.4 ns                                                      | 97.3 ns: 1.03x slower                                                   |
| dulwich_log                | 65.4 ms                                                      | 67.4 ms: 1.03x slower                                                   |
| docutils                   | 2.87 sec                                                     | 2.96 sec: 1.03x slower                                                  |
| sqlglot_normalize          | 116 ms                                                       | 120 ms: 1.03x slower                                                    |
| meteor_contest             | 128 ms                                                       | 133 ms: 1.04x slower                                                    |
| python_startup_no_site     | 8.64 ms                                                      | 9.03 ms: 1.05x slower                                                   |
| sqlglot_optimize           | 57.5 ms                                                      | 60.3 ms: 1.05x slower                                                   |
| json                       | 5.12 ms                                                      | 5.41 ms: 1.06x slower                                                   |
| pickle_pure_python         | 318 us                                                       | 337 us: 1.06x slower                                                    |
| deltablue                  | 3.24 ms                                                      | 3.44 ms: 1.06x slower                                                   |
| sympy_expand               | 484 ms                                                       | 515 ms: 1.06x slower                                                    |
| regex_v8                   | 23.6 ms                                                      | 25.5 ms: 1.08x slower                                                   |
| telco                      | 6.96 ms                                                      | 7.58 ms: 1.09x slower                                                   |
| fannkuch                   | 350 ms                                                       | 382 ms: 1.09x slower                                                    |
| json_loads                 | 24.4 us                                                      | 26.6 us: 1.09x slower                                                   |
| nqueens                    | 89.9 ms                                                      | 99.3 ms: 1.10x slower                                                   |
| async_generators           | 390 ms                                                       | 434 ms: 1.11x slower                                                    |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.73 ms: 1.12x slower                                                   |
| nbody                      | 88.0 ms                                                      | 100.0 ms: 1.14x slower                                                  |
| json_dumps                 | 10.2 ms                                                      | 11.8 ms: 1.15x slower                                                   |
| coverage                   | 66.7 ms                                                      | 77.8 ms: 1.17x slower                                                   |
| typing_runtime_protocols   | 152 us                                                       | 177 us: 1.17x slower                                                    |
| hexiom                     | 5.96 ms                                                      | 7.04 ms: 1.18x slower                                                   |
| python_startup             | 11.6 ms                                                      | 16.0 ms: 1.38x slower                                                   |
| create_gc_cycles           | 1.59 ms                                                      | 2.68 ms: 1.69x slower                                                   |
| gc_traversal               | 3.48 ms                                                      | 6.33 ms: 1.82x slower                                                   |
| bench_mp_pool              | 4.76 ms                                                      | 1.64 sec: 343.82x slower                                                |
| Geometric mean             | (ref)                                                        | 1.04x slower                                                            |

Benchmark hidden because not significant (6): mdp, sqlite_synth, pprint_pformat, sqlglot_transpile, asyncio_websockets, bench_thread_pool
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250222-3.14.0a5-b856d47-JIT/bm-20250222-pythonperf2-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.033x faster

# HPT report

- Reliability score: 99.14% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x