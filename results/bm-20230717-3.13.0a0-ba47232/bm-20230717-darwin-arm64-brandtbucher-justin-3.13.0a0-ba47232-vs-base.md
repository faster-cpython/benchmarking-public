
# Results vs. base

- fork: brandtbucher
- ref: justin
- machine: darwin-arm64
- commit hash: ba47232
- commit date: 2023-07-17
- overall geometric mean: 1.02x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230602-darwin-arm64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230717-darwin-arm64-brandtbucher-justin-3.13.0a0-ba47232 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| docutils       | 1.51 sec                                                              | 1.54 sec: 1.02x slower                                        |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                  |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230602-darwin-arm64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230717-darwin-arm64-brandtbucher-justin-3.13.0a0-ba47232 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| nbody          | 69.0 ms                                                               | 69.4 ms: 1.01x slower                                         |
| float          | 57.0 ms                                                               | 57.6 ms: 1.01x slower                                         |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                  |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230602-darwin-arm64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230717-darwin-arm64-brandtbucher-justin-3.13.0a0-ba47232 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_effbot   | 2.59 ms                                                               | 2.56 ms: 1.01x faster                                         |
| regex_v8       | 15.8 ms                                                               | 15.9 ms: 1.00x slower                                         |
| regex_compile  | 75.5 ms                                                               | 75.9 ms: 1.00x slower                                         |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                  |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230602-darwin-arm64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230717-darwin-arm64-brandtbucher-justin-3.13.0a0-ba47232 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| pickle_pure_python   | 189 us                                                                | 183 us: 1.03x faster                                          |
| xml_etree_process    | 39.0 ms                                                               | 38.2 ms: 1.02x faster                                         |
| unpickle_pure_python | 145 us                                                                | 143 us: 1.01x faster                                          |
| xml_etree_generate   | 56.1 ms                                                               | 56.0 ms: 1.00x faster                                         |
| unpickle             | 9.27 us                                                               | 9.31 us: 1.00x slower                                         |
| unpickle_list        | 3.19 us                                                               | 3.25 us: 1.02x slower                                         |
| json_dumps           | 6.31 ms                                                               | 6.44 ms: 1.02x slower                                         |
| tomli_loads          | 1.39 sec                                                              | 1.52 sec: 1.09x slower                                        |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                  |

Benchmark hidden because not significant (6): json_loads, pickle_dict, xml_etree_iterparse, pickle, pickle_list, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230602-darwin-arm64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230717-darwin-arm64-brandtbucher-justin-3.13.0a0-ba47232 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 12.4 ms                                                               | 12.7 ms: 1.02x slower                                         |
| python_startup_no_site | 10.2 ms                                                               | 10.5 ms: 1.03x slower                                         |
| Geometric mean         | (ref)                                                                 | 1.03x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230602-darwin-arm64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230717-darwin-arm64-brandtbucher-justin-3.13.0a0-ba47232 |
|-----------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| mako      | 7.53 ms                                                               | 8.10 ms: 1.07x slower                                         |

All benchmarks:
===============

| Benchmark                | bm-20230602-darwin-arm64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230717-darwin-arm64-brandtbucher-justin-3.13.0a0-ba47232 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| generators               | 26.7 ms                                                               | 24.8 ms: 1.08x faster                                         |
| logging_silent           | 69.4 ns                                                               | 65.8 ns: 1.06x faster                                         |
| unpack_sequence          | 28.4 ns                                                               | 27.2 ns: 1.04x faster                                         |
| coroutines               | 17.8 ms                                                               | 17.2 ms: 1.04x faster                                         |
| pickle_pure_python       | 189 us                                                                | 183 us: 1.03x faster                                          |
| pprint_pformat           | 1.01 sec                                                              | 989 ms: 1.02x faster                                          |
| xml_etree_process        | 39.0 ms                                                               | 38.2 ms: 1.02x faster                                         |
| pprint_safe_repr         | 497 ms                                                                | 488 ms: 1.02x faster                                          |
| richards_super           | 34.0 ms                                                               | 33.5 ms: 1.02x faster                                         |
| pycparser                | 674 ms                                                                | 664 ms: 1.01x faster                                          |
| async_tree_none          | 280 ms                                                                | 276 ms: 1.01x faster                                          |
| coverage                 | 51.1 ms                                                               | 50.4 ms: 1.01x faster                                         |
| async_generators         | 311 ms                                                                | 307 ms: 1.01x faster                                          |
| spectral_norm            | 74.8 ms                                                               | 73.8 ms: 1.01x faster                                         |
| unpickle_pure_python     | 145 us                                                                | 143 us: 1.01x faster                                          |
| regex_effbot             | 2.59 ms                                                               | 2.56 ms: 1.01x faster                                         |
| richards                 | 30.1 ms                                                               | 29.8 ms: 1.01x faster                                         |
| deepcopy_reduce          | 2.07 us                                                               | 2.05 us: 1.01x faster                                         |
| typing_runtime_protocols | 89.3 us                                                               | 88.8 us: 1.01x faster                                         |
| sqlglot_optimize         | 34.2 ms                                                               | 34.0 ms: 1.01x faster                                         |
| sqlglot_normalize        | 184 ms                                                                | 183 ms: 1.00x faster                                          |
| create_gc_cycles         | 698 us                                                                | 696 us: 1.00x faster                                          |
| xml_etree_generate       | 56.1 ms                                                               | 56.0 ms: 1.00x faster                                         |
| gc_traversal             | 2.40 ms                                                               | 2.40 ms: 1.00x faster                                         |
| hexiom                   | 4.23 ms                                                               | 4.23 ms: 1.00x faster                                         |
| unpickle                 | 9.27 us                                                               | 9.31 us: 1.00x slower                                         |
| regex_v8                 | 15.8 ms                                                               | 15.9 ms: 1.00x slower                                         |
| bench_thread_pool        | 482 us                                                                | 484 us: 1.00x slower                                          |
| scimark_lu               | 73.1 ms                                                               | 73.5 ms: 1.00x slower                                         |
| regex_compile            | 75.5 ms                                                               | 75.9 ms: 1.00x slower                                         |
| nbody                    | 69.0 ms                                                               | 69.4 ms: 1.01x slower                                         |
| sqlite_synth             | 1.56 us                                                               | 1.57 us: 1.01x slower                                         |
| dulwich_log              | 30.1 ms                                                               | 30.4 ms: 1.01x slower                                         |
| asyncio_tcp_ssl          | 1.25 sec                                                              | 1.27 sec: 1.01x slower                                        |
| float                    | 57.0 ms                                                               | 57.6 ms: 1.01x slower                                         |
| nqueens                  | 59.7 ms                                                               | 60.4 ms: 1.01x slower                                         |
| json                     | 2.96 ms                                                               | 3.00 ms: 1.01x slower                                         |
| dask                     | 320 ms                                                                | 325 ms: 1.02x slower                                          |
| unpickle_list            | 3.19 us                                                               | 3.25 us: 1.02x slower                                         |
| docutils                 | 1.51 sec                                                              | 1.54 sec: 1.02x slower                                        |
| json_dumps               | 6.31 ms                                                               | 6.44 ms: 1.02x slower                                         |
| logging_format           | 3.86 us                                                               | 3.95 us: 1.02x slower                                         |
| bench_mp_pool            | 46.3 ms                                                               | 47.3 ms: 1.02x slower                                         |
| python_startup           | 12.4 ms                                                               | 12.7 ms: 1.02x slower                                         |
| logging_simple           | 3.58 us                                                               | 3.67 us: 1.02x slower                                         |
| telco                    | 3.74 ms                                                               | 3.84 ms: 1.03x slower                                         |
| scimark_fft              | 199 ms                                                                | 205 ms: 1.03x slower                                          |
| crypto_pyaes             | 51.5 ms                                                               | 53.2 ms: 1.03x slower                                         |
| python_startup_no_site   | 10.2 ms                                                               | 10.5 ms: 1.03x slower                                         |
| deltablue                | 2.41 ms                                                               | 2.50 ms: 1.04x slower                                         |
| fannkuch                 | 265 ms                                                                | 279 ms: 1.06x slower                                          |
| sqlglot_transpile        | 1.00 ms                                                               | 1.07 ms: 1.06x slower                                         |
| chaos                    | 41.7 ms                                                               | 44.3 ms: 1.06x slower                                         |
| sqlglot_parse            | 830 us                                                                | 888 us: 1.07x slower                                          |
| pyflate                  | 313 ms                                                                | 336 ms: 1.07x slower                                          |
| mako                     | 7.53 ms                                                               | 8.10 ms: 1.07x slower                                         |
| scimark_sor              | 85.5 ms                                                               | 92.0 ms: 1.08x slower                                         |
| comprehensions           | 15.0 us                                                               | 16.1 us: 1.08x slower                                         |
| tomli_loads              | 1.39 sec                                                              | 1.52 sec: 1.09x slower                                        |
| go                       | 94.0 ms                                                               | 105 ms: 1.11x slower                                          |
| scimark_sparse_mat_mult  | 3.16 ms                                                               | 3.54 ms: 1.12x slower                                         |
| deepcopy_memo            | 25.1 us                                                               | 28.2 us: 1.12x slower                                         |
| scimark_monte_carlo      | 43.4 ms                                                               | 49.4 ms: 1.14x slower                                         |
| raytrace                 | 207 ms                                                                | 242 ms: 1.17x slower                                          |
| Geometric mean           | (ref)                                                                 | 1.02x slower                                                  |

Benchmark hidden because not significant (18): asyncio_tcp, async_tree_memoization, async_tree_cpu_io_mixed, mdp, json_loads, pickle_dict, meteor_contest, xml_etree_iterparse, pickle, mypy2, pidigits, regex_dna, deepcopy, async_tree_io, pickle_list, xml_etree_parse, pathlib, tornado_http
