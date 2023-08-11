
# Results vs. 3.10.4

- fork: faster-cpython
- ref: no_untrack_dicts
- machine: linux-x86_64
- commit hash: f204b0a
- commit date: 2023-08-10
- overall geometric mean: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230810-pythonperf2-x86_64-faster%2dcpython-no_untrack_dicts-3.13.0a0-f204b0a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| docutils       | 3.40 sec                                                     | 2.93 sec: 1.16x faster                                                            |
| tornado_http   | 152 ms                                                       | 120 ms: 1.27x faster                                                              |
| Geometric mean | (ref)                                                        | 1.21x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230810-pythonperf2-x86_64-faster%2dcpython-no_untrack_dicts-3.13.0a0-f204b0a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 87.8 ms: 1.56x faster                                                             |
| float          | 110 ms                                                       | 81.3 ms: 1.36x faster                                                             |
| pidigits       | 271 ms                                                       | 259 ms: 1.04x faster                                                              |
| Geometric mean | (ref)                                                        | 1.30x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230810-pythonperf2-x86_64-faster%2dcpython-no_untrack_dicts-3.13.0a0-f204b0a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 149 ms: 1.30x faster                                                              |
| regex_v8       | 26.6 ms                                                      | 24.2 ms: 1.10x faster                                                             |
| regex_dna      | 259 ms                                                       | 252 ms: 1.03x faster                                                              |
| regex_effbot   | 2.99 ms                                                      | 3.62 ms: 1.21x slower                                                             |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230810-pythonperf2-x86_64-faster%2dcpython-no_untrack_dicts-3.13.0a0-f204b0a |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 220 us: 1.46x faster                                                              |
| pickle_pure_python   | 457 us                                                       | 315 us: 1.45x faster                                                              |
| json_dumps           | 14.2 ms                                                      | 10.2 ms: 1.39x faster                                                             |
| tomli_loads          | 2.97 sec                                                     | 2.29 sec: 1.30x faster                                                            |
| xml_etree_process    | 76.0 ms                                                      | 60.4 ms: 1.26x faster                                                             |
| json_loads           | 30.0 us                                                      | 25.5 us: 1.18x faster                                                             |
| xml_etree_parse      | 162 ms                                                       | 147 ms: 1.10x faster                                                              |
| xml_etree_generate   | 94.6 ms                                                      | 87.1 ms: 1.09x faster                                                             |
| xml_etree_iterparse  | 110 ms                                                       | 107 ms: 1.04x faster                                                              |
| pickle               | 9.94 us                                                      | 10.2 us: 1.02x slower                                                             |
| unpickle             | 14.2 us                                                      | 14.7 us: 1.04x slower                                                             |
| unpickle_list        | 4.49 us                                                      | 4.75 us: 1.06x slower                                                             |
| pickle_dict          | 30.0 us                                                      | 32.0 us: 1.07x slower                                                             |
| pickle_list          | 4.11 us                                                      | 4.52 us: 1.10x slower                                                             |
| Geometric mean       | (ref)                                                        | 1.13x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230810-pythonperf2-x86_64-faster%2dcpython-no_untrack_dicts-3.13.0a0-f204b0a |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.5 ms: 1.00x slower                                                             |
| python_startup_no_site | 7.32 ms                                                      | 8.55 ms: 1.17x slower                                                             |
| Geometric mean         | (ref)                                                        | 1.08x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230810-pythonperf2-x86_64-faster%2dcpython-no_untrack_dicts-3.13.0a0-f204b0a |
|-----------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako      | 14.7 ms                                                      | 10.3 ms: 1.42x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230810-pythonperf2-x86_64-faster%2dcpython-no_untrack_dicts-3.13.0a0-f204b0a |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 153 us: 3.42x faster                                                              |
| asyncio_tcp              | 782 ms                                                       | 369 ms: 2.12x faster                                                              |
| deltablue                | 7.47 ms                                                      | 3.78 ms: 1.98x faster                                                             |
| asyncio_tcp_ssl          | 3.09 sec                                                     | 1.58 sec: 1.96x faster                                                            |
| chaos                    | 107 ms                                                       | 62.1 ms: 1.72x faster                                                             |
| raytrace                 | 488 ms                                                       | 288 ms: 1.69x faster                                                              |
| logging_silent           | 166 ns                                                       | 98.4 ns: 1.68x faster                                                             |
| crypto_pyaes             | 118 ms                                                       | 74.3 ms: 1.59x faster                                                             |
| generators               | 58.0 ms                                                      | 36.4 ms: 1.59x faster                                                             |
| scimark_lu               | 164 ms                                                       | 104 ms: 1.58x faster                                                              |
| sqlglot_parse            | 2.26 ms                                                      | 1.44 ms: 1.57x faster                                                             |
| nbody                    | 137 ms                                                       | 87.8 ms: 1.56x faster                                                             |
| async_tree_io            | 1.61 sec                                                     | 1.04 sec: 1.55x faster                                                            |
| bench_mp_pool            | 7.18 ms                                                      | 4.65 ms: 1.54x faster                                                             |
| async_tree_none          | 700 ms                                                       | 453 ms: 1.54x faster                                                              |
| async_tree_memoization   | 824 ms                                                       | 535 ms: 1.54x faster                                                              |
| scimark_monte_carlo      | 109 ms                                                       | 72.4 ms: 1.51x faster                                                             |
| richards_super           | 90.8 ms                                                      | 60.4 ms: 1.50x faster                                                             |
| go                       | 259 ms                                                       | 173 ms: 1.50x faster                                                              |
| sqlglot_transpile        | 2.71 ms                                                      | 1.85 ms: 1.47x faster                                                             |
| spectral_norm            | 136 ms                                                       | 93.0 ms: 1.47x faster                                                             |
| unpickle_pure_python     | 321 us                                                       | 220 us: 1.46x faster                                                              |
| pickle_pure_python       | 457 us                                                       | 315 us: 1.45x faster                                                              |
| hexiom                   | 9.52 ms                                                      | 6.57 ms: 1.45x faster                                                             |
| mako                     | 14.7 ms                                                      | 10.3 ms: 1.42x faster                                                             |
| json_dumps               | 14.2 ms                                                      | 10.2 ms: 1.39x faster                                                             |
| richards                 | 74.1 ms                                                      | 53.5 ms: 1.39x faster                                                             |
| async_tree_cpu_io_mixed  | 952 ms                                                       | 698 ms: 1.36x faster                                                              |
| pyflate                  | 697 ms                                                       | 512 ms: 1.36x faster                                                              |
| float                    | 110 ms                                                       | 81.3 ms: 1.36x faster                                                             |
| logging_simple           | 8.90 us                                                      | 6.73 us: 1.32x faster                                                             |
| regex_compile            | 194 ms                                                       | 149 ms: 1.30x faster                                                              |
| logging_format           | 9.57 us                                                      | 7.36 us: 1.30x faster                                                             |
| tomli_loads              | 2.97 sec                                                     | 2.29 sec: 1.30x faster                                                            |
| deepcopy_memo            | 48.9 us                                                      | 37.9 us: 1.29x faster                                                             |
| pprint_pformat           | 2.15 sec                                                     | 1.68 sec: 1.29x faster                                                            |
| pprint_safe_repr         | 1.05 sec                                                     | 820 ms: 1.28x faster                                                              |
| fannkuch                 | 496 ms                                                       | 389 ms: 1.27x faster                                                              |
| scimark_sparse_mat_mult  | 5.19 ms                                                      | 4.10 ms: 1.27x faster                                                             |
| tornado_http             | 152 ms                                                       | 120 ms: 1.27x faster                                                              |
| coroutines               | 30.4 ms                                                      | 24.1 ms: 1.26x faster                                                             |
| xml_etree_process        | 76.0 ms                                                      | 60.4 ms: 1.26x faster                                                             |
| pycparser                | 1.66 sec                                                     | 1.33 sec: 1.25x faster                                                            |
| nqueens                  | 112 ms                                                       | 90.6 ms: 1.24x faster                                                             |
| create_gc_cycles         | 1.82 ms                                                      | 1.47 ms: 1.24x faster                                                             |
| sqlglot_normalize        | 144 ms                                                       | 117 ms: 1.23x faster                                                              |
| comprehensions           | 26.9 us                                                      | 22.3 us: 1.21x faster                                                             |
| scimark_fft              | 359 ms                                                       | 301 ms: 1.19x faster                                                              |
| bench_thread_pool        | 1.14 ms                                                      | 958 us: 1.19x faster                                                              |
| sqlglot_optimize         | 70.3 ms                                                      | 59.4 ms: 1.18x faster                                                             |
| scimark_sor              | 177 ms                                                       | 150 ms: 1.18x faster                                                              |
| json_loads               | 30.0 us                                                      | 25.5 us: 1.18x faster                                                             |
| mdp                      | 3.03 sec                                                     | 2.58 sec: 1.17x faster                                                            |
| deepcopy                 | 454 us                                                       | 389 us: 1.17x faster                                                              |
| deepcopy_reduce          | 4.03 us                                                      | 3.45 us: 1.17x faster                                                             |
| dulwich_log              | 80.1 ms                                                      | 68.7 ms: 1.17x faster                                                             |
| docutils                 | 3.40 sec                                                     | 2.93 sec: 1.16x faster                                                            |
| json                     | 5.96 ms                                                      | 5.20 ms: 1.15x faster                                                             |
| pathlib                  | 21.7 ms                                                      | 19.7 ms: 1.10x faster                                                             |
| regex_v8                 | 26.6 ms                                                      | 24.2 ms: 1.10x faster                                                             |
| xml_etree_parse          | 162 ms                                                       | 147 ms: 1.10x faster                                                              |
| sqlite_synth             | 2.97 us                                                      | 2.71 us: 1.09x faster                                                             |
| xml_etree_generate       | 94.6 ms                                                      | 87.1 ms: 1.09x faster                                                             |
| async_generators         | 422 ms                                                       | 392 ms: 1.08x faster                                                              |
| meteor_contest           | 137 ms                                                       | 129 ms: 1.06x faster                                                              |
| pidigits                 | 271 ms                                                       | 259 ms: 1.04x faster                                                              |
| xml_etree_iterparse      | 110 ms                                                       | 107 ms: 1.04x faster                                                              |
| regex_dna                | 259 ms                                                       | 252 ms: 1.03x faster                                                              |
| python_startup           | 11.5 ms                                                      | 11.5 ms: 1.00x slower                                                             |
| unpack_sequence          | 59.5 ns                                                      | 60.1 ns: 1.01x slower                                                             |
| pickle                   | 9.94 us                                                      | 10.2 us: 1.02x slower                                                             |
| unpickle                 | 14.2 us                                                      | 14.7 us: 1.04x slower                                                             |
| unpickle_list            | 4.49 us                                                      | 4.75 us: 1.06x slower                                                             |
| pickle_dict              | 30.0 us                                                      | 32.0 us: 1.07x slower                                                             |
| gc_traversal             | 3.45 ms                                                      | 3.80 ms: 1.10x slower                                                             |
| pickle_list              | 4.11 us                                                      | 4.52 us: 1.10x slower                                                             |
| telco                    | 7.14 ms                                                      | 8.08 ms: 1.13x slower                                                             |
| python_startup_no_site   | 7.32 ms                                                      | 8.55 ms: 1.17x slower                                                             |
| regex_effbot             | 2.99 ms                                                      | 3.62 ms: 1.21x slower                                                             |
| dask                     | 463 ms                                                       | 587 ms: 1.27x slower                                                              |
| coverage                 | 64.0 ms                                                      | 81.5 ms: 1.27x slower                                                             |
| Geometric mean           | (ref)                                                        | 1.26x faster                                                                      |

Benchmark hidden because not significant (1): mypy2
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
