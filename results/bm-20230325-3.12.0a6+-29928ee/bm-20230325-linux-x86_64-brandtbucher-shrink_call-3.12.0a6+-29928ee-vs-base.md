
# Results vs. base

- fork: brandtbucher
- ref: shrink_call
- machine: linux-x86_64
- commit hash: 29928ee
- commit date: 2023-03-25
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230403-linux-x86_64-python-2a721258a199e9bcdcee-3.12.0a6+-2a72125 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-29928ee |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 252 ms                                                                 | 251 ms: 1.00x faster                                                |
| chameleon      | 6.57 ms                                                                | 6.55 ms: 1.00x faster                                               |
| docutils       | 2.53 sec                                                               | 2.54 sec: 1.01x slower                                              |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230403-linux-x86_64-python-2a721258a199e9bcdcee-3.12.0a6+-2a72125 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-29928ee |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 188 ms                                                                 | 188 ms: 1.00x slower                                                |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (2): nbody, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230403-linux-x86_64-python-2a721258a199e9bcdcee-3.12.0a6+-2a72125 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-29928ee |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 21.9 ms                                                                | 21.4 ms: 1.02x faster                                               |
| regex_dna      | 205 ms                                                                 | 207 ms: 1.01x slower                                                |
| regex_effbot   | 3.41 ms                                                                | 3.45 ms: 1.01x slower                                               |
| regex_compile  | 133 ms                                                                 | 135 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230403-linux-x86_64-python-2a721258a199e9bcdcee-3.12.0a6+-2a72125 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-29928ee |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_dict          | 32.5 us                                                                | 30.7 us: 1.06x faster                                               |
| pickle_list          | 4.33 us                                                                | 4.12 us: 1.05x faster                                               |
| pickle               | 10.6 us                                                                | 10.2 us: 1.04x faster                                               |
| xml_etree_generate   | 80.8 ms                                                                | 81.4 ms: 1.01x slower                                               |
| unpickle_pure_python | 199 us                                                                 | 202 us: 1.01x slower                                                |
| json_loads           | 24.1 us                                                                | 24.4 us: 1.01x slower                                               |
| unpickle_list        | 5.13 us                                                                | 5.23 us: 1.02x slower                                               |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (6): unpickle, json_dumps, xml_etree_process, xml_etree_iterparse, pickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230403-linux-x86_64-python-2a721258a199e9bcdcee-3.12.0a6+-2a72125 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-29928ee |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 8.87 ms                                                                | 8.85 ms: 1.00x faster                                               |
| python_startup_no_site | 6.55 ms                                                                | 6.55 ms: 1.00x faster                                               |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230403-linux-x86_64-python-2a721258a199e9bcdcee-3.12.0a6+-2a72125 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-29928ee |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 21.5 ms                                                                | 21.2 ms: 1.01x faster                                               |
| django_template | 32.9 ms                                                                | 33.3 ms: 1.01x slower                                               |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (2): genshi_xml, mako

All benchmarks:
===============

| Benchmark              | bm-20230403-linux-x86_64-python-2a721258a199e9bcdcee-3.12.0a6+-2a72125 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-29928ee |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mdp                    | 2.69 sec                                                               | 2.50 sec: 1.08x faster                                              |
| pickle_dict            | 32.5 us                                                                | 30.7 us: 1.06x faster                                               |
| pickle_list            | 4.33 us                                                                | 4.12 us: 1.05x faster                                               |
| pickle                 | 10.6 us                                                                | 10.2 us: 1.04x faster                                               |
| chaos                  | 67.5 ms                                                                | 65.8 ms: 1.02x faster                                               |
| json                   | 4.76 ms                                                                | 4.65 ms: 1.02x faster                                               |
| pathlib                | 17.8 ms                                                                | 17.4 ms: 1.02x faster                                               |
| regex_v8               | 21.9 ms                                                                | 21.4 ms: 1.02x faster                                               |
| deepcopy_reduce        | 3.01 us                                                                | 2.96 us: 1.02x faster                                               |
| crypto_pyaes           | 74.3 ms                                                                | 73.1 ms: 1.02x faster                                               |
| async_generators       | 414 ms                                                                 | 408 ms: 1.01x faster                                                |
| deepcopy_memo          | 34.1 us                                                                | 33.7 us: 1.01x faster                                               |
| pprint_pformat         | 1.43 sec                                                               | 1.41 sec: 1.01x faster                                              |
| logging_simple         | 5.79 us                                                                | 5.73 us: 1.01x faster                                               |
| genshi_text            | 21.5 ms                                                                | 21.2 ms: 1.01x faster                                               |
| pprint_safe_repr       | 690 ms                                                                 | 686 ms: 1.01x faster                                                |
| pycparser              | 1.15 sec                                                               | 1.14 sec: 1.01x faster                                              |
| go                     | 138 ms                                                                 | 138 ms: 1.01x faster                                                |
| bench_thread_pool      | 789 us                                                                 | 784 us: 1.01x faster                                                |
| chameleon              | 6.57 ms                                                                | 6.55 ms: 1.00x faster                                               |
| deepcopy               | 328 us                                                                 | 327 us: 1.00x faster                                                |
| 2to3                   | 252 ms                                                                 | 251 ms: 1.00x faster                                                |
| python_startup         | 8.87 ms                                                                | 8.85 ms: 1.00x faster                                               |
| python_startup_no_site | 6.55 ms                                                                | 6.55 ms: 1.00x faster                                               |
| pidigits               | 188 ms                                                                 | 188 ms: 1.00x slower                                                |
| sympy_integrate        | 20.4 ms                                                                | 20.5 ms: 1.00x slower                                               |
| sqlglot_normalize      | 105 ms                                                                 | 105 ms: 1.00x slower                                                |
| sqlglot_optimize       | 51.3 ms                                                                | 51.5 ms: 1.00x slower                                               |
| asyncio_tcp            | 501 ms                                                                 | 504 ms: 1.00x slower                                                |
| deltablue              | 3.19 ms                                                                | 3.21 ms: 1.00x slower                                               |
| sympy_expand           | 460 ms                                                                 | 462 ms: 1.00x slower                                                |
| docutils               | 2.53 sec                                                               | 2.54 sec: 1.01x slower                                              |
| create_gc_cycles       | 1.49 ms                                                                | 1.50 ms: 1.01x slower                                               |
| raytrace               | 283 ms                                                                 | 285 ms: 1.01x slower                                                |
| aiohttp                | 1.01 ms                                                                | 1.01 ms: 1.01x slower                                               |
| nqueens                | 80.0 ms                                                                | 80.6 ms: 1.01x slower                                               |
| sqlglot_parse          | 1.43 ms                                                                | 1.44 ms: 1.01x slower                                               |
| xml_etree_generate     | 80.8 ms                                                                | 81.4 ms: 1.01x slower                                               |
| sympy_str              | 283 ms                                                                 | 285 ms: 1.01x slower                                                |
| sqlglot_transpile      | 1.72 ms                                                                | 1.73 ms: 1.01x slower                                               |
| regex_dna              | 205 ms                                                                 | 207 ms: 1.01x slower                                                |
| meteor_contest         | 103 ms                                                                 | 104 ms: 1.01x slower                                                |
| fannkuch               | 380 ms                                                                 | 384 ms: 1.01x slower                                                |
| sympy_sum              | 165 ms                                                                 | 167 ms: 1.01x slower                                                |
| regex_effbot           | 3.41 ms                                                                | 3.45 ms: 1.01x slower                                               |
| regex_compile          | 133 ms                                                                 | 135 ms: 1.01x slower                                                |
| unpickle_pure_python   | 199 us                                                                 | 202 us: 1.01x slower                                                |
| richards               | 43.6 ms                                                                | 44.2 ms: 1.01x slower                                               |
| json_loads             | 24.1 us                                                                | 24.4 us: 1.01x slower                                               |
| django_template        | 32.9 ms                                                                | 33.3 ms: 1.01x slower                                               |
| unpickle_list          | 5.13 us                                                                | 5.23 us: 1.02x slower                                               |
| scimark_fft            | 304 ms                                                                 | 310 ms: 1.02x slower                                                |
| coverage               | 96.7 ms                                                                | 99.1 ms: 1.02x slower                                               |
| pyflate                | 419 ms                                                                 | 431 ms: 1.03x slower                                                |
| sqlalchemy_declarative | 136 ms                                                                 | 140 ms: 1.03x slower                                                |
| spectral_norm          | 93.1 ms                                                                | 97.3 ms: 1.04x slower                                               |
| generators             | 28.8 ms                                                                | 30.2 ms: 1.05x slower                                               |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (37): unpickle, scimark_lu, logging_silent, genshi_xml, unpack_sequence, thrift, json_dumps, dulwich_log, scimark_monte_carlo, html5lib, sqlite_synth, coroutines, logging_format, nbody, async_tree_io, comprehensions, scimark_sparse_mat_mult, hexiom, gc_traversal, bench_mp_pool, async_tree_none, mako, float, gunicorn, xml_etree_process, xml_etree_iterparse, pickle_pure_python, async_tree_cpu_io_mixed, mypy2, tornado_http, xml_etree_parse, scimark_sor, sqlalchemy_imperative, dask, telco, async_tree_memoization, djangocms
