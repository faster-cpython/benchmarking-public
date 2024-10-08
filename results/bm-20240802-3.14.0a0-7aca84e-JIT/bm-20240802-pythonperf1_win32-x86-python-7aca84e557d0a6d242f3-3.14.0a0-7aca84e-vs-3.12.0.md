# Results vs. 3.12.0

- fork: python
- ref: 7aca84e557d0a6d242f3
- machine: windows-x86
- commit hash: 7aca84e
- commit date: 2024-08-02
- overall geometric mean: 1.22x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 261 ms: 1.07x faster                                                           |
| tornado_http   | 105 ms                                                          | 107 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                   |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none_tg         | 278 ms                                                          | 197 ms: 1.41x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 253 ms: 1.38x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 506 ms: 1.34x faster                                                           |
| async_tree_none            | 298 ms                                                          | 229 ms: 1.30x faster                                                           |
| async_tree_io              | 693 ms                                                          | 546 ms: 1.27x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 288 ms: 1.26x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 458 ms: 1.19x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 479 ms: 1.18x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.29x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 52.6 ms: 2.41x faster                                                          |
| float          | 76.7 ms                                                         | 42.5 ms: 1.80x faster                                                          |
| pidigits       | 199 ms                                                          | 196 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                           | 1.64x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 96.1 ms: 1.34x faster                                                          |
| regex_dna      | 127 ms                                                          | 120 ms: 1.06x faster                                                           |
| regex_v8       | 15.0 ms                                                         | 16.1 ms: 1.07x slower                                                          |
| Geometric mean | (ref)                                                           | 1.08x faster                                                                   |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 147 us: 1.43x faster                                                           |
| tomli_loads          | 2.20 sec                                                        | 1.54 sec: 1.43x faster                                                         |
| pickle_pure_python   | 286 us                                                          | 213 us: 1.35x faster                                                           |
| xml_etree_iterparse  | 77.6 ms                                                         | 63.9 ms: 1.22x faster                                                          |
| xml_etree_generate   | 72.1 ms                                                         | 59.6 ms: 1.21x faster                                                          |
| xml_etree_process    | 53.2 ms                                                         | 44.9 ms: 1.18x faster                                                          |
| xml_etree_parse      | 113 ms                                                          | 107 ms: 1.06x faster                                                           |
| json_dumps           | 7.40 ms                                                         | 7.05 ms: 1.05x faster                                                          |
| json_loads           | 20.4 us                                                         | 21.1 us: 1.04x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.20x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.8 ms: 1.09x slower                                                          |
| python_startup         | 22.4 ms                                                         | 24.8 ms: 1.11x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.43 ms: 1.83x faster                                                          |
| django_template | 36.9 ms                                                         | 32.8 ms: 1.13x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.44x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody                      | 127 ms                                                          | 52.6 ms: 2.41x faster                                                          |
| deepcopy_memo              | 38.4 us                                                         | 16.4 us: 2.34x faster                                                          |
| spectral_norm              | 104 ms                                                          | 47.9 ms: 2.17x faster                                                          |
| scimark_sor                | 130 ms                                                          | 67.0 ms: 1.94x faster                                                          |
| mako                       | 9.96 ms                                                         | 5.43 ms: 1.83x faster                                                          |
| float                      | 76.7 ms                                                         | 42.5 ms: 1.80x faster                                                          |
| logging_silent             | 101 ns                                                          | 58.2 ns: 1.74x faster                                                          |
| comprehensions             | 19.2 us                                                         | 11.5 us: 1.67x faster                                                          |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.32 ms: 1.66x faster                                                          |
| scimark_fft                | 271 ms                                                          | 168 ms: 1.61x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 41.8 ms: 1.59x faster                                                          |
| pyflate                    | 424 ms                                                          | 269 ms: 1.58x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 59.7 ms: 1.56x faster                                                          |
| generators                 | 38.5 ms                                                         | 24.7 ms: 1.56x faster                                                          |
| fannkuch                   | 354 ms                                                          | 227 ms: 1.56x faster                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 46.9 ms: 1.47x faster                                                          |
| unpickle_pure_python       | 210 us                                                          | 147 us: 1.43x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.54 sec: 1.43x faster                                                         |
| deepcopy                   | 360 us                                                          | 254 us: 1.42x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 4.84 ms: 1.41x faster                                                          |
| async_tree_none_tg         | 278 ms                                                          | 197 ms: 1.41x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 253 ms: 1.38x faster                                                           |
| raytrace                   | 308 ms                                                          | 227 ms: 1.36x faster                                                           |
| pickle_pure_python         | 286 us                                                          | 213 us: 1.35x faster                                                           |
| chaos                      | 69.4 ms                                                         | 51.6 ms: 1.34x faster                                                          |
| regex_compile              | 129 ms                                                          | 96.1 ms: 1.34x faster                                                          |
| async_tree_io_tg           | 677 ms                                                          | 506 ms: 1.34x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.75 ms: 1.30x faster                                                          |
| async_tree_none            | 298 ms                                                          | 229 ms: 1.30x faster                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 973 us: 1.28x faster                                                           |
| logging_simple             | 9.75 us                                                         | 7.62 us: 1.28x faster                                                          |
| async_tree_io              | 693 ms                                                          | 546 ms: 1.27x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.54 us: 1.27x faster                                                          |
| async_tree_memoization     | 364 ms                                                          | 288 ms: 1.26x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 69.0 ms: 1.26x faster                                                          |
| pprint_pformat             | 1.50 sec                                                        | 1.20 sec: 1.25x faster                                                         |
| logging_format             | 10.4 us                                                         | 8.36 us: 1.24x faster                                                          |
| pycparser                  | 978 ms                                                          | 793 ms: 1.23x faster                                                           |
| pprint_safe_repr           | 721 ms                                                          | 586 ms: 1.23x faster                                                           |
| sqlglot_transpile          | 1.53 ms                                                         | 1.25 ms: 1.22x faster                                                          |
| xml_etree_iterparse        | 77.6 ms                                                         | 63.9 ms: 1.22x faster                                                          |
| nqueens                    | 93.7 ms                                                         | 77.2 ms: 1.21x faster                                                          |
| xml_etree_generate         | 72.1 ms                                                         | 59.6 ms: 1.21x faster                                                          |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 458 ms: 1.19x faster                                                           |
| go                         | 137 ms                                                          | 115 ms: 1.19x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 44.9 ms: 1.18x faster                                                          |
| richards                   | 41.3 ms                                                         | 35.1 ms: 1.18x faster                                                          |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 479 ms: 1.18x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 17.8 ms: 1.17x faster                                                          |
| dulwich_log                | 58.5 ms                                                         | 50.2 ms: 1.17x faster                                                          |
| mdp                        | 1.91 sec                                                        | 1.69 sec: 1.13x faster                                                         |
| django_template            | 36.9 ms                                                         | 32.8 ms: 1.13x faster                                                          |
| richards_super             | 46.5 ms                                                         | 41.7 ms: 1.11x faster                                                          |
| sympy_sum                  | 123 ms                                                          | 112 ms: 1.09x faster                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 1.02 ms: 1.08x faster                                                          |
| sympy_str                  | 240 ms                                                          | 222 ms: 1.08x faster                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 44.9 ms: 1.08x faster                                                          |
| 2to3                       | 280 ms                                                          | 261 ms: 1.07x faster                                                           |
| sympy_integrate            | 17.5 ms                                                         | 16.6 ms: 1.06x faster                                                          |
| xml_etree_parse            | 113 ms                                                          | 107 ms: 1.06x faster                                                           |
| regex_dna                  | 127 ms                                                          | 120 ms: 1.06x faster                                                           |
| json_dumps                 | 7.40 ms                                                         | 7.05 ms: 1.05x faster                                                          |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.1 sec: 1.03x faster                                                         |
| pathlib                    | 91.4 ms                                                         | 88.7 ms: 1.03x faster                                                          |
| pidigits                   | 199 ms                                                          | 196 ms: 1.02x faster                                                           |
| sympy_expand               | 398 ms                                                          | 394 ms: 1.01x faster                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.46 ms: 1.01x slower                                                          |
| tornado_http               | 105 ms                                                          | 107 ms: 1.02x slower                                                           |
| async_generators           | 313 ms                                                          | 320 ms: 1.02x slower                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 77.3 ms: 1.02x slower                                                          |
| json_loads                 | 20.4 us                                                         | 21.1 us: 1.04x slower                                                          |
| json                       | 4.15 ms                                                         | 4.43 ms: 1.07x slower                                                          |
| coverage                   | 48.4 ms                                                         | 51.8 ms: 1.07x slower                                                          |
| regex_v8                   | 15.0 ms                                                         | 16.1 ms: 1.07x slower                                                          |
| telco                      | 5.51 ms                                                         | 6.01 ms: 1.09x slower                                                          |
| python_startup_no_site     | 19.1 ms                                                         | 20.8 ms: 1.09x slower                                                          |
| python_startup             | 22.4 ms                                                         | 24.8 ms: 1.11x slower                                                          |
| asyncio_tcp                | 662 ms                                                          | 782 ms: 1.18x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 771 us: 1.18x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 153 us: 1.22x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 232 ms: 2.32x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.22x faster                                                                   |

Benchmark hidden because not significant (2): regex_effbot, docutils
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240802-3.14.0a0-7aca84e-JIT/bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: unknown