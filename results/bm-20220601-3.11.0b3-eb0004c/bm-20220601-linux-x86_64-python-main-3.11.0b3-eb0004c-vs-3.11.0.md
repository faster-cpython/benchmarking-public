
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: eb0004c
- commit date: 2022-06-01
- overall geometric mean: 1.02x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220601-linux-x86_64-python-main-3.11.0b3-eb0004c |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 257 ms                                                              | 256 ms: 1.00x faster                                  |
| chameleon      | 6.52 ms                                                             | 6.67 ms: 1.02x slower                                 |
| html5lib       | 64.0 ms                                                             | 62.6 ms: 1.02x faster                                 |
| tornado_http   | 96.7 ms                                                             | 93.8 ms: 1.03x faster                                 |
| Geometric mean | (ref)                                                               | 1.01x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220601-linux-x86_64-python-main-3.11.0b3-eb0004c |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 96.7 ms                                                             | 90.6 ms: 1.07x faster                                 |
| float          | 76.0 ms                                                             | 72.9 ms: 1.04x faster                                 |
| pidigits       | 197 ms                                                              | 194 ms: 1.02x faster                                  |
| Geometric mean | (ref)                                                               | 1.04x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220601-linux-x86_64-python-main-3.11.0b3-eb0004c |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| regex_effbot   | 3.32 ms                                                             | 2.92 ms: 1.14x faster                                 |
| regex_v8       | 22.0 ms                                                             | 21.2 ms: 1.04x faster                                 |
| regex_dna      | 196 ms                                                              | 192 ms: 1.03x faster                                  |
| regex_compile  | 137 ms                                                              | 135 ms: 1.01x faster                                  |
| Geometric mean | (ref)                                                               | 1.05x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220601-linux-x86_64-python-main-3.11.0b3-eb0004c |
|---------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_dict         | 30.9 us                                                             | 25.6 us: 1.21x faster                                 |
| json_loads          | 26.2 us                                                             | 24.4 us: 1.07x faster                                 |
| xml_etree_parse     | 162 ms                                                              | 156 ms: 1.04x faster                                  |
| xml_etree_iterparse | 108 ms                                                              | 105 ms: 1.03x faster                                  |
| pickle              | 9.79 us                                                             | 9.55 us: 1.02x faster                                 |
| pickle_pure_python  | 307 us                                                              | 302 us: 1.02x faster                                  |
| unpickle_list       | 4.96 us                                                             | 4.89 us: 1.01x faster                                 |
| xml_etree_process   | 54.1 ms                                                             | 53.8 ms: 1.01x faster                                 |
| xml_etree_generate  | 76.5 ms                                                             | 76.3 ms: 1.00x faster                                 |
| unpickle            | 13.2 us                                                             | 13.3 us: 1.01x slower                                 |
| pickle_list         | 4.03 us                                                             | 4.33 us: 1.07x slower                                 |
| Geometric mean      | (ref)                                                               | 1.03x faster                                          |

Benchmark hidden because not significant (2): json_dumps, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220601-linux-x86_64-python-main-3.11.0b3-eb0004c |
|------------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 8.49 ms                                                             | 8.33 ms: 1.02x faster                                 |
| python_startup_no_site | 5.98 ms                                                             | 6.17 ms: 1.03x slower                                 |
| Geometric mean         | (ref)                                                               | 1.01x slower                                          |

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220601-linux-x86_64-python-main-3.11.0b3-eb0004c |
|-------------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_dict             | 30.9 us                                                             | 25.6 us: 1.21x faster                                 |
| regex_effbot            | 3.32 ms                                                             | 2.92 ms: 1.14x faster                                 |
| unpack_sequence         | 49.5 ns                                                             | 43.4 ns: 1.14x faster                                 |
| json_loads              | 26.2 us                                                             | 24.4 us: 1.07x faster                                 |
| nbody                   | 96.7 ms                                                             | 90.6 ms: 1.07x faster                                 |
| sympy_sum               | 167 ms                                                              | 159 ms: 1.05x faster                                  |
| float                   | 76.0 ms                                                             | 72.9 ms: 1.04x faster                                 |
| xml_etree_parse         | 162 ms                                                              | 156 ms: 1.04x faster                                  |
| nqueens                 | 84.0 ms                                                             | 80.7 ms: 1.04x faster                                 |
| pycparser               | 1.14 sec                                                            | 1.10 sec: 1.04x faster                                |
| regex_v8                | 22.0 ms                                                             | 21.2 ms: 1.04x faster                                 |
| scimark_fft             | 328 ms                                                              | 317 ms: 1.03x faster                                  |
| fannkuch                | 384 ms                                                              | 372 ms: 1.03x faster                                  |
| logging_format          | 6.64 us                                                             | 6.44 us: 1.03x faster                                 |
| tornado_http            | 96.7 ms                                                             | 93.8 ms: 1.03x faster                                 |
| xml_etree_iterparse     | 108 ms                                                              | 105 ms: 1.03x faster                                  |
| sympy_integrate         | 21.0 ms                                                             | 20.5 ms: 1.03x faster                                 |
| scimark_monte_carlo     | 67.8 ms                                                             | 66.0 ms: 1.03x faster                                 |
| hexiom                  | 6.48 ms                                                             | 6.32 ms: 1.03x faster                                 |
| regex_dna               | 196 ms                                                              | 192 ms: 1.03x faster                                  |
| pickle                  | 9.79 us                                                             | 9.55 us: 1.02x faster                                 |
| sympy_str               | 291 ms                                                              | 284 ms: 1.02x faster                                  |
| logging_simple          | 6.09 us                                                             | 5.95 us: 1.02x faster                                 |
| json                    | 4.86 ms                                                             | 4.75 ms: 1.02x faster                                 |
| html5lib                | 64.0 ms                                                             | 62.6 ms: 1.02x faster                                 |
| meteor_contest          | 106 ms                                                              | 104 ms: 1.02x faster                                  |
| sympy_expand            | 477 ms                                                              | 467 ms: 1.02x faster                                  |
| python_startup          | 8.49 ms                                                             | 8.33 ms: 1.02x faster                                 |
| pathlib                 | 18.2 ms                                                             | 17.9 ms: 1.02x faster                                 |
| spectral_norm           | 99.5 ms                                                             | 97.6 ms: 1.02x faster                                 |
| scimark_lu              | 108 ms                                                              | 107 ms: 1.02x faster                                  |
| pickle_pure_python      | 307 us                                                              | 302 us: 1.02x faster                                  |
| pidigits                | 197 ms                                                              | 194 ms: 1.02x faster                                  |
| telco                   | 6.59 ms                                                             | 6.49 ms: 1.02x faster                                 |
| chaos                   | 68.0 ms                                                             | 66.9 ms: 1.02x faster                                 |
| unpickle_list           | 4.96 us                                                             | 4.89 us: 1.01x faster                                 |
| go                      | 138 ms                                                              | 137 ms: 1.01x faster                                  |
| deltablue               | 3.66 ms                                                             | 3.62 ms: 1.01x faster                                 |
| thrift                  | 766 us                                                              | 759 us: 1.01x faster                                  |
| sqlite_synth            | 2.51 us                                                             | 2.49 us: 1.01x faster                                 |
| regex_compile           | 137 ms                                                              | 135 ms: 1.01x faster                                  |
| crypto_pyaes            | 73.8 ms                                                             | 73.1 ms: 1.01x faster                                 |
| dulwich_log             | 63.6 ms                                                             | 63.1 ms: 1.01x faster                                 |
| xml_etree_process       | 54.1 ms                                                             | 53.8 ms: 1.01x faster                                 |
| pyflate                 | 414 ms                                                              | 411 ms: 1.01x faster                                  |
| 2to3                    | 257 ms                                                              | 256 ms: 1.00x faster                                  |
| xml_etree_generate      | 76.5 ms                                                             | 76.3 ms: 1.00x faster                                 |
| unpickle                | 13.2 us                                                             | 13.3 us: 1.01x slower                                 |
| scimark_sparse_mat_mult | 4.47 ms                                                             | 4.54 ms: 1.02x slower                                 |
| richards                | 45.7 ms                                                             | 46.5 ms: 1.02x slower                                 |
| chameleon               | 6.52 ms                                                             | 6.67 ms: 1.02x slower                                 |
| logging_silent          | 98.7 ns                                                             | 101 ns: 1.03x slower                                  |
| python_startup_no_site  | 5.98 ms                                                             | 6.17 ms: 1.03x slower                                 |
| pickle_list             | 4.03 us                                                             | 4.33 us: 1.07x slower                                 |
| Geometric mean          | (ref)                                                               | 1.02x faster                                          |

Benchmark hidden because not significant (6): json_dumps, unpickle_pure_python, django_template, mako, raytrace, scimark_sor
Ignored benchmarks (36) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, bench_mp_pool, bench_thread_pool, comprehensions, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
