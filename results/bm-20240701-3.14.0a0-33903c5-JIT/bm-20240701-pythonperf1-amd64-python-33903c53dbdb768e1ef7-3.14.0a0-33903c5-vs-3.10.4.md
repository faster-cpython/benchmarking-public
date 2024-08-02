# Results vs. 3.10.4

- fork: python
- ref: 33903c53dbdb768e1ef7
- machine: windows-amd64
- commit hash: 33903c5
- commit date: 2024-07-01
- overall geometric mean: 1.24x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-pythonperf1-amd64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 234 ms: 1.05x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.77 sec: 1.09x faster                                                     |
| html5lib       | 51.0 ms                                                     | 37.3 ms: 1.37x faster                                                      |
| tornado_http   | 108 ms                                                      | 83.7 ms: 1.29x faster                                                      |
| Geometric mean | (ref)                                                       | 1.19x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-pythonperf1-amd64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 210 ms: 2.07x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 540 ms: 2.05x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 257 ms: 2.05x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 386 ms: 1.65x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.95x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-pythonperf1-amd64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 50.2 ms: 1.42x faster                                                      |
| float          | 61.7 ms                                                     | 45.7 ms: 1.35x faster                                                      |
| Geometric mean | (ref)                                                       | 1.24x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-pythonperf1-amd64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 88.5 ms: 1.20x faster                                                      |
| regex_dna      | 136 ms                                                      | 120 ms: 1.13x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.61 ms: 1.03x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 22.3 ms: 1.44x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-pythonperf1-amd64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.85 ms: 1.57x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 178 us: 1.51x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 135 us: 1.36x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.27 sec: 1.32x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 38.1 ms: 1.17x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 61.0 ms: 1.06x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 92.7 ms: 1.04x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 53.4 ms: 1.04x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.1 us: 1.01x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.21x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-pythonperf1-amd64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 20.8 ms: 1.01x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 17.2 ms: 1.11x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.06x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-pythonperf1-amd64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.21 ms: 1.73x faster                                                      |
| django_template | 28.9 ms                                                     | 26.2 ms: 1.10x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 18.2 ms: 1.09x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 46.2 ms: 1.13x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.17x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-pythonperf1-amd64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 116 us: 2.90x faster                                                       |
| async_tree_none          | 435 ms                                                      | 210 ms: 2.07x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 540 ms: 2.05x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 257 ms: 2.05x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 15.9 us: 1.81x faster                                                      |
| deltablue                | 4.19 ms                                                     | 2.31 ms: 1.81x faster                                                      |
| mako                     | 9.03 ms                                                     | 5.21 ms: 1.73x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 386 ms: 1.65x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 46.9 ms: 1.65x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 59.2 ns: 1.60x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 5.85 ms: 1.57x faster                                                      |
| comprehensions           | 16.5 us                                                     | 10.6 us: 1.56x faster                                                      |
| pyflate                  | 409 ms                                                      | 263 ms: 1.56x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 472 ms: 1.55x faster                                                       |
| richards_super           | 52.2 ms                                                     | 33.9 ms: 1.54x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 41.1 ms: 1.52x faster                                                      |
| chaos                    | 61.7 ms                                                     | 40.6 ms: 1.52x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 178 us: 1.51x faster                                                       |
| pylint                   | 350 ms                                                      | 236 ms: 1.49x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 38.5 ms: 1.49x faster                                                      |
| raytrace                 | 273 ms                                                      | 185 ms: 1.48x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 823 us: 1.48x faster                                                       |
| go                       | 139 ms                                                      | 94.7 ms: 1.47x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.46 sec: 1.45x faster                                                     |
| deepcopy                 | 255 us                                                      | 179 us: 1.42x faster                                                       |
| nbody                    | 71.3 ms                                                     | 50.2 ms: 1.42x faster                                                      |
| sqlglot_transpile        | 1.48 ms                                                     | 1.05 ms: 1.41x faster                                                      |
| richards                 | 42.4 ms                                                     | 30.3 ms: 1.40x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 37.3 ms: 1.37x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 135 us: 1.36x faster                                                       |
| float                    | 61.7 ms                                                     | 45.7 ms: 1.35x faster                                                      |
| generators               | 32.4 ms                                                     | 24.5 ms: 1.32x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.27 sec: 1.32x faster                                                     |
| tornado_http             | 108 ms                                                      | 83.7 ms: 1.29x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.14 ms: 1.27x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.41 sec: 1.26x faster                                                     |
| pprint_pformat           | 1.22 sec                                                    | 985 ms: 1.24x faster                                                       |
| scimark_fft              | 187 ms                                                      | 152 ms: 1.23x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.69 ms: 1.23x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 486 ms: 1.22x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 787 us: 1.22x faster                                                       |
| regex_compile            | 106 ms                                                      | 88.5 ms: 1.20x faster                                                      |
| scimark_sor              | 106 ms                                                      | 88.6 ms: 1.20x faster                                                      |
| pycparser                | 930 ms                                                      | 781 ms: 1.19x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.85 us: 1.19x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 73.4 ms: 1.17x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 38.1 ms: 1.17x faster                                                      |
| thrift                   | 617 us                                                      | 533 us: 1.16x faster                                                       |
| sympy_sum                | 107 ms                                                      | 92.9 ms: 1.15x faster                                                      |
| fannkuch                 | 256 ms                                                      | 223 ms: 1.15x faster                                                       |
| regex_dna                | 136 ms                                                      | 120 ms: 1.13x faster                                                       |
| django_template          | 28.9 ms                                                     | 26.2 ms: 1.10x faster                                                      |
| sqlglot_optimize         | 39.8 ms                                                     | 36.2 ms: 1.10x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 14.0 ms: 1.09x faster                                                      |
| sympy_str                | 194 ms                                                      | 178 ms: 1.09x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.77 sec: 1.09x faster                                                     |
| genshi_text              | 19.8 ms                                                     | 18.2 ms: 1.09x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.23 us: 1.09x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.8 ms: 1.08x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 61.9 ms: 1.08x faster                                                      |
| logging_simple           | 6.22 us                                                     | 5.83 us: 1.07x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 61.0 ms: 1.06x faster                                                      |
| sqlglot_normalize        | 205 ms                                                      | 194 ms: 1.06x faster                                                       |
| json                     | 3.14 ms                                                     | 2.98 ms: 1.05x faster                                                      |
| 2to3                     | 246 ms                                                      | 234 ms: 1.05x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 92.7 ms: 1.04x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 53.4 ms: 1.04x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.61 ms: 1.03x faster                                                      |
| sympy_expand             | 314 ms                                                      | 307 ms: 1.02x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 75.0 ms: 1.01x faster                                                      |
| json_loads               | 14.0 us                                                     | 14.1 us: 1.01x slower                                                      |
| python_startup           | 20.6 ms                                                     | 20.8 ms: 1.01x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.56 ms: 1.10x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 17.2 ms: 1.11x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 69.1 ms: 1.11x slower                                                      |
| genshi_xml               | 41.0 ms                                                     | 46.2 ms: 1.13x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 906 us: 1.13x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.54 ms: 1.15x slower                                                      |
| async_generators         | 222 ms                                                      | 272 ms: 1.23x slower                                                       |
| coverage                 | 39.0 ms                                                     | 48.2 ms: 1.24x slower                                                      |
| regex_v8                 | 15.4 ms                                                     | 22.3 ms: 1.44x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.24x faster                                                               |

Benchmark hidden because not significant (2): pidigits, pathlib
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240701-3.14.0a0-33903c5-JIT/bm-20240701-pythonperf1-amd64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: unknown