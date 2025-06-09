# Results vs. 3.10.4

- fork: python
- ref: b150b6aca7b17efe1bb1
- machine: windows-amd64
- commit hash: b150b6a
- commit date: 2025-06-09
- overall geometric mean: 1.173x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250609-pythonperf1-amd64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 220 ms: 1.12x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.62 sec: 1.19x faster                                                     |
| html5lib       | 51.0 ms                                                     | 38.1 ms: 1.34x faster                                                      |
| Geometric mean | (ref)                                                       | 1.21x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250609-pythonperf1-amd64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 395 ms: 2.81x faster                                                       |
| async_tree_none         | 435 ms                                                      | 170 ms: 2.57x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 207 ms: 2.54x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 328 ms: 1.94x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.44x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250609-pythonperf1-amd64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 43.5 ms: 1.42x faster                                                      |
| nbody          | 71.3 ms                                                     | 62.7 ms: 1.14x faster                                                      |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250609-pythonperf1-amd64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 78.8 ms: 1.35x faster                                                      |
| regex_dna      | 136 ms                                                      | 119 ms: 1.15x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.2 ms: 1.09x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.53 ms: 1.08x faster                                                      |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250609-pythonperf1-amd64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.29 ms: 1.46x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 132 us: 1.39x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 214 us: 1.26x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.35 sec: 1.23x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 39.1 ms: 1.14x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 87.9 ms: 1.10x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.8 ms: 1.02x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 56.1 ms: 1.01x slower                                                      |
| json_loads           | 14.0 us                                                     | 14.3 us: 1.02x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250609-pythonperf1-amd64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.3 ms: 1.24x slower                                                      |
| python_startup         | 20.6 ms                                                     | 25.6 ms: 1.24x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.24x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250609-pythonperf1-amd64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.61 ms: 1.37x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.1 ms: 1.31x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 34.2 ms: 1.20x faster                                                      |
| django_template | 28.9 ms                                                     | 24.3 ms: 1.19x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.27x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250609-pythonperf1-amd64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 102 us: 3.31x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 395 ms: 2.81x faster                                                       |
| async_tree_none          | 435 ms                                                      | 170 ms: 2.57x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 207 ms: 2.54x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 31.8 ms: 2.38x faster                                                      |
| mdp                      | 1.78 sec                                                    | 808 ms: 2.20x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 328 ms: 1.94x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.18 ms: 1.92x faster                                                      |
| go                       | 139 ms                                                      | 75.0 ms: 1.85x faster                                                      |
| pylint                   | 350 ms                                                      | 197 ms: 1.78x faster                                                       |
| richards_super           | 52.2 ms                                                     | 30.7 ms: 1.70x faster                                                      |
| generators               | 32.4 ms                                                     | 19.6 ms: 1.65x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 17.9 us: 1.60x faster                                                      |
| chaos                    | 61.7 ms                                                     | 39.1 ms: 1.58x faster                                                      |
| richards                 | 42.4 ms                                                     | 27.0 ms: 1.57x faster                                                      |
| comprehensions           | 16.5 us                                                     | 10.7 us: 1.54x faster                                                      |
| raytrace                 | 273 ms                                                      | 179 ms: 1.53x faster                                                       |
| deepcopy                 | 255 us                                                      | 172 us: 1.49x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.29 ms: 1.46x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 59.0 ms: 1.45x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.01 ms: 1.43x faster                                                      |
| pyflate                  | 409 ms                                                      | 286 ms: 1.43x faster                                                       |
| scimark_sor              | 106 ms                                                      | 74.7 ms: 1.42x faster                                                      |
| float                    | 61.7 ms                                                     | 43.5 ms: 1.42x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.5 ms: 1.41x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 132 us: 1.39x faster                                                       |
| mako                     | 9.03 ms                                                     | 6.61 ms: 1.37x faster                                                      |
| regex_compile            | 106 ms                                                      | 78.8 ms: 1.35x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 38.1 ms: 1.34x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 47.4 ms: 1.32x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 15.1 ms: 1.31x faster                                                      |
| pycparser                | 930 ms                                                      | 709 ms: 1.31x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 59.0 ms: 1.31x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 214 us: 1.26x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 40.9 ms: 1.24x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.35 sec: 1.23x faster                                                     |
| sympy_integrate          | 15.3 ms                                                     | 12.4 ms: 1.23x faster                                                      |
| sympy_sum                | 107 ms                                                      | 87.4 ms: 1.22x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 34.2 ms: 1.20x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.59 us: 1.20x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.84 us: 1.20x faster                                                      |
| django_template          | 28.9 ms                                                     | 24.3 ms: 1.19x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.62 sec: 1.19x faster                                                     |
| sympy_str                | 194 ms                                                      | 168 ms: 1.15x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.9 ms: 1.15x faster                                                      |
| regex_dna                | 136 ms                                                      | 119 ms: 1.15x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 39.1 ms: 1.14x faster                                                      |
| nbody                    | 71.3 ms                                                     | 62.7 ms: 1.14x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 58.9 ms: 1.13x faster                                                      |
| 2to3                     | 246 ms                                                      | 220 ms: 1.12x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.09 sec: 1.12x faster                                                     |
| pprint_safe_repr         | 592 ms                                                      | 531 ms: 1.12x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 87.9 ms: 1.10x faster                                                      |
| sympy_expand             | 314 ms                                                      | 289 ms: 1.09x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 14.2 ms: 1.09x faster                                                      |
| scimark_fft              | 187 ms                                                      | 172 ms: 1.09x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.53 ms: 1.08x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.52 ms: 1.08x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 72.0 ms: 1.06x faster                                                      |
| json                     | 3.14 ms                                                     | 3.02 ms: 1.04x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.8 ms: 1.02x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.68 us: 1.01x faster                                                      |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                                       |
| logging_simple           | 6.22 us                                                     | 6.28 us: 1.01x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 56.1 ms: 1.01x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.3 us: 1.02x slower                                                      |
| async_generators         | 222 ms                                                      | 229 ms: 1.03x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.59 ms: 1.17x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 19.3 ms: 1.24x slower                                                      |
| python_startup           | 20.6 ms                                                     | 25.6 ms: 1.24x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.18 ms: 1.55x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.33 ms: 1.66x slower                                                      |
| logging_silent           | 94.6 ns                                                     | 325 ns: 3.43x slower                                                       |
| coverage                 | 39.0 ms                                                     | 296 ms: 7.60x slower                                                       |
| thrift                   | 617 us                                                      | 93.2 ms: 150.97x slower                                                    |
| Geometric mean           | (ref)                                                       | 1.15x faster                                                               |

Benchmark hidden because not significant (1): fannkuch
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250609-3.15.0a0-b150b6a/bm-20250609-pythonperf1-amd64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.173x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: unknown