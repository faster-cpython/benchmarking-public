
# Results vs. 3.10.4

- fork: faster-cpython
- ref: gc_scan_roots
- machine: linux-x86_64
- commit hash: fb9e869
- commit date: 2023-08-04
- overall geometric mean: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230804-pythonperf2-x86_64-faster%2dcpython-gc_scan_roots-3.13.0a0-fb9e869 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| docutils       | 3.40 sec                                                     | 2.98 sec: 1.14x faster                                                         |
| tornado_http   | 152 ms                                                       | 120 ms: 1.27x faster                                                           |
| Geometric mean | (ref)                                                        | 1.20x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230804-pythonperf2-x86_64-faster%2dcpython-gc_scan_roots-3.13.0a0-fb9e869 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 90.2 ms: 1.52x faster                                                          |
| float          | 110 ms                                                       | 81.9 ms: 1.35x faster                                                          |
| pidigits       | 271 ms                                                       | 260 ms: 1.04x faster                                                           |
| Geometric mean | (ref)                                                        | 1.29x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230804-pythonperf2-x86_64-faster%2dcpython-gc_scan_roots-3.13.0a0-fb9e869 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 150 ms: 1.29x faster                                                           |
| regex_v8       | 26.6 ms                                                      | 24.3 ms: 1.10x faster                                                          |
| regex_dna      | 259 ms                                                       | 245 ms: 1.06x faster                                                           |
| regex_effbot   | 2.99 ms                                                      | 3.47 ms: 1.16x slower                                                          |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230804-pythonperf2-x86_64-faster%2dcpython-gc_scan_roots-3.13.0a0-fb9e869 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                       | 318 us: 1.44x faster                                                           |
| json_dumps           | 14.2 ms                                                      | 10.3 ms: 1.38x faster                                                          |
| unpickle_pure_python | 321 us                                                       | 234 us: 1.37x faster                                                           |
| tomli_loads          | 2.97 sec                                                     | 2.34 sec: 1.27x faster                                                         |
| xml_etree_process    | 76.0 ms                                                      | 60.4 ms: 1.26x faster                                                          |
| json_loads           | 30.0 us                                                      | 25.2 us: 1.19x faster                                                          |
| xml_etree_parse      | 162 ms                                                       | 146 ms: 1.10x faster                                                           |
| xml_etree_generate   | 94.6 ms                                                      | 87.2 ms: 1.08x faster                                                          |
| xml_etree_iterparse  | 110 ms                                                       | 107 ms: 1.03x faster                                                           |
| pickle               | 9.94 us                                                      | 10.1 us: 1.01x slower                                                          |
| unpickle             | 14.2 us                                                      | 14.5 us: 1.03x slower                                                          |
| unpickle_list        | 4.49 us                                                      | 4.67 us: 1.04x slower                                                          |
| pickle_dict          | 30.0 us                                                      | 32.9 us: 1.10x slower                                                          |
| pickle_list          | 4.11 us                                                      | 4.53 us: 1.10x slower                                                          |
| Geometric mean       | (ref)                                                        | 1.12x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230804-pythonperf2-x86_64-faster%2dcpython-gc_scan_roots-3.13.0a0-fb9e869 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.6 ms: 1.01x slower                                                          |
| python_startup_no_site | 7.32 ms                                                      | 8.68 ms: 1.19x slower                                                          |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230804-pythonperf2-x86_64-faster%2dcpython-gc_scan_roots-3.13.0a0-fb9e869 |
|-----------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako      | 14.7 ms                                                      | 10.3 ms: 1.43x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230804-pythonperf2-x86_64-faster%2dcpython-gc_scan_roots-3.13.0a0-fb9e869 |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 156 us: 3.34x faster                                                           |
| asyncio_tcp              | 782 ms                                                       | 369 ms: 2.12x faster                                                           |
| deltablue                | 7.47 ms                                                      | 3.72 ms: 2.01x faster                                                          |
| asyncio_tcp_ssl          | 3.09 sec                                                     | 1.58 sec: 1.96x faster                                                         |
| raytrace                 | 488 ms                                                       | 282 ms: 1.73x faster                                                           |
| chaos                    | 107 ms                                                       | 62.0 ms: 1.73x faster                                                          |
| logging_silent           | 166 ns                                                       | 98.3 ns: 1.69x faster                                                          |
| scimark_lu               | 164 ms                                                       | 97.9 ms: 1.67x faster                                                          |
| crypto_pyaes             | 118 ms                                                       | 72.9 ms: 1.62x faster                                                          |
| scimark_monte_carlo      | 109 ms                                                       | 68.9 ms: 1.59x faster                                                          |
| sqlglot_parse            | 2.26 ms                                                      | 1.44 ms: 1.57x faster                                                          |
| generators               | 58.0 ms                                                      | 37.1 ms: 1.56x faster                                                          |
| nbody                    | 137 ms                                                       | 90.2 ms: 1.52x faster                                                          |
| bench_mp_pool            | 7.18 ms                                                      | 4.82 ms: 1.49x faster                                                          |
| go                       | 259 ms                                                       | 177 ms: 1.47x faster                                                           |
| sqlglot_transpile        | 2.71 ms                                                      | 1.85 ms: 1.46x faster                                                          |
| hexiom                   | 9.52 ms                                                      | 6.51 ms: 1.46x faster                                                          |
| richards_super           | 90.8 ms                                                      | 62.2 ms: 1.46x faster                                                          |
| async_tree_none          | 700 ms                                                       | 479 ms: 1.46x faster                                                           |
| async_tree_io            | 1.61 sec                                                     | 1.11 sec: 1.45x faster                                                         |
| pickle_pure_python       | 457 us                                                       | 318 us: 1.44x faster                                                           |
| async_tree_memoization   | 824 ms                                                       | 575 ms: 1.43x faster                                                           |
| mako                     | 14.7 ms                                                      | 10.3 ms: 1.43x faster                                                          |
| spectral_norm            | 136 ms                                                       | 96.9 ms: 1.41x faster                                                          |
| json_dumps               | 14.2 ms                                                      | 10.3 ms: 1.38x faster                                                          |
| unpickle_pure_python     | 321 us                                                       | 234 us: 1.37x faster                                                           |
| pyflate                  | 697 ms                                                       | 514 ms: 1.36x faster                                                           |
| richards                 | 74.1 ms                                                      | 54.9 ms: 1.35x faster                                                          |
| float                    | 110 ms                                                       | 81.9 ms: 1.35x faster                                                          |
| logging_simple           | 8.90 us                                                      | 6.76 us: 1.32x faster                                                          |
| async_tree_cpu_io_mixed  | 952 ms                                                       | 723 ms: 1.32x faster                                                           |
| logging_format           | 9.57 us                                                      | 7.40 us: 1.29x faster                                                          |
| regex_compile            | 194 ms                                                       | 150 ms: 1.29x faster                                                           |
| coroutines               | 30.4 ms                                                      | 23.7 ms: 1.29x faster                                                          |
| pprint_pformat           | 2.15 sec                                                     | 1.69 sec: 1.28x faster                                                         |
| deepcopy_memo            | 48.9 us                                                      | 38.3 us: 1.28x faster                                                          |
| pprint_safe_repr         | 1.05 sec                                                     | 825 ms: 1.27x faster                                                           |
| tomli_loads              | 2.97 sec                                                     | 2.34 sec: 1.27x faster                                                         |
| tornado_http             | 152 ms                                                       | 120 ms: 1.27x faster                                                           |
| fannkuch                 | 496 ms                                                       | 393 ms: 1.26x faster                                                           |
| xml_etree_process        | 76.0 ms                                                      | 60.4 ms: 1.26x faster                                                          |
| mypy2                    | 466 ms                                                       | 373 ms: 1.25x faster                                                           |
| pycparser                | 1.66 sec                                                     | 1.34 sec: 1.24x faster                                                         |
| sqlglot_normalize        | 144 ms                                                       | 118 ms: 1.23x faster                                                           |
| nqueens                  | 112 ms                                                       | 92.3 ms: 1.22x faster                                                          |
| scimark_sor              | 177 ms                                                       | 146 ms: 1.21x faster                                                           |
| comprehensions           | 26.9 us                                                      | 22.5 us: 1.20x faster                                                          |
| bench_thread_pool        | 1.14 ms                                                      | 952 us: 1.19x faster                                                           |
| sqlglot_optimize         | 70.3 ms                                                      | 58.9 ms: 1.19x faster                                                          |
| mdp                      | 3.03 sec                                                     | 2.55 sec: 1.19x faster                                                         |
| json_loads               | 30.0 us                                                      | 25.2 us: 1.19x faster                                                          |
| scimark_sparse_mat_mult  | 5.19 ms                                                      | 4.41 ms: 1.18x faster                                                          |
| deepcopy                 | 454 us                                                       | 385 us: 1.18x faster                                                           |
| scimark_fft              | 359 ms                                                       | 306 ms: 1.18x faster                                                           |
| dulwich_log              | 80.1 ms                                                      | 68.7 ms: 1.17x faster                                                          |
| deepcopy_reduce          | 4.03 us                                                      | 3.49 us: 1.15x faster                                                          |
| docutils                 | 3.40 sec                                                     | 2.98 sec: 1.14x faster                                                         |
| json                     | 5.96 ms                                                      | 5.26 ms: 1.13x faster                                                          |
| pathlib                  | 21.7 ms                                                      | 19.6 ms: 1.11x faster                                                          |
| xml_etree_parse          | 162 ms                                                       | 146 ms: 1.10x faster                                                           |
| sqlite_synth             | 2.97 us                                                      | 2.70 us: 1.10x faster                                                          |
| regex_v8                 | 26.6 ms                                                      | 24.3 ms: 1.10x faster                                                          |
| xml_etree_generate       | 94.6 ms                                                      | 87.2 ms: 1.08x faster                                                          |
| async_generators         | 422 ms                                                       | 396 ms: 1.07x faster                                                           |
| regex_dna                | 259 ms                                                       | 245 ms: 1.06x faster                                                           |
| meteor_contest           | 137 ms                                                       | 129 ms: 1.06x faster                                                           |
| create_gc_cycles         | 1.82 ms                                                      | 1.73 ms: 1.05x faster                                                          |
| pidigits                 | 271 ms                                                       | 260 ms: 1.04x faster                                                           |
| xml_etree_iterparse      | 110 ms                                                       | 107 ms: 1.03x faster                                                           |
| python_startup           | 11.5 ms                                                      | 11.6 ms: 1.01x slower                                                          |
| pickle                   | 9.94 us                                                      | 10.1 us: 1.01x slower                                                          |
| unpickle                 | 14.2 us                                                      | 14.5 us: 1.03x slower                                                          |
| unpickle_list            | 4.49 us                                                      | 4.67 us: 1.04x slower                                                          |
| pickle_dict              | 30.0 us                                                      | 32.9 us: 1.10x slower                                                          |
| pickle_list              | 4.11 us                                                      | 4.53 us: 1.10x slower                                                          |
| telco                    | 7.14 ms                                                      | 8.00 ms: 1.12x slower                                                          |
| regex_effbot             | 2.99 ms                                                      | 3.47 ms: 1.16x slower                                                          |
| gc_traversal             | 3.45 ms                                                      | 4.08 ms: 1.18x slower                                                          |
| python_startup_no_site   | 7.32 ms                                                      | 8.68 ms: 1.19x slower                                                          |
| dask                     | 463 ms                                                       | 594 ms: 1.28x slower                                                           |
| coverage                 | 64.0 ms                                                      | 87.5 ms: 1.37x slower                                                          |
| Geometric mean           | (ref)                                                        | 1.26x faster                                                                   |

Benchmark hidden because not significant (1): unpack_sequence
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
