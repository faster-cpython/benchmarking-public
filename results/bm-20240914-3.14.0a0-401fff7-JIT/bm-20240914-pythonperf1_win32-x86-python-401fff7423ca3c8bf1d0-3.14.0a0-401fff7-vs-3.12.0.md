# Results vs. 3.12.0

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: windows-x86
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.22x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 257 ms: 1.09x faster                                                           |
| docutils       | 1.98 sec                                                        | 2.00 sec: 1.01x slower                                                         |
| tornado_http   | 105 ms                                                          | 99.7 ms: 1.05x faster                                                          |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none_tg         | 278 ms                                                          | 204 ms: 1.36x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 258 ms: 1.36x faster                                                           |
| async_tree_none            | 298 ms                                                          | 223 ms: 1.34x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 281 ms: 1.29x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 524 ms: 1.29x faster                                                           |
| async_tree_io              | 693 ms                                                          | 547 ms: 1.27x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 485 ms: 1.16x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 476 ms: 1.15x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.28x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 50.6 ms: 2.51x faster                                                          |
| float          | 76.7 ms                                                         | 43.8 ms: 1.75x faster                                                          |
| pidigits       | 199 ms                                                          | 195 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                           | 1.65x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 103 ms: 1.25x faster                                                           |
| regex_dna      | 127 ms                                                          | 116 ms: 1.09x faster                                                           |
| regex_effbot   | 2.04 ms                                                         | 1.95 ms: 1.04x faster                                                          |
| regex_v8       | 15.0 ms                                                         | 15.9 ms: 1.06x slower                                                          |
| Geometric mean | (ref)                                                           | 1.08x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.50 sec: 1.46x faster                                                         |
| xml_etree_generate   | 72.1 ms                                                         | 52.7 ms: 1.37x faster                                                          |
| xml_etree_process    | 53.2 ms                                                         | 39.5 ms: 1.35x faster                                                          |
| unpickle_pure_python | 210 us                                                          | 164 us: 1.28x faster                                                           |
| xml_etree_iterparse  | 77.6 ms                                                         | 61.7 ms: 1.26x faster                                                          |
| pickle_pure_python   | 286 us                                                          | 247 us: 1.16x faster                                                           |
| json_dumps           | 7.40 ms                                                         | 6.71 ms: 1.10x faster                                                          |
| xml_etree_parse      | 113 ms                                                          | 104 ms: 1.09x faster                                                           |
| pickle_list          | 3.37 us                                                         | 3.29 us: 1.02x faster                                                          |
| json_loads           | 20.4 us                                                         | 20.6 us: 1.01x slower                                                          |
| pickle               | 7.79 us                                                         | 7.94 us: 1.02x slower                                                          |
| unpickle             | 9.71 us                                                         | 10.3 us: 1.06x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.13x faster                                                                   |

Benchmark hidden because not significant (2): pickle_dict, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.5 ms: 1.02x slower                                                          |
| python_startup         | 22.4 ms                                                         | 23.7 ms: 1.06x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.04x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.47 ms: 1.82x faster                                                          |
| django_template | 36.9 ms                                                         | 35.1 ms: 1.05x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.38x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 15.2 us: 2.52x faster                                                          |
| nbody                      | 127 ms                                                          | 50.6 ms: 2.51x faster                                                          |
| spectral_norm              | 104 ms                                                          | 46.0 ms: 2.25x faster                                                          |
| scimark_sor                | 130 ms                                                          | 68.7 ms: 1.89x faster                                                          |
| mako                       | 9.96 ms                                                         | 5.47 ms: 1.82x faster                                                          |
| float                      | 76.7 ms                                                         | 43.8 ms: 1.75x faster                                                          |
| deltablue                  | 3.58 ms                                                         | 2.09 ms: 1.72x faster                                                          |
| comprehensions             | 19.2 us                                                         | 11.3 us: 1.70x faster                                                          |
| logging_silent             | 101 ns                                                          | 60.3 ns: 1.67x faster                                                          |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.39 ms: 1.62x faster                                                          |
| generators                 | 38.5 ms                                                         | 24.0 ms: 1.61x faster                                                          |
| scimark_fft                | 271 ms                                                          | 174 ms: 1.56x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 59.9 ms: 1.56x faster                                                          |
| deepcopy                   | 360 us                                                          | 233 us: 1.55x faster                                                           |
| pyflate                    | 424 ms                                                          | 274 ms: 1.54x faster                                                           |
| unpack_sequence            | 62.5 ns                                                         | 41.5 ns: 1.51x faster                                                          |
| fannkuch                   | 354 ms                                                          | 238 ms: 1.48x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.50 sec: 1.46x faster                                                         |
| crypto_pyaes               | 69.2 ms                                                         | 47.5 ms: 1.46x faster                                                          |
| hexiom                     | 6.82 ms                                                         | 4.91 ms: 1.39x faster                                                          |
| xml_etree_generate         | 72.1 ms                                                         | 52.7 ms: 1.37x faster                                                          |
| async_tree_none_tg         | 278 ms                                                          | 204 ms: 1.36x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 258 ms: 1.36x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 39.5 ms: 1.35x faster                                                          |
| async_tree_none            | 298 ms                                                          | 223 ms: 1.34x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 49.9 ms: 1.33x faster                                                          |
| go                         | 137 ms                                                          | 103 ms: 1.33x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 281 ms: 1.29x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 524 ms: 1.29x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 164 us: 1.28x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.52 us: 1.28x faster                                                          |
| richards_super             | 46.5 ms                                                         | 36.4 ms: 1.28x faster                                                          |
| chaos                      | 69.4 ms                                                         | 54.6 ms: 1.27x faster                                                          |
| async_tree_io              | 693 ms                                                          | 547 ms: 1.27x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 61.7 ms: 1.26x faster                                                          |
| regex_compile              | 129 ms                                                          | 103 ms: 1.25x faster                                                           |
| richards                   | 41.3 ms                                                         | 33.0 ms: 1.25x faster                                                          |
| raytrace                   | 308 ms                                                          | 248 ms: 1.24x faster                                                           |
| logging_simple             | 9.75 us                                                         | 7.93 us: 1.23x faster                                                          |
| logging_format             | 10.4 us                                                         | 8.56 us: 1.22x faster                                                          |
| dulwich_log                | 58.5 ms                                                         | 48.3 ms: 1.21x faster                                                          |
| pprint_safe_repr           | 721 ms                                                          | 600 ms: 1.20x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 72.7 ms: 1.19x faster                                                          |
| nqueens                    | 93.7 ms                                                         | 78.7 ms: 1.19x faster                                                          |
| sqlglot_parse              | 1.25 ms                                                         | 1.05 ms: 1.19x faster                                                          |
| pprint_pformat             | 1.50 sec                                                        | 1.27 sec: 1.18x faster                                                         |
| pycparser                  | 978 ms                                                          | 839 ms: 1.17x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 485 ms: 1.16x faster                                                           |
| pickle_pure_python         | 286 us                                                          | 247 us: 1.16x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 476 ms: 1.15x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 18.5 ms: 1.13x faster                                                          |
| sqlglot_transpile          | 1.53 ms                                                         | 1.36 ms: 1.13x faster                                                          |
| bench_thread_pool          | 1.10 ms                                                         | 984 us: 1.12x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 82.2 ms: 1.11x faster                                                          |
| json_dumps                 | 7.40 ms                                                         | 6.71 ms: 1.10x faster                                                          |
| 2to3                       | 280 ms                                                          | 257 ms: 1.09x faster                                                           |
| regex_dna                  | 127 ms                                                          | 116 ms: 1.09x faster                                                           |
| xml_etree_parse            | 113 ms                                                          | 104 ms: 1.09x faster                                                           |
| asyncio_tcp                | 662 ms                                                          | 612 ms: 1.08x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 114 ms: 1.08x faster                                                           |
| sympy_str                  | 240 ms                                                          | 222 ms: 1.08x faster                                                           |
| sqlite_synth               | 2.07 us                                                         | 1.94 us: 1.07x faster                                                          |
| tornado_http               | 105 ms                                                          | 99.7 ms: 1.05x faster                                                          |
| django_template            | 36.9 ms                                                         | 35.1 ms: 1.05x faster                                                          |
| sympy_integrate            | 17.5 ms                                                         | 16.8 ms: 1.05x faster                                                          |
| mdp                        | 1.91 sec                                                        | 1.83 sec: 1.04x faster                                                         |
| sqlglot_optimize           | 48.5 ms                                                         | 46.4 ms: 1.04x faster                                                          |
| regex_effbot               | 2.04 ms                                                         | 1.95 ms: 1.04x faster                                                          |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.0 sec: 1.04x faster                                                         |
| json                       | 4.15 ms                                                         | 4.01 ms: 1.04x faster                                                          |
| pickle_list                | 3.37 us                                                         | 3.29 us: 1.02x faster                                                          |
| pidigits                   | 199 ms                                                          | 195 ms: 1.02x faster                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.42 ms: 1.01x faster                                                          |
| bench_mp_pool              | 75.4 ms                                                         | 75.0 ms: 1.01x faster                                                          |
| docutils                   | 1.98 sec                                                        | 2.00 sec: 1.01x slower                                                         |
| sympy_expand               | 398 ms                                                          | 402 ms: 1.01x slower                                                           |
| json_loads                 | 20.4 us                                                         | 20.6 us: 1.01x slower                                                          |
| pickle                     | 7.79 us                                                         | 7.94 us: 1.02x slower                                                          |
| async_generators           | 313 ms                                                          | 320 ms: 1.02x slower                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 19.5 ms: 1.02x slower                                                          |
| regex_v8                   | 15.0 ms                                                         | 15.9 ms: 1.06x slower                                                          |
| python_startup             | 22.4 ms                                                         | 23.7 ms: 1.06x slower                                                          |
| unpickle                   | 9.71 us                                                         | 10.3 us: 1.06x slower                                                          |
| coverage                   | 48.4 ms                                                         | 53.8 ms: 1.11x slower                                                          |
| telco                      | 5.51 ms                                                         | 6.20 ms: 1.13x slower                                                          |
| create_gc_cycles           | 652 us                                                          | 750 us: 1.15x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 151 us: 1.19x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.22x faster                                                                   |

Benchmark hidden because not significant (3): sqlglot_normalize, pickle_dict, unpickle_list
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240914-3.14.0a0-401fff7-JIT/bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: unknown