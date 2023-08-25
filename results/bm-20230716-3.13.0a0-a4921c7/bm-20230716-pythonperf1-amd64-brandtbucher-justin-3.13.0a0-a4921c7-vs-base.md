
# Results vs. base

- fork: brandtbucher
- ref: justin
- machine: windows-amd64
- commit hash: a4921c7
- commit date: 2023-07-16
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230602-pythonperf1-amd64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230716-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-a4921c7 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| docutils       | 1.61 sec                                                                   | 1.64 sec: 1.02x slower                                             |
| tornado_http   | 87.1 ms                                                                    | 89.6 ms: 1.03x slower                                              |
| Geometric mean | (ref)                                                                      | 1.02x slower                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230602-pythonperf1-amd64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230716-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-a4921c7 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 53.4 ms                                                                    | 52.0 ms: 1.03x faster                                              |
| pidigits       | 150 ms                                                                     | 151 ms: 1.01x slower                                               |
| nbody          | 67.2 ms                                                                    | 72.1 ms: 1.07x slower                                              |
| Geometric mean | (ref)                                                                      | 1.02x slower                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230602-pythonperf1-amd64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230716-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-a4921c7 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_dna      | 117 ms                                                                     | 116 ms: 1.01x faster                                               |
| regex_effbot   | 1.57 ms                                                                    | 1.56 ms: 1.01x faster                                              |
| regex_compile  | 85.9 ms                                                                    | 88.7 ms: 1.03x slower                                              |
| regex_v8       | 13.2 ms                                                                    | 24.0 ms: 1.82x slower                                              |
| Geometric mean | (ref)                                                                      | 1.17x slower                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230602-pythonperf1-amd64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230716-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-a4921c7 |
|----------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| pickle               | 7.33 us                                                                    | 7.15 us: 1.03x faster                                              |
| json_loads           | 13.7 us                                                                    | 13.5 us: 1.01x faster                                              |
| unpickle             | 8.19 us                                                                    | 8.26 us: 1.01x slower                                              |
| xml_etree_iterparse  | 63.3 ms                                                                    | 64.0 ms: 1.01x slower                                              |
| unpickle_list        | 2.79 us                                                                    | 2.84 us: 1.02x slower                                              |
| pickle_list          | 2.87 us                                                                    | 2.92 us: 1.02x slower                                              |
| xml_etree_generate   | 55.4 ms                                                                    | 56.8 ms: 1.02x slower                                              |
| pickle_dict          | 18.6 us                                                                    | 19.1 us: 1.03x slower                                              |
| pickle_pure_python   | 189 us                                                                     | 196 us: 1.03x slower                                               |
| json_dumps           | 5.53 ms                                                                    | 5.78 ms: 1.05x slower                                              |
| xml_etree_process    | 37.4 ms                                                                    | 39.2 ms: 1.05x slower                                              |
| tomli_loads          | 1.34 sec                                                                   | 1.41 sec: 1.06x slower                                             |
| unpickle_pure_python | 128 us                                                                     | 136 us: 1.07x slower                                               |
| Geometric mean       | (ref)                                                                      | 1.02x slower                                                       |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230602-pythonperf1-amd64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230716-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-a4921c7 |
|------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 18.6 ms                                                                    | 22.2 ms: 1.19x slower                                              |
| python_startup_no_site | 15.9 ms                                                                    | 19.3 ms: 1.21x slower                                              |
| Geometric mean         | (ref)                                                                      | 1.20x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230602-pythonperf1-amd64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230716-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-a4921c7 |
|-----------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| mako      | 6.69 ms                                                                    | 7.39 ms: 1.10x slower                                              |

All benchmarks:
===============

| Benchmark                | bm-20230602-pythonperf1-amd64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230716-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-a4921c7 |
|--------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| json                     | 2.98 ms                                                                    | 2.87 ms: 1.04x faster                                              |
| float                    | 53.4 ms                                                                    | 52.0 ms: 1.03x faster                                              |
| pickle                   | 7.33 us                                                                    | 7.15 us: 1.03x faster                                              |
| mdp                      | 1.42 sec                                                                   | 1.40 sec: 1.02x faster                                             |
| json_loads               | 13.7 us                                                                    | 13.5 us: 1.01x faster                                              |
| async_generators         | 242 ms                                                                     | 239 ms: 1.01x faster                                               |
| regex_dna                | 117 ms                                                                     | 116 ms: 1.01x faster                                               |
| regex_effbot             | 1.57 ms                                                                    | 1.56 ms: 1.01x faster                                              |
| sqlite_synth             | 1.73 us                                                                    | 1.74 us: 1.01x slower                                              |
| pidigits                 | 150 ms                                                                     | 151 ms: 1.01x slower                                               |
| unpickle                 | 8.19 us                                                                    | 8.26 us: 1.01x slower                                              |
| scimark_monte_carlo      | 42.3 ms                                                                    | 42.8 ms: 1.01x slower                                              |
| dask                     | 360 ms                                                                     | 363 ms: 1.01x slower                                               |
| xml_etree_iterparse      | 63.3 ms                                                                    | 64.0 ms: 1.01x slower                                              |
| richards_super           | 29.7 ms                                                                    | 30.1 ms: 1.01x slower                                              |
| scimark_sparse_mat_mult  | 2.45 ms                                                                    | 2.48 ms: 1.01x slower                                              |
| telco                    | 4.05 ms                                                                    | 4.11 ms: 1.01x slower                                              |
| pycparser                | 674 ms                                                                     | 685 ms: 1.02x slower                                               |
| pathlib                  | 79.0 ms                                                                    | 80.3 ms: 1.02x slower                                              |
| docutils                 | 1.61 sec                                                                   | 1.64 sec: 1.02x slower                                             |
| unpickle_list            | 2.79 us                                                                    | 2.84 us: 1.02x slower                                              |
| mypy2                    | 211 ms                                                                     | 215 ms: 1.02x slower                                               |
| pickle_list              | 2.87 us                                                                    | 2.92 us: 1.02x slower                                              |
| coverage                 | 52.3 ms                                                                    | 53.3 ms: 1.02x slower                                              |
| deepcopy_reduce          | 2.07 us                                                                    | 2.11 us: 1.02x slower                                              |
| xml_etree_generate       | 55.4 ms                                                                    | 56.8 ms: 1.02x slower                                              |
| async_tree_none          | 287 ms                                                                     | 294 ms: 1.02x slower                                               |
| pickle_dict              | 18.6 us                                                                    | 19.1 us: 1.03x slower                                              |
| richards                 | 25.8 ms                                                                    | 26.5 ms: 1.03x slower                                              |
| scimark_sor              | 77.5 ms                                                                    | 79.6 ms: 1.03x slower                                              |
| tornado_http             | 87.1 ms                                                                    | 89.6 ms: 1.03x slower                                              |
| bench_thread_pool        | 809 us                                                                     | 832 us: 1.03x slower                                               |
| sqlglot_optimize         | 33.7 ms                                                                    | 34.8 ms: 1.03x slower                                              |
| unpack_sequence          | 36.6 ns                                                                    | 37.8 ns: 1.03x slower                                              |
| sqlglot_normalize        | 182 ms                                                                     | 188 ms: 1.03x slower                                               |
| regex_compile            | 85.9 ms                                                                    | 88.7 ms: 1.03x slower                                              |
| deepcopy                 | 233 us                                                                     | 240 us: 1.03x slower                                               |
| pyflate                  | 291 ms                                                                     | 301 ms: 1.03x slower                                               |
| pickle_pure_python       | 189 us                                                                     | 196 us: 1.03x slower                                               |
| meteor_contest           | 72.8 ms                                                                    | 75.4 ms: 1.04x slower                                              |
| scimark_fft              | 175 ms                                                                     | 181 ms: 1.04x slower                                               |
| spectral_norm            | 63.4 ms                                                                    | 66.0 ms: 1.04x slower                                              |
| logging_format           | 6.73 us                                                                    | 7.01 us: 1.04x slower                                              |
| pprint_safe_repr         | 497 ms                                                                     | 520 ms: 1.05x slower                                               |
| json_dumps               | 5.53 ms                                                                    | 5.78 ms: 1.05x slower                                              |
| raytrace                 | 188 ms                                                                     | 197 ms: 1.05x slower                                               |
| xml_etree_process        | 37.4 ms                                                                    | 39.2 ms: 1.05x slower                                              |
| go                       | 87.0 ms                                                                    | 91.4 ms: 1.05x slower                                              |
| pprint_pformat           | 1.01 sec                                                                   | 1.06 sec: 1.05x slower                                             |
| fannkuch                 | 242 ms                                                                     | 255 ms: 1.05x slower                                               |
| logging_silent           | 59.8 ns                                                                    | 62.9 ns: 1.05x slower                                              |
| logging_simple           | 6.24 us                                                                    | 6.58 us: 1.05x slower                                              |
| nqueens                  | 60.6 ms                                                                    | 63.9 ms: 1.05x slower                                              |
| tomli_loads              | 1.34 sec                                                                   | 1.41 sec: 1.06x slower                                             |
| sqlglot_transpile        | 1.00 ms                                                                    | 1.06 ms: 1.06x slower                                              |
| chaos                    | 41.8 ms                                                                    | 44.2 ms: 1.06x slower                                              |
| coroutines               | 14.0 ms                                                                    | 14.8 ms: 1.06x slower                                              |
| typing_runtime_protocols | 91.5 us                                                                    | 97.3 us: 1.06x slower                                              |
| bench_mp_pool            | 65.8 ms                                                                    | 70.0 ms: 1.06x slower                                              |
| unpickle_pure_python     | 128 us                                                                     | 136 us: 1.07x slower                                               |
| sqlglot_parse            | 786 us                                                                     | 842 us: 1.07x slower                                               |
| nbody                    | 67.2 ms                                                                    | 72.1 ms: 1.07x slower                                              |
| deltablue                | 2.12 ms                                                                    | 2.31 ms: 1.09x slower                                              |
| mako                     | 6.69 ms                                                                    | 7.39 ms: 1.10x slower                                              |
| comprehensions           | 14.0 us                                                                    | 15.5 us: 1.11x slower                                              |
| generators               | 21.4 ms                                                                    | 23.9 ms: 1.12x slower                                              |
| hexiom                   | 4.00 ms                                                                    | 4.62 ms: 1.16x slower                                              |
| deepcopy_memo            | 23.5 us                                                                    | 27.2 us: 1.16x slower                                              |
| crypto_pyaes             | 46.0 ms                                                                    | 53.6 ms: 1.16x slower                                              |
| python_startup           | 18.6 ms                                                                    | 22.2 ms: 1.19x slower                                              |
| python_startup_no_site   | 15.9 ms                                                                    | 19.3 ms: 1.21x slower                                              |
| scimark_lu               | 55.8 ms                                                                    | 70.3 ms: 1.26x slower                                              |
| regex_v8                 | 13.2 ms                                                                    | 24.0 ms: 1.82x slower                                              |
| Geometric mean           | (ref)                                                                      | 1.05x slower                                                       |

Benchmark hidden because not significant (9): asyncio_tcp_ssl, gc_traversal, dulwich_log, async_tree_io, xml_etree_parse, create_gc_cycles, async_tree_cpu_io_mixed, async_tree_memoization, asyncio_tcp


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x
