
# Results vs. base

- fork: brandtbucher
- ref: justin
- machine: windows-amd64
- commit hash: a4921c7
- commit date: 2023-07-16
- overall geometric mean: 1.04x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230602-pythonperf1-amd64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230716-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-a4921c7 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| docutils       | 1.61 sec                                                                   | 1.64 sec: 1.02x slower                                             |
| tornado_http   | 87.5 ms                                                                    | 89.6 ms: 1.02x slower                                              |
| Geometric mean | (ref)                                                                      | 1.02x slower                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230602-pythonperf1-amd64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230716-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-a4921c7 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 54.0 ms                                                                    | 52.0 ms: 1.04x faster                                              |
| pidigits       | 150 ms                                                                     | 151 ms: 1.00x slower                                               |
| Geometric mean | (ref)                                                                      | 1.01x faster                                                       |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230602-pythonperf1-amd64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230716-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-a4921c7 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_dna      | 117 ms                                                                     | 116 ms: 1.01x faster                                               |
| regex_effbot   | 1.57 ms                                                                    | 1.56 ms: 1.00x faster                                              |
| regex_compile  | 86.7 ms                                                                    | 88.7 ms: 1.02x slower                                              |
| regex_v8       | 12.9 ms                                                                    | 24.0 ms: 1.85x slower                                              |
| Geometric mean | (ref)                                                                      | 1.17x slower                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230602-pythonperf1-amd64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230716-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-a4921c7 |
|----------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| unpickle             | 8.46 us                                                                    | 8.26 us: 1.02x faster                                              |
| unpickle_list        | 2.86 us                                                                    | 2.84 us: 1.01x faster                                              |
| json_dumps           | 5.68 ms                                                                    | 5.78 ms: 1.02x slower                                              |
| xml_etree_iterparse  | 62.7 ms                                                                    | 64.0 ms: 1.02x slower                                              |
| xml_etree_parse      | 90.8 ms                                                                    | 92.8 ms: 1.02x slower                                              |
| pickle_pure_python   | 191 us                                                                     | 196 us: 1.03x slower                                               |
| pickle               | 6.93 us                                                                    | 7.15 us: 1.03x slower                                              |
| unpickle_pure_python | 132 us                                                                     | 136 us: 1.03x slower                                               |
| pickle_list          | 2.83 us                                                                    | 2.92 us: 1.03x slower                                              |
| xml_etree_generate   | 54.8 ms                                                                    | 56.8 ms: 1.04x slower                                              |
| xml_etree_process    | 37.8 ms                                                                    | 39.2 ms: 1.04x slower                                              |
| tomli_loads          | 1.35 sec                                                                   | 1.41 sec: 1.05x slower                                             |
| pickle_dict          | 18.0 us                                                                    | 19.1 us: 1.06x slower                                              |
| Geometric mean       | (ref)                                                                      | 1.02x slower                                                       |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230602-pythonperf1-amd64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230716-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-a4921c7 |
|------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 18.2 ms                                                                    | 22.2 ms: 1.22x slower                                              |
| python_startup_no_site | 15.5 ms                                                                    | 19.3 ms: 1.25x slower                                              |
| Geometric mean         | (ref)                                                                      | 1.23x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230602-pythonperf1-amd64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230716-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-a4921c7 |
|-----------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| mako      | 6.79 ms                                                                    | 7.39 ms: 1.09x slower                                              |

All benchmarks:
===============

| Benchmark                | bm-20230602-pythonperf1-amd64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230716-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-a4921c7 |
|--------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| json                     | 3.07 ms                                                                    | 2.87 ms: 1.07x faster                                              |
| unpack_sequence          | 39.6 ns                                                                    | 37.8 ns: 1.05x faster                                              |
| float                    | 54.0 ms                                                                    | 52.0 ms: 1.04x faster                                              |
| mdp                      | 1.43 sec                                                                   | 1.40 sec: 1.02x faster                                             |
| unpickle                 | 8.46 us                                                                    | 8.26 us: 1.02x faster                                              |
| async_generators         | 242 ms                                                                     | 239 ms: 1.01x faster                                               |
| unpickle_list            | 2.86 us                                                                    | 2.84 us: 1.01x faster                                              |
| scimark_sparse_mat_mult  | 2.50 ms                                                                    | 2.48 ms: 1.01x faster                                              |
| regex_dna                | 117 ms                                                                     | 116 ms: 1.01x faster                                               |
| regex_effbot             | 1.57 ms                                                                    | 1.56 ms: 1.00x faster                                              |
| pidigits                 | 150 ms                                                                     | 151 ms: 1.00x slower                                               |
| dulwich_log              | 42.5 ms                                                                    | 42.9 ms: 1.01x slower                                              |
| fannkuch                 | 253 ms                                                                     | 255 ms: 1.01x slower                                               |
| sqlite_synth             | 1.72 us                                                                    | 1.74 us: 1.01x slower                                              |
| meteor_contest           | 74.5 ms                                                                    | 75.4 ms: 1.01x slower                                              |
| deepcopy_reduce          | 2.08 us                                                                    | 2.11 us: 1.01x slower                                              |
| pycparser                | 674 ms                                                                     | 685 ms: 1.02x slower                                               |
| docutils                 | 1.61 sec                                                                   | 1.64 sec: 1.02x slower                                             |
| spectral_norm            | 65.0 ms                                                                    | 66.0 ms: 1.02x slower                                              |
| pprint_safe_repr         | 511 ms                                                                     | 520 ms: 1.02x slower                                               |
| telco                    | 4.03 ms                                                                    | 4.11 ms: 1.02x slower                                              |
| json_dumps               | 5.68 ms                                                                    | 5.78 ms: 1.02x slower                                              |
| pathlib                  | 78.8 ms                                                                    | 80.3 ms: 1.02x slower                                              |
| scimark_sor              | 78.1 ms                                                                    | 79.6 ms: 1.02x slower                                              |
| coverage                 | 52.3 ms                                                                    | 53.3 ms: 1.02x slower                                              |
| sqlglot_optimize         | 34.1 ms                                                                    | 34.8 ms: 1.02x slower                                              |
| pprint_pformat           | 1.04 sec                                                                   | 1.06 sec: 1.02x slower                                             |
| mypy2                    | 210 ms                                                                     | 215 ms: 1.02x slower                                               |
| xml_etree_iterparse      | 62.7 ms                                                                    | 64.0 ms: 1.02x slower                                              |
| xml_etree_parse          | 90.8 ms                                                                    | 92.8 ms: 1.02x slower                                              |
| regex_compile            | 86.7 ms                                                                    | 88.7 ms: 1.02x slower                                              |
| scimark_monte_carlo      | 41.8 ms                                                                    | 42.8 ms: 1.02x slower                                              |
| tornado_http             | 87.5 ms                                                                    | 89.6 ms: 1.02x slower                                              |
| deepcopy                 | 235 us                                                                     | 240 us: 1.02x slower                                               |
| sqlglot_normalize        | 183 ms                                                                     | 188 ms: 1.02x slower                                               |
| pickle_pure_python       | 191 us                                                                     | 196 us: 1.03x slower                                               |
| richards_super           | 29.2 ms                                                                    | 30.1 ms: 1.03x slower                                              |
| logging_format           | 6.81 us                                                                    | 7.01 us: 1.03x slower                                              |
| pyflate                  | 292 ms                                                                     | 301 ms: 1.03x slower                                               |
| pickle                   | 6.93 us                                                                    | 7.15 us: 1.03x slower                                              |
| unpickle_pure_python     | 132 us                                                                     | 136 us: 1.03x slower                                               |
| pickle_list              | 2.83 us                                                                    | 2.92 us: 1.03x slower                                              |
| xml_etree_generate       | 54.8 ms                                                                    | 56.8 ms: 1.04x slower                                              |
| xml_etree_process        | 37.8 ms                                                                    | 39.2 ms: 1.04x slower                                              |
| logging_simple           | 6.34 us                                                                    | 6.58 us: 1.04x slower                                              |
| go                       | 87.6 ms                                                                    | 91.4 ms: 1.04x slower                                              |
| richards                 | 25.4 ms                                                                    | 26.5 ms: 1.04x slower                                              |
| nqueens                  | 61.0 ms                                                                    | 63.9 ms: 1.05x slower                                              |
| tomli_loads              | 1.35 sec                                                                   | 1.41 sec: 1.05x slower                                             |
| coroutines               | 14.1 ms                                                                    | 14.8 ms: 1.05x slower                                              |
| chaos                    | 42.1 ms                                                                    | 44.2 ms: 1.05x slower                                              |
| sqlglot_transpile        | 1.00 ms                                                                    | 1.06 ms: 1.05x slower                                              |
| raytrace                 | 187 ms                                                                     | 197 ms: 1.06x slower                                               |
| pickle_dict              | 18.0 us                                                                    | 19.1 us: 1.06x slower                                              |
| scimark_fft              | 171 ms                                                                     | 181 ms: 1.06x slower                                               |
| logging_silent           | 59.4 ns                                                                    | 62.9 ns: 1.06x slower                                              |
| bench_mp_pool            | 65.8 ms                                                                    | 70.0 ms: 1.06x slower                                              |
| sqlglot_parse            | 791 us                                                                     | 842 us: 1.06x slower                                               |
| typing_runtime_protocols | 91.2 us                                                                    | 97.3 us: 1.07x slower                                              |
| mako                     | 6.79 ms                                                                    | 7.39 ms: 1.09x slower                                              |
| generators               | 21.6 ms                                                                    | 23.9 ms: 1.11x slower                                              |
| deltablue                | 2.07 ms                                                                    | 2.31 ms: 1.11x slower                                              |
| comprehensions           | 13.9 us                                                                    | 15.5 us: 1.12x slower                                              |
| deepcopy_memo            | 23.9 us                                                                    | 27.2 us: 1.14x slower                                              |
| hexiom                   | 4.01 ms                                                                    | 4.62 ms: 1.15x slower                                              |
| crypto_pyaes             | 46.5 ms                                                                    | 53.6 ms: 1.15x slower                                              |
| python_startup           | 18.2 ms                                                                    | 22.2 ms: 1.22x slower                                              |
| python_startup_no_site   | 15.5 ms                                                                    | 19.3 ms: 1.25x slower                                              |
| scimark_lu               | 55.8 ms                                                                    | 70.3 ms: 1.26x slower                                              |
| regex_v8                 | 12.9 ms                                                                    | 24.0 ms: 1.85x slower                                              |
| Geometric mean           | (ref)                                                                      | 1.04x slower                                                       |

Benchmark hidden because not significant (12): create_gc_cycles, gc_traversal, asyncio_tcp, async_tree_cpu_io_mixed, nbody, json_loads, async_tree_io, bench_thread_pool, async_tree_none, dask, async_tree_memoization, asyncio_tcp_ssl
