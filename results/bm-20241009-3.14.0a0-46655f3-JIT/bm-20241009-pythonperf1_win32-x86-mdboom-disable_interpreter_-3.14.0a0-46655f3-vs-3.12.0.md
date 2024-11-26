# Results vs. 3.12.0

- fork: mdboom
- ref: disable_interpreter_
- machine: windows-x86
- commit hash: 46655f3
- commit date: 2024-10-09
- overall geometric mean: 1.235x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241009-pythonperf1_win32-x86-mdboom-disable_interpreter_-3.14.0a0-46655f3 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 262 ms: 1.07x faster                                                           |
| docutils       | 1.98 sec                                                        | 2.05 sec: 1.03x slower                                                         |
| tornado_http   | 105 ms                                                          | 108 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                           | 1.00x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241009-pythonperf1_win32-x86-mdboom-disable_interpreter_-3.14.0a0-46655f3 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none_tg         | 278 ms                                                          | 196 ms: 1.41x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 251 ms: 1.40x faster                                                           |
| async_tree_none            | 298 ms                                                          | 219 ms: 1.36x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 274 ms: 1.33x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 510 ms: 1.33x faster                                                           |
| async_tree_io              | 693 ms                                                          | 539 ms: 1.29x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 477 ms: 1.15x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 494 ms: 1.14x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.30x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241009-pythonperf1_win32-x86-mdboom-disable_interpreter_-3.14.0a0-46655f3 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 52.9 ms: 2.40x faster                                                          |
| float          | 76.7 ms                                                         | 45.3 ms: 1.69x faster                                                          |
| pidigits       | 199 ms                                                          | 205 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                           | 1.58x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241009-pythonperf1_win32-x86-mdboom-disable_interpreter_-3.14.0a0-46655f3 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 106 ms: 1.22x faster                                                           |
| regex_dna      | 127 ms                                                          | 114 ms: 1.11x faster                                                           |
| regex_effbot   | 2.04 ms                                                         | 1.84 ms: 1.11x faster                                                          |
| regex_v8       | 15.0 ms                                                         | 15.7 ms: 1.04x slower                                                          |
| Geometric mean | (ref)                                                           | 1.10x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241009-pythonperf1_win32-x86-mdboom-disable_interpreter_-3.14.0a0-46655f3 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.53 sec: 1.44x faster                                                         |
| xml_etree_generate   | 72.1 ms                                                         | 54.1 ms: 1.33x faster                                                          |
| unpickle_pure_python | 210 us                                                          | 159 us: 1.32x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 40.6 ms: 1.31x faster                                                          |
| xml_etree_iterparse  | 77.6 ms                                                         | 63.4 ms: 1.22x faster                                                          |
| pickle_pure_python   | 286 us                                                          | 250 us: 1.14x faster                                                           |
| json_dumps           | 7.40 ms                                                         | 6.79 ms: 1.09x faster                                                          |
| xml_etree_parse      | 113 ms                                                          | 109 ms: 1.04x faster                                                           |
| pickle_list          | 3.37 us                                                         | 3.44 us: 1.02x slower                                                          |
| json_loads           | 20.4 us                                                         | 21.2 us: 1.04x slower                                                          |
| pickle_dict          | 19.9 us                                                         | 21.6 us: 1.08x slower                                                          |
| pickle               | 7.79 us                                                         | 8.46 us: 1.09x slower                                                          |
| unpickle             | 9.71 us                                                         | 10.6 us: 1.09x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.10x faster                                                                   |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241009-pythonperf1_win32-x86-mdboom-disable_interpreter_-3.14.0a0-46655f3 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.2 ms: 1.06x slower                                                          |
| python_startup         | 22.4 ms                                                         | 24.4 ms: 1.09x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.07x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241009-pythonperf1_win32-x86-mdboom-disable_interpreter_-3.14.0a0-46655f3 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.69 ms: 1.75x faster                                                          |
| django_template | 36.9 ms                                                         | 32.8 ms: 1.13x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.40x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241009-pythonperf1_win32-x86-mdboom-disable_interpreter_-3.14.0a0-46655f3 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 15.2 us: 2.53x faster                                                          |
| nbody                      | 127 ms                                                          | 52.9 ms: 2.40x faster                                                          |
| spectral_norm              | 104 ms                                                          | 50.9 ms: 2.04x faster                                                          |
| scimark_sor                | 130 ms                                                          | 69.6 ms: 1.86x faster                                                          |
| logging_silent             | 101 ns                                                          | 56.7 ns: 1.78x faster                                                          |
| deltablue                  | 3.58 ms                                                         | 2.03 ms: 1.76x faster                                                          |
| mako                       | 9.96 ms                                                         | 5.69 ms: 1.75x faster                                                          |
| float                      | 76.7 ms                                                         | 45.3 ms: 1.69x faster                                                          |
| scimark_lu                 | 93.2 ms                                                         | 57.9 ms: 1.61x faster                                                          |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.41 ms: 1.60x faster                                                          |
| scimark_fft                | 271 ms                                                          | 170 ms: 1.59x faster                                                           |
| comprehensions             | 19.2 us                                                         | 12.1 us: 1.59x faster                                                          |
| generators                 | 38.5 ms                                                         | 24.4 ms: 1.58x faster                                                          |
| deepcopy                   | 360 us                                                          | 232 us: 1.55x faster                                                           |
| fannkuch                   | 354 ms                                                          | 239 ms: 1.48x faster                                                           |
| pyflate                    | 424 ms                                                          | 288 ms: 1.47x faster                                                           |
| unpack_sequence            | 62.5 ns                                                         | 42.8 ns: 1.46x faster                                                          |
| crypto_pyaes               | 69.2 ms                                                         | 47.8 ms: 1.45x faster                                                          |
| tomli_loads                | 2.20 sec                                                        | 1.53 sec: 1.44x faster                                                         |
| scimark_monte_carlo        | 66.4 ms                                                         | 46.8 ms: 1.42x faster                                                          |
| async_tree_none_tg         | 278 ms                                                          | 196 ms: 1.41x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 251 ms: 1.40x faster                                                           |
| go                         | 137 ms                                                          | 100 ms: 1.37x faster                                                           |
| async_tree_none            | 298 ms                                                          | 219 ms: 1.36x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.39 us: 1.35x faster                                                          |
| hexiom                     | 6.82 ms                                                         | 5.08 ms: 1.34x faster                                                          |
| xml_etree_generate         | 72.1 ms                                                         | 54.1 ms: 1.33x faster                                                          |
| async_tree_memoization     | 364 ms                                                          | 274 ms: 1.33x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 510 ms: 1.33x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 159 us: 1.32x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 40.6 ms: 1.31x faster                                                          |
| chaos                      | 69.4 ms                                                         | 53.9 ms: 1.29x faster                                                          |
| async_tree_io              | 693 ms                                                          | 539 ms: 1.29x faster                                                           |
| logging_simple             | 9.75 us                                                         | 7.69 us: 1.27x faster                                                          |
| pprint_safe_repr           | 721 ms                                                          | 572 ms: 1.26x faster                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.19 sec: 1.26x faster                                                         |
| nqueens                    | 93.7 ms                                                         | 75.1 ms: 1.25x faster                                                          |
| logging_format             | 10.4 us                                                         | 8.36 us: 1.24x faster                                                          |
| richards_super             | 46.5 ms                                                         | 37.4 ms: 1.24x faster                                                          |
| xml_etree_iterparse        | 77.6 ms                                                         | 63.4 ms: 1.22x faster                                                          |
| sqlglot_parse              | 1.25 ms                                                         | 1.02 ms: 1.22x faster                                                          |
| richards                   | 41.3 ms                                                         | 33.8 ms: 1.22x faster                                                          |
| regex_compile              | 129 ms                                                          | 106 ms: 1.22x faster                                                           |
| raytrace                   | 308 ms                                                          | 253 ms: 1.22x faster                                                           |
| pycparser                  | 978 ms                                                          | 824 ms: 1.19x faster                                                           |
| dulwich_log                | 58.5 ms                                                         | 49.7 ms: 1.18x faster                                                          |
| meteor_contest             | 86.9 ms                                                         | 74.3 ms: 1.17x faster                                                          |
| coroutines                 | 20.9 ms                                                         | 18.1 ms: 1.16x faster                                                          |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 477 ms: 1.15x faster                                                           |
| pickle_pure_python         | 286 us                                                          | 250 us: 1.14x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 494 ms: 1.14x faster                                                           |
| sqlglot_transpile          | 1.53 ms                                                         | 1.34 ms: 1.14x faster                                                          |
| django_template            | 36.9 ms                                                         | 32.8 ms: 1.13x faster                                                          |
| mdp                        | 1.91 sec                                                        | 1.70 sec: 1.12x faster                                                         |
| regex_dna                  | 127 ms                                                          | 114 ms: 1.11x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.84 ms: 1.11x faster                                                          |
| sqlite_synth               | 2.07 us                                                         | 1.89 us: 1.10x faster                                                          |
| bench_thread_pool          | 1.10 ms                                                         | 1.01 ms: 1.09x faster                                                          |
| json_dumps                 | 7.40 ms                                                         | 6.79 ms: 1.09x faster                                                          |
| 2to3                       | 280 ms                                                          | 262 ms: 1.07x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 117 ms: 1.05x faster                                                           |
| sympy_str                  | 240 ms                                                          | 230 ms: 1.04x faster                                                           |
| xml_etree_parse            | 113 ms                                                          | 109 ms: 1.04x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 88.4 ms: 1.03x faster                                                          |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.4 sec: 1.01x faster                                                         |
| sympy_expand               | 398 ms                                                          | 403 ms: 1.01x slower                                                           |
| pickle_list                | 3.37 us                                                         | 3.44 us: 1.02x slower                                                          |
| pidigits                   | 199 ms                                                          | 205 ms: 1.03x slower                                                           |
| tornado_http               | 105 ms                                                          | 108 ms: 1.03x slower                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 77.8 ms: 1.03x slower                                                          |
| docutils                   | 1.98 sec                                                        | 2.05 sec: 1.03x slower                                                         |
| sqlglot_optimize           | 48.5 ms                                                         | 50.1 ms: 1.03x slower                                                          |
| sqlglot_normalize          | 100 ms                                                          | 104 ms: 1.04x slower                                                           |
| json_loads                 | 20.4 us                                                         | 21.2 us: 1.04x slower                                                          |
| async_generators           | 313 ms                                                          | 326 ms: 1.04x slower                                                           |
| regex_v8                   | 15.0 ms                                                         | 15.7 ms: 1.04x slower                                                          |
| python_startup_no_site     | 19.1 ms                                                         | 20.2 ms: 1.06x slower                                                          |
| coverage                   | 48.4 ms                                                         | 51.6 ms: 1.07x slower                                                          |
| pickle_dict                | 19.9 us                                                         | 21.6 us: 1.08x slower                                                          |
| pickle                     | 7.79 us                                                         | 8.46 us: 1.09x slower                                                          |
| unpickle                   | 9.71 us                                                         | 10.6 us: 1.09x slower                                                          |
| python_startup             | 22.4 ms                                                         | 24.4 ms: 1.09x slower                                                          |
| telco                      | 5.51 ms                                                         | 6.02 ms: 1.09x slower                                                          |
| typing_runtime_protocols   | 126 us                                                          | 145 us: 1.15x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 784 us: 1.20x slower                                                           |
| asyncio_tcp                | 662 ms                                                          | 809 ms: 1.22x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.21x faster                                                                   |

Benchmark hidden because not significant (4): unpickle_list, json, gc_traversal, sympy_integrate
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20241009-3.14.0a0-46655f3-JIT/bm-20241009-pythonperf1_win32-x86-mdboom-disable_interpreter_-3.14.0a0-46655f3.json: genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.235x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: unknown