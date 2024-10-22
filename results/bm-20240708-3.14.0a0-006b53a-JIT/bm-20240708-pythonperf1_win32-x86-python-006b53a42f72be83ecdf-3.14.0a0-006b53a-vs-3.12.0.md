# Results vs. 3.12.0

- fork: python
- ref: 006b53a42f72be83ecdf
- machine: windows-x86
- commit hash: 006b53a
- commit date: 2024-07-08
- overall geometric mean: 1.23x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 252 ms: 1.11x faster                                                           |
| docutils       | 1.98 sec                                                        | 1.93 sec: 1.03x faster                                                         |
| tornado_http   | 105 ms                                                          | 98.3 ms: 1.07x faster                                                          |
| Geometric mean | (ref)                                                           | 1.07x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none_tg         | 278 ms                                                          | 195 ms: 1.43x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 248 ms: 1.42x faster                                                           |
| async_tree_none            | 298 ms                                                          | 219 ms: 1.36x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 503 ms: 1.35x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 272 ms: 1.34x faster                                                           |
| async_tree_io              | 693 ms                                                          | 539 ms: 1.29x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 470 ms: 1.20x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 462 ms: 1.18x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.32x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 55.7 ms: 2.28x faster                                                          |
| float          | 76.7 ms                                                         | 44.1 ms: 1.74x faster                                                          |
| pidigits       | 199 ms                                                          | 195 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                           | 1.59x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 95.0 ms: 1.36x faster                                                          |
| regex_effbot   | 2.04 ms                                                         | 1.90 ms: 1.07x faster                                                          |
| regex_dna      | 127 ms                                                          | 123 ms: 1.04x faster                                                           |
| regex_v8       | 15.0 ms                                                         | 15.8 ms: 1.05x slower                                                          |
| Geometric mean | (ref)                                                           | 1.10x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.48 sec: 1.48x faster                                                         |
| unpickle_pure_python | 210 us                                                          | 148 us: 1.42x faster                                                           |
| pickle_pure_python   | 286 us                                                          | 212 us: 1.35x faster                                                           |
| xml_etree_iterparse  | 77.6 ms                                                         | 61.8 ms: 1.26x faster                                                          |
| xml_etree_process    | 53.2 ms                                                         | 44.0 ms: 1.21x faster                                                          |
| xml_etree_generate   | 72.1 ms                                                         | 60.9 ms: 1.18x faster                                                          |
| xml_etree_parse      | 113 ms                                                          | 104 ms: 1.09x faster                                                           |
| json_dumps           | 7.40 ms                                                         | 7.14 ms: 1.04x faster                                                          |
| json_loads           | 20.4 us                                                         | 21.3 us: 1.05x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.21x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.3 ms: 1.01x slower                                                          |
| python_startup         | 22.4 ms                                                         | 23.2 ms: 1.04x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.02x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.44 ms: 1.83x faster                                                          |
| django_template | 36.9 ms                                                         | 32.6 ms: 1.13x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.44x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 15.5 us: 2.48x faster                                                          |
| nbody                      | 127 ms                                                          | 55.7 ms: 2.28x faster                                                          |
| spectral_norm              | 104 ms                                                          | 47.3 ms: 2.20x faster                                                          |
| mako                       | 9.96 ms                                                         | 5.44 ms: 1.83x faster                                                          |
| float                      | 76.7 ms                                                         | 44.1 ms: 1.74x faster                                                          |
| logging_silent             | 101 ns                                                          | 58.6 ns: 1.72x faster                                                          |
| comprehensions             | 19.2 us                                                         | 11.4 us: 1.69x faster                                                          |
| scimark_fft                | 271 ms                                                          | 165 ms: 1.65x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.36 ms: 1.64x faster                                                          |
| scimark_monte_carlo        | 66.4 ms                                                         | 41.2 ms: 1.61x faster                                                          |
| fannkuch                   | 354 ms                                                          | 226 ms: 1.56x faster                                                           |
| pyflate                    | 424 ms                                                          | 278 ms: 1.52x faster                                                           |
| deepcopy                   | 360 us                                                          | 239 us: 1.51x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 4.60 ms: 1.48x faster                                                          |
| tomli_loads                | 2.20 sec                                                        | 1.48 sec: 1.48x faster                                                         |
| async_tree_none_tg         | 278 ms                                                          | 195 ms: 1.43x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 148 us: 1.42x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 248 ms: 1.42x faster                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 49.2 ms: 1.41x faster                                                          |
| generators                 | 38.5 ms                                                         | 27.7 ms: 1.39x faster                                                          |
| regex_compile              | 129 ms                                                          | 95.0 ms: 1.36x faster                                                          |
| deepcopy_reduce            | 3.23 us                                                         | 2.37 us: 1.36x faster                                                          |
| async_tree_none            | 298 ms                                                          | 219 ms: 1.36x faster                                                           |
| pickle_pure_python         | 286 us                                                          | 212 us: 1.35x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 503 ms: 1.35x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 272 ms: 1.34x faster                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.14 sec: 1.32x faster                                                         |
| raytrace                   | 308 ms                                                          | 235 ms: 1.31x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.73 ms: 1.31x faster                                                          |
| pprint_safe_repr           | 721 ms                                                          | 552 ms: 1.31x faster                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 958 us: 1.30x faster                                                           |
| logging_simple             | 9.75 us                                                         | 7.55 us: 1.29x faster                                                          |
| async_tree_io              | 693 ms                                                          | 539 ms: 1.29x faster                                                           |
| chaos                      | 69.4 ms                                                         | 54.0 ms: 1.29x faster                                                          |
| nqueens                    | 93.7 ms                                                         | 73.2 ms: 1.28x faster                                                          |
| logging_format             | 10.4 us                                                         | 8.13 us: 1.28x faster                                                          |
| richards                   | 41.3 ms                                                         | 32.4 ms: 1.28x faster                                                          |
| scimark_sor                | 130 ms                                                          | 102 ms: 1.27x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 61.8 ms: 1.26x faster                                                          |
| sqlglot_transpile          | 1.53 ms                                                         | 1.22 ms: 1.26x faster                                                          |
| go                         | 137 ms                                                          | 112 ms: 1.22x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 44.0 ms: 1.21x faster                                                          |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 470 ms: 1.20x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 77.9 ms: 1.20x faster                                                          |
| richards_super             | 46.5 ms                                                         | 38.9 ms: 1.19x faster                                                          |
| xml_etree_generate         | 72.1 ms                                                         | 60.9 ms: 1.18x faster                                                          |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 462 ms: 1.18x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 17.9 ms: 1.17x faster                                                          |
| meteor_contest             | 86.9 ms                                                         | 74.6 ms: 1.16x faster                                                          |
| pycparser                  | 978 ms                                                          | 844 ms: 1.16x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.66 sec: 1.15x faster                                                         |
| django_template            | 36.9 ms                                                         | 32.6 ms: 1.13x faster                                                          |
| bench_thread_pool          | 1.10 ms                                                         | 978 us: 1.13x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 109 ms: 1.13x faster                                                           |
| 2to3                       | 280 ms                                                          | 252 ms: 1.11x faster                                                           |
| sympy_integrate            | 17.5 ms                                                         | 15.9 ms: 1.10x faster                                                          |
| sqlglot_optimize           | 48.5 ms                                                         | 44.1 ms: 1.10x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 83.3 ms: 1.10x faster                                                          |
| sympy_str                  | 240 ms                                                          | 219 ms: 1.09x faster                                                           |
| xml_etree_parse            | 113 ms                                                          | 104 ms: 1.09x faster                                                           |
| asyncio_tcp                | 662 ms                                                          | 613 ms: 1.08x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.90 ms: 1.07x faster                                                          |
| tornado_http               | 105 ms                                                          | 98.3 ms: 1.07x faster                                                          |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 16.8 sec: 1.05x faster                                                         |
| json_dumps                 | 7.40 ms                                                         | 7.14 ms: 1.04x faster                                                          |
| regex_dna                  | 127 ms                                                          | 123 ms: 1.04x faster                                                           |
| docutils                   | 1.98 sec                                                        | 1.93 sec: 1.03x faster                                                         |
| bench_mp_pool              | 75.4 ms                                                         | 73.7 ms: 1.02x faster                                                          |
| pidigits                   | 199 ms                                                          | 195 ms: 1.02x faster                                                           |
| sympy_expand               | 398 ms                                                          | 392 ms: 1.01x faster                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.45 ms: 1.01x slower                                                          |
| python_startup_no_site     | 19.1 ms                                                         | 19.3 ms: 1.01x slower                                                          |
| async_generators           | 313 ms                                                          | 317 ms: 1.01x slower                                                           |
| json                       | 4.15 ms                                                         | 4.20 ms: 1.01x slower                                                          |
| python_startup             | 22.4 ms                                                         | 23.2 ms: 1.04x slower                                                          |
| json_loads                 | 20.4 us                                                         | 21.3 us: 1.05x slower                                                          |
| regex_v8                   | 15.0 ms                                                         | 15.8 ms: 1.05x slower                                                          |
| coverage                   | 48.4 ms                                                         | 51.3 ms: 1.06x slower                                                          |
| telco                      | 5.51 ms                                                         | 5.92 ms: 1.07x slower                                                          |
| typing_runtime_protocols   | 126 us                                                          | 145 us: 1.14x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 751 us: 1.15x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 241 ms: 2.40x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.23x faster                                                                   |
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240708-3.14.0a0-006b53a-JIT/bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: unknown