# Results vs. 3.10.4

- fork: faster-cpython
- ref: monitoring_branch_ta
- machine: windows-amd64
- commit hash: 1b65c46
- commit date: 2024-08-01
- overall geometric mean: 1.24x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-pythonperf1-amd64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-1b65c46 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 240 ms: 1.02x faster                                                                 |
| docutils       | 1.92 sec                                                    | 1.83 sec: 1.05x faster                                                               |
| html5lib       | 51.0 ms                                                     | 41.9 ms: 1.22x faster                                                                |
| tornado_http   | 108 ms                                                      | 96.0 ms: 1.13x faster                                                                |
| Geometric mean | (ref)                                                       | 1.10x faster                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-pythonperf1-amd64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-1b65c46 |
|-------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 215 ms: 2.02x faster                                                                 |
| async_tree_io           | 1.11 sec                                                    | 561 ms: 1.97x faster                                                                 |
| async_tree_memoization  | 526 ms                                                      | 267 ms: 1.97x faster                                                                 |
| async_tree_cpu_io_mixed | 638 ms                                                      | 396 ms: 1.61x faster                                                                 |
| Geometric mean          | (ref)                                                       | 1.89x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-pythonperf1-amd64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-1b65c46 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 49.7 ms: 1.43x faster                                                                |
| float          | 61.7 ms                                                     | 45.3 ms: 1.36x faster                                                                |
| pidigits       | 149 ms                                                      | 150 ms: 1.00x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.25x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-pythonperf1-amd64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-1b65c46 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 116 ms: 1.18x faster                                                                 |
| regex_compile  | 106 ms                                                      | 90.5 ms: 1.17x faster                                                                |
| regex_v8       | 15.4 ms                                                     | 14.4 ms: 1.08x faster                                                                |
| regex_effbot   | 1.66 ms                                                     | 1.56 ms: 1.06x faster                                                                |
| Geometric mean | (ref)                                                       | 1.12x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-pythonperf1-amd64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-1b65c46 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.10 ms: 1.50x faster                                                                |
| pickle_pure_python   | 270 us                                                      | 187 us: 1.44x faster                                                                 |
| unpickle_pure_python | 183 us                                                      | 135 us: 1.36x faster                                                                 |
| tomli_loads          | 1.67 sec                                                    | 1.28 sec: 1.31x faster                                                               |
| xml_etree_process    | 44.5 ms                                                     | 37.3 ms: 1.19x faster                                                                |
| xml_etree_generate   | 55.5 ms                                                     | 51.4 ms: 1.08x faster                                                                |
| xml_etree_iterparse  | 65.0 ms                                                     | 61.2 ms: 1.06x faster                                                                |
| xml_etree_parse      | 96.8 ms                                                     | 92.8 ms: 1.04x faster                                                                |
| json_loads           | 14.0 us                                                     | 14.1 us: 1.01x slower                                                                |
| Geometric mean       | (ref)                                                       | 1.21x faster                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-pythonperf1-amd64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-1b65c46 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 22.7 ms: 1.10x slower                                                                |
| python_startup_no_site | 15.5 ms                                                     | 18.7 ms: 1.20x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.15x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-pythonperf1-amd64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-1b65c46 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.10 ms: 1.77x faster                                                                |
| django_template | 28.9 ms                                                     | 25.6 ms: 1.13x faster                                                                |
| genshi_text     | 19.8 ms                                                     | 17.8 ms: 1.11x faster                                                                |
| genshi_xml      | 41.0 ms                                                     | 38.6 ms: 1.06x faster                                                                |
| Geometric mean  | (ref)                                                       | 1.24x faster                                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-pythonperf1-amd64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-1b65c46 |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 116 us: 2.90x faster                                                                 |
| async_tree_none          | 435 ms                                                      | 215 ms: 2.02x faster                                                                 |
| async_tree_io            | 1.11 sec                                                    | 561 ms: 1.97x faster                                                                 |
| async_tree_memoization   | 526 ms                                                      | 267 ms: 1.97x faster                                                                 |
| deepcopy_memo            | 28.8 us                                                     | 16.1 us: 1.79x faster                                                                |
| mako                     | 9.03 ms                                                     | 5.10 ms: 1.77x faster                                                                |
| deltablue                | 4.19 ms                                                     | 2.37 ms: 1.77x faster                                                                |
| spectral_norm            | 77.3 ms                                                     | 45.7 ms: 1.69x faster                                                                |
| logging_silent           | 94.6 ns                                                     | 57.3 ns: 1.65x faster                                                                |
| pyflate                  | 409 ms                                                      | 253 ms: 1.62x faster                                                                 |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 396 ms: 1.61x faster                                                                 |
| comprehensions           | 16.5 us                                                     | 10.4 us: 1.59x faster                                                                |
| chaos                    | 61.7 ms                                                     | 39.9 ms: 1.55x faster                                                                |
| crypto_pyaes             | 62.5 ms                                                     | 40.8 ms: 1.53x faster                                                                |
| json_dumps               | 9.16 ms                                                     | 6.10 ms: 1.50x faster                                                                |
| scimark_monte_carlo      | 57.3 ms                                                     | 38.2 ms: 1.50x faster                                                                |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.41 sec: 1.49x faster                                                               |
| richards_super           | 52.2 ms                                                     | 35.6 ms: 1.47x faster                                                                |
| generators               | 32.4 ms                                                     | 22.2 ms: 1.46x faster                                                                |
| sqlglot_parse            | 1.22 ms                                                     | 837 us: 1.45x faster                                                                 |
| pickle_pure_python       | 270 us                                                      | 187 us: 1.44x faster                                                                 |
| nbody                    | 71.3 ms                                                     | 49.7 ms: 1.43x faster                                                                |
| raytrace                 | 273 ms                                                      | 195 ms: 1.40x faster                                                                 |
| pylint                   | 350 ms                                                      | 253 ms: 1.38x faster                                                                 |
| go                       | 139 ms                                                      | 101 ms: 1.37x faster                                                                 |
| deepcopy                 | 255 us                                                      | 187 us: 1.36x faster                                                                 |
| float                    | 61.7 ms                                                     | 45.3 ms: 1.36x faster                                                                |
| sqlglot_transpile        | 1.48 ms                                                     | 1.08 ms: 1.36x faster                                                                |
| unpickle_pure_python     | 183 us                                                      | 135 us: 1.36x faster                                                                 |
| richards                 | 42.4 ms                                                     | 31.3 ms: 1.35x faster                                                                |
| asyncio_tcp              | 732 ms                                                      | 542 ms: 1.35x faster                                                                 |
| pycparser                | 930 ms                                                      | 695 ms: 1.34x faster                                                                 |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.04 ms: 1.34x faster                                                                |
| tomli_loads              | 1.67 sec                                                    | 1.28 sec: 1.31x faster                                                               |
| scimark_fft              | 187 ms                                                      | 147 ms: 1.28x faster                                                                 |
| pprint_pformat           | 1.22 sec                                                    | 973 ms: 1.25x faster                                                                 |
| pprint_safe_repr         | 592 ms                                                      | 477 ms: 1.24x faster                                                                 |
| html5lib                 | 51.0 ms                                                     | 41.9 ms: 1.22x faster                                                                |
| hexiom                   | 5.74 ms                                                     | 4.77 ms: 1.20x faster                                                                |
| scimark_lu               | 85.8 ms                                                     | 71.5 ms: 1.20x faster                                                                |
| deepcopy_reduce          | 2.20 us                                                     | 1.85 us: 1.19x faster                                                                |
| xml_etree_process        | 44.5 ms                                                     | 37.3 ms: 1.19x faster                                                                |
| thrift                   | 617 us                                                      | 519 us: 1.19x faster                                                                 |
| bench_thread_pool        | 958 us                                                      | 807 us: 1.19x faster                                                                 |
| regex_dna                | 136 ms                                                      | 116 ms: 1.18x faster                                                                 |
| regex_compile            | 106 ms                                                      | 90.5 ms: 1.17x faster                                                                |
| fannkuch                 | 256 ms                                                      | 219 ms: 1.17x faster                                                                 |
| dulwich_log              | 50.5 ms                                                     | 43.2 ms: 1.17x faster                                                                |
| coroutines               | 16.0 ms                                                     | 13.8 ms: 1.16x faster                                                                |
| scimark_sor              | 106 ms                                                      | 92.0 ms: 1.15x faster                                                                |
| mdp                      | 1.78 sec                                                    | 1.55 sec: 1.15x faster                                                               |
| django_template          | 28.9 ms                                                     | 25.6 ms: 1.13x faster                                                                |
| tornado_http             | 108 ms                                                      | 96.0 ms: 1.13x faster                                                                |
| genshi_text              | 19.8 ms                                                     | 17.8 ms: 1.11x faster                                                                |
| sympy_sum                | 107 ms                                                      | 98.0 ms: 1.09x faster                                                                |
| xml_etree_generate       | 55.5 ms                                                     | 51.4 ms: 1.08x faster                                                                |
| sqlglot_optimize         | 39.8 ms                                                     | 37.0 ms: 1.08x faster                                                                |
| regex_v8                 | 15.4 ms                                                     | 14.4 ms: 1.08x faster                                                                |
| meteor_contest           | 75.9 ms                                                     | 71.1 ms: 1.07x faster                                                                |
| xml_etree_iterparse      | 65.0 ms                                                     | 61.2 ms: 1.06x faster                                                                |
| regex_effbot             | 1.66 ms                                                     | 1.56 ms: 1.06x faster                                                                |
| genshi_xml               | 41.0 ms                                                     | 38.6 ms: 1.06x faster                                                                |
| sqlglot_normalize        | 205 ms                                                      | 195 ms: 1.05x faster                                                                 |
| nqueens                  | 66.6 ms                                                     | 63.5 ms: 1.05x faster                                                                |
| logging_format           | 6.76 us                                                     | 6.45 us: 1.05x faster                                                                |
| docutils                 | 1.92 sec                                                    | 1.83 sec: 1.05x faster                                                               |
| xml_etree_parse          | 96.8 ms                                                     | 92.8 ms: 1.04x faster                                                                |
| logging_simple           | 6.22 us                                                     | 6.03 us: 1.03x faster                                                                |
| json                     | 3.14 ms                                                     | 3.04 ms: 1.03x faster                                                                |
| sympy_integrate          | 15.3 ms                                                     | 14.9 ms: 1.03x faster                                                                |
| sympy_str                | 194 ms                                                      | 190 ms: 1.03x faster                                                                 |
| 2to3                     | 246 ms                                                      | 240 ms: 1.02x faster                                                                 |
| pidigits                 | 149 ms                                                      | 150 ms: 1.00x slower                                                                 |
| json_loads               | 14.0 us                                                     | 14.1 us: 1.01x slower                                                                |
| sympy_expand             | 314 ms                                                      | 329 ms: 1.04x slower                                                                 |
| pathlib                  | 75.7 ms                                                     | 81.1 ms: 1.07x slower                                                                |
| python_startup           | 20.6 ms                                                     | 22.7 ms: 1.10x slower                                                                |
| gc_traversal             | 1.41 ms                                                     | 1.56 ms: 1.11x slower                                                                |
| create_gc_cycles         | 800 us                                                      | 907 us: 1.13x slower                                                                 |
| telco                    | 3.94 ms                                                     | 4.51 ms: 1.14x slower                                                                |
| async_generators         | 222 ms                                                      | 258 ms: 1.16x slower                                                                 |
| python_startup_no_site   | 15.5 ms                                                     | 18.7 ms: 1.20x slower                                                                |
| coverage                 | 39.0 ms                                                     | 47.0 ms: 1.21x slower                                                                |
| bench_mp_pool            | 62.0 ms                                                     | 76.7 ms: 1.24x slower                                                                |
| Geometric mean           | (ref)                                                       | 1.24x faster                                                                         |
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240801-3.14.0a0-1b65c46-JIT/bm-20240801-pythonperf1-amd64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-1b65c46.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: unknown