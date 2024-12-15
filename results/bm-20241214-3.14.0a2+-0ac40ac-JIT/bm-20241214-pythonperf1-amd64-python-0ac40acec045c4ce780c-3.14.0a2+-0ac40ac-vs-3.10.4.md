# Results vs. 3.10.4

- fork: python
- ref: 0ac40acec045c4ce780c
- machine: windows-amd64
- commit hash: 0ac40ac
- commit date: 2024-12-14
- overall geometric mean: 1.253x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 219 ms: 1.12x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.72 sec: 1.11x faster                                                      |
| html5lib       | 51.0 ms                                                     | 39.2 ms: 1.30x faster                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 405 ms: 2.74x faster                                                        |
| async_tree_none         | 435 ms                                                      | 185 ms: 2.36x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 224 ms: 2.35x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 362 ms: 1.76x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.27x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 43.8 ms: 1.41x faster                                                       |
| nbody          | 71.3 ms                                                     | 54.6 ms: 1.31x faster                                                       |
| pidigits       | 149 ms                                                      | 147 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                       | 1.23x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 79.6 ms: 1.33x faster                                                       |
| regex_dna      | 136 ms                                                      | 116 ms: 1.17x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.45 ms: 1.14x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 22.5 ms: 1.45x slower                                                       |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 112 us: 1.64x faster                                                        |
| json_dumps           | 9.16 ms                                                     | 6.30 ms: 1.45x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.21 sec: 1.38x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 205 us: 1.32x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 35.3 ms: 1.26x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 86.4 ms: 1.12x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 49.9 ms: 1.11x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 59.1 ms: 1.10x faster                                                       |
| json_loads           | 14.0 us                                                     | 14.2 us: 1.02x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.25x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 17.2 ms: 1.11x slower                                                       |
| python_startup         | 20.6 ms                                                     | 23.3 ms: 1.13x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.04 ms: 1.79x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 18.5 ms: 1.07x faster                                                       |
| django_template | 28.9 ms                                                     | 27.0 ms: 1.07x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 46.9 ms: 1.14x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.16x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 114 us: 2.96x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 405 ms: 2.74x faster                                                        |
| async_tree_none          | 435 ms                                                      | 185 ms: 2.36x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 224 ms: 2.35x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.26 ms: 1.85x faster                                                       |
| mako                     | 9.03 ms                                                     | 5.04 ms: 1.79x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 16.1 us: 1.79x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 362 ms: 1.76x faster                                                        |
| logging_silent           | 94.6 ns                                                     | 54.8 ns: 1.73x faster                                                       |
| scimark_sor              | 106 ms                                                      | 62.6 ms: 1.70x faster                                                       |
| pylint                   | 350 ms                                                      | 207 ms: 1.69x faster                                                        |
| spectral_norm            | 77.3 ms                                                     | 46.9 ms: 1.65x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 112 us: 1.64x faster                                                        |
| scimark_monte_carlo      | 57.3 ms                                                     | 35.8 ms: 1.60x faster                                                       |
| go                       | 139 ms                                                      | 88.1 ms: 1.58x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 41.0 ms: 1.52x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 56.8 ms: 1.51x faster                                                       |
| chaos                    | 61.7 ms                                                     | 41.5 ms: 1.49x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 833 us: 1.46x faster                                                        |
| json_dumps               | 9.16 ms                                                     | 6.30 ms: 1.45x faster                                                       |
| pyflate                  | 409 ms                                                      | 282 ms: 1.45x faster                                                        |
| generators               | 32.4 ms                                                     | 22.8 ms: 1.42x faster                                                       |
| float                    | 61.7 ms                                                     | 43.8 ms: 1.41x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.8 us: 1.39x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.21 sec: 1.38x faster                                                      |
| richards_super           | 52.2 ms                                                     | 38.0 ms: 1.38x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.07 ms: 1.38x faster                                                       |
| deepcopy                 | 255 us                                                      | 186 us: 1.37x faster                                                        |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.00 ms: 1.36x faster                                                       |
| regex_compile            | 106 ms                                                      | 79.6 ms: 1.33x faster                                                       |
| scimark_fft              | 187 ms                                                      | 142 ms: 1.32x faster                                                        |
| pickle_pure_python       | 270 us                                                      | 205 us: 1.32x faster                                                        |
| raytrace                 | 273 ms                                                      | 209 ms: 1.31x faster                                                        |
| nbody                    | 71.3 ms                                                     | 54.6 ms: 1.31x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 39.2 ms: 1.30x faster                                                       |
| pycparser                | 930 ms                                                      | 722 ms: 1.29x faster                                                        |
| pprint_pformat           | 1.22 sec                                                    | 962 ms: 1.27x faster                                                        |
| richards                 | 42.4 ms                                                     | 33.7 ms: 1.26x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 35.3 ms: 1.26x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 40.6 ms: 1.24x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.56 us: 1.23x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 489 ms: 1.21x faster                                                        |
| deepcopy_reduce          | 2.20 us                                                     | 1.83 us: 1.21x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.3 ms: 1.21x faster                                                       |
| thrift                   | 617 us                                                      | 516 us: 1.20x faster                                                        |
| sympy_sum                | 107 ms                                                      | 90.5 ms: 1.18x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 816 us: 1.17x faster                                                        |
| regex_dna                | 136 ms                                                      | 116 ms: 1.17x faster                                                        |
| hexiom                   | 5.74 ms                                                     | 4.95 ms: 1.16x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.55 sec: 1.15x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.45 ms: 1.14x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 13.5 ms: 1.14x faster                                                       |
| 2to3                     | 246 ms                                                      | 219 ms: 1.12x faster                                                        |
| xml_etree_parse          | 96.8 ms                                                     | 86.4 ms: 1.12x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.72 sec: 1.11x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 49.9 ms: 1.11x faster                                                       |
| sympy_str                | 194 ms                                                      | 175 ms: 1.11x faster                                                        |
| json                     | 3.14 ms                                                     | 2.84 ms: 1.10x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 59.1 ms: 1.10x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 18.5 ms: 1.07x faster                                                       |
| django_template          | 28.9 ms                                                     | 27.0 ms: 1.07x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 37.2 ms: 1.07x faster                                                       |
| sympy_expand             | 314 ms                                                      | 301 ms: 1.04x faster                                                        |
| nqueens                  | 66.6 ms                                                     | 64.0 ms: 1.04x faster                                                       |
| pidigits                 | 149 ms                                                      | 147 ms: 1.02x faster                                                        |
| sqlglot_normalize        | 205 ms                                                      | 202 ms: 1.01x faster                                                        |
| meteor_contest           | 75.9 ms                                                     | 75.1 ms: 1.01x faster                                                       |
| fannkuch                 | 256 ms                                                      | 253 ms: 1.01x faster                                                        |
| logging_format           | 6.76 us                                                     | 6.70 us: 1.01x faster                                                       |
| logging_simple           | 6.22 us                                                     | 6.29 us: 1.01x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.2 us: 1.02x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.34 ms: 1.10x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 17.2 ms: 1.11x slower                                                       |
| async_generators         | 222 ms                                                      | 249 ms: 1.12x slower                                                        |
| python_startup           | 20.6 ms                                                     | 23.3 ms: 1.13x slower                                                       |
| mypy2                    | 555 ms                                                      | 631 ms: 1.14x slower                                                        |
| genshi_xml               | 41.0 ms                                                     | 46.9 ms: 1.14x slower                                                       |
| coverage                 | 39.0 ms                                                     | 44.7 ms: 1.15x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 82.1 ms: 1.32x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.97 ms: 1.40x slower                                                       |
| regex_v8                 | 15.4 ms                                                     | 22.5 ms: 1.45x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.21 ms: 1.51x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.25x faster                                                                |

Benchmark hidden because not significant (1): pathlib
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241214-3.14.0a2+-0ac40ac-JIT/bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.253x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: unknown