# Results vs. 3.12.0

- fork: faster-cpython
- ref: spill_before_escapin
- machine: linux-x86_64
- commit hash: e5d0e67
- commit date: 2024-09-17
- overall geometric mean: 1.018x faster
- HPT reliability: 69.26%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240917-pythonperf2-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-e5d0e67 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 310 ms: 1.09x slower                                                                  |
| docutils       | 2.87 sec                                                     | 3.17 sec: 1.11x slower                                                                |
| Geometric mean | (ref)                                                        | 1.07x slower                                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240917-pythonperf2-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-e5d0e67 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 310 ms: 1.39x faster                                                                  |
| async_tree_none            | 452 ms                                                       | 325 ms: 1.39x faster                                                                  |
| async_tree_memoization_tg  | 540 ms                                                       | 391 ms: 1.38x faster                                                                  |
| async_tree_memoization     | 544 ms                                                       | 406 ms: 1.34x faster                                                                  |
| async_tree_io_tg           | 1.05 sec                                                     | 791 ms: 1.33x faster                                                                  |
| async_tree_io              | 1.04 sec                                                     | 814 ms: 1.28x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 549 ms: 1.27x faster                                                                  |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 579 ms: 1.20x faster                                                                  |
| Geometric mean             | (ref)                                                        | 1.32x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240917-pythonperf2-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-e5d0e67 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 78.2 ms: 1.13x faster                                                                 |
| pidigits       | 265 ms                                                       | 250 ms: 1.06x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                          |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240917-pythonperf2-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-e5d0e67 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 148 ms: 1.03x slower                                                                  |
| regex_dna      | 239 ms                                                       | 252 ms: 1.06x slower                                                                  |
| regex_v8       | 23.6 ms                                                      | 26.2 ms: 1.11x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.05x slower                                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240917-pythonperf2-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-e5d0e67 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 80.7 ms: 1.07x faster                                                                 |
| xml_etree_iterparse  | 103 ms                                                       | 97.8 ms: 1.05x faster                                                                 |
| xml_etree_process    | 58.4 ms                                                      | 55.8 ms: 1.05x faster                                                                 |
| pickle_dict          | 32.5 us                                                      | 31.9 us: 1.02x faster                                                                 |
| json_loads           | 24.4 us                                                      | 23.9 us: 1.02x faster                                                                 |
| xml_etree_parse      | 144 ms                                                       | 142 ms: 1.02x faster                                                                  |
| tomli_loads          | 2.16 sec                                                     | 2.13 sec: 1.01x faster                                                                |
| pickle               | 10.5 us                                                      | 10.6 us: 1.01x slower                                                                 |
| pickle_list          | 4.43 us                                                      | 4.52 us: 1.02x slower                                                                 |
| pickle_pure_python   | 318 us                                                       | 325 us: 1.02x slower                                                                  |
| json_dumps           | 10.2 ms                                                      | 10.5 ms: 1.02x slower                                                                 |
| unpickle_pure_python | 210 us                                                       | 215 us: 1.03x slower                                                                  |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                          |

Benchmark hidden because not significant (2): unpickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240917-pythonperf2-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-e5d0e67 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.99 ms: 1.04x slower                                                                 |
| python_startup         | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                                 |
| Geometric mean         | (ref)                                                        | 1.09x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240917-pythonperf2-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-e5d0e67 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.23 ms: 1.08x faster                                                                 |
| django_template | 38.2 ms                                                      | 43.6 ms: 1.14x slower                                                                 |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240917-pythonperf2-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-e5d0e67 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 310 ms: 1.39x faster                                                                  |
| async_tree_none            | 452 ms                                                       | 325 ms: 1.39x faster                                                                  |
| async_tree_memoization_tg  | 540 ms                                                       | 391 ms: 1.38x faster                                                                  |
| async_tree_memoization     | 544 ms                                                       | 406 ms: 1.34x faster                                                                  |
| async_tree_io_tg           | 1.05 sec                                                     | 791 ms: 1.33x faster                                                                  |
| deepcopy_memo              | 36.8 us                                                      | 28.3 us: 1.30x faster                                                                 |
| async_tree_io              | 1.04 sec                                                     | 814 ms: 1.28x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 549 ms: 1.27x faster                                                                  |
| deepcopy                   | 368 us                                                       | 300 us: 1.23x faster                                                                  |
| comprehensions             | 21.9 us                                                      | 18.2 us: 1.21x faster                                                                 |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 579 ms: 1.20x faster                                                                  |
| pathlib                    | 18.9 ms                                                      | 15.8 ms: 1.20x faster                                                                 |
| crypto_pyaes               | 80.3 ms                                                      | 68.8 ms: 1.17x faster                                                                 |
| spectral_norm              | 91.6 ms                                                      | 80.4 ms: 1.14x faster                                                                 |
| deepcopy_reduce            | 3.37 us                                                      | 2.99 us: 1.13x faster                                                                 |
| nbody                      | 88.0 ms                                                      | 78.2 ms: 1.13x faster                                                                 |
| mako                       | 10.0 ms                                                      | 9.23 ms: 1.08x faster                                                                 |
| richards                   | 45.7 ms                                                      | 42.8 ms: 1.07x faster                                                                 |
| xml_etree_generate         | 86.1 ms                                                      | 80.7 ms: 1.07x faster                                                                 |
| coroutines                 | 23.0 ms                                                      | 21.6 ms: 1.06x faster                                                                 |
| scimark_sor                | 109 ms                                                       | 103 ms: 1.06x faster                                                                  |
| pidigits                   | 265 ms                                                       | 250 ms: 1.06x faster                                                                  |
| xml_etree_iterparse        | 103 ms                                                       | 97.8 ms: 1.05x faster                                                                 |
| xml_etree_process          | 58.4 ms                                                      | 55.8 ms: 1.05x faster                                                                 |
| scimark_fft                | 301 ms                                                       | 288 ms: 1.05x faster                                                                  |
| logging_format             | 7.48 us                                                      | 7.21 us: 1.04x faster                                                                 |
| richards_super             | 51.3 ms                                                      | 49.7 ms: 1.03x faster                                                                 |
| bench_thread_pool          | 950 us                                                       | 924 us: 1.03x faster                                                                  |
| sqlite_synth               | 2.77 us                                                      | 2.70 us: 1.03x faster                                                                 |
| scimark_lu                 | 98.8 ms                                                      | 96.3 ms: 1.03x faster                                                                 |
| scimark_monte_carlo        | 69.0 ms                                                      | 67.7 ms: 1.02x faster                                                                 |
| pickle_dict                | 32.5 us                                                      | 31.9 us: 1.02x faster                                                                 |
| json_loads                 | 24.4 us                                                      | 23.9 us: 1.02x faster                                                                 |
| logging_simple             | 6.71 us                                                      | 6.60 us: 1.02x faster                                                                 |
| xml_etree_parse            | 144 ms                                                       | 142 ms: 1.02x faster                                                                  |
| deltablue                  | 3.24 ms                                                      | 3.19 ms: 1.01x faster                                                                 |
| tomli_loads                | 2.16 sec                                                     | 2.13 sec: 1.01x faster                                                                |
| pprint_safe_repr           | 807 ms                                                       | 797 ms: 1.01x faster                                                                  |
| async_generators           | 390 ms                                                       | 386 ms: 1.01x faster                                                                  |
| mdp                        | 2.57 sec                                                     | 2.55 sec: 1.01x faster                                                                |
| asyncio_tcp                | 378 ms                                                       | 376 ms: 1.01x faster                                                                  |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                                                |
| dulwich_log                | 65.4 ms                                                      | 65.0 ms: 1.00x faster                                                                 |
| pickle                     | 10.5 us                                                      | 10.6 us: 1.01x slower                                                                 |
| go                         | 150 ms                                                       | 151 ms: 1.01x slower                                                                  |
| meteor_contest             | 128 ms                                                       | 130 ms: 1.01x slower                                                                  |
| asyncio_websockets         | 387 ms                                                       | 393 ms: 1.02x slower                                                                  |
| json                       | 5.12 ms                                                      | 5.22 ms: 1.02x slower                                                                 |
| pickle_list                | 4.43 us                                                      | 4.52 us: 1.02x slower                                                                 |
| fannkuch                   | 350 ms                                                       | 357 ms: 1.02x slower                                                                  |
| pickle_pure_python         | 318 us                                                       | 325 us: 1.02x slower                                                                  |
| json_dumps                 | 10.2 ms                                                      | 10.5 ms: 1.02x slower                                                                 |
| unpickle_pure_python       | 210 us                                                       | 215 us: 1.03x slower                                                                  |
| regex_compile              | 144 ms                                                       | 148 ms: 1.03x slower                                                                  |
| pycparser                  | 1.23 sec                                                     | 1.27 sec: 1.03x slower                                                                |
| sympy_str                  | 302 ms                                                       | 313 ms: 1.03x slower                                                                  |
| chaos                      | 64.0 ms                                                      | 66.4 ms: 1.04x slower                                                                 |
| python_startup_no_site     | 8.64 ms                                                      | 8.99 ms: 1.04x slower                                                                 |
| sympy_sum                  | 162 ms                                                       | 170 ms: 1.05x slower                                                                  |
| regex_dna                  | 239 ms                                                       | 252 ms: 1.06x slower                                                                  |
| sqlglot_parse              | 1.38 ms                                                      | 1.49 ms: 1.08x slower                                                                 |
| logging_silent             | 94.4 ns                                                      | 102 ns: 1.08x slower                                                                  |
| sympy_expand               | 484 ms                                                       | 525 ms: 1.08x slower                                                                  |
| pyflate                    | 439 ms                                                       | 476 ms: 1.09x slower                                                                  |
| 2to3                       | 285 ms                                                       | 310 ms: 1.09x slower                                                                  |
| bench_mp_pool              | 4.76 ms                                                      | 5.19 ms: 1.09x slower                                                                 |
| sqlglot_transpile          | 1.78 ms                                                      | 1.94 ms: 1.09x slower                                                                 |
| sqlglot_normalize          | 116 ms                                                       | 127 ms: 1.10x slower                                                                  |
| raytrace                   | 298 ms                                                       | 328 ms: 1.10x slower                                                                  |
| docutils                   | 2.87 sec                                                     | 3.17 sec: 1.11x slower                                                                |
| regex_v8                   | 23.6 ms                                                      | 26.2 ms: 1.11x slower                                                                 |
| sympy_integrate            | 23.9 ms                                                      | 26.7 ms: 1.12x slower                                                                 |
| nqueens                    | 89.9 ms                                                      | 101 ms: 1.12x slower                                                                  |
| sqlglot_optimize           | 57.5 ms                                                      | 64.5 ms: 1.12x slower                                                                 |
| django_template            | 38.2 ms                                                      | 43.6 ms: 1.14x slower                                                                 |
| telco                      | 6.96 ms                                                      | 8.01 ms: 1.15x slower                                                                 |
| python_startup             | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                                 |
| hexiom                     | 5.96 ms                                                      | 6.99 ms: 1.17x slower                                                                 |
| create_gc_cycles           | 1.59 ms                                                      | 1.89 ms: 1.19x slower                                                                 |
| typing_runtime_protocols   | 152 us                                                       | 184 us: 1.21x slower                                                                  |
| coverage                   | 66.7 ms                                                      | 81.2 ms: 1.22x slower                                                                 |
| gc_traversal               | 3.48 ms                                                      | 4.36 ms: 1.25x slower                                                                 |
| unpack_sequence            | 53.2 ns                                                      | 88.0 ns: 1.65x slower                                                                 |
| Geometric mean             | (ref)                                                        | 1.01x faster                                                                          |

Benchmark hidden because not significant (8): generators, scimark_sparse_mat_mult, unpickle_list, float, pprint_pformat, regex_effbot, unpickle, tornado_http
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240917-3.14.0a0-e5d0e67-JIT/bm-20240917-pythonperf2-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-e5d0e67.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.018x faster
# HPT report

- Reliability score: 69.26% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x