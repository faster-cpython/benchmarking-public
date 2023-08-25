
# Results vs. base

- fork: brandtbucher
- ref: uops_enabled
- machine: darwin-arm64
- commit hash: 9016d52
- commit date: 2023-08-06
- overall geometric mean: 1.04x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230806-darwin-arm64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-darwin-arm64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| docutils       | 1.54 sec                                                              | 1.59 sec: 1.03x slower                                              |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                        |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230806-darwin-arm64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-darwin-arm64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 59.7 ms                                                               | 63.7 ms: 1.07x slower                                               |
| nbody          | 72.1 ms                                                               | 77.5 ms: 1.07x slower                                               |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                        |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230806-darwin-arm64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-darwin-arm64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 2.54 ms                                                               | 2.56 ms: 1.01x slower                                               |
| regex_dna      | 149 ms                                                                | 151 ms: 1.01x slower                                                |
| regex_v8       | 15.6 ms                                                               | 16.0 ms: 1.03x slower                                               |
| regex_compile  | 80.4 ms                                                               | 88.7 ms: 1.10x slower                                               |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230806-darwin-arm64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-darwin-arm64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_dict          | 18.1 us                                                               | 17.9 us: 1.01x faster                                               |
| pickle               | 7.38 us                                                               | 7.42 us: 1.01x slower                                               |
| unpickle_list        | 3.16 us                                                               | 3.18 us: 1.01x slower                                               |
| json_dumps           | 6.70 ms                                                               | 6.76 ms: 1.01x slower                                               |
| pickle_pure_python   | 203 us                                                                | 206 us: 1.02x slower                                                |
| xml_etree_iterparse  | 76.6 ms                                                               | 78.9 ms: 1.03x slower                                               |
| pickle_list          | 2.85 us                                                               | 2.94 us: 1.03x slower                                               |
| xml_etree_process    | 40.8 ms                                                               | 42.3 ms: 1.04x slower                                               |
| unpickle_pure_python | 164 us                                                                | 173 us: 1.05x slower                                                |
| xml_etree_generate   | 58.9 ms                                                               | 62.0 ms: 1.05x slower                                               |
| tomli_loads          | 1.63 sec                                                              | 1.84 sec: 1.13x slower                                              |
| Geometric mean       | (ref)                                                                 | 1.02x slower                                                        |

Benchmark hidden because not significant (3): xml_etree_parse, json_loads, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230806-darwin-arm64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-darwin-arm64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 11.3 ms                                                               | 11.2 ms: 1.00x faster                                               |
| python_startup_no_site | 9.12 ms                                                               | 9.18 ms: 1.01x slower                                               |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230806-darwin-arm64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-darwin-arm64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|-----------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako      | 7.61 ms                                                               | 8.68 ms: 1.14x slower                                               |

All benchmarks:
===============

| Benchmark                | bm-20230806-darwin-arm64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-darwin-arm64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pathlib                  | 31.2 ms                                                               | 28.7 ms: 1.09x faster                                               |
| gc_traversal             | 2.54 ms                                                               | 2.40 ms: 1.06x faster                                               |
| pickle_dict              | 18.1 us                                                               | 17.9 us: 1.01x faster                                               |
| create_gc_cycles         | 709 us                                                                | 703 us: 1.01x faster                                                |
| telco                    | 4.62 ms                                                               | 4.60 ms: 1.01x faster                                               |
| python_startup           | 11.3 ms                                                               | 11.2 ms: 1.00x faster                                               |
| regex_effbot             | 2.54 ms                                                               | 2.56 ms: 1.01x slower                                               |
| pickle                   | 7.38 us                                                               | 7.42 us: 1.01x slower                                               |
| bench_mp_pool            | 45.4 ms                                                               | 45.7 ms: 1.01x slower                                               |
| unpickle_list            | 3.16 us                                                               | 3.18 us: 1.01x slower                                               |
| python_startup_no_site   | 9.12 ms                                                               | 9.18 ms: 1.01x slower                                               |
| json                     | 2.98 ms                                                               | 3.00 ms: 1.01x slower                                               |
| json_dumps               | 6.70 ms                                                               | 6.76 ms: 1.01x slower                                               |
| generators               | 28.4 ms                                                               | 28.7 ms: 1.01x slower                                               |
| async_tree_io            | 680 ms                                                                | 686 ms: 1.01x slower                                                |
| regex_dna                | 149 ms                                                                | 151 ms: 1.01x slower                                                |
| deepcopy_reduce          | 2.09 us                                                               | 2.12 us: 1.01x slower                                               |
| async_tree_none          | 274 ms                                                                | 278 ms: 1.01x slower                                                |
| logging_format           | 4.11 us                                                               | 4.18 us: 1.02x slower                                               |
| dulwich_log              | 31.3 ms                                                               | 31.8 ms: 1.02x slower                                               |
| dask                     | 339 ms                                                                | 345 ms: 1.02x slower                                                |
| logging_simple           | 3.85 us                                                               | 3.91 us: 1.02x slower                                               |
| pickle_pure_python       | 203 us                                                                | 206 us: 1.02x slower                                                |
| logging_silent           | 76.8 ns                                                               | 78.2 ns: 1.02x slower                                               |
| scimark_monte_carlo      | 53.6 ms                                                               | 54.6 ms: 1.02x slower                                               |
| async_tree_memoization   | 323 ms                                                                | 329 ms: 1.02x slower                                                |
| scimark_sor              | 118 ms                                                                | 121 ms: 1.02x slower                                                |
| sqlglot_parse            | 924 us                                                                | 947 us: 1.02x slower                                                |
| sqlglot_transpile        | 1.11 ms                                                               | 1.14 ms: 1.03x slower                                               |
| regex_v8                 | 15.6 ms                                                               | 16.0 ms: 1.03x slower                                               |
| richards_super           | 40.9 ms                                                               | 42.0 ms: 1.03x slower                                               |
| pycparser                | 709 ms                                                                | 730 ms: 1.03x slower                                                |
| richards                 | 37.2 ms                                                               | 38.3 ms: 1.03x slower                                               |
| xml_etree_iterparse      | 76.6 ms                                                               | 78.9 ms: 1.03x slower                                               |
| docutils                 | 1.54 sec                                                              | 1.59 sec: 1.03x slower                                              |
| raytrace                 | 230 ms                                                                | 237 ms: 1.03x slower                                                |
| pickle_list              | 2.85 us                                                               | 2.94 us: 1.03x slower                                               |
| deepcopy                 | 230 us                                                                | 238 us: 1.03x slower                                                |
| pprint_safe_repr         | 515 ms                                                                | 533 ms: 1.03x slower                                                |
| async_generators         | 312 ms                                                                | 323 ms: 1.04x slower                                                |
| sqlite_synth             | 1.58 us                                                               | 1.64 us: 1.04x slower                                               |
| pprint_pformat           | 1.05 sec                                                              | 1.09 sec: 1.04x slower                                              |
| xml_etree_process        | 40.8 ms                                                               | 42.3 ms: 1.04x slower                                               |
| coroutines               | 19.8 ms                                                               | 20.6 ms: 1.04x slower                                               |
| sqlglot_optimize         | 35.4 ms                                                               | 36.9 ms: 1.04x slower                                               |
| sqlglot_normalize        | 192 ms                                                                | 201 ms: 1.04x slower                                                |
| unpickle_pure_python     | 164 us                                                                | 173 us: 1.05x slower                                                |
| xml_etree_generate       | 58.9 ms                                                               | 62.0 ms: 1.05x slower                                               |
| go                       | 120 ms                                                                | 127 ms: 1.05x slower                                                |
| spectral_norm            | 74.1 ms                                                               | 78.2 ms: 1.05x slower                                               |
| crypto_pyaes             | 47.6 ms                                                               | 50.4 ms: 1.06x slower                                               |
| typing_runtime_protocols | 93.4 us                                                               | 99.1 us: 1.06x slower                                               |
| chaos                    | 45.3 ms                                                               | 48.1 ms: 1.06x slower                                               |
| deltablue                | 2.83 ms                                                               | 3.00 ms: 1.06x slower                                               |
| bench_thread_pool        | 495 us                                                                | 527 us: 1.06x slower                                                |
| float                    | 59.7 ms                                                               | 63.7 ms: 1.07x slower                                               |
| scimark_lu               | 76.3 ms                                                               | 81.6 ms: 1.07x slower                                               |
| mdp                      | 1.64 sec                                                              | 1.75 sec: 1.07x slower                                              |
| nbody                    | 72.1 ms                                                               | 77.5 ms: 1.07x slower                                               |
| pyflate                  | 359 ms                                                                | 387 ms: 1.08x slower                                                |
| scimark_fft              | 201 ms                                                                | 222 ms: 1.10x slower                                                |
| regex_compile            | 80.4 ms                                                               | 88.7 ms: 1.10x slower                                               |
| meteor_contest           | 75.0 ms                                                               | 82.9 ms: 1.11x slower                                               |
| tomli_loads              | 1.63 sec                                                              | 1.84 sec: 1.13x slower                                              |
| mako                     | 7.61 ms                                                               | 8.68 ms: 1.14x slower                                               |
| deepcopy_memo            | 25.6 us                                                               | 29.4 us: 1.15x slower                                               |
| fannkuch                 | 290 ms                                                                | 341 ms: 1.18x slower                                                |
| nqueens                  | 59.5 ms                                                               | 73.0 ms: 1.23x slower                                               |
| comprehensions           | 15.7 us                                                               | 19.4 us: 1.24x slower                                               |
| hexiom                   | 4.96 ms                                                               | 6.15 ms: 1.24x slower                                               |
| scimark_sparse_mat_mult  | 3.14 ms                                                               | 4.24 ms: 1.35x slower                                               |
| Geometric mean           | (ref)                                                                 | 1.04x slower                                                        |

Benchmark hidden because not significant (11): xml_etree_parse, asyncio_tcp_ssl, pidigits, json_loads, coverage, unpickle, unpack_sequence, asyncio_tcp, async_tree_cpu_io_mixed, mypy2, tornado_http


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.02x
