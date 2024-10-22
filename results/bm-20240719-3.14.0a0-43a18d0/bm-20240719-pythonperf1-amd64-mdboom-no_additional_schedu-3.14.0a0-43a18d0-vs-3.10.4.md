# Results vs. 3.10.4

- fork: mdboom
- ref: no_additional_schedu
- machine: windows-amd64
- commit hash: 43a18d0
- commit date: 2024-07-19
- overall geometric mean: 1.19x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-43a18d0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 226 ms: 1.09x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.70 sec: 1.13x faster                                                     |
| html5lib       | 51.0 ms                                                     | 40.2 ms: 1.27x faster                                                      |
| tornado_http   | 108 ms                                                      | 91.8 ms: 1.18x faster                                                      |
| Geometric mean | (ref)                                                       | 1.17x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-43a18d0 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 546 ms: 2.03x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 261 ms: 2.02x faster                                                       |
| async_tree_none         | 435 ms                                                      | 217 ms: 2.00x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 384 ms: 1.66x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.92x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-43a18d0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 56.7 ms: 1.09x faster                                                      |
| pidigits       | 149 ms                                                      | 150 ms: 1.00x slower                                                       |
| nbody          | 71.3 ms                                                     | 77.8 ms: 1.09x slower                                                      |
| Geometric mean | (ref)                                                       | 1.00x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-43a18d0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 89.7 ms: 1.18x faster                                                      |
| regex_dna      | 136 ms                                                      | 116 ms: 1.18x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 14.7 ms: 1.05x faster                                                      |
| Geometric mean | (ref)                                                       | 1.11x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-43a18d0 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.13 ms: 1.49x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 213 us: 1.26x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 152 us: 1.20x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 41.3 ms: 1.08x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.57 sec: 1.06x faster                                                     |
| xml_etree_parse      | 96.8 ms                                                     | 94.2 ms: 1.03x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 65.9 ms: 1.01x slower                                                      |
| json_loads           | 14.0 us                                                     | 14.6 us: 1.04x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 58.3 ms: 1.05x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.10x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-43a18d0 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 21.5 ms: 1.04x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 17.8 ms: 1.15x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.09x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-43a18d0 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 7.52 ms: 1.20x faster                                                      |
| django_template | 28.9 ms                                                     | 24.1 ms: 1.20x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 16.6 ms: 1.19x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 35.9 ms: 1.14x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.18x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-43a18d0 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 111 us: 3.03x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 546 ms: 2.03x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 261 ms: 2.02x faster                                                       |
| async_tree_none          | 435 ms                                                      | 217 ms: 2.00x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.14 ms: 1.96x faster                                                      |
| pylint                   | 350 ms                                                      | 210 ms: 1.67x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 384 ms: 1.66x faster                                                       |
| generators               | 32.4 ms                                                     | 20.4 ms: 1.59x faster                                                      |
| raytrace                 | 273 ms                                                      | 176 ms: 1.56x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 62.7 ns: 1.51x faster                                                      |
| richards_super           | 52.2 ms                                                     | 34.8 ms: 1.50x faster                                                      |
| go                       | 139 ms                                                      | 93.0 ms: 1.49x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.13 ms: 1.49x faster                                                      |
| chaos                    | 61.7 ms                                                     | 43.3 ms: 1.43x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 517 ms: 1.42x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.8 us: 1.40x faster                                                      |
| richards                 | 42.4 ms                                                     | 30.8 ms: 1.38x faster                                                      |
| deepcopy                 | 255 us                                                      | 187 us: 1.37x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 891 us: 1.36x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.10 ms: 1.34x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 21.7 us: 1.32x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.34 ms: 1.32x faster                                                      |
| pyflate                  | 409 ms                                                      | 313 ms: 1.31x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 67.2 ms: 1.28x faster                                                      |
| scimark_sor              | 106 ms                                                      | 83.2 ms: 1.28x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 40.2 ms: 1.27x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 213 us: 1.26x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.41 sec: 1.26x faster                                                     |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.70 sec: 1.24x faster                                                     |
| crypto_pyaes             | 62.5 ms                                                     | 51.2 ms: 1.22x faster                                                      |
| sympy_sum                | 107 ms                                                      | 88.2 ms: 1.21x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 152 us: 1.20x faster                                                       |
| mako                     | 9.03 ms                                                     | 7.52 ms: 1.20x faster                                                      |
| django_template          | 28.9 ms                                                     | 24.1 ms: 1.20x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 800 us: 1.20x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 16.6 ms: 1.19x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 12.8 ms: 1.19x faster                                                      |
| coroutines               | 16.0 ms                                                     | 13.5 ms: 1.18x faster                                                      |
| regex_compile            | 106 ms                                                      | 89.7 ms: 1.18x faster                                                      |
| tornado_http             | 108 ms                                                      | 91.8 ms: 1.18x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 48.6 ms: 1.18x faster                                                      |
| regex_dna                | 136 ms                                                      | 116 ms: 1.18x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.90 us: 1.16x faster                                                      |
| thrift                   | 617 us                                                      | 533 us: 1.16x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 35.9 ms: 1.14x faster                                                      |
| sqlglot_optimize         | 39.8 ms                                                     | 35.1 ms: 1.13x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.70 sec: 1.13x faster                                                     |
| sympy_str                | 194 ms                                                      | 173 ms: 1.12x faster                                                       |
| pycparser                | 930 ms                                                      | 830 ms: 1.12x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 187 ms: 1.10x faster                                                       |
| 2to3                     | 246 ms                                                      | 226 ms: 1.09x faster                                                       |
| float                    | 61.7 ms                                                     | 56.7 ms: 1.09x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 61.2 ms: 1.09x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.12 sec: 1.08x faster                                                     |
| xml_etree_process        | 44.5 ms                                                     | 41.3 ms: 1.08x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 72.0 ms: 1.07x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.57 sec: 1.06x faster                                                     |
| pprint_safe_repr         | 592 ms                                                      | 557 ms: 1.06x faster                                                       |
| sympy_expand             | 314 ms                                                      | 298 ms: 1.06x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 14.7 ms: 1.05x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 94.2 ms: 1.03x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.67 us: 1.01x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 75.5 ms: 1.01x faster                                                      |
| pidigits                 | 149 ms                                                      | 150 ms: 1.00x slower                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 65.9 ms: 1.01x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.6 us: 1.04x slower                                                      |
| python_startup           | 20.6 ms                                                     | 21.5 ms: 1.04x slower                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.84 ms: 1.04x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 58.3 ms: 1.05x slower                                                      |
| pathlib                  | 75.7 ms                                                     | 80.5 ms: 1.06x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 67.6 ms: 1.09x slower                                                      |
| nbody                    | 71.3 ms                                                     | 77.8 ms: 1.09x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.55 ms: 1.10x slower                                                      |
| async_generators         | 222 ms                                                      | 244 ms: 1.10x slower                                                       |
| scimark_fft              | 187 ms                                                      | 207 ms: 1.10x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 897 us: 1.12x slower                                                       |
| fannkuch                 | 256 ms                                                      | 290 ms: 1.13x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 17.8 ms: 1.15x slower                                                      |
| coverage                 | 39.0 ms                                                     | 44.9 ms: 1.15x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.86 ms: 1.23x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.19x faster                                                               |

Benchmark hidden because not significant (2): json, logging_simple
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240719-3.14.0a0-43a18d0/bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-43a18d0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: unknown