# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_mcmodel_again
- machine: windows-x86
- commit hash: 86ef9a1
- commit date: 2025-02-12
- overall geometric mean: 1.090x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-pythonperf1_win32-x86-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 273 ms: 1.03x faster                                                                  |
| docutils       | 1.98 sec                                                        | 1.97 sec: 1.01x faster                                                                |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-pythonperf1_win32-x86-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_io              | 693 ms                                                          | 479 ms: 1.45x faster                                                                  |
| async_tree_io_tg           | 677 ms                                                          | 477 ms: 1.42x faster                                                                  |
| async_tree_memoization_tg  | 350 ms                                                          | 266 ms: 1.32x faster                                                                  |
| async_tree_none_tg         | 278 ms                                                          | 212 ms: 1.31x faster                                                                  |
| async_tree_memoization     | 364 ms                                                          | 278 ms: 1.31x faster                                                                  |
| async_tree_none            | 298 ms                                                          | 230 ms: 1.29x faster                                                                  |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 490 ms: 1.15x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 478 ms: 1.14x faster                                                                  |
| Geometric mean             | (ref)                                                           | 1.29x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-pythonperf1_win32-x86-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| float          | 76.7 ms                                                         | 52.5 ms: 1.46x faster                                                                 |
| nbody          | 127 ms                                                          | 111 ms: 1.14x faster                                                                  |
| pidigits       | 199 ms                                                          | 203 ms: 1.02x slower                                                                  |
| Geometric mean | (ref)                                                           | 1.18x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-pythonperf1_win32-x86-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.53 ms: 1.33x faster                                                                 |
| regex_compile  | 129 ms                                                          | 118 ms: 1.10x faster                                                                  |
| regex_dna      | 127 ms                                                          | 117 ms: 1.09x faster                                                                  |
| regex_v8       | 15.0 ms                                                         | 15.7 ms: 1.04x slower                                                                 |
| Geometric mean | (ref)                                                           | 1.11x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-pythonperf1_win32-x86-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.80 sec: 1.22x faster                                                                |
| xml_etree_iterparse  | 77.6 ms                                                         | 67.0 ms: 1.16x faster                                                                 |
| xml_etree_parse      | 113 ms                                                          | 107 ms: 1.05x faster                                                                  |
| xml_etree_generate   | 72.1 ms                                                         | 75.8 ms: 1.05x slower                                                                 |
| xml_etree_process    | 53.2 ms                                                         | 56.2 ms: 1.06x slower                                                                 |
| unpickle_pure_python | 210 us                                                          | 227 us: 1.08x slower                                                                  |
| json_loads           | 20.4 us                                                         | 22.2 us: 1.09x slower                                                                 |
| pickle_pure_python   | 286 us                                                          | 325 us: 1.14x slower                                                                  |
| json_dumps           | 7.40 ms                                                         | 9.38 ms: 1.27x slower                                                                 |
| Geometric mean       | (ref)                                                           | 1.03x slower                                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-pythonperf1_win32-x86-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 21.7 ms: 1.14x slower                                                                 |
| python_startup         | 22.4 ms                                                         | 28.4 ms: 1.27x slower                                                                 |
| Geometric mean         | (ref)                                                           | 1.20x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-pythonperf1_win32-x86-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.47 ms: 1.33x faster                                                                 |
| django_template | 36.9 ms                                                         | 36.4 ms: 1.01x faster                                                                 |
| Geometric mean  | (ref)                                                           | 1.16x faster                                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-pythonperf1_win32-x86-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 22.3 us: 1.72x faster                                                                 |
| generators                 | 38.5 ms                                                         | 23.3 ms: 1.65x faster                                                                 |
| spectral_norm              | 104 ms                                                          | 65.7 ms: 1.58x faster                                                                 |
| float                      | 76.7 ms                                                         | 52.5 ms: 1.46x faster                                                                 |
| async_tree_io              | 693 ms                                                          | 479 ms: 1.45x faster                                                                  |
| pathlib                    | 91.4 ms                                                         | 63.3 ms: 1.44x faster                                                                 |
| logging_silent             | 101 ns                                                          | 71.1 ns: 1.42x faster                                                                 |
| async_tree_io_tg           | 677 ms                                                          | 477 ms: 1.42x faster                                                                  |
| deepcopy                   | 360 us                                                          | 259 us: 1.39x faster                                                                  |
| scimark_lu                 | 93.2 ms                                                         | 67.2 ms: 1.39x faster                                                                 |
| scimark_sor                | 130 ms                                                          | 96.4 ms: 1.35x faster                                                                 |
| scimark_monte_carlo        | 66.4 ms                                                         | 49.4 ms: 1.34x faster                                                                 |
| mako                       | 9.96 ms                                                         | 7.47 ms: 1.33x faster                                                                 |
| regex_effbot               | 2.04 ms                                                         | 1.53 ms: 1.33x faster                                                                 |
| async_tree_memoization_tg  | 350 ms                                                          | 266 ms: 1.32x faster                                                                  |
| coroutines                 | 20.9 ms                                                         | 15.9 ms: 1.32x faster                                                                 |
| async_tree_none_tg         | 278 ms                                                          | 212 ms: 1.31x faster                                                                  |
| async_tree_memoization     | 364 ms                                                          | 278 ms: 1.31x faster                                                                  |
| async_tree_none            | 298 ms                                                          | 230 ms: 1.29x faster                                                                  |
| go                         | 137 ms                                                          | 109 ms: 1.25x faster                                                                  |
| pyflate                    | 424 ms                                                          | 339 ms: 1.25x faster                                                                  |
| tomli_loads                | 2.20 sec                                                        | 1.80 sec: 1.22x faster                                                                |
| chaos                      | 69.4 ms                                                         | 57.1 ms: 1.22x faster                                                                 |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.18 ms: 1.21x faster                                                                 |
| raytrace                   | 308 ms                                                          | 254 ms: 1.21x faster                                                                  |
| deltablue                  | 3.58 ms                                                         | 2.99 ms: 1.20x faster                                                                 |
| logging_simple             | 9.75 us                                                         | 8.30 us: 1.17x faster                                                                 |
| deepcopy_reduce            | 3.23 us                                                         | 2.75 us: 1.17x faster                                                                 |
| comprehensions             | 19.2 us                                                         | 16.5 us: 1.17x faster                                                                 |
| xml_etree_iterparse        | 77.6 ms                                                         | 67.0 ms: 1.16x faster                                                                 |
| logging_format             | 10.4 us                                                         | 9.03 us: 1.15x faster                                                                 |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 490 ms: 1.15x faster                                                                  |
| nbody                      | 127 ms                                                          | 111 ms: 1.14x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 478 ms: 1.14x faster                                                                  |
| hexiom                     | 6.82 ms                                                         | 5.98 ms: 1.14x faster                                                                 |
| richards                   | 41.3 ms                                                         | 36.9 ms: 1.12x faster                                                                 |
| dulwich_log                | 58.5 ms                                                         | 52.5 ms: 1.11x faster                                                                 |
| sqlite_synth               | 2.07 us                                                         | 1.86 us: 1.11x faster                                                                 |
| regex_compile              | 129 ms                                                          | 118 ms: 1.10x faster                                                                  |
| regex_dna                  | 127 ms                                                          | 117 ms: 1.09x faster                                                                  |
| sympy_sum                  | 123 ms                                                          | 115 ms: 1.07x faster                                                                  |
| richards_super             | 46.5 ms                                                         | 43.5 ms: 1.07x faster                                                                 |
| scimark_fft                | 271 ms                                                          | 255 ms: 1.06x faster                                                                  |
| xml_etree_parse            | 113 ms                                                          | 107 ms: 1.05x faster                                                                  |
| sqlglot_parse              | 1.25 ms                                                         | 1.20 ms: 1.04x faster                                                                 |
| sqlglot_transpile          | 1.53 ms                                                         | 1.47 ms: 1.04x faster                                                                 |
| mdp                        | 1.91 sec                                                        | 1.86 sec: 1.03x faster                                                                |
| sympy_integrate            | 17.5 ms                                                         | 17.0 ms: 1.03x faster                                                                 |
| 2to3                       | 280 ms                                                          | 273 ms: 1.03x faster                                                                  |
| sympy_str                  | 240 ms                                                          | 235 ms: 1.02x faster                                                                  |
| django_template            | 36.9 ms                                                         | 36.4 ms: 1.01x faster                                                                 |
| docutils                   | 1.98 sec                                                        | 1.97 sec: 1.01x faster                                                                |
| pycparser                  | 978 ms                                                          | 983 ms: 1.01x slower                                                                  |
| pidigits                   | 199 ms                                                          | 203 ms: 1.02x slower                                                                  |
| sympy_expand               | 398 ms                                                          | 412 ms: 1.04x slower                                                                  |
| meteor_contest             | 86.9 ms                                                         | 90.3 ms: 1.04x slower                                                                 |
| async_generators           | 313 ms                                                          | 326 ms: 1.04x slower                                                                  |
| regex_v8                   | 15.0 ms                                                         | 15.7 ms: 1.04x slower                                                                 |
| sqlglot_optimize           | 48.5 ms                                                         | 50.5 ms: 1.04x slower                                                                 |
| pprint_pformat             | 1.50 sec                                                        | 1.56 sec: 1.04x slower                                                                |
| pprint_safe_repr           | 721 ms                                                          | 756 ms: 1.05x slower                                                                  |
| xml_etree_generate         | 72.1 ms                                                         | 75.8 ms: 1.05x slower                                                                 |
| xml_etree_process          | 53.2 ms                                                         | 56.2 ms: 1.06x slower                                                                 |
| crypto_pyaes               | 69.2 ms                                                         | 73.2 ms: 1.06x slower                                                                 |
| sqlglot_normalize          | 100 ms                                                          | 106 ms: 1.06x slower                                                                  |
| fannkuch                   | 354 ms                                                          | 375 ms: 1.06x slower                                                                  |
| coverage                   | 48.4 ms                                                         | 51.6 ms: 1.07x slower                                                                 |
| unpickle_pure_python       | 210 us                                                          | 227 us: 1.08x slower                                                                  |
| json                       | 4.15 ms                                                         | 4.51 ms: 1.09x slower                                                                 |
| json_loads                 | 20.4 us                                                         | 22.2 us: 1.09x slower                                                                 |
| nqueens                    | 93.7 ms                                                         | 106 ms: 1.13x slower                                                                  |
| pickle_pure_python         | 286 us                                                          | 325 us: 1.14x slower                                                                  |
| python_startup_no_site     | 19.1 ms                                                         | 21.7 ms: 1.14x slower                                                                 |
| bench_thread_pool          | 1.10 ms                                                         | 1.34 ms: 1.22x slower                                                                 |
| bench_mp_pool              | 75.4 ms                                                         | 93.6 ms: 1.24x slower                                                                 |
| gc_traversal               | 1.44 ms                                                         | 1.81 ms: 1.26x slower                                                                 |
| json_dumps                 | 7.40 ms                                                         | 9.38 ms: 1.27x slower                                                                 |
| python_startup             | 22.4 ms                                                         | 28.4 ms: 1.27x slower                                                                 |
| typing_runtime_protocols   | 126 us                                                          | 168 us: 1.33x slower                                                                  |
| telco                      | 5.51 ms                                                         | 7.80 ms: 1.42x slower                                                                 |
| create_gc_cycles           | 652 us                                                          | 1.05 ms: 1.60x slower                                                                 |
| Geometric mean             | (ref)                                                           | 1.09x faster                                                                          |
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250212-3.14.0a4+-86ef9a1-JIT/bm-20250212-pythonperf1_win32-x86-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.090x faster

# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown