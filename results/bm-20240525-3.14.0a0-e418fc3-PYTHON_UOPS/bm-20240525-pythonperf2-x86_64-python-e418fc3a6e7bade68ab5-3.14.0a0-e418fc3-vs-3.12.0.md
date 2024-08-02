# Results vs. 3.12.0

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: linux-x86_64
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.17x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x slower
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 343 ms: 1.20x slower                                                        |
| chameleon      | 7.23 ms                                                      | 8.74 ms: 1.21x slower                                                       |
| docutils       | 2.87 sec                                                     | 3.45 sec: 1.20x slower                                                      |
| tornado_http   | 121 ms                                                       | 130 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                        | 1.17x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 363 ms: 1.19x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 459 ms: 1.18x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 603 ms: 1.16x faster                                                        |
| async_tree_none            | 452 ms                                                       | 396 ms: 1.14x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 932 ms: 1.13x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 935 ms: 1.11x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 496 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 645 ms: 1.08x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.13x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 254 ms: 1.04x faster                                                        |
| float          | 76.6 ms                                                      | 97.3 ms: 1.27x slower                                                       |
| nbody          | 88.0 ms                                                      | 124 ms: 1.40x slower                                                        |
| Geometric mean | (ref)                                                        | 1.20x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.49 ms: 1.02x faster                                                       |
| regex_dna      | 239 ms                                                       | 241 ms: 1.01x slower                                                        |
| regex_v8       | 23.6 ms                                                      | 26.4 ms: 1.12x slower                                                       |
| regex_compile  | 144 ms                                                       | 215 ms: 1.50x slower                                                        |
| Geometric mean | (ref)                                                        | 1.13x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_dict          | 32.5 us                                                      | 30.8 us: 1.06x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 145 ms: 1.01x slower                                                        |
| unpickle_list        | 4.66 us                                                      | 4.70 us: 1.01x slower                                                       |
| pickle               | 10.5 us                                                      | 10.6 us: 1.01x slower                                                       |
| json_loads           | 24.4 us                                                      | 24.9 us: 1.02x slower                                                       |
| pickle_list          | 4.43 us                                                      | 4.65 us: 1.05x slower                                                       |
| unpickle             | 14.8 us                                                      | 15.6 us: 1.05x slower                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 113 ms: 1.10x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 11.3 ms: 1.11x slower                                                       |
| xml_etree_generate   | 86.1 ms                                                      | 98.3 ms: 1.14x slower                                                       |
| xml_etree_process    | 58.4 ms                                                      | 68.8 ms: 1.18x slower                                                       |
| tomli_loads          | 2.16 sec                                                     | 2.95 sec: 1.36x slower                                                      |
| pickle_pure_python   | 318 us                                                       | 437 us: 1.37x slower                                                        |
| unpickle_pure_python | 210 us                                                       | 311 us: 1.48x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.12x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.93 ms: 1.03x slower                                                       |
| python_startup         | 11.6 ms                                                      | 13.2 ms: 1.13x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.08x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 45.9 ms: 1.20x slower                                                       |
| mako            | 10.0 ms                                                      | 14.0 ms: 1.40x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.30x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 363 ms: 1.19x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 459 ms: 1.18x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 603 ms: 1.16x faster                                                        |
| async_tree_none            | 452 ms                                                       | 396 ms: 1.14x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 932 ms: 1.13x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 935 ms: 1.11x faster                                                        |
| generators                 | 37.4 ms                                                      | 33.9 ms: 1.10x faster                                                       |
| pathlib                    | 18.9 ms                                                      | 17.2 ms: 1.10x faster                                                       |
| async_tree_memoization     | 544 ms                                                       | 496 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 645 ms: 1.08x faster                                                        |
| pickle_dict                | 32.5 us                                                      | 30.8 us: 1.06x faster                                                       |
| pidigits                   | 265 ms                                                       | 254 ms: 1.04x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.49 ms: 1.02x faster                                                       |
| coroutines                 | 23.0 ms                                                      | 22.9 ms: 1.01x faster                                                       |
| xml_etree_parse            | 144 ms                                                       | 145 ms: 1.01x slower                                                        |
| unpickle_list              | 4.66 us                                                      | 4.70 us: 1.01x slower                                                       |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.60 sec: 1.01x slower                                                      |
| pickle                     | 10.5 us                                                      | 10.6 us: 1.01x slower                                                       |
| regex_dna                  | 239 ms                                                       | 241 ms: 1.01x slower                                                        |
| asyncio_websockets         | 387 ms                                                       | 392 ms: 1.01x slower                                                        |
| asyncio_tcp                | 378 ms                                                       | 386 ms: 1.02x slower                                                        |
| json_loads                 | 24.4 us                                                      | 24.9 us: 1.02x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 8.93 ms: 1.03x slower                                                       |
| logging_simple             | 6.71 us                                                      | 6.94 us: 1.03x slower                                                       |
| async_generators           | 390 ms                                                       | 404 ms: 1.04x slower                                                        |
| sqlite_synth               | 2.77 us                                                      | 2.90 us: 1.05x slower                                                       |
| pickle_list                | 4.43 us                                                      | 4.65 us: 1.05x slower                                                       |
| unpickle                   | 14.8 us                                                      | 15.6 us: 1.05x slower                                                       |
| json                       | 5.12 ms                                                      | 5.46 ms: 1.07x slower                                                       |
| dask                       | 392 ms                                                       | 422 ms: 1.08x slower                                                        |
| tornado_http               | 121 ms                                                       | 130 ms: 1.08x slower                                                        |
| bench_thread_pool          | 950 us                                                       | 1.02 ms: 1.08x slower                                                       |
| raytrace                   | 298 ms                                                       | 323 ms: 1.08x slower                                                        |
| mdp                        | 2.57 sec                                                     | 2.81 sec: 1.09x slower                                                      |
| xml_etree_iterparse        | 103 ms                                                       | 113 ms: 1.10x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 11.3 ms: 1.11x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 26.4 ms: 1.12x slower                                                       |
| meteor_contest             | 128 ms                                                       | 144 ms: 1.12x slower                                                        |
| python_startup             | 11.6 ms                                                      | 13.2 ms: 1.13x slower                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 98.3 ms: 1.14x slower                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 93.4 ms: 1.16x slower                                                       |
| sympy_sum                  | 162 ms                                                       | 190 ms: 1.17x slower                                                        |
| pycparser                  | 1.23 sec                                                     | 1.45 sec: 1.18x slower                                                      |
| sympy_integrate            | 23.9 ms                                                      | 28.2 ms: 1.18x slower                                                       |
| xml_etree_process          | 58.4 ms                                                      | 68.8 ms: 1.18x slower                                                       |
| dulwich_log                | 65.4 ms                                                      | 78.0 ms: 1.19x slower                                                       |
| docutils                   | 2.87 sec                                                     | 3.45 sec: 1.20x slower                                                      |
| django_template            | 38.2 ms                                                      | 45.9 ms: 1.20x slower                                                       |
| 2to3                       | 285 ms                                                       | 343 ms: 1.20x slower                                                        |
| chameleon                  | 7.23 ms                                                      | 8.74 ms: 1.21x slower                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 4.08 us: 1.21x slower                                                       |
| sqlglot_normalize          | 116 ms                                                       | 140 ms: 1.21x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 2.18 ms: 1.23x slower                                                       |
| sqlglot_optimize           | 57.5 ms                                                      | 70.6 ms: 1.23x slower                                                       |
| sympy_str                  | 302 ms                                                       | 372 ms: 1.23x slower                                                        |
| coverage                   | 66.7 ms                                                      | 82.4 ms: 1.24x slower                                                       |
| comprehensions             | 21.9 us                                                      | 27.4 us: 1.25x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.73 ms: 1.25x slower                                                       |
| pprint_pformat             | 1.65 sec                                                     | 2.08 sec: 1.26x slower                                                      |
| pprint_safe_repr           | 807 ms                                                       | 1.02 sec: 1.26x slower                                                      |
| chaos                      | 64.0 ms                                                      | 80.9 ms: 1.26x slower                                                       |
| float                      | 76.6 ms                                                      | 97.3 ms: 1.27x slower                                                       |
| deepcopy                   | 368 us                                                       | 473 us: 1.28x slower                                                        |
| richards_super             | 51.3 ms                                                      | 65.9 ms: 1.28x slower                                                       |
| richards                   | 45.7 ms                                                      | 58.9 ms: 1.29x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 2.05 ms: 1.29x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 4.51 ms: 1.30x slower                                                       |
| sympy_expand               | 484 ms                                                       | 636 ms: 1.31x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 118 ms: 1.32x slower                                                        |
| telco                      | 6.96 ms                                                      | 9.20 ms: 1.32x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 204 us: 1.34x slower                                                        |
| go                         | 150 ms                                                       | 202 ms: 1.35x slower                                                        |
| fannkuch                   | 350 ms                                                       | 473 ms: 1.35x slower                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.95 sec: 1.36x slower                                                      |
| pickle_pure_python         | 318 us                                                       | 437 us: 1.37x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 4.53 ms: 1.40x slower                                                       |
| mako                       | 10.0 ms                                                      | 14.0 ms: 1.40x slower                                                       |
| nbody                      | 88.0 ms                                                      | 124 ms: 1.40x slower                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 97.8 ms: 1.42x slower                                                       |
| scimark_fft                | 301 ms                                                       | 428 ms: 1.42x slower                                                        |
| scimark_lu                 | 98.8 ms                                                      | 142 ms: 1.43x slower                                                        |
| scimark_sor                | 109 ms                                                       | 159 ms: 1.46x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 311 us: 1.48x slower                                                        |
| pyflate                    | 439 ms                                                       | 651 ms: 1.48x slower                                                        |
| regex_compile              | 144 ms                                                       | 215 ms: 1.50x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 6.49 ms: 1.54x slower                                                       |
| deepcopy_memo              | 36.8 us                                                      | 57.8 us: 1.57x slower                                                       |
| spectral_norm              | 91.6 ms                                                      | 148 ms: 1.61x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 165 ns: 1.75x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 10.4 ms: 1.75x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.17x slower                                                                |

Benchmark hidden because not significant (2): logging_format, bench_mp_pool
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240525-3.14.0a0-e418fc3-PYTHON_UOPS/bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.12x
- 95% likely to have a slowdown of 1.11x
- 99% likely to have a slowdown of 1.09x

# Memory
- memory change: 0.93x