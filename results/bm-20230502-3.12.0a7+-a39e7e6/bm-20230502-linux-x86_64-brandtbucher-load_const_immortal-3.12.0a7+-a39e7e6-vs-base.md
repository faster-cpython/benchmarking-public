
# Results vs. base

- fork: brandtbucher
- ref: load_const_immortal
- machine: linux-x86_64
- commit hash: a39e7e6
- commit date: 2023-05-02
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230503-linux-x86_64-python-da1980afcb8820ffaa05-3.12.0a7+-da1980a | bm-20230502-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-a39e7e6 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 271 ms                                                                 | 270 ms: 1.00x faster                                                        |
| docutils       | 2.73 sec                                                               | 2.71 sec: 1.00x faster                                                      |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230503-linux-x86_64-python-da1980afcb8820ffaa05-3.12.0a7+-da1980a | bm-20230502-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-a39e7e6 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 82.0 ms                                                                | 81.6 ms: 1.01x faster                                                       |
| nbody          | 87.4 ms                                                                | 90.3 ms: 1.03x slower                                                       |
| pidigits       | 189 ms                                                                 | 197 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230503-linux-x86_64-python-da1980afcb8820ffaa05-3.12.0a7+-da1980a | bm-20230502-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-a39e7e6 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 205 ms                                                                 | 200 ms: 1.02x faster                                                        |
| regex_compile  | 145 ms                                                                 | 146 ms: 1.00x slower                                                        |
| regex_effbot   | 3.40 ms                                                                | 3.57 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20230503-linux-x86_64-python-da1980afcb8820ffaa05-3.12.0a7+-da1980a | bm-20230502-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-a39e7e6 |
|--------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_dict        | 31.8 us                                                                | 30.7 us: 1.04x faster                                                       |
| unpickle_list      | 5.10 us                                                                | 4.94 us: 1.03x faster                                                       |
| xml_etree_generate | 84.3 ms                                                                | 84.8 ms: 1.01x slower                                                       |
| pickle_list        | 4.58 us                                                                | 4.62 us: 1.01x slower                                                       |
| xml_etree_process  | 58.7 ms                                                                | 59.4 ms: 1.01x slower                                                       |
| pickle             | 10.5 us                                                                | 10.7 us: 1.02x slower                                                       |
| json_loads         | 25.7 us                                                                | 26.2 us: 1.02x slower                                                       |
| Geometric mean     | (ref)                                                                  | 1.00x faster                                                                |

Benchmark hidden because not significant (6): unpickle, json_dumps, unpickle_pure_python, xml_etree_iterparse, pickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230503-linux-x86_64-python-da1980afcb8820ffaa05-3.12.0a7+-da1980a | bm-20230502-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-a39e7e6 |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 9.14 ms                                                                | 9.21 ms: 1.01x slower                                                       |
| python_startup_no_site | 6.69 ms                                                                | 6.74 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230503-linux-x86_64-python-da1980afcb8820ffaa05-3.12.0a7+-da1980a | bm-20230502-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-a39e7e6 |
|-----------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako      | 10.9 ms                                                                | 10.8 ms: 1.01x faster                                                       |

All benchmarks:
===============

| Benchmark               | bm-20230503-linux-x86_64-python-da1980afcb8820ffaa05-3.12.0a7+-da1980a | bm-20230502-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-a39e7e6 |
|-------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| meteor_contest          | 118 ms                                                                 | 104 ms: 1.13x faster                                                        |
| pickle_dict             | 31.8 us                                                                | 30.7 us: 1.04x faster                                                       |
| deepcopy_memo           | 38.9 us                                                                | 37.6 us: 1.03x faster                                                       |
| unpickle_list           | 5.10 us                                                                | 4.94 us: 1.03x faster                                                       |
| logging_silent          | 104 ns                                                                 | 101 ns: 1.03x faster                                                        |
| nqueens                 | 82.8 ms                                                                | 80.6 ms: 1.03x faster                                                       |
| deltablue               | 3.64 ms                                                                | 3.54 ms: 1.03x faster                                                       |
| regex_dna               | 205 ms                                                                 | 200 ms: 1.02x faster                                                        |
| scimark_lu              | 115 ms                                                                 | 113 ms: 1.02x faster                                                        |
| deepcopy_reduce         | 3.28 us                                                                | 3.21 us: 1.02x faster                                                       |
| scimark_sor             | 127 ms                                                                 | 124 ms: 1.02x faster                                                        |
| chaos                   | 69.9 ms                                                                | 68.6 ms: 1.02x faster                                                       |
| pyflate                 | 456 ms                                                                 | 450 ms: 1.01x faster                                                        |
| mdp                     | 2.61 sec                                                               | 2.58 sec: 1.01x faster                                                      |
| deepcopy                | 370 us                                                                 | 366 us: 1.01x faster                                                        |
| coverage                | 103 ms                                                                 | 102 ms: 1.01x faster                                                        |
| raytrace                | 306 ms                                                                 | 304 ms: 1.01x faster                                                        |
| mako                    | 10.9 ms                                                                | 10.8 ms: 1.01x faster                                                       |
| float                   | 82.0 ms                                                                | 81.6 ms: 1.01x faster                                                       |
| asyncio_tcp             | 510 ms                                                                 | 507 ms: 1.00x faster                                                        |
| docutils                | 2.73 sec                                                               | 2.71 sec: 1.00x faster                                                      |
| sqlglot_optimize        | 55.5 ms                                                                | 55.3 ms: 1.00x faster                                                       |
| 2to3                    | 271 ms                                                                 | 270 ms: 1.00x faster                                                        |
| bench_thread_pool       | 836 us                                                                 | 838 us: 1.00x slower                                                        |
| sqlglot_normalize       | 114 ms                                                                 | 114 ms: 1.00x slower                                                        |
| fannkuch                | 383 ms                                                                 | 385 ms: 1.00x slower                                                        |
| regex_compile           | 145 ms                                                                 | 146 ms: 1.00x slower                                                        |
| sqlglot_transpile       | 1.67 ms                                                                | 1.68 ms: 1.01x slower                                                       |
| pprint_pformat          | 1.50 sec                                                               | 1.50 sec: 1.01x slower                                                      |
| xml_etree_generate      | 84.3 ms                                                                | 84.8 ms: 1.01x slower                                                       |
| scimark_monte_carlo     | 73.3 ms                                                                | 73.8 ms: 1.01x slower                                                       |
| python_startup          | 9.14 ms                                                                | 9.21 ms: 1.01x slower                                                       |
| hexiom                  | 6.23 ms                                                                | 6.27 ms: 1.01x slower                                                       |
| sqlglot_parse           | 1.34 ms                                                                | 1.35 ms: 1.01x slower                                                       |
| dulwich_log             | 67.8 ms                                                                | 68.3 ms: 1.01x slower                                                       |
| python_startup_no_site  | 6.69 ms                                                                | 6.74 ms: 1.01x slower                                                       |
| pickle_list             | 4.58 us                                                                | 4.62 us: 1.01x slower                                                       |
| async_tree_io           | 1.23 sec                                                               | 1.24 sec: 1.01x slower                                                      |
| scimark_sparse_mat_mult | 4.73 ms                                                                | 4.77 ms: 1.01x slower                                                       |
| sqlalchemy_declarative  | 146 ms                                                                 | 147 ms: 1.01x slower                                                        |
| scimark_fft             | 353 ms                                                                 | 356 ms: 1.01x slower                                                        |
| pathlib                 | 18.5 ms                                                                | 18.7 ms: 1.01x slower                                                       |
| pprint_safe_repr        | 734 ms                                                                 | 742 ms: 1.01x slower                                                        |
| crypto_pyaes            | 79.6 ms                                                                | 80.6 ms: 1.01x slower                                                       |
| xml_etree_process       | 58.7 ms                                                                | 59.4 ms: 1.01x slower                                                       |
| logging_format          | 7.06 us                                                                | 7.16 us: 1.01x slower                                                       |
| generators              | 32.3 ms                                                                | 32.8 ms: 1.01x slower                                                       |
| comprehensions          | 23.2 us                                                                | 23.5 us: 1.01x slower                                                       |
| pickle                  | 10.5 us                                                                | 10.7 us: 1.02x slower                                                       |
| json                    | 4.91 ms                                                                | 5.00 ms: 1.02x slower                                                       |
| json_loads              | 25.7 us                                                                | 26.2 us: 1.02x slower                                                       |
| telco                   | 6.78 ms                                                                | 6.94 ms: 1.02x slower                                                       |
| create_gc_cycles        | 1.46 ms                                                                | 1.50 ms: 1.03x slower                                                       |
| nbody                   | 87.4 ms                                                                | 90.3 ms: 1.03x slower                                                       |
| pidigits                | 189 ms                                                                 | 197 ms: 1.05x slower                                                        |
| regex_effbot            | 3.40 ms                                                                | 3.57 ms: 1.05x slower                                                       |
| gc_traversal            | 3.64 ms                                                                | 3.89 ms: 1.07x slower                                                       |
| unpack_sequence         | 49.9 ns                                                                | 53.4 ns: 1.07x slower                                                       |
| Geometric mean          | (ref)                                                                  | 1.00x slower                                                                |

Benchmark hidden because not significant (23): unpickle, async_generators, sqlite_synth, spectral_norm, richards, mypy2, tornado_http, bench_mp_pool, dask, json_dumps, regex_v8, sqlalchemy_imperative, unpickle_pure_python, logging_simple, pycparser, async_tree_cpu_io_mixed, xml_etree_iterparse, pickle_pure_python, go, async_tree_memoization, async_tree_none, xml_etree_parse, coroutines
