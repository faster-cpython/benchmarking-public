# Results vs. 3.12.0

- fork: brandtbucher
- ref: nojit
- machine: windows-x86
- commit hash: f098037
- commit date: 2025-01-07
- overall geometric mean: 1.162x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 247 ms: 1.13x faster                                                   |
| docutils       | 1.98 sec                                                        | 1.84 sec: 1.08x faster                                                 |
| Geometric mean | (ref)                                                           | 1.11x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 433 ms: 1.56x faster                                                   |
| async_tree_io              | 693 ms                                                          | 446 ms: 1.55x faster                                                   |
| async_tree_memoization_tg  | 350 ms                                                          | 230 ms: 1.53x faster                                                   |
| async_tree_none_tg         | 278 ms                                                          | 183 ms: 1.52x faster                                                   |
| async_tree_memoization     | 364 ms                                                          | 254 ms: 1.43x faster                                                   |
| async_tree_none            | 298 ms                                                          | 208 ms: 1.43x faster                                                   |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 451 ms: 1.25x faster                                                   |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 437 ms: 1.25x faster                                                   |
| Geometric mean             | (ref)                                                           | 1.44x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 89.2 ms: 1.42x faster                                                  |
| float          | 76.7 ms                                                         | 55.6 ms: 1.38x faster                                                  |
| pidigits       | 199 ms                                                          | 197 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                           | 1.26x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.57 ms: 1.30x faster                                                  |
| regex_compile  | 129 ms                                                          | 104 ms: 1.24x faster                                                   |
| regex_dna      | 127 ms                                                          | 124 ms: 1.02x faster                                                   |
| regex_v8       | 15.0 ms                                                         | 17.4 ms: 1.16x slower                                                  |
| Geometric mean | (ref)                                                           | 1.09x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.58 sec: 1.39x faster                                                 |
| unpickle_pure_python | 210 us                                                          | 166 us: 1.27x faster                                                   |
| xml_etree_iterparse  | 77.6 ms                                                         | 66.7 ms: 1.16x faster                                                  |
| pickle_pure_python   | 286 us                                                          | 258 us: 1.11x faster                                                   |
| xml_etree_process    | 53.2 ms                                                         | 48.8 ms: 1.09x faster                                                  |
| xml_etree_generate   | 72.1 ms                                                         | 68.0 ms: 1.06x faster                                                  |
| xml_etree_parse      | 113 ms                                                          | 108 ms: 1.05x faster                                                   |
| json_loads           | 20.4 us                                                         | 20.7 us: 1.02x slower                                                  |
| json_dumps           | 7.40 ms                                                         | 8.76 ms: 1.18x slower                                                  |
| Geometric mean       | (ref)                                                           | 1.10x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup | 22.4 ms                                                         | 25.4 ms: 1.13x slower                                                  |
| Geometric mean | (ref)                                                           | 1.07x slower                                                           |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|-----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.74 ms: 1.29x faster                                                  |
| django_template | 36.9 ms                                                         | 33.3 ms: 1.11x faster                                                  |
| Geometric mean  | (ref)                                                           | 1.19x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 20.7 us: 1.86x faster                                                  |
| deepcopy                   | 360 us                                                          | 225 us: 1.60x faster                                                   |
| async_tree_io_tg           | 677 ms                                                          | 433 ms: 1.56x faster                                                   |
| generators                 | 38.5 ms                                                         | 24.7 ms: 1.56x faster                                                  |
| async_tree_io              | 693 ms                                                          | 446 ms: 1.55x faster                                                   |
| async_tree_memoization_tg  | 350 ms                                                          | 230 ms: 1.53x faster                                                   |
| async_tree_none_tg         | 278 ms                                                          | 183 ms: 1.52x faster                                                   |
| spectral_norm              | 104 ms                                                          | 69.3 ms: 1.50x faster                                                  |
| comprehensions             | 19.2 us                                                         | 13.2 us: 1.46x faster                                                  |
| async_tree_memoization     | 364 ms                                                          | 254 ms: 1.43x faster                                                   |
| async_tree_none            | 298 ms                                                          | 208 ms: 1.43x faster                                                   |
| nbody                      | 127 ms                                                          | 89.2 ms: 1.42x faster                                                  |
| go                         | 137 ms                                                          | 97.4 ms: 1.41x faster                                                  |
| hexiom                     | 6.82 ms                                                         | 4.88 ms: 1.40x faster                                                  |
| scimark_sor                | 130 ms                                                          | 93.1 ms: 1.39x faster                                                  |
| tomli_loads                | 2.20 sec                                                        | 1.58 sec: 1.39x faster                                                 |
| float                      | 76.7 ms                                                         | 55.6 ms: 1.38x faster                                                  |
| logging_silent             | 101 ns                                                          | 73.6 ns: 1.37x faster                                                  |
| scimark_lu                 | 93.2 ms                                                         | 68.2 ms: 1.37x faster                                                  |
| deepcopy_reduce            | 3.23 us                                                         | 2.38 us: 1.35x faster                                                  |
| deltablue                  | 3.58 ms                                                         | 2.68 ms: 1.34x faster                                                  |
| scimark_monte_carlo        | 66.4 ms                                                         | 50.5 ms: 1.32x faster                                                  |
| regex_effbot               | 2.04 ms                                                         | 1.57 ms: 1.30x faster                                                  |
| mako                       | 9.96 ms                                                         | 7.74 ms: 1.29x faster                                                  |
| chaos                      | 69.4 ms                                                         | 54.0 ms: 1.28x faster                                                  |
| unpickle_pure_python       | 210 us                                                          | 166 us: 1.27x faster                                                   |
| coroutines                 | 20.9 ms                                                         | 16.5 ms: 1.27x faster                                                  |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.08 ms: 1.25x faster                                                  |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 451 ms: 1.25x faster                                                   |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 437 ms: 1.25x faster                                                   |
| nqueens                    | 93.7 ms                                                         | 75.2 ms: 1.25x faster                                                  |
| regex_compile              | 129 ms                                                          | 104 ms: 1.24x faster                                                   |
| logging_simple             | 9.75 us                                                         | 7.87 us: 1.24x faster                                                  |
| raytrace                   | 308 ms                                                          | 252 ms: 1.22x faster                                                   |
| pyflate                    | 424 ms                                                          | 349 ms: 1.21x faster                                                   |
| logging_format             | 10.4 us                                                         | 8.62 us: 1.21x faster                                                  |
| sqlglot_transpile          | 1.53 ms                                                         | 1.29 ms: 1.18x faster                                                  |
| scimark_fft                | 271 ms                                                          | 229 ms: 1.18x faster                                                   |
| sqlglot_parse              | 1.25 ms                                                         | 1.06 ms: 1.18x faster                                                  |
| sqlglot_optimize           | 48.5 ms                                                         | 41.3 ms: 1.17x faster                                                  |
| sympy_sum                  | 123 ms                                                          | 105 ms: 1.17x faster                                                   |
| xml_etree_iterparse        | 77.6 ms                                                         | 66.7 ms: 1.16x faster                                                  |
| richards                   | 41.3 ms                                                         | 35.6 ms: 1.16x faster                                                  |
| dulwich_log                | 58.5 ms                                                         | 50.7 ms: 1.15x faster                                                  |
| fannkuch                   | 354 ms                                                          | 309 ms: 1.14x faster                                                   |
| pprint_pformat             | 1.50 sec                                                        | 1.31 sec: 1.14x faster                                                 |
| 2to3                       | 280 ms                                                          | 247 ms: 1.13x faster                                                   |
| pprint_safe_repr           | 721 ms                                                          | 637 ms: 1.13x faster                                                   |
| sympy_integrate            | 17.5 ms                                                         | 15.6 ms: 1.13x faster                                                  |
| richards_super             | 46.5 ms                                                         | 41.5 ms: 1.12x faster                                                  |
| sympy_str                  | 240 ms                                                          | 215 ms: 1.12x faster                                                   |
| mdp                        | 1.91 sec                                                        | 1.72 sec: 1.11x faster                                                 |
| django_template            | 36.9 ms                                                         | 33.3 ms: 1.11x faster                                                  |
| pickle_pure_python         | 286 us                                                          | 258 us: 1.11x faster                                                   |
| bench_thread_pool          | 1.10 ms                                                         | 997 us: 1.11x faster                                                   |
| crypto_pyaes               | 69.2 ms                                                         | 63.0 ms: 1.10x faster                                                  |
| pathlib                    | 91.4 ms                                                         | 83.7 ms: 1.09x faster                                                  |
| meteor_contest             | 86.9 ms                                                         | 79.6 ms: 1.09x faster                                                  |
| xml_etree_process          | 53.2 ms                                                         | 48.8 ms: 1.09x faster                                                  |
| pycparser                  | 978 ms                                                          | 900 ms: 1.09x faster                                                   |
| docutils                   | 1.98 sec                                                        | 1.84 sec: 1.08x faster                                                 |
| xml_etree_generate         | 72.1 ms                                                         | 68.0 ms: 1.06x faster                                                  |
| async_generators           | 313 ms                                                          | 295 ms: 1.06x faster                                                   |
| sympy_expand               | 398 ms                                                          | 378 ms: 1.05x faster                                                   |
| sqlite_synth               | 2.07 us                                                         | 1.98 us: 1.05x faster                                                  |
| xml_etree_parse            | 113 ms                                                          | 108 ms: 1.05x faster                                                   |
| regex_dna                  | 127 ms                                                          | 124 ms: 1.02x faster                                                   |
| pidigits                   | 199 ms                                                          | 197 ms: 1.01x faster                                                   |
| json                       | 4.15 ms                                                         | 4.22 ms: 1.02x slower                                                  |
| json_loads                 | 20.4 us                                                         | 20.7 us: 1.02x slower                                                  |
| coverage                   | 48.4 ms                                                         | 52.4 ms: 1.08x slower                                                  |
| typing_runtime_protocols   | 126 us                                                          | 140 us: 1.11x slower                                                   |
| python_startup             | 22.4 ms                                                         | 25.4 ms: 1.13x slower                                                  |
| bench_mp_pool              | 75.4 ms                                                         | 87.3 ms: 1.16x slower                                                  |
| regex_v8                   | 15.0 ms                                                         | 17.4 ms: 1.16x slower                                                  |
| json_dumps                 | 7.40 ms                                                         | 8.76 ms: 1.18x slower                                                  |
| mypy2                      | 584 ms                                                          | 695 ms: 1.19x slower                                                   |
| telco                      | 5.51 ms                                                         | 6.71 ms: 1.22x slower                                                  |
| gc_traversal               | 1.44 ms                                                         | 1.78 ms: 1.24x slower                                                  |
| create_gc_cycles           | 652 us                                                          | 1.06 ms: 1.63x slower                                                  |
| sqlglot_normalize          | 100 ms                                                          | 214 ms: 2.13x slower                                                   |
| Geometric mean             | (ref)                                                           | 1.16x faster                                                           |

Benchmark hidden because not significant (1): python_startup_no_site
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250107-3.14.0a3+-f098037/bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.162x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: unknown