# Results vs. 3.10.4

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: windows-amd64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.17x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 234 ms: 1.05x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.75 sec: 1.10x faster                                                     |
| html5lib       | 51.0 ms                                                     | 42.0 ms: 1.21x faster                                                      |
| tornado_http   | 108 ms                                                      | 93.3 ms: 1.16x faster                                                      |
| Geometric mean | (ref)                                                       | 1.13x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 216 ms: 2.01x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 265 ms: 1.99x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 559 ms: 1.98x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 386 ms: 1.65x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.90x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 55.9 ms: 1.10x faster                                                      |
| pidigits       | 149 ms                                                      | 151 ms: 1.01x slower                                                       |
| nbody          | 71.3 ms                                                     | 83.2 ms: 1.17x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 90.4 ms: 1.17x faster                                                      |
| regex_dna      | 136 ms                                                      | 119 ms: 1.15x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 17.5 ms: 1.13x slower                                                      |
| Geometric mean | (ref)                                                       | 1.06x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.26 ms: 1.46x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 213 us: 1.27x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 151 us: 1.22x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 41.2 ms: 1.08x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.59 sec: 1.05x faster                                                     |
| xml_etree_parse      | 96.8 ms                                                     | 92.8 ms: 1.04x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 65.9 ms: 1.01x slower                                                      |
| json_loads           | 14.0 us                                                     | 14.4 us: 1.03x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 58.9 ms: 1.06x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.10x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 22.2 ms: 1.08x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 18.4 ms: 1.19x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 7.07 ms: 1.28x faster                                                      |
| django_template | 28.9 ms                                                     | 24.6 ms: 1.17x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 17.3 ms: 1.14x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 36.9 ms: 1.11x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.18x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 114 us: 2.95x faster                                                       |
| async_tree_none          | 435 ms                                                      | 216 ms: 2.01x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 265 ms: 1.99x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 559 ms: 1.98x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.25 ms: 1.86x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 386 ms: 1.65x faster                                                       |
| generators               | 32.4 ms                                                     | 20.3 ms: 1.59x faster                                                      |
| pylint                   | 350 ms                                                      | 227 ms: 1.55x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 63.7 ns: 1.49x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.26 ms: 1.46x faster                                                      |
| richards_super           | 52.2 ms                                                     | 36.4 ms: 1.44x faster                                                      |
| go                       | 139 ms                                                      | 96.8 ms: 1.44x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 20.6 us: 1.40x faster                                                      |
| raytrace                 | 273 ms                                                      | 197 ms: 1.39x faster                                                       |
| chaos                    | 61.7 ms                                                     | 44.4 ms: 1.39x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 533 ms: 1.37x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 886 us: 1.37x faster                                                       |
| comprehensions           | 16.5 us                                                     | 12.0 us: 1.37x faster                                                      |
| deepcopy                 | 255 us                                                      | 187 us: 1.37x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 63.2 ms: 1.36x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.56 sec: 1.36x faster                                                     |
| sqlglot_transpile        | 1.48 ms                                                     | 1.11 ms: 1.33x faster                                                      |
| richards                 | 42.4 ms                                                     | 32.3 ms: 1.31x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.43 ms: 1.30x faster                                                      |
| pyflate                  | 409 ms                                                      | 319 ms: 1.28x faster                                                       |
| mako                     | 9.03 ms                                                     | 7.07 ms: 1.28x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 213 us: 1.27x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 50.6 ms: 1.24x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 151 us: 1.22x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 42.0 ms: 1.21x faster                                                      |
| scimark_sor              | 106 ms                                                      | 88.0 ms: 1.21x faster                                                      |
| thrift                   | 617 us                                                      | 519 us: 1.19x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 805 us: 1.19x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 42.7 ms: 1.18x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.51 sec: 1.18x faster                                                     |
| sympy_sum                | 107 ms                                                      | 90.6 ms: 1.18x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.87 us: 1.18x faster                                                      |
| django_template          | 28.9 ms                                                     | 24.6 ms: 1.17x faster                                                      |
| regex_compile            | 106 ms                                                      | 90.4 ms: 1.17x faster                                                      |
| tornado_http             | 108 ms                                                      | 93.3 ms: 1.16x faster                                                      |
| coroutines               | 16.0 ms                                                     | 13.8 ms: 1.16x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.3 ms: 1.15x faster                                                      |
| regex_dna                | 136 ms                                                      | 119 ms: 1.15x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 17.3 ms: 1.14x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 50.9 ms: 1.13x faster                                                      |
| pycparser                | 930 ms                                                      | 834 ms: 1.12x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 36.9 ms: 1.11x faster                                                      |
| float                    | 61.7 ms                                                     | 55.9 ms: 1.10x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.75 sec: 1.10x faster                                                     |
| sympy_str                | 194 ms                                                      | 178 ms: 1.09x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 70.9 ms: 1.09x faster                                                      |
| sqlglot_optimize         | 39.8 ms                                                     | 36.8 ms: 1.08x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 41.2 ms: 1.08x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.15 sec: 1.06x faster                                                     |
| regex_effbot             | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.59 sec: 1.05x faster                                                     |
| 2to3                     | 246 ms                                                      | 234 ms: 1.05x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 196 ms: 1.05x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 566 ms: 1.05x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 92.8 ms: 1.04x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 64.5 ms: 1.03x faster                                                      |
| sympy_expand             | 314 ms                                                      | 306 ms: 1.03x faster                                                       |
| json                     | 3.14 ms                                                     | 3.17 ms: 1.01x slower                                                      |
| pidigits                 | 149 ms                                                      | 151 ms: 1.01x slower                                                       |
| meteor_contest           | 75.9 ms                                                     | 77.0 ms: 1.01x slower                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 65.9 ms: 1.01x slower                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.79 ms: 1.02x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.4 us: 1.03x slower                                                      |
| logging_format           | 6.76 us                                                     | 6.98 us: 1.03x slower                                                      |
| logging_simple           | 6.22 us                                                     | 6.43 us: 1.03x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 58.9 ms: 1.06x slower                                                      |
| pathlib                  | 75.7 ms                                                     | 80.9 ms: 1.07x slower                                                      |
| python_startup           | 20.6 ms                                                     | 22.2 ms: 1.08x slower                                                      |
| async_generators         | 222 ms                                                      | 240 ms: 1.08x slower                                                       |
| scimark_fft              | 187 ms                                                      | 206 ms: 1.10x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.55 ms: 1.10x slower                                                      |
| regex_v8                 | 15.4 ms                                                     | 17.5 ms: 1.13x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 908 us: 1.14x slower                                                       |
| fannkuch                 | 256 ms                                                      | 291 ms: 1.14x slower                                                       |
| nbody                    | 71.3 ms                                                     | 83.2 ms: 1.17x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 72.7 ms: 1.17x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 18.4 ms: 1.19x slower                                                      |
| coverage                 | 39.0 ms                                                     | 47.0 ms: 1.20x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.89 ms: 1.24x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.17x faster                                                               |
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: unknown