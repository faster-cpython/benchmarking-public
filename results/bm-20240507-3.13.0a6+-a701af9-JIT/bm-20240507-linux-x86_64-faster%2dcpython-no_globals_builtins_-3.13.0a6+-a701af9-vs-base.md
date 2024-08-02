# Results vs. base

- fork: faster-cpython
- ref: no_globals_builtins_
- machine: linux-x86_64
- commit hash: a701af9
- commit date: 2024-05-07
- overall geometric mean: 1.00x faster
- HPT reliability: 74.41%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240507-linux-x86_64-python-976212223541b89329d8-3.13.0a6+-9762122 | bm-20240507-linux-x86_64-faster%2dcpython-no_globals_builtins_-3.13.0a6+-a701af9 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| html5lib       | 68.2 ms                                                                | 68.7 ms: 1.01x slower                                                            |
| tornado_http   | 98.3 ms                                                                | 97.5 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                     |

Benchmark hidden because not significant (3): 2to3, chameleon, docutils

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_none, async_tree_none_tg, async_tree_memoization, async_tree_io_tg, async_tree_io, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240507-linux-x86_64-python-976212223541b89329d8-3.13.0a6+-9762122 | bm-20240507-linux-x86_64-faster%2dcpython-no_globals_builtins_-3.13.0a6+-a701af9 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 71.2 ms                                                                | 71.7 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                     |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240507-linux-x86_64-python-976212223541b89329d8-3.13.0a6+-9762122 | bm-20240507-linux-x86_64-faster%2dcpython-no_globals_builtins_-3.13.0a6+-a701af9 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.66 ms                                                                | 3.73 ms: 1.02x slower                                                            |
| regex_dna      | 221 ms                                                                 | 228 ms: 1.03x slower                                                             |
| regex_v8       | 24.8 ms                                                                | 25.7 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                                     |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240507-linux-x86_64-python-976212223541b89329d8-3.13.0a6+-9762122 | bm-20240507-linux-x86_64-faster%2dcpython-no_globals_builtins_-3.13.0a6+-a701af9 |
|---------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pickle_dict         | 35.2 us                                                                | 33.1 us: 1.06x faster                                                            |
| unpickle            | 16.5 us                                                                | 15.7 us: 1.05x faster                                                            |
| pickle_pure_python  | 312 us                                                                 | 301 us: 1.04x faster                                                             |
| pickle_list         | 5.22 us                                                                | 5.05 us: 1.03x faster                                                            |
| unpickle_list       | 5.44 us                                                                | 5.30 us: 1.03x faster                                                            |
| json_dumps          | 10.3 ms                                                                | 10.3 ms: 1.01x faster                                                            |
| xml_etree_generate  | 84.1 ms                                                                | 83.7 ms: 1.00x faster                                                            |
| xml_etree_iterparse | 102 ms                                                                 | 101 ms: 1.00x faster                                                             |
| tomli_loads         | 1.96 sec                                                               | 1.98 sec: 1.01x slower                                                           |
| pickle              | 11.8 us                                                                | 12.0 us: 1.02x slower                                                            |
| xml_etree_parse     | 150 ms                                                                 | 154 ms: 1.03x slower                                                             |
| Geometric mean      | (ref)                                                                  | 1.01x faster                                                                     |

Benchmark hidden because not significant (3): unpickle_pure_python, json_loads, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240507-linux-x86_64-python-976212223541b89329d8-3.13.0a6+-9762122 | bm-20240507-linux-x86_64-faster%2dcpython-no_globals_builtins_-3.13.0a6+-a701af9 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                                | 11.2 ms: 1.01x faster                                                            |
| python_startup_no_site | 7.69 ms                                                                | 7.65 ms: 1.00x faster                                                            |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240507-linux-x86_64-python-976212223541b89329d8-3.13.0a6+-9762122 | bm-20240507-linux-x86_64-faster%2dcpython-no_globals_builtins_-3.13.0a6+-a701af9 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.74 ms                                                                | 9.60 ms: 1.01x faster                                                            |
| django_template | 37.4 ms                                                                | 36.9 ms: 1.01x faster                                                            |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                                     |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                | bm-20240507-linux-x86_64-python-976212223541b89329d8-3.13.0a6+-9762122 | bm-20240507-linux-x86_64-faster%2dcpython-no_globals_builtins_-3.13.0a6+-a701af9 |
|--------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pickle_dict              | 35.2 us                                                                | 33.1 us: 1.06x faster                                                            |
| unpickle                 | 16.5 us                                                                | 15.7 us: 1.05x faster                                                            |
| deepcopy_reduce          | 3.38 us                                                                | 3.23 us: 1.05x faster                                                            |
| pickle_pure_python       | 312 us                                                                 | 301 us: 1.04x faster                                                             |
| pickle_list              | 5.22 us                                                                | 5.05 us: 1.03x faster                                                            |
| logging_format           | 6.58 us                                                                | 6.40 us: 1.03x faster                                                            |
| scimark_lu               | 128 ms                                                                 | 124 ms: 1.03x faster                                                             |
| unpickle_list            | 5.44 us                                                                | 5.30 us: 1.03x faster                                                            |
| pathlib                  | 18.0 ms                                                                | 17.6 ms: 1.02x faster                                                            |
| logging_silent           | 108 ns                                                                 | 106 ns: 1.02x faster                                                             |
| go                       | 151 ms                                                                 | 148 ms: 1.02x faster                                                             |
| scimark_fft              | 321 ms                                                                 | 316 ms: 1.02x faster                                                             |
| nqueens                  | 87.9 ms                                                                | 86.7 ms: 1.01x faster                                                            |
| mako                     | 9.74 ms                                                                | 9.60 ms: 1.01x faster                                                            |
| dask                     | 385 ms                                                                 | 380 ms: 1.01x faster                                                             |
| telco                    | 174 ms                                                                 | 172 ms: 1.01x faster                                                             |
| django_template          | 37.4 ms                                                                | 36.9 ms: 1.01x faster                                                            |
| thrift                   | 819 us                                                                 | 809 us: 1.01x faster                                                             |
| deepcopy_memo            | 37.7 us                                                                | 37.2 us: 1.01x faster                                                            |
| bench_thread_pool        | 878 us                                                                 | 869 us: 1.01x faster                                                             |
| logging_simple           | 5.87 us                                                                | 5.81 us: 1.01x faster                                                            |
| coverage                 | 87.1 ms                                                                | 86.3 ms: 1.01x faster                                                            |
| tornado_http             | 98.3 ms                                                                | 97.5 ms: 1.01x faster                                                            |
| sympy_str                | 303 ms                                                                 | 300 ms: 1.01x faster                                                             |
| sqlite_synth             | 2.86 us                                                                | 2.84 us: 1.01x faster                                                            |
| typing_runtime_protocols | 175 us                                                                 | 174 us: 1.01x faster                                                             |
| sqlglot_optimize         | 57.2 ms                                                                | 56.9 ms: 1.01x faster                                                            |
| python_startup           | 11.2 ms                                                                | 11.2 ms: 1.01x faster                                                            |
| json_dumps               | 10.3 ms                                                                | 10.3 ms: 1.01x faster                                                            |
| gc_traversal             | 3.86 ms                                                                | 3.84 ms: 1.00x faster                                                            |
| generators               | 30.5 ms                                                                | 30.3 ms: 1.00x faster                                                            |
| sqlglot_transpile        | 1.64 ms                                                                | 1.63 ms: 1.00x faster                                                            |
| xml_etree_generate       | 84.1 ms                                                                | 83.7 ms: 1.00x faster                                                            |
| python_startup_no_site   | 7.69 ms                                                                | 7.65 ms: 1.00x faster                                                            |
| raytrace                 | 280 ms                                                                 | 279 ms: 1.00x faster                                                             |
| create_gc_cycles         | 1.83 ms                                                                | 1.82 ms: 1.00x faster                                                            |
| async_generators         | 466 ms                                                                 | 465 ms: 1.00x faster                                                             |
| xml_etree_iterparse      | 102 ms                                                                 | 101 ms: 1.00x faster                                                             |
| asyncio_tcp_ssl          | 1.86 sec                                                               | 1.86 sec: 1.00x faster                                                           |
| asyncio_tcp              | 518 ms                                                                 | 519 ms: 1.00x slower                                                             |
| spectral_norm            | 99.9 ms                                                                | 100 ms: 1.01x slower                                                             |
| float                    | 71.2 ms                                                                | 71.7 ms: 1.01x slower                                                            |
| html5lib                 | 68.2 ms                                                                | 68.7 ms: 1.01x slower                                                            |
| tomli_loads              | 1.96 sec                                                               | 1.98 sec: 1.01x slower                                                           |
| sqlglot_normalize        | 114 ms                                                                 | 115 ms: 1.01x slower                                                             |
| richards_super           | 49.0 ms                                                                | 49.5 ms: 1.01x slower                                                            |
| pyflate                  | 449 ms                                                                 | 453 ms: 1.01x slower                                                             |
| coroutines               | 22.8 ms                                                                | 23.1 ms: 1.01x slower                                                            |
| chaos                    | 58.6 ms                                                                | 59.3 ms: 1.01x slower                                                            |
| mdp                      | 2.58 sec                                                               | 2.61 sec: 1.01x slower                                                           |
| pickle                   | 11.8 us                                                                | 12.0 us: 1.02x slower                                                            |
| regex_effbot             | 3.66 ms                                                                | 3.73 ms: 1.02x slower                                                            |
| xml_etree_parse          | 150 ms                                                                 | 154 ms: 1.03x slower                                                             |
| regex_dna                | 221 ms                                                                 | 228 ms: 1.03x slower                                                             |
| regex_v8                 | 24.8 ms                                                                | 25.7 ms: 1.03x slower                                                            |
| pycparser                | 1.16 sec                                                               | 1.21 sec: 1.05x slower                                                           |
| Geometric mean           | (ref)                                                                  | 1.00x faster                                                                     |

Benchmark hidden because not significant (46): genshi_xml, aiohttp, crypto_pyaes, gunicorn, unpickle_pure_python, sqlglot_parse, mypy2, flaskblogging, json, hexiom, 2to3, bench_mp_pool, pidigits, sympy_expand, fannkuch, chameleon, pylint, regex_compile, nbody, sympy_integrate, djangocms, deltablue, dulwich_log, json_loads, scimark_sparse_mat_mult, pprint_safe_repr, scimark_sor, meteor_contest, scimark_monte_carlo, sympy_sum, docutils, genshi_text, richards, comprehensions, asyncio_websockets, xml_etree_process, deepcopy, async_tree_none, async_tree_none_tg, async_tree_memoization, pprint_pformat, async_tree_io_tg, async_tree_io, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg

# HPT report

- Reliability score: 74.41% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.99x