
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 3a5be87
- commit date: 2023-05-28
- overall geometric mean: 1.30x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230528-pythonperf2-x86_64-python-main-3.13.0a0-3a5be87 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| docutils       | 3.40 sec                                                     | 2.87 sec: 1.19x faster                                      |
| html5lib       | 94.6 ms                                                      | 68.7 ms: 1.38x faster                                       |
| tornado_http   | 152 ms                                                       | 114 ms: 1.33x faster                                        |
| Geometric mean | (ref)                                                        | 1.30x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230528-pythonperf2-x86_64-python-main-3.13.0a0-3a5be87 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| nbody          | 137 ms                                                       | 86.3 ms: 1.59x faster                                       |
| float          | 110 ms                                                       | 78.7 ms: 1.40x faster                                       |
| pidigits       | 271 ms                                                       | 260 ms: 1.04x faster                                        |
| Geometric mean | (ref)                                                        | 1.32x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230528-pythonperf2-x86_64-python-main-3.13.0a0-3a5be87 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 143 ms: 1.35x faster                                        |
| regex_v8       | 26.6 ms                                                      | 24.6 ms: 1.08x faster                                       |
| regex_dna      | 259 ms                                                       | 245 ms: 1.06x faster                                        |
| regex_effbot   | 2.99 ms                                                      | 3.68 ms: 1.23x slower                                       |
| Geometric mean | (ref)                                                        | 1.06x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230528-pythonperf2-x86_64-python-main-3.13.0a0-3a5be87 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 205 us: 1.57x faster                                        |
| pickle_pure_python   | 457 us                                                       | 318 us: 1.44x faster                                        |
| json_dumps           | 14.2 ms                                                      | 10.3 ms: 1.39x faster                                       |
| tomli_loads          | 2.97 sec                                                     | 2.19 sec: 1.36x faster                                      |
| xml_etree_process    | 76.0 ms                                                      | 58.6 ms: 1.30x faster                                       |
| json_loads           | 30.0 us                                                      | 24.1 us: 1.24x faster                                       |
| xml_etree_generate   | 94.6 ms                                                      | 86.1 ms: 1.10x faster                                       |
| xml_etree_parse      | 162 ms                                                       | 147 ms: 1.10x faster                                        |
| xml_etree_iterparse  | 110 ms                                                       | 105 ms: 1.05x faster                                        |
| unpickle             | 14.2 us                                                      | 14.6 us: 1.03x slower                                       |
| pickle               | 9.94 us                                                      | 10.3 us: 1.04x slower                                       |
| unpickle_list        | 4.49 us                                                      | 4.72 us: 1.05x slower                                       |
| pickle_list          | 4.11 us                                                      | 4.43 us: 1.08x slower                                       |
| pickle_dict          | 30.0 us                                                      | 33.0 us: 1.10x slower                                       |
| Geometric mean       | (ref)                                                        | 1.14x faster                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230528-pythonperf2-x86_64-python-main-3.13.0a0-3a5be87 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.3 ms: 1.01x faster                                       |
| python_startup_no_site | 7.32 ms                                                      | 8.49 ms: 1.16x slower                                       |
| Geometric mean         | (ref)                                                        | 1.07x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230528-pythonperf2-x86_64-python-main-3.13.0a0-3a5be87 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| mako           | 14.7 ms                                                      | 9.94 ms: 1.48x faster                                       |
| genshi_text    | 31.5 ms                                                      | 24.9 ms: 1.26x faster                                       |
| genshi_xml     | 64.7 ms                                                      | 53.8 ms: 1.20x faster                                       |
| Geometric mean | (ref)                                                        | 1.31x faster                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230528-pythonperf2-x86_64-python-main-3.13.0a0-3a5be87 |
|--------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 146 us: 3.58x faster                                        |
| deltablue                | 7.47 ms                                                      | 3.19 ms: 2.34x faster                                       |
| asyncio_tcp              | 782 ms                                                       | 381 ms: 2.05x faster                                        |
| asyncio_tcp_ssl          | 3.09 sec                                                     | 1.57 sec: 1.97x faster                                      |
| logging_silent           | 166 ns                                                       | 90.9 ns: 1.82x faster                                       |
| richards_super           | 90.8 ms                                                      | 50.6 ms: 1.79x faster                                       |
| go                       | 259 ms                                                       | 145 ms: 1.78x faster                                        |
| chaos                    | 107 ms                                                       | 63.4 ms: 1.69x faster                                       |
| scimark_sor              | 177 ms                                                       | 105 ms: 1.69x faster                                        |
| richards                 | 74.1 ms                                                      | 44.6 ms: 1.66x faster                                       |
| hexiom                   | 9.52 ms                                                      | 5.76 ms: 1.65x faster                                       |
| generators               | 58.0 ms                                                      | 35.4 ms: 1.64x faster                                       |
| sqlglot_parse            | 2.26 ms                                                      | 1.39 ms: 1.63x faster                                       |
| scimark_lu               | 164 ms                                                       | 101 ms: 1.63x faster                                        |
| raytrace                 | 488 ms                                                       | 301 ms: 1.62x faster                                        |
| pyflate                  | 697 ms                                                       | 437 ms: 1.59x faster                                        |
| nbody                    | 137 ms                                                       | 86.3 ms: 1.59x faster                                       |
| unpickle_pure_python     | 321 us                                                       | 205 us: 1.57x faster                                        |
| spectral_norm            | 136 ms                                                       | 89.4 ms: 1.52x faster                                       |
| sqlglot_transpile        | 2.71 ms                                                      | 1.79 ms: 1.52x faster                                       |
| async_tree_io            | 1.61 sec                                                     | 1.07 sec: 1.50x faster                                      |
| async_tree_none          | 700 ms                                                       | 467 ms: 1.50x faster                                        |
| scimark_monte_carlo      | 109 ms                                                       | 73.5 ms: 1.49x faster                                       |
| mako                     | 14.7 ms                                                      | 9.94 ms: 1.48x faster                                       |
| async_tree_memoization   | 824 ms                                                       | 562 ms: 1.47x faster                                        |
| fannkuch                 | 496 ms                                                       | 344 ms: 1.44x faster                                        |
| pickle_pure_python       | 457 us                                                       | 318 us: 1.44x faster                                        |
| crypto_pyaes             | 118 ms                                                       | 83.0 ms: 1.42x faster                                       |
| float                    | 110 ms                                                       | 78.7 ms: 1.40x faster                                       |
| json_dumps               | 14.2 ms                                                      | 10.3 ms: 1.39x faster                                       |
| html5lib                 | 94.6 ms                                                      | 68.7 ms: 1.38x faster                                       |
| tomli_loads              | 2.97 sec                                                     | 2.19 sec: 1.36x faster                                      |
| regex_compile            | 194 ms                                                       | 143 ms: 1.35x faster                                        |
| async_tree_cpu_io_mixed  | 952 ms                                                       | 710 ms: 1.34x faster                                        |
| tornado_http             | 152 ms                                                       | 114 ms: 1.33x faster                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.62 sec: 1.33x faster                                      |
| coroutines               | 30.4 ms                                                      | 22.9 ms: 1.33x faster                                       |
| deepcopy_memo            | 48.9 us                                                      | 36.9 us: 1.33x faster                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 796 ms: 1.32x faster                                        |
| logging_simple           | 8.90 us                                                      | 6.76 us: 1.32x faster                                       |
| pycparser                | 1.66 sec                                                     | 1.27 sec: 1.30x faster                                      |
| logging_format           | 9.57 us                                                      | 7.34 us: 1.30x faster                                       |
| xml_etree_process        | 76.0 ms                                                      | 58.6 ms: 1.30x faster                                       |
| mypy2                    | 466 ms                                                       | 362 ms: 1.29x faster                                        |
| genshi_text              | 31.5 ms                                                      | 24.9 ms: 1.26x faster                                       |
| nqueens                  | 112 ms                                                       | 89.4 ms: 1.26x faster                                       |
| sqlglot_normalize        | 144 ms                                                       | 115 ms: 1.25x faster                                        |
| comprehensions           | 26.9 us                                                      | 21.6 us: 1.24x faster                                       |
| json_loads               | 30.0 us                                                      | 24.1 us: 1.24x faster                                       |
| dulwich_log              | 80.1 ms                                                      | 64.9 ms: 1.23x faster                                       |
| sqlglot_optimize         | 70.3 ms                                                      | 57.2 ms: 1.23x faster                                       |
| mdp                      | 3.03 sec                                                     | 2.51 sec: 1.21x faster                                      |
| genshi_xml               | 64.7 ms                                                      | 53.8 ms: 1.20x faster                                       |
| deepcopy                 | 454 us                                                       | 379 us: 1.20x faster                                        |
| bench_thread_pool        | 1.14 ms                                                      | 954 us: 1.19x faster                                        |
| scimark_fft              | 359 ms                                                       | 303 ms: 1.19x faster                                        |
| docutils                 | 3.40 sec                                                     | 2.87 sec: 1.19x faster                                      |
| deepcopy_reduce          | 4.03 us                                                      | 3.42 us: 1.18x faster                                       |
| json                     | 5.96 ms                                                      | 5.07 ms: 1.17x faster                                       |
| scimark_sparse_mat_mult  | 5.19 ms                                                      | 4.43 ms: 1.17x faster                                       |
| bench_mp_pool            | 7.18 ms                                                      | 6.22 ms: 1.15x faster                                       |
| unpack_sequence          | 59.5 ns                                                      | 51.8 ns: 1.15x faster                                       |
| xml_etree_generate       | 94.6 ms                                                      | 86.1 ms: 1.10x faster                                       |
| create_gc_cycles         | 1.82 ms                                                      | 1.66 ms: 1.10x faster                                       |
| xml_etree_parse          | 162 ms                                                       | 147 ms: 1.10x faster                                        |
| sqlite_synth             | 2.97 us                                                      | 2.73 us: 1.09x faster                                       |
| regex_v8                 | 26.6 ms                                                      | 24.6 ms: 1.08x faster                                       |
| async_generators         | 422 ms                                                       | 390 ms: 1.08x faster                                        |
| meteor_contest           | 137 ms                                                       | 127 ms: 1.07x faster                                        |
| pathlib                  | 21.7 ms                                                      | 20.4 ms: 1.06x faster                                       |
| regex_dna                | 259 ms                                                       | 245 ms: 1.06x faster                                        |
| xml_etree_iterparse      | 110 ms                                                       | 105 ms: 1.05x faster                                        |
| pidigits                 | 271 ms                                                       | 260 ms: 1.04x faster                                        |
| python_startup           | 11.5 ms                                                      | 11.3 ms: 1.01x faster                                       |
| unpickle                 | 14.2 us                                                      | 14.6 us: 1.03x slower                                       |
| pickle                   | 9.94 us                                                      | 10.3 us: 1.04x slower                                       |
| unpickle_list            | 4.49 us                                                      | 4.72 us: 1.05x slower                                       |
| pickle_list              | 4.11 us                                                      | 4.43 us: 1.08x slower                                       |
| gc_traversal             | 3.45 ms                                                      | 3.76 ms: 1.09x slower                                       |
| pickle_dict              | 30.0 us                                                      | 33.0 us: 1.10x slower                                       |
| python_startup_no_site   | 7.32 ms                                                      | 8.49 ms: 1.16x slower                                       |
| regex_effbot             | 2.99 ms                                                      | 3.68 ms: 1.23x slower                                       |
| coverage                 | 64.0 ms                                                      | 89.4 ms: 1.40x slower                                       |
| Geometric mean           | (ref)                                                        | 1.30x faster                                                |

Benchmark hidden because not significant (1): telco
Ignored benchmarks (15) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, dask, django_template, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
