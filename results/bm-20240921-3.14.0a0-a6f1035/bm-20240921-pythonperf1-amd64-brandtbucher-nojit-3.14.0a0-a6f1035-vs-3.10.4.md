# Results vs. 3.10.4

- fork: brandtbucher
- ref: nojit
- machine: windows-amd64
- commit hash: a6f1035
- commit date: 2024-09-21
- overall geometric mean: 1.171x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 226 ms: 1.09x faster                                              |
| docutils       | 1.92 sec                                                    | 1.70 sec: 1.13x faster                                            |
| html5lib       | 51.0 ms                                                     | 40.9 ms: 1.25x faster                                             |
| tornado_http   | 108 ms                                                      | 84.2 ms: 1.29x faster                                             |
| Geometric mean | (ref)                                                       | 1.18x faster                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|-------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 209 ms: 2.08x faster                                              |
| async_tree_memoization  | 526 ms                                                      | 260 ms: 2.02x faster                                              |
| async_tree_io           | 1.11 sec                                                    | 570 ms: 1.94x faster                                              |
| async_tree_cpu_io_mixed | 638 ms                                                      | 385 ms: 1.66x faster                                              |
| Geometric mean          | (ref)                                                       | 1.92x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 55.3 ms: 1.12x faster                                             |
| pidigits       | 149 ms                                                      | 151 ms: 1.01x slower                                              |
| nbody          | 71.3 ms                                                     | 83.8 ms: 1.17x slower                                             |
| Geometric mean | (ref)                                                       | 1.02x slower                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 93.1 ms: 1.14x faster                                             |
| regex_dna      | 136 ms                                                      | 121 ms: 1.12x faster                                              |
| regex_effbot   | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                             |
| regex_v8       | 15.4 ms                                                     | 15.3 ms: 1.01x faster                                             |
| Geometric mean | (ref)                                                       | 1.08x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.26 ms: 1.46x faster                                             |
| pickle_pure_python   | 270 us                                                      | 215 us: 1.25x faster                                              |
| unpickle_pure_python | 183 us                                                      | 153 us: 1.19x faster                                              |
| xml_etree_process    | 44.5 ms                                                     | 40.9 ms: 1.09x faster                                             |
| tomli_loads          | 1.67 sec                                                    | 1.61 sec: 1.04x faster                                            |
| xml_etree_parse      | 96.8 ms                                                     | 94.3 ms: 1.03x faster                                             |
| json_loads           | 14.0 us                                                     | 14.2 us: 1.01x slower                                             |
| unpickle_list        | 2.71 us                                                     | 2.78 us: 1.03x slower                                             |
| pickle_dict          | 17.2 us                                                     | 17.6 us: 1.03x slower                                             |
| pickle               | 6.85 us                                                     | 7.10 us: 1.04x slower                                             |
| xml_etree_generate   | 55.5 ms                                                     | 58.6 ms: 1.06x slower                                             |
| Geometric mean       | (ref)                                                       | 1.06x faster                                                      |

Benchmark hidden because not significant (3): pickle_list, unpickle, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 21.9 ms: 1.06x slower                                             |
| python_startup_no_site | 15.5 ms                                                     | 17.9 ms: 1.16x slower                                             |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.85 ms: 1.32x faster                                             |
| genshi_text     | 19.8 ms                                                     | 16.9 ms: 1.17x faster                                             |
| genshi_xml      | 41.0 ms                                                     | 35.6 ms: 1.15x faster                                             |
| django_template | 28.9 ms                                                     | 25.9 ms: 1.11x faster                                             |
| Geometric mean  | (ref)                                                       | 1.19x faster                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|--------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 111 us: 3.03x faster                                              |
| async_tree_none          | 435 ms                                                      | 209 ms: 2.08x faster                                              |
| async_tree_memoization   | 526 ms                                                      | 260 ms: 2.02x faster                                              |
| async_tree_io            | 1.11 sec                                                    | 570 ms: 1.94x faster                                              |
| deltablue                | 4.19 ms                                                     | 2.32 ms: 1.80x faster                                             |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 385 ms: 1.66x faster                                              |
| go                       | 139 ms                                                      | 88.9 ms: 1.56x faster                                             |
| asyncio_tcp              | 732 ms                                                      | 469 ms: 1.56x faster                                              |
| pylint                   | 350 ms                                                      | 225 ms: 1.56x faster                                              |
| generators               | 32.4 ms                                                     | 21.3 ms: 1.52x faster                                             |
| logging_silent           | 94.6 ns                                                     | 63.5 ns: 1.49x faster                                             |
| json_dumps               | 9.16 ms                                                     | 6.26 ms: 1.46x faster                                             |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.45 sec: 1.45x faster                                            |
| richards_super           | 52.2 ms                                                     | 36.9 ms: 1.42x faster                                             |
| deepcopy_memo            | 28.8 us                                                     | 20.6 us: 1.39x faster                                             |
| raytrace                 | 273 ms                                                      | 197 ms: 1.39x faster                                              |
| comprehensions           | 16.5 us                                                     | 12.0 us: 1.38x faster                                             |
| chaos                    | 61.7 ms                                                     | 44.9 ms: 1.38x faster                                             |
| sqlglot_parse            | 1.22 ms                                                     | 902 us: 1.35x faster                                              |
| deepcopy                 | 255 us                                                      | 191 us: 1.34x faster                                              |
| mako                     | 9.03 ms                                                     | 6.85 ms: 1.32x faster                                             |
| sqlglot_transpile        | 1.48 ms                                                     | 1.12 ms: 1.32x faster                                             |
| scimark_lu               | 85.8 ms                                                     | 65.7 ms: 1.31x faster                                             |
| crypto_pyaes             | 62.5 ms                                                     | 47.9 ms: 1.31x faster                                             |
| tornado_http             | 108 ms                                                      | 84.2 ms: 1.29x faster                                             |
| richards                 | 42.4 ms                                                     | 33.0 ms: 1.29x faster                                             |
| pyflate                  | 409 ms                                                      | 324 ms: 1.26x faster                                              |
| pickle_pure_python       | 270 us                                                      | 215 us: 1.25x faster                                              |
| html5lib                 | 51.0 ms                                                     | 40.9 ms: 1.25x faster                                             |
| hexiom                   | 5.74 ms                                                     | 4.62 ms: 1.24x faster                                             |
| pycparser                | 930 ms                                                      | 770 ms: 1.21x faster                                              |
| thrift                   | 617 us                                                      | 512 us: 1.21x faster                                              |
| unpickle_pure_python     | 183 us                                                      | 153 us: 1.19x faster                                              |
| bench_thread_pool        | 958 us                                                      | 805 us: 1.19x faster                                              |
| mdp                      | 1.78 sec                                                    | 1.51 sec: 1.18x faster                                            |
| sympy_sum                | 107 ms                                                      | 90.6 ms: 1.18x faster                                             |
| scimark_sor              | 106 ms                                                      | 90.7 ms: 1.17x faster                                             |
| genshi_text              | 19.8 ms                                                     | 16.9 ms: 1.17x faster                                             |
| sqlite_synth             | 1.91 us                                                     | 1.64 us: 1.17x faster                                             |
| dulwich_log              | 50.5 ms                                                     | 43.4 ms: 1.16x faster                                             |
| coroutines               | 16.0 ms                                                     | 13.8 ms: 1.16x faster                                             |
| sympy_integrate          | 15.3 ms                                                     | 13.2 ms: 1.15x faster                                             |
| genshi_xml               | 41.0 ms                                                     | 35.6 ms: 1.15x faster                                             |
| regex_compile            | 106 ms                                                      | 93.1 ms: 1.14x faster                                             |
| deepcopy_reduce          | 2.20 us                                                     | 1.94 us: 1.14x faster                                             |
| docutils                 | 1.92 sec                                                    | 1.70 sec: 1.13x faster                                            |
| regex_dna                | 136 ms                                                      | 121 ms: 1.12x faster                                              |
| float                    | 61.7 ms                                                     | 55.3 ms: 1.12x faster                                             |
| scimark_monte_carlo      | 57.3 ms                                                     | 51.4 ms: 1.11x faster                                             |
| django_template          | 28.9 ms                                                     | 25.9 ms: 1.11x faster                                             |
| spectral_norm            | 77.3 ms                                                     | 69.9 ms: 1.11x faster                                             |
| sympy_str                | 194 ms                                                      | 178 ms: 1.09x faster                                              |
| 2to3                     | 246 ms                                                      | 226 ms: 1.09x faster                                              |
| xml_etree_process        | 44.5 ms                                                     | 40.9 ms: 1.09x faster                                             |
| sqlglot_optimize         | 39.8 ms                                                     | 36.8 ms: 1.08x faster                                             |
| pprint_pformat           | 1.22 sec                                                    | 1.13 sec: 1.08x faster                                            |
| pprint_safe_repr         | 592 ms                                                      | 551 ms: 1.07x faster                                              |
| regex_effbot             | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                             |
| sqlglot_normalize        | 205 ms                                                      | 197 ms: 1.04x faster                                              |
| tomli_loads              | 1.67 sec                                                    | 1.61 sec: 1.04x faster                                            |
| sympy_expand             | 314 ms                                                      | 305 ms: 1.03x faster                                              |
| xml_etree_parse          | 96.8 ms                                                     | 94.3 ms: 1.03x faster                                             |
| nqueens                  | 66.6 ms                                                     | 65.9 ms: 1.01x faster                                             |
| regex_v8                 | 15.4 ms                                                     | 15.3 ms: 1.01x faster                                             |
| json_loads               | 14.0 us                                                     | 14.2 us: 1.01x slower                                             |
| pidigits                 | 149 ms                                                      | 151 ms: 1.01x slower                                              |
| unpickle_list            | 2.71 us                                                     | 2.78 us: 1.03x slower                                             |
| pickle_dict              | 17.2 us                                                     | 17.6 us: 1.03x slower                                             |
| pickle                   | 6.85 us                                                     | 7.10 us: 1.04x slower                                             |
| meteor_contest           | 75.9 ms                                                     | 78.9 ms: 1.04x slower                                             |
| logging_format           | 6.76 us                                                     | 7.08 us: 1.05x slower                                             |
| xml_etree_generate       | 55.5 ms                                                     | 58.6 ms: 1.06x slower                                             |
| python_startup           | 20.6 ms                                                     | 21.9 ms: 1.06x slower                                             |
| bench_mp_pool            | 62.0 ms                                                     | 66.6 ms: 1.07x slower                                             |
| logging_simple           | 6.22 us                                                     | 6.68 us: 1.07x slower                                             |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.93 ms: 1.08x slower                                             |
| unpack_sequence          | 39.6 ns                                                     | 42.7 ns: 1.08x slower                                             |
| gc_traversal             | 1.41 ms                                                     | 1.53 ms: 1.08x slower                                             |
| create_gc_cycles         | 800 us                                                      | 882 us: 1.10x slower                                              |
| async_generators         | 222 ms                                                      | 245 ms: 1.11x slower                                              |
| scimark_fft              | 187 ms                                                      | 212 ms: 1.13x slower                                              |
| python_startup_no_site   | 15.5 ms                                                     | 17.9 ms: 1.16x slower                                             |
| nbody                    | 71.3 ms                                                     | 83.8 ms: 1.17x slower                                             |
| fannkuch                 | 256 ms                                                      | 308 ms: 1.20x slower                                              |
| coverage                 | 39.0 ms                                                     | 48.5 ms: 1.24x slower                                             |
| telco                    | 3.94 ms                                                     | 5.20 ms: 1.32x slower                                             |
| Geometric mean           | (ref)                                                       | 1.16x faster                                                      |

Benchmark hidden because not significant (5): json, pickle_list, pathlib, unpickle, xml_etree_iterparse
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240921-3.14.0a0-a6f1035/bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

- Geometric mean (including insignificant results): 1.171x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: unknown