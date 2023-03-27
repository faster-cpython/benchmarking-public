
# Results vs. 3.11.0

- fork: python
- ref: v3.11.2
- machine: linux-x86_64
- commit hash: 878ead1
- commit date: 2023-02-07
- overall geometric mean: 1.00x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-v3.11.2-3.11.2-878ead1 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 257 ms                                                              | 257 ms: 1.00x slower                                   |
| chameleon      | 6.52 ms                                                             | 6.49 ms: 1.00x faster                                  |
| docutils       | 2.59 sec                                                            | 2.55 sec: 1.02x faster                                 |
| tornado_http   | 96.7 ms                                                             | 96.1 ms: 1.01x faster                                  |
| Geometric mean | (ref)                                                               | 1.01x faster                                           |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-v3.11.2-3.11.2-878ead1 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 96.7 ms                                                             | 93.0 ms: 1.04x faster                                  |
| pidigits       | 197 ms                                                              | 190 ms: 1.04x faster                                   |
| float          | 76.0 ms                                                             | 76.6 ms: 1.01x slower                                  |
| Geometric mean | (ref)                                                               | 1.02x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-v3.11.2-3.11.2-878ead1 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| regex_v8       | 22.0 ms                                                             | 21.3 ms: 1.03x faster                                  |
| regex_dna      | 196 ms                                                              | 192 ms: 1.02x faster                                   |
| regex_compile  | 137 ms                                                              | 138 ms: 1.01x slower                                   |
| regex_effbot   | 3.32 ms                                                             | 3.39 ms: 1.02x slower                                  |
| Geometric mean | (ref)                                                               | 1.00x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-v3.11.2-3.11.2-878ead1 |
|---------------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| xml_etree_iterparse | 108 ms                                                              | 104 ms: 1.04x faster                                   |
| xml_etree_parse     | 162 ms                                                              | 159 ms: 1.02x faster                                   |
| json_dumps          | 12.5 ms                                                             | 12.5 ms: 1.01x faster                                  |
| pickle_pure_python  | 307 us                                                              | 305 us: 1.01x faster                                   |
| xml_etree_process   | 54.1 ms                                                             | 53.8 ms: 1.01x faster                                  |
| pickle_dict         | 30.9 us                                                             | 31.4 us: 1.02x slower                                  |
| pickle              | 9.79 us                                                             | 10.00 us: 1.02x slower                                 |
| pickle_list         | 4.03 us                                                             | 4.16 us: 1.03x slower                                  |
| Geometric mean      | (ref)                                                               | 1.00x faster                                           |

Benchmark hidden because not significant (5): unpickle_list, unpickle_pure_python, json_loads, xml_etree_generate, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-v3.11.2-3.11.2-878ead1 |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.49 ms                                                             | 8.47 ms: 1.00x faster                                  |
| python_startup_no_site | 5.98 ms                                                             | 5.97 ms: 1.00x faster                                  |
| Geometric mean         | (ref)                                                               | 1.00x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-v3.11.2-3.11.2-878ead1 |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| genshi_text     | 21.8 ms                                                             | 21.7 ms: 1.01x faster                                  |
| django_template | 32.9 ms                                                             | 32.7 ms: 1.01x faster                                  |
| Geometric mean  | (ref)                                                               | 1.00x faster                                           |

Benchmark hidden because not significant (2): genshi_xml, mako

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-v3.11.2-3.11.2-878ead1 |
|-------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| nbody                   | 96.7 ms                                                             | 93.0 ms: 1.04x faster                                  |
| pidigits                | 197 ms                                                              | 190 ms: 1.04x faster                                   |
| xml_etree_iterparse     | 108 ms                                                              | 104 ms: 1.04x faster                                   |
| pycparser               | 1.14 sec                                                            | 1.11 sec: 1.03x faster                                 |
| regex_v8                | 22.0 ms                                                             | 21.3 ms: 1.03x faster                                  |
| coroutines              | 26.3 ms                                                             | 25.6 ms: 1.03x faster                                  |
| pathlib                 | 18.2 ms                                                             | 17.8 ms: 1.02x faster                                  |
| logging_format          | 6.64 us                                                             | 6.49 us: 1.02x faster                                  |
| regex_dna               | 196 ms                                                              | 192 ms: 1.02x faster                                   |
| logging_simple          | 6.09 us                                                             | 5.97 us: 1.02x faster                                  |
| sqlite_synth            | 2.51 us                                                             | 2.46 us: 1.02x faster                                  |
| hexiom                  | 6.48 ms                                                             | 6.36 ms: 1.02x faster                                  |
| xml_etree_parse         | 162 ms                                                              | 159 ms: 1.02x faster                                   |
| sympy_expand            | 477 ms                                                              | 468 ms: 1.02x faster                                   |
| docutils                | 2.59 sec                                                            | 2.55 sec: 1.02x faster                                 |
| meteor_contest          | 106 ms                                                              | 105 ms: 1.02x faster                                   |
| scimark_lu              | 108 ms                                                              | 107 ms: 1.01x faster                                   |
| unpack_sequence         | 49.5 ns                                                             | 48.8 ns: 1.01x faster                                  |
| async_generators        | 361 ms                                                              | 357 ms: 1.01x faster                                   |
| sympy_str               | 291 ms                                                              | 288 ms: 1.01x faster                                   |
| nqueens                 | 84.0 ms                                                             | 83.1 ms: 1.01x faster                                  |
| spectral_norm           | 99.5 ms                                                             | 98.4 ms: 1.01x faster                                  |
| sympy_sum               | 167 ms                                                              | 166 ms: 1.01x faster                                   |
| dask                    | 368 ms                                                              | 365 ms: 1.01x faster                                   |
| sympy_integrate         | 21.0 ms                                                             | 20.8 ms: 1.01x faster                                  |
| flaskblogging           | 7.09 ms                                                             | 7.02 ms: 1.01x faster                                  |
| bench_thread_pool       | 820 us                                                              | 812 us: 1.01x faster                                   |
| genshi_text             | 21.8 ms                                                             | 21.7 ms: 1.01x faster                                  |
| json_dumps              | 12.5 ms                                                             | 12.5 ms: 1.01x faster                                  |
| pprint_safe_repr        | 701 ms                                                              | 697 ms: 1.01x faster                                   |
| pickle_pure_python      | 307 us                                                              | 305 us: 1.01x faster                                   |
| aiohttp                 | 1.05 ms                                                             | 1.05 ms: 1.01x faster                                  |
| tornado_http            | 96.7 ms                                                             | 96.1 ms: 1.01x faster                                  |
| django_template         | 32.9 ms                                                             | 32.7 ms: 1.01x faster                                  |
| xml_etree_process       | 54.1 ms                                                             | 53.8 ms: 1.01x faster                                  |
| chameleon               | 6.52 ms                                                             | 6.49 ms: 1.00x faster                                  |
| asyncio_tcp             | 888 ms                                                              | 884 ms: 1.00x faster                                   |
| python_startup          | 8.49 ms                                                             | 8.47 ms: 1.00x faster                                  |
| python_startup_no_site  | 5.98 ms                                                             | 5.97 ms: 1.00x faster                                  |
| 2to3                    | 257 ms                                                              | 257 ms: 1.00x slower                                   |
| chaos                   | 68.0 ms                                                             | 68.2 ms: 1.00x slower                                  |
| create_gc_cycles        | 1.48 ms                                                             | 1.49 ms: 1.00x slower                                  |
| deltablue               | 3.66 ms                                                             | 3.68 ms: 1.00x slower                                  |
| async_tree_cpu_io_mixed | 736 ms                                                              | 740 ms: 1.01x slower                                   |
| pyflate                 | 414 ms                                                              | 417 ms: 1.01x slower                                   |
| float                   | 76.0 ms                                                             | 76.6 ms: 1.01x slower                                  |
| sqlglot_transpile       | 1.65 ms                                                             | 1.67 ms: 1.01x slower                                  |
| generators              | 73.4 ms                                                             | 74.1 ms: 1.01x slower                                  |
| deepcopy_memo           | 36.4 us                                                             | 36.8 us: 1.01x slower                                  |
| logging_silent          | 98.7 ns                                                             | 99.8 ns: 1.01x slower                                  |
| async_tree_memoization  | 621 ms                                                              | 628 ms: 1.01x slower                                   |
| regex_compile           | 137 ms                                                              | 138 ms: 1.01x slower                                   |
| sqlglot_parse           | 1.36 ms                                                             | 1.38 ms: 1.01x slower                                  |
| async_tree_io           | 1.28 sec                                                            | 1.30 sec: 1.01x slower                                 |
| json                    | 4.86 ms                                                             | 4.92 ms: 1.01x slower                                  |
| pickle_dict             | 30.9 us                                                             | 31.4 us: 1.02x slower                                  |
| regex_effbot            | 3.32 ms                                                             | 3.39 ms: 1.02x slower                                  |
| sqlalchemy_declarative  | 138 ms                                                              | 141 ms: 1.02x slower                                   |
| go                      | 138 ms                                                              | 141 ms: 1.02x slower                                   |
| fannkuch                | 384 ms                                                              | 392 ms: 1.02x slower                                   |
| pickle                  | 9.79 us                                                             | 10.00 us: 1.02x slower                                 |
| coverage                | 101 ms                                                              | 103 ms: 1.02x slower                                   |
| deepcopy                | 339 us                                                              | 348 us: 1.03x slower                                   |
| deepcopy_reduce         | 2.96 us                                                             | 3.04 us: 1.03x slower                                  |
| pickle_list             | 4.03 us                                                             | 4.16 us: 1.03x slower                                  |
| scimark_sparse_mat_mult | 4.47 ms                                                             | 4.63 ms: 1.04x slower                                  |
| mdp                     | 2.64 sec                                                            | 2.77 sec: 1.05x slower                                 |
| gc_traversal            | 3.63 ms                                                             | 4.15 ms: 1.14x slower                                  |
| Geometric mean          | (ref)                                                               | 1.00x faster                                           |

Benchmark hidden because not significant (27): genshi_xml, raytrace, unpickle_list, pylint, pprint_pformat, async_tree_none, mypy2, richards, sqlglot_optimize, scimark_fft, html5lib, scimark_monte_carlo, unpickle_pure_python, scimark_sor, json_loads, xml_etree_generate, bench_mp_pool, crypto_pyaes, telco, gunicorn, mako, dulwich_log, djangocms, sqlglot_normalize, unpickle, thrift, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: comprehensions
