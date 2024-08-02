# Results vs. 3.12.0

- fork: python
- ref: caf6064a1bc15ac344af
- machine: linux-x86_64
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.20x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x slower
- Memory change: 0.94x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 343 ms: 1.20x slower                                                        |
| chameleon      | 7.23 ms                                                      | 8.61 ms: 1.19x slower                                                       |
| docutils       | 2.87 sec                                                     | 3.46 sec: 1.21x slower                                                      |
| tornado_http   | 121 ms                                                       | 129 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                        | 1.17x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 352 ms: 1.22x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 458 ms: 1.18x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 907 ms: 1.16x faster                                                        |
| async_tree_none            | 452 ms                                                       | 389 ms: 1.16x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 898 ms: 1.16x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 607 ms: 1.15x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 491 ms: 1.11x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 642 ms: 1.08x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.15x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 254 ms: 1.04x faster                                                        |
| float          | 76.6 ms                                                      | 95.7 ms: 1.25x slower                                                       |
| nbody          | 88.0 ms                                                      | 123 ms: 1.39x slower                                                        |
| Geometric mean | (ref)                                                        | 1.19x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.46 ms: 1.03x faster                                                       |
| regex_v8       | 23.6 ms                                                      | 26.1 ms: 1.11x slower                                                       |
| regex_compile  | 144 ms                                                       | 214 ms: 1.49x slower                                                        |
| Geometric mean | (ref)                                                        | 1.12x slower                                                                |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_dict          | 32.5 us                                                      | 30.7 us: 1.06x faster                                                       |
| unpickle_list        | 4.66 us                                                      | 4.68 us: 1.00x slower                                                       |
| json_loads           | 24.4 us                                                      | 24.6 us: 1.01x slower                                                       |
| pickle_list          | 4.43 us                                                      | 4.49 us: 1.01x slower                                                       |
| unpickle             | 14.8 us                                                      | 15.4 us: 1.04x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 11.1 ms: 1.08x slower                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 113 ms: 1.10x slower                                                        |
| xml_etree_generate   | 86.1 ms                                                      | 96.4 ms: 1.12x slower                                                       |
| xml_etree_process    | 58.4 ms                                                      | 67.8 ms: 1.16x slower                                                       |
| tomli_loads          | 2.16 sec                                                     | 2.88 sec: 1.34x slower                                                      |
| pickle_pure_python   | 318 us                                                       | 440 us: 1.38x slower                                                        |
| unpickle_pure_python | 210 us                                                       | 308 us: 1.47x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.11x slower                                                                |

Benchmark hidden because not significant (2): pickle, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.90 ms: 1.03x slower                                                       |
| python_startup         | 11.6 ms                                                      | 12.9 ms: 1.11x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.07x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 45.8 ms: 1.20x slower                                                       |
| mako            | 10.0 ms                                                      | 14.7 ms: 1.47x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.33x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 352 ms: 1.22x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 458 ms: 1.18x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 907 ms: 1.16x faster                                                        |
| async_tree_none            | 452 ms                                                       | 389 ms: 1.16x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 898 ms: 1.16x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 607 ms: 1.15x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 491 ms: 1.11x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 17.1 ms: 1.10x faster                                                       |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 642 ms: 1.08x faster                                                        |
| generators                 | 37.4 ms                                                      | 34.6 ms: 1.08x faster                                                       |
| pickle_dict                | 32.5 us                                                      | 30.7 us: 1.06x faster                                                       |
| pidigits                   | 265 ms                                                       | 254 ms: 1.04x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.46 ms: 1.03x faster                                                       |
| logging_format             | 7.48 us                                                      | 7.36 us: 1.02x faster                                                       |
| unpickle_list              | 4.66 us                                                      | 4.68 us: 1.00x slower                                                       |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.60 sec: 1.01x slower                                                      |
| json_loads                 | 24.4 us                                                      | 24.6 us: 1.01x slower                                                       |
| pickle_list                | 4.43 us                                                      | 4.49 us: 1.01x slower                                                       |
| asyncio_tcp                | 378 ms                                                       | 387 ms: 1.02x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 8.90 ms: 1.03x slower                                                       |
| unpickle                   | 14.8 us                                                      | 15.4 us: 1.04x slower                                                       |
| sqlite_synth               | 2.77 us                                                      | 2.91 us: 1.05x slower                                                       |
| async_generators           | 390 ms                                                       | 411 ms: 1.05x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 5.02 ms: 1.05x slower                                                       |
| tornado_http               | 121 ms                                                       | 129 ms: 1.06x slower                                                        |
| dask                       | 392 ms                                                       | 423 ms: 1.08x slower                                                        |
| mdp                        | 2.57 sec                                                     | 2.78 sec: 1.08x slower                                                      |
| json                       | 5.12 ms                                                      | 5.53 ms: 1.08x slower                                                       |
| json_dumps                 | 10.2 ms                                                      | 11.1 ms: 1.08x slower                                                       |
| bench_thread_pool          | 950 us                                                       | 1.03 ms: 1.08x slower                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 113 ms: 1.10x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 26.1 ms: 1.11x slower                                                       |
| python_startup             | 11.6 ms                                                      | 12.9 ms: 1.11x slower                                                       |
| raytrace                   | 298 ms                                                       | 333 ms: 1.12x slower                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 96.4 ms: 1.12x slower                                                       |
| meteor_contest             | 128 ms                                                       | 148 ms: 1.16x slower                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 93.0 ms: 1.16x slower                                                       |
| xml_etree_process          | 58.4 ms                                                      | 67.8 ms: 1.16x slower                                                       |
| sympy_sum                  | 162 ms                                                       | 189 ms: 1.17x slower                                                        |
| pycparser                  | 1.23 sec                                                     | 1.46 sec: 1.18x slower                                                      |
| sympy_integrate            | 23.9 ms                                                      | 28.3 ms: 1.18x slower                                                       |
| chameleon                  | 7.23 ms                                                      | 8.61 ms: 1.19x slower                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 4.03 us: 1.19x slower                                                       |
| dulwich_log                | 65.4 ms                                                      | 78.3 ms: 1.20x slower                                                       |
| django_template            | 38.2 ms                                                      | 45.8 ms: 1.20x slower                                                       |
| 2to3                       | 285 ms                                                       | 343 ms: 1.20x slower                                                        |
| docutils                   | 2.87 sec                                                     | 3.46 sec: 1.21x slower                                                      |
| coverage                   | 66.7 ms                                                      | 80.7 ms: 1.21x slower                                                       |
| sympy_str                  | 302 ms                                                       | 370 ms: 1.23x slower                                                        |
| sqlglot_normalize          | 116 ms                                                       | 142 ms: 1.23x slower                                                        |
| sqlglot_optimize           | 57.5 ms                                                      | 71.0 ms: 1.24x slower                                                       |
| sqlglot_transpile          | 1.78 ms                                                      | 2.20 ms: 1.24x slower                                                       |
| float                      | 76.6 ms                                                      | 95.7 ms: 1.25x slower                                                       |
| comprehensions             | 21.9 us                                                      | 27.6 us: 1.26x slower                                                       |
| chaos                      | 64.0 ms                                                      | 80.5 ms: 1.26x slower                                                       |
| pprint_pformat             | 1.65 sec                                                     | 2.09 sec: 1.26x slower                                                      |
| sqlglot_parse              | 1.38 ms                                                      | 1.75 ms: 1.27x slower                                                       |
| pprint_safe_repr           | 807 ms                                                       | 1.03 sec: 1.27x slower                                                      |
| deepcopy                   | 368 us                                                       | 473 us: 1.28x slower                                                        |
| sympy_expand               | 484 ms                                                       | 624 ms: 1.29x slower                                                        |
| richards                   | 45.7 ms                                                      | 59.3 ms: 1.30x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 4.51 ms: 1.30x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 2.07 ms: 1.30x slower                                                       |
| richards_super             | 51.3 ms                                                      | 66.9 ms: 1.30x slower                                                       |
| nqueens                    | 89.9 ms                                                      | 119 ms: 1.32x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 200 us: 1.32x slower                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.88 sec: 1.34x slower                                                      |
| go                         | 150 ms                                                       | 203 ms: 1.35x slower                                                        |
| fannkuch                   | 350 ms                                                       | 483 ms: 1.38x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 440 us: 1.38x slower                                                        |
| nbody                      | 88.0 ms                                                      | 123 ms: 1.39x slower                                                        |
| scimark_lu                 | 98.8 ms                                                      | 138 ms: 1.40x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 4.56 ms: 1.41x slower                                                       |
| scimark_fft                | 301 ms                                                       | 429 ms: 1.43x slower                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 98.8 ms: 1.43x slower                                                       |
| mako                       | 10.0 ms                                                      | 14.7 ms: 1.47x slower                                                       |
| unpickle_pure_python       | 210 us                                                       | 308 us: 1.47x slower                                                        |
| pyflate                    | 439 ms                                                       | 645 ms: 1.47x slower                                                        |
| regex_compile              | 144 ms                                                       | 214 ms: 1.49x slower                                                        |
| scimark_sor                | 109 ms                                                       | 166 ms: 1.52x slower                                                        |
| deepcopy_memo              | 36.8 us                                                      | 58.2 us: 1.58x slower                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 6.97 ms: 1.66x slower                                                       |
| spectral_norm              | 91.6 ms                                                      | 155 ms: 1.69x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 161 ns: 1.70x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 10.6 ms: 1.77x slower                                                       |
| telco                      | 6.96 ms                                                      | 182 ms: 26.14x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.20x slower                                                                |

Benchmark hidden because not significant (6): coroutines, logging_simple, pickle, regex_dna, xml_etree_parse, asyncio_websockets
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240518-3.14.0a0-caf6064-PYTHON_UOPS/bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.12x
- 95% likely to have a slowdown of 1.11x
- 99% likely to have a slowdown of 1.08x

# Memory
- memory change: 0.94x