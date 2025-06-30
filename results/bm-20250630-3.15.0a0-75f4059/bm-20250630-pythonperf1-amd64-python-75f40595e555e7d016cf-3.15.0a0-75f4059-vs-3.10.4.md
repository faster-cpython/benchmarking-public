# Results vs. 3.10.4

- fork: python
- ref: 75f40595e555e7d016cf
- machine: windows-amd64
- commit hash: 75f4059
- commit date: 2025-06-30
- overall geometric mean: 1.284x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 220 ms: 1.12x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.61 sec: 1.19x faster                                                     |
| html5lib       | 51.0 ms                                                     | 38.6 ms: 1.32x faster                                                      |
| Geometric mean | (ref)                                                       | 1.21x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 394 ms: 2.81x faster                                                       |
| async_tree_none         | 435 ms                                                      | 170 ms: 2.57x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 206 ms: 2.56x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 328 ms: 1.95x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.45x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 44.1 ms: 1.40x faster                                                      |
| nbody          | 71.3 ms                                                     | 65.2 ms: 1.09x faster                                                      |
| pidigits       | 149 ms                                                      | 146 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 79.0 ms: 1.34x faster                                                      |
| regex_dna      | 136 ms                                                      | 119 ms: 1.14x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 13.9 ms: 1.11x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                      |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.34 ms: 1.45x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 132 us: 1.38x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 209 us: 1.29x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.39 sec: 1.20x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 38.7 ms: 1.15x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 89.5 ms: 1.08x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.57 us: 1.06x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.4 us: 1.02x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 2.94 us: 1.08x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 20.1 us: 1.17x slower                                                      |
| pickle               | 6.85 us                                                     | 8.09 us: 1.18x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.36 us: 1.22x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.06x faster                                                               |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 25.7 ms: 1.24x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 19.5 ms: 1.26x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.58 ms: 1.37x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.2 ms: 1.30x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 34.1 ms: 1.20x faster                                                      |
| django_template | 28.9 ms                                                     | 24.0 ms: 1.20x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.27x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 102 us: 3.30x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 394 ms: 2.81x faster                                                       |
| async_tree_none          | 435 ms                                                      | 170 ms: 2.57x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 206 ms: 2.56x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 32.1 ms: 2.36x faster                                                      |
| mdp                      | 1.78 sec                                                    | 811 ms: 2.19x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.13 ms: 1.97x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 328 ms: 1.95x faster                                                       |
| go                       | 139 ms                                                      | 77.5 ms: 1.79x faster                                                      |
| pylint                   | 350 ms                                                      | 198 ms: 1.77x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 428 ms: 1.71x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 55.7 ns: 1.70x faster                                                      |
| richards_super           | 52.2 ms                                                     | 30.9 ms: 1.69x faster                                                      |
| generators               | 32.4 ms                                                     | 19.2 ms: 1.69x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 18.0 us: 1.60x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.32 sec: 1.60x faster                                                     |
| richards                 | 42.4 ms                                                     | 27.1 ms: 1.57x faster                                                      |
| raytrace                 | 273 ms                                                      | 177 ms: 1.54x faster                                                       |
| comprehensions           | 16.5 us                                                     | 10.7 us: 1.54x faster                                                      |
| chaos                    | 61.7 ms                                                     | 40.5 ms: 1.52x faster                                                      |
| deepcopy                 | 255 us                                                      | 170 us: 1.50x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.34 ms: 1.45x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 59.7 ms: 1.44x faster                                                      |
| scimark_sor              | 106 ms                                                      | 74.0 ms: 1.44x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.2 ms: 1.43x faster                                                      |
| pyflate                  | 409 ms                                                      | 287 ms: 1.43x faster                                                       |
| float                    | 61.7 ms                                                     | 44.1 ms: 1.40x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 132 us: 1.38x faster                                                       |
| mako                     | 9.03 ms                                                     | 6.58 ms: 1.37x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.19 ms: 1.37x faster                                                      |
| regex_compile            | 106 ms                                                      | 79.0 ms: 1.34x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 46.9 ms: 1.33x faster                                                      |
| pycparser                | 930 ms                                                      | 702 ms: 1.33x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 38.6 ms: 1.32x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 15.2 ms: 1.30x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 209 us: 1.29x faster                                                       |
| thrift                   | 617 us                                                      | 488 us: 1.26x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 61.9 ms: 1.25x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 40.5 ms: 1.25x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 12.4 ms: 1.24x faster                                                      |
| sympy_sum                | 107 ms                                                      | 88.2 ms: 1.21x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 34.1 ms: 1.20x faster                                                      |
| django_template          | 28.9 ms                                                     | 24.0 ms: 1.20x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 493 ms: 1.20x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.84 us: 1.20x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.39 sec: 1.20x faster                                                     |
| sqlite_synth             | 1.91 us                                                     | 1.60 us: 1.20x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.61 sec: 1.19x faster                                                     |
| pprint_pformat           | 1.22 sec                                                    | 1.02 sec: 1.19x faster                                                     |
| sympy_str                | 194 ms                                                      | 168 ms: 1.15x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 38.7 ms: 1.15x faster                                                      |
| regex_dna                | 136 ms                                                      | 119 ms: 1.14x faster                                                       |
| coroutines               | 16.0 ms                                                     | 14.2 ms: 1.13x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 857 us: 1.12x faster                                                       |
| 2to3                     | 246 ms                                                      | 220 ms: 1.12x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 13.9 ms: 1.11x faster                                                      |
| nbody                    | 71.3 ms                                                     | 65.2 ms: 1.09x faster                                                      |
| sympy_expand             | 314 ms                                                      | 288 ms: 1.09x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 89.5 ms: 1.08x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.53 ms: 1.08x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 62.1 ms: 1.07x faster                                                      |
| scimark_fft              | 187 ms                                                      | 175 ms: 1.07x faster                                                       |
| unpickle                 | 9.09 us                                                     | 8.57 us: 1.06x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 72.0 ms: 1.05x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.49 us: 1.04x faster                                                      |
| json                     | 3.14 ms                                                     | 3.02 ms: 1.04x faster                                                      |
| logging_simple           | 6.22 us                                                     | 6.00 us: 1.04x faster                                                      |
| pidigits                 | 149 ms                                                      | 146 ms: 1.02x faster                                                       |
| async_generators         | 222 ms                                                      | 226 ms: 1.02x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.4 us: 1.02x slower                                                      |
| unpack_sequence          | 39.6 ns                                                     | 40.6 ns: 1.03x slower                                                      |
| fannkuch                 | 256 ms                                                      | 267 ms: 1.05x slower                                                       |
| unpickle_list            | 2.71 us                                                     | 2.94 us: 1.08x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 20.1 us: 1.17x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.61 ms: 1.17x slower                                                      |
| pickle                   | 6.85 us                                                     | 8.09 us: 1.18x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.36 us: 1.22x slower                                                      |
| python_startup           | 20.6 ms                                                     | 25.7 ms: 1.24x slower                                                      |
| coverage                 | 39.0 ms                                                     | 48.8 ms: 1.25x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 19.5 ms: 1.26x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 95.9 ms: 1.55x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.21 ms: 1.57x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.34 ms: 1.67x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.25x faster                                                               |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_generate
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250630-3.15.0a0-75f4059/bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.284x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: unknown