# Results vs. 3.12.0

- fork: python
- ref: e1baa778f602ede66831
- machine: windows-x86
- commit hash: e1baa77
- commit date: 2025-01-02
- overall geometric mean: 1.167x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-pythonperf1_win32-x86-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 243 ms: 1.15x faster                                                            |
| docutils       | 1.98 sec                                                        | 1.80 sec: 1.10x faster                                                          |
| Geometric mean | (ref)                                                           | 1.13x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-pythonperf1_win32-x86-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 408 ms: 1.66x faster                                                            |
| async_tree_io              | 693 ms                                                          | 426 ms: 1.63x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 222 ms: 1.58x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 177 ms: 1.57x faster                                                            |
| async_tree_none            | 298 ms                                                          | 194 ms: 1.53x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 240 ms: 1.51x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 434 ms: 1.30x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 423 ms: 1.29x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.50x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-pythonperf1_win32-x86-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 85.8 ms: 1.48x faster                                                           |
| float          | 76.7 ms                                                         | 55.8 ms: 1.37x faster                                                           |
| pidigits       | 199 ms                                                          | 197 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                           | 1.27x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-pythonperf1_win32-x86-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 101 ms: 1.28x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.65 ms: 1.23x faster                                                           |
| regex_dna      | 127 ms                                                          | 126 ms: 1.01x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 15.8 ms: 1.05x slower                                                           |
| Geometric mean | (ref)                                                           | 1.11x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-pythonperf1_win32-x86-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.64 sec: 1.34x faster                                                          |
| unpickle_pure_python | 210 us                                                          | 171 us: 1.23x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 67.2 ms: 1.16x faster                                                           |
| pickle_pure_python   | 286 us                                                          | 259 us: 1.10x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 67.8 ms: 1.06x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 50.0 ms: 1.06x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 111 ms: 1.02x faster                                                            |
| json_loads           | 20.4 us                                                         | 20.7 us: 1.02x slower                                                           |
| json_dumps           | 7.40 ms                                                         | 8.81 ms: 1.19x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.08x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-pythonperf1_win32-x86-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.3 ms: 1.07x slower                                                           |
| python_startup         | 22.4 ms                                                         | 26.9 ms: 1.20x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.13x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-pythonperf1_win32-x86-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.79 ms: 1.28x faster                                                           |
| django_template | 36.9 ms                                                         | 31.8 ms: 1.16x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.22x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-pythonperf1_win32-x86-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 22.2 us: 1.73x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 408 ms: 1.66x faster                                                            |
| async_tree_io              | 693 ms                                                          | 426 ms: 1.63x faster                                                            |
| deepcopy                   | 360 us                                                          | 227 us: 1.59x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 222 ms: 1.58x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 177 ms: 1.57x faster                                                            |
| generators                 | 38.5 ms                                                         | 24.6 ms: 1.57x faster                                                           |
| async_tree_none            | 298 ms                                                          | 194 ms: 1.53x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 240 ms: 1.51x faster                                                            |
| nbody                      | 127 ms                                                          | 85.8 ms: 1.48x faster                                                           |
| spectral_norm              | 104 ms                                                          | 71.3 ms: 1.46x faster                                                           |
| logging_silent             | 101 ns                                                          | 70.7 ns: 1.43x faster                                                           |
| go                         | 137 ms                                                          | 96.4 ms: 1.42x faster                                                           |
| comprehensions             | 19.2 us                                                         | 13.8 us: 1.39x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.59 ms: 1.38x faster                                                           |
| float                      | 76.7 ms                                                         | 55.8 ms: 1.37x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 5.00 ms: 1.36x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 68.6 ms: 1.36x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.64 sec: 1.34x faster                                                          |
| deepcopy_reduce            | 3.23 us                                                         | 2.42 us: 1.33x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.97 ms: 1.30x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 434 ms: 1.30x faster                                                            |
| scimark_sor                | 130 ms                                                          | 101 ms: 1.29x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 423 ms: 1.29x faster                                                            |
| chaos                      | 69.4 ms                                                         | 54.0 ms: 1.28x faster                                                           |
| regex_compile              | 129 ms                                                          | 101 ms: 1.28x faster                                                            |
| mako                       | 9.96 ms                                                         | 7.79 ms: 1.28x faster                                                           |
| raytrace                   | 308 ms                                                          | 242 ms: 1.27x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 16.6 ms: 1.26x faster                                                           |
| pyflate                    | 424 ms                                                          | 336 ms: 1.26x faster                                                            |
| scimark_fft                | 271 ms                                                          | 216 ms: 1.26x faster                                                            |
| logging_simple             | 9.75 us                                                         | 7.80 us: 1.25x faster                                                           |
| nqueens                    | 93.7 ms                                                         | 75.6 ms: 1.24x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 53.8 ms: 1.24x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.65 ms: 1.23x faster                                                           |
| logging_format             | 10.4 us                                                         | 8.44 us: 1.23x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 171 us: 1.23x faster                                                            |
| sqlglot_parse              | 1.25 ms                                                         | 1.02 ms: 1.22x faster                                                           |
| sqlglot_transpile          | 1.53 ms                                                         | 1.27 ms: 1.20x faster                                                           |
| pycparser                  | 978 ms                                                          | 812 ms: 1.20x faster                                                            |
| fannkuch                   | 354 ms                                                          | 298 ms: 1.19x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 49.4 ms: 1.18x faster                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 41.7 ms: 1.16x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 106 ms: 1.16x faster                                                            |
| django_template            | 36.9 ms                                                         | 31.8 ms: 1.16x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 67.2 ms: 1.16x faster                                                           |
| 2to3                       | 280 ms                                                          | 243 ms: 1.15x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 15.3 ms: 1.15x faster                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 60.9 ms: 1.14x faster                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.32 sec: 1.13x faster                                                          |
| sympy_str                  | 240 ms                                                          | 213 ms: 1.12x faster                                                            |
| richards                   | 41.3 ms                                                         | 36.8 ms: 1.12x faster                                                           |
| pprint_safe_repr           | 721 ms                                                          | 647 ms: 1.11x faster                                                            |
| pathlib                    | 91.4 ms                                                         | 82.9 ms: 1.10x faster                                                           |
| pickle_pure_python         | 286 us                                                          | 259 us: 1.10x faster                                                            |
| mdp                        | 1.91 sec                                                        | 1.73 sec: 1.10x faster                                                          |
| docutils                   | 1.98 sec                                                        | 1.80 sec: 1.10x faster                                                          |
| richards_super             | 46.5 ms                                                         | 42.3 ms: 1.10x faster                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 1.00 ms: 1.10x faster                                                           |
| sqlite_synth               | 2.07 us                                                         | 1.93 us: 1.08x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 67.8 ms: 1.06x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 50.0 ms: 1.06x faster                                                           |
| sympy_expand               | 398 ms                                                          | 375 ms: 1.06x faster                                                            |
| meteor_contest             | 86.9 ms                                                         | 82.2 ms: 1.06x faster                                                           |
| async_generators           | 313 ms                                                          | 302 ms: 1.04x faster                                                            |
| xml_etree_parse            | 113 ms                                                          | 111 ms: 1.02x faster                                                            |
| pidigits                   | 199 ms                                                          | 197 ms: 1.01x faster                                                            |
| regex_dna                  | 127 ms                                                          | 126 ms: 1.01x faster                                                            |
| json_loads                 | 20.4 us                                                         | 20.7 us: 1.02x slower                                                           |
| regex_v8                   | 15.0 ms                                                         | 15.8 ms: 1.05x slower                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 20.3 ms: 1.07x slower                                                           |
| coverage                   | 48.4 ms                                                         | 51.6 ms: 1.07x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 141 us: 1.12x slower                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 87.2 ms: 1.16x slower                                                           |
| mypy2                      | 584 ms                                                          | 680 ms: 1.17x slower                                                            |
| json_dumps                 | 7.40 ms                                                         | 8.81 ms: 1.19x slower                                                           |
| python_startup             | 22.4 ms                                                         | 26.9 ms: 1.20x slower                                                           |
| telco                      | 5.51 ms                                                         | 6.73 ms: 1.22x slower                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.81 ms: 1.25x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 1.05 ms: 1.62x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 217 ms: 2.17x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.17x faster                                                                    |

Benchmark hidden because not significant (1): json
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250102-3.14.0a3+-e1baa77/bm-20250102-pythonperf1_win32-x86-python-e1baa778f602ede66831-3.14.0a3+-e1baa77.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.167x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: unknown