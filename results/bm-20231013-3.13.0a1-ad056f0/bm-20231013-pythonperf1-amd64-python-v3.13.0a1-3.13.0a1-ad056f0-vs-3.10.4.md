
# Results vs. 3.10.4

- fork: python
- ref: v3.13.0a1
- machine: windows-amd64
- commit hash: ad056f0
- commit date: 2023-10-13
- overall geometric mean: 1.19x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 216 ms: 1.14x faster                                            |
| chameleon      | 5.79 ms                                                     | 4.98 ms: 1.16x faster                                           |
| docutils       | 1.92 sec                                                    | 1.61 sec: 1.19x faster                                          |
| tornado_http   | 108 ms                                                      | 89.1 ms: 1.22x faster                                           |
| Geometric mean | (ref)                                                       | 1.18x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 267 ms: 1.63x faster                                            |
| async_tree_memoization  | 526 ms                                                      | 340 ms: 1.55x faster                                            |
| async_tree_io           | 1.11 sec                                                    | 723 ms: 1.53x faster                                            |
| async_tree_cpu_io_mixed | 638 ms                                                      | 455 ms: 1.40x faster                                            |
| Geometric mean          | (ref)                                                       | 1.53x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 53.6 ms: 1.15x faster                                           |
| pidigits       | 149 ms                                                      | 150 ms: 1.01x slower                                            |
| nbody          | 71.3 ms                                                     | 72.2 ms: 1.01x slower                                           |
| Geometric mean | (ref)                                                       | 1.04x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 90.8 ms: 1.17x faster                                           |
| regex_dna      | 136 ms                                                      | 119 ms: 1.15x faster                                            |
| regex_v8       | 15.4 ms                                                     | 14.8 ms: 1.04x faster                                           |
| regex_effbot   | 1.66 ms                                                     | 1.60 ms: 1.04x faster                                           |
| Geometric mean | (ref)                                                       | 1.10x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.60 ms: 1.64x faster                                           |
| pickle_pure_python   | 270 us                                                      | 190 us: 1.42x faster                                            |
| unpickle_pure_python | 183 us                                                      | 137 us: 1.33x faster                                            |
| xml_etree_process    | 44.5 ms                                                     | 38.2 ms: 1.16x faster                                           |
| tomli_loads          | 1.67 sec                                                    | 1.48 sec: 1.13x faster                                          |
| unpickle             | 9.09 us                                                     | 8.12 us: 1.12x faster                                           |
| xml_etree_parse      | 96.8 ms                                                     | 91.6 ms: 1.06x faster                                           |
| json_loads           | 14.0 us                                                     | 13.5 us: 1.04x faster                                           |
| xml_etree_iterparse  | 65.0 ms                                                     | 64.0 ms: 1.01x faster                                           |
| pickle               | 6.85 us                                                     | 6.98 us: 1.02x slower                                           |
| pickle_list          | 2.75 us                                                     | 2.94 us: 1.07x slower                                           |
| pickle_dict          | 17.2 us                                                     | 18.4 us: 1.07x slower                                           |
| Geometric mean       | (ref)                                                       | 1.11x faster                                                    |

Benchmark hidden because not significant (2): xml_etree_generate, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 19.7 ms: 1.05x faster                                           |
| python_startup_no_site | 15.5 ms                                                     | 16.2 ms: 1.05x slower                                           |
| Geometric mean         | (ref)                                                       | 1.00x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|-----------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako      | 9.03 ms                                                     | 7.20 ms: 1.25x faster                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 96.3 us: 3.49x faster                                           |
| deltablue                | 4.19 ms                                                     | 2.19 ms: 1.91x faster                                           |
| json_dumps               | 9.16 ms                                                     | 5.60 ms: 1.64x faster                                           |
| async_tree_none          | 435 ms                                                      | 267 ms: 1.63x faster                                            |
| richards_super           | 52.2 ms                                                     | 32.0 ms: 1.63x faster                                           |
| raytrace                 | 273 ms                                                      | 174 ms: 1.57x faster                                            |
| asyncio_tcp              | 732 ms                                                      | 470 ms: 1.56x faster                                            |
| async_tree_memoization   | 526 ms                                                      | 340 ms: 1.55x faster                                            |
| go                       | 139 ms                                                      | 90.0 ms: 1.54x faster                                           |
| async_tree_io            | 1.11 sec                                                    | 723 ms: 1.53x faster                                            |
| chaos                    | 61.7 ms                                                     | 40.4 ms: 1.53x faster                                           |
| sqlglot_parse            | 1.22 ms                                                     | 811 us: 1.50x faster                                            |
| logging_silent           | 94.6 ns                                                     | 63.2 ns: 1.50x faster                                           |
| richards                 | 42.4 ms                                                     | 28.8 ms: 1.47x faster                                           |
| scimark_lu               | 85.8 ms                                                     | 58.6 ms: 1.46x faster                                           |
| generators               | 32.4 ms                                                     | 22.3 ms: 1.45x faster                                           |
| crypto_pyaes             | 62.5 ms                                                     | 43.3 ms: 1.44x faster                                           |
| sqlglot_transpile        | 1.48 ms                                                     | 1.03 ms: 1.43x faster                                           |
| pickle_pure_python       | 270 us                                                      | 190 us: 1.42x faster                                            |
| hexiom                   | 5.74 ms                                                     | 4.09 ms: 1.40x faster                                           |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 455 ms: 1.40x faster                                            |
| scimark_monte_carlo      | 57.3 ms                                                     | 41.0 ms: 1.40x faster                                           |
| scimark_sor              | 106 ms                                                      | 77.0 ms: 1.38x faster                                           |
| pyflate                  | 409 ms                                                      | 298 ms: 1.37x faster                                            |
| unpickle_pure_python     | 183 us                                                      | 137 us: 1.33x faster                                            |
| mako                     | 9.03 ms                                                     | 7.20 ms: 1.25x faster                                           |
| spectral_norm            | 77.3 ms                                                     | 63.0 ms: 1.23x faster                                           |
| tornado_http             | 108 ms                                                      | 89.1 ms: 1.22x faster                                           |
| docutils                 | 1.92 sec                                                    | 1.61 sec: 1.19x faster                                          |
| mdp                      | 1.78 sec                                                    | 1.49 sec: 1.19x faster                                          |
| pprint_pformat           | 1.22 sec                                                    | 1.03 sec: 1.18x faster                                          |
| sympy_sum                | 107 ms                                                      | 91.1 ms: 1.17x faster                                           |
| regex_compile            | 106 ms                                                      | 90.8 ms: 1.17x faster                                           |
| pprint_safe_repr         | 592 ms                                                      | 507 ms: 1.17x faster                                            |
| comprehensions           | 16.5 us                                                     | 14.2 us: 1.17x faster                                           |
| sympy_integrate          | 15.3 ms                                                     | 13.1 ms: 1.16x faster                                           |
| xml_etree_process        | 44.5 ms                                                     | 38.2 ms: 1.16x faster                                           |
| deepcopy_memo            | 28.8 us                                                     | 24.8 us: 1.16x faster                                           |
| chameleon                | 5.79 ms                                                     | 4.98 ms: 1.16x faster                                           |
| sqlite_synth             | 1.91 us                                                     | 1.65 us: 1.16x faster                                           |
| float                    | 61.7 ms                                                     | 53.6 ms: 1.15x faster                                           |
| regex_dna                | 136 ms                                                      | 119 ms: 1.15x faster                                            |
| bench_thread_pool        | 958 us                                                      | 836 us: 1.14x faster                                            |
| sqlglot_optimize         | 39.8 ms                                                     | 34.8 ms: 1.14x faster                                           |
| 2to3                     | 246 ms                                                      | 216 ms: 1.14x faster                                            |
| tomli_loads              | 1.67 sec                                                    | 1.48 sec: 1.13x faster                                          |
| nqueens                  | 66.6 ms                                                     | 59.1 ms: 1.13x faster                                           |
| unpickle                 | 9.09 us                                                     | 8.12 us: 1.12x faster                                           |
| sqlglot_normalize        | 205 ms                                                      | 184 ms: 1.12x faster                                            |
| dulwich_log              | 50.5 ms                                                     | 45.2 ms: 1.12x faster                                           |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.89 sec: 1.12x faster                                          |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.45 ms: 1.11x faster                                           |
| sympy_str                | 194 ms                                                      | 175 ms: 1.11x faster                                            |
| deepcopy                 | 255 us                                                      | 230 us: 1.11x faster                                            |
| create_gc_cycles         | 800 us                                                      | 728 us: 1.10x faster                                            |
| sympy_expand             | 314 ms                                                      | 287 ms: 1.10x faster                                            |
| coroutines               | 16.0 ms                                                     | 14.7 ms: 1.09x faster                                           |
| pycparser                | 930 ms                                                      | 861 ms: 1.08x faster                                            |
| scimark_fft              | 187 ms                                                      | 176 ms: 1.07x faster                                            |
| deepcopy_reduce          | 2.20 us                                                     | 2.07 us: 1.06x faster                                           |
| xml_etree_parse          | 96.8 ms                                                     | 91.6 ms: 1.06x faster                                           |
| python_startup           | 20.6 ms                                                     | 19.7 ms: 1.05x faster                                           |
| regex_v8                 | 15.4 ms                                                     | 14.8 ms: 1.04x faster                                           |
| regex_effbot             | 1.66 ms                                                     | 1.60 ms: 1.04x faster                                           |
| json_loads               | 14.0 us                                                     | 13.5 us: 1.04x faster                                           |
| unpack_sequence          | 39.6 ns                                                     | 38.5 ns: 1.03x faster                                           |
| fannkuch                 | 256 ms                                                      | 249 ms: 1.03x faster                                            |
| meteor_contest           | 75.9 ms                                                     | 74.5 ms: 1.02x faster                                           |
| xml_etree_iterparse      | 65.0 ms                                                     | 64.0 ms: 1.01x faster                                           |
| pidigits                 | 149 ms                                                      | 150 ms: 1.01x slower                                            |
| logging_format           | 6.76 us                                                     | 6.81 us: 1.01x slower                                           |
| nbody                    | 71.3 ms                                                     | 72.2 ms: 1.01x slower                                           |
| pickle                   | 6.85 us                                                     | 6.98 us: 1.02x slower                                           |
| logging_simple           | 6.22 us                                                     | 6.40 us: 1.03x slower                                           |
| bench_mp_pool            | 62.0 ms                                                     | 64.0 ms: 1.03x slower                                           |
| pathlib                  | 75.7 ms                                                     | 78.5 ms: 1.04x slower                                           |
| python_startup_no_site   | 15.5 ms                                                     | 16.2 ms: 1.05x slower                                           |
| gc_traversal             | 1.41 ms                                                     | 1.49 ms: 1.05x slower                                           |
| async_generators         | 222 ms                                                      | 236 ms: 1.06x slower                                            |
| pickle_list              | 2.75 us                                                     | 2.94 us: 1.07x slower                                           |
| pickle_dict              | 17.2 us                                                     | 18.4 us: 1.07x slower                                           |
| coverage                 | 39.0 ms                                                     | 45.4 ms: 1.16x slower                                           |
| telco                    | 3.94 ms                                                     | 4.73 ms: 1.20x slower                                           |
| Geometric mean           | (ref)                                                       | 1.19x faster                                                    |

Benchmark hidden because not significant (3): json, xml_etree_generate, unpickle_list
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
Ignored benchmarks (4) of results/bm-20231013-3.13.0a1-ad056f0/bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.12x


# Memory

- memory change: unknown