
# Results vs. base

- fork: brandtbucher
- ref: justin
- machine: darwin-arm64
- commit hash: a4921c7
- commit date: 2023-07-16
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230602-darwin-arm64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230716-darwin-arm64-brandtbucher-justin-3.13.0a0-a4921c7 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| docutils       | 1.51 sec                                                              | 1.52 sec: 1.01x slower                                        |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                  |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230602-darwin-arm64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230716-darwin-arm64-brandtbucher-justin-3.13.0a0-a4921c7 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| nbody          | 69.0 ms                                                               | 69.8 ms: 1.01x slower                                         |
| float          | 57.1 ms                                                               | 59.7 ms: 1.05x slower                                         |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                  |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230602-darwin-arm64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230716-darwin-arm64-brandtbucher-justin-3.13.0a0-a4921c7 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_effbot   | 2.59 ms                                                               | 2.56 ms: 1.01x faster                                         |
| regex_v8       | 15.6 ms                                                               | 15.8 ms: 1.01x slower                                         |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                  |

Benchmark hidden because not significant (2): regex_compile, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230602-darwin-arm64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230716-darwin-arm64-brandtbucher-justin-3.13.0a0-a4921c7 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| pickle_pure_python   | 190 us                                                                | 180 us: 1.06x faster                                          |
| xml_etree_process    | 39.0 ms                                                               | 37.8 ms: 1.03x faster                                         |
| unpickle_pure_python | 145 us                                                                | 140 us: 1.03x faster                                          |
| xml_etree_iterparse  | 75.1 ms                                                               | 73.7 ms: 1.02x faster                                         |
| pickle_dict          | 18.2 us                                                               | 17.9 us: 1.02x faster                                         |
| xml_etree_generate   | 56.2 ms                                                               | 55.9 ms: 1.01x faster                                         |
| pickle               | 7.42 us                                                               | 7.47 us: 1.01x slower                                         |
| json_loads           | 17.5 us                                                               | 17.7 us: 1.01x slower                                         |
| pickle_list          | 2.87 us                                                               | 2.89 us: 1.01x slower                                         |
| unpickle             | 9.27 us                                                               | 9.38 us: 1.01x slower                                         |
| json_dumps           | 6.33 ms                                                               | 6.48 ms: 1.02x slower                                         |
| unpickle_list        | 3.19 us                                                               | 3.27 us: 1.02x slower                                         |
| tomli_loads          | 1.39 sec                                                              | 1.54 sec: 1.11x slower                                        |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                  |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230602-darwin-arm64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230716-darwin-arm64-brandtbucher-justin-3.13.0a0-a4921c7 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 12.3 ms                                                               | 12.7 ms: 1.03x slower                                         |
| python_startup_no_site | 10.2 ms                                                               | 10.6 ms: 1.04x slower                                         |
| Geometric mean         | (ref)                                                                 | 1.04x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230602-darwin-arm64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230716-darwin-arm64-brandtbucher-justin-3.13.0a0-a4921c7 |
|-----------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| mako      | 7.54 ms                                                               | 8.57 ms: 1.14x slower                                         |

All benchmarks:
===============

| Benchmark                | bm-20230602-darwin-arm64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230716-darwin-arm64-brandtbucher-justin-3.13.0a0-a4921c7 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| logging_silent           | 69.7 ns                                                               | 65.2 ns: 1.07x faster                                         |
| scimark_sor              | 85.4 ms                                                               | 80.4 ms: 1.06x faster                                         |
| coroutines               | 17.7 ms                                                               | 16.7 ms: 1.06x faster                                         |
| pickle_pure_python       | 190 us                                                                | 180 us: 1.06x faster                                          |
| generators               | 26.7 ms                                                               | 25.3 ms: 1.05x faster                                         |
| unpack_sequence          | 28.3 ns                                                               | 27.4 ns: 1.03x faster                                         |
| xml_etree_process        | 39.0 ms                                                               | 37.8 ms: 1.03x faster                                         |
| unpickle_pure_python     | 145 us                                                                | 140 us: 1.03x faster                                          |
| richards_super           | 34.1 ms                                                               | 33.1 ms: 1.03x faster                                         |
| pprint_pformat           | 1.01 sec                                                              | 981 ms: 1.02x faster                                          |
| sqlglot_optimize         | 34.3 ms                                                               | 33.5 ms: 1.02x faster                                         |
| logging_simple           | 3.58 us                                                               | 3.50 us: 1.02x faster                                         |
| logging_format           | 3.85 us                                                               | 3.77 us: 1.02x faster                                         |
| spectral_norm            | 74.7 ms                                                               | 73.1 ms: 1.02x faster                                         |
| sqlglot_normalize        | 184 ms                                                                | 181 ms: 1.02x faster                                          |
| xml_etree_iterparse      | 75.1 ms                                                               | 73.7 ms: 1.02x faster                                         |
| deepcopy                 | 227 us                                                                | 223 us: 1.02x faster                                          |
| richards                 | 30.2 ms                                                               | 29.7 ms: 1.02x faster                                         |
| async_generators         | 311 ms                                                                | 306 ms: 1.02x faster                                          |
| typing_runtime_protocols | 89.3 us                                                               | 87.9 us: 1.02x faster                                         |
| coverage                 | 50.8 ms                                                               | 50.0 ms: 1.02x faster                                         |
| pickle_dict              | 18.2 us                                                               | 17.9 us: 1.02x faster                                         |
| pycparser                | 672 ms                                                                | 662 ms: 1.01x faster                                          |
| deepcopy_reduce          | 2.06 us                                                               | 2.03 us: 1.01x faster                                         |
| hexiom                   | 4.23 ms                                                               | 4.18 ms: 1.01x faster                                         |
| pprint_safe_repr         | 494 ms                                                                | 489 ms: 1.01x faster                                          |
| regex_effbot             | 2.59 ms                                                               | 2.56 ms: 1.01x faster                                         |
| async_tree_none          | 280 ms                                                                | 278 ms: 1.01x faster                                          |
| meteor_contest           | 73.2 ms                                                               | 72.7 ms: 1.01x faster                                         |
| dulwich_log              | 30.0 ms                                                               | 29.8 ms: 1.01x faster                                         |
| xml_etree_generate       | 56.2 ms                                                               | 55.9 ms: 1.01x faster                                         |
| create_gc_cycles         | 697 us                                                                | 695 us: 1.00x faster                                          |
| gc_traversal             | 2.40 ms                                                               | 2.39 ms: 1.00x faster                                         |
| bench_thread_pool        | 483 us                                                                | 484 us: 1.00x slower                                          |
| async_tree_io            | 701 ms                                                                | 705 ms: 1.01x slower                                          |
| pickle                   | 7.42 us                                                               | 7.47 us: 1.01x slower                                         |
| json_loads               | 17.5 us                                                               | 17.7 us: 1.01x slower                                         |
| nqueens                  | 59.7 ms                                                               | 60.2 ms: 1.01x slower                                         |
| pickle_list              | 2.87 us                                                               | 2.89 us: 1.01x slower                                         |
| regex_v8                 | 15.6 ms                                                               | 15.8 ms: 1.01x slower                                         |
| docutils                 | 1.51 sec                                                              | 1.52 sec: 1.01x slower                                        |
| nbody                    | 69.0 ms                                                               | 69.8 ms: 1.01x slower                                         |
| dask                     | 319 ms                                                                | 323 ms: 1.01x slower                                          |
| deltablue                | 2.40 ms                                                               | 2.43 ms: 1.01x slower                                         |
| unpickle                 | 9.27 us                                                               | 9.38 us: 1.01x slower                                         |
| bench_mp_pool            | 46.3 ms                                                               | 47.1 ms: 1.02x slower                                         |
| json_dumps               | 6.33 ms                                                               | 6.48 ms: 1.02x slower                                         |
| unpickle_list            | 3.19 us                                                               | 3.27 us: 1.02x slower                                         |
| telco                    | 3.74 ms                                                               | 3.85 ms: 1.03x slower                                         |
| scimark_fft              | 199 ms                                                                | 205 ms: 1.03x slower                                          |
| python_startup           | 12.3 ms                                                               | 12.7 ms: 1.03x slower                                         |
| crypto_pyaes             | 51.6 ms                                                               | 53.3 ms: 1.03x slower                                         |
| sqlglot_transpile        | 1.00 ms                                                               | 1.04 ms: 1.04x slower                                         |
| python_startup_no_site   | 10.2 ms                                                               | 10.6 ms: 1.04x slower                                         |
| float                    | 57.1 ms                                                               | 59.7 ms: 1.05x slower                                         |
| sqlglot_parse            | 829 us                                                                | 872 us: 1.05x slower                                          |
| chaos                    | 41.9 ms                                                               | 44.3 ms: 1.06x slower                                         |
| scimark_lu               | 72.9 ms                                                               | 78.1 ms: 1.07x slower                                         |
| pyflate                  | 313 ms                                                                | 339 ms: 1.08x slower                                          |
| fannkuch                 | 266 ms                                                                | 292 ms: 1.10x slower                                          |
| scimark_sparse_mat_mult  | 3.15 ms                                                               | 3.48 ms: 1.10x slower                                         |
| go                       | 94.0 ms                                                               | 104 ms: 1.11x slower                                          |
| comprehensions           | 14.9 us                                                               | 16.6 us: 1.11x slower                                         |
| tomli_loads              | 1.39 sec                                                              | 1.54 sec: 1.11x slower                                        |
| scimark_monte_carlo      | 43.2 ms                                                               | 48.8 ms: 1.13x slower                                         |
| mako                     | 7.54 ms                                                               | 8.57 ms: 1.14x slower                                         |
| raytrace                 | 207 ms                                                                | 239 ms: 1.15x slower                                          |
| deepcopy_memo            | 25.0 us                                                               | 29.7 us: 1.19x slower                                         |
| Geometric mean           | (ref)                                                                 | 1.01x slower                                                  |

Benchmark hidden because not significant (14): xml_etree_parse, asyncio_tcp_ssl, tornado_http, mypy2, json, regex_compile, async_tree_cpu_io_mixed, pidigits, pathlib, regex_dna, async_tree_memoization, sqlite_synth, mdp, asyncio_tcp
