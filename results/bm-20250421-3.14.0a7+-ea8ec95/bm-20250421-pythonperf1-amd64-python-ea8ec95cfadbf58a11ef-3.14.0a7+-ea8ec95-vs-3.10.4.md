# Results vs. 3.10.4

- fork: python
- ref: ea8ec95cfadbf58a11ef
- machine: windows-amd64
- commit hash: ea8ec95
- commit date: 2025-04-21
- overall geometric mean: 1.292x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250421-pythonperf1-amd64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 220 ms: 1.12x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.65 sec: 1.16x faster                                                      |
| html5lib       | 51.0 ms                                                     | 37.7 ms: 1.35x faster                                                       |
| Geometric mean | (ref)                                                       | 1.21x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250421-pythonperf1-amd64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 408 ms: 2.72x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 204 ms: 2.58x faster                                                        |
| async_tree_none         | 435 ms                                                      | 180 ms: 2.42x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 329 ms: 1.94x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.40x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250421-pythonperf1-amd64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 42.3 ms: 1.46x faster                                                       |
| nbody          | 71.3 ms                                                     | 62.2 ms: 1.15x faster                                                       |
| Geometric mean | (ref)                                                       | 1.19x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250421-pythonperf1-amd64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 79.6 ms: 1.33x faster                                                       |
| regex_dna      | 136 ms                                                      | 115 ms: 1.19x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.41 ms: 1.18x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 13.4 ms: 1.16x faster                                                       |
| Geometric mean | (ref)                                                       | 1.21x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250421-pythonperf1-amd64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 134 us: 1.36x faster                                                        |
| json_dumps           | 9.16 ms                                                     | 6.80 ms: 1.35x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 209 us: 1.29x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.35 sec: 1.24x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 39.5 ms: 1.12x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 89.4 ms: 1.08x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.7 ms: 1.02x faster                                                       |
| json_loads           | 14.0 us                                                     | 14.9 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.15x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250421-pythonperf1-amd64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 26.3 ms: 1.28x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 20.5 ms: 1.32x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.30x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250421-pythonperf1-amd64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.61 ms: 1.37x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 15.4 ms: 1.29x faster                                                       |
| django_template | 28.9 ms                                                     | 24.0 ms: 1.20x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 34.3 ms: 1.20x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.26x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250421-pythonperf1-amd64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 105 us: 3.19x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 408 ms: 2.72x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 204 ms: 2.58x faster                                                        |
| async_tree_none          | 435 ms                                                      | 180 ms: 2.42x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 32.4 ms: 2.34x faster                                                       |
| mdp                      | 1.78 sec                                                    | 785 ms: 2.27x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.10 ms: 1.99x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 329 ms: 1.94x faster                                                        |
| go                       | 139 ms                                                      | 75.8 ms: 1.83x faster                                                       |
| pylint                   | 350 ms                                                      | 200 ms: 1.75x faster                                                        |
| logging_silent           | 94.6 ns                                                     | 54.9 ns: 1.72x faster                                                       |
| richards_super           | 52.2 ms                                                     | 31.4 ms: 1.66x faster                                                       |
| chaos                    | 61.7 ms                                                     | 37.9 ms: 1.63x faster                                                       |
| generators               | 32.4 ms                                                     | 20.1 ms: 1.61x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 18.2 us: 1.58x faster                                                       |
| raytrace                 | 273 ms                                                      | 174 ms: 1.57x faster                                                        |
| richards                 | 42.4 ms                                                     | 27.6 ms: 1.54x faster                                                       |
| deepcopy                 | 255 us                                                      | 170 us: 1.50x faster                                                        |
| comprehensions           | 16.5 us                                                     | 11.1 us: 1.48x faster                                                       |
| float                    | 61.7 ms                                                     | 42.3 ms: 1.46x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 3.94 ms: 1.46x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 58.9 ms: 1.46x faster                                                       |
| pyflate                  | 409 ms                                                      | 281 ms: 1.46x faster                                                        |
| scimark_monte_carlo      | 57.3 ms                                                     | 39.9 ms: 1.44x faster                                                       |
| scimark_sor              | 106 ms                                                      | 75.0 ms: 1.42x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 56.4 ms: 1.37x faster                                                       |
| mako                     | 9.03 ms                                                     | 6.61 ms: 1.37x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 134 us: 1.36x faster                                                        |
| html5lib                 | 51.0 ms                                                     | 37.7 ms: 1.35x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.80 ms: 1.35x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 46.7 ms: 1.34x faster                                                       |
| regex_compile            | 106 ms                                                      | 79.6 ms: 1.33x faster                                                       |
| pycparser                | 930 ms                                                      | 702 ms: 1.32x faster                                                        |
| pickle_pure_python       | 270 us                                                      | 209 us: 1.29x faster                                                        |
| genshi_text              | 19.8 ms                                                     | 15.4 ms: 1.29x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.35 sec: 1.24x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.79 us: 1.23x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 991 ms: 1.23x faster                                                        |
| sympy_integrate          | 15.3 ms                                                     | 12.5 ms: 1.23x faster                                                       |
| sympy_sum                | 107 ms                                                      | 87.8 ms: 1.22x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 486 ms: 1.22x faster                                                        |
| sqlite_synth             | 1.91 us                                                     | 1.59 us: 1.20x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 41.9 ms: 1.20x faster                                                       |
| django_template          | 28.9 ms                                                     | 24.0 ms: 1.20x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 34.3 ms: 1.20x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.4 ms: 1.19x faster                                                       |
| regex_dna                | 136 ms                                                      | 115 ms: 1.19x faster                                                        |
| regex_effbot             | 1.66 ms                                                     | 1.41 ms: 1.18x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.65 sec: 1.16x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 13.4 ms: 1.16x faster                                                       |
| nbody                    | 71.3 ms                                                     | 62.2 ms: 1.15x faster                                                       |
| sympy_str                | 194 ms                                                      | 171 ms: 1.14x faster                                                        |
| nqueens                  | 66.6 ms                                                     | 59.0 ms: 1.13x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 39.5 ms: 1.12x faster                                                       |
| 2to3                     | 246 ms                                                      | 220 ms: 1.12x faster                                                        |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.47 ms: 1.10x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 871 us: 1.10x faster                                                        |
| xml_etree_parse          | 96.8 ms                                                     | 89.4 ms: 1.08x faster                                                       |
| sympy_expand             | 314 ms                                                      | 295 ms: 1.07x faster                                                        |
| scimark_fft              | 187 ms                                                      | 178 ms: 1.06x faster                                                        |
| meteor_contest           | 75.9 ms                                                     | 72.7 ms: 1.04x faster                                                       |
| fannkuch                 | 256 ms                                                      | 250 ms: 1.02x faster                                                        |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.7 ms: 1.02x faster                                                       |
| json                     | 3.14 ms                                                     | 3.10 ms: 1.01x faster                                                       |
| logging_simple           | 6.22 us                                                     | 6.35 us: 1.02x slower                                                       |
| async_generators         | 222 ms                                                      | 229 ms: 1.03x slower                                                        |
| json_loads               | 14.0 us                                                     | 14.9 us: 1.06x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.53 ms: 1.15x slower                                                       |
| coverage                 | 39.0 ms                                                     | 49.8 ms: 1.28x slower                                                       |
| python_startup           | 20.6 ms                                                     | 26.3 ms: 1.28x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 20.5 ms: 1.32x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 89.4 ms: 1.44x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.11 ms: 1.49x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.26 ms: 1.57x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.28x faster                                                                |

Benchmark hidden because not significant (3): xml_etree_generate, pidigits, logging_format
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250421-3.14.0a7+-ea8ec95/bm-20250421-pythonperf1-amd64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.292x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: unknown