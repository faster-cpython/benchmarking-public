
# Results vs. base

- fork: faster-cpython
- ref: no_local_eval_breake
- machine: linux-x86_64
- commit hash: f8eb171
- commit date: 2023-03-23
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230324-pythonperf2-x86_64-python-d49409196e0c73c38e3f-3.12.0a6+-d494091 | bm-20230323-pythonperf2-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a6+-f8eb171 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 281 ms                                                                       | 285 ms: 1.01x slower                                                                   |
| chameleon      | 7.24 ms                                                                      | 7.59 ms: 1.05x slower                                                                  |
| docutils       | 2.80 sec                                                                     | 2.82 sec: 1.01x slower                                                                 |
| html5lib       | 68.3 ms                                                                      | 69.7 ms: 1.02x slower                                                                  |
| Geometric mean | (ref)                                                                        | 1.02x slower                                                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): nbody, pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230324-pythonperf2-x86_64-python-d49409196e0c73c38e3f-3.12.0a6+-d494091 | bm-20230323-pythonperf2-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a6+-f8eb171 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_v8       | 22.8 ms                                                                      | 22.7 ms: 1.00x faster                                                                  |
| regex_compile  | 148 ms                                                                       | 150 ms: 1.01x slower                                                                   |
| regex_dna      | 227 ms                                                                       | 232 ms: 1.02x slower                                                                   |
| regex_effbot   | 3.34 ms                                                                      | 3.44 ms: 1.03x slower                                                                  |
| Geometric mean | (ref)                                                                        | 1.02x slower                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230324-pythonperf2-x86_64-python-d49409196e0c73c38e3f-3.12.0a6+-d494091 | bm-20230323-pythonperf2-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a6+-f8eb171 |
|----------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| pickle_list          | 3.88 us                                                                      | 3.74 us: 1.04x faster                                                                  |
| xml_etree_iterparse  | 104 ms                                                                       | 100 ms: 1.03x faster                                                                   |
| unpickle_list        | 4.53 us                                                                      | 4.43 us: 1.02x faster                                                                  |
| xml_etree_parse      | 143 ms                                                                       | 140 ms: 1.02x faster                                                                   |
| pickle               | 10.3 us                                                                      | 10.2 us: 1.01x faster                                                                  |
| json_dumps           | 10.4 ms                                                                      | 10.3 ms: 1.01x faster                                                                  |
| pickle_dict          | 31.6 us                                                                      | 31.8 us: 1.01x slower                                                                  |
| pickle_pure_python   | 312 us                                                                       | 316 us: 1.01x slower                                                                   |
| xml_etree_process    | 57.4 ms                                                                      | 58.1 ms: 1.01x slower                                                                  |
| xml_etree_generate   | 82.7 ms                                                                      | 83.9 ms: 1.01x slower                                                                  |
| unpickle_pure_python | 206 us                                                                       | 215 us: 1.04x slower                                                                   |
| Geometric mean       | (ref)                                                                        | 1.00x faster                                                                           |

Benchmark hidden because not significant (3): json_loads, unpickle, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230324-pythonperf2-x86_64-python-d49409196e0c73c38e3f-3.12.0a6+-d494091 | bm-20230323-pythonperf2-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a6+-f8eb171 |
|------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup         | 11.1 ms                                                                      | 11.0 ms: 1.00x faster                                                                  |
| python_startup_no_site | 8.28 ms                                                                      | 8.26 ms: 1.00x faster                                                                  |
| Geometric mean         | (ref)                                                                        | 1.00x faster                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20230324-pythonperf2-x86_64-python-d49409196e0c73c38e3f-3.12.0a6+-d494091 | bm-20230323-pythonperf2-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a6+-f8eb171 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| genshi_text    | 25.7 ms                                                                      | 25.1 ms: 1.02x faster                                                                  |
| mako           | 10.0 ms                                                                      | 9.92 ms: 1.01x faster                                                                  |
| Geometric mean | (ref)                                                                        | 1.01x faster                                                                           |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20230324-pythonperf2-x86_64-python-d49409196e0c73c38e3f-3.12.0a6+-d494091 | bm-20230323-pythonperf2-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a6+-f8eb171 |
|--------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| coverage                 | 91.5 ms                                                                      | 83.9 ms: 1.09x faster                                                                  |
| coroutines               | 26.6 ms                                                                      | 25.3 ms: 1.05x faster                                                                  |
| pickle_list              | 3.88 us                                                                      | 3.74 us: 1.04x faster                                                                  |
| nqueens                  | 98.0 ms                                                                      | 94.8 ms: 1.03x faster                                                                  |
| create_gc_cycles         | 1.66 ms                                                                      | 1.60 ms: 1.03x faster                                                                  |
| xml_etree_iterparse      | 104 ms                                                                       | 100 ms: 1.03x faster                                                                   |
| thrift                   | 945 us                                                                       | 917 us: 1.03x faster                                                                   |
| unpickle_list            | 4.53 us                                                                      | 4.43 us: 1.02x faster                                                                  |
| genshi_text              | 25.7 ms                                                                      | 25.1 ms: 1.02x faster                                                                  |
| xml_etree_parse          | 143 ms                                                                       | 140 ms: 1.02x faster                                                                   |
| scimark_sparse_mat_mult  | 3.88 ms                                                                      | 3.81 ms: 1.02x faster                                                                  |
| pickle                   | 10.3 us                                                                      | 10.2 us: 1.01x faster                                                                  |
| mako                     | 10.0 ms                                                                      | 9.92 ms: 1.01x faster                                                                  |
| spectral_norm            | 91.8 ms                                                                      | 91.0 ms: 1.01x faster                                                                  |
| sqlglot_normalize        | 121 ms                                                                       | 120 ms: 1.01x faster                                                                   |
| json_dumps               | 10.4 ms                                                                      | 10.3 ms: 1.01x faster                                                                  |
| async_tree_io            | 1.17 sec                                                                     | 1.16 sec: 1.01x faster                                                                 |
| sympy_expand             | 541 ms                                                                       | 536 ms: 1.01x faster                                                                   |
| sqlglot_parse            | 1.58 ms                                                                      | 1.57 ms: 1.01x faster                                                                  |
| sqlglot_transpile        | 1.95 ms                                                                      | 1.93 ms: 1.01x faster                                                                  |
| sqlite_synth             | 2.62 us                                                                      | 2.61 us: 1.01x faster                                                                  |
| python_startup           | 11.1 ms                                                                      | 11.0 ms: 1.00x faster                                                                  |
| sympy_str                | 332 ms                                                                       | 331 ms: 1.00x faster                                                                   |
| regex_v8                 | 22.8 ms                                                                      | 22.7 ms: 1.00x faster                                                                  |
| python_startup_no_site   | 8.28 ms                                                                      | 8.26 ms: 1.00x faster                                                                  |
| asyncio_tcp_ssl          | 1.58 sec                                                                     | 1.58 sec: 1.00x slower                                                                 |
| mdp                      | 2.56 sec                                                                     | 2.57 sec: 1.00x slower                                                                 |
| sympy_integrate          | 25.1 ms                                                                      | 25.2 ms: 1.00x slower                                                                  |
| docutils                 | 2.80 sec                                                                     | 2.82 sec: 1.01x slower                                                                 |
| asyncio_tcp              | 384 ms                                                                       | 386 ms: 1.01x slower                                                                   |
| pickle_dict              | 31.6 us                                                                      | 31.8 us: 1.01x slower                                                                  |
| dulwich_log              | 65.0 ms                                                                      | 65.5 ms: 1.01x slower                                                                  |
| pathlib                  | 18.6 ms                                                                      | 18.8 ms: 1.01x slower                                                                  |
| dask                     | 561 ms                                                                       | 566 ms: 1.01x slower                                                                   |
| pickle_pure_python       | 312 us                                                                       | 316 us: 1.01x slower                                                                   |
| meteor_contest           | 128 ms                                                                       | 129 ms: 1.01x slower                                                                   |
| xml_etree_process        | 57.4 ms                                                                      | 58.1 ms: 1.01x slower                                                                  |
| 2to3                     | 281 ms                                                                       | 285 ms: 1.01x slower                                                                   |
| regex_compile            | 148 ms                                                                       | 150 ms: 1.01x slower                                                                   |
| deltablue                | 3.40 ms                                                                      | 3.44 ms: 1.01x slower                                                                  |
| xml_etree_generate       | 82.7 ms                                                                      | 83.9 ms: 1.01x slower                                                                  |
| deepcopy_memo            | 34.6 us                                                                      | 35.1 us: 1.01x slower                                                                  |
| pyflate                  | 448 ms                                                                       | 456 ms: 1.02x slower                                                                   |
| scimark_fft              | 270 ms                                                                       | 276 ms: 1.02x slower                                                                   |
| pprint_pformat           | 1.56 sec                                                                     | 1.59 sec: 1.02x slower                                                                 |
| async_generators         | 377 ms                                                                       | 385 ms: 1.02x slower                                                                   |
| html5lib                 | 68.3 ms                                                                      | 69.7 ms: 1.02x slower                                                                  |
| pprint_safe_repr         | 762 ms                                                                       | 778 ms: 1.02x slower                                                                   |
| telco                    | 6.78 ms                                                                      | 6.92 ms: 1.02x slower                                                                  |
| regex_dna                | 227 ms                                                                       | 232 ms: 1.02x slower                                                                   |
| chaos                    | 69.1 ms                                                                      | 71.1 ms: 1.03x slower                                                                  |
| regex_effbot             | 3.34 ms                                                                      | 3.44 ms: 1.03x slower                                                                  |
| deepcopy_reduce          | 3.32 us                                                                      | 3.42 us: 1.03x slower                                                                  |
| typing_runtime_protocols | 514 us                                                                       | 530 us: 1.03x slower                                                                   |
| logging_format           | 7.57 us                                                                      | 7.82 us: 1.03x slower                                                                  |
| raytrace                 | 288 ms                                                                       | 298 ms: 1.03x slower                                                                   |
| scimark_sor              | 112 ms                                                                       | 116 ms: 1.04x slower                                                                   |
| unpickle_pure_python     | 206 us                                                                       | 215 us: 1.04x slower                                                                   |
| logging_simple           | 6.79 us                                                                      | 7.10 us: 1.05x slower                                                                  |
| crypto_pyaes             | 84.5 ms                                                                      | 88.5 ms: 1.05x slower                                                                  |
| chameleon                | 7.24 ms                                                                      | 7.59 ms: 1.05x slower                                                                  |
| gc_traversal             | 3.60 ms                                                                      | 3.78 ms: 1.05x slower                                                                  |
| fannkuch                 | 417 ms                                                                       | 439 ms: 1.05x slower                                                                   |
| logging_silent           | 94.2 ns                                                                      | 100 ns: 1.06x slower                                                                   |
| scimark_monte_carlo      | 68.5 ms                                                                      | 74.9 ms: 1.09x slower                                                                  |
| go                       | 157 ms                                                                       | 173 ms: 1.10x slower                                                                   |
| richards                 | 44.8 ms                                                                      | 49.4 ms: 1.10x slower                                                                  |
| richards_super           | 55.7 ms                                                                      | 61.6 ms: 1.11x slower                                                                  |
| Geometric mean           | (ref)                                                                        | 1.01x slower                                                                           |

Benchmark hidden because not significant (25): bench_mp_pool, nbody, bench_thread_pool, json, django_template, genshi_xml, async_tree_cpu_io_mixed, sqlglot_optimize, unpack_sequence, generators, comprehensions, sympy_sum, async_tree_none, pidigits, json_loads, scimark_lu, async_tree_memoization, tornado_http, hexiom, float, unpickle, tomli_loads, mypy2, deepcopy, pycparser
