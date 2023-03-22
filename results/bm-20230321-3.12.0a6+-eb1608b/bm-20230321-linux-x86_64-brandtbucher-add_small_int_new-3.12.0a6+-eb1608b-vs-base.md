
# Results vs. base

- fork: brandtbucher
- ref: add_small_int_new
- machine: linux-x86_64
- commit hash: eb1608b
- commit date: 2023-03-21
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230319-linux-x86_64-python-5e6661bce968173fa45b-3.12.0a6+-5e6661b | bm-20230321-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-eb1608b |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 249 ms                                                                 | 250 ms: 1.00x slower                                                      |
| chameleon      | 6.42 ms                                                                | 6.23 ms: 1.03x faster                                                     |
| docutils       | 2.52 sec                                                               | 2.53 sec: 1.00x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230319-linux-x86_64-python-5e6661bce968173fa45b-3.12.0a6+-5e6661b | bm-20230321-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-eb1608b |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 88.8 ms                                                                | 85.9 ms: 1.03x faster                                                     |
| pidigits       | 198 ms                                                                 | 193 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                              |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230319-linux-x86_64-python-5e6661bce968173fa45b-3.12.0a6+-5e6661b | bm-20230321-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-eb1608b |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.39 ms                                                                | 3.38 ms: 1.01x faster                                                     |
| regex_v8       | 21.5 ms                                                                | 21.6 ms: 1.00x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                              |

Benchmark hidden because not significant (2): regex_compile, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230319-linux-x86_64-python-5e6661bce968173fa45b-3.12.0a6+-5e6661b | bm-20230321-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-eb1608b |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_parse      | 149 ms                                                                 | 147 ms: 1.01x faster                                                      |
| xml_etree_process    | 55.9 ms                                                                | 55.3 ms: 1.01x faster                                                     |
| xml_etree_generate   | 80.5 ms                                                                | 79.8 ms: 1.01x faster                                                     |
| unpickle_pure_python | 198 us                                                                 | 197 us: 1.01x faster                                                      |
| json_dumps           | 9.44 ms                                                                | 9.54 ms: 1.01x slower                                                     |
| pickle_pure_python   | 281 us                                                                 | 284 us: 1.01x slower                                                      |
| pickle_dict          | 31.2 us                                                                | 31.6 us: 1.01x slower                                                     |
| pickle               | 10.1 us                                                                | 10.5 us: 1.03x slower                                                     |
| pickle_list          | 4.13 us                                                                | 4.32 us: 1.05x slower                                                     |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (4): json_loads, xml_etree_iterparse, unpickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230319-linux-x86_64-python-5e6661bce968173fa45b-3.12.0a6+-5e6661b | bm-20230321-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-eb1608b |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.55 ms                                                                | 6.51 ms: 1.01x faster                                                     |
| python_startup         | 8.95 ms                                                                | 8.90 ms: 1.01x faster                                                     |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230319-linux-x86_64-python-5e6661bce968173fa45b-3.12.0a6+-5e6661b | bm-20230321-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-eb1608b |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 33.5 ms                                                                | 32.5 ms: 1.03x faster                                                     |
| genshi_xml      | 47.5 ms                                                                | 48.3 ms: 1.02x slower                                                     |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                              |

Benchmark hidden because not significant (2): mako, genshi_text

All benchmarks:
===============

| Benchmark               | bm-20230319-linux-x86_64-python-5e6661bce968173fa45b-3.12.0a6+-5e6661b | bm-20230321-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-eb1608b |
|-------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mdp                     | 2.55 sec                                                               | 2.43 sec: 1.05x faster                                                    |
| go                      | 135 ms                                                                 | 130 ms: 1.04x faster                                                      |
| nbody                   | 88.8 ms                                                                | 85.9 ms: 1.03x faster                                                     |
| unpack_sequence         | 44.9 ns                                                                | 43.5 ns: 1.03x faster                                                     |
| django_template         | 33.5 ms                                                                | 32.5 ms: 1.03x faster                                                     |
| richards                | 43.0 ms                                                                | 41.7 ms: 1.03x faster                                                     |
| chameleon               | 6.42 ms                                                                | 6.23 ms: 1.03x faster                                                     |
| logging_silent          | 95.4 ns                                                                | 92.8 ns: 1.03x faster                                                     |
| scimark_monte_carlo     | 67.0 ms                                                                | 65.2 ms: 1.03x faster                                                     |
| pidigits                | 198 ms                                                                 | 193 ms: 1.03x faster                                                      |
| hexiom                  | 6.19 ms                                                                | 6.04 ms: 1.02x faster                                                     |
| async_tree_memoization  | 640 ms                                                                 | 628 ms: 1.02x faster                                                      |
| comprehensions          | 23.7 us                                                                | 23.3 us: 1.02x faster                                                     |
| thrift                  | 787 us                                                                 | 773 us: 1.02x faster                                                      |
| logging_format          | 6.31 us                                                                | 6.20 us: 1.02x faster                                                     |
| telco                   | 6.53 ms                                                                | 6.42 ms: 1.02x faster                                                     |
| logging_simple          | 5.71 us                                                                | 5.64 us: 1.01x faster                                                     |
| pathlib                 | 17.8 ms                                                                | 17.6 ms: 1.01x faster                                                     |
| xml_etree_parse         | 149 ms                                                                 | 147 ms: 1.01x faster                                                      |
| json                    | 4.66 ms                                                                | 4.61 ms: 1.01x faster                                                     |
| xml_etree_process       | 55.9 ms                                                                | 55.3 ms: 1.01x faster                                                     |
| pprint_pformat          | 1.41 sec                                                               | 1.40 sec: 1.01x faster                                                    |
| coverage                | 94.8 ms                                                                | 94.0 ms: 1.01x faster                                                     |
| xml_etree_generate      | 80.5 ms                                                                | 79.8 ms: 1.01x faster                                                     |
| chaos                   | 66.3 ms                                                                | 65.7 ms: 1.01x faster                                                     |
| deepcopy                | 325 us                                                                 | 323 us: 1.01x faster                                                      |
| async_tree_io           | 1.29 sec                                                               | 1.28 sec: 1.01x faster                                                    |
| deepcopy_memo           | 34.3 us                                                                | 34.1 us: 1.01x faster                                                     |
| python_startup_no_site  | 6.55 ms                                                                | 6.51 ms: 1.01x faster                                                     |
| python_startup          | 8.95 ms                                                                | 8.90 ms: 1.01x faster                                                     |
| unpickle_pure_python    | 198 us                                                                 | 197 us: 1.01x faster                                                      |
| regex_effbot            | 3.39 ms                                                                | 3.38 ms: 1.01x faster                                                     |
| create_gc_cycles        | 1.50 ms                                                                | 1.49 ms: 1.00x faster                                                     |
| deltablue               | 3.16 ms                                                                | 3.15 ms: 1.00x faster                                                     |
| gc_traversal            | 3.98 ms                                                                | 3.98 ms: 1.00x faster                                                     |
| asyncio_tcp             | 507 ms                                                                 | 508 ms: 1.00x slower                                                      |
| dulwich_log             | 63.4 ms                                                                | 63.6 ms: 1.00x slower                                                     |
| sqlglot_optimize        | 50.8 ms                                                                | 51.0 ms: 1.00x slower                                                     |
| docutils                | 2.52 sec                                                               | 2.53 sec: 1.00x slower                                                    |
| regex_v8                | 21.5 ms                                                                | 21.6 ms: 1.00x slower                                                     |
| aiohttp                 | 1.00 ms                                                                | 1.01 ms: 1.00x slower                                                     |
| 2to3                    | 249 ms                                                                 | 250 ms: 1.00x slower                                                      |
| sympy_integrate         | 20.3 ms                                                                | 20.4 ms: 1.00x slower                                                     |
| sqlglot_transpile       | 1.71 ms                                                                | 1.72 ms: 1.01x slower                                                     |
| crypto_pyaes            | 74.2 ms                                                                | 74.7 ms: 1.01x slower                                                     |
| meteor_contest          | 103 ms                                                                 | 104 ms: 1.01x slower                                                      |
| sqlglot_parse           | 1.42 ms                                                                | 1.43 ms: 1.01x slower                                                     |
| gunicorn                | 1.08 ms                                                                | 1.09 ms: 1.01x slower                                                     |
| json_dumps              | 9.44 ms                                                                | 9.54 ms: 1.01x slower                                                     |
| pickle_pure_python      | 281 us                                                                 | 284 us: 1.01x slower                                                      |
| generators              | 29.4 ms                                                                | 29.8 ms: 1.01x slower                                                     |
| pyflate                 | 405 ms                                                                 | 410 ms: 1.01x slower                                                      |
| async_generators        | 411 ms                                                                 | 416 ms: 1.01x slower                                                      |
| pickle_dict             | 31.2 us                                                                | 31.6 us: 1.01x slower                                                     |
| sympy_expand            | 459 ms                                                                 | 465 ms: 1.01x slower                                                      |
| genshi_xml              | 47.5 ms                                                                | 48.3 ms: 1.02x slower                                                     |
| scimark_fft             | 302 ms                                                                 | 308 ms: 1.02x slower                                                      |
| coroutines              | 21.9 ms                                                                | 22.3 ms: 1.02x slower                                                     |
| scimark_sparse_mat_mult | 4.07 ms                                                                | 4.18 ms: 1.02x slower                                                     |
| spectral_norm           | 92.7 ms                                                                | 95.6 ms: 1.03x slower                                                     |
| pickle                  | 10.1 us                                                                | 10.5 us: 1.03x slower                                                     |
| pickle_list             | 4.13 us                                                                | 4.32 us: 1.05x slower                                                     |
| Geometric mean          | (ref)                                                                  | 1.00x faster                                                              |

Benchmark hidden because not significant (32): html5lib, async_tree_none, regex_compile, json_loads, pprint_safe_repr, async_tree_cpu_io_mixed, xml_etree_iterparse, raytrace, sqlalchemy_declarative, sqlite_synth, fannkuch, float, sqlglot_normalize, bench_mp_pool, mypy2, sympy_sum, djangocms, tornado_http, dask, pycparser, regex_dna, deepcopy_reduce, mako, nqueens, bench_thread_pool, sympy_str, sqlalchemy_imperative, unpickle_list, unpickle, scimark_sor, genshi_text, scimark_lu
