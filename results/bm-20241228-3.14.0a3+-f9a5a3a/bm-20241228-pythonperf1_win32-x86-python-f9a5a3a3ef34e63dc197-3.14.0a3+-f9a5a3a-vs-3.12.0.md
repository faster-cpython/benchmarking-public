# Results vs. 3.12.0

- fork: python
- ref: f9a5a3a3ef34e63dc197
- machine: windows-x86
- commit hash: f9a5a3a
- commit date: 2024-12-28
- overall geometric mean: 1.176x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 245 ms: 1.14x faster                                                            |
| docutils       | 1.98 sec                                                        | 1.78 sec: 1.11x faster                                                          |
| Geometric mean | (ref)                                                           | 1.13x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 427 ms: 1.58x faster                                                            |
| async_tree_io              | 693 ms                                                          | 442 ms: 1.57x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 229 ms: 1.53x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 183 ms: 1.52x faster                                                            |
| async_tree_none            | 298 ms                                                          | 202 ms: 1.47x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 250 ms: 1.46x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 442 ms: 1.27x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 437 ms: 1.25x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.45x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 86.5 ms: 1.47x faster                                                           |
| float          | 76.7 ms                                                         | 59.1 ms: 1.30x faster                                                           |
| pidigits       | 199 ms                                                          | 197 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                           | 1.24x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.56 ms: 1.31x faster                                                           |
| regex_compile  | 129 ms                                                          | 101 ms: 1.28x faster                                                            |
| regex_dna      | 127 ms                                                          | 114 ms: 1.11x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 15.4 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                           | 1.16x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.60 sec: 1.37x faster                                                          |
| unpickle_pure_python | 210 us                                                          | 169 us: 1.24x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 65.3 ms: 1.19x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 48.5 ms: 1.10x faster                                                           |
| pickle_pure_python   | 286 us                                                          | 262 us: 1.09x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 66.5 ms: 1.08x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 107 ms: 1.05x faster                                                            |
| json_loads           | 20.4 us                                                         | 20.6 us: 1.01x slower                                                           |
| json_dumps           | 7.40 ms                                                         | 8.64 ms: 1.17x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.10x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.4 ms: 1.02x slower                                                           |
| python_startup         | 22.4 ms                                                         | 26.1 ms: 1.17x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.53 ms: 1.32x faster                                                           |
| django_template | 36.9 ms                                                         | 32.2 ms: 1.15x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.23x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 22.1 us: 1.74x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 427 ms: 1.58x faster                                                            |
| async_tree_io              | 693 ms                                                          | 442 ms: 1.57x faster                                                            |
| deepcopy                   | 360 us                                                          | 231 us: 1.56x faster                                                            |
| generators                 | 38.5 ms                                                         | 25.0 ms: 1.54x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 229 ms: 1.53x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 183 ms: 1.52x faster                                                            |
| spectral_norm              | 104 ms                                                          | 69.9 ms: 1.48x faster                                                           |
| async_tree_none            | 298 ms                                                          | 202 ms: 1.47x faster                                                            |
| nbody                      | 127 ms                                                          | 86.5 ms: 1.47x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 250 ms: 1.46x faster                                                            |
| logging_silent             | 101 ns                                                          | 70.2 ns: 1.44x faster                                                           |
| go                         | 137 ms                                                          | 95.8 ms: 1.43x faster                                                           |
| comprehensions             | 19.2 us                                                         | 13.6 us: 1.41x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 4.87 ms: 1.40x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.56 ms: 1.40x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.60 sec: 1.37x faster                                                          |
| scimark_sor                | 130 ms                                                          | 94.6 ms: 1.37x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 68.4 ms: 1.36x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.39 us: 1.35x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.92 ms: 1.32x faster                                                           |
| mako                       | 9.96 ms                                                         | 7.53 ms: 1.32x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.56 ms: 1.31x faster                                                           |
| float                      | 76.7 ms                                                         | 59.1 ms: 1.30x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 16.2 ms: 1.29x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 51.5 ms: 1.29x faster                                                           |
| nqueens                    | 93.7 ms                                                         | 73.1 ms: 1.28x faster                                                           |
| chaos                      | 69.4 ms                                                         | 54.2 ms: 1.28x faster                                                           |
| regex_compile              | 129 ms                                                          | 101 ms: 1.28x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 442 ms: 1.27x faster                                                            |
| pyflate                    | 424 ms                                                          | 334 ms: 1.27x faster                                                            |
| logging_simple             | 9.75 us                                                         | 7.69 us: 1.27x faster                                                           |
| scimark_fft                | 271 ms                                                          | 217 ms: 1.25x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 437 ms: 1.25x faster                                                            |
| raytrace                   | 308 ms                                                          | 247 ms: 1.25x faster                                                            |
| unpickle_pure_python       | 210 us                                                          | 169 us: 1.24x faster                                                            |
| logging_format             | 10.4 us                                                         | 8.44 us: 1.23x faster                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 1.02 ms: 1.23x faster                                                           |
| sqlglot_transpile          | 1.53 ms                                                         | 1.26 ms: 1.22x faster                                                           |
| fannkuch                   | 354 ms                                                          | 293 ms: 1.21x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 65.3 ms: 1.19x faster                                                           |
| pycparser                  | 978 ms                                                          | 828 ms: 1.18x faster                                                            |
| richards                   | 41.3 ms                                                         | 35.2 ms: 1.17x faster                                                           |
| dulwich_log                | 58.5 ms                                                         | 49.8 ms: 1.17x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 105 ms: 1.17x faster                                                            |
| pprint_pformat             | 1.50 sec                                                        | 1.29 sec: 1.16x faster                                                          |
| sqlglot_optimize           | 48.5 ms                                                         | 41.8 ms: 1.16x faster                                                           |
| pprint_safe_repr           | 721 ms                                                          | 624 ms: 1.16x faster                                                            |
| mdp                        | 1.91 sec                                                        | 1.65 sec: 1.16x faster                                                          |
| sympy_integrate            | 17.5 ms                                                         | 15.2 ms: 1.15x faster                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 59.9 ms: 1.15x faster                                                           |
| richards_super             | 46.5 ms                                                         | 40.4 ms: 1.15x faster                                                           |
| django_template            | 36.9 ms                                                         | 32.2 ms: 1.15x faster                                                           |
| 2to3                       | 280 ms                                                          | 245 ms: 1.14x faster                                                            |
| sympy_str                  | 240 ms                                                          | 212 ms: 1.13x faster                                                            |
| regex_dna                  | 127 ms                                                          | 114 ms: 1.11x faster                                                            |
| docutils                   | 1.98 sec                                                        | 1.78 sec: 1.11x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 83.1 ms: 1.10x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 48.5 ms: 1.10x faster                                                           |
| pickle_pure_python         | 286 us                                                          | 262 us: 1.09x faster                                                            |
| meteor_contest             | 86.9 ms                                                         | 79.9 ms: 1.09x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 66.5 ms: 1.08x faster                                                           |
| sqlite_synth               | 2.07 us                                                         | 1.92 us: 1.08x faster                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 1.02 ms: 1.08x faster                                                           |
| sympy_expand               | 398 ms                                                          | 372 ms: 1.07x faster                                                            |
| async_generators           | 313 ms                                                          | 298 ms: 1.05x faster                                                            |
| xml_etree_parse            | 113 ms                                                          | 107 ms: 1.05x faster                                                            |
| pidigits                   | 199 ms                                                          | 197 ms: 1.01x faster                                                            |
| json_loads                 | 20.4 us                                                         | 20.6 us: 1.01x slower                                                           |
| json                       | 4.15 ms                                                         | 4.21 ms: 1.01x slower                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 19.4 ms: 1.02x slower                                                           |
| regex_v8                   | 15.0 ms                                                         | 15.4 ms: 1.03x slower                                                           |
| coverage                   | 48.4 ms                                                         | 51.2 ms: 1.06x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 139 us: 1.10x slower                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 87.3 ms: 1.16x slower                                                           |
| python_startup             | 22.4 ms                                                         | 26.1 ms: 1.17x slower                                                           |
| json_dumps                 | 7.40 ms                                                         | 8.64 ms: 1.17x slower                                                           |
| telco                      | 5.51 ms                                                         | 6.47 ms: 1.17x slower                                                           |
| mypy2                      | 584 ms                                                          | 686 ms: 1.18x slower                                                            |
| gc_traversal               | 1.44 ms                                                         | 1.79 ms: 1.24x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 1.05 ms: 1.62x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 221 ms: 2.20x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.17x faster                                                                    |
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241228-3.14.0a3+-f9a5a3a/bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.176x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: unknown