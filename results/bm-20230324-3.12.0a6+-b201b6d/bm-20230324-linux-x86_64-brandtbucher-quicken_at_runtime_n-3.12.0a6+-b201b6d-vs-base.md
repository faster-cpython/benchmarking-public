
# Results vs. base

- fork: brandtbucher
- ref: quicken_at_runtime_n
- machine: linux-x86_64
- commit hash: b201b6d
- commit date: 2023-03-24
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230324-linux-x86_64-python-f2e5a6ee628502d307a9-3.12.0a6+-f2e5a6e | bm-20230324-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a6+-b201b6d |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                                 | 253 ms: 1.00x faster                                                         |
| chameleon      | 6.57 ms                                                                | 6.51 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (3): docutils, html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230324-linux-x86_64-python-f2e5a6ee628502d307a9-3.12.0a6+-f2e5a6e | bm-20230324-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a6+-b201b6d |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 188 ms                                                                 | 188 ms: 1.00x slower                                                         |
| nbody          | 87.8 ms                                                                | 88.6 ms: 1.01x slower                                                        |
| float          | 73.6 ms                                                                | 74.4 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230324-linux-x86_64-python-f2e5a6ee628502d307a9-3.12.0a6+-f2e5a6e | bm-20230324-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a6+-b201b6d |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 134 ms                                                                 | 136 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (3): regex_dna, regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20230324-linux-x86_64-python-f2e5a6ee628502d307a9-3.12.0a6+-f2e5a6e | bm-20230324-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a6+-b201b6d |
|--------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_list        | 4.39 us                                                                | 4.20 us: 1.05x faster                                                        |
| unpickle_list      | 5.06 us                                                                | 4.92 us: 1.03x faster                                                        |
| xml_etree_generate | 82.1 ms                                                                | 81.1 ms: 1.01x faster                                                        |
| xml_etree_process  | 57.0 ms                                                                | 56.5 ms: 1.01x faster                                                        |
| pickle_dict        | 31.5 us                                                                | 31.7 us: 1.01x slower                                                        |
| pickle             | 10.3 us                                                                | 10.5 us: 1.02x slower                                                        |
| json_dumps         | 9.50 ms                                                                | 9.73 ms: 1.02x slower                                                        |
| json_loads         | 23.9 us                                                                | 24.5 us: 1.03x slower                                                        |
| pickle_pure_python | 286 us                                                                 | 294 us: 1.03x slower                                                         |
| unpickle           | 13.4 us                                                                | 13.9 us: 1.04x slower                                                        |
| Geometric mean     | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (3): xml_etree_parse, unpickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230324-linux-x86_64-python-f2e5a6ee628502d307a9-3.12.0a6+-f2e5a6e | bm-20230324-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a6+-b201b6d |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.50 ms                                                                | 6.34 ms: 1.03x faster                                                        |
| python_startup         | 8.80 ms                                                                | 8.65 ms: 1.02x faster                                                        |
| Geometric mean         | (ref)                                                                  | 1.02x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20230324-linux-x86_64-python-f2e5a6ee628502d307a9-3.12.0a6+-f2e5a6e | bm-20230324-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a6+-b201b6d |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml     | 48.0 ms                                                                | 48.5 ms: 1.01x slower                                                        |
| mako           | 9.91 ms                                                                | 10.1 ms: 1.02x slower                                                        |
| genshi_text    | 21.4 ms                                                                | 22.5 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                                 |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20230324-linux-x86_64-python-f2e5a6ee628502d307a9-3.12.0a6+-f2e5a6e | bm-20230324-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a6+-b201b6d |
|-------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_list             | 4.39 us                                                                | 4.20 us: 1.05x faster                                                        |
| gc_traversal            | 4.06 ms                                                                | 3.93 ms: 1.03x faster                                                        |
| mdp                     | 2.63 sec                                                               | 2.55 sec: 1.03x faster                                                       |
| unpickle_list           | 5.06 us                                                                | 4.92 us: 1.03x faster                                                        |
| python_startup_no_site  | 6.50 ms                                                                | 6.34 ms: 1.03x faster                                                        |
| spectral_norm           | 92.7 ms                                                                | 91.1 ms: 1.02x faster                                                        |
| python_startup          | 8.80 ms                                                                | 8.65 ms: 1.02x faster                                                        |
| scimark_sparse_mat_mult | 4.24 ms                                                                | 4.17 ms: 1.02x faster                                                        |
| sqlite_synth            | 2.64 us                                                                | 2.60 us: 1.01x faster                                                        |
| xml_etree_generate      | 82.1 ms                                                                | 81.1 ms: 1.01x faster                                                        |
| scimark_sor             | 113 ms                                                                 | 111 ms: 1.01x faster                                                         |
| nqueens                 | 81.3 ms                                                                | 80.6 ms: 1.01x faster                                                        |
| chameleon               | 6.57 ms                                                                | 6.51 ms: 1.01x faster                                                        |
| xml_etree_process       | 57.0 ms                                                                | 56.5 ms: 1.01x faster                                                        |
| async_generators        | 412 ms                                                                 | 409 ms: 1.01x faster                                                         |
| raytrace                | 286 ms                                                                 | 284 ms: 1.01x faster                                                         |
| comprehensions          | 23.7 us                                                                | 23.7 us: 1.00x faster                                                        |
| hexiom                  | 6.08 ms                                                                | 6.06 ms: 1.00x faster                                                        |
| 2to3                    | 253 ms                                                                 | 253 ms: 1.00x faster                                                         |
| pidigits                | 188 ms                                                                 | 188 ms: 1.00x slower                                                         |
| aiohttp                 | 1.01 ms                                                                | 1.01 ms: 1.00x slower                                                        |
| gunicorn                | 1.09 ms                                                                | 1.09 ms: 1.00x slower                                                        |
| crypto_pyaes            | 73.5 ms                                                                | 73.8 ms: 1.00x slower                                                        |
| dulwich_log             | 63.4 ms                                                                | 63.6 ms: 1.00x slower                                                        |
| sqlglot_optimize        | 51.4 ms                                                                | 51.6 ms: 1.00x slower                                                        |
| pickle_dict             | 31.5 us                                                                | 31.7 us: 1.01x slower                                                        |
| sqlglot_normalize       | 107 ms                                                                 | 108 ms: 1.01x slower                                                         |
| bench_thread_pool       | 789 us                                                                 | 794 us: 1.01x slower                                                         |
| richards                | 43.9 ms                                                                | 44.2 ms: 1.01x slower                                                        |
| sqlglot_parse           | 1.43 ms                                                                | 1.44 ms: 1.01x slower                                                        |
| deltablue               | 3.23 ms                                                                | 3.26 ms: 1.01x slower                                                        |
| sqlglot_transpile       | 1.72 ms                                                                | 1.73 ms: 1.01x slower                                                        |
| create_gc_cycles        | 1.47 ms                                                                | 1.48 ms: 1.01x slower                                                        |
| sympy_str               | 286 ms                                                                 | 288 ms: 1.01x slower                                                         |
| generators              | 28.9 ms                                                                | 29.1 ms: 1.01x slower                                                        |
| nbody                   | 87.8 ms                                                                | 88.6 ms: 1.01x slower                                                        |
| genshi_xml              | 48.0 ms                                                                | 48.5 ms: 1.01x slower                                                        |
| pathlib                 | 18.0 ms                                                                | 18.2 ms: 1.01x slower                                                        |
| deepcopy_memo           | 34.1 us                                                                | 34.4 us: 1.01x slower                                                        |
| pprint_pformat          | 1.41 sec                                                               | 1.42 sec: 1.01x slower                                                       |
| float                   | 73.6 ms                                                                | 74.4 ms: 1.01x slower                                                        |
| regex_compile           | 134 ms                                                                 | 136 ms: 1.01x slower                                                         |
| sympy_sum               | 166 ms                                                                 | 168 ms: 1.01x slower                                                         |
| sympy_expand            | 460 ms                                                                 | 467 ms: 1.01x slower                                                         |
| telco                   | 6.38 ms                                                                | 6.48 ms: 1.02x slower                                                        |
| sympy_integrate         | 20.4 ms                                                                | 20.8 ms: 1.02x slower                                                        |
| meteor_contest          | 102 ms                                                                 | 104 ms: 1.02x slower                                                         |
| pickle                  | 10.3 us                                                                | 10.5 us: 1.02x slower                                                        |
| sqlalchemy_imperative   | 17.8 ms                                                                | 18.1 ms: 1.02x slower                                                        |
| chaos                   | 65.6 ms                                                                | 66.9 ms: 1.02x slower                                                        |
| mako                    | 9.91 ms                                                                | 10.1 ms: 1.02x slower                                                        |
| deepcopy_reduce         | 2.97 us                                                                | 3.04 us: 1.02x slower                                                        |
| pprint_safe_repr        | 685 ms                                                                 | 700 ms: 1.02x slower                                                         |
| go                      | 138 ms                                                                 | 141 ms: 1.02x slower                                                         |
| fannkuch                | 376 ms                                                                 | 384 ms: 1.02x slower                                                         |
| deepcopy                | 326 us                                                                 | 333 us: 1.02x slower                                                         |
| json_dumps              | 9.50 ms                                                                | 9.73 ms: 1.02x slower                                                        |
| json_loads              | 23.9 us                                                                | 24.5 us: 1.03x slower                                                        |
| pickle_pure_python      | 286 us                                                                 | 294 us: 1.03x slower                                                         |
| pyflate                 | 413 ms                                                                 | 427 ms: 1.03x slower                                                         |
| unpack_sequence         | 42.9 ns                                                                | 44.4 ns: 1.04x slower                                                        |
| unpickle                | 13.4 us                                                                | 13.9 us: 1.04x slower                                                        |
| logging_format          | 6.31 us                                                                | 6.58 us: 1.04x slower                                                        |
| genshi_text             | 21.4 ms                                                                | 22.5 ms: 1.05x slower                                                        |
| logging_simple          | 5.74 us                                                                | 6.05 us: 1.05x slower                                                        |
| coroutines              | 22.8 ms                                                                | 24.1 ms: 1.06x slower                                                        |
| Geometric mean          | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (28): scimark_lu, sqlalchemy_declarative, logging_silent, scimark_fft, xml_etree_parse, async_tree_cpu_io_mixed, pycparser, async_tree_memoization, coverage, async_tree_none, regex_dna, thrift, asyncio_tcp, bench_mp_pool, regex_v8, docutils, async_tree_io, regex_effbot, html5lib, unpickle_pure_python, mypy2, xml_etree_iterparse, scimark_monte_carlo, djangocms, tornado_http, django_template, json, dask
