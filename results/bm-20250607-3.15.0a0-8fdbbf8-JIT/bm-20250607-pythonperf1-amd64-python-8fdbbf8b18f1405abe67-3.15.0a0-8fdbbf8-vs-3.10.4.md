# Results vs. 3.10.4

- fork: python
- ref: 8fdbbf8b18f1405abe67
- machine: windows-amd64
- commit hash: 8fdbbf8
- commit date: 2025-06-07
- overall geometric mean: 1.300x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-pythonperf1-amd64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 221 ms: 1.11x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.67 sec: 1.15x faster                                                     |
| html5lib       | 51.0 ms                                                     | 38.7 ms: 1.32x faster                                                      |
| Geometric mean | (ref)                                                       | 1.19x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-pythonperf1-amd64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 395 ms: 2.81x faster                                                       |
| async_tree_none         | 435 ms                                                      | 169 ms: 2.57x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 206 ms: 2.55x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 330 ms: 1.93x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.44x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-pythonperf1-amd64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 44.5 ms: 1.39x faster                                                      |
| nbody          | 71.3 ms                                                     | 59.5 ms: 1.20x faster                                                      |
| Geometric mean | (ref)                                                       | 1.18x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-pythonperf1-amd64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 78.2 ms: 1.36x faster                                                      |
| regex_dna      | 136 ms                                                      | 116 ms: 1.17x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 13.6 ms: 1.13x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.55 ms: 1.07x faster                                                      |
| Geometric mean | (ref)                                                       | 1.18x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-pythonperf1-amd64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 112 us: 1.64x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.16 sec: 1.45x faster                                                     |
| json_dumps           | 9.16 ms                                                     | 6.38 ms: 1.44x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 204 us: 1.32x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 36.7 ms: 1.21x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 87.0 ms: 1.11x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 50.8 ms: 1.09x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.8 ms: 1.02x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.4 us: 1.03x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.23x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-pythonperf1-amd64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.3 ms: 1.25x slower                                                      |
| python_startup         | 20.6 ms                                                     | 26.2 ms: 1.27x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-pythonperf1-amd64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.54 ms: 1.63x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.6 ms: 1.27x faster                                                      |
| django_template | 28.9 ms                                                     | 23.9 ms: 1.21x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 34.6 ms: 1.19x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.31x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-pythonperf1-amd64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 104 us: 3.23x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 395 ms: 2.81x faster                                                       |
| async_tree_none          | 435 ms                                                      | 169 ms: 2.57x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 206 ms: 2.55x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 32.0 ms: 2.36x faster                                                      |
| mdp                      | 1.78 sec                                                    | 809 ms: 2.20x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 330 ms: 1.93x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.22 ms: 1.88x faster                                                      |
| go                       | 139 ms                                                      | 75.7 ms: 1.83x faster                                                      |
| pylint                   | 350 ms                                                      | 201 ms: 1.74x faster                                                       |
| richards_super           | 52.2 ms                                                     | 30.7 ms: 1.70x faster                                                      |
| generators               | 32.4 ms                                                     | 19.7 ms: 1.64x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 112 us: 1.64x faster                                                       |
| mako                     | 9.03 ms                                                     | 5.54 ms: 1.63x faster                                                      |
| chaos                    | 61.7 ms                                                     | 39.2 ms: 1.57x faster                                                      |
| richards                 | 42.4 ms                                                     | 27.2 ms: 1.56x faster                                                      |
| pyflate                  | 409 ms                                                      | 264 ms: 1.55x faster                                                       |
| comprehensions           | 16.5 us                                                     | 10.7 us: 1.54x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 18.8 us: 1.53x faster                                                      |
| raytrace                 | 273 ms                                                      | 180 ms: 1.52x faster                                                       |
| deepcopy                 | 255 us                                                      | 171 us: 1.50x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.16 sec: 1.45x faster                                                     |
| scimark_monte_carlo      | 57.3 ms                                                     | 39.7 ms: 1.44x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.38 ms: 1.44x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 60.3 ms: 1.42x faster                                                      |
| scimark_sor              | 106 ms                                                      | 74.8 ms: 1.42x faster                                                      |
| float                    | 61.7 ms                                                     | 44.5 ms: 1.39x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.17 ms: 1.38x faster                                                      |
| regex_compile            | 106 ms                                                      | 78.2 ms: 1.36x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 46.7 ms: 1.34x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 204 us: 1.32x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 38.7 ms: 1.32x faster                                                      |
| pycparser                | 930 ms                                                      | 711 ms: 1.31x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 60.3 ms: 1.28x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 15.6 ms: 1.27x faster                                                      |
| thrift                   | 617 us                                                      | 492 us: 1.25x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 40.7 ms: 1.24x faster                                                      |
| sympy_sum                | 107 ms                                                      | 87.3 ms: 1.23x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 12.6 ms: 1.22x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 36.7 ms: 1.21x faster                                                      |
| django_template          | 28.9 ms                                                     | 23.9 ms: 1.21x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.82 us: 1.21x faster                                                      |
| nbody                    | 71.3 ms                                                     | 59.5 ms: 1.20x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.61 us: 1.19x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 34.6 ms: 1.19x faster                                                      |
| scimark_fft              | 187 ms                                                      | 158 ms: 1.19x faster                                                       |
| regex_dna                | 136 ms                                                      | 116 ms: 1.17x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.37 ms: 1.15x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.67 sec: 1.15x faster                                                     |
| sympy_str                | 194 ms                                                      | 170 ms: 1.14x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 521 ms: 1.14x faster                                                       |
| coroutines               | 16.0 ms                                                     | 14.1 ms: 1.14x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.07 sec: 1.14x faster                                                     |
| regex_v8                 | 15.4 ms                                                     | 13.6 ms: 1.13x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 87.0 ms: 1.11x faster                                                      |
| 2to3                     | 246 ms                                                      | 221 ms: 1.11x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 60.3 ms: 1.10x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 50.8 ms: 1.09x faster                                                      |
| fannkuch                 | 256 ms                                                      | 238 ms: 1.08x faster                                                       |
| sympy_expand             | 314 ms                                                      | 293 ms: 1.07x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.55 ms: 1.07x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 72.8 ms: 1.04x faster                                                      |
| json                     | 3.14 ms                                                     | 3.06 ms: 1.03x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.8 ms: 1.02x faster                                                      |
| logging_simple           | 6.22 us                                                     | 6.26 us: 1.01x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.4 us: 1.03x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.36 ms: 1.11x slower                                                      |
| async_generators         | 222 ms                                                      | 247 ms: 1.11x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 19.3 ms: 1.25x slower                                                      |
| python_startup           | 20.6 ms                                                     | 26.2 ms: 1.27x slower                                                      |
| coverage                 | 39.0 ms                                                     | 50.7 ms: 1.30x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.19 ms: 1.56x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.35 ms: 1.68x slower                                                      |
| logging_silent           | 94.6 ns                                                     | 325 ns: 3.43x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.27x faster                                                               |

Benchmark hidden because not significant (2): pidigits, logging_format
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-pythonperf1-amd64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.300x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: unknown