# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_unlikely
- machine: windows-amd64
- commit hash: 15229e0
- commit date: 2024-10-17
- overall geometric mean: 1.17x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 251 ms: 1.02x slower                                                         |
| docutils       | 1.92 sec                                                    | 1.93 sec: 1.01x slower                                                       |
| html5lib       | 51.0 ms                                                     | 39.9 ms: 1.28x faster                                                        |
| tornado_http   | 108 ms                                                      | 101 ms: 1.08x faster                                                         |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|-------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 557 ms: 1.99x faster                                                         |
| async_tree_none         | 435 ms                                                      | 220 ms: 1.98x faster                                                         |
| async_tree_memoization  | 526 ms                                                      | 283 ms: 1.86x faster                                                         |
| async_tree_cpu_io_mixed | 638 ms                                                      | 387 ms: 1.65x faster                                                         |
| Geometric mean          | (ref)                                                       | 1.87x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 51.8 ms: 1.38x faster                                                        |
| float          | 61.7 ms                                                     | 46.7 ms: 1.32x faster                                                        |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                       | 1.22x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 114 ms: 1.19x faster                                                         |
| regex_compile  | 106 ms                                                      | 92.5 ms: 1.15x faster                                                        |
| regex_v8       | 15.4 ms                                                     | 14.7 ms: 1.05x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.60 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                       | 1.10x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.24 ms: 1.47x faster                                                        |
| pickle_pure_python   | 270 us                                                      | 202 us: 1.33x faster                                                         |
| tomli_loads          | 1.67 sec                                                    | 1.32 sec: 1.27x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 147 us: 1.24x faster                                                         |
| xml_etree_process    | 44.5 ms                                                     | 36.4 ms: 1.22x faster                                                        |
| xml_etree_generate   | 55.5 ms                                                     | 51.0 ms: 1.09x faster                                                        |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.5 ms: 1.02x faster                                                        |
| xml_etree_parse      | 96.8 ms                                                     | 95.3 ms: 1.02x faster                                                        |
| json_loads           | 14.0 us                                                     | 14.4 us: 1.02x slower                                                        |
| pickle_dict          | 17.2 us                                                     | 17.9 us: 1.04x slower                                                        |
| unpickle_list        | 2.71 us                                                     | 2.86 us: 1.05x slower                                                        |
| pickle               | 6.85 us                                                     | 7.38 us: 1.08x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.09x faster                                                                 |

Benchmark hidden because not significant (2): pickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 24.3 ms: 1.18x slower                                                        |
| python_startup_no_site | 15.5 ms                                                     | 18.4 ms: 1.19x slower                                                        |
| Geometric mean         | (ref)                                                       | 1.18x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.02 ms: 1.80x faster                                                        |
| django_template | 28.9 ms                                                     | 27.0 ms: 1.07x faster                                                        |
| genshi_xml      | 41.0 ms                                                     | 46.9 ms: 1.14x slower                                                        |
| Geometric mean  | (ref)                                                       | 1.14x faster                                                                 |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|--------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 116 us: 2.89x faster                                                         |
| async_tree_io            | 1.11 sec                                                    | 557 ms: 1.99x faster                                                         |
| async_tree_none          | 435 ms                                                      | 220 ms: 1.98x faster                                                         |
| async_tree_memoization   | 526 ms                                                      | 283 ms: 1.86x faster                                                         |
| mako                     | 9.03 ms                                                     | 5.02 ms: 1.80x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.37 ms: 1.77x faster                                                        |
| scimark_sor              | 106 ms                                                      | 62.8 ms: 1.69x faster                                                        |
| deepcopy_memo            | 28.8 us                                                     | 17.1 us: 1.69x faster                                                        |
| logging_silent           | 94.6 ns                                                     | 57.4 ns: 1.65x faster                                                        |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 387 ms: 1.65x faster                                                         |
| crypto_pyaes             | 62.5 ms                                                     | 39.9 ms: 1.57x faster                                                        |
| scimark_lu               | 85.8 ms                                                     | 55.0 ms: 1.56x faster                                                        |
| scimark_monte_carlo      | 57.3 ms                                                     | 37.8 ms: 1.52x faster                                                        |
| chaos                    | 61.7 ms                                                     | 41.5 ms: 1.49x faster                                                        |
| json_dumps               | 9.16 ms                                                     | 6.24 ms: 1.47x faster                                                        |
| go                       | 139 ms                                                      | 95.4 ms: 1.46x faster                                                        |
| spectral_norm            | 77.3 ms                                                     | 53.2 ms: 1.45x faster                                                        |
| comprehensions           | 16.5 us                                                     | 11.6 us: 1.43x faster                                                        |
| pyflate                  | 409 ms                                                      | 289 ms: 1.41x faster                                                         |
| generators               | 32.4 ms                                                     | 22.9 ms: 1.41x faster                                                        |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.52 sec: 1.39x faster                                                       |
| nbody                    | 71.3 ms                                                     | 51.8 ms: 1.38x faster                                                        |
| richards_super           | 52.2 ms                                                     | 39.1 ms: 1.34x faster                                                        |
| pickle_pure_python       | 270 us                                                      | 202 us: 1.33x faster                                                         |
| sqlglot_parse            | 1.22 ms                                                     | 915 us: 1.33x faster                                                         |
| deepcopy                 | 255 us                                                      | 192 us: 1.33x faster                                                         |
| float                    | 61.7 ms                                                     | 46.7 ms: 1.32x faster                                                        |
| pprint_pformat           | 1.22 sec                                                    | 924 ms: 1.32x faster                                                         |
| pprint_safe_repr         | 592 ms                                                      | 449 ms: 1.32x faster                                                         |
| html5lib                 | 51.0 ms                                                     | 39.9 ms: 1.28x faster                                                        |
| raytrace                 | 273 ms                                                      | 214 ms: 1.28x faster                                                         |
| tomli_loads              | 1.67 sec                                                    | 1.32 sec: 1.27x faster                                                       |
| pycparser                | 930 ms                                                      | 745 ms: 1.25x faster                                                         |
| unpickle_pure_python     | 183 us                                                      | 147 us: 1.24x faster                                                         |
| pylint                   | 350 ms                                                      | 283 ms: 1.24x faster                                                         |
| richards                 | 42.4 ms                                                     | 34.5 ms: 1.23x faster                                                        |
| xml_etree_process        | 44.5 ms                                                     | 36.4 ms: 1.22x faster                                                        |
| dulwich_log              | 50.5 ms                                                     | 41.5 ms: 1.22x faster                                                        |
| sqlglot_transpile        | 1.48 ms                                                     | 1.21 ms: 1.21x faster                                                        |
| sqlite_synth             | 1.91 us                                                     | 1.59 us: 1.20x faster                                                        |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.26 ms: 1.20x faster                                                        |
| scimark_fft              | 187 ms                                                      | 157 ms: 1.19x faster                                                         |
| regex_dna                | 136 ms                                                      | 114 ms: 1.19x faster                                                         |
| thrift                   | 617 us                                                      | 526 us: 1.17x faster                                                         |
| bench_thread_pool        | 958 us                                                      | 825 us: 1.16x faster                                                         |
| deepcopy_reduce          | 2.20 us                                                     | 1.90 us: 1.16x faster                                                        |
| mdp                      | 1.78 sec                                                    | 1.55 sec: 1.15x faster                                                       |
| regex_compile            | 106 ms                                                      | 92.5 ms: 1.15x faster                                                        |
| coroutines               | 16.0 ms                                                     | 14.1 ms: 1.14x faster                                                        |
| asyncio_tcp              | 732 ms                                                      | 666 ms: 1.10x faster                                                         |
| hexiom                   | 5.74 ms                                                     | 5.25 ms: 1.09x faster                                                        |
| fannkuch                 | 256 ms                                                      | 234 ms: 1.09x faster                                                         |
| xml_etree_generate       | 55.5 ms                                                     | 51.0 ms: 1.09x faster                                                        |
| tornado_http             | 108 ms                                                      | 101 ms: 1.08x faster                                                         |
| django_template          | 28.9 ms                                                     | 27.0 ms: 1.07x faster                                                        |
| nqueens                  | 66.6 ms                                                     | 63.5 ms: 1.05x faster                                                        |
| regex_v8                 | 15.4 ms                                                     | 14.7 ms: 1.05x faster                                                        |
| json                     | 3.14 ms                                                     | 3.00 ms: 1.05x faster                                                        |
| sympy_sum                | 107 ms                                                      | 102 ms: 1.05x faster                                                         |
| regex_effbot             | 1.66 ms                                                     | 1.60 ms: 1.03x faster                                                        |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.5 ms: 1.02x faster                                                        |
| xml_etree_parse          | 96.8 ms                                                     | 95.3 ms: 1.02x faster                                                        |
| logging_format           | 6.76 us                                                     | 6.66 us: 1.02x faster                                                        |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                                         |
| meteor_contest           | 75.9 ms                                                     | 75.2 ms: 1.01x faster                                                        |
| logging_simple           | 6.22 us                                                     | 6.18 us: 1.01x faster                                                        |
| docutils                 | 1.92 sec                                                    | 1.93 sec: 1.01x slower                                                       |
| sqlglot_normalize        | 205 ms                                                      | 209 ms: 1.02x slower                                                         |
| 2to3                     | 246 ms                                                      | 251 ms: 1.02x slower                                                         |
| json_loads               | 14.0 us                                                     | 14.4 us: 1.02x slower                                                        |
| sympy_integrate          | 15.3 ms                                                     | 15.9 ms: 1.04x slower                                                        |
| pickle_dict              | 17.2 us                                                     | 17.9 us: 1.04x slower                                                        |
| sympy_expand             | 314 ms                                                      | 331 ms: 1.05x slower                                                         |
| unpickle_list            | 2.71 us                                                     | 2.86 us: 1.05x slower                                                        |
| pathlib                  | 75.7 ms                                                     | 81.3 ms: 1.07x slower                                                        |
| pickle                   | 6.85 us                                                     | 7.38 us: 1.08x slower                                                        |
| sqlglot_optimize         | 39.8 ms                                                     | 43.2 ms: 1.08x slower                                                        |
| telco                    | 3.94 ms                                                     | 4.42 ms: 1.12x slower                                                        |
| genshi_xml               | 41.0 ms                                                     | 46.9 ms: 1.14x slower                                                        |
| python_startup           | 20.6 ms                                                     | 24.3 ms: 1.18x slower                                                        |
| python_startup_no_site   | 15.5 ms                                                     | 18.4 ms: 1.19x slower                                                        |
| coverage                 | 39.0 ms                                                     | 47.1 ms: 1.21x slower                                                        |
| async_generators         | 222 ms                                                      | 269 ms: 1.21x slower                                                         |
| gc_traversal             | 1.41 ms                                                     | 1.96 ms: 1.39x slower                                                        |
| bench_mp_pool            | 62.0 ms                                                     | 89.3 ms: 1.44x slower                                                        |
| unpack_sequence          | 39.6 ns                                                     | 60.8 ns: 1.53x slower                                                        |
| create_gc_cycles         | 800 us                                                      | 1.42 ms: 1.77x slower                                                        |
| Geometric mean           | (ref)                                                       | 1.17x faster                                                                 |

Benchmark hidden because not significant (4): genshi_text, pickle_list, unpickle, sympy_str
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20241017-3.14.0a1+-15229e0-JIT/bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: unknown