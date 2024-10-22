# Results vs. 3.10.4

- fork: mdboom
- ref: no_additional_schedu
- machine: windows-amd64
- commit hash: 39fa464
- commit date: 2024-07-19
- overall geometric mean: 1.25x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-39fa464 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 218 ms: 1.13x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.67 sec: 1.15x faster                                                     |
| html5lib       | 51.0 ms                                                     | 39.0 ms: 1.31x faster                                                      |
| tornado_http   | 108 ms                                                      | 91.5 ms: 1.18x faster                                                      |
| Geometric mean | (ref)                                                       | 1.19x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-39fa464 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 527 ms: 2.10x faster                                                       |
| async_tree_none         | 435 ms                                                      | 208 ms: 2.10x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 252 ms: 2.09x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 380 ms: 1.68x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.98x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-39fa464 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 54.0 ms: 1.14x faster                                                      |
| nbody          | 71.3 ms                                                     | 68.8 ms: 1.04x faster                                                      |
| pidigits       | 149 ms                                                      | 150 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.05x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-39fa464 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 83.8 ms: 1.27x faster                                                      |
| regex_dna      | 136 ms                                                      | 120 ms: 1.14x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.57 ms: 1.05x faster                                                      |
| Geometric mean | (ref)                                                       | 1.11x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-39fa464 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.87 ms: 1.56x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 134 us: 1.37x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 198 us: 1.36x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 38.0 ms: 1.17x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.46 sec: 1.14x faster                                                     |
| xml_etree_parse      | 96.8 ms                                                     | 93.2 ms: 1.04x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.6 ms: 1.02x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 55.2 ms: 1.01x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.1 us: 1.01x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.17x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-39fa464 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 21.7 ms: 1.05x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 18.0 ms: 1.16x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-39fa464 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.88 ms: 1.31x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.6 ms: 1.27x faster                                                      |
| django_template | 28.9 ms                                                     | 23.0 ms: 1.26x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 34.0 ms: 1.21x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.26x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-39fa464 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 107 us: 3.13x faster                                                       |
| deltablue                | 4.19 ms                                                     | 1.95 ms: 2.15x faster                                                      |
| async_tree_io            | 1.11 sec                                                    | 527 ms: 2.10x faster                                                       |
| async_tree_none          | 435 ms                                                      | 208 ms: 2.10x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 252 ms: 2.09x faster                                                       |
| pylint                   | 350 ms                                                      | 208 ms: 1.68x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 380 ms: 1.68x faster                                                       |
| raytrace                 | 273 ms                                                      | 164 ms: 1.67x faster                                                       |
| generators               | 32.4 ms                                                     | 19.6 ms: 1.65x faster                                                      |
| richards_super           | 52.2 ms                                                     | 32.0 ms: 1.63x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 58.2 ns: 1.63x faster                                                      |
| chaos                    | 61.7 ms                                                     | 39.3 ms: 1.57x faster                                                      |
| go                       | 139 ms                                                      | 88.7 ms: 1.57x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 5.87 ms: 1.56x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 56.0 ms: 1.53x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 18.9 us: 1.53x faster                                                      |
| richards                 | 42.4 ms                                                     | 28.3 ms: 1.50x faster                                                      |
| comprehensions           | 16.5 us                                                     | 11.0 us: 1.50x faster                                                      |
| deepcopy                 | 255 us                                                      | 174 us: 1.47x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 830 us: 1.46x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 3.93 ms: 1.46x faster                                                      |
| sqlglot_transpile        | 1.48 ms                                                     | 1.04 ms: 1.42x faster                                                      |
| pyflate                  | 409 ms                                                      | 293 ms: 1.40x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 525 ms: 1.40x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 134 us: 1.37x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 45.9 ms: 1.36x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 198 us: 1.36x faster                                                       |
| scimark_sor              | 106 ms                                                      | 78.9 ms: 1.34x faster                                                      |
| mako                     | 9.03 ms                                                     | 6.88 ms: 1.31x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 39.0 ms: 1.31x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 44.2 ms: 1.30x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.39 sec: 1.28x faster                                                     |
| genshi_text              | 19.8 ms                                                     | 15.6 ms: 1.27x faster                                                      |
| regex_compile            | 106 ms                                                      | 83.8 ms: 1.27x faster                                                      |
| pycparser                | 930 ms                                                      | 738 ms: 1.26x faster                                                       |
| django_template          | 28.9 ms                                                     | 23.0 ms: 1.26x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.78 us: 1.23x faster                                                      |
| sympy_sum                | 107 ms                                                      | 87.5 ms: 1.22x faster                                                      |
| coroutines               | 16.0 ms                                                     | 13.1 ms: 1.22x faster                                                      |
| thrift                   | 617 us                                                      | 507 us: 1.22x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 791 us: 1.21x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.74 sec: 1.21x faster                                                     |
| sympy_integrate          | 15.3 ms                                                     | 12.6 ms: 1.21x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 34.0 ms: 1.21x faster                                                      |
| tornado_http             | 108 ms                                                      | 91.5 ms: 1.18x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 65.4 ms: 1.18x faster                                                      |
| sqlglot_optimize         | 39.8 ms                                                     | 33.7 ms: 1.18x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 38.0 ms: 1.17x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 57.4 ms: 1.16x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.67 sec: 1.15x faster                                                     |
| sqlglot_normalize        | 205 ms                                                      | 179 ms: 1.15x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.46 sec: 1.14x faster                                                     |
| float                    | 61.7 ms                                                     | 54.0 ms: 1.14x faster                                                      |
| sympy_str                | 194 ms                                                      | 171 ms: 1.14x faster                                                       |
| regex_dna                | 136 ms                                                      | 120 ms: 1.14x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.08 sec: 1.13x faster                                                     |
| 2to3                     | 246 ms                                                      | 218 ms: 1.13x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 535 ms: 1.11x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.52 ms: 1.08x faster                                                      |
| sympy_expand             | 314 ms                                                      | 292 ms: 1.08x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.40 us: 1.06x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.57 ms: 1.05x faster                                                      |
| json                     | 3.14 ms                                                     | 3.00 ms: 1.05x faster                                                      |
| logging_simple           | 6.22 us                                                     | 5.95 us: 1.05x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 93.2 ms: 1.04x faster                                                      |
| nbody                    | 71.3 ms                                                     | 68.8 ms: 1.04x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 73.4 ms: 1.03x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.6 ms: 1.02x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 55.2 ms: 1.01x faster                                                      |
| json_loads               | 14.0 us                                                     | 14.1 us: 1.01x slower                                                      |
| pidigits                 | 149 ms                                                      | 150 ms: 1.01x slower                                                       |
| fannkuch                 | 256 ms                                                      | 269 ms: 1.05x slower                                                       |
| python_startup           | 20.6 ms                                                     | 21.7 ms: 1.05x slower                                                      |
| async_generators         | 222 ms                                                      | 235 ms: 1.06x slower                                                       |
| pathlib                  | 75.7 ms                                                     | 80.3 ms: 1.06x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 67.8 ms: 1.09x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.55 ms: 1.10x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 905 us: 1.13x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 18.0 ms: 1.16x slower                                                      |
| coverage                 | 39.0 ms                                                     | 46.5 ms: 1.19x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.74 ms: 1.20x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.25x faster                                                               |

Benchmark hidden because not significant (2): scimark_fft, regex_v8
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240719-3.14.0a0-39fa464/bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-39fa464.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: unknown