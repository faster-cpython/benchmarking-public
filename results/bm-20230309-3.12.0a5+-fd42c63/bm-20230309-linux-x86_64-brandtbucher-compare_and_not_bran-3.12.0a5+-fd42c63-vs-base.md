
# Results vs. base

- fork: brandtbucher
- ref: compare_and_not_bran
- machine: linux-x86_64
- commit hash: fd42c63
- commit date: 2023-03-09
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230306-linux-x86_64-python-c84e6f32df989908685e-3.12.0a5+-c84e6f3 | bm-20230309-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-fd42c63 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 252 ms                                                                 | 253 ms: 1.00x slower                                                         |
| chameleon      | 6.37 ms                                                                | 6.41 ms: 1.01x slower                                                        |
| docutils       | 2.57 sec                                                               | 2.58 sec: 1.00x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230306-linux-x86_64-python-c84e6f32df989908685e-3.12.0a5+-c84e6f3 | bm-20230309-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-fd42c63 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 75.1 ms                                                                | 74.7 ms: 1.01x faster                                                        |
| pidigits       | 189 ms                                                                 | 193 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230306-linux-x86_64-python-c84e6f32df989908685e-3.12.0a5+-c84e6f3 | bm-20230309-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-fd42c63 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 22.1 ms                                                                | 21.9 ms: 1.01x faster                                                        |
| regex_effbot   | 3.57 ms                                                                | 3.53 ms: 1.01x faster                                                        |
| regex_dna      | 201 ms                                                                 | 199 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230306-linux-x86_64-python-c84e6f32df989908685e-3.12.0a5+-c84e6f3 | bm-20230309-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-fd42c63 |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_list          | 4.29 us                                                                | 4.07 us: 1.05x faster                                                        |
| pickle_dict          | 32.1 us                                                                | 30.7 us: 1.04x faster                                                        |
| json_dumps           | 9.50 ms                                                                | 9.42 ms: 1.01x faster                                                        |
| pickle_pure_python   | 288 us                                                                 | 290 us: 1.01x slower                                                         |
| json_loads           | 23.6 us                                                                | 23.9 us: 1.01x slower                                                        |
| unpickle_pure_python | 203 us                                                                 | 207 us: 1.02x slower                                                         |
| xml_etree_iterparse  | 101 ms                                                                 | 104 ms: 1.03x slower                                                         |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (6): pickle, xml_etree_parse, xml_etree_process, xml_etree_generate, unpickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230306-linux-x86_64-python-c84e6f32df989908685e-3.12.0a5+-c84e6f3 | bm-20230309-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-fd42c63 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 9.04 ms                                                                | 9.02 ms: 1.00x faster                                                        |
| python_startup_no_site | 6.55 ms                                                                | 6.54 ms: 1.00x faster                                                        |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230306-linux-x86_64-python-c84e6f32df989908685e-3.12.0a5+-c84e6f3 | bm-20230309-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-fd42c63 |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 34.1 ms                                                                | 33.5 ms: 1.02x faster                                                        |
| genshi_xml      | 47.6 ms                                                                | 47.9 ms: 1.01x slower                                                        |
| genshi_text     | 21.3 ms                                                                | 21.7 ms: 1.02x slower                                                        |
| mako            | 9.96 ms                                                                | 10.2 ms: 1.03x slower                                                        |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20230306-linux-x86_64-python-c84e6f32df989908685e-3.12.0a5+-c84e6f3 | bm-20230309-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-fd42c63 |
|-------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_list             | 4.29 us                                                                | 4.07 us: 1.05x faster                                                        |
| pickle_dict             | 32.1 us                                                                | 30.7 us: 1.04x faster                                                        |
| thrift                  | 789 us                                                                 | 765 us: 1.03x faster                                                         |
| go                      | 143 ms                                                                 | 140 ms: 1.02x faster                                                         |
| chaos                   | 68.0 ms                                                                | 66.6 ms: 1.02x faster                                                        |
| hexiom                  | 6.23 ms                                                                | 6.10 ms: 1.02x faster                                                        |
| raytrace                | 293 ms                                                                 | 287 ms: 1.02x faster                                                         |
| logging_format          | 6.52 us                                                                | 6.41 us: 1.02x faster                                                        |
| django_template         | 34.1 ms                                                                | 33.5 ms: 1.02x faster                                                        |
| logging_simple          | 5.96 us                                                                | 5.87 us: 1.02x faster                                                        |
| create_gc_cycles        | 1.50 ms                                                                | 1.48 ms: 1.01x faster                                                        |
| regex_v8                | 22.1 ms                                                                | 21.9 ms: 1.01x faster                                                        |
| pyflate                 | 417 ms                                                                 | 412 ms: 1.01x faster                                                         |
| regex_effbot            | 3.57 ms                                                                | 3.53 ms: 1.01x faster                                                        |
| comprehensions          | 24.5 us                                                                | 24.2 us: 1.01x faster                                                        |
| richards                | 44.3 ms                                                                | 43.8 ms: 1.01x faster                                                        |
| json_dumps              | 9.50 ms                                                                | 9.42 ms: 1.01x faster                                                        |
| regex_dna               | 201 ms                                                                 | 199 ms: 1.01x faster                                                         |
| float                   | 75.1 ms                                                                | 74.7 ms: 1.01x faster                                                        |
| mypy2                   | 334 ms                                                                 | 332 ms: 1.01x faster                                                         |
| asyncio_tcp             | 506 ms                                                                 | 504 ms: 1.01x faster                                                         |
| sympy_sum               | 168 ms                                                                 | 167 ms: 1.00x faster                                                         |
| crypto_pyaes            | 73.4 ms                                                                | 73.1 ms: 1.00x faster                                                        |
| dulwich_log             | 63.7 ms                                                                | 63.5 ms: 1.00x faster                                                        |
| python_startup          | 9.04 ms                                                                | 9.02 ms: 1.00x faster                                                        |
| python_startup_no_site  | 6.55 ms                                                                | 6.54 ms: 1.00x faster                                                        |
| 2to3                    | 252 ms                                                                 | 253 ms: 1.00x slower                                                         |
| docutils                | 2.57 sec                                                               | 2.58 sec: 1.00x slower                                                       |
| genshi_xml              | 47.6 ms                                                                | 47.9 ms: 1.01x slower                                                        |
| chameleon               | 6.37 ms                                                                | 6.41 ms: 1.01x slower                                                        |
| pickle_pure_python      | 288 us                                                                 | 290 us: 1.01x slower                                                         |
| deltablue               | 3.25 ms                                                                | 3.28 ms: 1.01x slower                                                        |
| deepcopy_memo           | 34.6 us                                                                | 35.0 us: 1.01x slower                                                        |
| pprint_pformat          | 1.39 sec                                                               | 1.41 sec: 1.01x slower                                                       |
| pprint_safe_repr        | 678 ms                                                                 | 686 ms: 1.01x slower                                                         |
| pathlib                 | 17.7 ms                                                                | 17.9 ms: 1.01x slower                                                        |
| json_loads              | 23.6 us                                                                | 23.9 us: 1.01x slower                                                        |
| sqlalchemy_declarative  | 138 ms                                                                 | 140 ms: 1.01x slower                                                         |
| genshi_text             | 21.3 ms                                                                | 21.7 ms: 1.02x slower                                                        |
| unpickle_pure_python    | 203 us                                                                 | 207 us: 1.02x slower                                                         |
| spectral_norm           | 94.0 ms                                                                | 95.6 ms: 1.02x slower                                                        |
| pidigits                | 189 ms                                                                 | 193 ms: 1.02x slower                                                         |
| deepcopy                | 330 us                                                                 | 337 us: 1.02x slower                                                         |
| unpack_sequence         | 41.9 ns                                                                | 42.7 ns: 1.02x slower                                                        |
| generators              | 30.2 ms                                                                | 30.9 ms: 1.02x slower                                                        |
| scimark_sor             | 107 ms                                                                 | 110 ms: 1.02x slower                                                         |
| coverage                | 94.1 ms                                                                | 96.5 ms: 1.03x slower                                                        |
| mako                    | 9.96 ms                                                                | 10.2 ms: 1.03x slower                                                        |
| xml_etree_iterparse     | 101 ms                                                                 | 104 ms: 1.03x slower                                                         |
| mdp                     | 2.52 sec                                                               | 2.61 sec: 1.03x slower                                                       |
| scimark_fft             | 315 ms                                                                 | 326 ms: 1.04x slower                                                         |
| logging_silent          | 93.8 ns                                                                | 97.2 ns: 1.04x slower                                                        |
| scimark_sparse_mat_mult | 4.45 ms                                                                | 4.62 ms: 1.04x slower                                                        |
| fannkuch                | 357 ms                                                                 | 375 ms: 1.05x slower                                                         |
| gc_traversal            | 3.94 ms                                                                | 4.19 ms: 1.06x slower                                                        |
| Geometric mean          | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (39): async_tree_memoization, pickle, scimark_monte_carlo, tornado_http, xml_etree_parse, xml_etree_process, nqueens, sqlite_synth, sympy_expand, async_tree_io, gunicorn, meteor_contest, aiohttp, telco, regex_compile, sqlglot_transpile, async_generators, sympy_str, sqlglot_parse, sqlalchemy_imperative, pycparser, bench_mp_pool, async_tree_none, bench_thread_pool, nbody, sympy_integrate, sqlglot_optimize, sqlglot_normalize, xml_etree_generate, unpickle_list, deepcopy_reduce, dask, html5lib, json, async_tree_cpu_io_mixed, djangocms, scimark_lu, unpickle, coroutines
