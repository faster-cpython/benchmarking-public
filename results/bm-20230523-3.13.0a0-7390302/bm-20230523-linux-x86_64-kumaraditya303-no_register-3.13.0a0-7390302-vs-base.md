
# Results vs. base

- fork: kumaraditya303
- ref: no_register
- machine: linux-x86_64
- commit hash: 7390302
- commit date: 2023-05-23
- overall geometric mean: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230522-linux-x86_64-python-5ecd8c85f934e13a5ff9-3.13.0a0-5ecd8c8 | bm-20230523-linux-x86_64-kumaraditya303-no_register-3.13.0a0-7390302 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 269 ms                                                                | 267 ms: 1.01x faster                                                 |
| docutils       | 2.73 sec                                                              | 2.67 sec: 1.02x faster                                               |
| tornado_http   | 102 ms                                                                | 97.7 ms: 1.04x faster                                                |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230522-linux-x86_64-python-5ecd8c85f934e13a5ff9-3.13.0a0-5ecd8c8 | bm-20230523-linux-x86_64-kumaraditya303-no_register-3.13.0a0-7390302 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 92.5 ms                                                               | 91.9 ms: 1.01x faster                                                |
| pidigits       | 197 ms                                                                | 196 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                         |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230522-linux-x86_64-python-5ecd8c85f934e13a5ff9-3.13.0a0-5ecd8c8 | bm-20230523-linux-x86_64-kumaraditya303-no_register-3.13.0a0-7390302 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.69 ms                                                               | 3.48 ms: 1.06x faster                                                |
| regex_v8       | 23.0 ms                                                               | 21.8 ms: 1.05x faster                                                |
| regex_dna      | 213 ms                                                                | 208 ms: 1.02x faster                                                 |
| regex_compile  | 143 ms                                                                | 145 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20230522-linux-x86_64-python-5ecd8c85f934e13a5ff9-3.13.0a0-5ecd8c8 | bm-20230523-linux-x86_64-kumaraditya303-no_register-3.13.0a0-7390302 |
|--------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_generate | 85.6 ms                                                               | 84.9 ms: 1.01x faster                                                |
| xml_etree_parse    | 154 ms                                                                | 153 ms: 1.01x faster                                                 |
| pickle             | 10.5 us                                                               | 10.5 us: 1.01x faster                                                |
| xml_etree_process  | 59.3 ms                                                               | 59.1 ms: 1.00x faster                                                |
| json_loads         | 24.8 us                                                               | 24.9 us: 1.00x slower                                                |
| pickle_list        | 4.51 us                                                               | 4.65 us: 1.03x slower                                                |
| pickle_dict        | 30.7 us                                                               | 32.9 us: 1.07x slower                                                |
| Geometric mean     | (ref)                                                                 | 1.00x slower                                                         |

Benchmark hidden because not significant (7): unpickle, xml_etree_iterparse, unpickle_list, pickle_pure_python, json_dumps, unpickle_pure_python, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230522-linux-x86_64-python-5ecd8c85f934e13a5ff9-3.13.0a0-5ecd8c8 | bm-20230523-linux-x86_64-kumaraditya303-no_register-3.13.0a0-7390302 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 9.33 ms                                                               | 9.14 ms: 1.02x faster                                                |
| python_startup_no_site | 6.78 ms                                                               | 6.77 ms: 1.00x faster                                                |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230522-linux-x86_64-python-5ecd8c85f934e13a5ff9-3.13.0a0-5ecd8c8 | bm-20230523-linux-x86_64-kumaraditya303-no_register-3.13.0a0-7390302 |
|-----------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako      | 10.7 ms                                                               | 10.8 ms: 1.01x slower                                                |

All benchmarks:
===============

| Benchmark               | bm-20230522-linux-x86_64-python-5ecd8c85f934e13a5ff9-3.13.0a0-5ecd8c8 | bm-20230523-linux-x86_64-kumaraditya303-no_register-3.13.0a0-7390302 |
|-------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none         | 471 ms                                                                | 378 ms: 1.25x faster                                                 |
| async_tree_cpu_io_mixed | 712 ms                                                                | 615 ms: 1.16x faster                                                 |
| async_tree_memoization  | 576 ms                                                                | 506 ms: 1.14x faster                                                 |
| async_tree_io           | 1.16 sec                                                              | 1.07 sec: 1.09x faster                                               |
| gc_traversal            | 3.84 ms                                                               | 3.54 ms: 1.08x faster                                                |
| regex_effbot            | 3.69 ms                                                               | 3.48 ms: 1.06x faster                                                |
| regex_v8                | 23.0 ms                                                               | 21.8 ms: 1.05x faster                                                |
| tornado_http            | 102 ms                                                                | 97.7 ms: 1.04x faster                                                |
| pyflate                 | 451 ms                                                                | 435 ms: 1.04x faster                                                 |
| regex_dna               | 213 ms                                                                | 208 ms: 1.02x faster                                                 |
| meteor_contest          | 105 ms                                                                | 103 ms: 1.02x faster                                                 |
| python_startup          | 9.33 ms                                                               | 9.14 ms: 1.02x faster                                                |
| docutils                | 2.73 sec                                                              | 2.67 sec: 1.02x faster                                               |
| scimark_fft             | 357 ms                                                                | 350 ms: 1.02x faster                                                 |
| scimark_sor             | 121 ms                                                                | 119 ms: 1.02x faster                                                 |
| logging_simple          | 6.44 us                                                               | 6.34 us: 1.02x faster                                                |
| pathlib                 | 18.8 ms                                                               | 18.5 ms: 1.01x faster                                                |
| asyncio_tcp             | 513 ms                                                                | 507 ms: 1.01x faster                                                 |
| sqlite_synth            | 2.74 us                                                               | 2.71 us: 1.01x faster                                                |
| scimark_monte_carlo     | 72.1 ms                                                               | 71.3 ms: 1.01x faster                                                |
| xml_etree_generate      | 85.6 ms                                                               | 84.9 ms: 1.01x faster                                                |
| spectral_norm           | 106 ms                                                                | 105 ms: 1.01x faster                                                 |
| json                    | 4.76 ms                                                               | 4.72 ms: 1.01x faster                                                |
| xml_etree_parse         | 154 ms                                                                | 153 ms: 1.01x faster                                                 |
| fannkuch                | 382 ms                                                                | 379 ms: 1.01x faster                                                 |
| create_gc_cycles        | 1.51 ms                                                               | 1.50 ms: 1.01x faster                                                |
| coroutines              | 22.2 ms                                                               | 22.0 ms: 1.01x faster                                                |
| pickle                  | 10.5 us                                                               | 10.5 us: 1.01x faster                                                |
| nbody                   | 92.5 ms                                                               | 91.9 ms: 1.01x faster                                                |
| deltablue               | 3.53 ms                                                               | 3.51 ms: 1.01x faster                                                |
| asyncio_tcp_ssl         | 1.79 sec                                                              | 1.79 sec: 1.01x faster                                               |
| 2to3                    | 269 ms                                                                | 267 ms: 1.01x faster                                                 |
| pidigits                | 197 ms                                                                | 196 ms: 1.00x faster                                                 |
| nqueens                 | 81.0 ms                                                               | 80.6 ms: 1.00x faster                                                |
| xml_etree_process       | 59.3 ms                                                               | 59.1 ms: 1.00x faster                                                |
| go                      | 135 ms                                                                | 135 ms: 1.00x faster                                                 |
| python_startup_no_site  | 6.78 ms                                                               | 6.77 ms: 1.00x faster                                                |
| logging_silent          | 98.7 ns                                                               | 98.9 ns: 1.00x slower                                                |
| sqlglot_normalize       | 108 ms                                                                | 108 ms: 1.00x slower                                                 |
| dulwich_log             | 67.7 ms                                                               | 68.0 ms: 1.00x slower                                                |
| crypto_pyaes            | 77.7 ms                                                               | 78.0 ms: 1.00x slower                                                |
| json_loads              | 24.8 us                                                               | 24.9 us: 1.00x slower                                                |
| pprint_pformat          | 1.50 sec                                                              | 1.50 sec: 1.01x slower                                               |
| pprint_safe_repr        | 730 ms                                                                | 736 ms: 1.01x slower                                                 |
| deepcopy                | 356 us                                                                | 359 us: 1.01x slower                                                 |
| richards_super          | 49.2 ms                                                               | 49.6 ms: 1.01x slower                                                |
| comprehensions          | 20.6 us                                                               | 20.8 us: 1.01x slower                                                |
| deepcopy_memo           | 37.7 us                                                               | 38.1 us: 1.01x slower                                                |
| mako                    | 10.7 ms                                                               | 10.8 ms: 1.01x slower                                                |
| regex_compile           | 143 ms                                                                | 145 ms: 1.01x slower                                                 |
| unpack_sequence         | 51.1 ns                                                               | 51.7 ns: 1.01x slower                                                |
| coverage                | 96.3 ms                                                               | 97.8 ms: 1.02x slower                                                |
| generators              | 30.5 ms                                                               | 31.0 ms: 1.02x slower                                                |
| pycparser               | 1.16 sec                                                              | 1.19 sec: 1.02x slower                                               |
| deepcopy_reduce         | 3.13 us                                                               | 3.22 us: 1.03x slower                                                |
| pickle_list             | 4.51 us                                                               | 4.65 us: 1.03x slower                                                |
| mdp                     | 2.56 sec                                                              | 2.71 sec: 1.06x slower                                               |
| pickle_dict             | 30.7 us                                                               | 32.9 us: 1.07x slower                                                |
| Geometric mean          | (ref)                                                                 | 1.01x faster                                                         |

Benchmark hidden because not significant (24): unpickle, richards, telco, sqlglot_transpile, xml_etree_iterparse, unpickle_list, async_generators, sqlglot_parse, float, logging_format, typing_runtime_protocols, raytrace, sqlglot_optimize, pickle_pure_python, hexiom, chaos, bench_mp_pool, mypy2, bench_thread_pool, json_dumps, unpickle_pure_python, scimark_sparse_mat_mult, tomli_loads, scimark_lu
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230522-3.13.0a0-5ecd8c8/bm-20230522-linux-x86_64-python-5ecd8c85f934e13a5ff9-3.13.0a0-5ecd8c8.json: dask
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20230523-3.13.0a0-7390302/bm-20230523-linux-x86_64-kumaraditya303-no_register-3.13.0a0-7390302.json: djangocms, genshi_text, genshi_xml, html5lib
