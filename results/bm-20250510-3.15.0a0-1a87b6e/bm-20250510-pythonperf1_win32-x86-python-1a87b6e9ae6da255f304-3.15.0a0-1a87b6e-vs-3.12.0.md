# Results vs. 3.12.0

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: windows-x86
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.166x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 268 ms: 1.04x faster                                                           |
| docutils       | 1.98 sec                                                        | 1.86 sec: 1.07x faster                                                         |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io              | 693 ms                                                          | 447 ms: 1.55x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 445 ms: 1.52x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 234 ms: 1.50x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 247 ms: 1.47x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 189 ms: 1.47x faster                                                           |
| async_tree_none            | 298 ms                                                          | 202 ms: 1.47x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 450 ms: 1.25x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 441 ms: 1.24x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.43x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 76.7 ms                                                         | 53.8 ms: 1.43x faster                                                          |
| nbody          | 127 ms                                                          | 93.6 ms: 1.36x faster                                                          |
| pidigits       | 199 ms                                                          | 205 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                           | 1.23x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 103 ms: 1.25x faster                                                           |
| regex_effbot   | 2.04 ms                                                         | 1.65 ms: 1.23x faster                                                          |
| regex_dna      | 127 ms                                                          | 120 ms: 1.06x faster                                                           |
| regex_v8       | 15.0 ms                                                         | 14.6 ms: 1.03x faster                                                          |
| Geometric mean | (ref)                                                           | 1.14x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.74 sec: 1.26x faster                                                         |
| unpickle_pure_python | 210 us                                                          | 176 us: 1.19x faster                                                           |
| xml_etree_iterparse  | 77.6 ms                                                         | 67.0 ms: 1.16x faster                                                          |
| xml_etree_process    | 53.2 ms                                                         | 50.0 ms: 1.06x faster                                                          |
| xml_etree_generate   | 72.1 ms                                                         | 68.3 ms: 1.06x faster                                                          |
| pickle_pure_python   | 286 us                                                          | 272 us: 1.05x faster                                                           |
| unpickle_list        | 2.95 us                                                         | 3.02 us: 1.03x slower                                                          |
| json_loads           | 20.4 us                                                         | 22.0 us: 1.08x slower                                                          |
| pickle_dict          | 19.9 us                                                         | 21.6 us: 1.08x slower                                                          |
| pickle_list          | 3.37 us                                                         | 3.80 us: 1.13x slower                                                          |
| unpickle             | 9.71 us                                                         | 11.0 us: 1.13x slower                                                          |
| json_dumps           | 7.40 ms                                                         | 8.43 ms: 1.14x slower                                                          |
| pickle               | 7.79 us                                                         | 9.13 us: 1.17x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.00x faster                                                                   |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 22.2 ms: 1.16x slower                                                          |
| python_startup         | 22.4 ms                                                         | 29.3 ms: 1.31x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.23x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 8.14 ms: 1.22x faster                                                          |
| django_template | 36.9 ms                                                         | 33.9 ms: 1.09x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.15x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pathlib                    | 91.4 ms                                                         | 37.6 ms: 2.43x faster                                                          |
| mdp                        | 1.91 sec                                                        | 1.02 sec: 1.87x faster                                                         |
| deepcopy_memo              | 38.4 us                                                         | 20.6 us: 1.87x faster                                                          |
| async_tree_io              | 693 ms                                                          | 447 ms: 1.55x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 445 ms: 1.52x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 234 ms: 1.50x faster                                                           |
| unpack_sequence            | 62.5 ns                                                         | 41.7 ns: 1.50x faster                                                          |
| deepcopy                   | 360 us                                                          | 243 us: 1.48x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 247 ms: 1.47x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 189 ms: 1.47x faster                                                           |
| async_tree_none            | 298 ms                                                          | 202 ms: 1.47x faster                                                           |
| generators                 | 38.5 ms                                                         | 26.5 ms: 1.45x faster                                                          |
| float                      | 76.7 ms                                                         | 53.8 ms: 1.43x faster                                                          |
| deltablue                  | 3.58 ms                                                         | 2.55 ms: 1.41x faster                                                          |
| scimark_sor                | 130 ms                                                          | 94.7 ms: 1.37x faster                                                          |
| nbody                      | 127 ms                                                          | 93.6 ms: 1.36x faster                                                          |
| hexiom                     | 6.82 ms                                                         | 5.04 ms: 1.35x faster                                                          |
| spectral_norm              | 104 ms                                                          | 77.4 ms: 1.34x faster                                                          |
| go                         | 137 ms                                                          | 103 ms: 1.33x faster                                                           |
| comprehensions             | 19.2 us                                                         | 14.8 us: 1.30x faster                                                          |
| scimark_lu                 | 93.2 ms                                                         | 72.1 ms: 1.29x faster                                                          |
| scimark_monte_carlo        | 66.4 ms                                                         | 51.6 ms: 1.29x faster                                                          |
| chaos                      | 69.4 ms                                                         | 54.6 ms: 1.27x faster                                                          |
| coroutines                 | 20.9 ms                                                         | 16.5 ms: 1.26x faster                                                          |
| tomli_loads                | 2.20 sec                                                        | 1.74 sec: 1.26x faster                                                         |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 450 ms: 1.25x faster                                                           |
| raytrace                   | 308 ms                                                          | 246 ms: 1.25x faster                                                           |
| regex_compile              | 129 ms                                                          | 103 ms: 1.25x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.60 us: 1.24x faster                                                          |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 441 ms: 1.24x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.65 ms: 1.23x faster                                                          |
| mako                       | 9.96 ms                                                         | 8.14 ms: 1.22x faster                                                          |
| pyflate                    | 424 ms                                                          | 347 ms: 1.22x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 176 us: 1.19x faster                                                           |
| sympy_integrate            | 17.5 ms                                                         | 15.0 ms: 1.17x faster                                                          |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.31 ms: 1.17x faster                                                          |
| xml_etree_iterparse        | 77.6 ms                                                         | 67.0 ms: 1.16x faster                                                          |
| scimark_fft                | 271 ms                                                          | 234 ms: 1.16x faster                                                           |
| dulwich_log                | 58.5 ms                                                         | 51.4 ms: 1.14x faster                                                          |
| richards                   | 41.3 ms                                                         | 36.4 ms: 1.14x faster                                                          |
| sympy_sum                  | 123 ms                                                          | 109 ms: 1.13x faster                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.33 sec: 1.12x faster                                                         |
| nqueens                    | 93.7 ms                                                         | 83.8 ms: 1.12x faster                                                          |
| richards_super             | 46.5 ms                                                         | 41.7 ms: 1.11x faster                                                          |
| pprint_safe_repr           | 721 ms                                                          | 650 ms: 1.11x faster                                                           |
| sympy_str                  | 240 ms                                                          | 217 ms: 1.11x faster                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 62.7 ms: 1.10x faster                                                          |
| django_template            | 36.9 ms                                                         | 33.9 ms: 1.09x faster                                                          |
| meteor_contest             | 86.9 ms                                                         | 80.1 ms: 1.08x faster                                                          |
| fannkuch                   | 354 ms                                                          | 327 ms: 1.08x faster                                                           |
| logging_simple             | 9.75 us                                                         | 9.03 us: 1.08x faster                                                          |
| pycparser                  | 978 ms                                                          | 906 ms: 1.08x faster                                                           |
| logging_format             | 10.4 us                                                         | 9.76 us: 1.07x faster                                                          |
| docutils                   | 1.98 sec                                                        | 1.86 sec: 1.07x faster                                                         |
| xml_etree_process          | 53.2 ms                                                         | 50.0 ms: 1.06x faster                                                          |
| regex_dna                  | 127 ms                                                          | 120 ms: 1.06x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 68.3 ms: 1.06x faster                                                          |
| pickle_pure_python         | 286 us                                                          | 272 us: 1.05x faster                                                           |
| async_generators           | 313 ms                                                          | 299 ms: 1.05x faster                                                           |
| 2to3                       | 280 ms                                                          | 268 ms: 1.04x faster                                                           |
| sqlite_synth               | 2.07 us                                                         | 2.00 us: 1.04x faster                                                          |
| sympy_expand               | 398 ms                                                          | 384 ms: 1.04x faster                                                           |
| regex_v8                   | 15.0 ms                                                         | 14.6 ms: 1.03x faster                                                          |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.5 sec: 1.01x faster                                                         |
| unpickle_list              | 2.95 us                                                         | 3.02 us: 1.03x slower                                                          |
| pidigits                   | 199 ms                                                          | 205 ms: 1.03x slower                                                           |
| json_loads                 | 20.4 us                                                         | 22.0 us: 1.08x slower                                                          |
| pickle_dict                | 19.9 us                                                         | 21.6 us: 1.08x slower                                                          |
| json                       | 4.15 ms                                                         | 4.51 ms: 1.09x slower                                                          |
| pickle_list                | 3.37 us                                                         | 3.80 us: 1.13x slower                                                          |
| unpickle                   | 9.71 us                                                         | 11.0 us: 1.13x slower                                                          |
| json_dumps                 | 7.40 ms                                                         | 8.43 ms: 1.14x slower                                                          |
| python_startup_no_site     | 19.1 ms                                                         | 22.2 ms: 1.16x slower                                                          |
| pickle                     | 7.79 us                                                         | 9.13 us: 1.17x slower                                                          |
| bench_thread_pool          | 1.10 ms                                                         | 1.33 ms: 1.20x slower                                                          |
| coverage                   | 48.4 ms                                                         | 58.8 ms: 1.21x slower                                                          |
| typing_runtime_protocols   | 126 us                                                          | 154 us: 1.22x slower                                                           |
| telco                      | 5.51 ms                                                         | 6.70 ms: 1.22x slower                                                          |
| python_startup             | 22.4 ms                                                         | 29.3 ms: 1.31x slower                                                          |
| gc_traversal               | 1.44 ms                                                         | 1.91 ms: 1.32x slower                                                          |
| bench_mp_pool              | 75.4 ms                                                         | 104 ms: 1.38x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 1.14 ms: 1.75x slower                                                          |
| logging_silent             | 101 ns                                                          | 345 ns: 3.41x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.12x faster                                                                   |

Benchmark hidden because not significant (2): xml_etree_parse, asyncio_tcp
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.166x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: unknown