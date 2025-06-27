# Results vs. 3.10.4

- fork: python
- ref: cebae977a63f32c3c03d
- machine: windows-amd64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.296x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 220 ms: 1.12x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.62 sec: 1.19x faster                                                     |
| html5lib       | 51.0 ms                                                     | 37.9 ms: 1.35x faster                                                      |
| Geometric mean | (ref)                                                       | 1.21x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 397 ms: 2.79x faster                                                       |
| async_tree_none         | 435 ms                                                      | 169 ms: 2.58x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 206 ms: 2.55x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 328 ms: 1.94x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.45x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 43.9 ms: 1.41x faster                                                      |
| nbody          | 71.3 ms                                                     | 60.9 ms: 1.17x faster                                                      |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 79.6 ms: 1.33x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 13.1 ms: 1.18x faster                                                      |
| regex_dna      | 136 ms                                                      | 116 ms: 1.18x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.45 ms: 1.15x faster                                                      |
| Geometric mean | (ref)                                                       | 1.21x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.23 ms: 1.47x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 134 us: 1.36x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 212 us: 1.27x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.35 sec: 1.24x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 39.1 ms: 1.14x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 88.1 ms: 1.10x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.4 ms: 1.02x faster                                                      |
| Geometric mean       | (ref)                                                       | 1.17x faster                                                               |

Benchmark hidden because not significant (2): json_loads, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 25.5 ms: 1.24x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 19.3 ms: 1.25x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.24x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.38 ms: 1.42x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.2 ms: 1.31x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 33.9 ms: 1.21x faster                                                      |
| django_template | 28.9 ms                                                     | 24.6 ms: 1.17x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.27x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 100 us: 3.35x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 397 ms: 2.79x faster                                                       |
| async_tree_none          | 435 ms                                                      | 169 ms: 2.58x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 206 ms: 2.55x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 31.9 ms: 2.37x faster                                                      |
| mdp                      | 1.78 sec                                                    | 795 ms: 2.24x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 328 ms: 1.94x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.19 ms: 1.91x faster                                                      |
| go                       | 139 ms                                                      | 75.7 ms: 1.84x faster                                                      |
| pylint                   | 350 ms                                                      | 198 ms: 1.77x faster                                                       |
| richards_super           | 52.2 ms                                                     | 30.9 ms: 1.69x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 17.3 us: 1.66x faster                                                      |
| generators               | 32.4 ms                                                     | 19.8 ms: 1.64x faster                                                      |
| chaos                    | 61.7 ms                                                     | 39.3 ms: 1.57x faster                                                      |
| comprehensions           | 16.5 us                                                     | 10.6 us: 1.56x faster                                                      |
| richards                 | 42.4 ms                                                     | 27.4 ms: 1.55x faster                                                      |
| raytrace                 | 273 ms                                                      | 180 ms: 1.52x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 57.1 ms: 1.50x faster                                                      |
| deepcopy                 | 255 us                                                      | 170 us: 1.50x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.23 ms: 1.47x faster                                                      |
| pyflate                  | 409 ms                                                      | 278 ms: 1.47x faster                                                       |
| scimark_sor              | 106 ms                                                      | 72.9 ms: 1.46x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 39.5 ms: 1.45x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.00 ms: 1.43x faster                                                      |
| mako                     | 9.03 ms                                                     | 6.38 ms: 1.42x faster                                                      |
| float                    | 61.7 ms                                                     | 43.9 ms: 1.41x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 134 us: 1.36x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 57.0 ms: 1.36x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 37.9 ms: 1.35x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 46.6 ms: 1.34x faster                                                      |
| regex_compile            | 106 ms                                                      | 79.6 ms: 1.33x faster                                                      |
| pycparser                | 930 ms                                                      | 702 ms: 1.33x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 15.2 ms: 1.31x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 212 us: 1.27x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.35 sec: 1.24x faster                                                     |
| thrift                   | 617 us                                                      | 498 us: 1.24x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 12.4 ms: 1.23x faster                                                      |
| sympy_sum                | 107 ms                                                      | 87.2 ms: 1.23x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 41.2 ms: 1.23x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 33.9 ms: 1.21x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.58 us: 1.21x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.84 us: 1.20x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.62 sec: 1.19x faster                                                     |
| regex_v8                 | 15.4 ms                                                     | 13.1 ms: 1.18x faster                                                      |
| regex_dna                | 136 ms                                                      | 116 ms: 1.18x faster                                                       |
| django_template          | 28.9 ms                                                     | 24.6 ms: 1.17x faster                                                      |
| nbody                    | 71.3 ms                                                     | 60.9 ms: 1.17x faster                                                      |
| coroutines               | 16.0 ms                                                     | 13.9 ms: 1.16x faster                                                      |
| sympy_str                | 194 ms                                                      | 169 ms: 1.15x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.45 ms: 1.15x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 39.1 ms: 1.14x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.09 sec: 1.12x faster                                                     |
| 2to3                     | 246 ms                                                      | 220 ms: 1.12x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 533 ms: 1.11x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 60.6 ms: 1.10x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 88.1 ms: 1.10x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.49 ms: 1.09x faster                                                      |
| scimark_fft              | 187 ms                                                      | 172 ms: 1.09x faster                                                       |
| sympy_expand             | 314 ms                                                      | 289 ms: 1.09x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 71.7 ms: 1.06x faster                                                      |
| json                     | 3.14 ms                                                     | 2.98 ms: 1.05x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.4 ms: 1.02x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.69 us: 1.01x faster                                                      |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                                       |
| logging_simple           | 6.22 us                                                     | 6.26 us: 1.01x slower                                                      |
| async_generators         | 222 ms                                                      | 227 ms: 1.02x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.65 ms: 1.18x slower                                                      |
| python_startup           | 20.6 ms                                                     | 25.5 ms: 1.24x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 19.3 ms: 1.25x slower                                                      |
| coverage                 | 39.0 ms                                                     | 49.4 ms: 1.27x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.14 ms: 1.52x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.32 ms: 1.66x slower                                                      |
| logging_silent           | 94.6 ns                                                     | 320 ns: 3.38x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.27x faster                                                               |

Benchmark hidden because not significant (3): fannkuch, json_loads, xml_etree_generate
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250601-3.15.0a0-cebae97/bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.296x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: unknown