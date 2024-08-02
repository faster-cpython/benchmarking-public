# Results vs. 3.10.4

- fork: python
- ref: 44995aab499b09a550de
- machine: windows-amd64
- commit hash: 44995aa
- commit date: 2024-05-13
- overall geometric mean: 1.12x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 234 ms: 1.05x faster                                                        |
| chameleon      | 5.79 ms                                                     | 5.12 ms: 1.13x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.83 sec: 1.05x faster                                                      |
| html5lib       | 51.0 ms                                                     | 41.3 ms: 1.24x faster                                                       |
| tornado_http   | 108 ms                                                      | 87.9 ms: 1.23x faster                                                       |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization  | 526 ms                                                      | 280 ms: 1.88x faster                                                        |
| async_tree_none         | 435 ms                                                      | 232 ms: 1.88x faster                                                        |
| async_tree_io           | 1.11 sec                                                    | 604 ms: 1.83x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 401 ms: 1.59x faster                                                        |
| Geometric mean          | (ref)                                                       | 1.79x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 51.7 ms: 1.19x faster                                                       |
| pidigits       | 149 ms                                                      | 150 ms: 1.01x slower                                                        |
| nbody          | 71.3 ms                                                     | 72.7 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 116 ms: 1.17x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.56 ms: 1.06x faster                                                       |
| regex_compile  | 106 ms                                                      | 107 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.71 ms: 1.60x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 212 us: 1.27x faster                                                        |
| unpickle_pure_python | 183 us                                                      | 155 us: 1.18x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.42 sec: 1.18x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 38.9 ms: 1.14x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 88.5 ms: 1.09x faster                                                       |
| unpickle             | 9.09 us                                                     | 8.36 us: 1.09x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 64.2 ms: 1.01x faster                                                       |
| json_loads           | 14.0 us                                                     | 14.1 us: 1.01x slower                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 56.1 ms: 1.01x slower                                                       |
| pickle               | 6.85 us                                                     | 7.16 us: 1.05x slower                                                       |
| pickle_dict          | 17.2 us                                                     | 18.5 us: 1.08x slower                                                       |
| pickle_list          | 2.75 us                                                     | 3.11 us: 1.13x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.08x faster                                                                |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 20.3 ms: 1.02x faster                                                       |
| python_startup_no_site | 15.5 ms                                                     | 16.6 ms: 1.07x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.03x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 7.20 ms: 1.25x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 16.7 ms: 1.19x faster                                                       |
| django_template | 28.9 ms                                                     | 24.5 ms: 1.18x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 36.5 ms: 1.13x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.19x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 115 us: 2.92x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 280 ms: 1.88x faster                                                        |
| async_tree_none          | 435 ms                                                      | 232 ms: 1.88x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 604 ms: 1.83x faster                                                        |
| generators               | 32.4 ms                                                     | 19.4 ms: 1.67x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.54 ms: 1.65x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 5.71 ms: 1.60x faster                                                       |
| richards_super           | 52.2 ms                                                     | 32.6 ms: 1.60x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 401 ms: 1.59x faster                                                        |
| pylint                   | 350 ms                                                      | 232 ms: 1.51x faster                                                        |
| raytrace                 | 273 ms                                                      | 182 ms: 1.50x faster                                                        |
| richards                 | 42.4 ms                                                     | 28.5 ms: 1.49x faster                                                       |
| chaos                    | 61.7 ms                                                     | 43.3 ms: 1.42x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 869 us: 1.40x faster                                                        |
| go                       | 139 ms                                                      | 99.6 ms: 1.39x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 69.1 ns: 1.37x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.55 sec: 1.36x faster                                                      |
| sqlglot_transpile        | 1.48 ms                                                     | 1.11 ms: 1.33x faster                                                       |
| pyflate                  | 409 ms                                                      | 321 ms: 1.27x faster                                                        |
| pickle_pure_python       | 270 us                                                      | 212 us: 1.27x faster                                                        |
| coroutines               | 16.0 ms                                                     | 12.6 ms: 1.27x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 49.3 ms: 1.27x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 578 ms: 1.27x faster                                                        |
| comprehensions           | 16.5 us                                                     | 13.1 us: 1.26x faster                                                       |
| mako                     | 9.03 ms                                                     | 7.20 ms: 1.25x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 41.3 ms: 1.24x faster                                                       |
| tornado_http             | 108 ms                                                      | 87.9 ms: 1.23x faster                                                       |
| scimark_sor              | 106 ms                                                      | 86.8 ms: 1.22x faster                                                       |
| pycparser                | 930 ms                                                      | 768 ms: 1.21x faster                                                        |
| scimark_monte_carlo      | 57.3 ms                                                     | 47.4 ms: 1.21x faster                                                       |
| float                    | 61.7 ms                                                     | 51.7 ms: 1.19x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 16.7 ms: 1.19x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.62 us: 1.18x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 155 us: 1.18x faster                                                        |
| django_template          | 28.9 ms                                                     | 24.5 ms: 1.18x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.42 sec: 1.18x faster                                                      |
| regex_dna                | 136 ms                                                      | 116 ms: 1.17x faster                                                        |
| mdp                      | 1.78 sec                                                    | 1.52 sec: 1.17x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 74.9 ms: 1.14x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 38.9 ms: 1.14x faster                                                       |
| chameleon                | 5.79 ms                                                     | 5.12 ms: 1.13x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 36.5 ms: 1.13x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.09 sec: 1.12x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 532 ms: 1.11x faster                                                        |
| bench_thread_pool        | 958 us                                                      | 868 us: 1.10x faster                                                        |
| hexiom                   | 5.74 ms                                                     | 5.23 ms: 1.10x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 46.0 ms: 1.10x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 88.5 ms: 1.09x faster                                                       |
| json                     | 3.14 ms                                                     | 2.88 ms: 1.09x faster                                                       |
| sympy_sum                | 107 ms                                                      | 98.4 ms: 1.09x faster                                                       |
| unpickle                 | 9.09 us                                                     | 8.36 us: 1.09x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.56 ms: 1.06x faster                                                       |
| 2to3                     | 246 ms                                                      | 234 ms: 1.05x faster                                                        |
| sympy_integrate          | 15.3 ms                                                     | 14.6 ms: 1.05x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.83 sec: 1.05x faster                                                      |
| aiohttp                  | 995 us                                                      | 953 us: 1.04x faster                                                        |
| sqlglot_optimize         | 39.8 ms                                                     | 38.2 ms: 1.04x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 27.8 us: 1.04x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 2.13 us: 1.03x faster                                                       |
| deepcopy                 | 255 us                                                      | 248 us: 1.03x faster                                                        |
| logging_format           | 6.76 us                                                     | 6.60 us: 1.02x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 65.3 ms: 1.02x faster                                                       |
| python_startup           | 20.6 ms                                                     | 20.3 ms: 1.02x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 76.0 ms: 1.02x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 64.2 ms: 1.01x faster                                                       |
| logging_simple           | 6.22 us                                                     | 6.17 us: 1.01x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 75.3 ms: 1.01x faster                                                       |
| flaskblogging            | 2.03 sec                                                    | 2.03 sec: 1.00x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.1 us: 1.01x slower                                                       |
| pidigits                 | 149 ms                                                      | 150 ms: 1.01x slower                                                        |
| xml_etree_generate       | 55.5 ms                                                     | 56.1 ms: 1.01x slower                                                       |
| regex_compile            | 106 ms                                                      | 107 ms: 1.01x slower                                                        |
| scimark_fft              | 187 ms                                                      | 190 ms: 1.02x slower                                                        |
| nbody                    | 71.3 ms                                                     | 72.7 ms: 1.02x slower                                                       |
| fannkuch                 | 256 ms                                                      | 261 ms: 1.02x slower                                                        |
| pickle                   | 6.85 us                                                     | 7.16 us: 1.05x slower                                                       |
| pathlib                  | 75.7 ms                                                     | 79.9 ms: 1.06x slower                                                       |
| sympy_expand             | 314 ms                                                      | 332 ms: 1.06x slower                                                        |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.88 ms: 1.06x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 16.6 ms: 1.07x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 18.5 us: 1.08x slower                                                       |
| async_generators         | 222 ms                                                      | 241 ms: 1.09x slower                                                        |
| bench_mp_pool            | 62.0 ms                                                     | 68.3 ms: 1.10x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.57 ms: 1.11x slower                                                       |
| pickle_list              | 2.75 us                                                     | 3.11 us: 1.13x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 914 us: 1.14x slower                                                        |
| coverage                 | 39.0 ms                                                     | 44.6 ms: 1.14x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.88 ms: 1.24x slower                                                       |
| thrift                   | 617 us                                                      | 9.71 ms: 15.73x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.12x faster                                                                |

Benchmark hidden because not significant (3): sympy_str, regex_v8, unpickle_list
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (4) of results/bm-20240513-3.13.0b1+-44995aa-PYTHON_UOPS/bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: unknown