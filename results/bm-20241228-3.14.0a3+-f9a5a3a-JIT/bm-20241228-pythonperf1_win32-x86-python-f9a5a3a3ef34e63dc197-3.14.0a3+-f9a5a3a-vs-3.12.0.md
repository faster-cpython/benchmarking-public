# Results vs. 3.12.0

- fork: python
- ref: f9a5a3a3ef34e63dc197
- machine: windows-x86
- commit hash: f9a5a3a
- commit date: 2024-12-28
- overall geometric mean: 1.066x faster
- HPT reliability: 99.93%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 264 ms: 1.06x faster                                                            |
| docutils       | 1.98 sec                                                        | 1.96 sec: 1.01x faster                                                          |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 468 ms: 1.45x faster                                                            |
| async_tree_io              | 693 ms                                                          | 495 ms: 1.40x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 256 ms: 1.37x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 206 ms: 1.35x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 289 ms: 1.26x faster                                                            |
| async_tree_none            | 298 ms                                                          | 237 ms: 1.25x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 453 ms: 1.21x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 486 ms: 1.16x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.30x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 76.7 ms                                                         | 55.5 ms: 1.38x faster                                                           |
| nbody          | 127 ms                                                          | 98.7 ms: 1.29x faster                                                           |
| pidigits       | 199 ms                                                          | 196 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                           | 1.22x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.54 ms: 1.32x faster                                                           |
| regex_compile  | 129 ms                                                          | 113 ms: 1.14x faster                                                            |
| regex_dna      | 127 ms                                                          | 114 ms: 1.11x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 15.6 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                           | 1.13x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.76 sec: 1.24x faster                                                          |
| xml_etree_iterparse  | 77.6 ms                                                         | 67.0 ms: 1.16x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 107 ms: 1.05x faster                                                            |
| unpickle_pure_python | 210 us                                                          | 204 us: 1.03x faster                                                            |
| json_loads           | 20.4 us                                                         | 20.2 us: 1.01x faster                                                           |
| xml_etree_generate   | 72.1 ms                                                         | 72.9 ms: 1.01x slower                                                           |
| xml_etree_process    | 53.2 ms                                                         | 54.3 ms: 1.02x slower                                                           |
| pickle_pure_python   | 286 us                                                          | 298 us: 1.04x slower                                                            |
| json_dumps           | 7.40 ms                                                         | 9.07 ms: 1.23x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.02x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.5 ms: 1.02x slower                                                           |
| python_startup         | 22.4 ms                                                         | 25.9 ms: 1.16x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.40 ms: 1.35x faster                                                           |
| django_template | 36.9 ms                                                         | 38.2 ms: 1.03x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.14x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 24.2 us: 1.58x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 468 ms: 1.45x faster                                                            |
| async_tree_io              | 693 ms                                                          | 495 ms: 1.40x faster                                                            |
| float                      | 76.7 ms                                                         | 55.5 ms: 1.38x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 256 ms: 1.37x faster                                                            |
| spectral_norm              | 104 ms                                                          | 76.4 ms: 1.36x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 206 ms: 1.35x faster                                                            |
| mako                       | 9.96 ms                                                         | 7.40 ms: 1.35x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.54 ms: 1.32x faster                                                           |
| deepcopy                   | 360 us                                                          | 275 us: 1.31x faster                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.99 ms: 1.29x faster                                                           |
| nbody                      | 127 ms                                                          | 98.7 ms: 1.29x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 16.4 ms: 1.28x faster                                                           |
| scimark_sor                | 130 ms                                                          | 102 ms: 1.27x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 73.7 ms: 1.26x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 289 ms: 1.26x faster                                                            |
| async_tree_none            | 298 ms                                                          | 237 ms: 1.25x faster                                                            |
| tomli_loads                | 2.20 sec                                                        | 1.76 sec: 1.24x faster                                                          |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 453 ms: 1.21x faster                                                            |
| logging_silent             | 101 ns                                                          | 86.3 ns: 1.17x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 486 ms: 1.16x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 67.0 ms: 1.16x faster                                                           |
| logging_simple             | 9.75 us                                                         | 8.43 us: 1.16x faster                                                           |
| scimark_fft                | 271 ms                                                          | 236 ms: 1.15x faster                                                            |
| logging_format             | 10.4 us                                                         | 9.11 us: 1.14x faster                                                           |
| regex_compile              | 129 ms                                                          | 113 ms: 1.14x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 51.2 ms: 1.14x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.84 us: 1.14x faster                                                           |
| go                         | 137 ms                                                          | 122 ms: 1.13x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 3.19 ms: 1.12x faster                                                           |
| regex_dna                  | 127 ms                                                          | 114 ms: 1.11x faster                                                            |
| pyflate                    | 424 ms                                                          | 385 ms: 1.10x faster                                                            |
| pathlib                    | 91.4 ms                                                         | 83.7 ms: 1.09x faster                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 1.15 ms: 1.08x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 61.7 ms: 1.08x faster                                                           |
| sqlglot_transpile          | 1.53 ms                                                         | 1.43 ms: 1.07x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 115 ms: 1.07x faster                                                            |
| fannkuch                   | 354 ms                                                          | 331 ms: 1.07x faster                                                            |
| chaos                      | 69.4 ms                                                         | 65.0 ms: 1.07x faster                                                           |
| sqlite_synth               | 2.07 us                                                         | 1.95 us: 1.06x faster                                                           |
| 2to3                       | 280 ms                                                          | 264 ms: 1.06x faster                                                            |
| xml_etree_parse            | 113 ms                                                          | 107 ms: 1.05x faster                                                            |
| generators                 | 38.5 ms                                                         | 36.9 ms: 1.04x faster                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 1.06 ms: 1.04x faster                                                           |
| pycparser                  | 978 ms                                                          | 945 ms: 1.03x faster                                                            |
| comprehensions             | 19.2 us                                                         | 18.7 us: 1.03x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 204 us: 1.03x faster                                                            |
| pidigits                   | 199 ms                                                          | 196 ms: 1.02x faster                                                            |
| mdp                        | 1.91 sec                                                        | 1.88 sec: 1.02x faster                                                          |
| sympy_str                  | 240 ms                                                          | 236 ms: 1.01x faster                                                            |
| docutils                   | 1.98 sec                                                        | 1.96 sec: 1.01x faster                                                          |
| json_loads                 | 20.4 us                                                         | 20.2 us: 1.01x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 72.9 ms: 1.01x slower                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.52 sec: 1.02x slower                                                          |
| raytrace                   | 308 ms                                                          | 313 ms: 1.02x slower                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 70.5 ms: 1.02x slower                                                           |
| xml_etree_process          | 53.2 ms                                                         | 54.3 ms: 1.02x slower                                                           |
| sympy_expand               | 398 ms                                                          | 406 ms: 1.02x slower                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 19.5 ms: 1.02x slower                                                           |
| json                       | 4.15 ms                                                         | 4.25 ms: 1.02x slower                                                           |
| pprint_safe_repr           | 721 ms                                                          | 744 ms: 1.03x slower                                                            |
| regex_v8                   | 15.0 ms                                                         | 15.6 ms: 1.03x slower                                                           |
| django_template            | 36.9 ms                                                         | 38.2 ms: 1.03x slower                                                           |
| meteor_contest             | 86.9 ms                                                         | 90.5 ms: 1.04x slower                                                           |
| pickle_pure_python         | 286 us                                                          | 298 us: 1.04x slower                                                            |
| sqlglot_optimize           | 48.5 ms                                                         | 51.1 ms: 1.05x slower                                                           |
| nqueens                    | 93.7 ms                                                         | 98.9 ms: 1.06x slower                                                           |
| richards_super             | 46.5 ms                                                         | 49.5 ms: 1.07x slower                                                           |
| async_generators           | 313 ms                                                          | 336 ms: 1.07x slower                                                            |
| sqlglot_normalize          | 100 ms                                                          | 107 ms: 1.07x slower                                                            |
| hexiom                     | 6.82 ms                                                         | 7.34 ms: 1.08x slower                                                           |
| richards                   | 41.3 ms                                                         | 44.5 ms: 1.08x slower                                                           |
| coverage                   | 48.4 ms                                                         | 52.2 ms: 1.08x slower                                                           |
| python_startup             | 22.4 ms                                                         | 25.9 ms: 1.16x slower                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 87.3 ms: 1.16x slower                                                           |
| json_dumps                 | 7.40 ms                                                         | 9.07 ms: 1.23x slower                                                           |
| mypy2                      | 584 ms                                                          | 725 ms: 1.24x slower                                                            |
| gc_traversal               | 1.44 ms                                                         | 1.82 ms: 1.27x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 166 us: 1.32x slower                                                            |
| telco                      | 5.51 ms                                                         | 7.44 ms: 1.35x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 1.06 ms: 1.63x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.06x faster                                                                    |

Benchmark hidden because not significant (1): sympy_integrate
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241228-3.14.0a3+-f9a5a3a-JIT/bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.066x faster

# HPT report

- Reliability score: 99.93% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown