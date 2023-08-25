
# Results vs. base

- fork: brandtbucher
- ref: justin
- machine: darwin-arm64
- commit hash: c209db9
- commit date: 2023-08-06
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230806-darwin-arm64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-darwin-arm64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| docutils       | 1.54 sec                                                              | 1.58 sec: 1.03x slower                                        |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                  |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230806-darwin-arm64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-darwin-arm64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 59.7 ms                                                               | 62.0 ms: 1.04x slower                                         |
| nbody          | 72.1 ms                                                               | 76.2 ms: 1.06x slower                                         |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                  |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230806-darwin-arm64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-darwin-arm64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_effbot   | 2.54 ms                                                               | 2.56 ms: 1.01x slower                                         |
| regex_dna      | 149 ms                                                                | 150 ms: 1.01x slower                                          |
| regex_v8       | 15.6 ms                                                               | 15.8 ms: 1.01x slower                                         |
| regex_compile  | 80.4 ms                                                               | 85.8 ms: 1.07x slower                                         |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230806-darwin-arm64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-darwin-arm64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| pickle_dict          | 18.1 us                                                               | 17.8 us: 1.02x faster                                         |
| json_dumps           | 6.70 ms                                                               | 6.67 ms: 1.00x faster                                         |
| json_loads           | 17.4 us                                                               | 17.4 us: 1.00x faster                                         |
| pickle_pure_python   | 203 us                                                                | 205 us: 1.01x slower                                          |
| unpickle_list        | 3.16 us                                                               | 3.19 us: 1.01x slower                                         |
| unpickle             | 9.27 us                                                               | 9.39 us: 1.01x slower                                         |
| pickle               | 7.38 us                                                               | 7.50 us: 1.02x slower                                         |
| pickle_list          | 2.85 us                                                               | 2.90 us: 1.02x slower                                         |
| xml_etree_process    | 40.8 ms                                                               | 41.7 ms: 1.02x slower                                         |
| xml_etree_generate   | 58.9 ms                                                               | 60.2 ms: 1.02x slower                                         |
| xml_etree_iterparse  | 76.6 ms                                                               | 78.6 ms: 1.03x slower                                         |
| tomli_loads          | 1.63 sec                                                              | 1.67 sec: 1.03x slower                                        |
| unpickle_pure_python | 164 us                                                                | 173 us: 1.05x slower                                          |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                  |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230806-darwin-arm64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-darwin-arm64-brandtbucher-justin-3.13.0a0-c209db9 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 11.3 ms                                                               | 11.1 ms: 1.01x faster                                         |
| python_startup_no_site | 9.12 ms                                                               | 9.05 ms: 1.01x faster                                         |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230806-darwin-arm64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-darwin-arm64-brandtbucher-justin-3.13.0a0-c209db9 |
|-----------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| mako      | 7.61 ms                                                               | 8.08 ms: 1.06x slower                                         |

All benchmarks:
===============

| Benchmark                | bm-20230806-darwin-arm64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-darwin-arm64-brandtbucher-justin-3.13.0a0-c209db9 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| pathlib                  | 31.2 ms                                                               | 27.3 ms: 1.14x faster                                         |
| gc_traversal             | 2.54 ms                                                               | 2.39 ms: 1.06x faster                                         |
| pickle_dict              | 18.1 us                                                               | 17.8 us: 1.02x faster                                         |
| create_gc_cycles         | 709 us                                                                | 699 us: 1.01x faster                                          |
| python_startup           | 11.3 ms                                                               | 11.1 ms: 1.01x faster                                         |
| telco                    | 4.62 ms                                                               | 4.57 ms: 1.01x faster                                         |
| asyncio_tcp_ssl          | 1.36 sec                                                              | 1.35 sec: 1.01x faster                                        |
| python_startup_no_site   | 9.12 ms                                                               | 9.05 ms: 1.01x faster                                         |
| json_dumps               | 6.70 ms                                                               | 6.67 ms: 1.00x faster                                         |
| json_loads               | 17.4 us                                                               | 17.4 us: 1.00x faster                                         |
| logging_simple           | 3.85 us                                                               | 3.87 us: 1.00x slower                                         |
| async_tree_io            | 680 ms                                                                | 683 ms: 1.01x slower                                          |
| coverage                 | 50.8 ms                                                               | 51.1 ms: 1.01x slower                                         |
| async_tree_none          | 274 ms                                                                | 276 ms: 1.01x slower                                          |
| regex_effbot             | 2.54 ms                                                               | 2.56 ms: 1.01x slower                                         |
| regex_dna                | 149 ms                                                                | 150 ms: 1.01x slower                                          |
| deepcopy_reduce          | 2.09 us                                                               | 2.11 us: 1.01x slower                                         |
| async_tree_memoization   | 323 ms                                                                | 325 ms: 1.01x slower                                          |
| logging_format           | 4.11 us                                                               | 4.16 us: 1.01x slower                                         |
| pickle_pure_python       | 203 us                                                                | 205 us: 1.01x slower                                          |
| unpickle_list            | 3.16 us                                                               | 3.19 us: 1.01x slower                                         |
| regex_v8                 | 15.6 ms                                                               | 15.8 ms: 1.01x slower                                         |
| unpickle                 | 9.27 us                                                               | 9.39 us: 1.01x slower                                         |
| logging_silent           | 76.8 ns                                                               | 77.8 ns: 1.01x slower                                         |
| pprint_safe_repr         | 515 ms                                                                | 522 ms: 1.01x slower                                          |
| dask                     | 339 ms                                                                | 344 ms: 1.01x slower                                          |
| richards_super           | 40.9 ms                                                               | 41.5 ms: 1.01x slower                                         |
| pprint_pformat           | 1.05 sec                                                              | 1.07 sec: 1.01x slower                                        |
| dulwich_log              | 31.3 ms                                                               | 31.8 ms: 1.02x slower                                         |
| richards                 | 37.2 ms                                                               | 37.8 ms: 1.02x slower                                         |
| pickle                   | 7.38 us                                                               | 7.50 us: 1.02x slower                                         |
| raytrace                 | 230 ms                                                                | 233 ms: 1.02x slower                                          |
| pickle_list              | 2.85 us                                                               | 2.90 us: 1.02x slower                                         |
| pycparser                | 709 ms                                                                | 722 ms: 1.02x slower                                          |
| scimark_sor              | 118 ms                                                                | 120 ms: 1.02x slower                                          |
| sqlglot_transpile        | 1.11 ms                                                               | 1.13 ms: 1.02x slower                                         |
| sqlite_synth             | 1.58 us                                                               | 1.61 us: 1.02x slower                                         |
| scimark_monte_carlo      | 53.6 ms                                                               | 54.7 ms: 1.02x slower                                         |
| generators               | 28.4 ms                                                               | 29.0 ms: 1.02x slower                                         |
| sqlglot_parse            | 924 us                                                                | 945 us: 1.02x slower                                          |
| xml_etree_process        | 40.8 ms                                                               | 41.7 ms: 1.02x slower                                         |
| xml_etree_generate       | 58.9 ms                                                               | 60.2 ms: 1.02x slower                                         |
| pyflate                  | 359 ms                                                                | 368 ms: 1.03x slower                                          |
| xml_etree_iterparse      | 76.6 ms                                                               | 78.6 ms: 1.03x slower                                         |
| docutils                 | 1.54 sec                                                              | 1.58 sec: 1.03x slower                                        |
| deepcopy                 | 230 us                                                                | 237 us: 1.03x slower                                          |
| tomli_loads              | 1.63 sec                                                              | 1.67 sec: 1.03x slower                                        |
| bench_mp_pool            | 45.4 ms                                                               | 46.7 ms: 1.03x slower                                         |
| async_generators         | 312 ms                                                                | 323 ms: 1.04x slower                                          |
| deltablue                | 2.83 ms                                                               | 2.93 ms: 1.04x slower                                         |
| chaos                    | 45.3 ms                                                               | 46.9 ms: 1.04x slower                                         |
| sqlglot_optimize         | 35.4 ms                                                               | 36.7 ms: 1.04x slower                                         |
| sqlglot_normalize        | 192 ms                                                                | 200 ms: 1.04x slower                                          |
| go                       | 120 ms                                                                | 125 ms: 1.04x slower                                          |
| crypto_pyaes             | 47.6 ms                                                               | 49.5 ms: 1.04x slower                                         |
| coroutines               | 19.8 ms                                                               | 20.5 ms: 1.04x slower                                         |
| float                    | 59.7 ms                                                               | 62.0 ms: 1.04x slower                                         |
| scimark_lu               | 76.3 ms                                                               | 79.4 ms: 1.04x slower                                         |
| typing_runtime_protocols | 93.4 us                                                               | 97.2 us: 1.04x slower                                         |
| unpickle_pure_python     | 164 us                                                                | 173 us: 1.05x slower                                          |
| spectral_norm            | 74.1 ms                                                               | 78.0 ms: 1.05x slower                                         |
| bench_thread_pool        | 495 us                                                                | 523 us: 1.06x slower                                          |
| nbody                    | 72.1 ms                                                               | 76.2 ms: 1.06x slower                                         |
| scimark_fft              | 201 ms                                                                | 213 ms: 1.06x slower                                          |
| mako                     | 7.61 ms                                                               | 8.08 ms: 1.06x slower                                         |
| fannkuch                 | 290 ms                                                                | 308 ms: 1.06x slower                                          |
| regex_compile            | 80.4 ms                                                               | 85.8 ms: 1.07x slower                                         |
| meteor_contest           | 75.0 ms                                                               | 80.3 ms: 1.07x slower                                         |
| mdp                      | 1.64 sec                                                              | 1.76 sec: 1.08x slower                                        |
| deepcopy_memo            | 25.6 us                                                               | 27.6 us: 1.08x slower                                         |
| hexiom                   | 4.96 ms                                                               | 5.67 ms: 1.14x slower                                         |
| nqueens                  | 59.5 ms                                                               | 68.8 ms: 1.16x slower                                         |
| comprehensions           | 15.7 us                                                               | 18.4 us: 1.17x slower                                         |
| scimark_sparse_mat_mult  | 3.14 ms                                                               | 3.77 ms: 1.20x slower                                         |
| Geometric mean           | (ref)                                                                 | 1.03x slower                                                  |

Benchmark hidden because not significant (8): asyncio_tcp, xml_etree_parse, pidigits, json, unpack_sequence, async_tree_cpu_io_mixed, tornado_http, mypy2


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x
