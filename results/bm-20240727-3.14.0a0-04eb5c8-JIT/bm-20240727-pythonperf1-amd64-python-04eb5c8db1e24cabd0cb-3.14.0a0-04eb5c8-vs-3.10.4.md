# Results vs. 3.10.4

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: windows-amd64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.20x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 233 ms: 1.06x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.88 sec: 1.02x faster                                                     |
| html5lib       | 51.0 ms                                                     | 41.6 ms: 1.23x faster                                                      |
| tornado_http   | 108 ms                                                      | 96.3 ms: 1.13x faster                                                      |
| Geometric mean | (ref)                                                       | 1.10x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 539 ms: 2.06x faster                                                       |
| async_tree_none         | 435 ms                                                      | 216 ms: 2.01x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 265 ms: 1.99x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 395 ms: 1.61x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.91x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 51.1 ms: 1.39x faster                                                      |
| float          | 61.7 ms                                                     | 45.0 ms: 1.37x faster                                                      |
| pidigits       | 149 ms                                                      | 152 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                       | 1.23x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 91.7 ms: 1.16x faster                                                      |
| regex_dna      | 136 ms                                                      | 125 ms: 1.09x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.63 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                       | 1.06x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.08 ms: 1.51x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 183 us: 1.47x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 135 us: 1.36x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.31 sec: 1.28x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 38.1 ms: 1.17x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 52.4 ms: 1.06x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 61.5 ms: 1.06x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 92.8 ms: 1.04x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.8 us: 1.06x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.20x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 21.3 ms: 1.03x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 17.5 ms: 1.13x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.08x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.19 ms: 1.74x faster                                                      |
| django_template | 28.9 ms                                                     | 26.2 ms: 1.10x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 18.9 ms: 1.05x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 46.7 ms: 1.14x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.15x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 120 us: 2.79x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 539 ms: 2.06x faster                                                       |
| async_tree_none          | 435 ms                                                      | 216 ms: 2.01x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 265 ms: 1.99x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.34 ms: 1.79x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 16.3 us: 1.76x faster                                                      |
| mako                     | 9.03 ms                                                     | 5.19 ms: 1.74x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 57.3 ns: 1.65x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 46.8 ms: 1.65x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 395 ms: 1.61x faster                                                       |
| pyflate                  | 409 ms                                                      | 256 ms: 1.60x faster                                                       |
| comprehensions           | 16.5 us                                                     | 10.5 us: 1.57x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 40.6 ms: 1.54x faster                                                      |
| chaos                    | 61.7 ms                                                     | 40.6 ms: 1.52x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.08 ms: 1.51x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 38.2 ms: 1.50x faster                                                      |
| generators               | 32.4 ms                                                     | 21.7 ms: 1.49x faster                                                      |
| richards_super           | 52.2 ms                                                     | 35.1 ms: 1.49x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 183 us: 1.47x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 835 us: 1.46x faster                                                       |
| raytrace                 | 273 ms                                                      | 192 ms: 1.43x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.50 sec: 1.40x faster                                                     |
| nbody                    | 71.3 ms                                                     | 51.1 ms: 1.39x faster                                                      |
| pylint                   | 350 ms                                                      | 255 ms: 1.38x faster                                                       |
| go                       | 139 ms                                                      | 101 ms: 1.38x faster                                                       |
| richards                 | 42.4 ms                                                     | 30.9 ms: 1.37x faster                                                      |
| float                    | 61.7 ms                                                     | 45.0 ms: 1.37x faster                                                      |
| sqlglot_transpile        | 1.48 ms                                                     | 1.08 ms: 1.37x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 536 ms: 1.37x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 135 us: 1.36x faster                                                       |
| deepcopy                 | 255 us                                                      | 191 us: 1.33x faster                                                       |
| pycparser                | 930 ms                                                      | 709 ms: 1.31x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.09 ms: 1.30x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.31 sec: 1.28x faster                                                     |
| scimark_fft              | 187 ms                                                      | 150 ms: 1.25x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 478 ms: 1.24x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 987 ms: 1.24x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 41.6 ms: 1.23x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.74 ms: 1.21x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 42.4 ms: 1.19x faster                                                      |
| thrift                   | 617 us                                                      | 523 us: 1.18x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.88 us: 1.17x faster                                                      |
| scimark_sor              | 106 ms                                                      | 90.5 ms: 1.17x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 38.1 ms: 1.17x faster                                                      |
| coroutines               | 16.0 ms                                                     | 13.7 ms: 1.17x faster                                                      |
| regex_compile            | 106 ms                                                      | 91.7 ms: 1.16x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.55 sec: 1.15x faster                                                     |
| scimark_lu               | 85.8 ms                                                     | 75.9 ms: 1.13x faster                                                      |
| tornado_http             | 108 ms                                                      | 96.3 ms: 1.13x faster                                                      |
| fannkuch                 | 256 ms                                                      | 229 ms: 1.12x faster                                                       |
| django_template          | 28.9 ms                                                     | 26.2 ms: 1.10x faster                                                      |
| regex_dna                | 136 ms                                                      | 125 ms: 1.09x faster                                                       |
| sympy_sum                | 107 ms                                                      | 98.7 ms: 1.08x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 62.1 ms: 1.07x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 52.4 ms: 1.06x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 61.5 ms: 1.06x faster                                                      |
| 2to3                     | 246 ms                                                      | 233 ms: 1.06x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 37.8 ms: 1.05x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 72.2 ms: 1.05x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 18.9 ms: 1.05x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 92.8 ms: 1.04x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 14.7 ms: 1.04x faster                                                      |
| sympy_str                | 194 ms                                                      | 189 ms: 1.03x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 201 ms: 1.02x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.88 sec: 1.02x faster                                                     |
| regex_effbot             | 1.66 ms                                                     | 1.63 ms: 1.02x faster                                                      |
| logging_simple           | 6.22 us                                                     | 6.13 us: 1.01x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.69 us: 1.01x faster                                                      |
| pidigits                 | 149 ms                                                      | 152 ms: 1.02x slower                                                       |
| python_startup           | 20.6 ms                                                     | 21.3 ms: 1.03x slower                                                      |
| sympy_expand             | 314 ms                                                      | 329 ms: 1.05x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.8 us: 1.06x slower                                                      |
| pathlib                  | 75.7 ms                                                     | 84.7 ms: 1.12x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 17.5 ms: 1.13x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.60 ms: 1.13x slower                                                      |
| genshi_xml               | 41.0 ms                                                     | 46.7 ms: 1.14x slower                                                      |
| async_generators         | 222 ms                                                      | 257 ms: 1.16x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 935 us: 1.17x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 73.2 ms: 1.18x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.72 ms: 1.20x slower                                                      |
| coverage                 | 39.0 ms                                                     | 48.4 ms: 1.24x slower                                                      |
| bench_thread_pool        | 958 us                                                      | 3.06 ms: 3.19x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.20x faster                                                               |

Benchmark hidden because not significant (2): regex_v8, json
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240727-3.14.0a0-04eb5c8-JIT/bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown