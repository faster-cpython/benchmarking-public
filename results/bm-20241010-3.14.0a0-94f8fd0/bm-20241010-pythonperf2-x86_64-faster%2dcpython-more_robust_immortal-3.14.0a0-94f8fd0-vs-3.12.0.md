# Results vs. 3.12.0

- fork: faster-cpython
- ref: more_robust_immortal
- machine: linux-x86_64
- commit hash: 94f8fd0
- commit date: 2024-10-10
- overall geometric mean: 1.033x faster
- HPT reliability: 97.17%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241010-pythonperf2-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 280 ms: 1.02x faster                                                                  |
| tornado_http   | 121 ms                                                       | 116 ms: 1.05x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                          |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241010-pythonperf2-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 320 ms: 1.41x faster                                                                  |
| async_tree_none_tg         | 431 ms                                                       | 310 ms: 1.39x faster                                                                  |
| async_tree_memoization_tg  | 540 ms                                                       | 391 ms: 1.38x faster                                                                  |
| async_tree_memoization     | 544 ms                                                       | 400 ms: 1.36x faster                                                                  |
| async_tree_io_tg           | 1.05 sec                                                     | 795 ms: 1.32x faster                                                                  |
| async_tree_io              | 1.04 sec                                                     | 812 ms: 1.28x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 549 ms: 1.27x faster                                                                  |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 571 ms: 1.22x faster                                                                  |
| Geometric mean             | (ref)                                                        | 1.33x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241010-pythonperf2-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 252 ms: 1.05x faster                                                                  |
| float          | 76.6 ms                                                      | 79.7 ms: 1.04x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241010-pythonperf2-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 137 ms: 1.05x faster                                                                  |
| regex_dna      | 239 ms                                                       | 247 ms: 1.04x slower                                                                  |
| regex_v8       | 23.6 ms                                                      | 26.2 ms: 1.11x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241010-pythonperf2-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| json_loads           | 24.4 us                                                      | 23.4 us: 1.04x faster                                                                 |
| xml_etree_iterparse  | 103 ms                                                       | 100 ms: 1.03x faster                                                                  |
| pickle_pure_python   | 318 us                                                       | 312 us: 1.02x faster                                                                  |
| xml_etree_generate   | 86.1 ms                                                      | 84.7 ms: 1.02x faster                                                                 |
| pickle               | 10.5 us                                                      | 10.4 us: 1.01x faster                                                                 |
| xml_etree_parse      | 144 ms                                                       | 142 ms: 1.01x faster                                                                  |
| unpickle_list        | 4.66 us                                                      | 4.72 us: 1.01x slower                                                                 |
| unpickle_pure_python | 210 us                                                       | 213 us: 1.02x slower                                                                  |
| unpickle             | 14.8 us                                                      | 15.1 us: 1.02x slower                                                                 |
| xml_etree_process    | 58.4 ms                                                      | 59.6 ms: 1.02x slower                                                                 |
| pickle_dict          | 32.5 us                                                      | 33.9 us: 1.04x slower                                                                 |
| pickle_list          | 4.43 us                                                      | 4.81 us: 1.09x slower                                                                 |
| json_dumps           | 10.2 ms                                                      | 11.1 ms: 1.09x slower                                                                 |
| tomli_loads          | 2.16 sec                                                     | 2.52 sec: 1.17x slower                                                                |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241010-pythonperf2-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.95 ms: 1.04x slower                                                                 |
| python_startup         | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                                 |
| Geometric mean         | (ref)                                                        | 1.09x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241010-pythonperf2-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 10.6 ms: 1.06x slower                                                                 |
| django_template | 38.2 ms                                                      | 41.8 ms: 1.10x slower                                                                 |
| Geometric mean  | (ref)                                                        | 1.08x slower                                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241010-pythonperf2-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 320 ms: 1.41x faster                                                                  |
| async_tree_none_tg         | 431 ms                                                       | 310 ms: 1.39x faster                                                                  |
| async_tree_memoization_tg  | 540 ms                                                       | 391 ms: 1.38x faster                                                                  |
| async_tree_memoization     | 544 ms                                                       | 400 ms: 1.36x faster                                                                  |
| generators                 | 37.4 ms                                                      | 28.0 ms: 1.34x faster                                                                 |
| async_tree_io_tg           | 1.05 sec                                                     | 795 ms: 1.32x faster                                                                  |
| deepcopy                   | 368 us                                                       | 284 us: 1.30x faster                                                                  |
| comprehensions             | 21.9 us                                                      | 16.9 us: 1.29x faster                                                                 |
| async_tree_io              | 1.04 sec                                                     | 812 ms: 1.28x faster                                                                  |
| deepcopy_memo              | 36.8 us                                                      | 28.9 us: 1.27x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 549 ms: 1.27x faster                                                                  |
| unpack_sequence            | 53.2 ns                                                      | 42.7 ns: 1.24x faster                                                                 |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 571 ms: 1.22x faster                                                                  |
| pathlib                    | 18.9 ms                                                      | 15.9 ms: 1.19x faster                                                                 |
| deepcopy_reduce            | 3.37 us                                                      | 2.90 us: 1.16x faster                                                                 |
| go                         | 150 ms                                                       | 133 ms: 1.13x faster                                                                  |
| raytrace                   | 298 ms                                                       | 266 ms: 1.12x faster                                                                  |
| crypto_pyaes               | 80.3 ms                                                      | 72.9 ms: 1.10x faster                                                                 |
| coroutines                 | 23.0 ms                                                      | 21.0 ms: 1.10x faster                                                                 |
| async_generators           | 390 ms                                                       | 358 ms: 1.09x faster                                                                  |
| bench_thread_pool          | 950 us                                                       | 881 us: 1.08x faster                                                                  |
| sympy_sum                  | 162 ms                                                       | 151 ms: 1.07x faster                                                                  |
| scimark_monte_carlo        | 69.0 ms                                                      | 64.4 ms: 1.07x faster                                                                 |
| logging_format             | 7.48 us                                                      | 7.09 us: 1.06x faster                                                                 |
| pidigits                   | 265 ms                                                       | 252 ms: 1.05x faster                                                                  |
| tornado_http               | 121 ms                                                       | 116 ms: 1.05x faster                                                                  |
| regex_compile              | 144 ms                                                       | 137 ms: 1.05x faster                                                                  |
| sympy_str                  | 302 ms                                                       | 289 ms: 1.04x faster                                                                  |
| scimark_lu                 | 98.8 ms                                                      | 94.8 ms: 1.04x faster                                                                 |
| json_loads                 | 24.4 us                                                      | 23.4 us: 1.04x faster                                                                 |
| mdp                        | 2.57 sec                                                     | 2.48 sec: 1.04x faster                                                                |
| chaos                      | 64.0 ms                                                      | 61.9 ms: 1.03x faster                                                                 |
| sympy_integrate            | 23.9 ms                                                      | 23.2 ms: 1.03x faster                                                                 |
| logging_simple             | 6.71 us                                                      | 6.50 us: 1.03x faster                                                                 |
| nqueens                    | 89.9 ms                                                      | 87.2 ms: 1.03x faster                                                                 |
| xml_etree_iterparse        | 103 ms                                                       | 100 ms: 1.03x faster                                                                  |
| pprint_pformat             | 1.65 sec                                                     | 1.61 sec: 1.03x faster                                                                |
| asyncio_tcp                | 378 ms                                                       | 370 ms: 1.02x faster                                                                  |
| scimark_fft                | 301 ms                                                       | 294 ms: 1.02x faster                                                                  |
| pickle_pure_python         | 318 us                                                       | 312 us: 1.02x faster                                                                  |
| pprint_safe_repr           | 807 ms                                                       | 792 ms: 1.02x faster                                                                  |
| meteor_contest             | 128 ms                                                       | 126 ms: 1.02x faster                                                                  |
| 2to3                       | 285 ms                                                       | 280 ms: 1.02x faster                                                                  |
| xml_etree_generate         | 86.1 ms                                                      | 84.7 ms: 1.02x faster                                                                 |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.14 ms: 1.02x faster                                                                 |
| pickle                     | 10.5 us                                                      | 10.4 us: 1.01x faster                                                                 |
| xml_etree_parse            | 144 ms                                                       | 142 ms: 1.01x faster                                                                  |
| sqlite_synth               | 2.77 us                                                      | 2.74 us: 1.01x faster                                                                 |
| pycparser                  | 1.23 sec                                                     | 1.22 sec: 1.01x faster                                                                |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.57 sec: 1.01x faster                                                                |
| scimark_sor                | 109 ms                                                       | 108 ms: 1.01x faster                                                                  |
| sqlglot_transpile          | 1.78 ms                                                      | 1.79 ms: 1.01x slower                                                                 |
| asyncio_websockets         | 387 ms                                                       | 392 ms: 1.01x slower                                                                  |
| unpickle_list              | 4.66 us                                                      | 4.72 us: 1.01x slower                                                                 |
| unpickle_pure_python       | 210 us                                                       | 213 us: 1.02x slower                                                                  |
| unpickle                   | 14.8 us                                                      | 15.1 us: 1.02x slower                                                                 |
| xml_etree_process          | 58.4 ms                                                      | 59.6 ms: 1.02x slower                                                                 |
| fannkuch                   | 350 ms                                                       | 358 ms: 1.02x slower                                                                  |
| sqlglot_parse              | 1.38 ms                                                      | 1.41 ms: 1.03x slower                                                                 |
| sympy_expand               | 484 ms                                                       | 497 ms: 1.03x slower                                                                  |
| sqlglot_normalize          | 116 ms                                                       | 119 ms: 1.03x slower                                                                  |
| sqlglot_optimize           | 57.5 ms                                                      | 59.5 ms: 1.04x slower                                                                 |
| regex_dna                  | 239 ms                                                       | 247 ms: 1.04x slower                                                                  |
| python_startup_no_site     | 8.64 ms                                                      | 8.95 ms: 1.04x slower                                                                 |
| deltablue                  | 3.24 ms                                                      | 3.36 ms: 1.04x slower                                                                 |
| logging_silent             | 94.4 ns                                                      | 98.0 ns: 1.04x slower                                                                 |
| float                      | 76.6 ms                                                      | 79.7 ms: 1.04x slower                                                                 |
| spectral_norm              | 91.6 ms                                                      | 95.3 ms: 1.04x slower                                                                 |
| hexiom                     | 5.96 ms                                                      | 6.20 ms: 1.04x slower                                                                 |
| pickle_dict                | 32.5 us                                                      | 33.9 us: 1.04x slower                                                                 |
| mako                       | 10.0 ms                                                      | 10.6 ms: 1.06x slower                                                                 |
| pickle_list                | 4.43 us                                                      | 4.81 us: 1.09x slower                                                                 |
| json_dumps                 | 10.2 ms                                                      | 11.1 ms: 1.09x slower                                                                 |
| django_template            | 38.2 ms                                                      | 41.8 ms: 1.10x slower                                                                 |
| pyflate                    | 439 ms                                                       | 481 ms: 1.10x slower                                                                  |
| richards_super             | 51.3 ms                                                      | 56.8 ms: 1.11x slower                                                                 |
| regex_v8                   | 23.6 ms                                                      | 26.2 ms: 1.11x slower                                                                 |
| richards                   | 45.7 ms                                                      | 50.8 ms: 1.11x slower                                                                 |
| telco                      | 6.96 ms                                                      | 7.87 ms: 1.13x slower                                                                 |
| typing_runtime_protocols   | 152 us                                                       | 173 us: 1.14x slower                                                                  |
| python_startup             | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                                 |
| tomli_loads                | 2.16 sec                                                     | 2.52 sec: 1.17x slower                                                                |
| coverage                   | 66.7 ms                                                      | 81.9 ms: 1.23x slower                                                                 |
| create_gc_cycles           | 1.59 ms                                                      | 2.02 ms: 1.27x slower                                                                 |
| gc_traversal               | 3.48 ms                                                      | 4.74 ms: 1.36x slower                                                                 |
| bench_mp_pool              | 4.76 ms                                                      | 1.92 sec: 403.47x slower                                                              |
| Geometric mean             | (ref)                                                        | 1.04x slower                                                                          |

Benchmark hidden because not significant (5): json, regex_effbot, docutils, dulwich_log, nbody
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241010-3.14.0a0-94f8fd0/bm-20241010-pythonperf2-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.033x faster
# HPT report

- Reliability score: 97.17% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x