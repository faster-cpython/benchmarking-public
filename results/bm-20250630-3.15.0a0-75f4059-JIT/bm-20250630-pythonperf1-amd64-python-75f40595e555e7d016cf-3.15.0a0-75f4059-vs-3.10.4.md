# Results vs. 3.10.4

- fork: python
- ref: 75f40595e555e7d016cf
- machine: windows-amd64
- commit hash: 75f4059
- commit date: 2025-06-30
- overall geometric mean: 1.301x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 221 ms: 1.11x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.68 sec: 1.14x faster                                                     |
| html5lib       | 51.0 ms                                                     | 38.8 ms: 1.31x faster                                                      |
| Geometric mean | (ref)                                                       | 1.19x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 400 ms: 2.77x faster                                                       |
| async_tree_none         | 435 ms                                                      | 171 ms: 2.54x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 208 ms: 2.53x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 329 ms: 1.94x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.42x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 44.9 ms: 1.37x faster                                                      |
| nbody          | 71.3 ms                                                     | 53.7 ms: 1.33x faster                                                      |
| pidigits       | 149 ms                                                      | 147 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.23x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 78.9 ms: 1.34x faster                                                      |
| regex_dna      | 136 ms                                                      | 120 ms: 1.14x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.0 ms: 1.10x faster                                                      |
| Geometric mean | (ref)                                                       | 1.14x faster                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 108 us: 1.70x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.14 sec: 1.47x faster                                                     |
| json_dumps           | 9.16 ms                                                     | 6.28 ms: 1.46x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 205 us: 1.31x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 35.9 ms: 1.24x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 88.9 ms: 1.09x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 51.2 ms: 1.08x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.54 us: 1.06x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.9 ms: 1.02x faster                                                      |
| unpickle_list        | 2.71 us                                                     | 2.79 us: 1.03x slower                                                      |
| json_loads           | 14.0 us                                                     | 14.4 us: 1.03x slower                                                      |
| pickle               | 6.85 us                                                     | 7.60 us: 1.11x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 19.9 us: 1.16x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.43 us: 1.25x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.11x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.5 ms: 1.26x slower                                                      |
| python_startup         | 20.6 ms                                                     | 26.0 ms: 1.26x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.39 ms: 1.68x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.6 ms: 1.27x faster                                                      |
| django_template | 28.9 ms                                                     | 24.3 ms: 1.19x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 35.2 ms: 1.16x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.31x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 103 us: 3.27x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 400 ms: 2.77x faster                                                       |
| async_tree_none          | 435 ms                                                      | 171 ms: 2.54x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 208 ms: 2.53x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 31.7 ms: 2.39x faster                                                      |
| mdp                      | 1.78 sec                                                    | 803 ms: 2.22x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 329 ms: 1.94x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.26 ms: 1.85x faster                                                      |
| go                       | 139 ms                                                      | 78.8 ms: 1.76x faster                                                      |
| pylint                   | 350 ms                                                      | 201 ms: 1.74x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 55.6 ns: 1.70x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 108 us: 1.70x faster                                                       |
| mako                     | 9.03 ms                                                     | 5.39 ms: 1.68x faster                                                      |
| richards_super           | 52.2 ms                                                     | 31.8 ms: 1.64x faster                                                      |
| generators               | 32.4 ms                                                     | 19.7 ms: 1.64x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 18.0 us: 1.60x faster                                                      |
| pyflate                  | 409 ms                                                      | 258 ms: 1.58x faster                                                       |
| comprehensions           | 16.5 us                                                     | 10.7 us: 1.54x faster                                                      |
| raytrace                 | 273 ms                                                      | 179 ms: 1.53x faster                                                       |
| richards                 | 42.4 ms                                                     | 27.8 ms: 1.53x faster                                                      |
| chaos                    | 61.7 ms                                                     | 40.8 ms: 1.51x faster                                                      |
| deepcopy                 | 255 us                                                      | 169 us: 1.51x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.14 sec: 1.47x faster                                                     |
| json_dumps               | 9.16 ms                                                     | 6.28 ms: 1.46x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.45 sec: 1.45x faster                                                     |
| asyncio_tcp              | 732 ms                                                      | 514 ms: 1.42x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 60.9 ms: 1.41x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 41.1 ms: 1.39x faster                                                      |
| float                    | 61.7 ms                                                     | 44.9 ms: 1.37x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.19 ms: 1.37x faster                                                      |
| regex_compile            | 106 ms                                                      | 78.9 ms: 1.34x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 46.6 ms: 1.34x faster                                                      |
| scimark_sor              | 106 ms                                                      | 79.3 ms: 1.34x faster                                                      |
| pycparser                | 930 ms                                                      | 701 ms: 1.33x faster                                                       |
| nbody                    | 71.3 ms                                                     | 53.7 ms: 1.33x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 38.8 ms: 1.31x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 205 us: 1.31x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 931 ms: 1.31x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 453 ms: 1.31x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 15.6 ms: 1.27x faster                                                      |
| thrift                   | 617 us                                                      | 490 us: 1.26x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 35.9 ms: 1.24x faster                                                      |
| scimark_fft              | 187 ms                                                      | 151 ms: 1.24x faster                                                       |
| sympy_sum                | 107 ms                                                      | 87.0 ms: 1.23x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 41.1 ms: 1.23x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.56 us: 1.22x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 63.5 ms: 1.22x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 12.6 ms: 1.21x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.27 ms: 1.20x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.85 us: 1.19x faster                                                      |
| django_template          | 28.9 ms                                                     | 24.3 ms: 1.19x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 35.2 ms: 1.16x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.68 sec: 1.14x faster                                                     |
| regex_dna                | 136 ms                                                      | 120 ms: 1.14x faster                                                       |
| sympy_str                | 194 ms                                                      | 172 ms: 1.13x faster                                                       |
| fannkuch                 | 256 ms                                                      | 228 ms: 1.12x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 860 us: 1.11x faster                                                       |
| 2to3                     | 246 ms                                                      | 221 ms: 1.11x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 60.2 ms: 1.11x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.5 ms: 1.10x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 14.0 ms: 1.10x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 88.9 ms: 1.09x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 51.2 ms: 1.08x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 71.1 ms: 1.07x faster                                                      |
| unpickle                 | 9.09 us                                                     | 8.54 us: 1.06x faster                                                      |
| sympy_expand             | 314 ms                                                      | 296 ms: 1.06x faster                                                       |
| json                     | 3.14 ms                                                     | 3.01 ms: 1.04x faster                                                      |
| unpack_sequence          | 39.6 ns                                                     | 38.5 ns: 1.03x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.65 us: 1.02x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.9 ms: 1.02x faster                                                      |
| pidigits                 | 149 ms                                                      | 147 ms: 1.01x faster                                                       |
| unpickle_list            | 2.71 us                                                     | 2.79 us: 1.03x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.4 us: 1.03x slower                                                      |
| pickle                   | 6.85 us                                                     | 7.60 us: 1.11x slower                                                      |
| async_generators         | 222 ms                                                      | 248 ms: 1.12x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.41 ms: 1.12x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 19.9 us: 1.16x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.43 us: 1.25x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 19.5 ms: 1.26x slower                                                      |
| python_startup           | 20.6 ms                                                     | 26.0 ms: 1.26x slower                                                      |
| coverage                 | 39.0 ms                                                     | 51.3 ms: 1.32x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 95.6 ms: 1.54x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.18 ms: 1.55x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.33 ms: 1.67x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.27x faster                                                               |

Benchmark hidden because not significant (2): regex_effbot, logging_simple
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250630-3.15.0a0-75f4059-JIT/bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.301x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: unknown