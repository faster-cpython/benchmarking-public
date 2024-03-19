# Results vs. 3.12.0

- fork: faster-cpython
- ref: tier2_hot_cold_split
- machine: linux-x86_64
- commit hash: 96941be
- commit date: 2024-03-19
- overall geometric mean: 1.15x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: 0.89x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240319-pythonperf2-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-96941be |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 333 ms: 1.17x slower                                                                   |
| chameleon      | 7.23 ms                                                      | 7.56 ms: 1.05x slower                                                                  |
| docutils       | 2.87 sec                                                     | 3.11 sec: 1.08x slower                                                                 |
| tornado_http   | 121 ms                                                       | 131 ms: 1.08x slower                                                                   |
| Geometric mean | (ref)                                                        | 1.09x slower                                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240319-pythonperf2-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-96941be |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 556 ms: 1.03x slower                                                                   |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 719 ms: 1.03x slower                                                                   |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 720 ms: 1.03x slower                                                                   |
| async_tree_none_tg         | 431 ms                                                       | 449 ms: 1.04x slower                                                                   |
| async_tree_memoization     | 544 ms                                                       | 571 ms: 1.05x slower                                                                   |
| async_tree_io_tg           | 1.05 sec                                                     | 1.11 sec: 1.05x slower                                                                 |
| async_tree_io              | 1.04 sec                                                     | 1.12 sec: 1.07x slower                                                                 |
| Geometric mean             | (ref)                                                        | 1.04x slower                                                                           |

Benchmark hidden because not significant (1): async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240319-pythonperf2-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-96941be |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 264 ms: 1.01x faster                                                                   |
| float          | 76.6 ms                                                      | 102 ms: 1.34x slower                                                                   |
| nbody          | 88.0 ms                                                      | 143 ms: 1.63x slower                                                                   |
| Geometric mean | (ref)                                                        | 1.29x slower                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240319-pythonperf2-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-96941be |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.63 ms: 1.02x slower                                                                  |
| regex_dna      | 239 ms                                                       | 244 ms: 1.02x slower                                                                   |
| regex_v8       | 23.6 ms                                                      | 26.2 ms: 1.11x slower                                                                  |
| regex_compile  | 144 ms                                                       | 215 ms: 1.49x slower                                                                   |
| Geometric mean | (ref)                                                        | 1.14x slower                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240319-pythonperf2-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-96941be |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| pickle_dict          | 32.5 us                                                      | 33.0 us: 1.02x slower                                                                  |
| pickle_list          | 4.43 us                                                      | 4.50 us: 1.02x slower                                                                  |
| unpickle_list        | 4.66 us                                                      | 4.74 us: 1.02x slower                                                                  |
| pickle_pure_python   | 318 us                                                       | 326 us: 1.02x slower                                                                   |
| json_loads           | 24.4 us                                                      | 25.0 us: 1.03x slower                                                                  |
| xml_etree_parse      | 144 ms                                                       | 148 ms: 1.03x slower                                                                   |
| pickle               | 10.5 us                                                      | 11.1 us: 1.05x slower                                                                  |
| json_dumps           | 10.2 ms                                                      | 10.9 ms: 1.07x slower                                                                  |
| xml_etree_generate   | 86.1 ms                                                      | 92.3 ms: 1.07x slower                                                                  |
| xml_etree_process    | 58.4 ms                                                      | 63.7 ms: 1.09x slower                                                                  |
| xml_etree_iterparse  | 103 ms                                                       | 114 ms: 1.11x slower                                                                   |
| tomli_loads          | 2.16 sec                                                     | 2.97 sec: 1.38x slower                                                                 |
| unpickle_pure_python | 210 us                                                       | 305 us: 1.46x slower                                                                   |
| Geometric mean       | (ref)                                                        | 1.09x slower                                                                           |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240319-pythonperf2-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-96941be |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup         | 11.6 ms                                                      | 12.8 ms: 1.10x slower                                                                  |
| python_startup_no_site | 8.64 ms                                                      | 11.2 ms: 1.30x slower                                                                  |
| Geometric mean         | (ref)                                                        | 1.19x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240319-pythonperf2-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-96941be |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 40.3 ms: 1.06x slower                                                                  |
| mako            | 10.0 ms                                                      | 13.9 ms: 1.39x slower                                                                  |
| Geometric mean  | (ref)                                                        | 1.21x slower                                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240319-pythonperf2-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-96941be |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| typing_runtime_protocols   | 152 us                                                       | 131 us: 1.16x faster                                                                   |
| generators                 | 37.4 ms                                                      | 33.9 ms: 1.10x faster                                                                  |
| pidigits                   | 265 ms                                                       | 264 ms: 1.01x faster                                                                   |
| asyncio_tcp                | 378 ms                                                       | 380 ms: 1.01x slower                                                                   |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.60 sec: 1.01x slower                                                                 |
| sqlite_synth               | 2.77 us                                                      | 2.81 us: 1.01x slower                                                                  |
| logging_simple             | 6.71 us                                                      | 6.79 us: 1.01x slower                                                                  |
| regex_effbot               | 3.57 ms                                                      | 3.63 ms: 1.02x slower                                                                  |
| pickle_dict                | 32.5 us                                                      | 33.0 us: 1.02x slower                                                                  |
| pickle_list                | 4.43 us                                                      | 4.50 us: 1.02x slower                                                                  |
| gc_traversal               | 3.48 ms                                                      | 3.54 ms: 1.02x slower                                                                  |
| unpickle_list              | 4.66 us                                                      | 4.74 us: 1.02x slower                                                                  |
| async_generators           | 390 ms                                                       | 398 ms: 1.02x slower                                                                   |
| regex_dna                  | 239 ms                                                       | 244 ms: 1.02x slower                                                                   |
| pickle_pure_python         | 318 us                                                       | 326 us: 1.02x slower                                                                   |
| json_loads                 | 24.4 us                                                      | 25.0 us: 1.03x slower                                                                  |
| xml_etree_parse            | 144 ms                                                       | 148 ms: 1.03x slower                                                                   |
| async_tree_memoization_tg  | 540 ms                                                       | 556 ms: 1.03x slower                                                                   |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 719 ms: 1.03x slower                                                                   |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 720 ms: 1.03x slower                                                                   |
| async_tree_none_tg         | 431 ms                                                       | 449 ms: 1.04x slower                                                                   |
| chameleon                  | 7.23 ms                                                      | 7.56 ms: 1.05x slower                                                                  |
| async_tree_memoization     | 544 ms                                                       | 571 ms: 1.05x slower                                                                   |
| mdp                        | 2.57 sec                                                     | 2.70 sec: 1.05x slower                                                                 |
| deepcopy_reduce            | 3.37 us                                                      | 3.54 us: 1.05x slower                                                                  |
| async_tree_io_tg           | 1.05 sec                                                     | 1.11 sec: 1.05x slower                                                                 |
| pickle                     | 10.5 us                                                      | 11.1 us: 1.05x slower                                                                  |
| django_template            | 38.2 ms                                                      | 40.3 ms: 1.06x slower                                                                  |
| dask                       | 392 ms                                                       | 416 ms: 1.06x slower                                                                   |
| crypto_pyaes               | 80.3 ms                                                      | 85.4 ms: 1.06x slower                                                                  |
| logging_silent             | 94.4 ns                                                      | 100 ns: 1.06x slower                                                                   |
| json                       | 5.12 ms                                                      | 5.45 ms: 1.06x slower                                                                  |
| json_dumps                 | 10.2 ms                                                      | 10.9 ms: 1.07x slower                                                                  |
| pathlib                    | 18.9 ms                                                      | 20.2 ms: 1.07x slower                                                                  |
| sympy_integrate            | 23.9 ms                                                      | 25.6 ms: 1.07x slower                                                                  |
| xml_etree_generate         | 86.1 ms                                                      | 92.3 ms: 1.07x slower                                                                  |
| async_tree_io              | 1.04 sec                                                     | 1.12 sec: 1.07x slower                                                                 |
| bench_mp_pool              | 4.76 ms                                                      | 5.12 ms: 1.08x slower                                                                  |
| tornado_http               | 121 ms                                                       | 131 ms: 1.08x slower                                                                   |
| sqlglot_normalize          | 116 ms                                                       | 125 ms: 1.08x slower                                                                   |
| sympy_sum                  | 162 ms                                                       | 176 ms: 1.08x slower                                                                   |
| docutils                   | 2.87 sec                                                     | 3.11 sec: 1.08x slower                                                                 |
| meteor_contest             | 128 ms                                                       | 139 ms: 1.09x slower                                                                   |
| gunicorn                   | 1.00 ms                                                      | 1.09 ms: 1.09x slower                                                                  |
| xml_etree_process          | 58.4 ms                                                      | 63.7 ms: 1.09x slower                                                                  |
| deepcopy                   | 368 us                                                       | 404 us: 1.10x slower                                                                   |
| python_startup             | 11.6 ms                                                      | 12.8 ms: 1.10x slower                                                                  |
| aiohttp                    | 1.02 ms                                                      | 1.12 ms: 1.10x slower                                                                  |
| xml_etree_iterparse        | 103 ms                                                       | 114 ms: 1.11x slower                                                                   |
| regex_v8                   | 23.6 ms                                                      | 26.2 ms: 1.11x slower                                                                  |
| comprehensions             | 21.9 us                                                      | 24.5 us: 1.12x slower                                                                  |
| sympy_str                  | 302 ms                                                       | 342 ms: 1.13x slower                                                                   |
| mypy2                      | 830 ms                                                       | 960 ms: 1.16x slower                                                                   |
| sqlglot_transpile          | 1.78 ms                                                      | 2.06 ms: 1.16x slower                                                                  |
| 2to3                       | 285 ms                                                       | 333 ms: 1.17x slower                                                                   |
| raytrace                   | 298 ms                                                       | 349 ms: 1.17x slower                                                                   |
| sqlglot_parse              | 1.38 ms                                                      | 1.62 ms: 1.18x slower                                                                  |
| dulwich_log                | 65.4 ms                                                      | 78.4 ms: 1.20x slower                                                                  |
| bench_thread_pool          | 950 us                                                       | 1.15 ms: 1.21x slower                                                                  |
| sympy_expand               | 484 ms                                                       | 585 ms: 1.21x slower                                                                   |
| sqlglot_optimize           | 57.5 ms                                                      | 69.5 ms: 1.21x slower                                                                  |
| chaos                      | 64.0 ms                                                      | 77.5 ms: 1.21x slower                                                                  |
| pprint_safe_repr           | 807 ms                                                       | 981 ms: 1.21x slower                                                                   |
| deepcopy_memo              | 36.8 us                                                      | 44.9 us: 1.22x slower                                                                  |
| pprint_pformat             | 1.65 sec                                                     | 2.02 sec: 1.22x slower                                                                 |
| pycparser                  | 1.23 sec                                                     | 1.51 sec: 1.22x slower                                                                 |
| telco                      | 6.96 ms                                                      | 8.67 ms: 1.25x slower                                                                  |
| nqueens                    | 89.9 ms                                                      | 115 ms: 1.28x slower                                                                   |
| unpack_sequence            | 53.2 ns                                                      | 68.0 ns: 1.28x slower                                                                  |
| deltablue                  | 3.24 ms                                                      | 4.14 ms: 1.28x slower                                                                  |
| python_startup_no_site     | 8.64 ms                                                      | 11.2 ms: 1.30x slower                                                                  |
| richards_super             | 51.3 ms                                                      | 67.5 ms: 1.31x slower                                                                  |
| float                      | 76.6 ms                                                      | 102 ms: 1.34x slower                                                                   |
| richards                   | 45.7 ms                                                      | 61.2 ms: 1.34x slower                                                                  |
| coverage                   | 66.7 ms                                                      | 89.3 ms: 1.34x slower                                                                  |
| scimark_lu                 | 98.8 ms                                                      | 132 ms: 1.34x slower                                                                   |
| tomli_loads                | 2.16 sec                                                     | 2.97 sec: 1.38x slower                                                                 |
| go                         | 150 ms                                                       | 208 ms: 1.39x slower                                                                   |
| scimark_monte_carlo        | 69.0 ms                                                      | 95.8 ms: 1.39x slower                                                                  |
| mako                       | 10.0 ms                                                      | 13.9 ms: 1.39x slower                                                                  |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.98 ms: 1.42x slower                                                                  |
| scimark_fft                | 301 ms                                                       | 432 ms: 1.44x slower                                                                   |
| unpickle_pure_python       | 210 us                                                       | 305 us: 1.46x slower                                                                   |
| scimark_sor                | 109 ms                                                       | 159 ms: 1.46x slower                                                                   |
| fannkuch                   | 350 ms                                                       | 519 ms: 1.48x slower                                                                   |
| regex_compile              | 144 ms                                                       | 215 ms: 1.49x slower                                                                   |
| pyflate                    | 439 ms                                                       | 660 ms: 1.50x slower                                                                   |
| spectral_norm              | 91.6 ms                                                      | 147 ms: 1.61x slower                                                                   |
| nbody                      | 88.0 ms                                                      | 143 ms: 1.63x slower                                                                   |
| hexiom                     | 5.96 ms                                                      | 10.7 ms: 1.79x slower                                                                  |
| Geometric mean             | (ref)                                                        | 1.15x slower                                                                           |

Benchmark hidden because not significant (6): coroutines, logging_format, async_tree_none, unpickle, asyncio_websockets, create_gc_cycles
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240319-3.13.0a5+-96941be-PYTHON_UOPS/bm-20240319-pythonperf2-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-96941be.json: genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.07x


# Memory

- memory change: 0.89x