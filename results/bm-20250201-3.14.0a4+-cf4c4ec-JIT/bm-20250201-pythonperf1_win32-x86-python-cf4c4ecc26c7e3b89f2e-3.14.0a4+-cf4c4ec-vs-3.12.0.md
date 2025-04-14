# Results vs. 3.12.0

- fork: python
- ref: cf4c4ecc26c7e3b89f2e
- machine: windows-x86
- commit hash: cf4c4ec
- commit date: 2025-02-01
- overall geometric mean: 1.050x faster
- HPT reliability: 98.60%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 272 ms: 1.03x faster                                                            |
| docutils       | 1.98 sec                                                        | 1.96 sec: 1.01x faster                                                          |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io              | 693 ms                                                          | 477 ms: 1.45x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 474 ms: 1.43x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 260 ms: 1.35x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 207 ms: 1.34x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 278 ms: 1.31x faster                                                            |
| async_tree_none            | 298 ms                                                          | 235 ms: 1.27x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 470 ms: 1.16x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 493 ms: 1.14x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.30x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 76.7 ms                                                         | 53.2 ms: 1.44x faster                                                           |
| nbody          | 127 ms                                                          | 110 ms: 1.16x faster                                                            |
| pidigits       | 199 ms                                                          | 202 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                           | 1.18x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.55 ms: 1.31x faster                                                           |
| regex_compile  | 129 ms                                                          | 119 ms: 1.08x faster                                                            |
| regex_dna      | 127 ms                                                          | 125 ms: 1.02x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 16.5 ms: 1.10x slower                                                           |
| Geometric mean | (ref)                                                           | 1.07x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.86 sec: 1.18x faster                                                          |
| xml_etree_iterparse  | 77.6 ms                                                         | 67.0 ms: 1.16x faster                                                           |
| pickle_dict          | 19.9 us                                                         | 18.6 us: 1.07x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 109 ms: 1.04x faster                                                            |
| pickle_list          | 3.37 us                                                         | 3.27 us: 1.03x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 54.6 ms: 1.03x slower                                                           |
| xml_etree_generate   | 72.1 ms                                                         | 74.3 ms: 1.03x slower                                                           |
| unpickle_pure_python | 210 us                                                          | 216 us: 1.03x slower                                                            |
| pickle_pure_python   | 286 us                                                          | 301 us: 1.05x slower                                                            |
| unpickle_list        | 2.95 us                                                         | 3.13 us: 1.06x slower                                                           |
| json_loads           | 20.4 us                                                         | 22.7 us: 1.12x slower                                                           |
| unpickle             | 9.71 us                                                         | 11.0 us: 1.13x slower                                                           |
| pickle               | 7.79 us                                                         | 9.22 us: 1.18x slower                                                           |
| json_dumps           | 7.40 ms                                                         | 9.76 ms: 1.32x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.03x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 22.1 ms: 1.16x slower                                                           |
| python_startup         | 22.4 ms                                                         | 28.8 ms: 1.29x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.22x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.64 ms: 1.30x faster                                                           |
| django_template | 36.9 ms                                                         | 38.1 ms: 1.03x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.12x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 25.4 us: 1.51x faster                                                           |
| async_tree_io              | 693 ms                                                          | 477 ms: 1.45x faster                                                            |
| float                      | 76.7 ms                                                         | 53.2 ms: 1.44x faster                                                           |
| spectral_norm              | 104 ms                                                          | 72.0 ms: 1.44x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 474 ms: 1.43x faster                                                            |
| unpack_sequence            | 62.5 ns                                                         | 44.6 ns: 1.40x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 66.8 ms: 1.37x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 260 ms: 1.35x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 207 ms: 1.34x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.55 ms: 1.31x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 278 ms: 1.31x faster                                                            |
| mako                       | 9.96 ms                                                         | 7.64 ms: 1.30x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 73.3 ms: 1.27x faster                                                           |
| async_tree_none            | 298 ms                                                          | 235 ms: 1.27x faster                                                            |
| scimark_sor                | 130 ms                                                          | 103 ms: 1.26x faster                                                            |
| deepcopy                   | 360 us                                                          | 287 us: 1.25x faster                                                            |
| logging_silent             | 101 ns                                                          | 81.6 ns: 1.24x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.16 ms: 1.22x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 17.2 ms: 1.22x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.86 sec: 1.18x faster                                                          |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 470 ms: 1.16x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 67.0 ms: 1.16x faster                                                           |
| nbody                      | 127 ms                                                          | 110 ms: 1.16x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 3.11 ms: 1.15x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 493 ms: 1.14x faster                                                            |
| logging_simple             | 9.75 us                                                         | 8.73 us: 1.12x faster                                                           |
| scimark_fft                | 271 ms                                                          | 244 ms: 1.11x faster                                                            |
| pyflate                    | 424 ms                                                          | 383 ms: 1.11x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 53.1 ms: 1.10x faster                                                           |
| logging_format             | 10.4 us                                                         | 9.51 us: 1.09x faster                                                           |
| sqlite_synth               | 2.07 us                                                         | 1.90 us: 1.09x faster                                                           |
| regex_compile              | 129 ms                                                          | 119 ms: 1.08x faster                                                            |
| go                         | 137 ms                                                          | 127 ms: 1.08x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 3.00 us: 1.07x faster                                                           |
| pickle_dict                | 19.9 us                                                         | 18.6 us: 1.07x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 117 ms: 1.05x faster                                                            |
| sqlglot_parse              | 1.25 ms                                                         | 1.20 ms: 1.04x faster                                                           |
| sqlglot_transpile          | 1.53 ms                                                         | 1.47 ms: 1.04x faster                                                           |
| chaos                      | 69.4 ms                                                         | 66.7 ms: 1.04x faster                                                           |
| xml_etree_parse            | 113 ms                                                          | 109 ms: 1.04x faster                                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 64.3 ms: 1.03x faster                                                           |
| comprehensions             | 19.2 us                                                         | 18.6 us: 1.03x faster                                                           |
| pickle_list                | 3.37 us                                                         | 3.27 us: 1.03x faster                                                           |
| 2to3                       | 280 ms                                                          | 272 ms: 1.03x faster                                                            |
| generators                 | 38.5 ms                                                         | 37.5 ms: 1.03x faster                                                           |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.2 sec: 1.03x faster                                                          |
| bench_thread_pool          | 1.10 ms                                                         | 1.08 ms: 1.03x faster                                                           |
| regex_dna                  | 127 ms                                                          | 125 ms: 1.02x faster                                                            |
| pycparser                  | 978 ms                                                          | 962 ms: 1.02x faster                                                            |
| docutils                   | 1.98 sec                                                        | 1.96 sec: 1.01x faster                                                          |
| sympy_str                  | 240 ms                                                          | 238 ms: 1.00x faster                                                            |
| pidigits                   | 199 ms                                                          | 202 ms: 1.01x slower                                                            |
| mdp                        | 1.91 sec                                                        | 1.93 sec: 1.01x slower                                                          |
| sympy_integrate            | 17.5 ms                                                         | 17.8 ms: 1.01x slower                                                           |
| richards_super             | 46.5 ms                                                         | 47.2 ms: 1.02x slower                                                           |
| richards                   | 41.3 ms                                                         | 42.3 ms: 1.02x slower                                                           |
| xml_etree_process          | 53.2 ms                                                         | 54.6 ms: 1.03x slower                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.54 sec: 1.03x slower                                                          |
| fannkuch                   | 354 ms                                                          | 364 ms: 1.03x slower                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 74.3 ms: 1.03x slower                                                           |
| unpickle_pure_python       | 210 us                                                          | 216 us: 1.03x slower                                                            |
| sympy_expand               | 398 ms                                                          | 411 ms: 1.03x slower                                                            |
| django_template            | 36.9 ms                                                         | 38.1 ms: 1.03x slower                                                           |
| raytrace                   | 308 ms                                                          | 318 ms: 1.03x slower                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 71.7 ms: 1.04x slower                                                           |
| async_generators           | 313 ms                                                          | 326 ms: 1.04x slower                                                            |
| pprint_safe_repr           | 721 ms                                                          | 752 ms: 1.04x slower                                                            |
| pickle_pure_python         | 286 us                                                          | 301 us: 1.05x slower                                                            |
| unpickle_list              | 2.95 us                                                         | 3.13 us: 1.06x slower                                                           |
| meteor_contest             | 86.9 ms                                                         | 92.6 ms: 1.07x slower                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 51.9 ms: 1.07x slower                                                           |
| hexiom                     | 6.82 ms                                                         | 7.37 ms: 1.08x slower                                                           |
| coverage                   | 48.4 ms                                                         | 52.8 ms: 1.09x slower                                                           |
| nqueens                    | 93.7 ms                                                         | 102 ms: 1.09x slower                                                            |
| regex_v8                   | 15.0 ms                                                         | 16.5 ms: 1.10x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 110 ms: 1.10x slower                                                            |
| json                       | 4.15 ms                                                         | 4.57 ms: 1.10x slower                                                           |
| json_loads                 | 20.4 us                                                         | 22.7 us: 1.12x slower                                                           |
| asyncio_tcp                | 662 ms                                                          | 741 ms: 1.12x slower                                                            |
| unpickle                   | 9.71 us                                                         | 11.0 us: 1.13x slower                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 22.1 ms: 1.16x slower                                                           |
| pickle                     | 7.79 us                                                         | 9.22 us: 1.18x slower                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 94.9 ms: 1.26x slower                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.85 ms: 1.29x slower                                                           |
| python_startup             | 22.4 ms                                                         | 28.8 ms: 1.29x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 166 us: 1.32x slower                                                            |
| json_dumps                 | 7.40 ms                                                         | 9.76 ms: 1.32x slower                                                           |
| telco                      | 5.51 ms                                                         | 7.91 ms: 1.44x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 1.05 ms: 1.62x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.04x faster                                                                    |
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (13) of results/bm-20250201-3.14.0a4+-cf4c4ec-JIT/bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.050x faster

# HPT report

- Reliability score: 98.60% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown