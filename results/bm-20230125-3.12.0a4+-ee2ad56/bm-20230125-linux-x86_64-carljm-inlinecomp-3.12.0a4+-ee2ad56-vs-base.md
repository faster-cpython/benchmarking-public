
# Results vs. base

- fork: carljm
- ref: inlinecomp
- machine: linux-x86_64
- commit hash: ee2ad56
- commit date: 2023-01-25
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230124-linux-x86_64-python-f02fa64bf2d03ef7a286-3.12.0a4+-f02fa64 | bm-20230125-linux-x86_64-carljm-inlinecomp-3.12.0a4+-ee2ad56 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 251 ms                                                                 | 249 ms: 1.01x faster                                         |
| docutils       | 2.55 sec                                                               | 2.51 sec: 1.02x faster                                       |
| tornado_http   | 93.6 ms                                                                | 94.5 ms: 1.01x slower                                        |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                 |

Benchmark hidden because not significant (2): chameleon, html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230124-linux-x86_64-python-f02fa64bf2d03ef7a286-3.12.0a4+-f02fa64 | bm-20230125-linux-x86_64-carljm-inlinecomp-3.12.0a4+-ee2ad56 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 73.2 ms                                                                | 72.0 ms: 1.02x faster                                        |
| pidigits       | 189 ms                                                                 | 190 ms: 1.00x slower                                         |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230124-linux-x86_64-python-f02fa64bf2d03ef7a286-3.12.0a4+-f02fa64 | bm-20230125-linux-x86_64-carljm-inlinecomp-3.12.0a4+-ee2ad56 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 127 ms                                                                 | 128 ms: 1.01x slower                                         |
| regex_dna      | 210 ms                                                                 | 201 ms: 1.05x faster                                         |
| regex_effbot   | 3.49 ms                                                                | 3.42 ms: 1.02x faster                                        |
| regex_v8       | 22.4 ms                                                                | 21.3 ms: 1.05x faster                                        |
| Geometric mean | (ref)                                                                  | 1.03x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230124-linux-x86_64-python-f02fa64bf2d03ef7a286-3.12.0a4+-f02fa64 | bm-20230125-linux-x86_64-carljm-inlinecomp-3.12.0a4+-ee2ad56 |
|----------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| json_dumps           | 9.32 ms                                                                | 9.57 ms: 1.03x slower                                        |
| json_loads           | 24.5 us                                                                | 24.2 us: 1.01x faster                                        |
| pickle               | 10.1 us                                                                | 10.2 us: 1.02x slower                                        |
| pickle_dict          | 30.9 us                                                                | 32.4 us: 1.05x slower                                        |
| pickle_list          | 4.12 us                                                                | 4.29 us: 1.04x slower                                        |
| pickle_pure_python   | 286 us                                                                 | 288 us: 1.01x slower                                         |
| unpickle             | 13.2 us                                                                | 13.1 us: 1.01x faster                                        |
| unpickle_pure_python | 197 us                                                                 | 201 us: 1.02x slower                                         |
| xml_etree_iterparse  | 109 ms                                                                 | 106 ms: 1.02x faster                                         |
| xml_etree_process    | 54.1 ms                                                                | 53.8 ms: 1.01x faster                                        |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                 |

Benchmark hidden because not significant (3): unpickle_list, xml_etree_parse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230124-linux-x86_64-python-f02fa64bf2d03ef7a286-3.12.0a4+-f02fa64 | bm-20230125-linux-x86_64-carljm-inlinecomp-3.12.0a4+-ee2ad56 |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 8.98 ms                                                                | 8.89 ms: 1.01x faster                                        |
| python_startup_no_site | 6.50 ms                                                                | 6.44 ms: 1.01x faster                                        |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20230124-linux-x86_64-python-f02fa64bf2d03ef7a286-3.12.0a4+-f02fa64 | bm-20230125-linux-x86_64-carljm-inlinecomp-3.12.0a4+-ee2ad56 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| mako           | 9.80 ms                                                                | 9.70 ms: 1.01x faster                                        |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                 |

Benchmark hidden because not significant (3): django_template, genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20230124-linux-x86_64-python-f02fa64bf2d03ef7a286-3.12.0a4+-f02fa64 | bm-20230125-linux-x86_64-carljm-inlinecomp-3.12.0a4+-ee2ad56 |
|-------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3                    | 251 ms                                                                 | 249 ms: 1.01x faster                                         |
| async_generators        | 349 ms                                                                 | 355 ms: 1.02x slower                                         |
| async_tree_memoization  | 624 ms                                                                 | 656 ms: 1.05x slower                                         |
| asyncio_tcp             | 488 ms                                                                 | 492 ms: 1.01x slower                                         |
| chaos                   | 66.2 ms                                                                | 64.6 ms: 1.02x faster                                        |
| bench_thread_pool       | 775 us                                                                 | 781 us: 1.01x slower                                         |
| coroutines              | 24.8 ms                                                                | 25.6 ms: 1.03x slower                                        |
| deepcopy_reduce         | 2.91 us                                                                | 2.96 us: 1.02x slower                                        |
| deepcopy_memo           | 33.8 us                                                                | 34.6 us: 1.02x slower                                        |
| docutils                | 2.55 sec                                                               | 2.51 sec: 1.02x faster                                       |
| fannkuch                | 373 ms                                                                 | 369 ms: 1.01x faster                                         |
| float                   | 73.2 ms                                                                | 72.0 ms: 1.02x faster                                        |
| create_gc_cycles        | 1.47 ms                                                                | 1.44 ms: 1.02x faster                                        |
| gc_traversal            | 4.30 ms                                                                | 3.64 ms: 1.18x faster                                        |
| generators              | 76.5 ms                                                                | 75.9 ms: 1.01x faster                                        |
| go                      | 138 ms                                                                 | 134 ms: 1.03x faster                                         |
| gunicorn                | 1.07 ms                                                                | 1.06 ms: 1.00x faster                                        |
| json                    | 4.62 ms                                                                | 4.69 ms: 1.01x slower                                        |
| json_dumps              | 9.32 ms                                                                | 9.57 ms: 1.03x slower                                        |
| json_loads              | 24.5 us                                                                | 24.2 us: 1.01x faster                                        |
| logging_format          | 6.40 us                                                                | 6.31 us: 1.01x faster                                        |
| logging_silent          | 92.8 ns                                                                | 91.7 ns: 1.01x faster                                        |
| logging_simple          | 5.76 us                                                                | 5.80 us: 1.01x slower                                        |
| mako                    | 9.80 ms                                                                | 9.70 ms: 1.01x faster                                        |
| mdp                     | 2.69 sec                                                               | 2.51 sec: 1.07x faster                                       |
| pathlib                 | 17.7 ms                                                                | 17.9 ms: 1.01x slower                                        |
| pickle                  | 10.1 us                                                                | 10.2 us: 1.02x slower                                        |
| pickle_dict             | 30.9 us                                                                | 32.4 us: 1.05x slower                                        |
| pickle_list             | 4.12 us                                                                | 4.29 us: 1.04x slower                                        |
| pickle_pure_python      | 286 us                                                                 | 288 us: 1.01x slower                                         |
| pidigits                | 189 ms                                                                 | 190 ms: 1.00x slower                                         |
| pycparser               | 1.15 sec                                                               | 1.09 sec: 1.05x faster                                       |
| pyflate                 | 402 ms                                                                 | 400 ms: 1.01x faster                                         |
| python_startup          | 8.98 ms                                                                | 8.89 ms: 1.01x faster                                        |
| python_startup_no_site  | 6.50 ms                                                                | 6.44 ms: 1.01x faster                                        |
| raytrace                | 281 ms                                                                 | 284 ms: 1.01x slower                                         |
| regex_compile           | 127 ms                                                                 | 128 ms: 1.01x slower                                         |
| regex_dna               | 210 ms                                                                 | 201 ms: 1.05x faster                                         |
| regex_effbot            | 3.49 ms                                                                | 3.42 ms: 1.02x faster                                        |
| regex_v8                | 22.4 ms                                                                | 21.3 ms: 1.05x faster                                        |
| richards                | 41.7 ms                                                                | 42.6 ms: 1.02x slower                                        |
| scimark_fft             | 301 ms                                                                 | 303 ms: 1.01x slower                                         |
| scimark_monte_carlo     | 65.6 ms                                                                | 64.7 ms: 1.01x faster                                        |
| scimark_sparse_mat_mult | 3.96 ms                                                                | 3.99 ms: 1.01x slower                                        |
| spectral_norm           | 95.3 ms                                                                | 96.2 ms: 1.01x slower                                        |
| sqlglot_optimize        | 51.0 ms                                                                | 50.5 ms: 1.01x faster                                        |
| sqlglot_normalize       | 105 ms                                                                 | 103 ms: 1.02x faster                                         |
| sympy_expand            | 453 ms                                                                 | 450 ms: 1.01x faster                                         |
| sympy_integrate         | 19.7 ms                                                                | 19.7 ms: 1.00x faster                                        |
| sympy_sum               | 154 ms                                                                 | 155 ms: 1.00x slower                                         |
| telco                   | 6.26 ms                                                                | 6.46 ms: 1.03x slower                                        |
| thrift                  | 737 us                                                                 | 748 us: 1.01x slower                                         |
| tornado_http            | 93.6 ms                                                                | 94.5 ms: 1.01x slower                                        |
| unpack_sequence         | 46.7 ns                                                                | 44.4 ns: 1.05x faster                                        |
| unpickle                | 13.2 us                                                                | 13.1 us: 1.01x faster                                        |
| unpickle_pure_python    | 197 us                                                                 | 201 us: 1.02x slower                                         |
| xml_etree_iterparse     | 109 ms                                                                 | 106 ms: 1.02x faster                                         |
| xml_etree_process       | 54.1 ms                                                                | 53.8 ms: 1.01x faster                                        |
| Geometric mean          | (ref)                                                                  | 1.00x faster                                                 |

Benchmark hidden because not significant (33): aiohttp, async_tree_none, async_tree_cpu_io_mixed, async_tree_io, chameleon, bench_mp_pool, coverage, crypto_pyaes, dask, deepcopy, deltablue, django_template, djangocms, dulwich_log, genshi_text, genshi_xml, hexiom, html5lib, meteor_contest, mypy, nbody, nqueens, pprint_safe_repr, pprint_pformat, scimark_lu, scimark_sor, sqlglot_parse, sqlglot_transpile, sqlite_synth, sympy_str, unpickle_list, xml_etree_parse, xml_etree_generate
