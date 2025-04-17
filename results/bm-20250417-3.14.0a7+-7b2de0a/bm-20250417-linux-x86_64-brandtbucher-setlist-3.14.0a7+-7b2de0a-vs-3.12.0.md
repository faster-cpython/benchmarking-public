# Results vs. 3.12.0

- fork: brandtbucher
- ref: setlist
- machine: linux-x86_64
- commit hash: 7b2de0a
- commit date: 2025-04-17
- overall geometric mean: 1.126x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250417-linux-x86_64-brandtbucher-setlist-3.14.0a7+-7b2de0a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 249 ms: 1.10x faster                                            |
| docutils       | 2.77 sec                                               | 2.60 sec: 1.07x faster                                          |
| Geometric mean | (ref)                                                  | 1.08x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250417-linux-x86_64-brandtbucher-setlist-3.14.0a7+-7b2de0a |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 612 ms: 1.93x faster                                            |
| async_tree_io              | 1.16 sec                                               | 613 ms: 1.89x faster                                            |
| async_tree_memoization     | 578 ms                                                 | 309 ms: 1.87x faster                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 311 ms: 1.85x faster                                            |
| async_tree_none            | 472 ms                                                 | 256 ms: 1.84x faster                                            |
| async_tree_none_tg         | 450 ms                                                 | 247 ms: 1.82x faster                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 474 ms: 1.53x faster                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 481 ms: 1.51x faster                                            |
| Geometric mean             | (ref)                                                  | 1.77x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250417-linux-x86_64-brandtbucher-setlist-3.14.0a7+-7b2de0a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 84.7 ms                                                | 68.7 ms: 1.23x faster                                           |
| pidigits       | 187 ms                                                 | 190 ms: 1.02x slower                                            |
| Geometric mean | (ref)                                                  | 1.07x faster                                                    |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250417-linux-x86_64-brandtbucher-setlist-3.14.0a7+-7b2de0a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 125 ms: 1.19x faster                                            |
| regex_effbot   | 3.61 ms                                                | 3.27 ms: 1.10x faster                                           |
| regex_dna      | 212 ms                                                 | 206 ms: 1.03x faster                                            |
| regex_v8       | 23.1 ms                                                | 22.6 ms: 1.02x faster                                           |
| Geometric mean | (ref)                                                  | 1.08x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250417-linux-x86_64-brandtbucher-setlist-3.14.0a7+-7b2de0a |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.96 sec: 1.19x faster                                          |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                            |
| xml_etree_iterparse  | 107 ms                                                 | 99.7 ms: 1.07x faster                                           |
| unpickle_pure_python | 230 us                                                 | 215 us: 1.07x faster                                            |
| xml_etree_generate   | 89.2 ms                                                | 84.3 ms: 1.06x faster                                           |
| pickle_pure_python   | 324 us                                                 | 311 us: 1.04x faster                                            |
| xml_etree_process    | 61.7 ms                                                | 59.2 ms: 1.04x faster                                           |
| json_loads           | 28.5 us                                                | 29.9 us: 1.05x slower                                           |
| json_dumps           | 10.4 ms                                                | 11.4 ms: 1.09x slower                                           |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250417-linux-x86_64-brandtbucher-setlist-3.14.0a7+-7b2de0a |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.20 ms: 1.18x slower                                           |
| python_startup         | 9.55 ms                                                | 13.2 ms: 1.38x slower                                           |
| Geometric mean         | (ref)                                                  | 1.28x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250417-linux-x86_64-brandtbucher-setlist-3.14.0a7+-7b2de0a |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.2 ms: 1.07x faster                                           |
| mako            | 11.9 ms                                                | 11.5 ms: 1.04x faster                                           |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250417-linux-x86_64-brandtbucher-setlist-3.14.0a7+-7b2de0a |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.22 sec: 2.16x faster                                          |
| async_tree_io_tg           | 1.18 sec                                               | 612 ms: 1.93x faster                                            |
| async_tree_io              | 1.16 sec                                               | 613 ms: 1.89x faster                                            |
| async_tree_memoization     | 578 ms                                                 | 309 ms: 1.87x faster                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 311 ms: 1.85x faster                                            |
| async_tree_none            | 472 ms                                                 | 256 ms: 1.84x faster                                            |
| async_tree_none_tg         | 450 ms                                                 | 247 ms: 1.82x faster                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 474 ms: 1.53x faster                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 481 ms: 1.51x faster                                            |
| deepcopy                   | 371 us                                                 | 250 us: 1.48x faster                                            |
| deepcopy_memo              | 40.7 us                                                | 28.4 us: 1.43x faster                                           |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                           |
| go                         | 139 ms                                                 | 110 ms: 1.26x faster                                            |
| deepcopy_reduce            | 3.35 us                                                | 2.71 us: 1.23x faster                                           |
| float                      | 84.7 ms                                                | 68.7 ms: 1.23x faster                                           |
| raytrace                   | 312 ms                                                 | 259 ms: 1.21x faster                                            |
| chaos                      | 67.0 ms                                                | 56.0 ms: 1.20x faster                                           |
| regex_compile              | 148 ms                                                 | 125 ms: 1.19x faster                                            |
| tomli_loads                | 2.33 sec                                               | 1.96 sec: 1.19x faster                                          |
| logging_format             | 7.23 us                                                | 6.14 us: 1.18x faster                                           |
| logging_simple             | 6.46 us                                                | 5.49 us: 1.18x faster                                           |
| async_generators           | 463 ms                                                 | 398 ms: 1.16x faster                                            |
| dulwich_log                | 68.5 ms                                                | 59.5 ms: 1.15x faster                                           |
| pathlib                    | 19.3 ms                                                | 16.8 ms: 1.15x faster                                           |
| sympy_sum                  | 169 ms                                                 | 148 ms: 1.14x faster                                            |
| sympy_str                  | 300 ms                                                 | 265 ms: 1.13x faster                                            |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                            |
| scimark_monte_carlo        | 75.1 ms                                                | 66.6 ms: 1.13x faster                                           |
| sympy_integrate            | 21.4 ms                                                | 19.0 ms: 1.13x faster                                           |
| logging_silent             | 104 ns                                                 | 93.3 ns: 1.12x faster                                           |
| crypto_pyaes               | 81.9 ms                                                | 73.1 ms: 1.12x faster                                           |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.9 ms: 1.11x faster                                           |
| sqlalchemy_declarative     | 147 ms                                                 | 133 ms: 1.11x faster                                            |
| regex_effbot               | 3.61 ms                                                | 3.27 ms: 1.10x faster                                           |
| deltablue                  | 3.72 ms                                                | 3.37 ms: 1.10x faster                                           |
| spectral_norm              | 115 ms                                                 | 104 ms: 1.10x faster                                            |
| 2to3                       | 274 ms                                                 | 249 ms: 1.10x faster                                            |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.09x faster                                            |
| pprint_safe_repr           | 776 ms                                                 | 714 ms: 1.09x faster                                            |
| pprint_pformat             | 1.57 sec                                               | 1.46 sec: 1.07x faster                                          |
| django_template            | 34.6 ms                                                | 32.2 ms: 1.07x faster                                           |
| scimark_fft                | 382 ms                                                 | 356 ms: 1.07x faster                                            |
| xml_etree_iterparse        | 107 ms                                                 | 99.7 ms: 1.07x faster                                           |
| pyflate                    | 482 ms                                                 | 451 ms: 1.07x faster                                            |
| unpickle_pure_python       | 230 us                                                 | 215 us: 1.07x faster                                            |
| richards                   | 45.8 ms                                                | 43.0 ms: 1.07x faster                                           |
| docutils                   | 2.77 sec                                               | 2.60 sec: 1.07x faster                                          |
| sympy_expand               | 478 ms                                                 | 450 ms: 1.06x faster                                            |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                            |
| xml_etree_generate         | 89.2 ms                                                | 84.3 ms: 1.06x faster                                           |
| nqueens                    | 83.3 ms                                                | 79.3 ms: 1.05x faster                                           |
| richards_super             | 51.5 ms                                                | 49.2 ms: 1.05x faster                                           |
| pickle_pure_python         | 324 us                                                 | 311 us: 1.04x faster                                            |
| xml_etree_process          | 61.7 ms                                                | 59.2 ms: 1.04x faster                                           |
| mako                       | 11.9 ms                                                | 11.5 ms: 1.04x faster                                           |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.89 ms: 1.03x faster                                           |
| regex_dna                  | 212 ms                                                 | 206 ms: 1.03x faster                                            |
| regex_v8                   | 23.1 ms                                                | 22.6 ms: 1.02x faster                                           |
| hexiom                     | 6.41 ms                                                | 6.27 ms: 1.02x faster                                           |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.02x faster                                          |
| sqlite_synth               | 2.83 us                                                | 2.78 us: 1.02x faster                                           |
| generators                 | 31.2 ms                                                | 30.7 ms: 1.02x faster                                           |
| fannkuch                   | 417 ms                                                 | 414 ms: 1.01x faster                                            |
| json                       | 5.26 ms                                                | 5.33 ms: 1.01x slower                                           |
| pidigits                   | 187 ms                                                 | 190 ms: 1.02x slower                                            |
| coroutines                 | 23.2 ms                                                | 24.0 ms: 1.04x slower                                           |
| json_loads                 | 28.5 us                                                | 29.9 us: 1.05x slower                                           |
| typing_runtime_protocols   | 158 us                                                 | 166 us: 1.05x slower                                            |
| bench_thread_pool          | 842 us                                                 | 889 us: 1.06x slower                                            |
| json_dumps                 | 10.4 ms                                                | 11.4 ms: 1.09x slower                                           |
| telco                      | 7.10 ms                                                | 7.85 ms: 1.11x slower                                           |
| python_startup_no_site     | 6.94 ms                                                | 8.20 ms: 1.18x slower                                           |
| coverage                   | 72.7 ms                                                | 88.2 ms: 1.21x slower                                           |
| gc_traversal               | 3.79 ms                                                | 5.04 ms: 1.33x slower                                           |
| python_startup             | 9.55 ms                                                | 13.2 ms: 1.38x slower                                           |
| create_gc_cycles           | 1.48 ms                                                | 2.49 ms: 1.68x slower                                           |
| bench_mp_pool              | 24.0 ms                                                | 81.8 ms: 3.41x slower                                           |
| Geometric mean             | (ref)                                                  | 1.11x faster                                                    |

Benchmark hidden because not significant (3): scimark_lu, asyncio_websockets, nbody
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250417-3.14.0a7+-7b2de0a/bm-20250417-linux-x86_64-brandtbucher-setlist-3.14.0a7+-7b2de0a.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.126x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.10x