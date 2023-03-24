
# Results vs. base

- fork: brandtbucher
- ref: shrink_binary_subscr
- machine: linux-x86_64
- commit hash: b174015
- commit date: 2023-03-23
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230324-linux-x86_64-python-f2e5a6ee628502d307a9-3.12.0a6+-f2e5a6e | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-b174015 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                                 | 254 ms: 1.00x slower                                                         |
| chameleon      | 6.57 ms                                                                | 6.52 ms: 1.01x faster                                                        |
| docutils       | 2.54 sec                                                               | 2.56 sec: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230324-linux-x86_64-python-f2e5a6ee628502d307a9-3.12.0a6+-f2e5a6e | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-b174015 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 188 ms                                                                 | 188 ms: 1.00x slower                                                         |
| float          | 73.6 ms                                                                | 74.0 ms: 1.01x slower                                                        |
| nbody          | 87.8 ms                                                                | 88.5 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230324-linux-x86_64-python-f2e5a6ee628502d307a9-3.12.0a6+-f2e5a6e | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-b174015 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.41 ms                                                                | 3.53 ms: 1.03x slower                                                        |
| regex_v8       | 21.3 ms                                                                | 22.2 ms: 1.05x slower                                                        |
| regex_dna      | 202 ms                                                                 | 211 ms: 1.05x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                                 |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark         | bm-20230324-linux-x86_64-python-f2e5a6ee628502d307a9-3.12.0a6+-f2e5a6e | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-b174015 |
|-------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_dict       | 31.5 us                                                                | 31.1 us: 1.01x faster                                                        |
| pickle_list       | 4.39 us                                                                | 4.37 us: 1.01x faster                                                        |
| xml_etree_process | 57.0 ms                                                                | 57.2 ms: 1.00x slower                                                        |
| pickle            | 10.3 us                                                                | 10.4 us: 1.01x slower                                                        |
| json_dumps        | 9.50 ms                                                                | 9.68 ms: 1.02x slower                                                        |
| Geometric mean    | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (8): unpickle, unpickle_list, xml_etree_parse, json_loads, unpickle_pure_python, xml_etree_generate, pickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230324-linux-x86_64-python-f2e5a6ee628502d307a9-3.12.0a6+-f2e5a6e | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-b174015 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.50 ms                                                                | 6.53 ms: 1.00x slower                                                        |
| python_startup         | 8.80 ms                                                                | 8.84 ms: 1.00x slower                                                        |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230324-linux-x86_64-python-f2e5a6ee628502d307a9-3.12.0a6+-f2e5a6e | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-b174015 |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 33.7 ms                                                                | 33.0 ms: 1.02x faster                                                        |
| genshi_xml      | 48.0 ms                                                                | 47.7 ms: 1.01x faster                                                        |
| mako            | 9.91 ms                                                                | 9.85 ms: 1.01x faster                                                        |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20230324-linux-x86_64-python-f2e5a6ee628502d307a9-3.12.0a6+-f2e5a6e | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-b174015 |
|-------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| gc_traversal            | 4.06 ms                                                                | 3.90 ms: 1.04x faster                                                        |
| scimark_lu              | 110 ms                                                                 | 107 ms: 1.03x faster                                                         |
| raytrace                | 286 ms                                                                 | 278 ms: 1.03x faster                                                         |
| sqlglot_normalize       | 107 ms                                                                 | 104 ms: 1.03x faster                                                         |
| scimark_sparse_mat_mult | 4.24 ms                                                                | 4.14 ms: 1.02x faster                                                        |
| richards                | 43.9 ms                                                                | 42.9 ms: 1.02x faster                                                        |
| django_template         | 33.7 ms                                                                | 33.0 ms: 1.02x faster                                                        |
| scimark_sor             | 113 ms                                                                 | 111 ms: 1.02x faster                                                         |
| json                    | 4.62 ms                                                                | 4.55 ms: 1.02x faster                                                        |
| scimark_fft             | 310 ms                                                                 | 306 ms: 1.01x faster                                                         |
| deltablue               | 3.23 ms                                                                | 3.19 ms: 1.01x faster                                                        |
| pickle_dict             | 31.5 us                                                                | 31.1 us: 1.01x faster                                                        |
| unpack_sequence         | 42.9 ns                                                                | 42.4 ns: 1.01x faster                                                        |
| sqlglot_optimize        | 51.4 ms                                                                | 50.8 ms: 1.01x faster                                                        |
| deepcopy_reduce         | 2.97 us                                                                | 2.95 us: 1.01x faster                                                        |
| hexiom                  | 6.08 ms                                                                | 6.03 ms: 1.01x faster                                                        |
| sqlite_synth            | 2.64 us                                                                | 2.62 us: 1.01x faster                                                        |
| chameleon               | 6.57 ms                                                                | 6.52 ms: 1.01x faster                                                        |
| genshi_xml              | 48.0 ms                                                                | 47.7 ms: 1.01x faster                                                        |
| mako                    | 9.91 ms                                                                | 9.85 ms: 1.01x faster                                                        |
| async_generators        | 412 ms                                                                 | 409 ms: 1.01x faster                                                         |
| pickle_list             | 4.39 us                                                                | 4.37 us: 1.01x faster                                                        |
| asyncio_tcp             | 509 ms                                                                 | 507 ms: 1.01x faster                                                         |
| sympy_str               | 286 ms                                                                 | 284 ms: 1.01x faster                                                         |
| comprehensions          | 23.7 us                                                                | 23.7 us: 1.00x faster                                                        |
| pidigits                | 188 ms                                                                 | 188 ms: 1.00x slower                                                         |
| sympy_integrate         | 20.4 ms                                                                | 20.5 ms: 1.00x slower                                                        |
| dulwich_log             | 63.4 ms                                                                | 63.6 ms: 1.00x slower                                                        |
| 2to3                    | 253 ms                                                                 | 254 ms: 1.00x slower                                                         |
| sympy_expand            | 460 ms                                                                 | 462 ms: 1.00x slower                                                         |
| python_startup_no_site  | 6.50 ms                                                                | 6.53 ms: 1.00x slower                                                        |
| python_startup          | 8.80 ms                                                                | 8.84 ms: 1.00x slower                                                        |
| xml_etree_process       | 57.0 ms                                                                | 57.2 ms: 1.00x slower                                                        |
| sympy_sum               | 166 ms                                                                 | 167 ms: 1.00x slower                                                         |
| gunicorn                | 1.09 ms                                                                | 1.09 ms: 1.00x slower                                                        |
| float                   | 73.6 ms                                                                | 74.0 ms: 1.01x slower                                                        |
| pyflate                 | 413 ms                                                                 | 416 ms: 1.01x slower                                                         |
| meteor_contest          | 102 ms                                                                 | 102 ms: 1.01x slower                                                         |
| pickle                  | 10.3 us                                                                | 10.4 us: 1.01x slower                                                        |
| logging_simple          | 5.74 us                                                                | 5.78 us: 1.01x slower                                                        |
| aiohttp                 | 1.01 ms                                                                | 1.02 ms: 1.01x slower                                                        |
| nbody                   | 87.8 ms                                                                | 88.5 ms: 1.01x slower                                                        |
| pathlib                 | 18.0 ms                                                                | 18.2 ms: 1.01x slower                                                        |
| generators              | 28.9 ms                                                                | 29.1 ms: 1.01x slower                                                        |
| pprint_pformat          | 1.41 sec                                                               | 1.42 sec: 1.01x slower                                                       |
| docutils                | 2.54 sec                                                               | 2.56 sec: 1.01x slower                                                       |
| create_gc_cycles        | 1.47 ms                                                                | 1.49 ms: 1.01x slower                                                        |
| logging_format          | 6.31 us                                                                | 6.38 us: 1.01x slower                                                        |
| nqueens                 | 81.3 ms                                                                | 82.6 ms: 1.02x slower                                                        |
| go                      | 138 ms                                                                 | 140 ms: 1.02x slower                                                         |
| telco                   | 6.38 ms                                                                | 6.49 ms: 1.02x slower                                                        |
| json_dumps              | 9.50 ms                                                                | 9.68 ms: 1.02x slower                                                        |
| spectral_norm           | 92.7 ms                                                                | 94.5 ms: 1.02x slower                                                        |
| chaos                   | 65.6 ms                                                                | 66.9 ms: 1.02x slower                                                        |
| mdp                     | 2.63 sec                                                               | 2.68 sec: 1.02x slower                                                       |
| thrift                  | 796 us                                                                 | 812 us: 1.02x slower                                                         |
| fannkuch                | 376 ms                                                                 | 383 ms: 1.02x slower                                                         |
| scimark_monte_carlo     | 67.2 ms                                                                | 69.1 ms: 1.03x slower                                                        |
| regex_effbot            | 3.41 ms                                                                | 3.53 ms: 1.03x slower                                                        |
| pycparser               | 1.12 sec                                                               | 1.16 sec: 1.04x slower                                                       |
| regex_v8                | 21.3 ms                                                                | 22.2 ms: 1.05x slower                                                        |
| regex_dna               | 202 ms                                                                 | 211 ms: 1.05x slower                                                         |
| Geometric mean          | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (32): unpickle, unpickle_list, html5lib, async_tree_none, coverage, xml_etree_parse, mypy2, json_loads, async_tree_io, unpickle_pure_python, xml_etree_generate, pprint_safe_repr, regex_compile, deepcopy, crypto_pyaes, sqlalchemy_declarative, bench_mp_pool, dask, bench_thread_pool, tornado_http, pickle_pure_python, xml_etree_iterparse, genshi_text, deepcopy_memo, sqlglot_parse, async_tree_cpu_io_mixed, sqlglot_transpile, async_tree_memoization, djangocms, logging_silent, coroutines, sqlalchemy_imperative
