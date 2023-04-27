
# Results vs. base

- fork: brandtbucher
- ref: immortal_interpreter
- machine: linux-x86_64
- commit hash: fd95518
- commit date: 2023-04-26
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230426-linux-x86_64-python-dc3f97549a8fe4f7fea8-3.12.0a7+-dc3f975 | bm-20230426-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-fd95518 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 268 ms                                                                 | 269 ms: 1.01x slower                                                         |
| chameleon      | 6.94 ms                                                                | 7.01 ms: 1.01x slower                                                        |
| docutils       | 2.70 sec                                                               | 2.72 sec: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230426-linux-x86_64-python-dc3f97549a8fe4f7fea8-3.12.0a7+-dc3f975 | bm-20230426-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-fd95518 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 198 ms                                                                 | 189 ms: 1.05x faster                                                         |
| nbody          | 88.2 ms                                                                | 88.5 ms: 1.00x slower                                                        |
| float          | 80.0 ms                                                                | 81.1 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230426-linux-x86_64-python-dc3f97549a8fe4f7fea8-3.12.0a7+-dc3f975 | bm-20230426-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-fd95518 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.75 ms                                                                | 3.49 ms: 1.08x faster                                                        |
| regex_compile  | 145 ms                                                                 | 143 ms: 1.01x faster                                                         |
| regex_v8       | 22.2 ms                                                                | 22.4 ms: 1.01x slower                                                        |
| regex_dna      | 204 ms                                                                 | 207 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230426-linux-x86_64-python-dc3f97549a8fe4f7fea8-3.12.0a7+-dc3f975 | bm-20230426-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-fd95518 |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle               | 10.7 us                                                                | 10.4 us: 1.03x faster                                                        |
| pickle_list          | 4.62 us                                                                | 4.52 us: 1.02x faster                                                        |
| pickle_dict          | 31.6 us                                                                | 30.9 us: 1.02x faster                                                        |
| unpickle             | 15.0 us                                                                | 14.7 us: 1.02x faster                                                        |
| json_dumps           | 10.0 ms                                                                | 9.92 ms: 1.01x faster                                                        |
| unpickle_pure_python | 218 us                                                                 | 216 us: 1.01x faster                                                         |
| json_loads           | 25.8 us                                                                | 25.6 us: 1.01x faster                                                        |
| pickle_pure_python   | 313 us                                                                 | 315 us: 1.00x slower                                                         |
| xml_etree_generate   | 83.9 ms                                                                | 84.6 ms: 1.01x slower                                                        |
| xml_etree_parse      | 152 ms                                                                 | 154 ms: 1.02x slower                                                         |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (3): xml_etree_iterparse, unpickle_list, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230426-linux-x86_64-python-dc3f97549a8fe4f7fea8-3.12.0a7+-dc3f975 | bm-20230426-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-fd95518 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 9.03 ms                                                                | 9.13 ms: 1.01x slower                                                        |
| python_startup_no_site | 6.62 ms                                                                | 6.69 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20230426-linux-x86_64-python-dc3f97549a8fe4f7fea8-3.12.0a7+-dc3f975 | bm-20230426-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-fd95518 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako           | 10.9 ms                                                                | 10.8 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (3): django_template, genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark               | bm-20230426-linux-x86_64-python-dc3f97549a8fe4f7fea8-3.12.0a7+-dc3f975 | bm-20230426-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-fd95518 |
|-------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot            | 3.75 ms                                                                | 3.49 ms: 1.08x faster                                                        |
| nqueens                 | 84.5 ms                                                                | 79.8 ms: 1.06x faster                                                        |
| pidigits                | 198 ms                                                                 | 189 ms: 1.05x faster                                                         |
| generators              | 32.4 ms                                                                | 31.2 ms: 1.04x faster                                                        |
| scimark_fft             | 364 ms                                                                 | 352 ms: 1.04x faster                                                         |
| spectral_norm           | 108 ms                                                                 | 105 ms: 1.04x faster                                                         |
| pickle                  | 10.7 us                                                                | 10.4 us: 1.03x faster                                                        |
| scimark_sparse_mat_mult | 5.00 ms                                                                | 4.85 ms: 1.03x faster                                                        |
| fannkuch                | 385 ms                                                                 | 374 ms: 1.03x faster                                                         |
| meteor_contest          | 116 ms                                                                 | 112 ms: 1.03x faster                                                         |
| scimark_sor             | 126 ms                                                                 | 122 ms: 1.03x faster                                                         |
| async_generators        | 449 ms                                                                 | 437 ms: 1.03x faster                                                         |
| scimark_monte_carlo     | 73.1 ms                                                                | 71.3 ms: 1.02x faster                                                        |
| hexiom                  | 6.27 ms                                                                | 6.13 ms: 1.02x faster                                                        |
| pickle_list             | 4.62 us                                                                | 4.52 us: 1.02x faster                                                        |
| pickle_dict             | 31.6 us                                                                | 30.9 us: 1.02x faster                                                        |
| scimark_lu              | 112 ms                                                                 | 110 ms: 1.02x faster                                                         |
| unpickle                | 15.0 us                                                                | 14.7 us: 1.02x faster                                                        |
| regex_compile           | 145 ms                                                                 | 143 ms: 1.01x faster                                                         |
| deepcopy_memo           | 39.0 us                                                                | 38.5 us: 1.01x faster                                                        |
| pyflate                 | 451 ms                                                                 | 446 ms: 1.01x faster                                                         |
| json                    | 4.96 ms                                                                | 4.91 ms: 1.01x faster                                                        |
| deepcopy_reduce         | 3.22 us                                                                | 3.19 us: 1.01x faster                                                        |
| pprint_pformat          | 1.48 sec                                                               | 1.47 sec: 1.01x faster                                                       |
| json_dumps              | 10.0 ms                                                                | 9.92 ms: 1.01x faster                                                        |
| logging_silent          | 99.9 ns                                                                | 99.0 ns: 1.01x faster                                                        |
| unpickle_pure_python    | 218 us                                                                 | 216 us: 1.01x faster                                                         |
| deepcopy                | 368 us                                                                 | 366 us: 1.01x faster                                                         |
| json_loads              | 25.8 us                                                                | 25.6 us: 1.01x faster                                                        |
| mypy2                   | 351 ms                                                                 | 349 ms: 1.01x faster                                                         |
| mako                    | 10.9 ms                                                                | 10.8 ms: 1.01x faster                                                        |
| thrift                  | 805 us                                                                 | 800 us: 1.01x faster                                                         |
| comprehensions          | 23.5 us                                                                | 23.4 us: 1.00x faster                                                        |
| asyncio_tcp             | 507 ms                                                                 | 505 ms: 1.00x faster                                                         |
| nbody                   | 88.2 ms                                                                | 88.5 ms: 1.00x slower                                                        |
| pickle_pure_python      | 313 us                                                                 | 315 us: 1.00x slower                                                         |
| 2to3                    | 268 ms                                                                 | 269 ms: 1.01x slower                                                         |
| mdp                     | 2.57 sec                                                               | 2.59 sec: 1.01x slower                                                       |
| docutils                | 2.70 sec                                                               | 2.72 sec: 1.01x slower                                                       |
| xml_etree_generate      | 83.9 ms                                                                | 84.6 ms: 1.01x slower                                                        |
| sympy_sum               | 182 ms                                                                 | 183 ms: 1.01x slower                                                         |
| logging_format          | 6.90 us                                                                | 6.96 us: 1.01x slower                                                        |
| chameleon               | 6.94 ms                                                                | 7.01 ms: 1.01x slower                                                        |
| python_startup          | 9.03 ms                                                                | 9.13 ms: 1.01x slower                                                        |
| python_startup_no_site  | 6.62 ms                                                                | 6.69 ms: 1.01x slower                                                        |
| crypto_pyaes            | 79.5 ms                                                                | 80.5 ms: 1.01x slower                                                        |
| regex_v8                | 22.2 ms                                                                | 22.4 ms: 1.01x slower                                                        |
| pycparser               | 1.14 sec                                                               | 1.15 sec: 1.01x slower                                                       |
| float                   | 80.0 ms                                                                | 81.1 ms: 1.01x slower                                                        |
| coverage                | 99.0 ms                                                                | 100 ms: 1.01x slower                                                         |
| regex_dna               | 204 ms                                                                 | 207 ms: 1.02x slower                                                         |
| xml_etree_parse         | 152 ms                                                                 | 154 ms: 1.02x slower                                                         |
| telco                   | 6.78 ms                                                                | 6.90 ms: 1.02x slower                                                        |
| sqlalchemy_imperative   | 19.1 ms                                                                | 19.5 ms: 1.02x slower                                                        |
| coroutines              | 22.5 ms                                                                | 23.0 ms: 1.02x slower                                                        |
| go                      | 135 ms                                                                 | 139 ms: 1.02x slower                                                         |
| create_gc_cycles        | 1.46 ms                                                                | 1.51 ms: 1.03x slower                                                        |
| gc_traversal            | 3.76 ms                                                                | 3.99 ms: 1.06x slower                                                        |
| unpack_sequence         | 46.6 ns                                                                | 54.1 ns: 1.16x slower                                                        |
| Geometric mean          | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (34): djangocms, async_tree_memoization, raytrace, sympy_str, sympy_expand, sqlglot_parse, pprint_safe_repr, logging_simple, sqlglot_transpile, dask, sqlalchemy_declarative, xml_etree_iterparse, bench_thread_pool, dulwich_log, async_tree_io, chaos, deltablue, bench_mp_pool, pylint, pathlib, richards, sqlglot_optimize, django_template, sympy_integrate, sqlglot_normalize, genshi_xml, async_tree_none, unpickle_list, xml_etree_process, sqlite_synth, async_tree_cpu_io_mixed, genshi_text, html5lib, tornado_http
