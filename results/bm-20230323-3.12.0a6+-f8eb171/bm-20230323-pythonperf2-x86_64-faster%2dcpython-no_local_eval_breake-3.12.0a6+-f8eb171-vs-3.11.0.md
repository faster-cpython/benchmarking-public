
# Results vs. 3.11.0

- fork: faster-cpython
- ref: no_local_eval_breake
- machine: linux-x86_64
- commit hash: f8eb171
- commit date: 2023-03-23
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-pythonperf2-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a6+-f8eb171 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 285 ms: 1.01x faster                                                                   |
| chameleon      | 7.67 ms                                                      | 7.59 ms: 1.01x faster                                                                  |
| docutils       | 2.86 sec                                                     | 2.82 sec: 1.01x faster                                                                 |
| html5lib       | 72.9 ms                                                      | 69.7 ms: 1.05x faster                                                                  |
| tornado_http   | 122 ms                                                       | 112 ms: 1.08x faster                                                                   |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-pythonperf2-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a6+-f8eb171 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| nbody          | 90.7 ms                                                      | 83.7 ms: 1.08x faster                                                                  |
| float          | 74.2 ms                                                      | 72.4 ms: 1.02x faster                                                                  |
| pidigits       | 251 ms                                                       | 260 ms: 1.03x slower                                                                   |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-pythonperf2-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a6+-f8eb171 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_v8       | 23.9 ms                                                      | 22.7 ms: 1.05x faster                                                                  |
| regex_compile  | 158 ms                                                       | 150 ms: 1.05x faster                                                                   |
| regex_effbot   | 3.50 ms                                                      | 3.44 ms: 1.02x faster                                                                  |
| regex_dna      | 227 ms                                                       | 232 ms: 1.02x slower                                                                   |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-pythonperf2-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a6+-f8eb171 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.3 ms: 1.29x faster                                                                  |
| json_loads           | 28.7 us                                                      | 24.4 us: 1.17x faster                                                                  |
| xml_etree_parse      | 158 ms                                                       | 140 ms: 1.13x faster                                                                   |
| unpickle_pure_python | 241 us                                                       | 215 us: 1.12x faster                                                                   |
| xml_etree_iterparse  | 104 ms                                                       | 100 ms: 1.04x faster                                                                   |
| tomli_loads          | 2.26 sec                                                     | 2.18 sec: 1.04x faster                                                                 |
| unpickle_list        | 4.53 us                                                      | 4.43 us: 1.02x faster                                                                  |
| pickle_list          | 3.83 us                                                      | 3.74 us: 1.02x faster                                                                  |
| pickle_pure_python   | 319 us                                                       | 316 us: 1.01x faster                                                                   |
| unpickle             | 13.4 us                                                      | 13.7 us: 1.02x slower                                                                  |
| xml_etree_process    | 56.5 ms                                                      | 58.1 ms: 1.03x slower                                                                  |
| pickle_dict          | 30.8 us                                                      | 31.8 us: 1.03x slower                                                                  |
| xml_etree_generate   | 80.5 ms                                                      | 83.9 ms: 1.04x slower                                                                  |
| pickle               | 9.64 us                                                      | 10.2 us: 1.06x slower                                                                  |
| Geometric mean       | (ref)                                                        | 1.04x faster                                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-pythonperf2-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a6+-f8eb171 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.0 ms: 1.02x slower                                                                  |
| python_startup_no_site | 7.76 ms                                                      | 8.26 ms: 1.06x slower                                                                  |
| Geometric mean         | (ref)                                                        | 1.04x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-pythonperf2-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a6+-f8eb171 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| mako           | 11.0 ms                                                      | 9.92 ms: 1.11x faster                                                                  |
| genshi_xml     | 58.5 ms                                                      | 54.3 ms: 1.08x faster                                                                  |
| genshi_text    | 26.1 ms                                                      | 25.1 ms: 1.04x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                           |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-pythonperf2-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a6+-f8eb171 |
|--------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| asyncio_tcp              | 753 ms                                                       | 386 ms: 1.95x faster                                                                   |
| asyncio_tcp_ssl          | 3.08 sec                                                     | 1.58 sec: 1.95x faster                                                                 |
| generators               | 56.0 ms                                                      | 37.7 ms: 1.49x faster                                                                  |
| json_dumps               | 13.4 ms                                                      | 10.3 ms: 1.29x faster                                                                  |
| json_loads               | 28.7 us                                                      | 24.4 us: 1.17x faster                                                                  |
| deltablue                | 4.00 ms                                                      | 3.44 ms: 1.16x faster                                                                  |
| chaos                    | 80.9 ms                                                      | 71.1 ms: 1.14x faster                                                                  |
| xml_etree_parse          | 158 ms                                                       | 140 ms: 1.13x faster                                                                   |
| scimark_lu               | 115 ms                                                       | 102 ms: 1.13x faster                                                                   |
| json                     | 5.65 ms                                                      | 5.03 ms: 1.12x faster                                                                  |
| unpickle_pure_python     | 241 us                                                       | 215 us: 1.12x faster                                                                   |
| mako                     | 11.0 ms                                                      | 9.92 ms: 1.11x faster                                                                  |
| deepcopy_memo            | 38.8 us                                                      | 35.1 us: 1.11x faster                                                                  |
| coroutines               | 27.6 ms                                                      | 25.3 ms: 1.09x faster                                                                  |
| nqueens                  | 103 ms                                                       | 94.8 ms: 1.08x faster                                                                  |
| nbody                    | 90.7 ms                                                      | 83.7 ms: 1.08x faster                                                                  |
| tornado_http             | 122 ms                                                       | 112 ms: 1.08x faster                                                                   |
| genshi_xml               | 58.5 ms                                                      | 54.3 ms: 1.08x faster                                                                  |
| hexiom                   | 7.13 ms                                                      | 6.64 ms: 1.07x faster                                                                  |
| mdp                      | 2.75 sec                                                     | 2.57 sec: 1.07x faster                                                                 |
| scimark_sparse_mat_mult  | 4.05 ms                                                      | 3.81 ms: 1.06x faster                                                                  |
| raytrace                 | 317 ms                                                       | 298 ms: 1.06x faster                                                                   |
| deepcopy                 | 399 us                                                       | 377 us: 1.06x faster                                                                   |
| regex_v8                 | 23.9 ms                                                      | 22.7 ms: 1.05x faster                                                                  |
| regex_compile            | 158 ms                                                       | 150 ms: 1.05x faster                                                                   |
| sqlglot_normalize        | 126 ms                                                       | 120 ms: 1.05x faster                                                                   |
| pycparser                | 1.32 sec                                                     | 1.26 sec: 1.05x faster                                                                 |
| html5lib                 | 72.9 ms                                                      | 69.7 ms: 1.05x faster                                                                  |
| dulwich_log              | 68.4 ms                                                      | 65.5 ms: 1.05x faster                                                                  |
| genshi_text              | 26.1 ms                                                      | 25.1 ms: 1.04x faster                                                                  |
| xml_etree_iterparse      | 104 ms                                                       | 100 ms: 1.04x faster                                                                   |
| logging_format           | 8.11 us                                                      | 7.82 us: 1.04x faster                                                                  |
| tomli_loads              | 2.26 sec                                                     | 2.18 sec: 1.04x faster                                                                 |
| bench_thread_pool        | 1.01 ms                                                      | 977 us: 1.03x faster                                                                   |
| scimark_fft              | 285 ms                                                       | 276 ms: 1.03x faster                                                                   |
| sympy_expand             | 555 ms                                                       | 536 ms: 1.03x faster                                                                   |
| async_tree_memoization   | 630 ms                                                       | 610 ms: 1.03x faster                                                                   |
| unpack_sequence          | 45.6 ns                                                      | 44.3 ns: 1.03x faster                                                                  |
| deepcopy_reduce          | 3.51 us                                                      | 3.42 us: 1.03x faster                                                                  |
| sqlglot_optimize         | 59.8 ms                                                      | 58.2 ms: 1.03x faster                                                                  |
| pprint_pformat           | 1.63 sec                                                     | 1.59 sec: 1.03x faster                                                                 |
| spectral_norm            | 93.3 ms                                                      | 91.0 ms: 1.03x faster                                                                  |
| float                    | 74.2 ms                                                      | 72.4 ms: 1.02x faster                                                                  |
| unpickle_list            | 4.53 us                                                      | 4.43 us: 1.02x faster                                                                  |
| pickle_list              | 3.83 us                                                      | 3.74 us: 1.02x faster                                                                  |
| sympy_integrate          | 25.8 ms                                                      | 25.2 ms: 1.02x faster                                                                  |
| sympy_str                | 337 ms                                                       | 331 ms: 1.02x faster                                                                   |
| gc_traversal             | 3.85 ms                                                      | 3.78 ms: 1.02x faster                                                                  |
| regex_effbot             | 3.50 ms                                                      | 3.44 ms: 1.02x faster                                                                  |
| async_tree_none          | 519 ms                                                       | 511 ms: 1.02x faster                                                                   |
| pathlib                  | 19.1 ms                                                      | 18.8 ms: 1.02x faster                                                                  |
| docutils                 | 2.86 sec                                                     | 2.82 sec: 1.01x faster                                                                 |
| logging_simple           | 7.19 us                                                      | 7.10 us: 1.01x faster                                                                  |
| async_tree_io            | 1.17 sec                                                     | 1.16 sec: 1.01x faster                                                                 |
| chameleon                | 7.67 ms                                                      | 7.59 ms: 1.01x faster                                                                  |
| pickle_pure_python       | 319 us                                                       | 316 us: 1.01x faster                                                                   |
| 2to3                     | 288 ms                                                       | 285 ms: 1.01x faster                                                                   |
| meteor_contest           | 131 ms                                                       | 129 ms: 1.01x faster                                                                   |
| coverage                 | 84.8 ms                                                      | 83.9 ms: 1.01x faster                                                                  |
| thrift                   | 925 us                                                       | 917 us: 1.01x faster                                                                   |
| pprint_safe_repr         | 784 ms                                                       | 778 ms: 1.01x faster                                                                   |
| logging_silent           | 101 ns                                                       | 100 ns: 1.01x faster                                                                   |
| sympy_sum                | 185 ms                                                       | 186 ms: 1.00x slower                                                                   |
| sqlglot_transpile        | 1.92 ms                                                      | 1.93 ms: 1.01x slower                                                                  |
| richards_super           | 61.0 ms                                                      | 61.6 ms: 1.01x slower                                                                  |
| telco                    | 6.86 ms                                                      | 6.92 ms: 1.01x slower                                                                  |
| typing_runtime_protocols | 523 us                                                       | 530 us: 1.01x slower                                                                   |
| pyflate                  | 449 ms                                                       | 456 ms: 1.02x slower                                                                   |
| unpickle                 | 13.4 us                                                      | 13.7 us: 1.02x slower                                                                  |
| regex_dna                | 227 ms                                                       | 232 ms: 1.02x slower                                                                   |
| fannkuch                 | 429 ms                                                       | 439 ms: 1.02x slower                                                                   |
| richards                 | 48.3 ms                                                      | 49.4 ms: 1.02x slower                                                                  |
| python_startup           | 10.8 ms                                                      | 11.0 ms: 1.02x slower                                                                  |
| sqlglot_parse            | 1.53 ms                                                      | 1.57 ms: 1.03x slower                                                                  |
| xml_etree_process        | 56.5 ms                                                      | 58.1 ms: 1.03x slower                                                                  |
| pickle_dict              | 30.8 us                                                      | 31.8 us: 1.03x slower                                                                  |
| pidigits                 | 251 ms                                                       | 260 ms: 1.03x slower                                                                   |
| xml_etree_generate       | 80.5 ms                                                      | 83.9 ms: 1.04x slower                                                                  |
| sqlite_synth             | 2.50 us                                                      | 2.61 us: 1.04x slower                                                                  |
| scimark_sor              | 111 ms                                                       | 116 ms: 1.04x slower                                                                   |
| pickle                   | 9.64 us                                                      | 10.2 us: 1.06x slower                                                                  |
| go                       | 164 ms                                                       | 173 ms: 1.06x slower                                                                   |
| crypto_pyaes             | 83.4 ms                                                      | 88.5 ms: 1.06x slower                                                                  |
| python_startup_no_site   | 7.76 ms                                                      | 8.26 ms: 1.06x slower                                                                  |
| bench_mp_pool            | 4.62 ms                                                      | 4.97 ms: 1.07x slower                                                                  |
| comprehensions           | 24.6 us                                                      | 26.7 us: 1.08x slower                                                                  |
| scimark_monte_carlo      | 68.2 ms                                                      | 74.9 ms: 1.10x slower                                                                  |
| async_generators         | 316 ms                                                       | 385 ms: 1.22x slower                                                                   |
| dask                     | 410 ms                                                       | 566 ms: 1.38x slower                                                                   |
| Geometric mean           | (ref)                                                        | 1.04x faster                                                                           |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed, create_gc_cycles, django_template, mypy2
Ignored benchmarks (6) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative
