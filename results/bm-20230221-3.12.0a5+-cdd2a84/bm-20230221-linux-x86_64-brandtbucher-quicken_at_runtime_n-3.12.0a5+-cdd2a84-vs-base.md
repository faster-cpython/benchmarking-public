
# Results vs. base

- fork: brandtbucher
- ref: quicken_at_runtime_n
- machine: linux-x86_64
- commit hash: cdd2a84
- commit date: 2023-02-21
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230222-linux-x86_64-python-d5c7954d0c3ff874d2d2-3.12.0a5+-d5c7954 | bm-20230221-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a5+-cdd2a84 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 248 ms                                                                 | 247 ms: 1.00x faster                                                         |
| chameleon      | 6.50 ms                                                                | 6.42 ms: 1.01x faster                                                        |
| docutils       | 2.54 sec                                                               | 2.53 sec: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230222-linux-x86_64-python-d5c7954d0c3ff874d2d2-3.12.0a5+-d5c7954 | bm-20230221-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a5+-cdd2a84 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 197 ms                                                                 | 192 ms: 1.03x faster                                                         |
| nbody          | 97.1 ms                                                                | 96.0 ms: 1.01x faster                                                        |
| float          | 72.0 ms                                                                | 72.6 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230222-linux-x86_64-python-d5c7954d0c3ff874d2d2-3.12.0a5+-d5c7954 | bm-20230221-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a5+-cdd2a84 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 22.0 ms                                                                | 22.1 ms: 1.00x slower                                                        |
| regex_compile  | 128 ms                                                                 | 129 ms: 1.01x slower                                                         |
| regex_effbot   | 3.29 ms                                                                | 3.36 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230222-linux-x86_64-python-d5c7954d0c3ff874d2d2-3.12.0a5+-d5c7954 | bm-20230221-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a5+-cdd2a84 |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle             | 13.8 us                                                                | 13.3 us: 1.04x faster                                                        |
| json_loads           | 24.1 us                                                                | 23.6 us: 1.02x faster                                                        |
| unpickle_pure_python | 198 us                                                                 | 195 us: 1.02x faster                                                         |
| json_dumps           | 9.56 ms                                                                | 9.45 ms: 1.01x faster                                                        |
| xml_etree_generate   | 80.8 ms                                                                | 80.0 ms: 1.01x faster                                                        |
| xml_etree_process    | 55.0 ms                                                                | 54.6 ms: 1.01x faster                                                        |
| pickle               | 10.1 us                                                                | 10.3 us: 1.02x slower                                                        |
| pickle_dict          | 30.4 us                                                                | 32.4 us: 1.06x slower                                                        |
| pickle_list          | 4.02 us                                                                | 4.30 us: 1.07x slower                                                        |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (4): pickle_pure_python, unpickle_list, xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230222-linux-x86_64-python-d5c7954d0c3ff874d2d2-3.12.0a5+-d5c7954 | bm-20230221-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a5+-cdd2a84 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.51 ms                                                                | 6.34 ms: 1.03x faster                                                        |
| python_startup         | 8.98 ms                                                                | 8.81 ms: 1.02x faster                                                        |
| Geometric mean         | (ref)                                                                  | 1.02x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20230222-linux-x86_64-python-d5c7954d0c3ff874d2d2-3.12.0a5+-d5c7954 | bm-20230221-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a5+-cdd2a84 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml     | 47.4 ms                                                                | 46.5 ms: 1.02x faster                                                        |
| mako           | 9.75 ms                                                                | 9.82 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark               | bm-20230222-linux-x86_64-python-d5c7954d0c3ff874d2d2-3.12.0a5+-d5c7954 | bm-20230221-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a5+-cdd2a84 |
|-------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle                | 13.8 us                                                                | 13.3 us: 1.04x faster                                                        |
| python_startup_no_site  | 6.51 ms                                                                | 6.34 ms: 1.03x faster                                                        |
| pidigits                | 197 ms                                                                 | 192 ms: 1.03x faster                                                         |
| generators              | 30.2 ms                                                                | 29.5 ms: 1.02x faster                                                        |
| scimark_sor             | 106 ms                                                                 | 104 ms: 1.02x faster                                                         |
| json_loads              | 24.1 us                                                                | 23.6 us: 1.02x faster                                                        |
| json                    | 4.64 ms                                                                | 4.55 ms: 1.02x faster                                                        |
| genshi_xml              | 47.4 ms                                                                | 46.5 ms: 1.02x faster                                                        |
| scimark_monte_carlo     | 67.8 ms                                                                | 66.5 ms: 1.02x faster                                                        |
| python_startup          | 8.98 ms                                                                | 8.81 ms: 1.02x faster                                                        |
| unpickle_pure_python    | 198 us                                                                 | 195 us: 1.02x faster                                                         |
| sqlite_synth            | 2.64 us                                                                | 2.60 us: 1.01x faster                                                        |
| chameleon               | 6.50 ms                                                                | 6.42 ms: 1.01x faster                                                        |
| pprint_pformat          | 1.40 sec                                                               | 1.38 sec: 1.01x faster                                                       |
| json_dumps              | 9.56 ms                                                                | 9.45 ms: 1.01x faster                                                        |
| nbody                   | 97.1 ms                                                                | 96.0 ms: 1.01x faster                                                        |
| hexiom                  | 6.01 ms                                                                | 5.95 ms: 1.01x faster                                                        |
| xml_etree_generate      | 80.8 ms                                                                | 80.0 ms: 1.01x faster                                                        |
| xml_etree_process       | 55.0 ms                                                                | 54.6 ms: 1.01x faster                                                        |
| docutils                | 2.54 sec                                                               | 2.53 sec: 1.01x faster                                                       |
| pathlib                 | 17.8 ms                                                                | 17.7 ms: 1.01x faster                                                        |
| crypto_pyaes            | 73.4 ms                                                                | 73.1 ms: 1.00x faster                                                        |
| 2to3                    | 248 ms                                                                 | 247 ms: 1.00x faster                                                         |
| aiohttp                 | 1.01 ms                                                                | 1.01 ms: 1.00x slower                                                        |
| asyncio_tcp             | 502 ms                                                                 | 503 ms: 1.00x slower                                                         |
| sympy_integrate         | 20.3 ms                                                                | 20.4 ms: 1.00x slower                                                        |
| regex_v8                | 22.0 ms                                                                | 22.1 ms: 1.00x slower                                                        |
| sympy_str               | 282 ms                                                                 | 284 ms: 1.00x slower                                                         |
| deltablue               | 3.14 ms                                                                | 3.16 ms: 1.01x slower                                                        |
| bench_thread_pool       | 787 us                                                                 | 792 us: 1.01x slower                                                         |
| dulwich_log             | 62.9 ms                                                                | 63.3 ms: 1.01x slower                                                        |
| mako                    | 9.75 ms                                                                | 9.82 ms: 1.01x slower                                                        |
| thrift                  | 758 us                                                                 | 764 us: 1.01x slower                                                         |
| logging_simple          | 5.75 us                                                                | 5.80 us: 1.01x slower                                                        |
| regex_compile           | 128 ms                                                                 | 129 ms: 1.01x slower                                                         |
| float                   | 72.0 ms                                                                | 72.6 ms: 1.01x slower                                                        |
| nqueens                 | 77.5 ms                                                                | 78.2 ms: 1.01x slower                                                        |
| fannkuch                | 360 ms                                                                 | 364 ms: 1.01x slower                                                         |
| sqlglot_transpile       | 1.70 ms                                                                | 1.72 ms: 1.01x slower                                                        |
| coroutines              | 22.5 ms                                                                | 22.8 ms: 1.01x slower                                                        |
| sqlalchemy_declarative  | 136 ms                                                                 | 138 ms: 1.01x slower                                                         |
| scimark_fft             | 310 ms                                                                 | 314 ms: 1.01x slower                                                         |
| sqlglot_parse           | 1.41 ms                                                                | 1.42 ms: 1.01x slower                                                        |
| meteor_contest          | 102 ms                                                                 | 104 ms: 1.02x slower                                                         |
| raytrace                | 278 ms                                                                 | 284 ms: 1.02x slower                                                         |
| pickle                  | 10.1 us                                                                | 10.3 us: 1.02x slower                                                        |
| unpack_sequence         | 42.2 ns                                                                | 43.1 ns: 1.02x slower                                                        |
| regex_effbot            | 3.29 ms                                                                | 3.36 ms: 1.02x slower                                                        |
| go                      | 132 ms                                                                 | 135 ms: 1.02x slower                                                         |
| telco                   | 6.34 ms                                                                | 6.50 ms: 1.02x slower                                                        |
| chaos                   | 64.8 ms                                                                | 66.4 ms: 1.03x slower                                                        |
| mdp                     | 2.44 sec                                                               | 2.51 sec: 1.03x slower                                                       |
| async_tree_memoization  | 635 ms                                                                 | 656 ms: 1.03x slower                                                         |
| gc_traversal            | 3.54 ms                                                                | 3.67 ms: 1.04x slower                                                        |
| pickle_dict             | 30.4 us                                                                | 32.4 us: 1.06x slower                                                        |
| scimark_sparse_mat_mult | 3.98 ms                                                                | 4.23 ms: 1.06x slower                                                        |
| pickle_list             | 4.02 us                                                                | 4.30 us: 1.07x slower                                                        |
| Geometric mean          | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (36): gunicorn, async_tree_cpu_io_mixed, pycparser, richards, sympy_expand, pyflate, deepcopy_reduce, bench_mp_pool, sqlglot_normalize, pickle_pure_python, sympy_sum, regex_dna, django_template, create_gc_cycles, async_tree_none, deepcopy, async_generators, coverage, mypy2, genshi_text, sqlglot_optimize, deepcopy_memo, pprint_safe_repr, async_tree_io, logging_format, tornado_http, unpickle_list, dask, spectral_norm, xml_etree_iterparse, html5lib, sqlalchemy_imperative, scimark_lu, xml_etree_parse, logging_silent, djangocms
