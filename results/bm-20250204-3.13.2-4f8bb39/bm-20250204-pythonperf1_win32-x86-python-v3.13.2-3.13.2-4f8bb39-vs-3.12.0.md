# Results vs. 3.12.0

- fork: python
- ref: v3.13.2
- machine: windows-x86
- commit hash: 4f8bb39
- commit date: 2025-02-04
- overall geometric mean: 1.140x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-pythonperf1_win32-x86-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 254 ms: 1.10x faster                                            |
| chameleon      | 7.75 ms                                                         | 6.05 ms: 1.28x faster                                           |
| docutils       | 1.98 sec                                                        | 1.79 sec: 1.11x faster                                          |
| tornado_http   | 105 ms                                                          | 112 ms: 1.07x slower                                            |
| Geometric mean | (ref)                                                           | 1.10x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-pythonperf1_win32-x86-python-v3.13.2-3.13.2-4f8bb39 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_io              | 693 ms                                                          | 533 ms: 1.30x faster                                            |
| async_tree_io_tg           | 677 ms                                                          | 521 ms: 1.30x faster                                            |
| async_tree_none_tg         | 278 ms                                                          | 221 ms: 1.26x faster                                            |
| async_tree_memoization     | 364 ms                                                          | 301 ms: 1.21x faster                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 292 ms: 1.20x faster                                            |
| async_tree_none            | 298 ms                                                          | 248 ms: 1.20x faster                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 516 ms: 1.09x faster                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 506 ms: 1.08x faster                                            |
| Geometric mean             | (ref)                                                           | 1.20x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-pythonperf1_win32-x86-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 79.1 ms: 1.61x faster                                           |
| float          | 76.7 ms                                                         | 54.1 ms: 1.42x faster                                           |
| pidigits       | 199 ms                                                          | 203 ms: 1.02x slower                                            |
| Geometric mean | (ref)                                                           | 1.31x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-pythonperf1_win32-x86-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.58 ms: 1.29x faster                                           |
| regex_compile  | 129 ms                                                          | 103 ms: 1.25x faster                                            |
| regex_dna      | 127 ms                                                          | 128 ms: 1.01x slower                                            |
| regex_v8       | 15.0 ms                                                         | 16.1 ms: 1.07x slower                                           |
| Geometric mean | (ref)                                                           | 1.10x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-pythonperf1_win32-x86-python-v3.13.2-3.13.2-4f8bb39 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.65 sec: 1.33x faster                                          |
| unpickle_pure_python | 210 us                                                          | 158 us: 1.33x faster                                            |
| pickle_pure_python   | 286 us                                                          | 234 us: 1.22x faster                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 64.7 ms: 1.20x faster                                           |
| xml_etree_process    | 53.2 ms                                                         | 45.0 ms: 1.18x faster                                           |
| xml_etree_generate   | 72.1 ms                                                         | 62.9 ms: 1.15x faster                                           |
| xml_etree_parse      | 113 ms                                                          | 110 ms: 1.03x faster                                            |
| json_dumps           | 7.40 ms                                                         | 7.29 ms: 1.01x faster                                           |
| json_loads           | 20.4 us                                                         | 21.7 us: 1.07x slower                                           |
| Geometric mean       | (ref)                                                           | 1.15x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-pythonperf1_win32-x86-python-v3.13.2-3.13.2-4f8bb39 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 21.3 ms: 1.12x slower                                           |
| python_startup         | 22.4 ms                                                         | 29.8 ms: 1.33x slower                                           |
| Geometric mean         | (ref)                                                           | 1.22x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-pythonperf1_win32-x86-python-v3.13.2-3.13.2-4f8bb39 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.38 ms: 1.35x faster                                           |
| django_template | 36.9 ms                                                         | 29.6 ms: 1.25x faster                                           |
| Geometric mean  | (ref)                                                           | 1.30x faster                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-pythonperf1_win32-x86-python-v3.13.2-3.13.2-4f8bb39 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| generators                 | 38.5 ms                                                         | 22.0 ms: 1.75x faster                                           |
| logging_silent             | 101 ns                                                          | 62.1 ns: 1.63x faster                                           |
| nbody                      | 127 ms                                                          | 79.1 ms: 1.61x faster                                           |
| deepcopy_memo              | 38.4 us                                                         | 24.6 us: 1.56x faster                                           |
| scimark_lu                 | 93.2 ms                                                         | 60.1 ms: 1.55x faster                                           |
| scimark_sor                | 130 ms                                                          | 84.0 ms: 1.55x faster                                           |
| comprehensions             | 19.2 us                                                         | 12.7 us: 1.51x faster                                           |
| hexiom                     | 6.82 ms                                                         | 4.53 ms: 1.51x faster                                           |
| deltablue                  | 3.58 ms                                                         | 2.39 ms: 1.50x faster                                           |
| spectral_norm              | 104 ms                                                          | 69.3 ms: 1.50x faster                                           |
| raytrace                   | 308 ms                                                          | 208 ms: 1.48x faster                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 46.7 ms: 1.42x faster                                           |
| float                      | 76.7 ms                                                         | 54.1 ms: 1.42x faster                                           |
| pathlib                    | 91.4 ms                                                         | 67.2 ms: 1.36x faster                                           |
| chaos                      | 69.4 ms                                                         | 51.1 ms: 1.36x faster                                           |
| mako                       | 9.96 ms                                                         | 7.38 ms: 1.35x faster                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.88 ms: 1.34x faster                                           |
| tomli_loads                | 2.20 sec                                                        | 1.65 sec: 1.33x faster                                          |
| unpickle_pure_python       | 210 us                                                          | 158 us: 1.33x faster                                            |
| scimark_fft                | 271 ms                                                          | 207 ms: 1.31x faster                                            |
| coroutines                 | 20.9 ms                                                         | 16.0 ms: 1.31x faster                                           |
| async_tree_io              | 693 ms                                                          | 533 ms: 1.30x faster                                            |
| async_tree_io_tg           | 677 ms                                                          | 521 ms: 1.30x faster                                            |
| pyflate                    | 424 ms                                                          | 327 ms: 1.30x faster                                            |
| regex_effbot               | 2.04 ms                                                         | 1.58 ms: 1.29x faster                                           |
| chameleon                  | 7.75 ms                                                         | 6.05 ms: 1.28x faster                                           |
| async_tree_none_tg         | 278 ms                                                          | 221 ms: 1.26x faster                                            |
| nqueens                    | 93.7 ms                                                         | 74.9 ms: 1.25x faster                                           |
| regex_compile              | 129 ms                                                          | 103 ms: 1.25x faster                                            |
| django_template            | 36.9 ms                                                         | 29.6 ms: 1.25x faster                                           |
| fannkuch                   | 354 ms                                                          | 284 ms: 1.24x faster                                            |
| richards_super             | 46.5 ms                                                         | 37.7 ms: 1.23x faster                                           |
| go                         | 137 ms                                                          | 112 ms: 1.23x faster                                            |
| pickle_pure_python         | 286 us                                                          | 234 us: 1.22x faster                                            |
| richards                   | 41.3 ms                                                         | 33.9 ms: 1.22x faster                                           |
| sqlglot_parse              | 1.25 ms                                                         | 1.02 ms: 1.22x faster                                           |
| async_tree_memoization     | 364 ms                                                          | 301 ms: 1.21x faster                                            |
| crypto_pyaes               | 69.2 ms                                                         | 57.4 ms: 1.21x faster                                           |
| sqlglot_transpile          | 1.53 ms                                                         | 1.27 ms: 1.21x faster                                           |
| logging_simple             | 9.75 us                                                         | 8.09 us: 1.21x faster                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 292 ms: 1.20x faster                                            |
| async_tree_none            | 298 ms                                                          | 248 ms: 1.20x faster                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 64.7 ms: 1.20x faster                                           |
| mdp                        | 1.91 sec                                                        | 1.61 sec: 1.19x faster                                          |
| xml_etree_process          | 53.2 ms                                                         | 45.0 ms: 1.18x faster                                           |
| logging_format             | 10.4 us                                                         | 8.81 us: 1.18x faster                                           |
| deepcopy                   | 360 us                                                          | 306 us: 1.18x faster                                            |
| dulwich_log                | 58.5 ms                                                         | 50.1 ms: 1.17x faster                                           |
| sympy_integrate            | 17.5 ms                                                         | 15.1 ms: 1.16x faster                                           |
| async_generators           | 313 ms                                                          | 270 ms: 1.16x faster                                            |
| pprint_pformat             | 1.50 sec                                                        | 1.29 sec: 1.16x faster                                          |
| xml_etree_generate         | 72.1 ms                                                         | 62.9 ms: 1.15x faster                                           |
| sympy_sum                  | 123 ms                                                          | 107 ms: 1.14x faster                                            |
| sqlglot_optimize           | 48.5 ms                                                         | 42.4 ms: 1.14x faster                                           |
| pprint_safe_repr           | 721 ms                                                          | 631 ms: 1.14x faster                                            |
| sympy_str                  | 240 ms                                                          | 213 ms: 1.12x faster                                            |
| meteor_contest             | 86.9 ms                                                         | 77.6 ms: 1.12x faster                                           |
| pycparser                  | 978 ms                                                          | 875 ms: 1.12x faster                                            |
| docutils                   | 1.98 sec                                                        | 1.79 sec: 1.11x faster                                          |
| 2to3                       | 280 ms                                                          | 254 ms: 1.10x faster                                            |
| deepcopy_reduce            | 3.23 us                                                         | 2.93 us: 1.10x faster                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 516 ms: 1.09x faster                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 506 ms: 1.08x faster                                            |
| sqlite_synth               | 2.07 us                                                         | 1.92 us: 1.08x faster                                           |
| sqlalchemy_imperative      | 12.3 ms                                                         | 11.5 ms: 1.07x faster                                           |
| bench_thread_pool          | 1.10 ms                                                         | 1.03 ms: 1.07x faster                                           |
| sqlalchemy_declarative     | 103 ms                                                          | 96.1 ms: 1.07x faster                                           |
| sympy_expand               | 398 ms                                                          | 377 ms: 1.05x faster                                            |
| xml_etree_parse            | 113 ms                                                          | 110 ms: 1.03x faster                                            |
| json_dumps                 | 7.40 ms                                                         | 7.29 ms: 1.01x faster                                           |
| regex_dna                  | 127 ms                                                          | 128 ms: 1.01x slower                                            |
| pidigits                   | 199 ms                                                          | 203 ms: 1.02x slower                                            |
| json_loads                 | 20.4 us                                                         | 21.7 us: 1.07x slower                                           |
| tornado_http               | 105 ms                                                          | 112 ms: 1.07x slower                                            |
| json                       | 4.15 ms                                                         | 4.45 ms: 1.07x slower                                           |
| regex_v8                   | 15.0 ms                                                         | 16.1 ms: 1.07x slower                                           |
| python_startup_no_site     | 19.1 ms                                                         | 21.3 ms: 1.12x slower                                           |
| typing_runtime_protocols   | 126 us                                                          | 144 us: 1.14x slower                                            |
| bench_mp_pool              | 75.4 ms                                                         | 92.1 ms: 1.22x slower                                           |
| gc_traversal               | 1.44 ms                                                         | 1.77 ms: 1.23x slower                                           |
| telco                      | 5.51 ms                                                         | 6.95 ms: 1.26x slower                                           |
| python_startup             | 22.4 ms                                                         | 29.8 ms: 1.33x slower                                           |
| create_gc_cycles           | 652 us                                                          | 1.08 ms: 1.65x slower                                           |
| sqlglot_normalize          | 100 ms                                                          | 222 ms: 2.22x slower                                            |
| coverage                   | 48.4 ms                                                         | 318 ms: 6.56x slower                                            |
| Geometric mean             | (ref)                                                           | 1.14x faster                                                    |
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250204-3.13.2-4f8bb39/bm-20250204-pythonperf1_win32-x86-python-v3.13.2-3.13.2-4f8bb39.json: asyncio_websockets, bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.140x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: unknown