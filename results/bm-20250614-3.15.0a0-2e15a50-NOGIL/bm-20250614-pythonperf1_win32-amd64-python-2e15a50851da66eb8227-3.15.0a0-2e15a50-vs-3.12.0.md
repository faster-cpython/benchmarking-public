# Results vs. 3.12.0

- fork: python
- ref: 2e15a50851da66eb8227
- machine: windows-amd64
- commit hash: 2e15a50
- commit date: 2025-06-14
- overall geometric mean: 1.206x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 336 ms: 1.20x slower                                                             |
| docutils       | 1.98 sec                                                        | 4.15 sec: 2.09x slower                                                           |
| Geometric mean | (ref)                                                           | 1.58x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 549 ms: 1.23x faster                                                             |
| async_tree_io              | 693 ms                                                          | 577 ms: 1.20x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 456 ms: 1.20x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 479 ms: 1.18x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 311 ms: 1.13x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 246 ms: 1.13x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 334 ms: 1.09x faster                                                             |
| async_tree_none            | 298 ms                                                          | 274 ms: 1.08x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.15x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 199 ms                                                          | 141 ms: 1.41x faster                                                             |
| float          | 76.7 ms                                                         | 97.9 ms: 1.28x slower                                                            |
| nbody          | 127 ms                                                          | 177 ms: 1.39x slower                                                             |
| Geometric mean | (ref)                                                           | 1.08x slower                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.81 ms: 1.13x faster                                                            |
| regex_dna      | 127 ms                                                          | 113 ms: 1.12x faster                                                             |
| regex_v8       | 15.0 ms                                                         | 16.9 ms: 1.12x slower                                                            |
| regex_compile  | 129 ms                                                          | 160 ms: 1.24x slower                                                             |
| Geometric mean | (ref)                                                           | 1.03x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| xml_etree_parse      | 113 ms                                                          | 112 ms: 1.01x faster                                                             |
| pickle_dict          | 19.9 us                                                         | 22.0 us: 1.10x slower                                                            |
| json_loads           | 20.4 us                                                         | 22.7 us: 1.11x slower                                                            |
| pickle_list          | 3.37 us                                                         | 3.78 us: 1.12x slower                                                            |
| unpickle_list        | 2.95 us                                                         | 3.44 us: 1.17x slower                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 93.0 ms: 1.20x slower                                                            |
| pickle               | 7.79 us                                                         | 9.74 us: 1.25x slower                                                            |
| unpickle             | 9.71 us                                                         | 12.2 us: 1.26x slower                                                            |
| json_dumps           | 7.40 ms                                                         | 9.48 ms: 1.28x slower                                                            |
| xml_etree_process    | 53.2 ms                                                         | 79.0 ms: 1.48x slower                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 107 ms: 1.49x slower                                                             |
| pickle_pure_python   | 286 us                                                          | 448 us: 1.57x slower                                                             |
| unpickle_pure_python | 210 us                                                          | 358 us: 1.70x slower                                                             |
| tomli_loads          | 2.20 sec                                                        | 5.01 sec: 2.28x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.33x slower                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.3 ms: 1.06x slower                                                            |
| python_startup         | 22.4 ms                                                         | 28.0 ms: 1.25x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.15x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.9 ms                                                         | 45.4 ms: 1.23x slower                                                            |
| mako            | 9.96 ms                                                         | 16.5 ms: 1.66x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.43x slower                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 2.65 sec: 6.66x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 36.0 ms: 2.54x faster                                                            |
| pidigits                   | 199 ms                                                          | 141 ms: 1.41x faster                                                             |
| sqlite_synth               | 2.07 us                                                         | 1.67 us: 1.24x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 549 ms: 1.23x faster                                                             |
| async_tree_io              | 693 ms                                                          | 577 ms: 1.20x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 456 ms: 1.20x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 479 ms: 1.18x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 311 ms: 1.13x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 246 ms: 1.13x faster                                                             |
| regex_effbot               | 2.04 ms                                                         | 1.81 ms: 1.13x faster                                                            |
| regex_dna                  | 127 ms                                                          | 113 ms: 1.12x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 334 ms: 1.09x faster                                                             |
| async_tree_none            | 298 ms                                                          | 274 ms: 1.08x faster                                                             |
| deepcopy                   | 360 us                                                          | 332 us: 1.08x faster                                                             |
| asyncio_tcp                | 662 ms                                                          | 613 ms: 1.08x faster                                                             |
| dulwich_log                | 58.5 ms                                                         | 56.8 ms: 1.03x faster                                                            |
| xml_etree_parse            | 113 ms                                                          | 112 ms: 1.01x faster                                                             |
| json                       | 4.15 ms                                                         | 4.20 ms: 1.01x slower                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 20.3 ms: 1.06x slower                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 3.44 us: 1.06x slower                                                            |
| generators                 | 38.5 ms                                                         | 41.5 ms: 1.08x slower                                                            |
| pickle_dict                | 19.9 us                                                         | 22.0 us: 1.10x slower                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 1.22 ms: 1.11x slower                                                            |
| json_loads                 | 20.4 us                                                         | 22.7 us: 1.11x slower                                                            |
| logging_format             | 10.4 us                                                         | 11.7 us: 1.12x slower                                                            |
| pickle_list                | 3.37 us                                                         | 3.78 us: 1.12x slower                                                            |
| regex_v8                   | 15.0 ms                                                         | 16.9 ms: 1.12x slower                                                            |
| deepcopy_memo              | 38.4 us                                                         | 43.3 us: 1.13x slower                                                            |
| logging_simple             | 9.75 us                                                         | 11.0 us: 1.13x slower                                                            |
| unpickle_list              | 2.95 us                                                         | 3.44 us: 1.17x slower                                                            |
| sympy_sum                  | 123 ms                                                          | 144 ms: 1.17x slower                                                             |
| mdp                        | 1.91 sec                                                        | 2.24 sec: 1.17x slower                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 89.5 ms: 1.19x slower                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 93.0 ms: 1.20x slower                                                            |
| sympy_integrate            | 17.5 ms                                                         | 21.0 ms: 1.20x slower                                                            |
| 2to3                       | 280 ms                                                          | 336 ms: 1.20x slower                                                             |
| sympy_str                  | 240 ms                                                          | 292 ms: 1.22x slower                                                             |
| gc_traversal               | 1.44 ms                                                         | 1.77 ms: 1.23x slower                                                            |
| sympy_expand               | 398 ms                                                          | 490 ms: 1.23x slower                                                             |
| django_template            | 36.9 ms                                                         | 45.4 ms: 1.23x slower                                                            |
| regex_compile              | 129 ms                                                          | 160 ms: 1.24x slower                                                             |
| pickle                     | 7.79 us                                                         | 9.74 us: 1.25x slower                                                            |
| python_startup             | 22.4 ms                                                         | 28.0 ms: 1.25x slower                                                            |
| unpickle                   | 9.71 us                                                         | 12.2 us: 1.26x slower                                                            |
| float                      | 76.7 ms                                                         | 97.9 ms: 1.28x slower                                                            |
| json_dumps                 | 7.40 ms                                                         | 9.48 ms: 1.28x slower                                                            |
| unpack_sequence            | 62.5 ns                                                         | 80.4 ns: 1.29x slower                                                            |
| async_generators           | 313 ms                                                          | 410 ms: 1.31x slower                                                             |
| raytrace                   | 308 ms                                                          | 408 ms: 1.33x slower                                                             |
| comprehensions             | 19.2 us                                                         | 25.6 us: 1.33x slower                                                            |
| nqueens                    | 93.7 ms                                                         | 126 ms: 1.35x slower                                                             |
| meteor_contest             | 86.9 ms                                                         | 120 ms: 1.38x slower                                                             |
| chaos                      | 69.4 ms                                                         | 95.7 ms: 1.38x slower                                                            |
| go                         | 137 ms                                                          | 190 ms: 1.39x slower                                                             |
| nbody                      | 127 ms                                                          | 177 ms: 1.39x slower                                                             |
| telco                      | 5.51 ms                                                         | 7.92 ms: 1.44x slower                                                            |
| scimark_sor                | 130 ms                                                          | 187 ms: 1.44x slower                                                             |
| pyflate                    | 424 ms                                                          | 619 ms: 1.46x slower                                                             |
| xml_etree_process          | 53.2 ms                                                         | 79.0 ms: 1.48x slower                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 107 ms: 1.49x slower                                                             |
| scimark_fft                | 271 ms                                                          | 411 ms: 1.52x slower                                                             |
| hexiom                     | 6.82 ms                                                         | 10.6 ms: 1.55x slower                                                            |
| typing_runtime_protocols   | 126 us                                                          | 198 us: 1.57x slower                                                             |
| pickle_pure_python         | 286 us                                                          | 448 us: 1.57x slower                                                             |
| coroutines                 | 20.9 ms                                                         | 32.8 ms: 1.57x slower                                                            |
| spectral_norm              | 104 ms                                                          | 166 ms: 1.60x slower                                                             |
| scimark_monte_carlo        | 66.4 ms                                                         | 107 ms: 1.61x slower                                                             |
| fannkuch                   | 354 ms                                                          | 580 ms: 1.64x slower                                                             |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 6.37 ms: 1.65x slower                                                            |
| deltablue                  | 3.58 ms                                                         | 5.92 ms: 1.65x slower                                                            |
| mako                       | 9.96 ms                                                         | 16.5 ms: 1.66x slower                                                            |
| richards                   | 41.3 ms                                                         | 69.4 ms: 1.68x slower                                                            |
| richards_super             | 46.5 ms                                                         | 78.5 ms: 1.69x slower                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 118 ms: 1.70x slower                                                             |
| unpickle_pure_python       | 210 us                                                          | 358 us: 1.70x slower                                                             |
| pycparser                  | 978 ms                                                          | 1.68 sec: 1.72x slower                                                           |
| coverage                   | 48.4 ms                                                         | 83.7 ms: 1.73x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.13 ms: 1.73x slower                                                            |
| scimark_lu                 | 93.2 ms                                                         | 163 ms: 1.75x slower                                                             |
| pprint_safe_repr           | 721 ms                                                          | 1.43 sec: 1.98x slower                                                           |
| docutils                   | 1.98 sec                                                        | 4.15 sec: 2.09x slower                                                           |
| tomli_loads                | 2.20 sec                                                        | 5.01 sec: 2.28x slower                                                           |
| pprint_pformat             | 1.50 sec                                                        | 4.07 sec: 2.71x slower                                                           |
| logging_silent             | 101 ns                                                          | 589 ns: 5.83x slower                                                             |
| Geometric mean             | (ref)                                                           | 1.24x slower                                                                     |
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250614-3.15.0a0-2e15a50-NOGIL/bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.206x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.23x
- 95% likely to have a slowdown of 1.22x
- 99% likely to have a slowdown of 1.19x

# Memory
- memory change: unknown