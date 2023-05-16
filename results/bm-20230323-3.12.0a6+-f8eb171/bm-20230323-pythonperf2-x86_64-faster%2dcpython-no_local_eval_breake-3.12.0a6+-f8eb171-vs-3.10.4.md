
# Results vs. 3.10.4

- fork: faster-cpython
- ref: no_local_eval_breake
- machine: linux-x86_64
- commit hash: f8eb171
- commit date: 2023-03-23
- overall geometric mean: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-pythonperf2-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a6+-f8eb171 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 285 ms: 1.23x faster                                                                   |
| chameleon      | 9.72 ms                                                      | 7.59 ms: 1.28x faster                                                                  |
| docutils       | 3.40 sec                                                     | 2.82 sec: 1.21x faster                                                                 |
| html5lib       | 94.6 ms                                                      | 69.7 ms: 1.36x faster                                                                  |
| tornado_http   | 152 ms                                                       | 112 ms: 1.36x faster                                                                   |
| Geometric mean | (ref)                                                        | 1.28x faster                                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-pythonperf2-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a6+-f8eb171 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 83.7 ms: 1.64x faster                                                                  |
| float          | 110 ms                                                       | 72.4 ms: 1.52x faster                                                                  |
| pidigits       | 271 ms                                                       | 260 ms: 1.04x faster                                                                   |
| Geometric mean | (ref)                                                        | 1.38x faster                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-pythonperf2-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a6+-f8eb171 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 150 ms: 1.29x faster                                                                   |
| regex_v8       | 26.6 ms                                                      | 22.7 ms: 1.17x faster                                                                  |
| regex_dna      | 259 ms                                                       | 232 ms: 1.12x faster                                                                   |
| regex_effbot   | 2.99 ms                                                      | 3.44 ms: 1.15x slower                                                                  |
| Geometric mean | (ref)                                                        | 1.10x faster                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-pythonperf2-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a6+-f8eb171 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 215 us: 1.49x faster                                                                   |
| pickle_pure_python   | 457 us                                                       | 316 us: 1.45x faster                                                                   |
| json_dumps           | 14.2 ms                                                      | 10.3 ms: 1.37x faster                                                                  |
| tomli_loads          | 2.97 sec                                                     | 2.18 sec: 1.36x faster                                                                 |
| xml_etree_process    | 76.0 ms                                                      | 58.1 ms: 1.31x faster                                                                  |
| json_loads           | 30.0 us                                                      | 24.4 us: 1.23x faster                                                                  |
| xml_etree_parse      | 162 ms                                                       | 140 ms: 1.16x faster                                                                   |
| xml_etree_generate   | 94.6 ms                                                      | 83.9 ms: 1.13x faster                                                                  |
| xml_etree_iterparse  | 110 ms                                                       | 100 ms: 1.10x faster                                                                   |
| pickle_list          | 4.11 us                                                      | 3.74 us: 1.10x faster                                                                  |
| unpickle             | 14.2 us                                                      | 13.7 us: 1.04x faster                                                                  |
| unpickle_list        | 4.49 us                                                      | 4.43 us: 1.01x faster                                                                  |
| pickle               | 9.94 us                                                      | 10.2 us: 1.02x slower                                                                  |
| pickle_dict          | 30.0 us                                                      | 31.8 us: 1.06x slower                                                                  |
| Geometric mean       | (ref)                                                        | 1.18x faster                                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-pythonperf2-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a6+-f8eb171 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.0 ms: 1.04x faster                                                                  |
| python_startup_no_site | 7.32 ms                                                      | 8.26 ms: 1.13x slower                                                                  |
| Geometric mean         | (ref)                                                        | 1.04x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-pythonperf2-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a6+-f8eb171 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.92 ms: 1.48x faster                                                                  |
| django_template | 51.5 ms                                                      | 40.4 ms: 1.28x faster                                                                  |
| genshi_text     | 31.5 ms                                                      | 25.1 ms: 1.25x faster                                                                  |
| genshi_xml      | 64.7 ms                                                      | 54.3 ms: 1.19x faster                                                                  |
| Geometric mean  | (ref)                                                        | 1.30x faster                                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-pythonperf2-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a6+-f8eb171 |
|--------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| deltablue                | 7.47 ms                                                      | 3.44 ms: 2.17x faster                                                                  |
| asyncio_tcp              | 782 ms                                                       | 386 ms: 2.03x faster                                                                   |
| asyncio_tcp_ssl          | 3.09 sec                                                     | 1.58 sec: 1.96x faster                                                                 |
| logging_silent           | 166 ns                                                       | 100 ns: 1.65x faster                                                                   |
| nbody                    | 137 ms                                                       | 83.7 ms: 1.64x faster                                                                  |
| raytrace                 | 488 ms                                                       | 298 ms: 1.64x faster                                                                   |
| scimark_lu               | 164 ms                                                       | 102 ms: 1.61x faster                                                                   |
| generators               | 58.0 ms                                                      | 37.7 ms: 1.54x faster                                                                  |
| pyflate                  | 697 ms                                                       | 456 ms: 1.53x faster                                                                   |
| scimark_sor              | 177 ms                                                       | 116 ms: 1.52x faster                                                                   |
| float                    | 110 ms                                                       | 72.4 ms: 1.52x faster                                                                  |
| chaos                    | 107 ms                                                       | 71.1 ms: 1.51x faster                                                                  |
| richards                 | 74.1 ms                                                      | 49.4 ms: 1.50x faster                                                                  |
| spectral_norm            | 136 ms                                                       | 91.0 ms: 1.50x faster                                                                  |
| go                       | 259 ms                                                       | 173 ms: 1.50x faster                                                                   |
| unpickle_pure_python     | 321 us                                                       | 215 us: 1.49x faster                                                                   |
| mako                     | 14.7 ms                                                      | 9.92 ms: 1.48x faster                                                                  |
| richards_super           | 90.8 ms                                                      | 61.6 ms: 1.48x faster                                                                  |
| scimark_monte_carlo      | 109 ms                                                       | 74.9 ms: 1.46x faster                                                                  |
| pickle_pure_python       | 457 us                                                       | 316 us: 1.45x faster                                                                   |
| bench_mp_pool            | 7.18 ms                                                      | 4.97 ms: 1.45x faster                                                                  |
| sqlglot_parse            | 2.26 ms                                                      | 1.57 ms: 1.44x faster                                                                  |
| hexiom                   | 9.52 ms                                                      | 6.64 ms: 1.43x faster                                                                  |
| sqlglot_transpile        | 2.71 ms                                                      | 1.93 ms: 1.40x faster                                                                  |
| deepcopy_memo            | 48.9 us                                                      | 35.1 us: 1.39x faster                                                                  |
| async_tree_io            | 1.61 sec                                                     | 1.16 sec: 1.39x faster                                                                 |
| json_dumps               | 14.2 ms                                                      | 10.3 ms: 1.37x faster                                                                  |
| async_tree_none          | 700 ms                                                       | 511 ms: 1.37x faster                                                                   |
| scimark_sparse_mat_mult  | 5.19 ms                                                      | 3.81 ms: 1.36x faster                                                                  |
| tomli_loads              | 2.97 sec                                                     | 2.18 sec: 1.36x faster                                                                 |
| html5lib                 | 94.6 ms                                                      | 69.7 ms: 1.36x faster                                                                  |
| pprint_pformat           | 2.15 sec                                                     | 1.59 sec: 1.36x faster                                                                 |
| tornado_http             | 152 ms                                                       | 112 ms: 1.36x faster                                                                   |
| async_tree_memoization   | 824 ms                                                       | 610 ms: 1.35x faster                                                                   |
| pprint_safe_repr         | 1.05 sec                                                     | 778 ms: 1.35x faster                                                                   |
| unpack_sequence          | 59.5 ns                                                      | 44.3 ns: 1.34x faster                                                                  |
| crypto_pyaes             | 118 ms                                                       | 88.5 ms: 1.34x faster                                                                  |
| pycparser                | 1.66 sec                                                     | 1.26 sec: 1.32x faster                                                                 |
| xml_etree_process        | 76.0 ms                                                      | 58.1 ms: 1.31x faster                                                                  |
| scimark_fft              | 359 ms                                                       | 276 ms: 1.30x faster                                                                   |
| regex_compile            | 194 ms                                                       | 150 ms: 1.29x faster                                                                   |
| chameleon                | 9.72 ms                                                      | 7.59 ms: 1.28x faster                                                                  |
| django_template          | 51.5 ms                                                      | 40.4 ms: 1.28x faster                                                                  |
| async_tree_cpu_io_mixed  | 952 ms                                                       | 746 ms: 1.28x faster                                                                   |
| thrift                   | 1.16 ms                                                      | 917 us: 1.27x faster                                                                   |
| genshi_text              | 31.5 ms                                                      | 25.1 ms: 1.25x faster                                                                  |
| logging_simple           | 8.90 us                                                      | 7.10 us: 1.25x faster                                                                  |
| 2to3                     | 350 ms                                                       | 285 ms: 1.23x faster                                                                   |
| json_loads               | 30.0 us                                                      | 24.4 us: 1.23x faster                                                                  |
| logging_format           | 9.57 us                                                      | 7.82 us: 1.22x faster                                                                  |
| dulwich_log              | 80.1 ms                                                      | 65.5 ms: 1.22x faster                                                                  |
| docutils                 | 3.40 sec                                                     | 2.82 sec: 1.21x faster                                                                 |
| sqlglot_optimize         | 70.3 ms                                                      | 58.2 ms: 1.21x faster                                                                  |
| deepcopy                 | 454 us                                                       | 377 us: 1.20x faster                                                                   |
| sqlglot_normalize        | 144 ms                                                       | 120 ms: 1.20x faster                                                                   |
| coroutines               | 30.4 ms                                                      | 25.3 ms: 1.20x faster                                                                  |
| genshi_xml               | 64.7 ms                                                      | 54.3 ms: 1.19x faster                                                                  |
| nqueens                  | 112 ms                                                       | 94.8 ms: 1.19x faster                                                                  |
| json                     | 5.96 ms                                                      | 5.03 ms: 1.19x faster                                                                  |
| mdp                      | 3.03 sec                                                     | 2.57 sec: 1.18x faster                                                                 |
| deepcopy_reduce          | 4.03 us                                                      | 3.42 us: 1.18x faster                                                                  |
| regex_v8                 | 26.6 ms                                                      | 22.7 ms: 1.17x faster                                                                  |
| bench_thread_pool        | 1.14 ms                                                      | 977 us: 1.16x faster                                                                   |
| xml_etree_parse          | 162 ms                                                       | 140 ms: 1.16x faster                                                                   |
| pathlib                  | 21.7 ms                                                      | 18.8 ms: 1.16x faster                                                                  |
| sqlite_synth             | 2.97 us                                                      | 2.61 us: 1.14x faster                                                                  |
| create_gc_cycles         | 1.82 ms                                                      | 1.60 ms: 1.14x faster                                                                  |
| fannkuch                 | 496 ms                                                       | 439 ms: 1.13x faster                                                                   |
| xml_etree_generate       | 94.6 ms                                                      | 83.9 ms: 1.13x faster                                                                  |
| regex_dna                | 259 ms                                                       | 232 ms: 1.12x faster                                                                   |
| sympy_expand             | 599 ms                                                       | 536 ms: 1.12x faster                                                                   |
| sympy_integrate          | 28.1 ms                                                      | 25.2 ms: 1.11x faster                                                                  |
| xml_etree_iterparse      | 110 ms                                                       | 100 ms: 1.10x faster                                                                   |
| pickle_list              | 4.11 us                                                      | 3.74 us: 1.10x faster                                                                  |
| async_generators         | 422 ms                                                       | 385 ms: 1.10x faster                                                                   |
| sympy_str                | 358 ms                                                       | 331 ms: 1.08x faster                                                                   |
| meteor_contest           | 137 ms                                                       | 129 ms: 1.06x faster                                                                   |
| python_startup           | 11.5 ms                                                      | 11.0 ms: 1.04x faster                                                                  |
| pidigits                 | 271 ms                                                       | 260 ms: 1.04x faster                                                                   |
| sympy_sum                | 193 ms                                                       | 186 ms: 1.04x faster                                                                   |
| unpickle                 | 14.2 us                                                      | 13.7 us: 1.04x faster                                                                  |
| telco                    | 7.14 ms                                                      | 6.92 ms: 1.03x faster                                                                  |
| unpickle_list            | 4.49 us                                                      | 4.43 us: 1.01x faster                                                                  |
| comprehensions           | 26.9 us                                                      | 26.7 us: 1.01x faster                                                                  |
| typing_runtime_protocols | 523 us                                                       | 530 us: 1.01x slower                                                                   |
| pickle                   | 9.94 us                                                      | 10.2 us: 1.02x slower                                                                  |
| pickle_dict              | 30.0 us                                                      | 31.8 us: 1.06x slower                                                                  |
| gc_traversal             | 3.45 ms                                                      | 3.78 ms: 1.09x slower                                                                  |
| python_startup_no_site   | 7.32 ms                                                      | 8.26 ms: 1.13x slower                                                                  |
| regex_effbot             | 2.99 ms                                                      | 3.44 ms: 1.15x slower                                                                  |
| dask                     | 463 ms                                                       | 566 ms: 1.22x slower                                                                   |
| coverage                 | 64.0 ms                                                      | 83.9 ms: 1.31x slower                                                                  |
| Geometric mean           | (ref)                                                        | 1.25x faster                                                                           |

Benchmark hidden because not significant (1): mypy2
Ignored benchmarks (6) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative
