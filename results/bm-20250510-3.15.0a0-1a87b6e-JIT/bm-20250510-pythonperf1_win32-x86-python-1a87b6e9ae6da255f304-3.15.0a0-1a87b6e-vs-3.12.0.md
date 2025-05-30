# Results vs. 3.12.0

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: windows-x86
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.090x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 285 ms: 1.02x slower                                                           |
| docutils       | 1.98 sec                                                        | 1.97 sec: 1.01x faster                                                         |
| Geometric mean | (ref)                                                           | 1.00x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io              | 693 ms                                                          | 469 ms: 1.48x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 467 ms: 1.45x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 244 ms: 1.43x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 258 ms: 1.41x faster                                                           |
| async_tree_none            | 298 ms                                                          | 215 ms: 1.38x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 202 ms: 1.38x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 470 ms: 1.20x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 455 ms: 1.20x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.36x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 76.7 ms                                                         | 56.9 ms: 1.35x faster                                                          |
| nbody          | 127 ms                                                          | 119 ms: 1.06x faster                                                           |
| pidigits       | 199 ms                                                          | 204 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                           | 1.12x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.73 ms: 1.18x faster                                                          |
| regex_compile  | 129 ms                                                          | 111 ms: 1.16x faster                                                           |
| regex_dna      | 127 ms                                                          | 122 ms: 1.04x faster                                                           |
| regex_v8       | 15.0 ms                                                         | 14.9 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                           | 1.09x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.81 sec: 1.21x faster                                                         |
| xml_etree_iterparse  | 77.6 ms                                                         | 69.6 ms: 1.12x faster                                                          |
| xml_etree_generate   | 72.1 ms                                                         | 74.3 ms: 1.03x slower                                                          |
| xml_etree_process    | 53.2 ms                                                         | 55.9 ms: 1.05x slower                                                          |
| unpickle_list        | 2.95 us                                                         | 3.10 us: 1.05x slower                                                          |
| unpickle             | 9.71 us                                                         | 10.3 us: 1.07x slower                                                          |
| pickle_dict          | 19.9 us                                                         | 21.4 us: 1.07x slower                                                          |
| json_loads           | 20.4 us                                                         | 22.4 us: 1.10x slower                                                          |
| pickle_pure_python   | 286 us                                                          | 321 us: 1.12x slower                                                           |
| json_dumps           | 7.40 ms                                                         | 8.36 ms: 1.13x slower                                                          |
| pickle_list          | 3.37 us                                                         | 3.85 us: 1.14x slower                                                          |
| unpickle_pure_python | 210 us                                                          | 241 us: 1.15x slower                                                           |
| pickle               | 7.79 us                                                         | 9.34 us: 1.20x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.05x slower                                                                   |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 22.2 ms: 1.16x slower                                                          |
| python_startup         | 22.4 ms                                                         | 28.9 ms: 1.29x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.23x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 8.30 ms: 1.20x faster                                                          |
| django_template | 36.9 ms                                                         | 33.3 ms: 1.11x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.15x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pathlib                    | 91.4 ms                                                         | 37.2 ms: 2.46x faster                                                          |
| mdp                        | 1.91 sec                                                        | 1.07 sec: 1.79x faster                                                         |
| deepcopy_memo              | 38.4 us                                                         | 22.6 us: 1.70x faster                                                          |
| async_tree_io              | 693 ms                                                          | 469 ms: 1.48x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 467 ms: 1.45x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 244 ms: 1.43x faster                                                           |
| deepcopy                   | 360 us                                                          | 254 us: 1.42x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 258 ms: 1.41x faster                                                           |
| async_tree_none            | 298 ms                                                          | 215 ms: 1.38x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 202 ms: 1.38x faster                                                           |
| float                      | 76.7 ms                                                         | 56.9 ms: 1.35x faster                                                          |
| generators                 | 38.5 ms                                                         | 28.8 ms: 1.34x faster                                                          |
| spectral_norm              | 104 ms                                                          | 80.9 ms: 1.28x faster                                                          |
| raytrace                   | 308 ms                                                          | 246 ms: 1.25x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.59 us: 1.24x faster                                                          |
| go                         | 137 ms                                                          | 111 ms: 1.24x faster                                                           |
| scimark_sor                | 130 ms                                                          | 105 ms: 1.24x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.90 ms: 1.23x faster                                                          |
| chaos                      | 69.4 ms                                                         | 56.2 ms: 1.23x faster                                                          |
| tomli_loads                | 2.20 sec                                                        | 1.81 sec: 1.21x faster                                                         |
| scimark_monte_carlo        | 66.4 ms                                                         | 55.0 ms: 1.21x faster                                                          |
| pyflate                    | 424 ms                                                          | 353 ms: 1.20x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 470 ms: 1.20x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 455 ms: 1.20x faster                                                           |
| mako                       | 9.96 ms                                                         | 8.30 ms: 1.20x faster                                                          |
| scimark_lu                 | 93.2 ms                                                         | 78.7 ms: 1.18x faster                                                          |
| regex_effbot               | 2.04 ms                                                         | 1.73 ms: 1.18x faster                                                          |
| hexiom                     | 6.82 ms                                                         | 5.86 ms: 1.16x faster                                                          |
| regex_compile              | 129 ms                                                          | 111 ms: 1.16x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 18.2 ms: 1.15x faster                                                          |
| dulwich_log                | 58.5 ms                                                         | 51.7 ms: 1.13x faster                                                          |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.44 ms: 1.12x faster                                                          |
| xml_etree_iterparse        | 77.6 ms                                                         | 69.6 ms: 1.12x faster                                                          |
| sympy_sum                  | 123 ms                                                          | 111 ms: 1.11x faster                                                           |
| django_template            | 36.9 ms                                                         | 33.3 ms: 1.11x faster                                                          |
| sympy_integrate            | 17.5 ms                                                         | 16.0 ms: 1.10x faster                                                          |
| unpack_sequence            | 62.5 ns                                                         | 57.0 ns: 1.10x faster                                                          |
| logging_simple             | 9.75 us                                                         | 9.00 us: 1.08x faster                                                          |
| logging_format             | 10.4 us                                                         | 9.67 us: 1.08x faster                                                          |
| sympy_str                  | 240 ms                                                          | 224 ms: 1.07x faster                                                           |
| nbody                      | 127 ms                                                          | 119 ms: 1.06x faster                                                           |
| comprehensions             | 19.2 us                                                         | 18.1 us: 1.06x faster                                                          |
| sqlite_synth               | 2.07 us                                                         | 1.96 us: 1.06x faster                                                          |
| regex_dna                  | 127 ms                                                          | 122 ms: 1.04x faster                                                           |
| richards                   | 41.3 ms                                                         | 40.1 ms: 1.03x faster                                                          |
| nqueens                    | 93.7 ms                                                         | 91.7 ms: 1.02x faster                                                          |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.4 sec: 1.01x faster                                                         |
| scimark_fft                | 271 ms                                                          | 268 ms: 1.01x faster                                                           |
| richards_super             | 46.5 ms                                                         | 46.0 ms: 1.01x faster                                                          |
| docutils                   | 1.98 sec                                                        | 1.97 sec: 1.01x faster                                                         |
| pycparser                  | 978 ms                                                          | 971 ms: 1.01x faster                                                           |
| regex_v8                   | 15.0 ms                                                         | 14.9 ms: 1.01x faster                                                          |
| sympy_expand               | 398 ms                                                          | 396 ms: 1.00x faster                                                           |
| 2to3                       | 280 ms                                                          | 285 ms: 1.02x slower                                                           |
| pidigits                   | 199 ms                                                          | 204 ms: 1.02x slower                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 74.3 ms: 1.03x slower                                                          |
| async_generators           | 313 ms                                                          | 324 ms: 1.03x slower                                                           |
| xml_etree_process          | 53.2 ms                                                         | 55.9 ms: 1.05x slower                                                          |
| unpickle_list              | 2.95 us                                                         | 3.10 us: 1.05x slower                                                          |
| unpickle                   | 9.71 us                                                         | 10.3 us: 1.07x slower                                                          |
| pickle_dict                | 19.9 us                                                         | 21.4 us: 1.07x slower                                                          |
| json                       | 4.15 ms                                                         | 4.50 ms: 1.08x slower                                                          |
| pprint_pformat             | 1.50 sec                                                        | 1.63 sec: 1.09x slower                                                         |
| meteor_contest             | 86.9 ms                                                         | 94.5 ms: 1.09x slower                                                          |
| json_loads                 | 20.4 us                                                         | 22.4 us: 1.10x slower                                                          |
| pprint_safe_repr           | 721 ms                                                          | 799 ms: 1.11x slower                                                           |
| pickle_pure_python         | 286 us                                                          | 321 us: 1.12x slower                                                           |
| fannkuch                   | 354 ms                                                          | 400 ms: 1.13x slower                                                           |
| json_dumps                 | 7.40 ms                                                         | 8.36 ms: 1.13x slower                                                          |
| pickle_list                | 3.37 us                                                         | 3.85 us: 1.14x slower                                                          |
| unpickle_pure_python       | 210 us                                                          | 241 us: 1.15x slower                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 22.2 ms: 1.16x slower                                                          |
| coverage                   | 48.4 ms                                                         | 56.7 ms: 1.17x slower                                                          |
| crypto_pyaes               | 69.2 ms                                                         | 81.2 ms: 1.17x slower                                                          |
| pickle                     | 7.79 us                                                         | 9.34 us: 1.20x slower                                                          |
| bench_thread_pool          | 1.10 ms                                                         | 1.34 ms: 1.22x slower                                                          |
| python_startup             | 22.4 ms                                                         | 28.9 ms: 1.29x slower                                                          |
| telco                      | 5.51 ms                                                         | 7.28 ms: 1.32x slower                                                          |
| gc_traversal               | 1.44 ms                                                         | 1.94 ms: 1.34x slower                                                          |
| bench_mp_pool              | 75.4 ms                                                         | 104 ms: 1.38x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 177 us: 1.40x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 1.13 ms: 1.74x slower                                                          |
| logging_silent             | 101 ns                                                          | 375 ns: 3.71x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.05x faster                                                                   |

Benchmark hidden because not significant (2): xml_etree_parse, asyncio_tcp
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250510-3.15.0a0-1a87b6e-JIT/bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.090x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown