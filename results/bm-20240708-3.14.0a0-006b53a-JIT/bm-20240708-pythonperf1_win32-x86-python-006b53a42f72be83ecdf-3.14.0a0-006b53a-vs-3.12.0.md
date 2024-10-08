# Results vs. 3.12.0

- fork: python
- ref: 006b53a42f72be83ecdf
- machine: windows-x86
- commit hash: 006b53a
- commit date: 2024-07-08
- overall geometric mean: 1.23x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 254 ms: 1.10x faster                                                           |
| docutils       | 1.98 sec                                                        | 1.95 sec: 1.02x faster                                                         |
| tornado_http   | 105 ms                                                          | 98.2 ms: 1.07x faster                                                          |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none_tg         | 278 ms                                                          | 193 ms: 1.44x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 247 ms: 1.42x faster                                                           |
| async_tree_none            | 298 ms                                                          | 217 ms: 1.37x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 268 ms: 1.35x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 503 ms: 1.35x faster                                                           |
| async_tree_io              | 693 ms                                                          | 539 ms: 1.29x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 469 ms: 1.20x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 458 ms: 1.19x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.32x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 55.2 ms: 2.30x faster                                                          |
| float          | 76.7 ms                                                         | 43.0 ms: 1.78x faster                                                          |
| Geometric mean | (ref)                                                           | 1.59x faster                                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 95.5 ms: 1.35x faster                                                          |
| regex_effbot   | 2.04 ms                                                         | 1.91 ms: 1.07x faster                                                          |
| regex_v8       | 15.0 ms                                                         | 16.1 ms: 1.07x slower                                                          |
| Geometric mean | (ref)                                                           | 1.08x faster                                                                   |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.48 sec: 1.48x faster                                                         |
| unpickle_pure_python | 210 us                                                          | 150 us: 1.40x faster                                                           |
| pickle_pure_python   | 286 us                                                          | 218 us: 1.31x faster                                                           |
| xml_etree_iterparse  | 77.6 ms                                                         | 61.8 ms: 1.26x faster                                                          |
| xml_etree_process    | 53.2 ms                                                         | 43.6 ms: 1.22x faster                                                          |
| xml_etree_generate   | 72.1 ms                                                         | 59.8 ms: 1.21x faster                                                          |
| xml_etree_parse      | 113 ms                                                          | 104 ms: 1.09x faster                                                           |
| json_dumps           | 7.40 ms                                                         | 7.25 ms: 1.02x faster                                                          |
| json_loads           | 20.4 us                                                         | 21.6 us: 1.06x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.20x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.0 ms: 1.05x slower                                                          |
| python_startup         | 22.4 ms                                                         | 23.7 ms: 1.06x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.05x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.46 ms: 1.82x faster                                                          |
| django_template | 36.9 ms                                                         | 33.7 ms: 1.10x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.41x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 15.8 us: 2.43x faster                                                          |
| nbody                      | 127 ms                                                          | 55.2 ms: 2.30x faster                                                          |
| spectral_norm              | 104 ms                                                          | 47.7 ms: 2.17x faster                                                          |
| mako                       | 9.96 ms                                                         | 5.46 ms: 1.82x faster                                                          |
| float                      | 76.7 ms                                                         | 43.0 ms: 1.78x faster                                                          |
| logging_silent             | 101 ns                                                          | 58.5 ns: 1.73x faster                                                          |
| comprehensions             | 19.2 us                                                         | 11.5 us: 1.67x faster                                                          |
| scimark_fft                | 271 ms                                                          | 167 ms: 1.62x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.41 ms: 1.60x faster                                                          |
| scimark_monte_carlo        | 66.4 ms                                                         | 41.9 ms: 1.59x faster                                                          |
| fannkuch                   | 354 ms                                                          | 228 ms: 1.55x faster                                                           |
| deepcopy                   | 360 us                                                          | 238 us: 1.52x faster                                                           |
| pyflate                    | 424 ms                                                          | 285 ms: 1.49x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.48 sec: 1.48x faster                                                         |
| hexiom                     | 6.82 ms                                                         | 4.69 ms: 1.45x faster                                                          |
| async_tree_none_tg         | 278 ms                                                          | 193 ms: 1.44x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 247 ms: 1.42x faster                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 48.9 ms: 1.41x faster                                                          |
| unpickle_pure_python       | 210 us                                                          | 150 us: 1.40x faster                                                           |
| generators                 | 38.5 ms                                                         | 27.9 ms: 1.38x faster                                                          |
| async_tree_none            | 298 ms                                                          | 217 ms: 1.37x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.36 us: 1.37x faster                                                          |
| raytrace                   | 308 ms                                                          | 227 ms: 1.36x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 268 ms: 1.35x faster                                                           |
| regex_compile              | 129 ms                                                          | 95.5 ms: 1.35x faster                                                          |
| async_tree_io_tg           | 677 ms                                                          | 503 ms: 1.35x faster                                                           |
| logging_simple             | 9.75 us                                                         | 7.31 us: 1.33x faster                                                          |
| chaos                      | 69.4 ms                                                         | 52.4 ms: 1.32x faster                                                          |
| sqlglot_parse              | 1.25 ms                                                         | 949 us: 1.32x faster                                                           |
| pickle_pure_python         | 286 us                                                          | 218 us: 1.31x faster                                                           |
| logging_format             | 10.4 us                                                         | 7.99 us: 1.30x faster                                                          |
| deltablue                  | 3.58 ms                                                         | 2.76 ms: 1.30x faster                                                          |
| pprint_pformat             | 1.50 sec                                                        | 1.16 sec: 1.30x faster                                                         |
| scimark_sor                | 130 ms                                                          | 101 ms: 1.29x faster                                                           |
| async_tree_io              | 693 ms                                                          | 539 ms: 1.29x faster                                                           |
| pprint_safe_repr           | 721 ms                                                          | 565 ms: 1.28x faster                                                           |
| sqlglot_transpile          | 1.53 ms                                                         | 1.21 ms: 1.27x faster                                                          |
| nqueens                    | 93.7 ms                                                         | 74.0 ms: 1.27x faster                                                          |
| xml_etree_iterparse        | 77.6 ms                                                         | 61.8 ms: 1.26x faster                                                          |
| richards                   | 41.3 ms                                                         | 33.4 ms: 1.24x faster                                                          |
| xml_etree_process          | 53.2 ms                                                         | 43.6 ms: 1.22x faster                                                          |
| go                         | 137 ms                                                          | 113 ms: 1.22x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 59.8 ms: 1.21x faster                                                          |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 469 ms: 1.20x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 458 ms: 1.19x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 17.7 ms: 1.18x faster                                                          |
| pycparser                  | 978 ms                                                          | 836 ms: 1.17x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 79.7 ms: 1.17x faster                                                          |
| mdp                        | 1.91 sec                                                        | 1.66 sec: 1.15x faster                                                         |
| richards_super             | 46.5 ms                                                         | 40.7 ms: 1.14x faster                                                          |
| meteor_contest             | 86.9 ms                                                         | 76.3 ms: 1.14x faster                                                          |
| bench_thread_pool          | 1.10 ms                                                         | 970 us: 1.14x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 109 ms: 1.13x faster                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 43.5 ms: 1.12x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 82.2 ms: 1.11x faster                                                          |
| sympy_str                  | 240 ms                                                          | 217 ms: 1.10x faster                                                           |
| 2to3                       | 280 ms                                                          | 254 ms: 1.10x faster                                                           |
| sympy_integrate            | 17.5 ms                                                         | 16.0 ms: 1.10x faster                                                          |
| django_template            | 36.9 ms                                                         | 33.7 ms: 1.10x faster                                                          |
| xml_etree_parse            | 113 ms                                                          | 104 ms: 1.09x faster                                                           |
| tornado_http               | 105 ms                                                          | 98.2 ms: 1.07x faster                                                          |
| regex_effbot               | 2.04 ms                                                         | 1.91 ms: 1.07x faster                                                          |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 16.8 sec: 1.05x faster                                                         |
| asyncio_tcp                | 662 ms                                                          | 635 ms: 1.04x faster                                                           |
| sympy_expand               | 398 ms                                                          | 386 ms: 1.03x faster                                                           |
| json_dumps                 | 7.40 ms                                                         | 7.25 ms: 1.02x faster                                                          |
| docutils                   | 1.98 sec                                                        | 1.95 sec: 1.02x faster                                                         |
| async_generators           | 313 ms                                                          | 320 ms: 1.02x slower                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 77.1 ms: 1.02x slower                                                          |
| telco                      | 5.51 ms                                                         | 5.70 ms: 1.03x slower                                                          |
| python_startup_no_site     | 19.1 ms                                                         | 20.0 ms: 1.05x slower                                                          |
| python_startup             | 22.4 ms                                                         | 23.7 ms: 1.06x slower                                                          |
| json_loads                 | 20.4 us                                                         | 21.6 us: 1.06x slower                                                          |
| json                       | 4.15 ms                                                         | 4.43 ms: 1.07x slower                                                          |
| regex_v8                   | 15.0 ms                                                         | 16.1 ms: 1.07x slower                                                          |
| coverage                   | 48.4 ms                                                         | 52.1 ms: 1.08x slower                                                          |
| create_gc_cycles           | 652 us                                                          | 755 us: 1.16x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 151 us: 1.20x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 235 ms: 2.35x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.23x faster                                                                   |

Benchmark hidden because not significant (3): gc_traversal, regex_dna, pidigits
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240708-3.14.0a0-006b53a-JIT/bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: unknown