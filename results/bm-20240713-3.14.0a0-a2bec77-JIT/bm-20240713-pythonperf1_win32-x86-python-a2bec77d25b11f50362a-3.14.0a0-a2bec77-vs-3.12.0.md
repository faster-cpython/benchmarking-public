# Results vs. 3.12.0

- fork: python
- ref: a2bec77d25b11f50362a
- machine: windows-x86
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.23x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 253 ms: 1.11x faster                                                           |
| docutils       | 1.98 sec                                                        | 1.93 sec: 1.03x faster                                                         |
| tornado_http   | 105 ms                                                          | 97.5 ms: 1.08x faster                                                          |
| Geometric mean | (ref)                                                           | 1.07x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none_tg         | 278 ms                                                          | 196 ms: 1.42x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 249 ms: 1.41x faster                                                           |
| async_tree_none            | 298 ms                                                          | 220 ms: 1.35x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 501 ms: 1.35x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 272 ms: 1.34x faster                                                           |
| async_tree_io              | 693 ms                                                          | 538 ms: 1.29x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 468 ms: 1.20x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 458 ms: 1.19x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.32x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 54.7 ms: 2.32x faster                                                          |
| float          | 76.7 ms                                                         | 43.9 ms: 1.75x faster                                                          |
| pidigits       | 199 ms                                                          | 195 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                           | 1.61x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 95.3 ms: 1.35x faster                                                          |
| regex_dna      | 127 ms                                                          | 123 ms: 1.03x faster                                                           |
| regex_effbot   | 2.04 ms                                                         | 1.99 ms: 1.02x faster                                                          |
| regex_v8       | 15.0 ms                                                         | 16.0 ms: 1.06x slower                                                          |
| Geometric mean | (ref)                                                           | 1.08x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.53 sec: 1.44x faster                                                         |
| unpickle_pure_python | 210 us                                                          | 147 us: 1.42x faster                                                           |
| pickle_pure_python   | 286 us                                                          | 209 us: 1.37x faster                                                           |
| xml_etree_iterparse  | 77.6 ms                                                         | 61.9 ms: 1.25x faster                                                          |
| xml_etree_generate   | 72.1 ms                                                         | 61.4 ms: 1.17x faster                                                          |
| xml_etree_process    | 53.2 ms                                                         | 46.5 ms: 1.14x faster                                                          |
| xml_etree_parse      | 113 ms                                                          | 104 ms: 1.09x faster                                                           |
| json_dumps           | 7.40 ms                                                         | 7.15 ms: 1.03x faster                                                          |
| json_loads           | 20.4 us                                                         | 21.0 us: 1.03x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.20x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup | 22.4 ms                                                         | 23.1 ms: 1.03x slower                                                          |
| Geometric mean | (ref)                                                           | 1.02x slower                                                                   |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.44 ms: 1.83x faster                                                          |
| django_template | 36.9 ms                                                         | 33.3 ms: 1.11x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.43x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 15.3 us: 2.51x faster                                                          |
| nbody                      | 127 ms                                                          | 54.7 ms: 2.32x faster                                                          |
| spectral_norm              | 104 ms                                                          | 47.2 ms: 2.20x faster                                                          |
| mako                       | 9.96 ms                                                         | 5.44 ms: 1.83x faster                                                          |
| float                      | 76.7 ms                                                         | 43.9 ms: 1.75x faster                                                          |
| logging_silent             | 101 ns                                                          | 58.4 ns: 1.73x faster                                                          |
| comprehensions             | 19.2 us                                                         | 11.5 us: 1.67x faster                                                          |
| scimark_fft                | 271 ms                                                          | 166 ms: 1.63x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.38 ms: 1.62x faster                                                          |
| scimark_monte_carlo        | 66.4 ms                                                         | 42.3 ms: 1.57x faster                                                          |
| pyflate                    | 424 ms                                                          | 277 ms: 1.53x faster                                                           |
| deepcopy                   | 360 us                                                          | 237 us: 1.52x faster                                                           |
| fannkuch                   | 354 ms                                                          | 236 ms: 1.50x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 4.70 ms: 1.45x faster                                                          |
| crypto_pyaes               | 69.2 ms                                                         | 48.0 ms: 1.44x faster                                                          |
| tomli_loads                | 2.20 sec                                                        | 1.53 sec: 1.44x faster                                                         |
| unpickle_pure_python       | 210 us                                                          | 147 us: 1.42x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 196 ms: 1.42x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 249 ms: 1.41x faster                                                           |
| generators                 | 38.5 ms                                                         | 27.6 ms: 1.40x faster                                                          |
| pickle_pure_python         | 286 us                                                          | 209 us: 1.37x faster                                                           |
| regex_compile              | 129 ms                                                          | 95.3 ms: 1.35x faster                                                          |
| async_tree_none            | 298 ms                                                          | 220 ms: 1.35x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 501 ms: 1.35x faster                                                           |
| raytrace                   | 308 ms                                                          | 229 ms: 1.35x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.41 us: 1.34x faster                                                          |
| async_tree_memoization     | 364 ms                                                          | 272 ms: 1.34x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.69 ms: 1.33x faster                                                          |
| chaos                      | 69.4 ms                                                         | 52.3 ms: 1.33x faster                                                          |
| sqlglot_parse              | 1.25 ms                                                         | 956 us: 1.30x faster                                                           |
| logging_simple             | 9.75 us                                                         | 7.56 us: 1.29x faster                                                          |
| pprint_pformat             | 1.50 sec                                                        | 1.16 sec: 1.29x faster                                                         |
| async_tree_io              | 693 ms                                                          | 538 ms: 1.29x faster                                                           |
| nqueens                    | 93.7 ms                                                         | 73.3 ms: 1.28x faster                                                          |
| pprint_safe_repr           | 721 ms                                                          | 565 ms: 1.27x faster                                                           |
| logging_format             | 10.4 us                                                         | 8.21 us: 1.27x faster                                                          |
| xml_etree_iterparse        | 77.6 ms                                                         | 61.9 ms: 1.25x faster                                                          |
| sqlglot_transpile          | 1.53 ms                                                         | 1.22 ms: 1.25x faster                                                          |
| scimark_sor                | 130 ms                                                          | 104 ms: 1.25x faster                                                           |
| richards                   | 41.3 ms                                                         | 33.7 ms: 1.23x faster                                                          |
| go                         | 137 ms                                                          | 113 ms: 1.21x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 468 ms: 1.20x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 458 ms: 1.19x faster                                                           |
| richards_super             | 46.5 ms                                                         | 39.1 ms: 1.19x faster                                                          |
| xml_etree_generate         | 72.1 ms                                                         | 61.4 ms: 1.17x faster                                                          |
| coroutines                 | 20.9 ms                                                         | 18.0 ms: 1.16x faster                                                          |
| pycparser                  | 978 ms                                                          | 845 ms: 1.16x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 75.1 ms: 1.16x faster                                                          |
| xml_etree_process          | 53.2 ms                                                         | 46.5 ms: 1.14x faster                                                          |
| mdp                        | 1.91 sec                                                        | 1.68 sec: 1.14x faster                                                         |
| scimark_lu                 | 93.2 ms                                                         | 82.6 ms: 1.13x faster                                                          |
| bench_thread_pool          | 1.10 ms                                                         | 983 us: 1.12x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 82.0 ms: 1.11x faster                                                          |
| django_template            | 36.9 ms                                                         | 33.3 ms: 1.11x faster                                                          |
| sympy_sum                  | 123 ms                                                          | 111 ms: 1.11x faster                                                           |
| 2to3                       | 280 ms                                                          | 253 ms: 1.11x faster                                                           |
| sympy_integrate            | 17.5 ms                                                         | 16.0 ms: 1.10x faster                                                          |
| sqlglot_optimize           | 48.5 ms                                                         | 44.4 ms: 1.09x faster                                                          |
| xml_etree_parse            | 113 ms                                                          | 104 ms: 1.09x faster                                                           |
| sympy_str                  | 240 ms                                                          | 220 ms: 1.09x faster                                                           |
| tornado_http               | 105 ms                                                          | 97.5 ms: 1.08x faster                                                          |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 16.9 sec: 1.04x faster                                                         |
| telco                      | 5.51 ms                                                         | 5.31 ms: 1.04x faster                                                          |
| json_dumps                 | 7.40 ms                                                         | 7.15 ms: 1.03x faster                                                          |
| docutils                   | 1.98 sec                                                        | 1.93 sec: 1.03x faster                                                         |
| regex_dna                  | 127 ms                                                          | 123 ms: 1.03x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.99 ms: 1.02x faster                                                          |
| bench_mp_pool              | 75.4 ms                                                         | 73.7 ms: 1.02x faster                                                          |
| async_generators           | 313 ms                                                          | 307 ms: 1.02x faster                                                           |
| pidigits                   | 199 ms                                                          | 195 ms: 1.02x faster                                                           |
| sympy_expand               | 398 ms                                                          | 393 ms: 1.01x faster                                                           |
| json                       | 4.15 ms                                                         | 4.20 ms: 1.01x slower                                                          |
| json_loads                 | 20.4 us                                                         | 21.0 us: 1.03x slower                                                          |
| python_startup             | 22.4 ms                                                         | 23.1 ms: 1.03x slower                                                          |
| regex_v8                   | 15.0 ms                                                         | 16.0 ms: 1.06x slower                                                          |
| coverage                   | 48.4 ms                                                         | 52.0 ms: 1.07x slower                                                          |
| create_gc_cycles           | 652 us                                                          | 757 us: 1.16x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 153 us: 1.21x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 241 ms: 2.41x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.23x faster                                                                   |

Benchmark hidden because not significant (3): gc_traversal, python_startup_no_site, asyncio_tcp
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240713-3.14.0a0-a2bec77-JIT/bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: unknown