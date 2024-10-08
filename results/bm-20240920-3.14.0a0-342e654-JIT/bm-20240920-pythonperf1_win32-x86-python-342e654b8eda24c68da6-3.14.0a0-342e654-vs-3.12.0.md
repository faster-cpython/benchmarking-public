# Results vs. 3.12.0

- fork: python
- ref: 342e654b8eda24c68da6
- machine: windows-x86
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.22x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 258 ms: 1.09x faster                                                           |
| docutils       | 1.98 sec                                                        | 1.97 sec: 1.01x faster                                                         |
| tornado_http   | 105 ms                                                          | 100 ms: 1.04x faster                                                           |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none_tg         | 278 ms                                                          | 201 ms: 1.38x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 255 ms: 1.37x faster                                                           |
| async_tree_none            | 298 ms                                                          | 221 ms: 1.35x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 275 ms: 1.32x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 521 ms: 1.30x faster                                                           |
| async_tree_io              | 693 ms                                                          | 541 ms: 1.28x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 472 ms: 1.20x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 468 ms: 1.17x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.29x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 50.5 ms: 2.52x faster                                                          |
| float          | 76.7 ms                                                         | 43.5 ms: 1.76x faster                                                          |
| pidigits       | 199 ms                                                          | 199 ms: 1.00x faster                                                           |
| Geometric mean | (ref)                                                           | 1.64x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 102 ms: 1.27x faster                                                           |
| regex_dna      | 127 ms                                                          | 119 ms: 1.07x faster                                                           |
| regex_effbot   | 2.04 ms                                                         | 1.97 ms: 1.03x faster                                                          |
| regex_v8       | 15.0 ms                                                         | 15.8 ms: 1.05x slower                                                          |
| Geometric mean | (ref)                                                           | 1.07x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.53 sec: 1.44x faster                                                         |
| xml_etree_generate   | 72.1 ms                                                         | 53.5 ms: 1.35x faster                                                          |
| xml_etree_process    | 53.2 ms                                                         | 39.7 ms: 1.34x faster                                                          |
| unpickle_pure_python | 210 us                                                          | 163 us: 1.29x faster                                                           |
| xml_etree_iterparse  | 77.6 ms                                                         | 60.9 ms: 1.28x faster                                                          |
| pickle_pure_python   | 286 us                                                          | 242 us: 1.18x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 103 ms: 1.10x faster                                                           |
| unpickle_list        | 2.95 us                                                         | 2.78 us: 1.06x faster                                                          |
| json_dumps           | 7.40 ms                                                         | 7.03 ms: 1.05x faster                                                          |
| pickle_list          | 3.37 us                                                         | 3.31 us: 1.02x faster                                                          |
| pickle               | 7.79 us                                                         | 7.93 us: 1.02x slower                                                          |
| json_loads           | 20.4 us                                                         | 21.4 us: 1.05x slower                                                          |
| unpickle             | 9.71 us                                                         | 10.4 us: 1.07x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.13x faster                                                                   |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.1 ms: 1.05x slower                                                          |
| python_startup         | 22.4 ms                                                         | 24.0 ms: 1.07x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.06x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.47 ms: 1.82x faster                                                          |
| django_template | 36.9 ms                                                         | 34.0 ms: 1.08x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.40x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 15.2 us: 2.53x faster                                                          |
| nbody                      | 127 ms                                                          | 50.5 ms: 2.52x faster                                                          |
| spectral_norm              | 104 ms                                                          | 46.6 ms: 2.23x faster                                                          |
| scimark_sor                | 130 ms                                                          | 68.0 ms: 1.91x faster                                                          |
| mako                       | 9.96 ms                                                         | 5.47 ms: 1.82x faster                                                          |
| deltablue                  | 3.58 ms                                                         | 2.02 ms: 1.77x faster                                                          |
| float                      | 76.7 ms                                                         | 43.5 ms: 1.76x faster                                                          |
| logging_silent             | 101 ns                                                          | 59.7 ns: 1.69x faster                                                          |
| comprehensions             | 19.2 us                                                         | 11.6 us: 1.66x faster                                                          |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.36 ms: 1.63x faster                                                          |
| generators                 | 38.5 ms                                                         | 23.8 ms: 1.62x faster                                                          |
| scimark_lu                 | 93.2 ms                                                         | 60.0 ms: 1.55x faster                                                          |
| scimark_fft                | 271 ms                                                          | 175 ms: 1.55x faster                                                           |
| deepcopy                   | 360 us                                                          | 233 us: 1.54x faster                                                           |
| unpack_sequence            | 62.5 ns                                                         | 41.4 ns: 1.51x faster                                                          |
| pyflate                    | 424 ms                                                          | 282 ms: 1.50x faster                                                           |
| fannkuch                   | 354 ms                                                          | 237 ms: 1.49x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.53 sec: 1.44x faster                                                         |
| crypto_pyaes               | 69.2 ms                                                         | 48.4 ms: 1.43x faster                                                          |
| hexiom                     | 6.82 ms                                                         | 4.86 ms: 1.40x faster                                                          |
| async_tree_none_tg         | 278 ms                                                          | 201 ms: 1.38x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 255 ms: 1.37x faster                                                           |
| go                         | 137 ms                                                          | 102 ms: 1.35x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 53.5 ms: 1.35x faster                                                          |
| async_tree_none            | 298 ms                                                          | 221 ms: 1.35x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 39.7 ms: 1.34x faster                                                          |
| async_tree_memoization     | 364 ms                                                          | 275 ms: 1.32x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 50.4 ms: 1.32x faster                                                          |
| chaos                      | 69.4 ms                                                         | 53.3 ms: 1.30x faster                                                          |
| async_tree_io_tg           | 677 ms                                                          | 521 ms: 1.30x faster                                                           |
| richards_super             | 46.5 ms                                                         | 35.9 ms: 1.29x faster                                                          |
| unpickle_pure_python       | 210 us                                                          | 163 us: 1.29x faster                                                           |
| async_tree_io              | 693 ms                                                          | 541 ms: 1.28x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 60.9 ms: 1.28x faster                                                          |
| deepcopy_reduce            | 3.23 us                                                         | 2.53 us: 1.27x faster                                                          |
| regex_compile              | 129 ms                                                          | 102 ms: 1.27x faster                                                           |
| logging_simple             | 9.75 us                                                         | 7.72 us: 1.26x faster                                                          |
| raytrace                   | 308 ms                                                          | 244 ms: 1.26x faster                                                           |
| richards                   | 41.3 ms                                                         | 32.8 ms: 1.26x faster                                                          |
| logging_format             | 10.4 us                                                         | 8.34 us: 1.25x faster                                                          |
| nqueens                    | 93.7 ms                                                         | 76.2 ms: 1.23x faster                                                          |
| meteor_contest             | 86.9 ms                                                         | 71.8 ms: 1.21x faster                                                          |
| pprint_safe_repr           | 721 ms                                                          | 598 ms: 1.20x faster                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 1.04 ms: 1.20x faster                                                          |
| pprint_pformat             | 1.50 sec                                                        | 1.25 sec: 1.20x faster                                                         |
| dulwich_log                | 58.5 ms                                                         | 48.8 ms: 1.20x faster                                                          |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 472 ms: 1.20x faster                                                           |
| pycparser                  | 978 ms                                                          | 825 ms: 1.19x faster                                                           |
| pickle_pure_python         | 286 us                                                          | 242 us: 1.18x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 468 ms: 1.17x faster                                                           |
| sqlglot_transpile          | 1.53 ms                                                         | 1.33 ms: 1.15x faster                                                          |
| coroutines                 | 20.9 ms                                                         | 18.1 ms: 1.15x faster                                                          |
| mdp                        | 1.91 sec                                                        | 1.69 sec: 1.13x faster                                                         |
| xml_etree_parse            | 113 ms                                                          | 103 ms: 1.10x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 83.1 ms: 1.10x faster                                                          |
| bench_thread_pool          | 1.10 ms                                                         | 1.00 ms: 1.10x faster                                                          |
| sqlite_synth               | 2.07 us                                                         | 1.90 us: 1.09x faster                                                          |
| asyncio_tcp                | 662 ms                                                          | 607 ms: 1.09x faster                                                           |
| sympy_str                  | 240 ms                                                          | 220 ms: 1.09x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 113 ms: 1.09x faster                                                           |
| 2to3                       | 280 ms                                                          | 258 ms: 1.09x faster                                                           |
| django_template            | 36.9 ms                                                         | 34.0 ms: 1.08x faster                                                          |
| regex_dna                  | 127 ms                                                          | 119 ms: 1.07x faster                                                           |
| unpickle_list              | 2.95 us                                                         | 2.78 us: 1.06x faster                                                          |
| sqlglot_optimize           | 48.5 ms                                                         | 46.0 ms: 1.05x faster                                                          |
| json_dumps                 | 7.40 ms                                                         | 7.03 ms: 1.05x faster                                                          |
| sympy_integrate            | 17.5 ms                                                         | 16.7 ms: 1.05x faster                                                          |
| tornado_http               | 105 ms                                                          | 100 ms: 1.04x faster                                                           |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.0 sec: 1.04x faster                                                         |
| regex_effbot               | 2.04 ms                                                         | 1.97 ms: 1.03x faster                                                          |
| pickle_list                | 3.37 us                                                         | 3.31 us: 1.02x faster                                                          |
| bench_mp_pool              | 75.4 ms                                                         | 74.2 ms: 1.02x faster                                                          |
| sympy_expand               | 398 ms                                                          | 394 ms: 1.01x faster                                                           |
| docutils                   | 1.98 sec                                                        | 1.97 sec: 1.01x faster                                                         |
| pidigits                   | 199 ms                                                          | 199 ms: 1.00x faster                                                           |
| json                       | 4.15 ms                                                         | 4.22 ms: 1.02x slower                                                          |
| pickle                     | 7.79 us                                                         | 7.93 us: 1.02x slower                                                          |
| regex_v8                   | 15.0 ms                                                         | 15.8 ms: 1.05x slower                                                          |
| python_startup_no_site     | 19.1 ms                                                         | 20.1 ms: 1.05x slower                                                          |
| json_loads                 | 20.4 us                                                         | 21.4 us: 1.05x slower                                                          |
| unpickle                   | 9.71 us                                                         | 10.4 us: 1.07x slower                                                          |
| async_generators           | 313 ms                                                          | 335 ms: 1.07x slower                                                           |
| python_startup             | 22.4 ms                                                         | 24.0 ms: 1.07x slower                                                          |
| telco                      | 5.51 ms                                                         | 6.00 ms: 1.09x slower                                                          |
| coverage                   | 48.4 ms                                                         | 53.8 ms: 1.11x slower                                                          |
| create_gc_cycles           | 652 us                                                          | 745 us: 1.14x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 146 us: 1.16x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 231 ms: 2.30x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.22x faster                                                                   |

Benchmark hidden because not significant (2): pickle_dict, gc_traversal
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240920-3.14.0a0-342e654-JIT/bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: unknown