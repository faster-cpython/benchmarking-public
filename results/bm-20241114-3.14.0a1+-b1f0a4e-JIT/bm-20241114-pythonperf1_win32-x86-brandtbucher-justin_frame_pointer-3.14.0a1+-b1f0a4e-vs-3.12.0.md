# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_frame_pointer
- machine: windows-x86
- commit hash: b1f0a4e
- commit date: 2024-11-14
- overall geometric mean: 1.007x faster
- HPT reliability: 57.35%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-pythonperf1_win32-x86-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 298 ms: 1.07x slower                                                                  |
| docutils       | 1.98 sec                                                        | 2.17 sec: 1.09x slower                                                                |
| Geometric mean | (ref)                                                           | 1.08x slower                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-pythonperf1_win32-x86-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 276 ms: 1.27x faster                                                                  |
| async_tree_none_tg         | 278 ms                                                          | 220 ms: 1.26x faster                                                                  |
| async_tree_io              | 693 ms                                                          | 554 ms: 1.25x faster                                                                  |
| async_tree_none            | 298 ms                                                          | 250 ms: 1.19x faster                                                                  |
| async_tree_io_tg           | 677 ms                                                          | 570 ms: 1.19x faster                                                                  |
| async_tree_memoization     | 364 ms                                                          | 306 ms: 1.19x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 483 ms: 1.13x faster                                                                  |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 518 ms: 1.09x faster                                                                  |
| Geometric mean             | (ref)                                                           | 1.19x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-pythonperf1_win32-x86-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| float          | 76.7 ms                                                         | 59.5 ms: 1.29x faster                                                                 |
| nbody          | 127 ms                                                          | 124 ms: 1.03x faster                                                                  |
| pidigits       | 199 ms                                                          | 202 ms: 1.01x slower                                                                  |
| Geometric mean | (ref)                                                           | 1.09x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-pythonperf1_win32-x86-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.83 ms: 1.11x faster                                                                 |
| regex_dna      | 127 ms                                                          | 115 ms: 1.10x faster                                                                  |
| regex_compile  | 129 ms                                                          | 126 ms: 1.02x faster                                                                  |
| regex_v8       | 15.0 ms                                                         | 15.9 ms: 1.05x slower                                                                 |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-pythonperf1_win32-x86-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.98 sec: 1.11x faster                                                                |
| unpickle_pure_python | 210 us                                                          | 190 us: 1.10x faster                                                                  |
| xml_etree_iterparse  | 77.6 ms                                                         | 70.7 ms: 1.10x faster                                                                 |
| xml_etree_generate   | 72.1 ms                                                         | 76.0 ms: 1.05x slower                                                                 |
| json_loads           | 20.4 us                                                         | 21.9 us: 1.07x slower                                                                 |
| xml_etree_process    | 53.2 ms                                                         | 58.0 ms: 1.09x slower                                                                 |
| pickle_pure_python   | 286 us                                                          | 315 us: 1.10x slower                                                                  |
| json_dumps           | 7.40 ms                                                         | 9.18 ms: 1.24x slower                                                                 |
| Geometric mean       | (ref)                                                           | 1.03x slower                                                                          |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-pythonperf1_win32-x86-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.6 ms: 1.03x slower                                                                 |
| python_startup         | 22.4 ms                                                         | 25.7 ms: 1.15x slower                                                                 |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-pythonperf1_win32-x86-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.83 ms: 1.27x faster                                                                 |
| django_template | 36.9 ms                                                         | 37.1 ms: 1.01x slower                                                                 |
| Geometric mean  | (ref)                                                           | 1.12x faster                                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-pythonperf1_win32-x86-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 25.9 us: 1.48x faster                                                                 |
| float                      | 76.7 ms                                                         | 59.5 ms: 1.29x faster                                                                 |
| mako                       | 9.96 ms                                                         | 7.83 ms: 1.27x faster                                                                 |
| async_tree_memoization_tg  | 350 ms                                                          | 276 ms: 1.27x faster                                                                  |
| async_tree_none_tg         | 278 ms                                                          | 220 ms: 1.26x faster                                                                  |
| scimark_lu                 | 93.2 ms                                                         | 74.5 ms: 1.25x faster                                                                 |
| async_tree_io              | 693 ms                                                          | 554 ms: 1.25x faster                                                                  |
| coroutines                 | 20.9 ms                                                         | 16.7 ms: 1.25x faster                                                                 |
| deepcopy                   | 360 us                                                          | 292 us: 1.24x faster                                                                  |
| logging_silent             | 101 ns                                                          | 83.2 ns: 1.21x faster                                                                 |
| async_tree_none            | 298 ms                                                          | 250 ms: 1.19x faster                                                                  |
| async_tree_io_tg           | 677 ms                                                          | 570 ms: 1.19x faster                                                                  |
| async_tree_memoization     | 364 ms                                                          | 306 ms: 1.19x faster                                                                  |
| logging_simple             | 9.75 us                                                         | 8.25 us: 1.18x faster                                                                 |
| logging_format             | 10.4 us                                                         | 8.95 us: 1.16x faster                                                                 |
| scimark_sor                | 130 ms                                                          | 112 ms: 1.16x faster                                                                  |
| dulwich_log                | 58.5 ms                                                         | 51.3 ms: 1.14x faster                                                                 |
| spectral_norm              | 104 ms                                                          | 91.1 ms: 1.14x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 483 ms: 1.13x faster                                                                  |
| regex_effbot               | 2.04 ms                                                         | 1.83 ms: 1.11x faster                                                                 |
| deepcopy_reduce            | 3.23 us                                                         | 2.91 us: 1.11x faster                                                                 |
| tomli_loads                | 2.20 sec                                                        | 1.98 sec: 1.11x faster                                                                |
| unpickle_pure_python       | 210 us                                                          | 190 us: 1.10x faster                                                                  |
| pathlib                    | 91.4 ms                                                         | 83.1 ms: 1.10x faster                                                                 |
| regex_dna                  | 127 ms                                                          | 115 ms: 1.10x faster                                                                  |
| xml_etree_iterparse        | 77.6 ms                                                         | 70.7 ms: 1.10x faster                                                                 |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.51 ms: 1.10x faster                                                                 |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 518 ms: 1.09x faster                                                                  |
| go                         | 137 ms                                                          | 130 ms: 1.06x faster                                                                  |
| sqlite_synth               | 2.07 us                                                         | 1.96 us: 1.06x faster                                                                 |
| bench_thread_pool          | 1.10 ms                                                         | 1.05 ms: 1.05x faster                                                                 |
| deltablue                  | 3.58 ms                                                         | 3.42 ms: 1.05x faster                                                                 |
| pycparser                  | 978 ms                                                          | 951 ms: 1.03x faster                                                                  |
| nbody                      | 127 ms                                                          | 124 ms: 1.03x faster                                                                  |
| regex_compile              | 129 ms                                                          | 126 ms: 1.02x faster                                                                  |
| sqlglot_parse              | 1.25 ms                                                         | 1.23 ms: 1.01x faster                                                                 |
| pyflate                    | 424 ms                                                          | 419 ms: 1.01x faster                                                                  |
| generators                 | 38.5 ms                                                         | 38.2 ms: 1.01x faster                                                                 |
| django_template            | 36.9 ms                                                         | 37.1 ms: 1.01x slower                                                                 |
| mdp                        | 1.91 sec                                                        | 1.93 sec: 1.01x slower                                                                |
| pidigits                   | 199 ms                                                          | 202 ms: 1.01x slower                                                                  |
| scimark_monte_carlo        | 66.4 ms                                                         | 67.5 ms: 1.02x slower                                                                 |
| raytrace                   | 308 ms                                                          | 315 ms: 1.02x slower                                                                  |
| comprehensions             | 19.2 us                                                         | 19.7 us: 1.03x slower                                                                 |
| python_startup_no_site     | 19.1 ms                                                         | 19.6 ms: 1.03x slower                                                                 |
| sqlglot_transpile          | 1.53 ms                                                         | 1.58 ms: 1.03x slower                                                                 |
| chaos                      | 69.4 ms                                                         | 71.7 ms: 1.03x slower                                                                 |
| sympy_sum                  | 123 ms                                                          | 128 ms: 1.04x slower                                                                  |
| richards_super             | 46.5 ms                                                         | 48.8 ms: 1.05x slower                                                                 |
| fannkuch                   | 354 ms                                                          | 372 ms: 1.05x slower                                                                  |
| xml_etree_generate         | 72.1 ms                                                         | 76.0 ms: 1.05x slower                                                                 |
| regex_v8                   | 15.0 ms                                                         | 15.9 ms: 1.05x slower                                                                 |
| crypto_pyaes               | 69.2 ms                                                         | 73.4 ms: 1.06x slower                                                                 |
| scimark_fft                | 271 ms                                                          | 288 ms: 1.06x slower                                                                  |
| 2to3                       | 280 ms                                                          | 298 ms: 1.07x slower                                                                  |
| sympy_str                  | 240 ms                                                          | 256 ms: 1.07x slower                                                                  |
| meteor_contest             | 86.9 ms                                                         | 93.1 ms: 1.07x slower                                                                 |
| json_loads                 | 20.4 us                                                         | 21.9 us: 1.07x slower                                                                 |
| pprint_pformat             | 1.50 sec                                                        | 1.61 sec: 1.08x slower                                                                |
| coverage                   | 48.4 ms                                                         | 52.3 ms: 1.08x slower                                                                 |
| sympy_expand               | 398 ms                                                          | 430 ms: 1.08x slower                                                                  |
| richards                   | 41.3 ms                                                         | 45.0 ms: 1.09x slower                                                                 |
| xml_etree_process          | 53.2 ms                                                         | 58.0 ms: 1.09x slower                                                                 |
| async_generators           | 313 ms                                                          | 342 ms: 1.09x slower                                                                  |
| pprint_safe_repr           | 721 ms                                                          | 787 ms: 1.09x slower                                                                  |
| docutils                   | 1.98 sec                                                        | 2.17 sec: 1.09x slower                                                                |
| pickle_pure_python         | 286 us                                                          | 315 us: 1.10x slower                                                                  |
| nqueens                    | 93.7 ms                                                         | 104 ms: 1.11x slower                                                                  |
| json                       | 4.15 ms                                                         | 4.61 ms: 1.11x slower                                                                 |
| sympy_integrate            | 17.5 ms                                                         | 19.7 ms: 1.12x slower                                                                 |
| hexiom                     | 6.82 ms                                                         | 7.80 ms: 1.14x slower                                                                 |
| python_startup             | 22.4 ms                                                         | 25.7 ms: 1.15x slower                                                                 |
| sqlglot_normalize          | 100 ms                                                          | 118 ms: 1.18x slower                                                                  |
| sqlglot_optimize           | 48.5 ms                                                         | 59.3 ms: 1.22x slower                                                                 |
| gc_traversal               | 1.44 ms                                                         | 1.77 ms: 1.23x slower                                                                 |
| bench_mp_pool              | 75.4 ms                                                         | 92.6 ms: 1.23x slower                                                                 |
| json_dumps                 | 7.40 ms                                                         | 9.18 ms: 1.24x slower                                                                 |
| typing_runtime_protocols   | 126 us                                                          | 176 us: 1.40x slower                                                                  |
| telco                      | 5.51 ms                                                         | 7.71 ms: 1.40x slower                                                                 |
| create_gc_cycles           | 652 us                                                          | 1.16 ms: 1.78x slower                                                                 |
| Geometric mean             | (ref)                                                           | 1.01x faster                                                                          |

Benchmark hidden because not significant (1): xml_etree_parse
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241114-3.14.0a1+-b1f0a4e-JIT/bm-20241114-pythonperf1_win32-x86-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.007x faster
# HPT report

- Reliability score: 57.35% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown