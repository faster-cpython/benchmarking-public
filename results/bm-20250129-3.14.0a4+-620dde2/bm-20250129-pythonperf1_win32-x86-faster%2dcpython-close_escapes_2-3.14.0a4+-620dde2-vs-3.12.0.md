# Results vs. 3.12.0

- fork: faster-cpython
- ref: close_escapes_2
- machine: windows-x86
- commit hash: 620dde2
- commit date: 2025-01-29
- overall geometric mean: 1.109x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-pythonperf1_win32-x86-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 258 ms: 1.09x faster                                                                 |
| docutils       | 1.98 sec                                                        | 1.86 sec: 1.07x faster                                                               |
| Geometric mean | (ref)                                                           | 1.08x faster                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-pythonperf1_win32-x86-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_io              | 693 ms                                                          | 475 ms: 1.46x faster                                                                 |
| async_tree_io_tg           | 677 ms                                                          | 471 ms: 1.44x faster                                                                 |
| async_tree_memoization_tg  | 350 ms                                                          | 253 ms: 1.38x faster                                                                 |
| async_tree_none_tg         | 278 ms                                                          | 205 ms: 1.35x faster                                                                 |
| async_tree_memoization     | 364 ms                                                          | 269 ms: 1.35x faster                                                                 |
| async_tree_none            | 298 ms                                                          | 225 ms: 1.32x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 441 ms: 1.24x faster                                                                 |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 460 ms: 1.23x faster                                                                 |
| Geometric mean             | (ref)                                                           | 1.34x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-pythonperf1_win32-x86-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 87.2 ms: 1.46x faster                                                                |
| float          | 76.7 ms                                                         | 56.0 ms: 1.37x faster                                                                |
| pidigits       | 199 ms                                                          | 202 ms: 1.01x slower                                                                 |
| Geometric mean | (ref)                                                           | 1.25x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-pythonperf1_win32-x86-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.55 ms: 1.31x faster                                                                |
| regex_compile  | 129 ms                                                          | 110 ms: 1.18x faster                                                                 |
| regex_dna      | 127 ms                                                          | 116 ms: 1.10x faster                                                                 |
| regex_v8       | 15.0 ms                                                         | 15.8 ms: 1.05x slower                                                                |
| Geometric mean | (ref)                                                           | 1.13x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-pythonperf1_win32-x86-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.76 sec: 1.25x faster                                                               |
| xml_etree_iterparse  | 77.6 ms                                                         | 67.1 ms: 1.16x faster                                                                |
| unpickle_pure_python | 210 us                                                          | 183 us: 1.15x faster                                                                 |
| xml_etree_process    | 53.2 ms                                                         | 51.7 ms: 1.03x faster                                                                |
| xml_etree_parse      | 113 ms                                                          | 110 ms: 1.03x faster                                                                 |
| xml_etree_generate   | 72.1 ms                                                         | 70.5 ms: 1.02x faster                                                                |
| pickle_pure_python   | 286 us                                                          | 289 us: 1.01x slower                                                                 |
| json_loads           | 20.4 us                                                         | 23.2 us: 1.14x slower                                                                |
| json_dumps           | 7.40 ms                                                         | 9.24 ms: 1.25x slower                                                                |
| Geometric mean       | (ref)                                                           | 1.02x faster                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-pythonperf1_win32-x86-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.0 ms: 1.05x slower                                                                |
| python_startup         | 22.4 ms                                                         | 26.7 ms: 1.20x slower                                                                |
| Geometric mean         | (ref)                                                           | 1.12x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-pythonperf1_win32-x86-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.68 ms: 1.30x faster                                                                |
| django_template | 36.9 ms                                                         | 35.1 ms: 1.05x faster                                                                |
| Geometric mean  | (ref)                                                           | 1.17x faster                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-pythonperf1_win32-x86-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 21.7 us: 1.77x faster                                                                |
| deepcopy                   | 360 us                                                          | 247 us: 1.46x faster                                                                 |
| async_tree_io              | 693 ms                                                          | 475 ms: 1.46x faster                                                                 |
| nbody                      | 127 ms                                                          | 87.2 ms: 1.46x faster                                                                |
| spectral_norm              | 104 ms                                                          | 72.1 ms: 1.44x faster                                                                |
| async_tree_io_tg           | 677 ms                                                          | 471 ms: 1.44x faster                                                                 |
| generators                 | 38.5 ms                                                         | 27.1 ms: 1.42x faster                                                                |
| async_tree_memoization_tg  | 350 ms                                                          | 253 ms: 1.38x faster                                                                 |
| float                      | 76.7 ms                                                         | 56.0 ms: 1.37x faster                                                                |
| async_tree_none_tg         | 278 ms                                                          | 205 ms: 1.35x faster                                                                 |
| async_tree_memoization     | 364 ms                                                          | 269 ms: 1.35x faster                                                                 |
| async_tree_none            | 298 ms                                                          | 225 ms: 1.32x faster                                                                 |
| comprehensions             | 19.2 us                                                         | 14.6 us: 1.32x faster                                                                |
| regex_effbot               | 2.04 ms                                                         | 1.55 ms: 1.31x faster                                                                |
| logging_silent             | 101 ns                                                          | 77.5 ns: 1.30x faster                                                                |
| mako                       | 9.96 ms                                                         | 7.68 ms: 1.30x faster                                                                |
| go                         | 137 ms                                                          | 107 ms: 1.28x faster                                                                 |
| deltablue                  | 3.58 ms                                                         | 2.82 ms: 1.27x faster                                                                |
| hexiom                     | 6.82 ms                                                         | 5.43 ms: 1.26x faster                                                                |
| scimark_sor                | 130 ms                                                          | 104 ms: 1.25x faster                                                                 |
| tomli_loads                | 2.20 sec                                                        | 1.76 sec: 1.25x faster                                                               |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.11 ms: 1.24x faster                                                                |
| deepcopy_reduce            | 3.23 us                                                         | 2.60 us: 1.24x faster                                                                |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 441 ms: 1.24x faster                                                                 |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 460 ms: 1.23x faster                                                                 |
| scimark_monte_carlo        | 66.4 ms                                                         | 54.7 ms: 1.22x faster                                                                |
| pyflate                    | 424 ms                                                          | 354 ms: 1.20x faster                                                                 |
| nqueens                    | 93.7 ms                                                         | 78.4 ms: 1.19x faster                                                                |
| scimark_lu                 | 93.2 ms                                                         | 78.3 ms: 1.19x faster                                                                |
| chaos                      | 69.4 ms                                                         | 58.6 ms: 1.18x faster                                                                |
| regex_compile              | 129 ms                                                          | 110 ms: 1.18x faster                                                                 |
| coroutines                 | 20.9 ms                                                         | 17.8 ms: 1.18x faster                                                                |
| logging_simple             | 9.75 us                                                         | 8.43 us: 1.16x faster                                                                |
| xml_etree_iterparse        | 77.6 ms                                                         | 67.1 ms: 1.16x faster                                                                |
| scimark_fft                | 271 ms                                                          | 235 ms: 1.15x faster                                                                 |
| unpickle_pure_python       | 210 us                                                          | 183 us: 1.15x faster                                                                 |
| sqlglot_parse              | 1.25 ms                                                         | 1.09 ms: 1.14x faster                                                                |
| sqlglot_transpile          | 1.53 ms                                                         | 1.34 ms: 1.14x faster                                                                |
| logging_format             | 10.4 us                                                         | 9.15 us: 1.14x faster                                                                |
| fannkuch                   | 354 ms                                                          | 316 ms: 1.12x faster                                                                 |
| dulwich_log                | 58.5 ms                                                         | 52.3 ms: 1.12x faster                                                                |
| sympy_sum                  | 123 ms                                                          | 110 ms: 1.12x faster                                                                 |
| sympy_integrate            | 17.5 ms                                                         | 15.9 ms: 1.10x faster                                                                |
| regex_dna                  | 127 ms                                                          | 116 ms: 1.10x faster                                                                 |
| pycparser                  | 978 ms                                                          | 900 ms: 1.09x faster                                                                 |
| 2to3                       | 280 ms                                                          | 258 ms: 1.09x faster                                                                 |
| pprint_pformat             | 1.50 sec                                                        | 1.38 sec: 1.09x faster                                                               |
| mdp                        | 1.91 sec                                                        | 1.77 sec: 1.08x faster                                                               |
| sqlglot_optimize           | 48.5 ms                                                         | 45.0 ms: 1.08x faster                                                                |
| pprint_safe_repr           | 721 ms                                                          | 670 ms: 1.08x faster                                                                 |
| bench_thread_pool          | 1.10 ms                                                         | 1.03 ms: 1.07x faster                                                                |
| sqlite_synth               | 2.07 us                                                         | 1.93 us: 1.07x faster                                                                |
| meteor_contest             | 86.9 ms                                                         | 81.0 ms: 1.07x faster                                                                |
| raytrace                   | 308 ms                                                          | 287 ms: 1.07x faster                                                                 |
| sympy_str                  | 240 ms                                                          | 224 ms: 1.07x faster                                                                 |
| docutils                   | 1.98 sec                                                        | 1.86 sec: 1.07x faster                                                               |
| pathlib                    | 91.4 ms                                                         | 85.9 ms: 1.06x faster                                                                |
| crypto_pyaes               | 69.2 ms                                                         | 65.1 ms: 1.06x faster                                                                |
| django_template            | 36.9 ms                                                         | 35.1 ms: 1.05x faster                                                                |
| richards                   | 41.3 ms                                                         | 39.8 ms: 1.04x faster                                                                |
| xml_etree_process          | 53.2 ms                                                         | 51.7 ms: 1.03x faster                                                                |
| xml_etree_parse            | 113 ms                                                          | 110 ms: 1.03x faster                                                                 |
| richards_super             | 46.5 ms                                                         | 45.4 ms: 1.02x faster                                                                |
| xml_etree_generate         | 72.1 ms                                                         | 70.5 ms: 1.02x faster                                                                |
| async_generators           | 313 ms                                                          | 309 ms: 1.01x faster                                                                 |
| pickle_pure_python         | 286 us                                                          | 289 us: 1.01x slower                                                                 |
| pidigits                   | 199 ms                                                          | 202 ms: 1.01x slower                                                                 |
| regex_v8                   | 15.0 ms                                                         | 15.8 ms: 1.05x slower                                                                |
| python_startup_no_site     | 19.1 ms                                                         | 20.0 ms: 1.05x slower                                                                |
| coverage                   | 48.4 ms                                                         | 52.8 ms: 1.09x slower                                                                |
| json                       | 4.15 ms                                                         | 4.71 ms: 1.13x slower                                                                |
| json_loads                 | 20.4 us                                                         | 23.2 us: 1.14x slower                                                                |
| python_startup             | 22.4 ms                                                         | 26.7 ms: 1.20x slower                                                                |
| gc_traversal               | 1.44 ms                                                         | 1.78 ms: 1.24x slower                                                                |
| json_dumps                 | 7.40 ms                                                         | 9.24 ms: 1.25x slower                                                                |
| bench_mp_pool              | 75.4 ms                                                         | 94.2 ms: 1.25x slower                                                                |
| telco                      | 5.51 ms                                                         | 6.91 ms: 1.25x slower                                                                |
| typing_runtime_protocols   | 126 us                                                          | 164 us: 1.30x slower                                                                 |
| create_gc_cycles           | 652 us                                                          | 1.06 ms: 1.62x slower                                                                |
| sqlglot_normalize          | 100 ms                                                          | 232 ms: 2.32x slower                                                                 |
| Geometric mean             | (ref)                                                           | 1.11x faster                                                                         |

Benchmark hidden because not significant (1): sympy_expand
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250129-3.14.0a4+-620dde2/bm-20250129-pythonperf1_win32-x86-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.109x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: unknown