# Results vs. 3.10.4

- fork: python
- ref: 719e5c3f7111bcda5eee
- machine: windows-amd64
- commit hash: 719e5c3
- commit date: 2025-08-19
- overall geometric mean: 1.321x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250819-pythonperf1-amd64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 221 ms: 1.11x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.68 sec: 1.14x faster                                                     |
| html5lib       | 51.0 ms                                                     | 39.3 ms: 1.30x faster                                                      |
| Geometric mean | (ref)                                                       | 1.18x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250819-pythonperf1-amd64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 389 ms: 2.85x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 204 ms: 2.58x faster                                                       |
| async_tree_none         | 435 ms                                                      | 172 ms: 2.53x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 330 ms: 1.93x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.45x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250819-pythonperf1-amd64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 43.5 ms: 1.42x faster                                                      |
| nbody          | 71.3 ms                                                     | 53.4 ms: 1.34x faster                                                      |
| pidigits       | 149 ms                                                      | 146 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.24x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250819-pythonperf1-amd64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 78.4 ms: 1.35x faster                                                      |
| regex_dna      | 136 ms                                                      | 120 ms: 1.13x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.55 ms: 1.07x faster                                                      |
| Geometric mean | (ref)                                                       | 1.13x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250819-pythonperf1-amd64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 106 us: 1.73x faster                                                       |
| json_dumps           | 9.16 ms                                                     | 5.40 ms: 1.70x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.11 sec: 1.51x faster                                                     |
| pickle_pure_python   | 270 us                                                      | 205 us: 1.32x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 35.2 ms: 1.26x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 88.0 ms: 1.10x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 50.7 ms: 1.09x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.2 ms: 1.03x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.7 us: 1.05x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.27x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250819-pythonperf1-amd64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.4 ms: 1.25x slower                                                      |
| python_startup         | 20.6 ms                                                     | 25.8 ms: 1.25x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250819-pythonperf1-amd64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.41 ms: 1.67x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.5 ms: 1.28x faster                                                      |
| django_template | 28.9 ms                                                     | 24.3 ms: 1.19x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 35.2 ms: 1.17x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.31x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250819-pythonperf1-amd64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 104 us: 3.24x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 389 ms: 2.85x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 29.1 ms: 2.60x faster                                                      |
| async_tree_memoization   | 526 ms                                                      | 204 ms: 2.58x faster                                                       |
| async_tree_none          | 435 ms                                                      | 172 ms: 2.53x faster                                                       |
| mdp                      | 1.78 sec                                                    | 811 ms: 2.19x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 330 ms: 1.93x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.19 ms: 1.91x faster                                                      |
| go                       | 139 ms                                                      | 76.0 ms: 1.83x faster                                                      |
| pylint                   | 350 ms                                                      | 197 ms: 1.78x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 53.8 ns: 1.76x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 106 us: 1.73x faster                                                       |
| richards_super           | 52.2 ms                                                     | 30.5 ms: 1.71x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 5.40 ms: 1.70x faster                                                      |
| mako                     | 9.03 ms                                                     | 5.41 ms: 1.67x faster                                                      |
| generators               | 32.4 ms                                                     | 19.6 ms: 1.65x faster                                                      |
| richards                 | 42.4 ms                                                     | 26.8 ms: 1.59x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 18.2 us: 1.58x faster                                                      |
| pyflate                  | 409 ms                                                      | 264 ms: 1.55x faster                                                       |
| comprehensions           | 16.5 us                                                     | 10.7 us: 1.55x faster                                                      |
| chaos                    | 61.7 ms                                                     | 40.6 ms: 1.52x faster                                                      |
| deepcopy                 | 255 us                                                      | 169 us: 1.51x faster                                                       |
| raytrace                 | 273 ms                                                      | 181 ms: 1.51x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.11 sec: 1.51x faster                                                     |
| scimark_monte_carlo      | 57.3 ms                                                     | 39.7 ms: 1.44x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.00 ms: 1.44x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 60.1 ms: 1.43x faster                                                      |
| float                    | 61.7 ms                                                     | 43.5 ms: 1.42x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 865 ms: 1.41x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 423 ms: 1.40x faster                                                       |
| scimark_sor              | 106 ms                                                      | 76.5 ms: 1.39x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 45.6 ms: 1.37x faster                                                      |
| regex_compile            | 106 ms                                                      | 78.4 ms: 1.35x faster                                                      |
| nbody                    | 71.3 ms                                                     | 53.4 ms: 1.34x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 205 us: 1.32x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 39.3 ms: 1.30x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 15.5 ms: 1.28x faster                                                      |
| pycparser                | 930 ms                                                      | 727 ms: 1.28x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 35.2 ms: 1.26x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 40.5 ms: 1.25x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.55 us: 1.23x faster                                                      |
| thrift                   | 617 us                                                      | 501 us: 1.23x faster                                                       |
| scimark_fft              | 187 ms                                                      | 153 ms: 1.22x faster                                                       |
| sympy_sum                | 107 ms                                                      | 87.7 ms: 1.22x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 12.7 ms: 1.21x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.84 us: 1.20x faster                                                      |
| fannkuch                 | 256 ms                                                      | 214 ms: 1.20x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.28 ms: 1.19x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 64.9 ms: 1.19x faster                                                      |
| django_template          | 28.9 ms                                                     | 24.3 ms: 1.19x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 35.2 ms: 1.17x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.68 sec: 1.14x faster                                                     |
| regex_dna                | 136 ms                                                      | 120 ms: 1.13x faster                                                       |
| sympy_str                | 194 ms                                                      | 172 ms: 1.13x faster                                                       |
| coroutines               | 16.0 ms                                                     | 14.2 ms: 1.13x faster                                                      |
| 2to3                     | 246 ms                                                      | 221 ms: 1.11x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 88.0 ms: 1.10x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 50.7 ms: 1.09x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 61.0 ms: 1.09x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 70.5 ms: 1.08x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.55 ms: 1.07x faster                                                      |
| sympy_expand             | 314 ms                                                      | 295 ms: 1.07x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.38 us: 1.06x faster                                                      |
| logging_simple           | 6.22 us                                                     | 5.95 us: 1.05x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.2 ms: 1.03x faster                                                      |
| pidigits                 | 149 ms                                                      | 146 ms: 1.02x faster                                                       |
| telco                    | 3.94 ms                                                     | 4.06 ms: 1.03x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.7 us: 1.05x slower                                                      |
| async_generators         | 222 ms                                                      | 245 ms: 1.11x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 19.4 ms: 1.25x slower                                                      |
| python_startup           | 20.6 ms                                                     | 25.8 ms: 1.25x slower                                                      |
| coverage                 | 39.0 ms                                                     | 51.9 ms: 1.33x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.12 ms: 1.50x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.30 ms: 1.62x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.32x faster                                                               |

Benchmark hidden because not significant (2): json, regex_v8
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250819-3.15.0a0-719e5c3-JIT/bm-20250819-pythonperf1-amd64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.321x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: unknown