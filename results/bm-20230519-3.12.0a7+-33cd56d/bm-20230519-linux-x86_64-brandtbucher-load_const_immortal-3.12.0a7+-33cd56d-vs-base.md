
# Results vs. base

- fork: brandtbucher
- ref: load_const_immortal
- machine: linux-x86_64
- commit hash: 33cd56d
- commit date: 2023-05-19
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230519-linux-x86_64-python-3bc94e678f2961eafc9d-3.12.0a7+-3bc94e6 | bm-20230519-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-33cd56d |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 268 ms                                                                 | 267 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230519-linux-x86_64-python-3bc94e678f2961eafc9d-3.12.0a7+-3bc94e6 | bm-20230519-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-33cd56d |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 196 ms                                                                 | 197 ms: 1.00x slower                                                        |
| nbody          | 88.6 ms                                                                | 89.7 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230519-linux-x86_64-python-3bc94e678f2961eafc9d-3.12.0a7+-3bc94e6 | bm-20230519-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-33cd56d |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.63 ms                                                                | 3.60 ms: 1.01x faster                                                       |
| regex_v8       | 21.7 ms                                                                | 21.8 ms: 1.00x slower                                                       |
| regex_dna      | 205 ms                                                                 | 206 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20230519-linux-x86_64-python-3bc94e678f2961eafc9d-3.12.0a7+-3bc94e6 | bm-20230519-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-33cd56d |
|--------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_loads         | 24.8 us                                                                | 25.0 us: 1.01x slower                                                       |
| xml_etree_generate | 84.8 ms                                                                | 85.6 ms: 1.01x slower                                                       |
| xml_etree_process  | 58.9 ms                                                                | 59.7 ms: 1.01x slower                                                       |
| pickle_dict        | 30.4 us                                                                | 30.9 us: 1.02x slower                                                       |
| pickle_pure_python | 311 us                                                                 | 318 us: 1.02x slower                                                        |
| pickle_list        | 4.53 us                                                                | 4.68 us: 1.03x slower                                                       |
| pickle             | 10.5 us                                                                | 11.0 us: 1.05x slower                                                       |
| Geometric mean     | (ref)                                                                  | 1.01x slower                                                                |

Benchmark hidden because not significant (7): unpickle, xml_etree_iterparse, json_dumps, tomli_loads, unpickle_pure_python, xml_etree_parse, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230519-linux-x86_64-python-3bc94e678f2961eafc9d-3.12.0a7+-3bc94e6 | bm-20230519-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-33cd56d |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 9.30 ms                                                                | 9.33 ms: 1.00x slower                                                       |
| python_startup_no_site | 6.76 ms                                                                | 6.78 ms: 1.00x slower                                                       |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230519-linux-x86_64-python-3bc94e678f2961eafc9d-3.12.0a7+-3bc94e6 | bm-20230519-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-33cd56d |
|-----------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako      | 10.6 ms                                                                | 10.7 ms: 1.00x slower                                                       |

All benchmarks:
===============

| Benchmark                | bm-20230519-linux-x86_64-python-3bc94e678f2961eafc9d-3.12.0a7+-3bc94e6 | bm-20230519-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-33cd56d |
|--------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| gc_traversal             | 4.09 ms                                                                | 3.84 ms: 1.07x faster                                                       |
| unpack_sequence          | 48.8 ns                                                                | 47.0 ns: 1.04x faster                                                       |
| spectral_norm            | 108 ms                                                                 | 105 ms: 1.03x faster                                                        |
| fannkuch                 | 391 ms                                                                 | 381 ms: 1.03x faster                                                        |
| mdp                      | 2.59 sec                                                               | 2.54 sec: 1.02x faster                                                      |
| logging_silent           | 102 ns                                                                 | 100 ns: 1.02x faster                                                        |
| generators               | 31.4 ms                                                                | 30.8 ms: 1.02x faster                                                       |
| scimark_monte_carlo      | 72.9 ms                                                                | 71.6 ms: 1.02x faster                                                       |
| nqueens                  | 82.4 ms                                                                | 81.1 ms: 1.02x faster                                                       |
| richards_super           | 50.7 ms                                                                | 49.9 ms: 1.02x faster                                                       |
| deepcopy                 | 359 us                                                                 | 355 us: 1.01x faster                                                        |
| coverage                 | 96.6 ms                                                                | 95.4 ms: 1.01x faster                                                       |
| meteor_contest           | 105 ms                                                                 | 104 ms: 1.01x faster                                                        |
| pathlib                  | 18.6 ms                                                                | 18.4 ms: 1.01x faster                                                       |
| hexiom                   | 6.16 ms                                                                | 6.10 ms: 1.01x faster                                                       |
| deepcopy_memo            | 38.0 us                                                                | 37.6 us: 1.01x faster                                                       |
| crypto_pyaes             | 80.5 ms                                                                | 79.8 ms: 1.01x faster                                                       |
| raytrace                 | 299 ms                                                                 | 296 ms: 1.01x faster                                                        |
| pycparser                | 1.15 sec                                                               | 1.14 sec: 1.01x faster                                                      |
| regex_effbot             | 3.63 ms                                                                | 3.60 ms: 1.01x faster                                                       |
| comprehensions           | 20.7 us                                                                | 20.6 us: 1.00x faster                                                       |
| chaos                    | 65.0 ms                                                                | 64.7 ms: 1.00x faster                                                       |
| sqlglot_parse            | 1.33 ms                                                                | 1.33 ms: 1.00x faster                                                       |
| bench_thread_pool        | 824 us                                                                 | 821 us: 1.00x faster                                                        |
| asyncio_tcp_ssl          | 1.80 sec                                                               | 1.79 sec: 1.00x faster                                                      |
| 2to3                     | 268 ms                                                                 | 267 ms: 1.00x faster                                                        |
| regex_v8                 | 21.7 ms                                                                | 21.8 ms: 1.00x slower                                                       |
| regex_dna                | 205 ms                                                                 | 206 ms: 1.00x slower                                                        |
| asyncio_tcp              | 512 ms                                                                 | 514 ms: 1.00x slower                                                        |
| python_startup           | 9.30 ms                                                                | 9.33 ms: 1.00x slower                                                       |
| sqlglot_optimize         | 53.8 ms                                                                | 54.0 ms: 1.00x slower                                                       |
| python_startup_no_site   | 6.76 ms                                                                | 6.78 ms: 1.00x slower                                                       |
| pyflate                  | 449 ms                                                                 | 451 ms: 1.00x slower                                                        |
| pidigits                 | 196 ms                                                                 | 197 ms: 1.00x slower                                                        |
| go                       | 137 ms                                                                 | 137 ms: 1.00x slower                                                        |
| mako                     | 10.6 ms                                                                | 10.7 ms: 1.00x slower                                                       |
| dulwich_log              | 67.5 ms                                                                | 67.8 ms: 1.00x slower                                                       |
| json_loads               | 24.8 us                                                                | 25.0 us: 1.01x slower                                                       |
| sqlite_synth             | 2.72 us                                                                | 2.74 us: 1.01x slower                                                       |
| create_gc_cycles         | 1.49 ms                                                                | 1.51 ms: 1.01x slower                                                       |
| sqlglot_normalize        | 109 ms                                                                 | 110 ms: 1.01x slower                                                        |
| typing_runtime_protocols | 139 us                                                                 | 140 us: 1.01x slower                                                        |
| xml_etree_generate       | 84.8 ms                                                                | 85.6 ms: 1.01x slower                                                       |
| scimark_lu               | 114 ms                                                                 | 115 ms: 1.01x slower                                                        |
| async_tree_io            | 1.15 sec                                                               | 1.16 sec: 1.01x slower                                                      |
| nbody                    | 88.6 ms                                                                | 89.7 ms: 1.01x slower                                                       |
| xml_etree_process        | 58.9 ms                                                                | 59.7 ms: 1.01x slower                                                       |
| telco                    | 6.85 ms                                                                | 6.96 ms: 1.02x slower                                                       |
| pickle_dict              | 30.4 us                                                                | 30.9 us: 1.02x slower                                                       |
| scimark_fft              | 351 ms                                                                 | 358 ms: 1.02x slower                                                        |
| logging_format           | 7.00 us                                                                | 7.15 us: 1.02x slower                                                       |
| pickle_pure_python       | 311 us                                                                 | 318 us: 1.02x slower                                                        |
| logging_simple           | 6.35 us                                                                | 6.49 us: 1.02x slower                                                       |
| scimark_sparse_mat_mult  | 4.86 ms                                                                | 5.01 ms: 1.03x slower                                                       |
| pickle_list              | 4.53 us                                                                | 4.68 us: 1.03x slower                                                       |
| scimark_sor              | 120 ms                                                                 | 124 ms: 1.03x slower                                                        |
| pickle                   | 10.5 us                                                                | 11.0 us: 1.05x slower                                                       |
| Geometric mean           | (ref)                                                                  | 1.00x slower                                                                |

Benchmark hidden because not significant (28): unpickle, json, sqlalchemy_imperative, tornado_http, coroutines, sqlalchemy_declarative, deltablue, sqlglot_transpile, mypy2, docutils, xml_etree_iterparse, json_dumps, bench_mp_pool, tomli_loads, unpickle_pure_python, pprint_pformat, dask, async_generators, pprint_safe_repr, float, deepcopy_reduce, regex_compile, xml_etree_parse, async_tree_none, async_tree_memoization, richards, async_tree_cpu_io_mixed, unpickle_list
