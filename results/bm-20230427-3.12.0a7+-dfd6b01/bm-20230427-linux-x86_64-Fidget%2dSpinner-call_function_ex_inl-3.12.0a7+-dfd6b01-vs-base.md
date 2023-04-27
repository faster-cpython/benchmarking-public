
# Results vs. base

- fork: Fidget-Spinner
- ref: call_function_ex_inl
- machine: linux-x86_64
- commit hash: dfd6b01
- commit date: 2023-04-27
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230427-linux-x86_64-python-dff8e5dc8d0758d1f9c5-3.12.0a7+-dff8e5d | bm-20230427-linux-x86_64-Fidget%2dSpinner-call_function_ex_inl-3.12.0a7+-dfd6b01 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                                 | 269 ms: 1.00x slower                                                             |
| chameleon      | 6.90 ms                                                                | 6.96 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                     |

Benchmark hidden because not significant (3): docutils, html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230427-linux-x86_64-python-dff8e5dc8d0758d1f9c5-3.12.0a7+-dff8e5d | bm-20230427-linux-x86_64-Fidget%2dSpinner-call_function_ex_inl-3.12.0a7+-dfd6b01 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 81.6 ms                                                                | 82.2 ms: 1.01x slower                                                            |
| pidigits       | 189 ms                                                                 | 197 ms: 1.05x slower                                                             |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                                     |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230427-linux-x86_64-python-dff8e5dc8d0758d1f9c5-3.12.0a7+-dff8e5d | bm-20230427-linux-x86_64-Fidget%2dSpinner-call_function_ex_inl-3.12.0a7+-dfd6b01 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.79 ms                                                                | 3.45 ms: 1.10x faster                                                            |
| regex_dna      | 204 ms                                                                 | 207 ms: 1.01x slower                                                             |
| regex_v8       | 22.1 ms                                                                | 22.8 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                     |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230427-linux-x86_64-python-dff8e5dc8d0758d1f9c5-3.12.0a7+-dff8e5d | bm-20230427-linux-x86_64-Fidget%2dSpinner-call_function_ex_inl-3.12.0a7+-dfd6b01 |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pickle               | 10.7 us                                                                | 10.5 us: 1.03x faster                                                            |
| pickle_dict          | 32.3 us                                                                | 31.6 us: 1.02x faster                                                            |
| pickle_list          | 4.64 us                                                                | 4.61 us: 1.01x faster                                                            |
| pickle_pure_python   | 316 us                                                                 | 319 us: 1.01x slower                                                             |
| unpickle_pure_python | 216 us                                                                 | 219 us: 1.02x slower                                                             |
| unpickle_list        | 4.86 us                                                                | 5.00 us: 1.03x slower                                                            |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                                     |

Benchmark hidden because not significant (7): json_dumps, xml_etree_iterparse, json_loads, unpickle, xml_etree_generate, xml_etree_parse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230427-linux-x86_64-python-dff8e5dc8d0758d1f9c5-3.12.0a7+-dff8e5d | bm-20230427-linux-x86_64-Fidget%2dSpinner-call_function_ex_inl-3.12.0a7+-dfd6b01 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 6.66 ms                                                                | 6.68 ms: 1.00x slower                                                            |
| python_startup         | 9.07 ms                                                                | 9.11 ms: 1.00x slower                                                            |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230427-linux-x86_64-python-dff8e5dc8d0758d1f9c5-3.12.0a7+-dff8e5d | bm-20230427-linux-x86_64-Fidget%2dSpinner-call_function_ex_inl-3.12.0a7+-dfd6b01 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 35.1 ms                                                                | 34.4 ms: 1.02x faster                                                            |
| mako            | 10.7 ms                                                                | 11.0 ms: 1.02x slower                                                            |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                                     |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark               | bm-20230427-linux-x86_64-python-dff8e5dc8d0758d1f9c5-3.12.0a7+-dff8e5d | bm-20230427-linux-x86_64-Fidget%2dSpinner-call_function_ex_inl-3.12.0a7+-dfd6b01 |
|-------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot            | 3.79 ms                                                                | 3.45 ms: 1.10x faster                                                            |
| gc_traversal            | 3.95 ms                                                                | 3.60 ms: 1.10x faster                                                            |
| logging_silent          | 103 ns                                                                 | 99.1 ns: 1.04x faster                                                            |
| meteor_contest          | 114 ms                                                                 | 110 ms: 1.04x faster                                                             |
| pickle                  | 10.7 us                                                                | 10.5 us: 1.03x faster                                                            |
| pickle_dict             | 32.3 us                                                                | 31.6 us: 1.02x faster                                                            |
| django_template         | 35.1 ms                                                                | 34.4 ms: 1.02x faster                                                            |
| richards                | 43.7 ms                                                                | 43.1 ms: 1.02x faster                                                            |
| sympy_expand            | 503 ms                                                                 | 496 ms: 1.01x faster                                                             |
| telco                   | 6.89 ms                                                                | 6.80 ms: 1.01x faster                                                            |
| go                      | 138 ms                                                                 | 136 ms: 1.01x faster                                                             |
| coverage                | 101 ms                                                                 | 100 ms: 1.01x faster                                                             |
| json                    | 4.98 ms                                                                | 4.92 ms: 1.01x faster                                                            |
| sqlite_synth            | 2.73 us                                                                | 2.70 us: 1.01x faster                                                            |
| scimark_sor             | 126 ms                                                                 | 125 ms: 1.01x faster                                                             |
| pickle_list             | 4.64 us                                                                | 4.61 us: 1.01x faster                                                            |
| dulwich_log             | 68.0 ms                                                                | 67.8 ms: 1.00x faster                                                            |
| sqlglot_normalize       | 111 ms                                                                 | 111 ms: 1.00x faster                                                             |
| sympy_integrate         | 21.8 ms                                                                | 21.9 ms: 1.00x slower                                                            |
| python_startup_no_site  | 6.66 ms                                                                | 6.68 ms: 1.00x slower                                                            |
| python_startup          | 9.07 ms                                                                | 9.11 ms: 1.00x slower                                                            |
| 2to3                    | 267 ms                                                                 | 269 ms: 1.00x slower                                                             |
| bench_thread_pool       | 830 us                                                                 | 835 us: 1.01x slower                                                             |
| pyflate                 | 450 ms                                                                 | 453 ms: 1.01x slower                                                             |
| coroutines              | 22.3 ms                                                                | 22.4 ms: 1.01x slower                                                            |
| float                   | 81.6 ms                                                                | 82.2 ms: 1.01x slower                                                            |
| logging_simple          | 6.26 us                                                                | 6.31 us: 1.01x slower                                                            |
| chameleon               | 6.90 ms                                                                | 6.96 ms: 1.01x slower                                                            |
| pickle_pure_python      | 316 us                                                                 | 319 us: 1.01x slower                                                             |
| deepcopy_memo           | 38.9 us                                                                | 39.3 us: 1.01x slower                                                            |
| deepcopy                | 366 us                                                                 | 369 us: 1.01x slower                                                             |
| scimark_monte_carlo     | 72.8 ms                                                                | 73.7 ms: 1.01x slower                                                            |
| nqueens                 | 81.3 ms                                                                | 82.4 ms: 1.01x slower                                                            |
| comprehensions          | 23.2 us                                                                | 23.5 us: 1.01x slower                                                            |
| logging_format          | 6.93 us                                                                | 7.03 us: 1.01x slower                                                            |
| scimark_fft             | 359 ms                                                                 | 364 ms: 1.01x slower                                                             |
| regex_dna               | 204 ms                                                                 | 207 ms: 1.01x slower                                                             |
| unpickle_pure_python    | 216 us                                                                 | 219 us: 1.02x slower                                                             |
| chaos                   | 69.0 ms                                                                | 70.3 ms: 1.02x slower                                                            |
| sympy_str               | 309 ms                                                                 | 316 ms: 1.02x slower                                                             |
| mako                    | 10.7 ms                                                                | 11.0 ms: 1.02x slower                                                            |
| spectral_norm           | 106 ms                                                                 | 109 ms: 1.02x slower                                                             |
| scimark_lu              | 110 ms                                                                 | 113 ms: 1.02x slower                                                             |
| pathlib                 | 17.8 ms                                                                | 18.3 ms: 1.02x slower                                                            |
| unpickle_list           | 4.86 us                                                                | 5.00 us: 1.03x slower                                                            |
| fannkuch                | 373 ms                                                                 | 384 ms: 1.03x slower                                                             |
| regex_v8                | 22.1 ms                                                                | 22.8 ms: 1.03x slower                                                            |
| deepcopy_reduce         | 3.18 us                                                                | 3.29 us: 1.03x slower                                                            |
| hexiom                  | 6.11 ms                                                                | 6.34 ms: 1.04x slower                                                            |
| crypto_pyaes            | 78.5 ms                                                                | 81.6 ms: 1.04x slower                                                            |
| pidigits                | 189 ms                                                                 | 197 ms: 1.05x slower                                                             |
| mdp                     | 2.59 sec                                                               | 2.71 sec: 1.05x slower                                                           |
| pycparser               | 1.13 sec                                                               | 1.19 sec: 1.06x slower                                                           |
| generators              | 30.7 ms                                                                | 32.4 ms: 1.06x slower                                                            |
| scimark_sparse_mat_mult | 4.62 ms                                                                | 4.90 ms: 1.06x slower                                                            |
| unpack_sequence         | 47.3 ns                                                                | 52.4 ns: 1.11x slower                                                            |
| Geometric mean          | (ref)                                                                  | 1.00x slower                                                                     |

Benchmark hidden because not significant (37): djangocms, sqlalchemy_imperative, json_dumps, genshi_xml, xml_etree_iterparse, html5lib, create_gc_cycles, sqlglot_parse, async_generators, json_loads, sqlglot_optimize, raytrace, sqlalchemy_declarative, genshi_text, unpickle, async_tree_none, deltablue, bench_mp_pool, xml_etree_generate, asyncio_tcp, xml_etree_parse, async_tree_cpu_io_mixed, docutils, regex_compile, thrift, xml_etree_process, pprint_safe_repr, tornado_http, sympy_sum, mypy2, sqlglot_transpile, pprint_pformat, nbody, pylint, dask, async_tree_io, async_tree_memoization
