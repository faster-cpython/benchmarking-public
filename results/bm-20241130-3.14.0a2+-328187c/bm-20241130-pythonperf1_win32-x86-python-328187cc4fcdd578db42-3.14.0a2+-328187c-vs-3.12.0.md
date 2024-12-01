# Results vs. 3.12.0

- fork: python
- ref: 328187cc4fcdd578db42
- machine: windows-x86
- commit hash: 328187c
- commit date: 2024-11-30
- overall geometric mean: 1.150x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 241 ms: 1.16x faster                                                            |
| docutils       | 1.98 sec                                                        | 1.81 sec: 1.09x faster                                                          |
| Geometric mean | (ref)                                                           | 1.13x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 248 ms: 1.41x faster                                                            |
| async_tree_none            | 298 ms                                                          | 215 ms: 1.38x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 203 ms: 1.37x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 273 ms: 1.33x faster                                                            |
| async_tree_io              | 693 ms                                                          | 534 ms: 1.30x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 523 ms: 1.30x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 479 ms: 1.18x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 475 ms: 1.15x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.30x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 83.6 ms: 1.52x faster                                                           |
| float          | 76.7 ms                                                         | 60.2 ms: 1.27x faster                                                           |
| pidigits       | 199 ms                                                          | 204 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                           | 1.24x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.55 ms: 1.31x faster                                                           |
| regex_compile  | 129 ms                                                          | 107 ms: 1.21x faster                                                            |
| regex_dna      | 127 ms                                                          | 119 ms: 1.07x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 15.5 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                           | 1.13x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.77 sec: 1.24x faster                                                          |
| unpickle_pure_python | 210 us                                                          | 173 us: 1.21x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 67.6 ms: 1.15x faster                                                           |
| pickle_pure_python   | 286 us                                                          | 257 us: 1.11x faster                                                            |
| xml_etree_process    | 53.2 ms                                                         | 47.9 ms: 1.11x faster                                                           |
| xml_etree_generate   | 72.1 ms                                                         | 66.3 ms: 1.09x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 110 ms: 1.03x faster                                                            |
| json_loads           | 20.4 us                                                         | 20.8 us: 1.02x slower                                                           |
| json_dumps           | 7.40 ms                                                         | 8.64 ms: 1.17x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.08x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.1 ms: 1.05x slower                                                           |
| python_startup         | 22.4 ms                                                         | 26.7 ms: 1.19x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.12x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.49 ms: 1.33x faster                                                           |
| django_template | 36.9 ms                                                         | 32.6 ms: 1.13x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.23x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 21.2 us: 1.81x faster                                                           |
| generators                 | 38.5 ms                                                         | 24.0 ms: 1.61x faster                                                           |
| nbody                      | 127 ms                                                          | 83.6 ms: 1.52x faster                                                           |
| deepcopy                   | 360 us                                                          | 245 us: 1.47x faster                                                            |
| spectral_norm              | 104 ms                                                          | 71.4 ms: 1.45x faster                                                           |
| comprehensions             | 19.2 us                                                         | 13.4 us: 1.43x faster                                                           |
| logging_silent             | 101 ns                                                          | 71.0 ns: 1.42x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 4.81 ms: 1.42x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 66.0 ms: 1.41x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 248 ms: 1.41x faster                                                            |
| async_tree_none            | 298 ms                                                          | 215 ms: 1.38x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 2.59 ms: 1.38x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 203 ms: 1.37x faster                                                            |
| go                         | 137 ms                                                          | 102 ms: 1.34x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 273 ms: 1.33x faster                                                            |
| mako                       | 9.96 ms                                                         | 7.49 ms: 1.33x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.55 ms: 1.31x faster                                                           |
| scimark_sor                | 130 ms                                                          | 99.1 ms: 1.31x faster                                                           |
| async_tree_io              | 693 ms                                                          | 534 ms: 1.30x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 523 ms: 1.30x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 16.3 ms: 1.28x faster                                                           |
| chaos                      | 69.4 ms                                                         | 54.1 ms: 1.28x faster                                                           |
| float                      | 76.7 ms                                                         | 60.2 ms: 1.27x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.53 us: 1.27x faster                                                           |
| nqueens                    | 93.7 ms                                                         | 74.0 ms: 1.27x faster                                                           |
| raytrace                   | 308 ms                                                          | 244 ms: 1.26x faster                                                            |
| logging_simple             | 9.75 us                                                         | 7.75 us: 1.26x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.77 sec: 1.24x faster                                                          |
| scimark_monte_carlo        | 66.4 ms                                                         | 53.7 ms: 1.24x faster                                                           |
| logging_format             | 10.4 us                                                         | 8.46 us: 1.23x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 173 us: 1.21x faster                                                            |
| regex_compile              | 129 ms                                                          | 107 ms: 1.21x faster                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.20 ms: 1.20x faster                                                           |
| pycparser                  | 978 ms                                                          | 812 ms: 1.20x faster                                                            |
| pyflate                    | 424 ms                                                          | 353 ms: 1.20x faster                                                            |
| sqlglot_parse              | 1.25 ms                                                         | 1.04 ms: 1.20x faster                                                           |
| sqlglot_transpile          | 1.53 ms                                                         | 1.29 ms: 1.19x faster                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 58.4 ms: 1.18x faster                                                           |
| scimark_fft                | 271 ms                                                          | 230 ms: 1.18x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 479 ms: 1.18x faster                                                            |
| sympy_sum                  | 123 ms                                                          | 105 ms: 1.18x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 15.1 ms: 1.16x faster                                                           |
| dulwich_log                | 58.5 ms                                                         | 50.4 ms: 1.16x faster                                                           |
| 2to3                       | 280 ms                                                          | 241 ms: 1.16x faster                                                            |
| fannkuch                   | 354 ms                                                          | 305 ms: 1.16x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 475 ms: 1.15x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 67.6 ms: 1.15x faster                                                           |
| sympy_str                  | 240 ms                                                          | 210 ms: 1.14x faster                                                            |
| django_template            | 36.9 ms                                                         | 32.6 ms: 1.13x faster                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 42.8 ms: 1.13x faster                                                           |
| pprint_safe_repr           | 721 ms                                                          | 639 ms: 1.13x faster                                                            |
| pprint_pformat             | 1.50 sec                                                        | 1.34 sec: 1.12x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 81.7 ms: 1.12x faster                                                           |
| pickle_pure_python         | 286 us                                                          | 257 us: 1.11x faster                                                            |
| xml_etree_process          | 53.2 ms                                                         | 47.9 ms: 1.11x faster                                                           |
| docutils                   | 1.98 sec                                                        | 1.81 sec: 1.09x faster                                                          |
| bench_thread_pool          | 1.10 ms                                                         | 1.01 ms: 1.09x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 79.5 ms: 1.09x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.75 sec: 1.09x faster                                                          |
| xml_etree_generate         | 72.1 ms                                                         | 66.3 ms: 1.09x faster                                                           |
| richards_super             | 46.5 ms                                                         | 42.9 ms: 1.08x faster                                                           |
| richards                   | 41.3 ms                                                         | 38.2 ms: 1.08x faster                                                           |
| sympy_expand               | 398 ms                                                          | 369 ms: 1.08x faster                                                            |
| regex_dna                  | 127 ms                                                          | 119 ms: 1.07x faster                                                            |
| async_generators           | 313 ms                                                          | 298 ms: 1.05x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 2.00 us: 1.04x faster                                                           |
| xml_etree_parse            | 113 ms                                                          | 110 ms: 1.03x faster                                                            |
| json_loads                 | 20.4 us                                                         | 20.8 us: 1.02x slower                                                           |
| json                       | 4.15 ms                                                         | 4.25 ms: 1.02x slower                                                           |
| pidigits                   | 199 ms                                                          | 204 ms: 1.02x slower                                                            |
| regex_v8                   | 15.0 ms                                                         | 15.5 ms: 1.03x slower                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 20.1 ms: 1.05x slower                                                           |
| coverage                   | 48.4 ms                                                         | 54.1 ms: 1.12x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 143 us: 1.13x slower                                                            |
| json_dumps                 | 7.40 ms                                                         | 8.64 ms: 1.17x slower                                                           |
| python_startup             | 22.4 ms                                                         | 26.7 ms: 1.19x slower                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.72 ms: 1.20x slower                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 92.1 ms: 1.22x slower                                                           |
| telco                      | 5.51 ms                                                         | 6.87 ms: 1.25x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 1.12 ms: 1.71x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 220 ms: 2.19x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.15x faster                                                                    |
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241130-3.14.0a2+-328187c/bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.150x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: unknown