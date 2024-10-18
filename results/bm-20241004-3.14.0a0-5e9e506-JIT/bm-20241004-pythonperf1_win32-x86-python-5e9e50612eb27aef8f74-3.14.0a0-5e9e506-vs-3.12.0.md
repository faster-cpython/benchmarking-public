# Results vs. 3.12.0

- fork: python
- ref: 5e9e50612eb27aef8f74
- machine: windows-x86
- commit hash: 5e9e506
- commit date: 2024-10-04
- overall geometric mean: 1.19x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-pythonperf1_win32-x86-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 261 ms: 1.07x faster                                                           |
| docutils       | 1.98 sec                                                        | 2.04 sec: 1.03x slower                                                         |
| tornado_http   | 105 ms                                                          | 109 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                           | 1.00x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-pythonperf1_win32-x86-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none_tg         | 278 ms                                                          | 201 ms: 1.38x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 255 ms: 1.37x faster                                                           |
| async_tree_none            | 298 ms                                                          | 223 ms: 1.34x faster                                                           |
| async_tree_io              | 693 ms                                                          | 524 ms: 1.32x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 514 ms: 1.32x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 279 ms: 1.30x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 468 ms: 1.20x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 467 ms: 1.17x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.30x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-pythonperf1_win32-x86-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 50.4 ms: 2.52x faster                                                          |
| float          | 76.7 ms                                                         | 46.2 ms: 1.66x faster                                                          |
| pidigits       | 199 ms                                                          | 199 ms: 1.00x faster                                                           |
| Geometric mean | (ref)                                                           | 1.61x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-pythonperf1_win32-x86-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 105 ms: 1.23x faster                                                           |
| regex_effbot   | 2.04 ms                                                         | 1.81 ms: 1.13x faster                                                          |
| regex_dna      | 127 ms                                                          | 116 ms: 1.09x faster                                                           |
| regex_v8       | 15.0 ms                                                         | 15.3 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                           | 1.11x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-pythonperf1_win32-x86-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.51 sec: 1.45x faster                                                         |
| unpickle_pure_python | 210 us                                                          | 158 us: 1.33x faster                                                           |
| xml_etree_generate   | 72.1 ms                                                         | 54.7 ms: 1.32x faster                                                          |
| xml_etree_process    | 53.2 ms                                                         | 41.5 ms: 1.28x faster                                                          |
| xml_etree_iterparse  | 77.6 ms                                                         | 64.5 ms: 1.20x faster                                                          |
| pickle_pure_python   | 286 us                                                          | 242 us: 1.18x faster                                                           |
| json_dumps           | 7.40 ms                                                         | 6.98 ms: 1.06x faster                                                          |
| xml_etree_parse      | 113 ms                                                          | 109 ms: 1.03x faster                                                           |
| pickle_list          | 3.37 us                                                         | 3.47 us: 1.03x slower                                                          |
| json_loads           | 20.4 us                                                         | 21.0 us: 1.03x slower                                                          |
| unpickle             | 9.71 us                                                         | 10.4 us: 1.07x slower                                                          |
| pickle_dict          | 19.9 us                                                         | 21.3 us: 1.07x slower                                                          |
| pickle               | 7.79 us                                                         | 8.37 us: 1.07x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.10x faster                                                                   |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-pythonperf1_win32-x86-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.5 ms: 1.07x slower                                                          |
| python_startup         | 22.4 ms                                                         | 26.8 ms: 1.20x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.13x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-pythonperf1_win32-x86-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.57 ms: 1.79x faster                                                          |
| django_template | 36.9 ms                                                         | 32.0 ms: 1.15x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.44x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-pythonperf1_win32-x86-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody                      | 127 ms                                                          | 50.4 ms: 2.52x faster                                                          |
| deepcopy_memo              | 38.4 us                                                         | 16.0 us: 2.41x faster                                                          |
| scimark_sor                | 130 ms                                                          | 68.5 ms: 1.89x faster                                                          |
| mako                       | 9.96 ms                                                         | 5.57 ms: 1.79x faster                                                          |
| spectral_norm              | 104 ms                                                          | 58.4 ms: 1.78x faster                                                          |
| logging_silent             | 101 ns                                                          | 58.6 ns: 1.72x faster                                                          |
| scimark_monte_carlo        | 66.4 ms                                                         | 39.0 ms: 1.70x faster                                                          |
| float                      | 76.7 ms                                                         | 46.2 ms: 1.66x faster                                                          |
| scimark_lu                 | 93.2 ms                                                         | 59.1 ms: 1.58x faster                                                          |
| comprehensions             | 19.2 us                                                         | 12.3 us: 1.56x faster                                                          |
| unpack_sequence            | 62.5 ns                                                         | 40.5 ns: 1.54x faster                                                          |
| deepcopy                   | 360 us                                                          | 234 us: 1.54x faster                                                           |
| scimark_fft                | 271 ms                                                          | 177 ms: 1.53x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.60 ms: 1.48x faster                                                          |
| tomli_loads                | 2.20 sec                                                        | 1.51 sec: 1.45x faster                                                         |
| fannkuch                   | 354 ms                                                          | 245 ms: 1.44x faster                                                           |
| generators                 | 38.5 ms                                                         | 27.1 ms: 1.42x faster                                                          |
| go                         | 137 ms                                                          | 97.1 ms: 1.41x faster                                                          |
| async_tree_none_tg         | 278 ms                                                          | 201 ms: 1.38x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 255 ms: 1.37x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.63 ms: 1.36x faster                                                          |
| crypto_pyaes               | 69.2 ms                                                         | 51.2 ms: 1.35x faster                                                          |
| async_tree_none            | 298 ms                                                          | 223 ms: 1.34x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.43 us: 1.33x faster                                                          |
| unpickle_pure_python       | 210 us                                                          | 158 us: 1.33x faster                                                           |
| chaos                      | 69.4 ms                                                         | 52.4 ms: 1.32x faster                                                          |
| async_tree_io              | 693 ms                                                          | 524 ms: 1.32x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 54.7 ms: 1.32x faster                                                          |
| async_tree_io_tg           | 677 ms                                                          | 514 ms: 1.32x faster                                                           |
| pyflate                    | 424 ms                                                          | 325 ms: 1.31x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 279 ms: 1.30x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 41.5 ms: 1.28x faster                                                          |
| pprint_safe_repr           | 721 ms                                                          | 565 ms: 1.27x faster                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.18 sec: 1.27x faster                                                         |
| nqueens                    | 93.7 ms                                                         | 73.9 ms: 1.27x faster                                                          |
| hexiom                     | 6.82 ms                                                         | 5.48 ms: 1.25x faster                                                          |
| regex_compile              | 129 ms                                                          | 105 ms: 1.23x faster                                                           |
| logging_format             | 10.4 us                                                         | 8.52 us: 1.22x faster                                                          |
| logging_simple             | 9.75 us                                                         | 8.02 us: 1.22x faster                                                          |
| raytrace                   | 308 ms                                                          | 255 ms: 1.21x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 468 ms: 1.20x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 64.5 ms: 1.20x faster                                                          |
| coroutines                 | 20.9 ms                                                         | 17.5 ms: 1.19x faster                                                          |
| pycparser                  | 978 ms                                                          | 822 ms: 1.19x faster                                                           |
| pickle_pure_python         | 286 us                                                          | 242 us: 1.18x faster                                                           |
| dulwich_log                | 58.5 ms                                                         | 49.8 ms: 1.17x faster                                                          |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 467 ms: 1.17x faster                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 1.07 ms: 1.17x faster                                                          |
| meteor_contest             | 86.9 ms                                                         | 75.0 ms: 1.16x faster                                                          |
| django_template            | 36.9 ms                                                         | 32.0 ms: 1.15x faster                                                          |
| regex_effbot               | 2.04 ms                                                         | 1.81 ms: 1.13x faster                                                          |
| mdp                        | 1.91 sec                                                        | 1.70 sec: 1.12x faster                                                         |
| sqlglot_transpile          | 1.53 ms                                                         | 1.37 ms: 1.12x faster                                                          |
| sqlite_synth               | 2.07 us                                                         | 1.89 us: 1.10x faster                                                          |
| regex_dna                  | 127 ms                                                          | 116 ms: 1.09x faster                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 1.02 ms: 1.08x faster                                                          |
| 2to3                       | 280 ms                                                          | 261 ms: 1.07x faster                                                           |
| json_dumps                 | 7.40 ms                                                         | 6.98 ms: 1.06x faster                                                          |
| sympy_str                  | 240 ms                                                          | 227 ms: 1.06x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 117 ms: 1.05x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 87.8 ms: 1.04x faster                                                          |
| richards                   | 41.3 ms                                                         | 39.9 ms: 1.04x faster                                                          |
| xml_etree_parse            | 113 ms                                                          | 109 ms: 1.03x faster                                                           |
| richards_super             | 46.5 ms                                                         | 45.2 ms: 1.03x faster                                                          |
| sympy_integrate            | 17.5 ms                                                         | 17.1 ms: 1.02x faster                                                          |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.3 sec: 1.02x faster                                                         |
| sympy_expand               | 398 ms                                                          | 394 ms: 1.01x faster                                                           |
| pidigits                   | 199 ms                                                          | 199 ms: 1.00x faster                                                           |
| regex_v8                   | 15.0 ms                                                         | 15.3 ms: 1.01x slower                                                          |
| json                       | 4.15 ms                                                         | 4.22 ms: 1.02x slower                                                          |
| sqlglot_normalize          | 100 ms                                                          | 102 ms: 1.02x slower                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 49.7 ms: 1.03x slower                                                          |
| docutils                   | 1.98 sec                                                        | 2.04 sec: 1.03x slower                                                         |
| pickle_list                | 3.37 us                                                         | 3.47 us: 1.03x slower                                                          |
| json_loads                 | 20.4 us                                                         | 21.0 us: 1.03x slower                                                          |
| tornado_http               | 105 ms                                                          | 109 ms: 1.04x slower                                                           |
| async_generators           | 313 ms                                                          | 326 ms: 1.04x slower                                                           |
| unpickle                   | 9.71 us                                                         | 10.4 us: 1.07x slower                                                          |
| pickle_dict                | 19.9 us                                                         | 21.3 us: 1.07x slower                                                          |
| pickle                     | 7.79 us                                                         | 8.37 us: 1.07x slower                                                          |
| python_startup_no_site     | 19.1 ms                                                         | 20.5 ms: 1.07x slower                                                          |
| typing_runtime_protocols   | 126 us                                                          | 139 us: 1.10x slower                                                           |
| coverage                   | 48.4 ms                                                         | 53.5 ms: 1.10x slower                                                          |
| asyncio_tcp                | 662 ms                                                          | 771 ms: 1.16x slower                                                           |
| telco                      | 5.51 ms                                                         | 6.42 ms: 1.17x slower                                                          |
| python_startup             | 22.4 ms                                                         | 26.8 ms: 1.20x slower                                                          |
| gc_traversal               | 1.44 ms                                                         | 1.78 ms: 1.23x slower                                                          |
| bench_mp_pool              | 75.4 ms                                                         | 94.3 ms: 1.25x slower                                                          |
| create_gc_cycles           | 652 us                                                          | 1.16 ms: 1.78x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.19x faster                                                                   |

Benchmark hidden because not significant (1): unpickle_list
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241004-3.14.0a0-5e9e506-JIT/bm-20241004-pythonperf1_win32-x86-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506.json: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown