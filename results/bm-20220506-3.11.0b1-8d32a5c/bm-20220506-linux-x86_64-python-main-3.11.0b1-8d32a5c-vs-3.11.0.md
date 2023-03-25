
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 8d32a5c
- commit date: 2022-05-06
- overall geometric mean: 1.02x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220506-linux-x86_64-python-main-3.11.0b1-8d32a5c |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 257 ms                                                              | 256 ms: 1.00x faster                                  |
| chameleon      | 6.52 ms                                                             | 6.57 ms: 1.01x slower                                 |
| html5lib       | 64.0 ms                                                             | 60.1 ms: 1.06x faster                                 |
| tornado_http   | 96.7 ms                                                             | 94.6 ms: 1.02x faster                                 |
| Geometric mean | (ref)                                                               | 1.02x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220506-linux-x86_64-python-main-3.11.0b1-8d32a5c |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| float          | 76.0 ms                                                             | 72.5 ms: 1.05x faster                                 |
| nbody          | 96.7 ms                                                             | 93.1 ms: 1.04x faster                                 |
| pidigits       | 197 ms                                                              | 190 ms: 1.04x faster                                  |
| Geometric mean | (ref)                                                               | 1.04x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220506-linux-x86_64-python-main-3.11.0b1-8d32a5c |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| regex_effbot   | 3.32 ms                                                             | 2.93 ms: 1.13x faster                                 |
| regex_v8       | 22.0 ms                                                             | 21.6 ms: 1.02x faster                                 |
| regex_compile  | 137 ms                                                              | 135 ms: 1.01x faster                                  |
| regex_dna      | 196 ms                                                              | 204 ms: 1.04x slower                                  |
| Geometric mean | (ref)                                                               | 1.03x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220506-linux-x86_64-python-main-3.11.0b1-8d32a5c |
|---------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_dict         | 30.9 us                                                             | 25.6 us: 1.21x faster                                 |
| xml_etree_parse     | 162 ms                                                              | 157 ms: 1.03x faster                                  |
| xml_etree_iterparse | 108 ms                                                              | 104 ms: 1.03x faster                                  |
| json_loads          | 26.2 us                                                             | 25.4 us: 1.03x faster                                 |
| pickle              | 9.79 us                                                             | 9.56 us: 1.02x faster                                 |
| json_dumps          | 12.5 ms                                                             | 12.4 ms: 1.01x faster                                 |
| xml_etree_process   | 54.1 ms                                                             | 53.6 ms: 1.01x faster                                 |
| pickle_pure_python  | 307 us                                                              | 305 us: 1.01x faster                                  |
| unpickle            | 13.2 us                                                             | 13.4 us: 1.01x slower                                 |
| unpickle_list       | 4.96 us                                                             | 5.05 us: 1.02x slower                                 |
| pickle_list         | 4.03 us                                                             | 4.26 us: 1.06x slower                                 |
| Geometric mean      | (ref)                                                               | 1.02x faster                                          |

Benchmark hidden because not significant (2): xml_etree_generate, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220506-linux-x86_64-python-main-3.11.0b1-8d32a5c |
|------------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 8.49 ms                                                             | 8.25 ms: 1.03x faster                                 |
| python_startup_no_site | 5.98 ms                                                             | 6.16 ms: 1.03x slower                                 |
| Geometric mean         | (ref)                                                               | 1.00x slower                                          |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220506-linux-x86_64-python-main-3.11.0b1-8d32a5c |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| mako           | 9.82 ms                                                             | 9.88 ms: 1.01x slower                                 |
| Geometric mean | (ref)                                                               | 1.00x slower                                          |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220506-linux-x86_64-python-main-3.11.0b1-8d32a5c |
|-------------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_dict             | 30.9 us                                                             | 25.6 us: 1.21x faster                                 |
| regex_effbot            | 3.32 ms                                                             | 2.93 ms: 1.13x faster                                 |
| unpack_sequence         | 49.5 ns                                                             | 44.3 ns: 1.12x faster                                 |
| html5lib                | 64.0 ms                                                             | 60.1 ms: 1.06x faster                                 |
| float                   | 76.0 ms                                                             | 72.5 ms: 1.05x faster                                 |
| sympy_sum               | 167 ms                                                              | 161 ms: 1.04x faster                                  |
| nbody                   | 96.7 ms                                                             | 93.1 ms: 1.04x faster                                 |
| pidigits                | 197 ms                                                              | 190 ms: 1.04x faster                                  |
| logging_simple          | 6.09 us                                                             | 5.89 us: 1.03x faster                                 |
| thrift                  | 766 us                                                              | 741 us: 1.03x faster                                  |
| xml_etree_parse         | 162 ms                                                              | 157 ms: 1.03x faster                                  |
| xml_etree_iterparse     | 108 ms                                                              | 104 ms: 1.03x faster                                  |
| json_loads              | 26.2 us                                                             | 25.4 us: 1.03x faster                                 |
| hexiom                  | 6.48 ms                                                             | 6.29 ms: 1.03x faster                                 |
| logging_format          | 6.64 us                                                             | 6.44 us: 1.03x faster                                 |
| python_startup          | 8.49 ms                                                             | 8.25 ms: 1.03x faster                                 |
| sympy_integrate         | 21.0 ms                                                             | 20.5 ms: 1.03x faster                                 |
| sympy_str               | 291 ms                                                              | 284 ms: 1.03x faster                                  |
| pickle                  | 9.79 us                                                             | 9.56 us: 1.02x faster                                 |
| tornado_http            | 96.7 ms                                                             | 94.6 ms: 1.02x faster                                 |
| scimark_monte_carlo     | 67.8 ms                                                             | 66.5 ms: 1.02x faster                                 |
| sympy_expand            | 477 ms                                                              | 468 ms: 1.02x faster                                  |
| spectral_norm           | 99.5 ms                                                             | 97.6 ms: 1.02x faster                                 |
| pathlib                 | 18.2 ms                                                             | 17.9 ms: 1.02x faster                                 |
| go                      | 138 ms                                                              | 136 ms: 1.02x faster                                  |
| regex_v8                | 22.0 ms                                                             | 21.6 ms: 1.02x faster                                 |
| meteor_contest          | 106 ms                                                              | 105 ms: 1.01x faster                                  |
| json_dumps              | 12.5 ms                                                             | 12.4 ms: 1.01x faster                                 |
| regex_compile           | 137 ms                                                              | 135 ms: 1.01x faster                                  |
| deltablue               | 3.66 ms                                                             | 3.61 ms: 1.01x faster                                 |
| dulwich_log             | 63.6 ms                                                             | 62.8 ms: 1.01x faster                                 |
| xml_etree_process       | 54.1 ms                                                             | 53.6 ms: 1.01x faster                                 |
| pyflate                 | 414 ms                                                              | 411 ms: 1.01x faster                                  |
| pickle_pure_python      | 307 us                                                              | 305 us: 1.01x faster                                  |
| logging_silent          | 98.7 ns                                                             | 98.2 ns: 1.01x faster                                 |
| 2to3                    | 257 ms                                                              | 256 ms: 1.00x faster                                  |
| mako                    | 9.82 ms                                                             | 9.88 ms: 1.01x slower                                 |
| raytrace                | 292 ms                                                              | 294 ms: 1.01x slower                                  |
| crypto_pyaes            | 73.8 ms                                                             | 74.3 ms: 1.01x slower                                 |
| chameleon               | 6.52 ms                                                             | 6.57 ms: 1.01x slower                                 |
| nqueens                 | 84.0 ms                                                             | 84.7 ms: 1.01x slower                                 |
| chaos                   | 68.0 ms                                                             | 68.6 ms: 1.01x slower                                 |
| json                    | 4.86 ms                                                             | 4.91 ms: 1.01x slower                                 |
| unpickle                | 13.2 us                                                             | 13.4 us: 1.01x slower                                 |
| richards                | 45.7 ms                                                             | 46.4 ms: 1.02x slower                                 |
| unpickle_list           | 4.96 us                                                             | 5.05 us: 1.02x slower                                 |
| scimark_sparse_mat_mult | 4.47 ms                                                             | 4.57 ms: 1.02x slower                                 |
| python_startup_no_site  | 5.98 ms                                                             | 6.16 ms: 1.03x slower                                 |
| pycparser               | 1.14 sec                                                            | 1.18 sec: 1.03x slower                                |
| regex_dna               | 196 ms                                                              | 204 ms: 1.04x slower                                  |
| telco                   | 6.59 ms                                                             | 6.84 ms: 1.04x slower                                 |
| pickle_list             | 4.03 us                                                             | 4.26 us: 1.06x slower                                 |
| Geometric mean          | (ref)                                                               | 1.02x faster                                          |

Benchmark hidden because not significant (8): scimark_fft, django_template, scimark_sor, xml_etree_generate, unpickle_pure_python, fannkuch, sqlite_synth, scimark_lu
Ignored benchmarks (36) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, bench_mp_pool, bench_thread_pool, comprehensions, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
