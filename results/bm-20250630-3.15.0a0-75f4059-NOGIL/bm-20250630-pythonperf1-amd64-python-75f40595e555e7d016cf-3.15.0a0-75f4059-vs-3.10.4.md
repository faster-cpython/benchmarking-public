# Results vs. 3.10.4

- fork: python
- ref: 75f40595e555e7d016cf
- machine: windows-amd64
- commit hash: 75f4059
- commit date: 2025-06-30
- overall geometric mean: 1.132x faster
- HPT reliability: 99.68%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 230 ms: 1.07x faster                                                       |
| docutils       | 1.92 sec                                                    | 2.93 sec: 1.53x slower                                                     |
| html5lib       | 51.0 ms                                                     | 41.6 ms: 1.23x faster                                                      |
| Geometric mean | (ref)                                                       | 1.05x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 361 ms: 3.07x faster                                                       |
| async_tree_none         | 435 ms                                                      | 175 ms: 2.49x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 216 ms: 2.44x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 340 ms: 1.88x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.43x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 46.2 ms: 1.34x faster                                                      |
| pidigits       | 149 ms                                                      | 137 ms: 1.09x faster                                                       |
| nbody          | 71.3 ms                                                     | 83.3 ms: 1.17x slower                                                      |
| Geometric mean | (ref)                                                       | 1.08x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 114 ms: 1.19x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 13.6 ms: 1.14x faster                                                      |
| regex_compile  | 106 ms                                                      | 96.3 ms: 1.10x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.62 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                       | 1.11x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.68 ms: 1.37x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 156 us: 1.18x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 234 us: 1.15x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 58.6 ms: 1.11x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 90.7 ms: 1.07x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 45.8 ms: 1.03x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.05 us: 1.11x slower                                                      |
| unpickle             | 9.09 us                                                     | 10.2 us: 1.12x slower                                                      |
| json_loads           | 14.0 us                                                     | 16.0 us: 1.14x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 3.09 us: 1.14x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 64.4 ms: 1.16x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 20.6 us: 1.20x slower                                                      |
| pickle               | 6.85 us                                                     | 8.39 us: 1.22x slower                                                      |
| tomli_loads          | 1.67 sec                                                    | 2.71 sec: 1.62x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.05x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 25.9 ms: 1.26x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 19.6 ms: 1.26x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 28.9 ms                                                     | 27.6 ms: 1.05x faster                                                      |
| mako            | 9.03 ms                                                     | 9.77 ms: 1.08x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io            | 1.11 sec                                                    | 361 ms: 3.07x faster                                                       |
| typing_runtime_protocols | 336 us                                                      | 131 us: 2.57x faster                                                       |
| async_tree_none          | 435 ms                                                      | 175 ms: 2.49x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 216 ms: 2.44x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 32.1 ms: 2.36x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 340 ms: 1.88x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.48 ms: 1.69x faster                                                      |
| pylint                   | 350 ms                                                      | 220 ms: 1.59x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.15 sec: 1.54x faster                                                     |
| asyncio_tcp              | 732 ms                                                      | 486 ms: 1.50x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 63.1 ns: 1.50x faster                                                      |
| go                       | 139 ms                                                      | 93.7 ms: 1.48x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.33 us: 1.43x faster                                                      |
| generators               | 32.4 ms                                                     | 23.2 ms: 1.40x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.68 ms: 1.37x faster                                                      |
| comprehensions           | 16.5 us                                                     | 12.1 us: 1.36x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 21.2 us: 1.36x faster                                                      |
| float                    | 61.7 ms                                                     | 46.2 ms: 1.34x faster                                                      |
| chaos                    | 61.7 ms                                                     | 46.9 ms: 1.32x faster                                                      |
| richards_super           | 52.2 ms                                                     | 39.7 ms: 1.31x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 65.9 ms: 1.30x faster                                                      |
| pyflate                  | 409 ms                                                      | 315 ms: 1.30x faster                                                       |
| raytrace                 | 273 ms                                                      | 213 ms: 1.28x faster                                                       |
| pycparser                | 930 ms                                                      | 738 ms: 1.26x faster                                                       |
| deepcopy                 | 255 us                                                      | 205 us: 1.25x faster                                                       |
| richards                 | 42.4 ms                                                     | 34.0 ms: 1.25x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.62 ms: 1.24x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 41.6 ms: 1.23x faster                                                      |
| scimark_sor              | 106 ms                                                      | 88.9 ms: 1.19x faster                                                      |
| regex_dna                | 136 ms                                                      | 114 ms: 1.19x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 156 us: 1.18x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 43.1 ms: 1.17x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 49.7 ms: 1.15x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 234 us: 1.15x faster                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.24 ms: 1.14x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 13.6 ms: 1.14x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 58.6 ms: 1.11x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 56.4 ms: 1.11x faster                                                      |
| regex_compile            | 106 ms                                                      | 96.3 ms: 1.10x faster                                                      |
| pidigits                 | 149 ms                                                      | 137 ms: 1.09x faster                                                       |
| coroutines               | 16.0 ms                                                     | 14.8 ms: 1.08x faster                                                      |
| sympy_sum                | 107 ms                                                      | 99.7 ms: 1.07x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 14.3 ms: 1.07x faster                                                      |
| 2to3                     | 246 ms                                                      | 230 ms: 1.07x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 90.7 ms: 1.07x faster                                                      |
| thrift                   | 617 us                                                      | 580 us: 1.06x faster                                                       |
| unpack_sequence          | 39.6 ns                                                     | 37.8 ns: 1.05x faster                                                      |
| django_template          | 28.9 ms                                                     | 27.6 ms: 1.05x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 569 ms: 1.04x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 74.4 ms: 1.04x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 2.13 us: 1.03x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.62 ms: 1.02x faster                                                      |
| sympy_str                | 194 ms                                                      | 191 ms: 1.02x faster                                                       |
| json                     | 3.14 ms                                                     | 3.10 ms: 1.01x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 45.8 ms: 1.03x slower                                                      |
| sympy_expand             | 314 ms                                                      | 332 ms: 1.06x slower                                                       |
| logging_format           | 6.76 us                                                     | 7.31 us: 1.08x slower                                                      |
| mako                     | 9.03 ms                                                     | 9.77 ms: 1.08x slower                                                      |
| logging_simple           | 6.22 us                                                     | 6.81 us: 1.09x slower                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 2.32 sec: 1.10x slower                                                     |
| nqueens                  | 66.6 ms                                                     | 73.4 ms: 1.10x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.05 us: 1.11x slower                                                      |
| unpickle                 | 9.09 us                                                     | 10.2 us: 1.12x slower                                                      |
| bench_thread_pool        | 958 us                                                      | 1.08 ms: 1.13x slower                                                      |
| json_loads               | 14.0 us                                                     | 16.0 us: 1.14x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 3.09 us: 1.14x slower                                                      |
| meteor_contest           | 75.9 ms                                                     | 86.8 ms: 1.14x slower                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 3.12 ms: 1.14x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 64.4 ms: 1.16x slower                                                      |
| scimark_fft              | 187 ms                                                      | 219 ms: 1.17x slower                                                       |
| fannkuch                 | 256 ms                                                      | 299 ms: 1.17x slower                                                       |
| nbody                    | 71.3 ms                                                     | 83.3 ms: 1.17x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 20.6 us: 1.20x slower                                                      |
| async_generators         | 222 ms                                                      | 266 ms: 1.20x slower                                                       |
| pickle                   | 6.85 us                                                     | 8.39 us: 1.22x slower                                                      |
| python_startup           | 20.6 ms                                                     | 25.9 ms: 1.26x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 19.6 ms: 1.26x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 80.1 ms: 1.29x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.06 ms: 1.32x slower                                                      |
| telco                    | 3.94 ms                                                     | 5.55 ms: 1.41x slower                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.77 sec: 1.45x slower                                                     |
| docutils                 | 1.92 sec                                                    | 2.93 sec: 1.53x slower                                                     |
| tomli_loads              | 1.67 sec                                                    | 2.71 sec: 1.62x slower                                                     |
| coverage                 | 39.0 ms                                                     | 67.6 ms: 1.73x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.11x faster                                                               |

Benchmark hidden because not significant (2): genshi_xml, genshi_text
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250630-3.15.0a0-75f4059-NOGIL/bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.132x faster

# HPT report

- Reliability score: 99.68% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown