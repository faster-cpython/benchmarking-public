# Results vs. 3.12.0

- fork: python
- ref: a3990df6121880e8c678
- machine: windows-x86
- commit hash: a3990df
- commit date: 2025-03-08
- overall geometric mean: 1.200x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250308-pythonperf1_win32-x86-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 252 ms: 1.11x faster                                                            |
| docutils       | 1.98 sec                                                        | 1.82 sec: 1.09x faster                                                          |
| Geometric mean | (ref)                                                           | 1.10x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250308-pythonperf1_win32-x86-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 407 ms: 1.66x faster                                                            |
| async_tree_io              | 693 ms                                                          | 420 ms: 1.65x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 235 ms: 1.55x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 179 ms: 1.55x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 227 ms: 1.55x faster                                                            |
| async_tree_none            | 298 ms                                                          | 193 ms: 1.54x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 457 ms: 1.23x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 453 ms: 1.21x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.48x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250308-pythonperf1_win32-x86-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 72.8 ms: 1.75x faster                                                           |
| float          | 76.7 ms                                                         | 48.9 ms: 1.57x faster                                                           |
| pidigits       | 199 ms                                                          | 219 ms: 1.10x slower                                                            |
| Geometric mean | (ref)                                                           | 1.36x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250308-pythonperf1_win32-x86-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 99.1 ms: 1.30x faster                                                           |
| regex_effbot   | 2.04 ms                                                         | 1.95 ms: 1.04x faster                                                           |
| regex_dna      | 127 ms                                                          | 128 ms: 1.01x slower                                                            |
| regex_v8       | 15.0 ms                                                         | 17.3 ms: 1.15x slower                                                           |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250308-pythonperf1_win32-x86-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.57 sec: 1.40x faster                                                          |
| pickle_dict          | 19.9 us                                                         | 15.7 us: 1.27x faster                                                           |
| unpickle_pure_python | 210 us                                                          | 166 us: 1.26x faster                                                            |
| pickle_list          | 3.37 us                                                         | 2.72 us: 1.24x faster                                                           |
| unpickle_list        | 2.95 us                                                         | 2.60 us: 1.13x faster                                                           |
| pickle_pure_python   | 286 us                                                          | 256 us: 1.12x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 73.5 ms: 1.06x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 50.4 ms: 1.06x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 115 ms: 1.02x slower                                                            |
| json_loads           | 20.4 us                                                         | 21.5 us: 1.06x slower                                                           |
| unpickle             | 9.71 us                                                         | 10.5 us: 1.08x slower                                                           |
| pickle               | 7.79 us                                                         | 8.47 us: 1.09x slower                                                           |
| json_dumps           | 7.40 ms                                                         | 8.13 ms: 1.10x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.08x faster                                                                    |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250308-pythonperf1_win32-x86-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 23.5 ms: 1.23x slower                                                           |
| python_startup         | 22.4 ms                                                         | 29.5 ms: 1.32x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.28x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250308-pythonperf1_win32-x86-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 8.68 ms: 1.15x faster                                                           |
| django_template | 36.9 ms                                                         | 32.2 ms: 1.15x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.15x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250308-pythonperf1_win32-x86-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pathlib                    | 91.4 ms                                                         | 35.2 ms: 2.60x faster                                                           |
| unpack_sequence            | 62.5 ns                                                         | 32.4 ns: 1.93x faster                                                           |
| generators                 | 38.5 ms                                                         | 20.4 ms: 1.88x faster                                                           |
| deepcopy_memo              | 38.4 us                                                         | 20.5 us: 1.88x faster                                                           |
| nbody                      | 127 ms                                                          | 72.8 ms: 1.75x faster                                                           |
| deepcopy                   | 360 us                                                          | 215 us: 1.68x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 407 ms: 1.66x faster                                                            |
| async_tree_io              | 693 ms                                                          | 420 ms: 1.65x faster                                                            |
| scimark_sor                | 130 ms                                                          | 80.7 ms: 1.61x faster                                                           |
| spectral_norm              | 104 ms                                                          | 66.0 ms: 1.57x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.28 ms: 1.57x faster                                                           |
| float                      | 76.7 ms                                                         | 48.9 ms: 1.57x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 235 ms: 1.55x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 179 ms: 1.55x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 227 ms: 1.55x faster                                                            |
| async_tree_none            | 298 ms                                                          | 193 ms: 1.54x faster                                                            |
| go                         | 137 ms                                                          | 92.0 ms: 1.49x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 14.1 ms: 1.48x faster                                                           |
| logging_silent             | 101 ns                                                          | 69.0 ns: 1.46x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 45.8 ms: 1.45x faster                                                           |
| comprehensions             | 19.2 us                                                         | 13.3 us: 1.45x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.24 us: 1.44x faster                                                           |
| raytrace                   | 308 ms                                                          | 215 ms: 1.43x faster                                                            |
| chaos                      | 69.4 ms                                                         | 49.5 ms: 1.40x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 4.86 ms: 1.40x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.57 sec: 1.40x faster                                                          |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.82 ms: 1.37x faster                                                           |
| regex_compile              | 129 ms                                                          | 99.1 ms: 1.30x faster                                                           |
| pyflate                    | 424 ms                                                          | 327 ms: 1.30x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 72.2 ms: 1.30x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 72.2 ms: 1.29x faster                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 977 us: 1.28x faster                                                            |
| pprint_pformat             | 1.50 sec                                                        | 1.17 sec: 1.28x faster                                                          |
| pickle_dict                | 19.9 us                                                         | 15.7 us: 1.27x faster                                                           |
| scimark_fft                | 271 ms                                                          | 215 ms: 1.26x faster                                                            |
| unpickle_pure_python       | 210 us                                                          | 166 us: 1.26x faster                                                            |
| pprint_safe_repr           | 721 ms                                                          | 572 ms: 1.26x faster                                                            |
| sqlglot_transpile          | 1.53 ms                                                         | 1.22 ms: 1.26x faster                                                           |
| async_generators           | 313 ms                                                          | 249 ms: 1.26x faster                                                            |
| pickle_list                | 3.37 us                                                         | 2.72 us: 1.24x faster                                                           |
| logging_simple             | 9.75 us                                                         | 7.89 us: 1.24x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 457 ms: 1.23x faster                                                            |
| logging_format             | 10.4 us                                                         | 8.49 us: 1.23x faster                                                           |
| dulwich_log                | 58.5 ms                                                         | 48.0 ms: 1.22x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 102 ms: 1.21x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 453 ms: 1.21x faster                                                            |
| sympy_str                  | 240 ms                                                          | 201 ms: 1.19x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 15.0 ms: 1.17x faster                                                           |
| fannkuch                   | 354 ms                                                          | 303 ms: 1.17x faster                                                            |
| pycparser                  | 978 ms                                                          | 841 ms: 1.16x faster                                                            |
| sympy_expand               | 398 ms                                                          | 343 ms: 1.16x faster                                                            |
| sqlglot_optimize           | 48.5 ms                                                         | 42.2 ms: 1.15x faster                                                           |
| mako                       | 9.96 ms                                                         | 8.68 ms: 1.15x faster                                                           |
| django_template            | 36.9 ms                                                         | 32.2 ms: 1.15x faster                                                           |
| unpickle_list              | 2.95 us                                                         | 2.60 us: 1.13x faster                                                           |
| pickle_pure_python         | 286 us                                                          | 256 us: 1.12x faster                                                            |
| 2to3                       | 280 ms                                                          | 252 ms: 1.11x faster                                                            |
| richards                   | 41.3 ms                                                         | 37.4 ms: 1.11x faster                                                           |
| richards_super             | 46.5 ms                                                         | 42.3 ms: 1.10x faster                                                           |
| sqlite_synth               | 2.07 us                                                         | 1.90 us: 1.09x faster                                                           |
| docutils                   | 1.98 sec                                                        | 1.82 sec: 1.09x faster                                                          |
| crypto_pyaes               | 69.2 ms                                                         | 64.6 ms: 1.07x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 81.6 ms: 1.06x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 73.5 ms: 1.06x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 50.4 ms: 1.06x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.95 ms: 1.04x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.84 sec: 1.04x faster                                                          |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.4 sec: 1.01x faster                                                          |
| regex_dna                  | 127 ms                                                          | 128 ms: 1.01x slower                                                            |
| xml_etree_parse            | 113 ms                                                          | 115 ms: 1.02x slower                                                            |
| json                       | 4.15 ms                                                         | 4.32 ms: 1.04x slower                                                           |
| json_loads                 | 20.4 us                                                         | 21.5 us: 1.06x slower                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 1.18 ms: 1.07x slower                                                           |
| unpickle                   | 9.71 us                                                         | 10.5 us: 1.08x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 137 us: 1.08x slower                                                            |
| pickle                     | 7.79 us                                                         | 8.47 us: 1.09x slower                                                           |
| json_dumps                 | 7.40 ms                                                         | 8.13 ms: 1.10x slower                                                           |
| pidigits                   | 199 ms                                                          | 219 ms: 1.10x slower                                                            |
| telco                      | 5.51 ms                                                         | 6.23 ms: 1.13x slower                                                           |
| regex_v8                   | 15.0 ms                                                         | 17.3 ms: 1.15x slower                                                           |
| coverage                   | 48.4 ms                                                         | 56.3 ms: 1.16x slower                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 23.5 ms: 1.23x slower                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 96.0 ms: 1.27x slower                                                           |
| python_startup             | 22.4 ms                                                         | 29.5 ms: 1.32x slower                                                           |
| gc_traversal               | 1.44 ms                                                         | 2.44 ms: 1.70x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 1.20 ms: 1.84x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 219 ms: 2.18x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.19x faster                                                                    |

Benchmark hidden because not significant (2): asyncio_tcp, xml_etree_generate
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (13) of results/bm-20250308-3.14.0a5+-a3990df-CLANG/bm-20250308-pythonperf1_win32-x86-python-a3990df6121880e8c678-3.14.0a5+-a3990df.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.200x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: unknown