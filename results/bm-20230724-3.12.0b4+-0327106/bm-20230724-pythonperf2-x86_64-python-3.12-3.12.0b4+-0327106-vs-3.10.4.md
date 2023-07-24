
# Results vs. 3.10.4

- fork: python
- ref: 3.12
- machine: linux-x86_64
- commit hash: 0327106
- commit date: 2023-07-24
- overall geometric mean: 1.30x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230724-pythonperf2-x86_64-python-3.12-3.12.0b4+-0327106 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 285 ms: 1.23x faster                                         |
| docutils       | 3.40 sec                                                     | 2.89 sec: 1.18x faster                                       |
| tornado_http   | 152 ms                                                       | 120 ms: 1.27x faster                                         |
| Geometric mean | (ref)                                                        | 1.22x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230724-pythonperf2-x86_64-python-3.12-3.12.0b4+-0327106 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 87.1 ms: 1.58x faster                                        |
| float          | 110 ms                                                       | 79.2 ms: 1.39x faster                                        |
| pidigits       | 271 ms                                                       | 260 ms: 1.04x faster                                         |
| Geometric mean | (ref)                                                        | 1.32x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230724-pythonperf2-x86_64-python-3.12-3.12.0b4+-0327106 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 145 ms: 1.34x faster                                         |
| regex_v8       | 26.6 ms                                                      | 23.7 ms: 1.12x faster                                        |
| regex_dna      | 259 ms                                                       | 246 ms: 1.05x faster                                         |
| regex_effbot   | 2.99 ms                                                      | 3.50 ms: 1.17x slower                                        |
| Geometric mean | (ref)                                                        | 1.08x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230724-pythonperf2-x86_64-python-3.12-3.12.0b4+-0327106 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 213 us: 1.51x faster                                         |
| pickle_pure_python   | 457 us                                                       | 319 us: 1.44x faster                                         |
| json_dumps           | 14.2 ms                                                      | 10.3 ms: 1.38x faster                                        |
| tomli_loads          | 2.97 sec                                                     | 2.17 sec: 1.37x faster                                       |
| xml_etree_process    | 76.0 ms                                                      | 58.9 ms: 1.29x faster                                        |
| json_loads           | 30.0 us                                                      | 25.2 us: 1.19x faster                                        |
| xml_etree_generate   | 94.6 ms                                                      | 85.3 ms: 1.11x faster                                        |
| xml_etree_parse      | 162 ms                                                       | 146 ms: 1.11x faster                                         |
| xml_etree_iterparse  | 110 ms                                                       | 104 ms: 1.06x faster                                         |
| unpickle             | 14.2 us                                                      | 14.7 us: 1.03x slower                                        |
| pickle               | 9.94 us                                                      | 10.4 us: 1.05x slower                                        |
| unpickle_list        | 4.49 us                                                      | 4.72 us: 1.05x slower                                        |
| pickle_list          | 4.11 us                                                      | 4.44 us: 1.08x slower                                        |
| pickle_dict          | 30.0 us                                                      | 33.4 us: 1.11x slower                                        |
| Geometric mean       | (ref)                                                        | 1.14x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230724-pythonperf2-x86_64-python-3.12-3.12.0b4+-0327106 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 7.32 ms                                                      | 8.51 ms: 1.16x slower                                        |
| Geometric mean         | (ref)                                                        | 1.08x slower                                                 |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230724-pythonperf2-x86_64-python-3.12-3.12.0b4+-0327106 |
|-----------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| mako      | 14.7 ms                                                      | 9.96 ms: 1.47x faster                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230724-pythonperf2-x86_64-python-3.12-3.12.0b4+-0327106 |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 154 us: 3.39x faster                                         |
| deltablue                | 7.47 ms                                                      | 3.21 ms: 2.33x faster                                        |
| asyncio_tcp              | 782 ms                                                       | 380 ms: 2.06x faster                                         |
| asyncio_tcp_ssl          | 3.09 sec                                                     | 1.57 sec: 1.97x faster                                       |
| richards_super           | 90.8 ms                                                      | 50.5 ms: 1.80x faster                                        |
| go                       | 259 ms                                                       | 145 ms: 1.79x faster                                         |
| chaos                    | 107 ms                                                       | 62.6 ms: 1.71x faster                                        |
| scimark_lu               | 164 ms                                                       | 96.9 ms: 1.69x faster                                        |
| logging_silent           | 166 ns                                                       | 98.3 ns: 1.69x faster                                        |
| richards                 | 74.1 ms                                                      | 44.5 ms: 1.67x faster                                        |
| sqlglot_parse            | 2.26 ms                                                      | 1.39 ms: 1.62x faster                                        |
| hexiom                   | 9.52 ms                                                      | 5.90 ms: 1.61x faster                                        |
| scimark_sor              | 177 ms                                                       | 110 ms: 1.61x faster                                         |
| scimark_monte_carlo      | 109 ms                                                       | 68.0 ms: 1.61x faster                                        |
| generators               | 58.0 ms                                                      | 36.1 ms: 1.60x faster                                        |
| raytrace                 | 488 ms                                                       | 308 ms: 1.58x faster                                         |
| pyflate                  | 697 ms                                                       | 441 ms: 1.58x faster                                         |
| nbody                    | 137 ms                                                       | 87.1 ms: 1.58x faster                                        |
| bench_mp_pool            | 7.18 ms                                                      | 4.68 ms: 1.53x faster                                        |
| sqlglot_transpile        | 2.71 ms                                                      | 1.80 ms: 1.51x faster                                        |
| unpickle_pure_python     | 321 us                                                       | 213 us: 1.51x faster                                         |
| async_tree_io            | 1.61 sec                                                     | 1.07 sec: 1.51x faster                                       |
| async_tree_none          | 700 ms                                                       | 466 ms: 1.50x faster                                         |
| spectral_norm            | 136 ms                                                       | 91.9 ms: 1.48x faster                                        |
| async_tree_memoization   | 824 ms                                                       | 557 ms: 1.48x faster                                         |
| mako                     | 14.7 ms                                                      | 9.96 ms: 1.47x faster                                        |
| crypto_pyaes             | 118 ms                                                       | 81.0 ms: 1.46x faster                                        |
| fannkuch                 | 496 ms                                                       | 344 ms: 1.44x faster                                         |
| pickle_pure_python       | 457 us                                                       | 319 us: 1.44x faster                                         |
| float                    | 110 ms                                                       | 79.2 ms: 1.39x faster                                        |
| json_dumps               | 14.2 ms                                                      | 10.3 ms: 1.38x faster                                        |
| coroutines               | 30.4 ms                                                      | 22.2 ms: 1.37x faster                                        |
| tomli_loads              | 2.97 sec                                                     | 2.17 sec: 1.37x faster                                       |
| pycparser                | 1.66 sec                                                     | 1.24 sec: 1.34x faster                                       |
| regex_compile            | 194 ms                                                       | 145 ms: 1.34x faster                                         |
| async_tree_cpu_io_mixed  | 952 ms                                                       | 711 ms: 1.34x faster                                         |
| deepcopy_memo            | 48.9 us                                                      | 36.7 us: 1.33x faster                                        |
| logging_simple           | 8.90 us                                                      | 6.80 us: 1.31x faster                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.65 sec: 1.31x faster                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 809 ms: 1.30x faster                                         |
| xml_etree_process        | 76.0 ms                                                      | 58.9 ms: 1.29x faster                                        |
| tornado_http             | 152 ms                                                       | 120 ms: 1.27x faster                                         |
| logging_format           | 9.57 us                                                      | 7.54 us: 1.27x faster                                        |
| mypy2                    | 466 ms                                                       | 368 ms: 1.27x faster                                         |
| comprehensions           | 26.9 us                                                      | 21.6 us: 1.25x faster                                        |
| nqueens                  | 112 ms                                                       | 91.0 ms: 1.24x faster                                        |
| sqlglot_normalize        | 144 ms                                                       | 117 ms: 1.23x faster                                         |
| scimark_fft              | 359 ms                                                       | 293 ms: 1.23x faster                                         |
| 2to3                     | 350 ms                                                       | 285 ms: 1.23x faster                                         |
| sqlglot_optimize         | 70.3 ms                                                      | 57.6 ms: 1.22x faster                                        |
| deepcopy                 | 454 us                                                       | 372 us: 1.22x faster                                         |
| scimark_sparse_mat_mult  | 5.19 ms                                                      | 4.28 ms: 1.21x faster                                        |
| unpack_sequence          | 59.5 ns                                                      | 49.1 ns: 1.21x faster                                        |
| dulwich_log              | 80.1 ms                                                      | 66.3 ms: 1.21x faster                                        |
| mdp                      | 3.03 sec                                                     | 2.52 sec: 1.20x faster                                       |
| json_loads               | 30.0 us                                                      | 25.2 us: 1.19x faster                                        |
| deepcopy_reduce          | 4.03 us                                                      | 3.40 us: 1.19x faster                                        |
| docutils                 | 3.40 sec                                                     | 2.89 sec: 1.18x faster                                       |
| bench_thread_pool        | 1.14 ms                                                      | 971 us: 1.17x faster                                         |
| json                     | 5.96 ms                                                      | 5.21 ms: 1.14x faster                                        |
| pathlib                  | 21.7 ms                                                      | 19.3 ms: 1.13x faster                                        |
| regex_v8                 | 26.6 ms                                                      | 23.7 ms: 1.12x faster                                        |
| create_gc_cycles         | 1.82 ms                                                      | 1.64 ms: 1.11x faster                                        |
| xml_etree_generate       | 94.6 ms                                                      | 85.3 ms: 1.11x faster                                        |
| xml_etree_parse          | 162 ms                                                       | 146 ms: 1.11x faster                                         |
| sqlite_synth             | 2.97 us                                                      | 2.75 us: 1.08x faster                                        |
| meteor_contest           | 137 ms                                                       | 127 ms: 1.07x faster                                         |
| async_generators         | 422 ms                                                       | 396 ms: 1.07x faster                                         |
| xml_etree_iterparse      | 110 ms                                                       | 104 ms: 1.06x faster                                         |
| regex_dna                | 259 ms                                                       | 246 ms: 1.05x faster                                         |
| pidigits                 | 271 ms                                                       | 260 ms: 1.04x faster                                         |
| telco                    | 7.14 ms                                                      | 7.08 ms: 1.01x faster                                        |
| unpickle                 | 14.2 us                                                      | 14.7 us: 1.03x slower                                        |
| pickle                   | 9.94 us                                                      | 10.4 us: 1.05x slower                                        |
| unpickle_list            | 4.49 us                                                      | 4.72 us: 1.05x slower                                        |
| pickle_list              | 4.11 us                                                      | 4.44 us: 1.08x slower                                        |
| pickle_dict              | 30.0 us                                                      | 33.4 us: 1.11x slower                                        |
| gc_traversal             | 3.45 ms                                                      | 3.93 ms: 1.14x slower                                        |
| python_startup_no_site   | 7.32 ms                                                      | 8.51 ms: 1.16x slower                                        |
| regex_effbot             | 2.99 ms                                                      | 3.50 ms: 1.17x slower                                        |
| dask                     | 463 ms                                                       | 568 ms: 1.23x slower                                         |
| coverage                 | 64.0 ms                                                      | 89.4 ms: 1.40x slower                                        |
| Geometric mean           | (ref)                                                        | 1.30x faster                                                 |

Benchmark hidden because not significant (1): python_startup
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
