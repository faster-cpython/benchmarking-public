
# Results vs. base

- fork: brandtbucher
- ref: immortal_interpreter
- machine: linux-x86_64
- commit hash: 7f90633
- commit date: 2023-04-28
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230429-linux-x86_64-python-738c226786997262b765-3.12.0a7+-738c226 | bm-20230428-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-7f90633 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 270 ms                                                                 | 268 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (3): docutils, html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230429-linux-x86_64-python-738c226786997262b765-3.12.0a7+-738c226 | bm-20230428-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-7f90633 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 91.6 ms                                                                | 88.2 ms: 1.04x faster                                                        |
| pidigits       | 189 ms                                                                 | 189 ms: 1.00x faster                                                         |
| float          | 81.3 ms                                                                | 82.1 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230429-linux-x86_64-python-738c226786997262b765-3.12.0a7+-738c226 | bm-20230428-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-7f90633 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.52 ms                                                                | 3.41 ms: 1.03x faster                                                        |
| regex_compile  | 144 ms                                                                 | 143 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (2): regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20230429-linux-x86_64-python-738c226786997262b765-3.12.0a7+-738c226 | bm-20230428-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-7f90633 |
|--------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_process  | 59.6 ms                                                                | 58.7 ms: 1.01x faster                                                        |
| pickle_pure_python | 320 us                                                                 | 317 us: 1.01x faster                                                         |
| json_loads         | 26.0 us                                                                | 25.8 us: 1.01x faster                                                        |
| xml_etree_generate | 84.8 ms                                                                | 84.2 ms: 1.01x faster                                                        |
| unpickle           | 14.8 us                                                                | 14.9 us: 1.01x slower                                                        |
| xml_etree_parse    | 154 ms                                                                 | 158 ms: 1.03x slower                                                         |
| pickle             | 10.3 us                                                                | 10.8 us: 1.04x slower                                                        |
| pickle_dict        | 31.1 us                                                                | 32.6 us: 1.05x slower                                                        |
| pickle_list        | 4.45 us                                                                | 4.70 us: 1.06x slower                                                        |
| Geometric mean     | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (4): unpickle_list, unpickle_pure_python, xml_etree_iterparse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230429-linux-x86_64-python-738c226786997262b765-3.12.0a7+-738c226 | bm-20230428-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-7f90633 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 9.11 ms                                                                | 9.08 ms: 1.00x faster                                                        |
| python_startup_no_site | 6.68 ms                                                                | 6.66 ms: 1.00x faster                                                        |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20230429-linux-x86_64-python-738c226786997262b765-3.12.0a7+-738c226 | bm-20230428-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-7f90633 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text    | 22.9 ms                                                                | 22.7 ms: 1.01x faster                                                        |
| mako           | 10.9 ms                                                                | 10.9 ms: 1.00x faster                                                        |
| genshi_xml     | 50.2 ms                                                                | 50.8 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20230429-linux-x86_64-python-738c226786997262b765-3.12.0a7+-738c226 | bm-20230428-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-7f90633 |
|-------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mdp                     | 2.72 sec                                                               | 2.60 sec: 1.04x faster                                                       |
| hexiom                  | 6.32 ms                                                                | 6.08 ms: 1.04x faster                                                        |
| nbody                   | 91.6 ms                                                                | 88.2 ms: 1.04x faster                                                        |
| fannkuch                | 388 ms                                                                 | 376 ms: 1.03x faster                                                         |
| scimark_sor             | 127 ms                                                                 | 123 ms: 1.03x faster                                                         |
| regex_effbot            | 3.52 ms                                                                | 3.41 ms: 1.03x faster                                                        |
| thrift                  | 826 us                                                                 | 803 us: 1.03x faster                                                         |
| scimark_lu              | 114 ms                                                                 | 111 ms: 1.02x faster                                                         |
| nqueens                 | 81.1 ms                                                                | 79.3 ms: 1.02x faster                                                        |
| spectral_norm           | 111 ms                                                                 | 108 ms: 1.02x faster                                                         |
| async_tree_io           | 1.30 sec                                                               | 1.27 sec: 1.02x faster                                                       |
| pprint_safe_repr        | 733 ms                                                                 | 721 ms: 1.02x faster                                                         |
| raytrace                | 306 ms                                                                 | 301 ms: 1.02x faster                                                         |
| scimark_fft             | 361 ms                                                                 | 355 ms: 1.02x faster                                                         |
| pyflate                 | 451 ms                                                                 | 444 ms: 1.02x faster                                                         |
| chaos                   | 69.9 ms                                                                | 68.8 ms: 1.02x faster                                                        |
| xml_etree_process       | 59.6 ms                                                                | 58.7 ms: 1.01x faster                                                        |
| comprehensions          | 23.4 us                                                                | 23.1 us: 1.01x faster                                                        |
| logging_silent          | 99.6 ns                                                                | 98.2 ns: 1.01x faster                                                        |
| crypto_pyaes            | 79.7 ms                                                                | 78.6 ms: 1.01x faster                                                        |
| pprint_pformat          | 1.49 sec                                                               | 1.47 sec: 1.01x faster                                                       |
| scimark_sparse_mat_mult | 4.74 ms                                                                | 4.69 ms: 1.01x faster                                                        |
| async_tree_none         | 532 ms                                                                 | 526 ms: 1.01x faster                                                         |
| json                    | 4.93 ms                                                                | 4.88 ms: 1.01x faster                                                        |
| genshi_text             | 22.9 ms                                                                | 22.7 ms: 1.01x faster                                                        |
| pickle_pure_python      | 320 us                                                                 | 317 us: 1.01x faster                                                         |
| generators              | 31.3 ms                                                                | 31.1 ms: 1.01x faster                                                        |
| json_loads              | 26.0 us                                                                | 25.8 us: 1.01x faster                                                        |
| scimark_monte_carlo     | 71.9 ms                                                                | 71.3 ms: 1.01x faster                                                        |
| sqlite_synth            | 2.71 us                                                                | 2.69 us: 1.01x faster                                                        |
| deepcopy_reduce         | 3.19 us                                                                | 3.17 us: 1.01x faster                                                        |
| 2to3                    | 270 ms                                                                 | 268 ms: 1.01x faster                                                         |
| xml_etree_generate      | 84.8 ms                                                                | 84.2 ms: 1.01x faster                                                        |
| deepcopy                | 367 us                                                                 | 365 us: 1.01x faster                                                         |
| pathlib                 | 18.0 ms                                                                | 17.9 ms: 1.01x faster                                                        |
| sqlglot_optimize        | 54.7 ms                                                                | 54.4 ms: 1.01x faster                                                        |
| regex_compile           | 144 ms                                                                 | 143 ms: 1.01x faster                                                         |
| richards                | 43.6 ms                                                                | 43.4 ms: 1.01x faster                                                        |
| dulwich_log             | 67.6 ms                                                                | 67.3 ms: 1.01x faster                                                        |
| mako                    | 10.9 ms                                                                | 10.9 ms: 1.00x faster                                                        |
| python_startup          | 9.11 ms                                                                | 9.08 ms: 1.00x faster                                                        |
| python_startup_no_site  | 6.68 ms                                                                | 6.66 ms: 1.00x faster                                                        |
| pidigits                | 189 ms                                                                 | 189 ms: 1.00x faster                                                         |
| deepcopy_memo           | 38.8 us                                                                | 39.1 us: 1.01x slower                                                        |
| deltablue               | 3.51 ms                                                                | 3.53 ms: 1.01x slower                                                        |
| logging_format          | 6.86 us                                                                | 6.91 us: 1.01x slower                                                        |
| coroutines              | 22.1 ms                                                                | 22.4 ms: 1.01x slower                                                        |
| meteor_contest          | 110 ms                                                                 | 112 ms: 1.01x slower                                                         |
| float                   | 81.3 ms                                                                | 82.1 ms: 1.01x slower                                                        |
| unpickle                | 14.8 us                                                                | 14.9 us: 1.01x slower                                                        |
| pycparser               | 1.15 sec                                                               | 1.16 sec: 1.01x slower                                                       |
| genshi_xml              | 50.2 ms                                                                | 50.8 ms: 1.01x slower                                                        |
| xml_etree_parse         | 154 ms                                                                 | 158 ms: 1.03x slower                                                         |
| gc_traversal            | 3.82 ms                                                                | 3.94 ms: 1.03x slower                                                        |
| telco                   | 6.81 ms                                                                | 7.06 ms: 1.04x slower                                                        |
| pickle                  | 10.3 us                                                                | 10.8 us: 1.04x slower                                                        |
| pickle_dict             | 31.1 us                                                                | 32.6 us: 1.05x slower                                                        |
| unpack_sequence         | 49.4 ns                                                                | 52.1 ns: 1.05x slower                                                        |
| pickle_list             | 4.45 us                                                                | 4.70 us: 1.06x slower                                                        |
| Geometric mean          | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (26): async_tree_memoization, async_tree_cpu_io_mixed, sqlalchemy_imperative, async_generators, tornado_http, sqlalchemy_declarative, unpickle_list, bench_thread_pool, unpickle_pure_python, sqlglot_transpile, mypy2, sqlglot_parse, docutils, bench_mp_pool, coverage, logging_simple, regex_v8, go, dask, sqlglot_normalize, asyncio_tcp, create_gc_cycles, regex_dna, html5lib, xml_etree_iterparse, json_dumps
