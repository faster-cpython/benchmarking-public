
# Results vs. 3.11.0

- fork: python
- ref: v3.11.1
- machine: linux-x86_64
- commit hash: a7a450f
- commit date: 2022-12-06
- overall geometric mean: 1.00x slower \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 257 ms                                                              | 258 ms: 1.00x slower                                   |
| chameleon      | 6.52 ms                                                             | 6.63 ms: 1.02x slower                                  |
| docutils       | 2.59 sec                                                            | 2.57 sec: 1.01x faster                                 |
| tornado_http   | 96.7 ms                                                             | 99.8 ms: 1.03x slower                                  |
| Geometric mean | (ref)                                                               | 1.01x slower                                           |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| pidigits       | 197 ms                                                              | 190 ms: 1.04x faster                                   |
| nbody          | 96.7 ms                                                             | 95.4 ms: 1.01x faster                                  |
| Geometric mean | (ref)                                                               | 1.02x faster                                           |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.32 ms                                                             | 3.31 ms: 1.00x faster                                  |
| regex_compile  | 137 ms                                                              | 137 ms: 1.00x slower                                   |
| regex_v8       | 22.0 ms                                                             | 22.3 ms: 1.02x slower                                  |
| regex_dna      | 196 ms                                                              | 200 ms: 1.02x slower                                   |
| Geometric mean | (ref)                                                               | 1.01x slower                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|---------------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| json_loads          | 26.2 us                                                             | 24.0 us: 1.09x faster                                  |
| xml_etree_iterparse | 108 ms                                                              | 103 ms: 1.04x faster                                   |
| xml_etree_parse     | 162 ms                                                              | 158 ms: 1.03x faster                                   |
| pickle              | 9.79 us                                                             | 9.72 us: 1.01x faster                                  |
| xml_etree_process   | 54.1 ms                                                             | 53.7 ms: 1.01x faster                                  |
| pickle_dict         | 30.9 us                                                             | 31.1 us: 1.00x slower                                  |
| json_dumps          | 12.5 ms                                                             | 12.6 ms: 1.01x slower                                  |
| pickle_pure_python  | 307 us                                                              | 310 us: 1.01x slower                                   |
| unpickle            | 13.2 us                                                             | 13.4 us: 1.01x slower                                  |
| pickle_list         | 4.03 us                                                             | 4.17 us: 1.03x slower                                  |
| Geometric mean      | (ref)                                                               | 1.01x faster                                           |

Benchmark hidden because not significant (3): unpickle_list, xml_etree_generate, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 5.98 ms                                                             | 5.98 ms: 1.00x slower                                  |
| Geometric mean         | (ref)                                                               | 1.00x slower                                           |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 9.82 ms                                                             | 9.92 ms: 1.01x slower                                  |
| django_template | 32.9 ms                                                             | 33.2 ms: 1.01x slower                                  |
| genshi_xml      | 51.8 ms                                                             | 52.5 ms: 1.01x slower                                  |
| genshi_text     | 21.8 ms                                                             | 22.1 ms: 1.01x slower                                  |
| Geometric mean  | (ref)                                                               | 1.01x slower                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|-------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| unpack_sequence         | 49.5 ns                                                             | 44.6 ns: 1.11x faster                                  |
| json_loads              | 26.2 us                                                             | 24.0 us: 1.09x faster                                  |
| json                    | 4.86 ms                                                             | 4.63 ms: 1.05x faster                                  |
| xml_etree_iterparse     | 108 ms                                                              | 103 ms: 1.04x faster                                   |
| pidigits                | 197 ms                                                              | 190 ms: 1.04x faster                                   |
| coroutines              | 26.3 ms                                                             | 25.3 ms: 1.04x faster                                  |
| pylint                  | 476 ms                                                              | 461 ms: 1.03x faster                                   |
| xml_etree_parse         | 162 ms                                                              | 158 ms: 1.03x faster                                   |
| logging_simple          | 6.09 us                                                             | 5.95 us: 1.02x faster                                  |
| sqlite_synth            | 2.51 us                                                             | 2.47 us: 1.02x faster                                  |
| crypto_pyaes            | 73.8 ms                                                             | 72.6 ms: 1.02x faster                                  |
| logging_format          | 6.64 us                                                             | 6.54 us: 1.01x faster                                  |
| nbody                   | 96.7 ms                                                             | 95.4 ms: 1.01x faster                                  |
| scimark_lu              | 108 ms                                                              | 107 ms: 1.01x faster                                   |
| async_generators        | 361 ms                                                              | 358 ms: 1.01x faster                                   |
| pprint_pformat          | 1.45 sec                                                            | 1.44 sec: 1.01x faster                                 |
| sympy_sum               | 167 ms                                                              | 166 ms: 1.01x faster                                   |
| sympy_expand            | 477 ms                                                              | 472 ms: 1.01x faster                                   |
| docutils                | 2.59 sec                                                            | 2.57 sec: 1.01x faster                                 |
| dask                    | 368 ms                                                              | 365 ms: 1.01x faster                                   |
| bench_thread_pool       | 820 us                                                              | 813 us: 1.01x faster                                   |
| sympy_str               | 291 ms                                                              | 289 ms: 1.01x faster                                   |
| pickle                  | 9.79 us                                                             | 9.72 us: 1.01x faster                                  |
| xml_etree_process       | 54.1 ms                                                             | 53.7 ms: 1.01x faster                                  |
| pathlib                 | 18.2 ms                                                             | 18.1 ms: 1.01x faster                                  |
| aiohttp                 | 1.05 ms                                                             | 1.05 ms: 1.00x faster                                  |
| hexiom                  | 6.48 ms                                                             | 6.46 ms: 1.00x faster                                  |
| regex_effbot            | 3.32 ms                                                             | 3.31 ms: 1.00x faster                                  |
| sympy_integrate         | 21.0 ms                                                             | 21.0 ms: 1.00x faster                                  |
| gunicorn                | 1.13 ms                                                             | 1.13 ms: 1.00x faster                                  |
| generators              | 73.4 ms                                                             | 73.3 ms: 1.00x faster                                  |
| python_startup_no_site  | 5.98 ms                                                             | 5.98 ms: 1.00x slower                                  |
| regex_compile           | 137 ms                                                              | 137 ms: 1.00x slower                                   |
| pyflate                 | 414 ms                                                              | 415 ms: 1.00x slower                                   |
| pickle_dict             | 30.9 us                                                             | 31.1 us: 1.00x slower                                  |
| 2to3                    | 257 ms                                                              | 258 ms: 1.00x slower                                   |
| json_dumps              | 12.5 ms                                                             | 12.6 ms: 1.01x slower                                  |
| pickle_pure_python      | 307 us                                                              | 310 us: 1.01x slower                                   |
| async_tree_cpu_io_mixed | 736 ms                                                              | 742 ms: 1.01x slower                                   |
| go                      | 138 ms                                                              | 140 ms: 1.01x slower                                   |
| scimark_sor             | 115 ms                                                              | 116 ms: 1.01x slower                                   |
| mako                    | 9.82 ms                                                             | 9.92 ms: 1.01x slower                                  |
| django_template         | 32.9 ms                                                             | 33.2 ms: 1.01x slower                                  |
| telco                   | 6.59 ms                                                             | 6.66 ms: 1.01x slower                                  |
| nqueens                 | 84.0 ms                                                             | 85.0 ms: 1.01x slower                                  |
| unpickle                | 13.2 us                                                             | 13.4 us: 1.01x slower                                  |
| sqlglot_parse           | 1.36 ms                                                             | 1.38 ms: 1.01x slower                                  |
| genshi_xml              | 51.8 ms                                                             | 52.5 ms: 1.01x slower                                  |
| genshi_text             | 21.8 ms                                                             | 22.1 ms: 1.01x slower                                  |
| sqlglot_transpile       | 1.65 ms                                                             | 1.68 ms: 1.02x slower                                  |
| regex_v8                | 22.0 ms                                                             | 22.3 ms: 1.02x slower                                  |
| chameleon               | 6.52 ms                                                             | 6.63 ms: 1.02x slower                                  |
| pycparser               | 1.14 sec                                                            | 1.16 sec: 1.02x slower                                 |
| regex_dna               | 196 ms                                                              | 200 ms: 1.02x slower                                   |
| spectral_norm           | 99.5 ms                                                             | 101 ms: 1.02x slower                                   |
| async_tree_io           | 1.28 sec                                                            | 1.31 sec: 1.02x slower                                 |
| sqlalchemy_declarative  | 138 ms                                                              | 141 ms: 1.02x slower                                   |
| deepcopy_memo           | 36.4 us                                                             | 37.2 us: 1.02x slower                                  |
| chaos                   | 68.0 ms                                                             | 69.6 ms: 1.02x slower                                  |
| djangocms               | 32.3 us                                                             | 33.1 us: 1.03x slower                                  |
| scimark_sparse_mat_mult | 4.47 ms                                                             | 4.59 ms: 1.03x slower                                  |
| coverage                | 101 ms                                                              | 104 ms: 1.03x slower                                   |
| richards                | 45.7 ms                                                             | 46.9 ms: 1.03x slower                                  |
| deepcopy                | 339 us                                                              | 349 us: 1.03x slower                                   |
| tornado_http            | 96.7 ms                                                             | 99.8 ms: 1.03x slower                                  |
| logging_silent          | 98.7 ns                                                             | 102 ns: 1.03x slower                                   |
| pickle_list             | 4.03 us                                                             | 4.17 us: 1.03x slower                                  |
| deepcopy_reduce         | 2.96 us                                                             | 3.09 us: 1.05x slower                                  |
| gc_traversal            | 3.63 ms                                                             | 4.26 ms: 1.17x slower                                  |
| Geometric mean          | (ref)                                                               | 1.00x slower                                           |

Benchmark hidden because not significant (26): html5lib, async_tree_none, unpickle_list, mypy2, meteor_contest, flaskblogging, dulwich_log, pprint_safe_repr, sqlalchemy_imperative, sqlglot_optimize, bench_mp_pool, scimark_fft, thrift, mdp, sqlglot_normalize, python_startup, float, xml_etree_generate, fannkuch, unpickle_pure_python, asyncio_tcp, create_gc_cycles, deltablue, raytrace, scimark_monte_carlo, async_tree_memoization
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: comprehensions
