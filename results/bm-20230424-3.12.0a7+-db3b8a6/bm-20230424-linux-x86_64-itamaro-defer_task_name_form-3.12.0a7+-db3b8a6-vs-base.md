
# Results vs. base

- fork: itamaro
- ref: defer_task_name_form
- machine: linux-x86_64
- commit hash: db3b8a6
- commit date: 2023-04-24
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230424-linux-x86_64-python-dca27a69a8261353f7f9-3.12.0a7+-dca27a6 | bm-20230424-linux-x86_64-itamaro-defer_task_name_form-3.12.0a7+-db3b8a6 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 267 ms                                                                 | 267 ms: 1.00x faster                                                    |
| chameleon      | 6.76 ms                                                                | 6.82 ms: 1.01x slower                                                   |
| docutils       | 2.70 sec                                                               | 2.69 sec: 1.01x faster                                                  |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                            |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230424-linux-x86_64-python-dca27a69a8261353f7f9-3.12.0a7+-dca27a6 | bm-20230424-linux-x86_64-itamaro-defer_task_name_form-3.12.0a7+-db3b8a6 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 197 ms                                                                 | 189 ms: 1.04x faster                                                    |
| nbody          | 90.6 ms                                                                | 89.0 ms: 1.02x faster                                                   |
| float          | 79.4 ms                                                                | 80.0 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230424-linux-x86_64-python-dca27a69a8261353f7f9-3.12.0a7+-dca27a6 | bm-20230424-linux-x86_64-itamaro-defer_task_name_form-3.12.0a7+-db3b8a6 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 22.4 ms                                                                | 22.0 ms: 1.02x faster                                                   |
| regex_compile  | 144 ms                                                                 | 142 ms: 1.01x faster                                                    |
| regex_dna      | 204 ms                                                                 | 203 ms: 1.00x faster                                                    |
| regex_effbot   | 3.35 ms                                                                | 3.66 ms: 1.09x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230424-linux-x86_64-python-dca27a69a8261353f7f9-3.12.0a7+-dca27a6 | bm-20230424-linux-x86_64-itamaro-defer_task_name_form-3.12.0a7+-db3b8a6 |
|----------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle             | 14.8 us                                                                | 14.4 us: 1.03x faster                                                   |
| unpickle_list        | 5.19 us                                                                | 5.11 us: 1.02x faster                                                   |
| json_dumps           | 9.78 ms                                                                | 9.68 ms: 1.01x faster                                                   |
| pickle_list          | 4.44 us                                                                | 4.41 us: 1.01x faster                                                   |
| xml_etree_process    | 58.2 ms                                                                | 57.9 ms: 1.00x faster                                                   |
| xml_etree_generate   | 82.8 ms                                                                | 82.5 ms: 1.00x faster                                                   |
| pickle_dict          | 31.5 us                                                                | 31.6 us: 1.00x slower                                                   |
| pickle_pure_python   | 310 us                                                                 | 313 us: 1.01x slower                                                    |
| unpickle_pure_python | 215 us                                                                 | 218 us: 1.02x slower                                                    |
| pickle               | 10.4 us                                                                | 10.7 us: 1.03x slower                                                   |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                            |

Benchmark hidden because not significant (3): json_loads, xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230424-linux-x86_64-python-dca27a69a8261353f7f9-3.12.0a7+-dca27a6 | bm-20230424-linux-x86_64-itamaro-defer_task_name_form-3.12.0a7+-db3b8a6 |
|------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.64 ms                                                                | 6.60 ms: 1.01x faster                                                   |
| python_startup         | 9.05 ms                                                                | 8.99 ms: 1.01x faster                                                   |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20230424-linux-x86_64-python-dca27a69a8261353f7f9-3.12.0a7+-dca27a6 | bm-20230424-linux-x86_64-itamaro-defer_task_name_form-3.12.0a7+-db3b8a6 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text    | 22.8 ms                                                                | 23.0 ms: 1.01x slower                                                   |
| mako           | 10.6 ms                                                                | 10.8 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                            |

Benchmark hidden because not significant (2): genshi_xml, django_template

All benchmarks:
===============

| Benchmark               | bm-20230424-linux-x86_64-python-dca27a69a8261353f7f9-3.12.0a7+-dca27a6 | bm-20230424-linux-x86_64-itamaro-defer_task_name_form-3.12.0a7+-db3b8a6 |
|-------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| scimark_sor             | 131 ms                                                                 | 122 ms: 1.08x faster                                                    |
| mdp                     | 2.74 sec                                                               | 2.59 sec: 1.06x faster                                                  |
| async_tree_memoization  | 651 ms                                                                 | 621 ms: 1.05x faster                                                    |
| async_tree_none         | 523 ms                                                                 | 500 ms: 1.05x faster                                                    |
| pidigits                | 197 ms                                                                 | 189 ms: 1.04x faster                                                    |
| async_tree_io           | 1.29 sec                                                               | 1.25 sec: 1.04x faster                                                  |
| async_tree_cpu_io_mixed | 741 ms                                                                 | 718 ms: 1.03x faster                                                    |
| unpickle                | 14.8 us                                                                | 14.4 us: 1.03x faster                                                   |
| logging_silent          | 101 ns                                                                 | 98.8 ns: 1.02x faster                                                   |
| regex_v8                | 22.4 ms                                                                | 22.0 ms: 1.02x faster                                                   |
| nbody                   | 90.6 ms                                                                | 89.0 ms: 1.02x faster                                                   |
| thrift                  | 808 us                                                                 | 795 us: 1.02x faster                                                    |
| unpickle_list           | 5.19 us                                                                | 5.11 us: 1.02x faster                                                   |
| telco                   | 6.73 ms                                                                | 6.64 ms: 1.01x faster                                                   |
| crypto_pyaes            | 78.0 ms                                                                | 76.9 ms: 1.01x faster                                                   |
| pycparser               | 1.15 sec                                                               | 1.13 sec: 1.01x faster                                                  |
| scimark_monte_carlo     | 71.9 ms                                                                | 71.0 ms: 1.01x faster                                                   |
| json_dumps              | 9.78 ms                                                                | 9.68 ms: 1.01x faster                                                   |
| coroutines              | 22.3 ms                                                                | 22.0 ms: 1.01x faster                                                   |
| regex_compile           | 144 ms                                                                 | 142 ms: 1.01x faster                                                    |
| sqlite_synth            | 2.69 us                                                                | 2.67 us: 1.01x faster                                                   |
| python_startup_no_site  | 6.64 ms                                                                | 6.60 ms: 1.01x faster                                                   |
| python_startup          | 9.05 ms                                                                | 8.99 ms: 1.01x faster                                                   |
| docutils                | 2.70 sec                                                               | 2.69 sec: 1.01x faster                                                  |
| pickle_list             | 4.44 us                                                                | 4.41 us: 1.01x faster                                                   |
| create_gc_cycles        | 1.48 ms                                                                | 1.47 ms: 1.01x faster                                                   |
| xml_etree_process       | 58.2 ms                                                                | 57.9 ms: 1.00x faster                                                   |
| xml_etree_generate      | 82.8 ms                                                                | 82.5 ms: 1.00x faster                                                   |
| regex_dna               | 204 ms                                                                 | 203 ms: 1.00x faster                                                    |
| sympy_sum               | 181 ms                                                                 | 180 ms: 1.00x faster                                                    |
| 2to3                    | 267 ms                                                                 | 267 ms: 1.00x faster                                                    |
| bench_thread_pool       | 833 us                                                                 | 835 us: 1.00x slower                                                    |
| sqlglot_optimize        | 54.6 ms                                                                | 54.7 ms: 1.00x slower                                                   |
| sympy_integrate         | 21.9 ms                                                                | 21.9 ms: 1.00x slower                                                   |
| dulwich_log             | 67.8 ms                                                                | 68.0 ms: 1.00x slower                                                   |
| raytrace                | 299 ms                                                                 | 301 ms: 1.00x slower                                                    |
| unpack_sequence         | 49.3 ns                                                                | 49.5 ns: 1.00x slower                                                   |
| pickle_dict             | 31.5 us                                                                | 31.6 us: 1.00x slower                                                   |
| genshi_text             | 22.8 ms                                                                | 23.0 ms: 1.01x slower                                                   |
| richards                | 42.9 ms                                                                | 43.2 ms: 1.01x slower                                                   |
| pathlib                 | 17.8 ms                                                                | 17.9 ms: 1.01x slower                                                   |
| go                      | 135 ms                                                                 | 136 ms: 1.01x slower                                                    |
| logging_simple          | 6.19 us                                                                | 6.23 us: 1.01x slower                                                   |
| float                   | 79.4 ms                                                                | 80.0 ms: 1.01x slower                                                   |
| chameleon               | 6.76 ms                                                                | 6.82 ms: 1.01x slower                                                   |
| pprint_pformat          | 1.47 sec                                                               | 1.48 sec: 1.01x slower                                                  |
| pickle_pure_python      | 310 us                                                                 | 313 us: 1.01x slower                                                    |
| comprehensions          | 23.1 us                                                                | 23.4 us: 1.01x slower                                                   |
| unpickle_pure_python    | 215 us                                                                 | 218 us: 1.02x slower                                                    |
| mako                    | 10.6 ms                                                                | 10.8 ms: 1.02x slower                                                   |
| scimark_lu              | 108 ms                                                                 | 111 ms: 1.02x slower                                                    |
| pyflate                 | 448 ms                                                                 | 459 ms: 1.03x slower                                                    |
| meteor_contest          | 111 ms                                                                 | 114 ms: 1.03x slower                                                    |
| fannkuch                | 373 ms                                                                 | 383 ms: 1.03x slower                                                    |
| scimark_sparse_mat_mult | 4.65 ms                                                                | 4.78 ms: 1.03x slower                                                   |
| nqueens                 | 79.8 ms                                                                | 82.0 ms: 1.03x slower                                                   |
| pickle                  | 10.4 us                                                                | 10.7 us: 1.03x slower                                                   |
| hexiom                  | 6.13 ms                                                                | 6.36 ms: 1.04x slower                                                   |
| deepcopy_memo           | 37.3 us                                                                | 39.0 us: 1.04x slower                                                   |
| generators              | 30.3 ms                                                                | 32.2 ms: 1.06x slower                                                   |
| regex_effbot            | 3.35 ms                                                                | 3.66 ms: 1.09x slower                                                   |
| gc_traversal            | 3.66 ms                                                                | 4.08 ms: 1.11x slower                                                   |
| Geometric mean          | (ref)                                                                  | 1.00x slower                                                            |

Benchmark hidden because not significant (31): djangocms, tornado_http, sqlalchemy_imperative, genshi_xml, json_loads, sympy_str, sqlalchemy_declarative, json, mypy2, chaos, dask, xml_etree_iterparse, pylint, logging_format, html5lib, bench_mp_pool, asyncio_tcp, sqlglot_transpile, deltablue, coverage, spectral_norm, sqlglot_parse, sqlglot_normalize, async_generators, django_template, deepcopy, deepcopy_reduce, scimark_fft, pprint_safe_repr, xml_etree_parse, sympy_expand
