
# Results vs. base

- fork: brandtbucher
- ref: add_small_int_new
- machine: linux-x86_64
- commit hash: 114cba6
- commit date: 2023-03-20
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230319-linux-x86_64-python-5e6661bce968173fa45b-3.12.0a6+-5e6661b | bm-20230320-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-114cba6 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 249 ms                                                                 | 250 ms: 1.00x slower                                                      |
| chameleon      | 6.42 ms                                                                | 6.32 ms: 1.02x faster                                                     |
| docutils       | 2.52 sec                                                               | 2.55 sec: 1.01x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                              |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230319-linux-x86_64-python-5e6661bce968173fa45b-3.12.0a6+-5e6661b | bm-20230320-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-114cba6 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 198 ms                                                                 | 193 ms: 1.02x faster                                                      |
| nbody          | 88.8 ms                                                                | 87.7 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230319-linux-x86_64-python-5e6661bce968173fa45b-3.12.0a6+-5e6661b | bm-20230320-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-114cba6 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 21.5 ms                                                                | 21.4 ms: 1.01x faster                                                     |
| regex_compile  | 134 ms                                                                 | 133 ms: 1.00x faster                                                      |
| regex_dna      | 205 ms                                                                 | 210 ms: 1.02x slower                                                      |
| regex_effbot   | 3.39 ms                                                                | 3.50 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20230319-linux-x86_64-python-5e6661bce968173fa45b-3.12.0a6+-5e6661b | bm-20230320-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-114cba6 |
|--------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_process  | 55.9 ms                                                                | 55.3 ms: 1.01x faster                                                     |
| unpickle           | 13.5 us                                                                | 13.4 us: 1.01x faster                                                     |
| pickle             | 10.1 us                                                                | 10.2 us: 1.01x slower                                                     |
| pickle_dict        | 31.2 us                                                                | 31.4 us: 1.01x slower                                                     |
| pickle_pure_python | 281 us                                                                 | 283 us: 1.01x slower                                                      |
| json_dumps         | 9.44 ms                                                                | 9.53 ms: 1.01x slower                                                     |
| pickle_list        | 4.13 us                                                                | 4.20 us: 1.02x slower                                                     |
| unpickle_list      | 4.95 us                                                                | 5.12 us: 1.03x slower                                                     |
| Geometric mean     | (ref)                                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (5): xml_etree_parse, json_loads, unpickle_pure_python, xml_etree_iterparse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230319-linux-x86_64-python-5e6661bce968173fa45b-3.12.0a6+-5e6661b | bm-20230320-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-114cba6 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 8.95 ms                                                                | 8.89 ms: 1.01x faster                                                     |
| python_startup_no_site | 6.55 ms                                                                | 6.51 ms: 1.01x faster                                                     |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230319-linux-x86_64-python-5e6661bce968173fa45b-3.12.0a6+-5e6661b | bm-20230320-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-114cba6 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 33.5 ms                                                                | 32.5 ms: 1.03x faster                                                     |
| genshi_text     | 21.1 ms                                                                | 20.9 ms: 1.01x faster                                                     |
| mako            | 10.0 ms                                                                | 10.1 ms: 1.00x slower                                                     |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20230319-linux-x86_64-python-5e6661bce968173fa45b-3.12.0a6+-5e6661b | bm-20230320-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-114cba6 |
|-------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpack_sequence         | 44.9 ns                                                                | 43.3 ns: 1.03x faster                                                     |
| django_template         | 33.5 ms                                                                | 32.5 ms: 1.03x faster                                                     |
| richards                | 43.0 ms                                                                | 41.8 ms: 1.03x faster                                                     |
| pidigits                | 198 ms                                                                 | 193 ms: 1.02x faster                                                      |
| go                      | 135 ms                                                                 | 132 ms: 1.02x faster                                                      |
| pprint_pformat          | 1.41 sec                                                               | 1.39 sec: 1.02x faster                                                    |
| hexiom                  | 6.19 ms                                                                | 6.09 ms: 1.02x faster                                                     |
| chameleon               | 6.42 ms                                                                | 6.32 ms: 1.02x faster                                                     |
| mdp                     | 2.55 sec                                                               | 2.51 sec: 1.01x faster                                                    |
| nbody                   | 88.8 ms                                                                | 87.7 ms: 1.01x faster                                                     |
| thrift                  | 787 us                                                                 | 777 us: 1.01x faster                                                      |
| chaos                   | 66.3 ms                                                                | 65.4 ms: 1.01x faster                                                     |
| gc_traversal            | 3.98 ms                                                                | 3.93 ms: 1.01x faster                                                     |
| xml_etree_process       | 55.9 ms                                                                | 55.3 ms: 1.01x faster                                                     |
| deepcopy                | 325 us                                                                 | 322 us: 1.01x faster                                                      |
| genshi_text             | 21.1 ms                                                                | 20.9 ms: 1.01x faster                                                     |
| deepcopy_memo           | 34.3 us                                                                | 33.9 us: 1.01x faster                                                     |
| raytrace                | 280 ms                                                                 | 277 ms: 1.01x faster                                                      |
| pprint_safe_repr        | 692 ms                                                                 | 686 ms: 1.01x faster                                                      |
| json                    | 4.66 ms                                                                | 4.63 ms: 1.01x faster                                                     |
| sqlite_synth            | 2.63 us                                                                | 2.61 us: 1.01x faster                                                     |
| dulwich_log             | 63.4 ms                                                                | 63.0 ms: 1.01x faster                                                     |
| python_startup          | 8.95 ms                                                                | 8.89 ms: 1.01x faster                                                     |
| python_startup_no_site  | 6.55 ms                                                                | 6.51 ms: 1.01x faster                                                     |
| regex_v8                | 21.5 ms                                                                | 21.4 ms: 1.01x faster                                                     |
| unpickle                | 13.5 us                                                                | 13.4 us: 1.01x faster                                                     |
| meteor_contest          | 103 ms                                                                 | 102 ms: 1.00x faster                                                      |
| comprehensions          | 23.7 us                                                                | 23.6 us: 1.00x faster                                                     |
| deltablue               | 3.16 ms                                                                | 3.15 ms: 1.00x faster                                                     |
| create_gc_cycles        | 1.50 ms                                                                | 1.49 ms: 1.00x faster                                                     |
| regex_compile           | 134 ms                                                                 | 133 ms: 1.00x faster                                                      |
| 2to3                    | 249 ms                                                                 | 250 ms: 1.00x slower                                                      |
| sympy_integrate         | 20.3 ms                                                                | 20.4 ms: 1.00x slower                                                     |
| mako                    | 10.0 ms                                                                | 10.1 ms: 1.00x slower                                                     |
| sympy_expand            | 459 ms                                                                 | 461 ms: 1.01x slower                                                      |
| scimark_sor             | 106 ms                                                                 | 106 ms: 1.01x slower                                                      |
| sqlglot_optimize        | 50.8 ms                                                                | 51.1 ms: 1.01x slower                                                     |
| pycparser               | 1.15 sec                                                               | 1.16 sec: 1.01x slower                                                    |
| pickle                  | 10.1 us                                                                | 10.2 us: 1.01x slower                                                     |
| pickle_dict             | 31.2 us                                                                | 31.4 us: 1.01x slower                                                     |
| gunicorn                | 1.08 ms                                                                | 1.09 ms: 1.01x slower                                                     |
| docutils                | 2.52 sec                                                               | 2.55 sec: 1.01x slower                                                    |
| sqlglot_parse           | 1.42 ms                                                                | 1.43 ms: 1.01x slower                                                     |
| pickle_pure_python      | 281 us                                                                 | 283 us: 1.01x slower                                                      |
| json_dumps              | 9.44 ms                                                                | 9.53 ms: 1.01x slower                                                     |
| crypto_pyaes            | 74.2 ms                                                                | 75.0 ms: 1.01x slower                                                     |
| scimark_fft             | 302 ms                                                                 | 306 ms: 1.01x slower                                                      |
| sqlglot_normalize       | 104 ms                                                                 | 105 ms: 1.01x slower                                                      |
| pyflate                 | 405 ms                                                                 | 410 ms: 1.01x slower                                                      |
| pickle_list             | 4.13 us                                                                | 4.20 us: 1.02x slower                                                     |
| regex_dna               | 205 ms                                                                 | 210 ms: 1.02x slower                                                      |
| coroutines              | 21.9 ms                                                                | 22.5 ms: 1.03x slower                                                     |
| scimark_sparse_mat_mult | 4.07 ms                                                                | 4.19 ms: 1.03x slower                                                     |
| regex_effbot            | 3.39 ms                                                                | 3.50 ms: 1.03x slower                                                     |
| unpickle_list           | 4.95 us                                                                | 5.12 us: 1.03x slower                                                     |
| pathlib                 | 17.8 ms                                                                | 18.5 ms: 1.04x slower                                                     |
| generators              | 29.4 ms                                                                | 30.6 ms: 1.04x slower                                                     |
| spectral_norm           | 92.7 ms                                                                | 98.1 ms: 1.06x slower                                                     |
| Geometric mean          | (ref)                                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (36): sqlalchemy_imperative, html5lib, fannkuch, float, telco, scimark_monte_carlo, genshi_xml, xml_etree_parse, nqueens, djangocms, async_tree_none, async_tree_io, mypy2, asyncio_tcp, deepcopy_reduce, bench_mp_pool, sympy_str, sympy_sum, async_tree_memoization, tornado_http, sqlalchemy_declarative, json_loads, bench_thread_pool, unpickle_pure_python, dask, xml_etree_iterparse, aiohttp, coverage, logging_simple, async_tree_cpu_io_mixed, xml_etree_generate, sqlglot_transpile, scimark_lu, logging_format, async_generators, logging_silent
