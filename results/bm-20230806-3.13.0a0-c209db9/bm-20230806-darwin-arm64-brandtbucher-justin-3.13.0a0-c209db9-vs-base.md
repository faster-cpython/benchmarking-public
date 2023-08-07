
# Results vs. base

- fork: brandtbucher
- ref: justin
- machine: darwin-arm64
- commit hash: c209db9
- commit date: 2023-08-06
- overall geometric mean: 1.03x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230806-darwin-arm64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-darwin-arm64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| docutils       | 1.54 sec                                                              | 1.58 sec: 1.02x slower                                        |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                  |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230806-darwin-arm64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-darwin-arm64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| pidigits       | 281 ms                                                                | 282 ms: 1.00x slower                                          |
| float          | 59.6 ms                                                               | 62.0 ms: 1.04x slower                                         |
| nbody          | 72.1 ms                                                               | 76.2 ms: 1.06x slower                                         |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230806-darwin-arm64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-darwin-arm64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_effbot   | 2.56 ms                                                               | 2.56 ms: 1.00x slower                                         |
| regex_dna      | 149 ms                                                                | 150 ms: 1.01x slower                                          |
| regex_v8       | 15.6 ms                                                               | 15.8 ms: 1.01x slower                                         |
| regex_compile  | 80.8 ms                                                               | 85.8 ms: 1.06x slower                                         |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230806-darwin-arm64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-darwin-arm64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| pickle_dict          | 17.9 us                                                               | 17.8 us: 1.01x faster                                         |
| json_loads           | 17.5 us                                                               | 17.4 us: 1.01x faster                                         |
| json_dumps           | 6.71 ms                                                               | 6.67 ms: 1.01x faster                                         |
| unpickle_list        | 3.17 us                                                               | 3.19 us: 1.01x slower                                         |
| unpickle             | 9.32 us                                                               | 9.39 us: 1.01x slower                                         |
| pickle_pure_python   | 203 us                                                                | 205 us: 1.01x slower                                          |
| xml_etree_parse      | 110 ms                                                                | 112 ms: 1.01x slower                                          |
| pickle_list          | 2.86 us                                                               | 2.90 us: 1.01x slower                                         |
| xml_etree_process    | 40.9 ms                                                               | 41.7 ms: 1.02x slower                                         |
| pickle               | 7.36 us                                                               | 7.50 us: 1.02x slower                                         |
| xml_etree_generate   | 59.0 ms                                                               | 60.2 ms: 1.02x slower                                         |
| tomli_loads          | 1.63 sec                                                              | 1.67 sec: 1.03x slower                                        |
| xml_etree_iterparse  | 75.9 ms                                                               | 78.6 ms: 1.04x slower                                         |
| unpickle_pure_python | 166 us                                                                | 173 us: 1.04x slower                                          |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                  |

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230806-darwin-arm64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-darwin-arm64-brandtbucher-justin-3.13.0a0-c209db9 |
|-----------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| mako      | 7.61 ms                                                               | 8.08 ms: 1.06x slower                                         |

All benchmarks:
===============

| Benchmark                | bm-20230806-darwin-arm64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-darwin-arm64-brandtbucher-justin-3.13.0a0-c209db9 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| asyncio_tcp              | 447 ms                                                                | 421 ms: 1.06x faster                                          |
| pathlib                  | 28.9 ms                                                               | 27.3 ms: 1.06x faster                                         |
| logging_silent           | 79.2 ns                                                               | 77.8 ns: 1.02x faster                                         |
| create_gc_cycles         | 710 us                                                                | 699 us: 1.01x faster                                          |
| telco                    | 4.62 ms                                                               | 4.57 ms: 1.01x faster                                         |
| pickle_dict              | 17.9 us                                                               | 17.8 us: 1.01x faster                                         |
| json_loads               | 17.5 us                                                               | 17.4 us: 1.01x faster                                         |
| json_dumps               | 6.71 ms                                                               | 6.67 ms: 1.01x faster                                         |
| gc_traversal             | 2.40 ms                                                               | 2.39 ms: 1.00x faster                                         |
| pidigits                 | 281 ms                                                                | 282 ms: 1.00x slower                                          |
| regex_effbot             | 2.56 ms                                                               | 2.56 ms: 1.00x slower                                         |
| logging_simple           | 3.85 us                                                               | 3.87 us: 1.00x slower                                         |
| async_tree_io            | 679 ms                                                                | 683 ms: 1.01x slower                                          |
| async_tree_memoization   | 323 ms                                                                | 325 ms: 1.01x slower                                          |
| unpickle_list            | 3.17 us                                                               | 3.19 us: 1.01x slower                                         |
| logging_format           | 4.13 us                                                               | 4.16 us: 1.01x slower                                         |
| unpickle                 | 9.32 us                                                               | 9.39 us: 1.01x slower                                         |
| regex_dna                | 149 ms                                                                | 150 ms: 1.01x slower                                          |
| pickle_pure_python       | 203 us                                                                | 205 us: 1.01x slower                                          |
| sqlite_synth             | 1.60 us                                                               | 1.61 us: 1.01x slower                                         |
| regex_v8                 | 15.6 ms                                                               | 15.8 ms: 1.01x slower                                         |
| pprint_safe_repr         | 517 ms                                                                | 522 ms: 1.01x slower                                          |
| pprint_pformat           | 1.06 sec                                                              | 1.07 sec: 1.01x slower                                        |
| dask                     | 340 ms                                                                | 344 ms: 1.01x slower                                          |
| xml_etree_parse          | 110 ms                                                                | 112 ms: 1.01x slower                                          |
| deepcopy_reduce          | 2.08 us                                                               | 2.11 us: 1.01x slower                                         |
| raytrace                 | 230 ms                                                                | 233 ms: 1.01x slower                                          |
| pickle_list              | 2.86 us                                                               | 2.90 us: 1.01x slower                                         |
| richards_super           | 40.9 ms                                                               | 41.5 ms: 1.02x slower                                         |
| dulwich_log              | 31.3 ms                                                               | 31.8 ms: 1.02x slower                                         |
| scimark_sor              | 118 ms                                                                | 120 ms: 1.02x slower                                          |
| scimark_monte_carlo      | 53.9 ms                                                               | 54.7 ms: 1.02x slower                                         |
| pycparser                | 711 ms                                                                | 722 ms: 1.02x slower                                          |
| xml_etree_process        | 40.9 ms                                                               | 41.7 ms: 1.02x slower                                         |
| richards                 | 37.1 ms                                                               | 37.8 ms: 1.02x slower                                         |
| pickle                   | 7.36 us                                                               | 7.50 us: 1.02x slower                                         |
| sqlglot_parse            | 926 us                                                                | 945 us: 1.02x slower                                          |
| xml_etree_generate       | 59.0 ms                                                               | 60.2 ms: 1.02x slower                                         |
| generators               | 28.4 ms                                                               | 29.0 ms: 1.02x slower                                         |
| sqlglot_transpile        | 1.11 ms                                                               | 1.13 ms: 1.02x slower                                         |
| pyflate                  | 361 ms                                                                | 368 ms: 1.02x slower                                          |
| deepcopy                 | 231 us                                                                | 237 us: 1.02x slower                                          |
| docutils                 | 1.54 sec                                                              | 1.58 sec: 1.02x slower                                        |
| typing_runtime_protocols | 94.7 us                                                               | 97.2 us: 1.03x slower                                         |
| tomli_loads              | 1.63 sec                                                              | 1.67 sec: 1.03x slower                                        |
| scimark_lu               | 77.0 ms                                                               | 79.4 ms: 1.03x slower                                         |
| bench_mp_pool            | 45.2 ms                                                               | 46.7 ms: 1.03x slower                                         |
| deltablue                | 2.83 ms                                                               | 2.93 ms: 1.03x slower                                         |
| xml_etree_iterparse      | 75.9 ms                                                               | 78.6 ms: 1.04x slower                                         |
| chaos                    | 45.3 ms                                                               | 46.9 ms: 1.04x slower                                         |
| sqlglot_optimize         | 35.5 ms                                                               | 36.7 ms: 1.04x slower                                         |
| go                       | 120 ms                                                                | 125 ms: 1.04x slower                                          |
| async_generators         | 312 ms                                                                | 323 ms: 1.04x slower                                          |
| sqlglot_normalize        | 192 ms                                                                | 200 ms: 1.04x slower                                          |
| crypto_pyaes             | 47.6 ms                                                               | 49.5 ms: 1.04x slower                                         |
| float                    | 59.6 ms                                                               | 62.0 ms: 1.04x slower                                         |
| coroutines               | 19.7 ms                                                               | 20.5 ms: 1.04x slower                                         |
| unpickle_pure_python     | 166 us                                                                | 173 us: 1.04x slower                                          |
| bench_thread_pool        | 498 us                                                                | 523 us: 1.05x slower                                          |
| spectral_norm            | 74.2 ms                                                               | 78.0 ms: 1.05x slower                                         |
| nbody                    | 72.1 ms                                                               | 76.2 ms: 1.06x slower                                         |
| scimark_fft              | 201 ms                                                                | 213 ms: 1.06x slower                                          |
| regex_compile            | 80.8 ms                                                               | 85.8 ms: 1.06x slower                                         |
| fannkuch                 | 290 ms                                                                | 308 ms: 1.06x slower                                          |
| mako                     | 7.61 ms                                                               | 8.08 ms: 1.06x slower                                         |
| mdp                      | 1.66 sec                                                              | 1.76 sec: 1.06x slower                                        |
| meteor_contest           | 74.8 ms                                                               | 80.3 ms: 1.07x slower                                         |
| deepcopy_memo            | 25.7 us                                                               | 27.6 us: 1.08x slower                                         |
| hexiom                   | 4.97 ms                                                               | 5.67 ms: 1.14x slower                                         |
| nqueens                  | 59.7 ms                                                               | 68.8 ms: 1.15x slower                                         |
| comprehensions           | 15.8 us                                                               | 18.4 us: 1.16x slower                                         |
| scimark_sparse_mat_mult  | 3.14 ms                                                               | 3.77 ms: 1.20x slower                                         |
| Geometric mean           | (ref)                                                                 | 1.03x slower                                                  |

Benchmark hidden because not significant (10): asyncio_tcp_ssl, coverage, json, python_startup_no_site, python_startup, async_tree_cpu_io_mixed, async_tree_none, unpack_sequence, tornado_http, mypy2
