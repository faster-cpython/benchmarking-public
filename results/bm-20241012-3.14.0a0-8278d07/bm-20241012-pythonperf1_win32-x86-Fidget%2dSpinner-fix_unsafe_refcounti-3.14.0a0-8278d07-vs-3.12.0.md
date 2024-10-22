# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: fix_unsafe_refcounti
- machine: windows-x86
- commit hash: 8278d07
- commit date: 2024-10-12
- overall geometric mean: 1.13x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241012-pythonperf1_win32-x86-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 249 ms: 1.12x faster                                                                     |
| docutils       | 1.98 sec                                                        | 1.84 sec: 1.08x faster                                                                   |
| tornado_http   | 105 ms                                                          | 103 ms: 1.01x faster                                                                     |
| Geometric mean | (ref)                                                           | 1.07x faster                                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241012-pythonperf1_win32-x86-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| async_tree_none_tg         | 278 ms                                                          | 200 ms: 1.39x faster                                                                     |
| async_tree_memoization_tg  | 350 ms                                                          | 253 ms: 1.39x faster                                                                     |
| async_tree_none            | 298 ms                                                          | 218 ms: 1.37x faster                                                                     |
| async_tree_memoization     | 364 ms                                                          | 271 ms: 1.34x faster                                                                     |
| async_tree_io_tg           | 677 ms                                                          | 520 ms: 1.30x faster                                                                     |
| async_tree_io              | 693 ms                                                          | 537 ms: 1.29x faster                                                                     |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 454 ms: 1.20x faster                                                                     |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 470 ms: 1.20x faster                                                                     |
| Geometric mean             | (ref)                                                           | 1.31x faster                                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241012-pythonperf1_win32-x86-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 89.4 ms: 1.42x faster                                                                    |
| float          | 76.7 ms                                                         | 61.2 ms: 1.25x faster                                                                    |
| pidigits       | 199 ms                                                          | 201 ms: 1.01x slower                                                                     |
| Geometric mean | (ref)                                                           | 1.21x faster                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241012-pythonperf1_win32-x86-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 106 ms: 1.21x faster                                                                     |
| regex_effbot   | 2.04 ms                                                         | 1.79 ms: 1.14x faster                                                                    |
| regex_dna      | 127 ms                                                          | 113 ms: 1.13x faster                                                                     |
| regex_v8       | 15.0 ms                                                         | 15.3 ms: 1.02x slower                                                                    |
| Geometric mean | (ref)                                                           | 1.11x faster                                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241012-pythonperf1_win32-x86-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.77 sec: 1.24x faster                                                                   |
| unpickle_pure_python | 210 us                                                          | 180 us: 1.17x faster                                                                     |
| xml_etree_iterparse  | 77.6 ms                                                         | 68.1 ms: 1.14x faster                                                                    |
| xml_etree_process    | 53.2 ms                                                         | 47.4 ms: 1.12x faster                                                                    |
| xml_etree_generate   | 72.1 ms                                                         | 66.6 ms: 1.08x faster                                                                    |
| pickle_pure_python   | 286 us                                                          | 272 us: 1.05x faster                                                                     |
| unpickle_list        | 2.95 us                                                         | 2.99 us: 1.01x slower                                                                    |
| json_loads           | 20.4 us                                                         | 20.7 us: 1.02x slower                                                                    |
| pickle_list          | 3.37 us                                                         | 3.50 us: 1.04x slower                                                                    |
| unpickle             | 9.71 us                                                         | 10.4 us: 1.07x slower                                                                    |
| pickle               | 7.79 us                                                         | 8.48 us: 1.09x slower                                                                    |
| pickle_dict          | 19.9 us                                                         | 21.7 us: 1.09x slower                                                                    |
| json_dumps           | 7.40 ms                                                         | 9.02 ms: 1.22x slower                                                                    |
| Geometric mean       | (ref)                                                           | 1.02x faster                                                                             |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241012-pythonperf1_win32-x86-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.0 ms: 1.05x slower                                                                    |
| python_startup         | 22.4 ms                                                         | 24.3 ms: 1.09x slower                                                                    |
| Geometric mean         | (ref)                                                           | 1.07x slower                                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241012-pythonperf1_win32-x86-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|-----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.86 ms: 1.27x faster                                                                    |
| django_template | 36.9 ms                                                         | 32.8 ms: 1.13x faster                                                                    |
| Geometric mean  | (ref)                                                           | 1.19x faster                                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241012-pythonperf1_win32-x86-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 22.1 us: 1.73x faster                                                                    |
| generators                 | 38.5 ms                                                         | 23.6 ms: 1.63x faster                                                                    |
| deepcopy                   | 360 us                                                          | 241 us: 1.49x faster                                                                     |
| comprehensions             | 19.2 us                                                         | 13.3 us: 1.44x faster                                                                    |
| nbody                      | 127 ms                                                          | 89.4 ms: 1.42x faster                                                                    |
| async_tree_none_tg         | 278 ms                                                          | 200 ms: 1.39x faster                                                                     |
| async_tree_memoization_tg  | 350 ms                                                          | 253 ms: 1.39x faster                                                                     |
| hexiom                     | 6.82 ms                                                         | 4.94 ms: 1.38x faster                                                                    |
| logging_silent             | 101 ns                                                          | 73.2 ns: 1.38x faster                                                                    |
| scimark_lu                 | 93.2 ms                                                         | 67.8 ms: 1.38x faster                                                                    |
| spectral_norm              | 104 ms                                                          | 75.9 ms: 1.37x faster                                                                    |
| async_tree_none            | 298 ms                                                          | 218 ms: 1.37x faster                                                                     |
| async_tree_memoization     | 364 ms                                                          | 271 ms: 1.34x faster                                                                     |
| go                         | 137 ms                                                          | 103 ms: 1.34x faster                                                                     |
| deltablue                  | 3.58 ms                                                         | 2.72 ms: 1.32x faster                                                                    |
| async_tree_io_tg           | 677 ms                                                          | 520 ms: 1.30x faster                                                                     |
| async_tree_io              | 693 ms                                                          | 537 ms: 1.29x faster                                                                     |
| nqueens                    | 93.7 ms                                                         | 73.5 ms: 1.27x faster                                                                    |
| deepcopy_reduce            | 3.23 us                                                         | 2.53 us: 1.27x faster                                                                    |
| scimark_sor                | 130 ms                                                          | 102 ms: 1.27x faster                                                                     |
| mako                       | 9.96 ms                                                         | 7.86 ms: 1.27x faster                                                                    |
| logging_simple             | 9.75 us                                                         | 7.77 us: 1.26x faster                                                                    |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.08 ms: 1.25x faster                                                                    |
| float                      | 76.7 ms                                                         | 61.2 ms: 1.25x faster                                                                    |
| tomli_loads                | 2.20 sec                                                        | 1.77 sec: 1.24x faster                                                                   |
| chaos                      | 69.4 ms                                                         | 55.9 ms: 1.24x faster                                                                    |
| raytrace                   | 308 ms                                                          | 249 ms: 1.24x faster                                                                     |
| regex_compile              | 129 ms                                                          | 106 ms: 1.21x faster                                                                     |
| logging_format             | 10.4 us                                                         | 8.58 us: 1.21x faster                                                                    |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 454 ms: 1.20x faster                                                                     |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 470 ms: 1.20x faster                                                                     |
| unpack_sequence            | 62.5 ns                                                         | 52.3 ns: 1.20x faster                                                                    |
| coroutines                 | 20.9 ms                                                         | 17.5 ms: 1.19x faster                                                                    |
| scimark_fft                | 271 ms                                                          | 229 ms: 1.18x faster                                                                     |
| scimark_monte_carlo        | 66.4 ms                                                         | 56.7 ms: 1.17x faster                                                                    |
| pyflate                    | 424 ms                                                          | 362 ms: 1.17x faster                                                                     |
| pycparser                  | 978 ms                                                          | 835 ms: 1.17x faster                                                                     |
| crypto_pyaes               | 69.2 ms                                                         | 59.2 ms: 1.17x faster                                                                    |
| unpickle_pure_python       | 210 us                                                          | 180 us: 1.17x faster                                                                     |
| sympy_sum                  | 123 ms                                                          | 106 ms: 1.16x faster                                                                     |
| sqlglot_transpile          | 1.53 ms                                                         | 1.33 ms: 1.15x faster                                                                    |
| pprint_pformat             | 1.50 sec                                                        | 1.31 sec: 1.15x faster                                                                   |
| dulwich_log                | 58.5 ms                                                         | 51.2 ms: 1.14x faster                                                                    |
| sqlglot_parse              | 1.25 ms                                                         | 1.09 ms: 1.14x faster                                                                    |
| xml_etree_iterparse        | 77.6 ms                                                         | 68.1 ms: 1.14x faster                                                                    |
| regex_effbot               | 2.04 ms                                                         | 1.79 ms: 1.14x faster                                                                    |
| sympy_integrate            | 17.5 ms                                                         | 15.4 ms: 1.14x faster                                                                    |
| regex_dna                  | 127 ms                                                          | 113 ms: 1.13x faster                                                                     |
| django_template            | 36.9 ms                                                         | 32.8 ms: 1.13x faster                                                                    |
| 2to3                       | 280 ms                                                          | 249 ms: 1.12x faster                                                                     |
| xml_etree_process          | 53.2 ms                                                         | 47.4 ms: 1.12x faster                                                                    |
| sqlglot_optimize           | 48.5 ms                                                         | 43.5 ms: 1.11x faster                                                                    |
| pprint_safe_repr           | 721 ms                                                          | 647 ms: 1.11x faster                                                                     |
| mdp                        | 1.91 sec                                                        | 1.72 sec: 1.11x faster                                                                   |
| sympy_str                  | 240 ms                                                          | 216 ms: 1.11x faster                                                                     |
| bench_thread_pool          | 1.10 ms                                                         | 997 us: 1.11x faster                                                                     |
| fannkuch                   | 354 ms                                                          | 324 ms: 1.09x faster                                                                     |
| meteor_contest             | 86.9 ms                                                         | 79.8 ms: 1.09x faster                                                                    |
| xml_etree_generate         | 72.1 ms                                                         | 66.6 ms: 1.08x faster                                                                    |
| docutils                   | 1.98 sec                                                        | 1.84 sec: 1.08x faster                                                                   |
| sqlite_synth               | 2.07 us                                                         | 1.94 us: 1.07x faster                                                                    |
| pickle_pure_python         | 286 us                                                          | 272 us: 1.05x faster                                                                     |
| pathlib                    | 91.4 ms                                                         | 87.8 ms: 1.04x faster                                                                    |
| sympy_expand               | 398 ms                                                          | 384 ms: 1.04x faster                                                                     |
| async_generators           | 313 ms                                                          | 303 ms: 1.03x faster                                                                     |
| bench_mp_pool              | 75.4 ms                                                         | 73.6 ms: 1.02x faster                                                                    |
| tornado_http               | 105 ms                                                          | 103 ms: 1.01x faster                                                                     |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.5 sec: 1.01x faster                                                                   |
| richards_super             | 46.5 ms                                                         | 46.0 ms: 1.01x faster                                                                    |
| pidigits                   | 199 ms                                                          | 201 ms: 1.01x slower                                                                     |
| unpickle_list              | 2.95 us                                                         | 2.99 us: 1.01x slower                                                                    |
| regex_v8                   | 15.0 ms                                                         | 15.3 ms: 1.02x slower                                                                    |
| json_loads                 | 20.4 us                                                         | 20.7 us: 1.02x slower                                                                    |
| json                       | 4.15 ms                                                         | 4.30 ms: 1.03x slower                                                                    |
| pickle_list                | 3.37 us                                                         | 3.50 us: 1.04x slower                                                                    |
| python_startup_no_site     | 19.1 ms                                                         | 20.0 ms: 1.05x slower                                                                    |
| unpickle                   | 9.71 us                                                         | 10.4 us: 1.07x slower                                                                    |
| coverage                   | 48.4 ms                                                         | 52.6 ms: 1.09x slower                                                                    |
| pickle                     | 7.79 us                                                         | 8.48 us: 1.09x slower                                                                    |
| python_startup             | 22.4 ms                                                         | 24.3 ms: 1.09x slower                                                                    |
| pickle_dict                | 19.9 us                                                         | 21.7 us: 1.09x slower                                                                    |
| asyncio_tcp                | 662 ms                                                          | 737 ms: 1.11x slower                                                                     |
| typing_runtime_protocols   | 126 us                                                          | 145 us: 1.15x slower                                                                     |
| create_gc_cycles           | 652 us                                                          | 774 us: 1.19x slower                                                                     |
| json_dumps                 | 7.40 ms                                                         | 9.02 ms: 1.22x slower                                                                    |
| telco                      | 5.51 ms                                                         | 6.86 ms: 1.24x slower                                                                    |
| sqlglot_normalize          | 100 ms                                                          | 224 ms: 2.23x slower                                                                     |
| Geometric mean             | (ref)                                                           | 1.13x faster                                                                             |

Benchmark hidden because not significant (3): richards, gc_traversal, xml_etree_parse
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20241012-3.14.0a0-8278d07/bm-20241012-pythonperf1_win32-x86-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: unknown