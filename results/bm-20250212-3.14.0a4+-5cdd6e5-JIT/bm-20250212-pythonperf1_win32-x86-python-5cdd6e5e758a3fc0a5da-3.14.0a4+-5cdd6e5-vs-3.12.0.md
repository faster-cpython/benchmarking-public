# Results vs. 3.12.0

- fork: python
- ref: 5cdd6e5e758a3fc0a5da
- machine: windows-x86
- commit hash: 5cdd6e5
- commit date: 2025-02-12
- overall geometric mean: 1.097x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-pythonperf1_win32-x86-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 268 ms: 1.04x faster                                                            |
| docutils       | 1.98 sec                                                        | 2.01 sec: 1.01x slower                                                          |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-pythonperf1_win32-x86-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io              | 693 ms                                                          | 483 ms: 1.44x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 477 ms: 1.42x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 209 ms: 1.33x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 266 ms: 1.32x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 281 ms: 1.30x faster                                                            |
| async_tree_none            | 298 ms                                                          | 231 ms: 1.29x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 451 ms: 1.21x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 467 ms: 1.21x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.31x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-pythonperf1_win32-x86-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 76.7 ms                                                         | 53.6 ms: 1.43x faster                                                           |
| nbody          | 127 ms                                                          | 113 ms: 1.12x faster                                                            |
| Geometric mean | (ref)                                                           | 1.17x faster                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-pythonperf1_win32-x86-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.52 ms: 1.34x faster                                                           |
| regex_compile  | 129 ms                                                          | 118 ms: 1.09x faster                                                            |
| regex_dna      | 127 ms                                                          | 118 ms: 1.07x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 15.6 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                           | 1.11x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-pythonperf1_win32-x86-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.81 sec: 1.22x faster                                                          |
| xml_etree_iterparse  | 77.6 ms                                                         | 68.1 ms: 1.14x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 109 ms: 1.04x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 74.9 ms: 1.04x slower                                                           |
| xml_etree_process    | 53.2 ms                                                         | 55.7 ms: 1.05x slower                                                           |
| unpickle_pure_python | 210 us                                                          | 226 us: 1.08x slower                                                            |
| pickle_pure_python   | 286 us                                                          | 319 us: 1.12x slower                                                            |
| json_loads           | 20.4 us                                                         | 23.1 us: 1.14x slower                                                           |
| json_dumps           | 7.40 ms                                                         | 9.02 ms: 1.22x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.03x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-pythonperf1_win32-x86-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 21.7 ms: 1.14x slower                                                           |
| python_startup         | 22.4 ms                                                         | 28.2 ms: 1.26x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.20x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-pythonperf1_win32-x86-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.69 ms: 1.29x faster                                                           |
| django_template | 36.9 ms                                                         | 35.6 ms: 1.04x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.16x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-pythonperf1_win32-x86-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pathlib                    | 91.4 ms                                                         | 34.0 ms: 2.69x faster                                                           |
| deepcopy_memo              | 38.4 us                                                         | 21.4 us: 1.80x faster                                                           |
| generators                 | 38.5 ms                                                         | 23.7 ms: 1.63x faster                                                           |
| spectral_norm              | 104 ms                                                          | 66.2 ms: 1.57x faster                                                           |
| async_tree_io              | 693 ms                                                          | 483 ms: 1.44x faster                                                            |
| float                      | 76.7 ms                                                         | 53.6 ms: 1.43x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 477 ms: 1.42x faster                                                            |
| deepcopy                   | 360 us                                                          | 256 us: 1.41x faster                                                            |
| logging_silent             | 101 ns                                                          | 72.1 ns: 1.40x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 68.5 ms: 1.36x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.52 ms: 1.34x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 209 ms: 1.33x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 15.7 ms: 1.33x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 266 ms: 1.32x faster                                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 50.5 ms: 1.32x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.75 ms: 1.31x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 281 ms: 1.30x faster                                                            |
| mako                       | 9.96 ms                                                         | 7.69 ms: 1.29x faster                                                           |
| scimark_sor                | 130 ms                                                          | 101 ms: 1.29x faster                                                            |
| async_tree_none            | 298 ms                                                          | 231 ms: 1.29x faster                                                            |
| pyflate                    | 424 ms                                                          | 333 ms: 1.27x faster                                                            |
| go                         | 137 ms                                                          | 110 ms: 1.25x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 2.61 us: 1.23x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.17 ms: 1.22x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.81 sec: 1.22x faster                                                          |
| raytrace                   | 308 ms                                                          | 254 ms: 1.21x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 451 ms: 1.21x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 467 ms: 1.21x faster                                                            |
| chaos                      | 69.4 ms                                                         | 58.5 ms: 1.19x faster                                                           |
| logging_simple             | 9.75 us                                                         | 8.39 us: 1.16x faster                                                           |
| comprehensions             | 19.2 us                                                         | 16.6 us: 1.16x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 68.1 ms: 1.14x faster                                                           |
| logging_format             | 10.4 us                                                         | 9.17 us: 1.13x faster                                                           |
| nbody                      | 127 ms                                                          | 113 ms: 1.12x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 52.4 ms: 1.12x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 6.13 ms: 1.11x faster                                                           |
| richards                   | 41.3 ms                                                         | 37.2 ms: 1.11x faster                                                           |
| sqlite_synth               | 2.07 us                                                         | 1.89 us: 1.10x faster                                                           |
| regex_compile              | 129 ms                                                          | 118 ms: 1.09x faster                                                            |
| richards_super             | 46.5 ms                                                         | 42.9 ms: 1.08x faster                                                           |
| regex_dna                  | 127 ms                                                          | 118 ms: 1.07x faster                                                            |
| sympy_sum                  | 123 ms                                                          | 116 ms: 1.06x faster                                                            |
| 2to3                       | 280 ms                                                          | 268 ms: 1.04x faster                                                            |
| xml_etree_parse            | 113 ms                                                          | 109 ms: 1.04x faster                                                            |
| scimark_fft                | 271 ms                                                          | 261 ms: 1.04x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 16.9 ms: 1.04x faster                                                           |
| django_template            | 36.9 ms                                                         | 35.6 ms: 1.04x faster                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 1.21 ms: 1.03x faster                                                           |
| sympy_str                  | 240 ms                                                          | 233 ms: 1.03x faster                                                            |
| sqlglot_transpile          | 1.53 ms                                                         | 1.49 ms: 1.03x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.89 sec: 1.01x faster                                                          |
| pycparser                  | 978 ms                                                          | 970 ms: 1.01x faster                                                            |
| docutils                   | 1.98 sec                                                        | 2.01 sec: 1.01x slower                                                          |
| sympy_expand               | 398 ms                                                          | 407 ms: 1.02x slower                                                            |
| async_generators           | 313 ms                                                          | 322 ms: 1.03x slower                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 74.9 ms: 1.04x slower                                                           |
| regex_v8                   | 15.0 ms                                                         | 15.6 ms: 1.04x slower                                                           |
| xml_etree_process          | 53.2 ms                                                         | 55.7 ms: 1.05x slower                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 50.8 ms: 1.05x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 105 ms: 1.05x slower                                                            |
| fannkuch                   | 354 ms                                                          | 373 ms: 1.06x slower                                                            |
| pprint_pformat             | 1.50 sec                                                        | 1.59 sec: 1.06x slower                                                          |
| crypto_pyaes               | 69.2 ms                                                         | 73.5 ms: 1.06x slower                                                           |
| unpickle_pure_python       | 210 us                                                          | 226 us: 1.08x slower                                                            |
| pprint_safe_repr           | 721 ms                                                          | 775 ms: 1.08x slower                                                            |
| meteor_contest             | 86.9 ms                                                         | 95.1 ms: 1.10x slower                                                           |
| coverage                   | 48.4 ms                                                         | 53.4 ms: 1.10x slower                                                           |
| nqueens                    | 93.7 ms                                                         | 104 ms: 1.11x slower                                                            |
| json                       | 4.15 ms                                                         | 4.63 ms: 1.12x slower                                                           |
| pickle_pure_python         | 286 us                                                          | 319 us: 1.12x slower                                                            |
| json_loads                 | 20.4 us                                                         | 23.1 us: 1.14x slower                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 21.7 ms: 1.14x slower                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 89.9 ms: 1.19x slower                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 1.34 ms: 1.22x slower                                                           |
| json_dumps                 | 7.40 ms                                                         | 9.02 ms: 1.22x slower                                                           |
| python_startup             | 22.4 ms                                                         | 28.2 ms: 1.26x slower                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.82 ms: 1.26x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 174 us: 1.38x slower                                                            |
| telco                      | 5.51 ms                                                         | 7.68 ms: 1.39x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 1.06 ms: 1.62x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.09x faster                                                                    |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250212-3.14.0a4+-5cdd6e5-JIT/bm-20250212-pythonperf1_win32-x86-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.097x faster

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown