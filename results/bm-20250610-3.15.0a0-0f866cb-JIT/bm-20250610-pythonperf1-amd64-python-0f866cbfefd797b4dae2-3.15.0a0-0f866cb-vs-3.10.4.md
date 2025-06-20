# Results vs. 3.10.4

- fork: python
- ref: 0f866cbfefd797b4dae2
- machine: windows-amd64
- commit hash: 0f866cb
- commit date: 2025-06-10
- overall geometric mean: 1.302x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 221 ms: 1.11x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.66 sec: 1.16x faster                                                     |
| html5lib       | 51.0 ms                                                     | 38.4 ms: 1.33x faster                                                      |
| Geometric mean | (ref)                                                       | 1.20x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 398 ms: 2.79x faster                                                       |
| async_tree_none         | 435 ms                                                      | 169 ms: 2.58x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 205 ms: 2.56x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 335 ms: 1.91x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.43x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 43.8 ms: 1.41x faster                                                      |
| nbody          | 71.3 ms                                                     | 58.5 ms: 1.22x faster                                                      |
| Geometric mean | (ref)                                                       | 1.20x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 78.3 ms: 1.35x faster                                                      |
| regex_dna      | 136 ms                                                      | 119 ms: 1.14x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.1 ms: 1.09x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.56 ms: 1.06x faster                                                      |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 112 us: 1.63x faster                                                       |
| json_dumps           | 9.16 ms                                                     | 6.27 ms: 1.46x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.15 sec: 1.46x faster                                                     |
| pickle_pure_python   | 270 us                                                      | 204 us: 1.32x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 36.3 ms: 1.22x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 51.5 ms: 1.08x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 91.2 ms: 1.06x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.4 us: 1.02x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.23x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.5 ms: 1.26x slower                                                      |
| python_startup         | 20.6 ms                                                     | 26.0 ms: 1.26x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.61 ms: 1.61x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.5 ms: 1.28x faster                                                      |
| django_template | 28.9 ms                                                     | 23.9 ms: 1.21x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 34.6 ms: 1.19x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.31x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 106 us: 3.17x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 398 ms: 2.79x faster                                                       |
| async_tree_none          | 435 ms                                                      | 169 ms: 2.58x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 205 ms: 2.56x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 31.9 ms: 2.38x faster                                                      |
| mdp                      | 1.78 sec                                                    | 806 ms: 2.21x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 335 ms: 1.91x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.21 ms: 1.89x faster                                                      |
| go                       | 139 ms                                                      | 76.3 ms: 1.82x faster                                                      |
| pylint                   | 350 ms                                                      | 201 ms: 1.75x faster                                                       |
| richards_super           | 52.2 ms                                                     | 30.9 ms: 1.69x faster                                                      |
| generators               | 32.4 ms                                                     | 19.6 ms: 1.66x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 112 us: 1.63x faster                                                       |
| mako                     | 9.03 ms                                                     | 5.61 ms: 1.61x faster                                                      |
| chaos                    | 61.7 ms                                                     | 38.9 ms: 1.59x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 18.3 us: 1.57x faster                                                      |
| pyflate                  | 409 ms                                                      | 261 ms: 1.57x faster                                                       |
| richards                 | 42.4 ms                                                     | 27.3 ms: 1.55x faster                                                      |
| raytrace                 | 273 ms                                                      | 178 ms: 1.54x faster                                                       |
| deepcopy                 | 255 us                                                      | 168 us: 1.52x faster                                                       |
| comprehensions           | 16.5 us                                                     | 10.9 us: 1.51x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.27 ms: 1.46x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.15 sec: 1.46x faster                                                     |
| scimark_lu               | 85.8 ms                                                     | 59.0 ms: 1.45x faster                                                      |
| float                    | 61.7 ms                                                     | 43.8 ms: 1.41x faster                                                      |
| scimark_sor              | 106 ms                                                      | 75.5 ms: 1.41x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.8 ms: 1.41x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.12 ms: 1.39x faster                                                      |
| regex_compile            | 106 ms                                                      | 78.3 ms: 1.35x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 38.4 ms: 1.33x faster                                                      |
| pycparser                | 930 ms                                                      | 701 ms: 1.33x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 47.1 ms: 1.33x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 204 us: 1.32x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 59.9 ms: 1.29x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 15.5 ms: 1.28x faster                                                      |
| thrift                   | 617 us                                                      | 494 us: 1.25x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 41.1 ms: 1.23x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.56 us: 1.23x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 36.3 ms: 1.22x faster                                                      |
| sympy_sum                | 107 ms                                                      | 87.5 ms: 1.22x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.80 us: 1.22x faster                                                      |
| nbody                    | 71.3 ms                                                     | 58.5 ms: 1.22x faster                                                      |
| scimark_fft              | 187 ms                                                      | 154 ms: 1.21x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 12.6 ms: 1.21x faster                                                      |
| django_template          | 28.9 ms                                                     | 23.9 ms: 1.21x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.27 ms: 1.20x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 34.6 ms: 1.19x faster                                                      |
| coroutines               | 16.0 ms                                                     | 13.8 ms: 1.16x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.66 sec: 1.16x faster                                                     |
| pprint_pformat           | 1.22 sec                                                    | 1.06 sec: 1.15x faster                                                     |
| regex_dna                | 136 ms                                                      | 119 ms: 1.14x faster                                                       |
| sympy_str                | 194 ms                                                      | 172 ms: 1.13x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 524 ms: 1.13x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 59.7 ms: 1.12x faster                                                      |
| 2to3                     | 246 ms                                                      | 221 ms: 1.11x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 14.1 ms: 1.09x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 51.5 ms: 1.08x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.56 ms: 1.06x faster                                                      |
| sympy_expand             | 314 ms                                                      | 296 ms: 1.06x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 91.2 ms: 1.06x faster                                                      |
| fannkuch                 | 256 ms                                                      | 244 ms: 1.05x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 73.2 ms: 1.04x faster                                                      |
| json                     | 3.14 ms                                                     | 3.06 ms: 1.02x faster                                                      |
| logging_simple           | 6.22 us                                                     | 6.35 us: 1.02x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.4 us: 1.02x slower                                                      |
| async_generators         | 222 ms                                                      | 243 ms: 1.09x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.37 ms: 1.11x slower                                                      |
| coverage                 | 39.0 ms                                                     | 47.9 ms: 1.23x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 19.5 ms: 1.26x slower                                                      |
| python_startup           | 20.6 ms                                                     | 26.0 ms: 1.26x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.15 ms: 1.52x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.33 ms: 1.66x slower                                                      |
| logging_silent           | 94.6 ns                                                     | 316 ns: 3.34x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.27x faster                                                               |

Benchmark hidden because not significant (3): xml_etree_iterparse, pidigits, logging_format
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250610-3.15.0a0-0f866cb-JIT/bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.302x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: unknown