# Results vs. 3.12.0

- fork: brandtbucher
- ref: nojit
- machine: windows-x86
- commit hash: a6f1035
- commit date: 2024-09-21
- overall geometric mean: 1.129x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 253 ms: 1.11x faster                                                  |
| docutils       | 1.98 sec                                                        | 1.86 sec: 1.06x faster                                                |
| tornado_http   | 105 ms                                                          | 95.1 ms: 1.10x faster                                                 |
| Geometric mean | (ref)                                                           | 1.09x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 250 ms: 1.40x faster                                                  |
| async_tree_none_tg         | 278 ms                                                          | 200 ms: 1.39x faster                                                  |
| async_tree_none            | 298 ms                                                          | 217 ms: 1.37x faster                                                  |
| async_tree_memoization     | 364 ms                                                          | 270 ms: 1.35x faster                                                  |
| async_tree_io_tg           | 677 ms                                                          | 520 ms: 1.30x faster                                                  |
| async_tree_io              | 693 ms                                                          | 540 ms: 1.28x faster                                                  |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 470 ms: 1.20x faster                                                  |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 463 ms: 1.18x faster                                                  |
| Geometric mean             | (ref)                                                           | 1.31x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 90.2 ms: 1.41x faster                                                 |
| float          | 76.7 ms                                                         | 63.2 ms: 1.21x faster                                                 |
| pidigits       | 199 ms                                                          | 197 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                           | 1.20x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 108 ms: 1.19x faster                                                  |
| regex_effbot   | 2.04 ms                                                         | 1.91 ms: 1.07x faster                                                 |
| regex_dna      | 127 ms                                                          | 119 ms: 1.06x faster                                                  |
| regex_v8       | 15.0 ms                                                         | 16.2 ms: 1.08x slower                                                 |
| Geometric mean | (ref)                                                           | 1.06x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.84 sec: 1.19x faster                                                |
| unpickle_pure_python | 210 us                                                          | 182 us: 1.15x faster                                                  |
| xml_etree_iterparse  | 77.6 ms                                                         | 68.9 ms: 1.13x faster                                                 |
| pickle_pure_python   | 286 us                                                          | 260 us: 1.10x faster                                                  |
| xml_etree_process    | 53.2 ms                                                         | 48.6 ms: 1.09x faster                                                 |
| xml_etree_generate   | 72.1 ms                                                         | 67.0 ms: 1.08x faster                                                 |
| xml_etree_parse      | 113 ms                                                          | 108 ms: 1.05x faster                                                  |
| unpickle_list        | 2.95 us                                                         | 2.85 us: 1.03x faster                                                 |
| json_loads           | 20.4 us                                                         | 20.6 us: 1.01x slower                                                 |
| json_dumps           | 7.40 ms                                                         | 7.57 ms: 1.02x slower                                                 |
| pickle               | 7.79 us                                                         | 8.03 us: 1.03x slower                                                 |
| pickle_dict          | 19.9 us                                                         | 20.6 us: 1.03x slower                                                 |
| unpickle             | 9.71 us                                                         | 10.2 us: 1.05x slower                                                 |
| Geometric mean       | (ref)                                                           | 1.04x faster                                                          |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.6 ms: 1.03x slower                                                 |
| python_startup         | 22.4 ms                                                         | 23.7 ms: 1.06x slower                                                 |
| Geometric mean         | (ref)                                                           | 1.04x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 8.30 ms: 1.20x faster                                                 |
| django_template | 36.9 ms                                                         | 32.1 ms: 1.15x faster                                                 |
| Geometric mean  | (ref)                                                           | 1.17x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 23.1 us: 1.66x faster                                                 |
| deepcopy                   | 360 us                                                          | 249 us: 1.45x faster                                                  |
| generators                 | 38.5 ms                                                         | 27.2 ms: 1.42x faster                                                 |
| nbody                      | 127 ms                                                          | 90.2 ms: 1.41x faster                                                 |
| async_tree_memoization_tg  | 350 ms                                                          | 250 ms: 1.40x faster                                                  |
| async_tree_none_tg         | 278 ms                                                          | 200 ms: 1.39x faster                                                  |
| async_tree_none            | 298 ms                                                          | 217 ms: 1.37x faster                                                  |
| unpack_sequence            | 62.5 ns                                                         | 46.1 ns: 1.36x faster                                                 |
| async_tree_memoization     | 364 ms                                                          | 270 ms: 1.35x faster                                                  |
| logging_silent             | 101 ns                                                          | 75.2 ns: 1.34x faster                                                 |
| deepcopy_reduce            | 3.23 us                                                         | 2.42 us: 1.33x faster                                                 |
| comprehensions             | 19.2 us                                                         | 14.6 us: 1.32x faster                                                 |
| async_tree_io_tg           | 677 ms                                                          | 520 ms: 1.30x faster                                                  |
| scimark_lu                 | 93.2 ms                                                         | 71.7 ms: 1.30x faster                                                 |
| raytrace                   | 308 ms                                                          | 237 ms: 1.30x faster                                                  |
| async_tree_io              | 693 ms                                                          | 540 ms: 1.28x faster                                                  |
| hexiom                     | 6.82 ms                                                         | 5.33 ms: 1.28x faster                                                 |
| deltablue                  | 3.58 ms                                                         | 2.82 ms: 1.27x faster                                                 |
| chaos                      | 69.4 ms                                                         | 54.6 ms: 1.27x faster                                                 |
| spectral_norm              | 104 ms                                                          | 82.1 ms: 1.26x faster                                                 |
| go                         | 137 ms                                                          | 109 ms: 1.26x faster                                                  |
| scimark_sor                | 130 ms                                                          | 105 ms: 1.24x faster                                                  |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.13 ms: 1.23x faster                                                 |
| float                      | 76.7 ms                                                         | 63.2 ms: 1.21x faster                                                 |
| logging_simple             | 9.75 us                                                         | 8.09 us: 1.21x faster                                                 |
| mako                       | 9.96 ms                                                         | 8.30 ms: 1.20x faster                                                 |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 470 ms: 1.20x faster                                                  |
| nqueens                    | 93.7 ms                                                         | 78.2 ms: 1.20x faster                                                 |
| crypto_pyaes               | 69.2 ms                                                         | 57.9 ms: 1.19x faster                                                 |
| regex_compile              | 129 ms                                                          | 108 ms: 1.19x faster                                                  |
| tomli_loads                | 2.20 sec                                                        | 1.84 sec: 1.19x faster                                                |
| logging_format             | 10.4 us                                                         | 8.76 us: 1.19x faster                                                 |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 463 ms: 1.18x faster                                                  |
| pyflate                    | 424 ms                                                          | 364 ms: 1.17x faster                                                  |
| unpickle_pure_python       | 210 us                                                          | 182 us: 1.15x faster                                                  |
| dulwich_log                | 58.5 ms                                                         | 50.8 ms: 1.15x faster                                                 |
| django_template            | 36.9 ms                                                         | 32.1 ms: 1.15x faster                                                 |
| scimark_fft                | 271 ms                                                          | 236 ms: 1.15x faster                                                  |
| pycparser                  | 978 ms                                                          | 854 ms: 1.14x faster                                                  |
| pprint_pformat             | 1.50 sec                                                        | 1.32 sec: 1.14x faster                                                |
| sympy_sum                  | 123 ms                                                          | 108 ms: 1.14x faster                                                  |
| sympy_integrate            | 17.5 ms                                                         | 15.5 ms: 1.13x faster                                                 |
| scimark_monte_carlo        | 66.4 ms                                                         | 58.6 ms: 1.13x faster                                                 |
| sqlglot_parse              | 1.25 ms                                                         | 1.10 ms: 1.13x faster                                                 |
| pprint_safe_repr           | 721 ms                                                          | 636 ms: 1.13x faster                                                  |
| xml_etree_iterparse        | 77.6 ms                                                         | 68.9 ms: 1.13x faster                                                 |
| sqlglot_transpile          | 1.53 ms                                                         | 1.36 ms: 1.13x faster                                                 |
| coroutines                 | 20.9 ms                                                         | 18.7 ms: 1.12x faster                                                 |
| sqlglot_optimize           | 48.5 ms                                                         | 43.4 ms: 1.12x faster                                                 |
| 2to3                       | 280 ms                                                          | 253 ms: 1.11x faster                                                  |
| sympy_str                  | 240 ms                                                          | 217 ms: 1.11x faster                                                  |
| tornado_http               | 105 ms                                                          | 95.1 ms: 1.10x faster                                                 |
| pickle_pure_python         | 286 us                                                          | 260 us: 1.10x faster                                                  |
| xml_etree_process          | 53.2 ms                                                         | 48.6 ms: 1.09x faster                                                 |
| pathlib                    | 91.4 ms                                                         | 83.8 ms: 1.09x faster                                                 |
| bench_thread_pool          | 1.10 ms                                                         | 1.02 ms: 1.08x faster                                                 |
| mdp                        | 1.91 sec                                                        | 1.77 sec: 1.08x faster                                                |
| xml_etree_generate         | 72.1 ms                                                         | 67.0 ms: 1.08x faster                                                 |
| regex_effbot               | 2.04 ms                                                         | 1.91 ms: 1.07x faster                                                 |
| regex_dna                  | 127 ms                                                          | 119 ms: 1.06x faster                                                  |
| docutils                   | 1.98 sec                                                        | 1.86 sec: 1.06x faster                                                |
| meteor_contest             | 86.9 ms                                                         | 81.8 ms: 1.06x faster                                                 |
| sqlite_synth               | 2.07 us                                                         | 1.95 us: 1.06x faster                                                 |
| xml_etree_parse            | 113 ms                                                          | 108 ms: 1.05x faster                                                  |
| sympy_expand               | 398 ms                                                          | 380 ms: 1.05x faster                                                  |
| bench_mp_pool              | 75.4 ms                                                         | 72.2 ms: 1.04x faster                                                 |
| fannkuch                   | 354 ms                                                          | 341 ms: 1.04x faster                                                  |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.1 sec: 1.03x faster                                                |
| unpickle_list              | 2.95 us                                                         | 2.85 us: 1.03x faster                                                 |
| gc_traversal               | 1.44 ms                                                         | 1.41 ms: 1.02x faster                                                 |
| richards_super             | 46.5 ms                                                         | 45.6 ms: 1.02x faster                                                 |
| richards                   | 41.3 ms                                                         | 40.5 ms: 1.02x faster                                                 |
| async_generators           | 313 ms                                                          | 307 ms: 1.02x faster                                                  |
| pidigits                   | 199 ms                                                          | 197 ms: 1.01x faster                                                  |
| json_loads                 | 20.4 us                                                         | 20.6 us: 1.01x slower                                                 |
| json_dumps                 | 7.40 ms                                                         | 7.57 ms: 1.02x slower                                                 |
| python_startup_no_site     | 19.1 ms                                                         | 19.6 ms: 1.03x slower                                                 |
| pickle                     | 7.79 us                                                         | 8.03 us: 1.03x slower                                                 |
| pickle_dict                | 19.9 us                                                         | 20.6 us: 1.03x slower                                                 |
| unpickle                   | 9.71 us                                                         | 10.2 us: 1.05x slower                                                 |
| python_startup             | 22.4 ms                                                         | 23.7 ms: 1.06x slower                                                 |
| regex_v8                   | 15.0 ms                                                         | 16.2 ms: 1.08x slower                                                 |
| coverage                   | 48.4 ms                                                         | 53.2 ms: 1.10x slower                                                 |
| typing_runtime_protocols   | 126 us                                                          | 142 us: 1.12x slower                                                  |
| create_gc_cycles           | 652 us                                                          | 735 us: 1.13x slower                                                  |
| telco                      | 5.51 ms                                                         | 6.54 ms: 1.19x slower                                                 |
| sqlglot_normalize          | 100 ms                                                          | 230 ms: 2.29x slower                                                  |
| Geometric mean             | (ref)                                                           | 1.12x faster                                                          |

Benchmark hidden because not significant (3): json, pickle_list, asyncio_tcp
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240921-3.14.0a0-a6f1035/bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035.json: genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.129x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown