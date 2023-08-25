
# Results vs. base

- fork: brandtbucher
- ref: justin
- machine: windows-amd64
- commit hash: ba47232
- commit date: 2023-07-17
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230602-pythonperf1-amd64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230717-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-ba47232 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| docutils       | 1.61 sec                                                                   | 1.62 sec: 1.01x slower                                             |
| tornado_http   | 87.1 ms                                                                    | 88.6 ms: 1.02x slower                                              |
| Geometric mean | (ref)                                                                      | 1.01x slower                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230602-pythonperf1-amd64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230717-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-ba47232 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 53.4 ms                                                                    | 50.5 ms: 1.06x faster                                              |
| pidigits       | 150 ms                                                                     | 150 ms: 1.00x slower                                               |
| nbody          | 67.2 ms                                                                    | 72.3 ms: 1.08x slower                                              |
| Geometric mean | (ref)                                                                      | 1.01x slower                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230602-pythonperf1-amd64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230717-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-ba47232 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 85.9 ms                                                                    | 88.6 ms: 1.03x slower                                              |
| regex_effbot   | 1.57 ms                                                                    | 1.63 ms: 1.04x slower                                              |
| regex_dna      | 117 ms                                                                     | 126 ms: 1.08x slower                                               |
| regex_v8       | 13.2 ms                                                                    | 26.0 ms: 1.97x slower                                              |
| Geometric mean | (ref)                                                                      | 1.23x slower                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230602-pythonperf1-amd64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230717-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-ba47232 |
|----------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| pickle               | 7.33 us                                                                    | 7.20 us: 1.02x faster                                              |
| pickle_dict          | 18.6 us                                                                    | 18.5 us: 1.01x faster                                              |
| tomli_loads          | 1.34 sec                                                                   | 1.36 sec: 1.01x slower                                             |
| unpickle             | 8.19 us                                                                    | 8.30 us: 1.01x slower                                              |
| xml_etree_iterparse  | 63.3 ms                                                                    | 64.6 ms: 1.02x slower                                              |
| json_dumps           | 5.53 ms                                                                    | 5.67 ms: 1.03x slower                                              |
| xml_etree_process    | 37.4 ms                                                                    | 38.4 ms: 1.03x slower                                              |
| unpickle_list        | 2.79 us                                                                    | 2.89 us: 1.04x slower                                              |
| pickle_pure_python   | 189 us                                                                     | 197 us: 1.04x slower                                               |
| unpickle_pure_python | 128 us                                                                     | 137 us: 1.07x slower                                               |
| Geometric mean       | (ref)                                                                      | 1.02x slower                                                       |

Benchmark hidden because not significant (4): pickle_list, xml_etree_generate, json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230602-pythonperf1-amd64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230717-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-ba47232 |
|------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 18.6 ms                                                                    | 21.1 ms: 1.13x slower                                              |
| python_startup_no_site | 15.9 ms                                                                    | 18.1 ms: 1.14x slower                                              |
| Geometric mean         | (ref)                                                                      | 1.14x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230602-pythonperf1-amd64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230717-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-ba47232 |
|-----------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| mako      | 6.69 ms                                                                    | 6.42 ms: 1.04x faster                                              |

All benchmarks:
===============

| Benchmark                | bm-20230602-pythonperf1-amd64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230717-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-ba47232 |
|--------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| float                    | 53.4 ms                                                                    | 50.5 ms: 1.06x faster                                              |
| mako                     | 6.69 ms                                                                    | 6.42 ms: 1.04x faster                                              |
| json                     | 2.98 ms                                                                    | 2.88 ms: 1.04x faster                                              |
| coverage                 | 52.3 ms                                                                    | 50.8 ms: 1.03x faster                                              |
| pyflate                  | 291 ms                                                                     | 286 ms: 1.02x faster                                               |
| pickle                   | 7.33 us                                                                    | 7.20 us: 1.02x faster                                              |
| gc_traversal             | 1.49 ms                                                                    | 1.47 ms: 1.01x faster                                              |
| telco                    | 4.05 ms                                                                    | 4.02 ms: 1.01x faster                                              |
| pickle_dict              | 18.6 us                                                                    | 18.5 us: 1.01x faster                                              |
| richards_super           | 29.7 ms                                                                    | 29.6 ms: 1.00x faster                                              |
| sqlite_synth             | 1.73 us                                                                    | 1.72 us: 1.00x faster                                              |
| pidigits                 | 150 ms                                                                     | 150 ms: 1.00x slower                                               |
| docutils                 | 1.61 sec                                                                   | 1.62 sec: 1.01x slower                                             |
| deepcopy_reduce          | 2.07 us                                                                    | 2.08 us: 1.01x slower                                              |
| fannkuch                 | 242 ms                                                                     | 245 ms: 1.01x slower                                               |
| async_generators         | 242 ms                                                                     | 244 ms: 1.01x slower                                               |
| dask                     | 360 ms                                                                     | 364 ms: 1.01x slower                                               |
| richards                 | 25.8 ms                                                                    | 26.1 ms: 1.01x slower                                              |
| pycparser                | 674 ms                                                                     | 683 ms: 1.01x slower                                               |
| tomli_loads              | 1.34 sec                                                                   | 1.36 sec: 1.01x slower                                             |
| unpickle                 | 8.19 us                                                                    | 8.30 us: 1.01x slower                                              |
| async_tree_memoization   | 340 ms                                                                     | 344 ms: 1.01x slower                                               |
| dulwich_log              | 42.9 ms                                                                    | 43.6 ms: 1.02x slower                                              |
| tornado_http             | 87.1 ms                                                                    | 88.6 ms: 1.02x slower                                              |
| go                       | 87.0 ms                                                                    | 88.5 ms: 1.02x slower                                              |
| scimark_lu               | 55.8 ms                                                                    | 56.8 ms: 1.02x slower                                              |
| mypy2                    | 211 ms                                                                     | 215 ms: 1.02x slower                                               |
| async_tree_none          | 287 ms                                                                     | 293 ms: 1.02x slower                                               |
| xml_etree_iterparse      | 63.3 ms                                                                    | 64.6 ms: 1.02x slower                                              |
| unpack_sequence          | 36.6 ns                                                                    | 37.4 ns: 1.02x slower                                              |
| pprint_safe_repr         | 497 ms                                                                     | 509 ms: 1.02x slower                                               |
| sqlglot_optimize         | 33.7 ms                                                                    | 34.5 ms: 1.02x slower                                              |
| scimark_sparse_mat_mult  | 2.45 ms                                                                    | 2.51 ms: 1.02x slower                                              |
| bench_thread_pool        | 809 us                                                                     | 829 us: 1.02x slower                                               |
| comprehensions           | 14.0 us                                                                    | 14.3 us: 1.03x slower                                              |
| scimark_monte_carlo      | 42.3 ms                                                                    | 43.4 ms: 1.03x slower                                              |
| logging_format           | 6.73 us                                                                    | 6.90 us: 1.03x slower                                              |
| json_dumps               | 5.53 ms                                                                    | 5.67 ms: 1.03x slower                                              |
| pprint_pformat           | 1.01 sec                                                                   | 1.04 sec: 1.03x slower                                             |
| xml_etree_process        | 37.4 ms                                                                    | 38.4 ms: 1.03x slower                                              |
| sqlglot_normalize        | 182 ms                                                                     | 187 ms: 1.03x slower                                               |
| meteor_contest           | 72.8 ms                                                                    | 75.1 ms: 1.03x slower                                              |
| regex_compile            | 85.9 ms                                                                    | 88.6 ms: 1.03x slower                                              |
| raytrace                 | 188 ms                                                                     | 195 ms: 1.03x slower                                               |
| spectral_norm            | 63.4 ms                                                                    | 65.5 ms: 1.03x slower                                              |
| sqlglot_transpile        | 1.00 ms                                                                    | 1.04 ms: 1.03x slower                                              |
| deepcopy                 | 233 us                                                                     | 241 us: 1.03x slower                                               |
| logging_silent           | 59.8 ns                                                                    | 61.8 ns: 1.03x slower                                              |
| logging_simple           | 6.24 us                                                                    | 6.46 us: 1.03x slower                                              |
| nqueens                  | 60.6 ms                                                                    | 62.7 ms: 1.04x slower                                              |
| unpickle_list            | 2.79 us                                                                    | 2.89 us: 1.04x slower                                              |
| scimark_fft              | 175 ms                                                                     | 181 ms: 1.04x slower                                               |
| regex_effbot             | 1.57 ms                                                                    | 1.63 ms: 1.04x slower                                              |
| pickle_pure_python       | 189 us                                                                     | 197 us: 1.04x slower                                               |
| sqlglot_parse            | 786 us                                                                     | 821 us: 1.04x slower                                               |
| coroutines               | 14.0 ms                                                                    | 14.7 ms: 1.05x slower                                              |
| chaos                    | 41.8 ms                                                                    | 44.1 ms: 1.05x slower                                              |
| bench_mp_pool            | 65.8 ms                                                                    | 69.6 ms: 1.06x slower                                              |
| mdp                      | 1.42 sec                                                                   | 1.51 sec: 1.06x slower                                             |
| scimark_sor              | 77.5 ms                                                                    | 82.3 ms: 1.06x slower                                              |
| typing_runtime_protocols | 91.5 us                                                                    | 97.8 us: 1.07x slower                                              |
| unpickle_pure_python     | 128 us                                                                     | 137 us: 1.07x slower                                               |
| generators               | 21.4 ms                                                                    | 23.0 ms: 1.07x slower                                              |
| nbody                    | 67.2 ms                                                                    | 72.3 ms: 1.08x slower                                              |
| regex_dna                | 117 ms                                                                     | 126 ms: 1.08x slower                                               |
| crypto_pyaes             | 46.0 ms                                                                    | 50.5 ms: 1.10x slower                                              |
| hexiom                   | 4.00 ms                                                                    | 4.41 ms: 1.10x slower                                              |
| python_startup           | 18.6 ms                                                                    | 21.1 ms: 1.13x slower                                              |
| python_startup_no_site   | 15.9 ms                                                                    | 18.1 ms: 1.14x slower                                              |
| regex_v8                 | 13.2 ms                                                                    | 26.0 ms: 1.97x slower                                              |
| Geometric mean           | (ref)                                                                      | 1.03x slower                                                       |

Benchmark hidden because not significant (12): asyncio_tcp_ssl, create_gc_cycles, deepcopy_memo, pickle_list, deltablue, xml_etree_generate, async_tree_io, json_loads, xml_etree_parse, async_tree_cpu_io_mixed, pathlib, asyncio_tcp


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x
