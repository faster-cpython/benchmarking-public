# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: macro_ify
- machine: windows-x86
- commit hash: 2302696
- commit date: 2024-07-02
- overall geometric mean: 1.15x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-pythonperf1_win32-x86-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 253 ms: 1.11x faster                                                          |
| docutils       | 1.98 sec                                                        | 1.89 sec: 1.05x faster                                                        |
| tornado_http   | 105 ms                                                          | 95.2 ms: 1.10x faster                                                         |
| Geometric mean | (ref)                                                           | 1.09x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-pythonperf1_win32-x86-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_none_tg         | 278 ms                                                          | 190 ms: 1.46x faster                                                          |
| async_tree_memoization_tg  | 350 ms                                                          | 242 ms: 1.45x faster                                                          |
| async_tree_io_tg           | 677 ms                                                          | 495 ms: 1.37x faster                                                          |
| async_tree_memoization     | 364 ms                                                          | 272 ms: 1.34x faster                                                          |
| async_tree_none            | 298 ms                                                          | 223 ms: 1.33x faster                                                          |
| async_tree_io              | 693 ms                                                          | 539 ms: 1.29x faster                                                          |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 470 ms: 1.20x faster                                                          |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 459 ms: 1.19x faster                                                          |
| Geometric mean             | (ref)                                                           | 1.33x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-pythonperf1_win32-x86-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 93.6 ms: 1.36x faster                                                         |
| float          | 76.7 ms                                                         | 60.9 ms: 1.26x faster                                                         |
| pidigits       | 199 ms                                                          | 196 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                           | 1.20x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-pythonperf1_win32-x86-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 106 ms: 1.22x faster                                                          |
| regex_effbot   | 2.04 ms                                                         | 1.92 ms: 1.06x faster                                                         |
| regex_dna      | 127 ms                                                          | 124 ms: 1.03x faster                                                          |
| regex_v8       | 15.0 ms                                                         | 16.3 ms: 1.08x slower                                                         |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-pythonperf1_win32-x86-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 171 us: 1.23x faster                                                          |
| tomli_loads          | 2.20 sec                                                        | 1.82 sec: 1.21x faster                                                        |
| pickle_pure_python   | 286 us                                                          | 245 us: 1.17x faster                                                          |
| xml_etree_iterparse  | 77.6 ms                                                         | 67.1 ms: 1.16x faster                                                         |
| xml_etree_process    | 53.2 ms                                                         | 48.6 ms: 1.09x faster                                                         |
| xml_etree_generate   | 72.1 ms                                                         | 66.0 ms: 1.09x faster                                                         |
| xml_etree_parse      | 113 ms                                                          | 106 ms: 1.06x faster                                                          |
| json_dumps           | 7.40 ms                                                         | 7.29 ms: 1.01x faster                                                         |
| json_loads           | 20.4 us                                                         | 20.5 us: 1.01x slower                                                         |
| Geometric mean       | (ref)                                                           | 1.11x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-pythonperf1_win32-x86-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 18.8 ms: 1.01x faster                                                         |
| python_startup         | 22.4 ms                                                         | 22.9 ms: 1.03x slower                                                         |
| Geometric mean         | (ref)                                                           | 1.01x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-pythonperf1_win32-x86-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|-----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 8.10 ms: 1.23x faster                                                         |
| django_template | 36.9 ms                                                         | 34.0 ms: 1.09x faster                                                         |
| Geometric mean  | (ref)                                                           | 1.15x faster                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-pythonperf1_win32-x86-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 21.6 us: 1.77x faster                                                         |
| async_tree_none_tg         | 278 ms                                                          | 190 ms: 1.46x faster                                                          |
| async_tree_memoization_tg  | 350 ms                                                          | 242 ms: 1.45x faster                                                          |
| deepcopy                   | 360 us                                                          | 249 us: 1.44x faster                                                          |
| generators                 | 38.5 ms                                                         | 27.3 ms: 1.41x faster                                                         |
| comprehensions             | 19.2 us                                                         | 14.0 us: 1.37x faster                                                         |
| async_tree_io_tg           | 677 ms                                                          | 495 ms: 1.37x faster                                                          |
| raytrace                   | 308 ms                                                          | 226 ms: 1.36x faster                                                          |
| deltablue                  | 3.58 ms                                                         | 2.64 ms: 1.36x faster                                                         |
| spectral_norm              | 104 ms                                                          | 76.4 ms: 1.36x faster                                                         |
| scimark_lu                 | 93.2 ms                                                         | 68.7 ms: 1.36x faster                                                         |
| nbody                      | 127 ms                                                          | 93.6 ms: 1.36x faster                                                         |
| logging_silent             | 101 ns                                                          | 75.1 ns: 1.35x faster                                                         |
| async_tree_memoization     | 364 ms                                                          | 272 ms: 1.34x faster                                                          |
| hexiom                     | 6.82 ms                                                         | 5.09 ms: 1.34x faster                                                         |
| scimark_sor                | 130 ms                                                          | 97.2 ms: 1.34x faster                                                         |
| async_tree_none            | 298 ms                                                          | 223 ms: 1.33x faster                                                          |
| chaos                      | 69.4 ms                                                         | 53.7 ms: 1.29x faster                                                         |
| async_tree_io              | 693 ms                                                          | 539 ms: 1.29x faster                                                          |
| float                      | 76.7 ms                                                         | 60.9 ms: 1.26x faster                                                         |
| deepcopy_reduce            | 3.23 us                                                         | 2.57 us: 1.26x faster                                                         |
| scimark_monte_carlo        | 66.4 ms                                                         | 53.1 ms: 1.25x faster                                                         |
| scimark_fft                | 271 ms                                                          | 217 ms: 1.25x faster                                                          |
| pyflate                    | 424 ms                                                          | 342 ms: 1.24x faster                                                          |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.12 ms: 1.24x faster                                                         |
| unpickle_pure_python       | 210 us                                                          | 171 us: 1.23x faster                                                          |
| mako                       | 9.96 ms                                                         | 8.10 ms: 1.23x faster                                                         |
| regex_compile              | 129 ms                                                          | 106 ms: 1.22x faster                                                          |
| logging_simple             | 9.75 us                                                         | 8.04 us: 1.21x faster                                                         |
| tomli_loads                | 2.20 sec                                                        | 1.82 sec: 1.21x faster                                                        |
| coroutines                 | 20.9 ms                                                         | 17.3 ms: 1.21x faster                                                         |
| nqueens                    | 93.7 ms                                                         | 77.8 ms: 1.20x faster                                                         |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 470 ms: 1.20x faster                                                          |
| go                         | 137 ms                                                          | 115 ms: 1.20x faster                                                          |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 459 ms: 1.19x faster                                                          |
| logging_format             | 10.4 us                                                         | 8.75 us: 1.19x faster                                                         |
| crypto_pyaes               | 69.2 ms                                                         | 58.2 ms: 1.19x faster                                                         |
| pycparser                  | 978 ms                                                          | 838 ms: 1.17x faster                                                          |
| pickle_pure_python         | 286 us                                                          | 245 us: 1.17x faster                                                          |
| richards                   | 41.3 ms                                                         | 35.4 ms: 1.17x faster                                                         |
| sqlglot_transpile          | 1.53 ms                                                         | 1.31 ms: 1.17x faster                                                         |
| sqlglot_parse              | 1.25 ms                                                         | 1.07 ms: 1.16x faster                                                         |
| richards_super             | 46.5 ms                                                         | 40.1 ms: 1.16x faster                                                         |
| xml_etree_iterparse        | 77.6 ms                                                         | 67.1 ms: 1.16x faster                                                         |
| mdp                        | 1.91 sec                                                        | 1.67 sec: 1.14x faster                                                        |
| sympy_integrate            | 17.5 ms                                                         | 15.4 ms: 1.14x faster                                                         |
| sympy_sum                  | 123 ms                                                          | 109 ms: 1.13x faster                                                          |
| bench_thread_pool          | 1.10 ms                                                         | 983 us: 1.12x faster                                                          |
| pprint_pformat             | 1.50 sec                                                        | 1.35 sec: 1.11x faster                                                        |
| 2to3                       | 280 ms                                                          | 253 ms: 1.11x faster                                                          |
| fannkuch                   | 354 ms                                                          | 320 ms: 1.10x faster                                                          |
| tornado_http               | 105 ms                                                          | 95.2 ms: 1.10x faster                                                         |
| pprint_safe_repr           | 721 ms                                                          | 653 ms: 1.10x faster                                                          |
| sqlglot_optimize           | 48.5 ms                                                         | 44.0 ms: 1.10x faster                                                         |
| sympy_str                  | 240 ms                                                          | 218 ms: 1.10x faster                                                          |
| xml_etree_process          | 53.2 ms                                                         | 48.6 ms: 1.09x faster                                                         |
| meteor_contest             | 86.9 ms                                                         | 79.4 ms: 1.09x faster                                                         |
| xml_etree_generate         | 72.1 ms                                                         | 66.0 ms: 1.09x faster                                                         |
| pathlib                    | 91.4 ms                                                         | 83.8 ms: 1.09x faster                                                         |
| django_template            | 36.9 ms                                                         | 34.0 ms: 1.09x faster                                                         |
| async_generators           | 313 ms                                                          | 292 ms: 1.07x faster                                                          |
| bench_mp_pool              | 75.4 ms                                                         | 70.5 ms: 1.07x faster                                                         |
| xml_etree_parse            | 113 ms                                                          | 106 ms: 1.06x faster                                                          |
| regex_effbot               | 2.04 ms                                                         | 1.92 ms: 1.06x faster                                                         |
| docutils                   | 1.98 sec                                                        | 1.89 sec: 1.05x faster                                                        |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 16.9 sec: 1.05x faster                                                        |
| sympy_expand               | 398 ms                                                          | 382 ms: 1.04x faster                                                          |
| regex_dna                  | 127 ms                                                          | 124 ms: 1.03x faster                                                          |
| pidigits                   | 199 ms                                                          | 196 ms: 1.01x faster                                                          |
| json_dumps                 | 7.40 ms                                                         | 7.29 ms: 1.01x faster                                                         |
| python_startup_no_site     | 19.1 ms                                                         | 18.8 ms: 1.01x faster                                                         |
| json_loads                 | 20.4 us                                                         | 20.5 us: 1.01x slower                                                         |
| json                       | 4.15 ms                                                         | 4.24 ms: 1.02x slower                                                         |
| python_startup             | 22.4 ms                                                         | 22.9 ms: 1.03x slower                                                         |
| coverage                   | 48.4 ms                                                         | 51.5 ms: 1.06x slower                                                         |
| regex_v8                   | 15.0 ms                                                         | 16.3 ms: 1.08x slower                                                         |
| telco                      | 5.51 ms                                                         | 6.23 ms: 1.13x slower                                                         |
| create_gc_cycles           | 652 us                                                          | 749 us: 1.15x slower                                                          |
| typing_runtime_protocols   | 126 us                                                          | 153 us: 1.21x slower                                                          |
| sqlglot_normalize          | 100 ms                                                          | 228 ms: 2.27x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.15x faster                                                                  |

Benchmark hidden because not significant (2): gc_traversal, asyncio_tcp
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240702-3.14.0a0-2302696/bm-20240702-pythonperf1_win32-x86-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown