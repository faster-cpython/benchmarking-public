# Results vs. 3.12.0

- fork: python
- ref: d27a53fc02a87e76066f
- machine: windows-x86
- commit hash: d27a53f
- commit date: 2024-07-30
- overall geometric mean: 1.16x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 251 ms: 1.12x faster                                                           |
| docutils       | 1.98 sec                                                        | 1.91 sec: 1.04x faster                                                         |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 246 ms: 1.43x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 195 ms: 1.43x faster                                                           |
| async_tree_none            | 298 ms                                                          | 224 ms: 1.33x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 511 ms: 1.32x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 276 ms: 1.32x faster                                                           |
| async_tree_io              | 693 ms                                                          | 549 ms: 1.26x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 467 ms: 1.21x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 454 ms: 1.20x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.31x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 88.5 ms: 1.43x faster                                                          |
| float          | 76.7 ms                                                         | 58.2 ms: 1.32x faster                                                          |
| pidigits       | 199 ms                                                          | 199 ms: 1.00x faster                                                           |
| Geometric mean | (ref)                                                           | 1.24x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 103 ms: 1.25x faster                                                           |
| regex_effbot   | 2.04 ms                                                         | 1.91 ms: 1.06x faster                                                          |
| regex_dna      | 127 ms                                                          | 122 ms: 1.04x faster                                                           |
| regex_v8       | 15.0 ms                                                         | 16.3 ms: 1.08x slower                                                          |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 169 us: 1.24x faster                                                           |
| tomli_loads          | 2.20 sec                                                        | 1.82 sec: 1.21x faster                                                         |
| pickle_pure_python   | 286 us                                                          | 244 us: 1.17x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 47.3 ms: 1.13x faster                                                          |
| xml_etree_iterparse  | 77.6 ms                                                         | 69.2 ms: 1.12x faster                                                          |
| xml_etree_generate   | 72.1 ms                                                         | 66.8 ms: 1.08x faster                                                          |
| xml_etree_parse      | 113 ms                                                          | 107 ms: 1.06x faster                                                           |
| json_loads           | 20.4 us                                                         | 20.0 us: 1.02x faster                                                          |
| json_dumps           | 7.40 ms                                                         | 7.53 ms: 1.02x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.11x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.7 ms: 1.03x slower                                                          |
| python_startup         | 22.4 ms                                                         | 23.7 ms: 1.06x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.05x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 8.01 ms: 1.24x faster                                                          |
| django_template | 36.9 ms                                                         | 34.7 ms: 1.06x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.15x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 21.1 us: 1.82x faster                                                          |
| generators                 | 38.5 ms                                                         | 25.7 ms: 1.50x faster                                                          |
| deepcopy                   | 360 us                                                          | 241 us: 1.49x faster                                                           |
| comprehensions             | 19.2 us                                                         | 13.1 us: 1.46x faster                                                          |
| nbody                      | 127 ms                                                          | 88.5 ms: 1.43x faster                                                          |
| async_tree_memoization_tg  | 350 ms                                                          | 246 ms: 1.43x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 195 ms: 1.43x faster                                                           |
| raytrace                   | 308 ms                                                          | 218 ms: 1.41x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.57 ms: 1.39x faster                                                          |
| chaos                      | 69.4 ms                                                         | 50.5 ms: 1.37x faster                                                          |
| scimark_sor                | 130 ms                                                          | 94.8 ms: 1.37x faster                                                          |
| hexiom                     | 6.82 ms                                                         | 4.99 ms: 1.37x faster                                                          |
| logging_silent             | 101 ns                                                          | 74.2 ns: 1.36x faster                                                          |
| spectral_norm              | 104 ms                                                          | 76.5 ms: 1.36x faster                                                          |
| scimark_lu                 | 93.2 ms                                                         | 70.1 ms: 1.33x faster                                                          |
| async_tree_none            | 298 ms                                                          | 224 ms: 1.33x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 511 ms: 1.32x faster                                                           |
| float                      | 76.7 ms                                                         | 58.2 ms: 1.32x faster                                                          |
| async_tree_memoization     | 364 ms                                                          | 276 ms: 1.32x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 50.6 ms: 1.31x faster                                                          |
| pyflate                    | 424 ms                                                          | 331 ms: 1.28x faster                                                           |
| nqueens                    | 93.7 ms                                                         | 73.9 ms: 1.27x faster                                                          |
| deepcopy_reduce            | 3.23 us                                                         | 2.55 us: 1.27x faster                                                          |
| async_tree_io              | 693 ms                                                          | 549 ms: 1.26x faster                                                           |
| scimark_fft                | 271 ms                                                          | 217 ms: 1.25x faster                                                           |
| regex_compile              | 129 ms                                                          | 103 ms: 1.25x faster                                                           |
| mako                       | 9.96 ms                                                         | 8.01 ms: 1.24x faster                                                          |
| unpickle_pure_python       | 210 us                                                          | 169 us: 1.24x faster                                                           |
| go                         | 137 ms                                                          | 111 ms: 1.24x faster                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 55.9 ms: 1.24x faster                                                          |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.14 ms: 1.23x faster                                                          |
| coroutines                 | 20.9 ms                                                         | 17.3 ms: 1.21x faster                                                          |
| tomli_loads                | 2.20 sec                                                        | 1.82 sec: 1.21x faster                                                         |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 467 ms: 1.21x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 454 ms: 1.20x faster                                                           |
| logging_simple             | 9.75 us                                                         | 8.12 us: 1.20x faster                                                          |
| dulwich_log                | 58.5 ms                                                         | 49.4 ms: 1.18x faster                                                          |
| sqlglot_parse              | 1.25 ms                                                         | 1.06 ms: 1.18x faster                                                          |
| sqlglot_transpile          | 1.53 ms                                                         | 1.30 ms: 1.17x faster                                                          |
| pickle_pure_python         | 286 us                                                          | 244 us: 1.17x faster                                                           |
| logging_format             | 10.4 us                                                         | 8.87 us: 1.17x faster                                                          |
| pycparser                  | 978 ms                                                          | 836 ms: 1.17x faster                                                           |
| richards_super             | 46.5 ms                                                         | 40.2 ms: 1.16x faster                                                          |
| richards                   | 41.3 ms                                                         | 35.8 ms: 1.15x faster                                                          |
| mdp                        | 1.91 sec                                                        | 1.67 sec: 1.15x faster                                                         |
| fannkuch                   | 354 ms                                                          | 310 ms: 1.14x faster                                                           |
| sympy_integrate            | 17.5 ms                                                         | 15.4 ms: 1.14x faster                                                          |
| meteor_contest             | 86.9 ms                                                         | 76.7 ms: 1.13x faster                                                          |
| sympy_sum                  | 123 ms                                                          | 109 ms: 1.13x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 47.3 ms: 1.13x faster                                                          |
| xml_etree_iterparse        | 77.6 ms                                                         | 69.2 ms: 1.12x faster                                                          |
| async_generators           | 313 ms                                                          | 280 ms: 1.12x faster                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 986 us: 1.12x faster                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.34 sec: 1.12x faster                                                         |
| 2to3                       | 280 ms                                                          | 251 ms: 1.12x faster                                                           |
| sympy_str                  | 240 ms                                                          | 217 ms: 1.10x faster                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 44.0 ms: 1.10x faster                                                          |
| pprint_safe_repr           | 721 ms                                                          | 657 ms: 1.10x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 66.8 ms: 1.08x faster                                                          |
| regex_effbot               | 2.04 ms                                                         | 1.91 ms: 1.06x faster                                                          |
| django_template            | 36.9 ms                                                         | 34.7 ms: 1.06x faster                                                          |
| xml_etree_parse            | 113 ms                                                          | 107 ms: 1.06x faster                                                           |
| regex_dna                  | 127 ms                                                          | 122 ms: 1.04x faster                                                           |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.0 sec: 1.04x faster                                                         |
| docutils                   | 1.98 sec                                                        | 1.91 sec: 1.04x faster                                                         |
| sympy_expand               | 398 ms                                                          | 385 ms: 1.03x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 88.6 ms: 1.03x faster                                                          |
| bench_mp_pool              | 75.4 ms                                                         | 73.4 ms: 1.03x faster                                                          |
| json_loads                 | 20.4 us                                                         | 20.0 us: 1.02x faster                                                          |
| pidigits                   | 199 ms                                                          | 199 ms: 1.00x faster                                                           |
| json_dumps                 | 7.40 ms                                                         | 7.53 ms: 1.02x slower                                                          |
| python_startup_no_site     | 19.1 ms                                                         | 19.7 ms: 1.03x slower                                                          |
| python_startup             | 22.4 ms                                                         | 23.7 ms: 1.06x slower                                                          |
| coverage                   | 48.4 ms                                                         | 51.8 ms: 1.07x slower                                                          |
| typing_runtime_protocols   | 126 us                                                          | 137 us: 1.08x slower                                                           |
| regex_v8                   | 15.0 ms                                                         | 16.3 ms: 1.08x slower                                                          |
| asyncio_tcp                | 662 ms                                                          | 719 ms: 1.09x slower                                                           |
| telco                      | 5.51 ms                                                         | 6.15 ms: 1.12x slower                                                          |
| create_gc_cycles           | 652 us                                                          | 758 us: 1.16x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 230 ms: 2.29x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.16x faster                                                                   |

Benchmark hidden because not significant (3): tornado_http, gc_traversal, json
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240730-3.14.0a0-d27a53f/bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: unknown