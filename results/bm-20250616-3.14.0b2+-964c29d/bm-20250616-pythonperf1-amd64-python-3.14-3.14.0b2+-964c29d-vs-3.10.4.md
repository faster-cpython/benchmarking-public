# Results vs. 3.10.4

- fork: python
- ref: 3.14
- machine: windows-amd64
- commit hash: 964c29d
- commit date: 2025-06-16
- overall geometric mean: 1.282x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250616-pythonperf1-amd64-python-3.14-3.14.0b2+-964c29d |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 223 ms: 1.10x faster                                        |
| docutils       | 1.92 sec                                                    | 1.67 sec: 1.15x faster                                      |
| html5lib       | 51.0 ms                                                     | 39.2 ms: 1.30x faster                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250616-pythonperf1-amd64-python-3.14-3.14.0b2+-964c29d |
|-------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 397 ms: 2.79x faster                                        |
| async_tree_memoization  | 526 ms                                                      | 209 ms: 2.52x faster                                        |
| async_tree_none         | 435 ms                                                      | 174 ms: 2.50x faster                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 330 ms: 1.93x faster                                        |
| Geometric mean          | (ref)                                                       | 2.41x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250616-pythonperf1-amd64-python-3.14-3.14.0b2+-964c29d |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 61.7 ms                                                     | 43.4 ms: 1.42x faster                                       |
| nbody          | 71.3 ms                                                     | 62.4 ms: 1.14x faster                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250616-pythonperf1-amd64-python-3.14-3.14.0b2+-964c29d |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 79.3 ms: 1.34x faster                                       |
| regex_v8       | 15.4 ms                                                     | 13.2 ms: 1.17x faster                                       |
| regex_dna      | 136 ms                                                      | 118 ms: 1.16x faster                                        |
| regex_effbot   | 1.66 ms                                                     | 1.56 ms: 1.06x faster                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250616-pythonperf1-amd64-python-3.14-3.14.0b2+-964c29d |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.27 ms: 1.46x faster                                       |
| unpickle_pure_python | 183 us                                                      | 132 us: 1.39x faster                                        |
| pickle_pure_python   | 270 us                                                      | 209 us: 1.29x faster                                        |
| tomli_loads          | 1.67 sec                                                    | 1.37 sec: 1.22x faster                                      |
| xml_etree_process    | 44.5 ms                                                     | 39.1 ms: 1.14x faster                                       |
| xml_etree_parse      | 96.8 ms                                                     | 88.6 ms: 1.09x faster                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.4 ms: 1.03x faster                                       |
| json_loads           | 14.0 us                                                     | 14.9 us: 1.06x slower                                       |
| Geometric mean       | (ref)                                                       | 1.16x faster                                                |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250616-pythonperf1-amd64-python-3.14-3.14.0b2+-964c29d |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.5 ms: 1.26x slower                                       |
| python_startup         | 20.6 ms                                                     | 26.5 ms: 1.28x slower                                       |
| Geometric mean         | (ref)                                                       | 1.27x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250616-pythonperf1-amd64-python-3.14-3.14.0b2+-964c29d |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.76 ms: 1.34x faster                                       |
| genshi_text     | 19.8 ms                                                     | 15.1 ms: 1.31x faster                                       |
| genshi_xml      | 41.0 ms                                                     | 34.5 ms: 1.19x faster                                       |
| django_template | 28.9 ms                                                     | 24.8 ms: 1.17x faster                                       |
| Geometric mean  | (ref)                                                       | 1.25x faster                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250616-pythonperf1-amd64-python-3.14-3.14.0b2+-964c29d |
|--------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 105 us: 3.19x faster                                        |
| async_tree_io            | 1.11 sec                                                    | 397 ms: 2.79x faster                                        |
| async_tree_memoization   | 526 ms                                                      | 209 ms: 2.52x faster                                        |
| async_tree_none          | 435 ms                                                      | 174 ms: 2.50x faster                                        |
| pathlib                  | 75.7 ms                                                     | 32.4 ms: 2.34x faster                                       |
| mdp                      | 1.78 sec                                                    | 819 ms: 2.17x faster                                        |
| deltablue                | 4.19 ms                                                     | 2.11 ms: 1.99x faster                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 330 ms: 1.93x faster                                        |
| go                       | 139 ms                                                      | 77.0 ms: 1.81x faster                                       |
| pylint                   | 350 ms                                                      | 200 ms: 1.75x faster                                        |
| richards_super           | 52.2 ms                                                     | 30.7 ms: 1.70x faster                                       |
| generators               | 32.4 ms                                                     | 19.8 ms: 1.64x faster                                       |
| richards                 | 42.4 ms                                                     | 26.8 ms: 1.58x faster                                       |
| deepcopy_memo            | 28.8 us                                                     | 18.3 us: 1.57x faster                                       |
| chaos                    | 61.7 ms                                                     | 39.6 ms: 1.56x faster                                       |
| scimark_lu               | 85.8 ms                                                     | 57.3 ms: 1.50x faster                                       |
| raytrace                 | 273 ms                                                      | 183 ms: 1.49x faster                                        |
| deepcopy                 | 255 us                                                      | 172 us: 1.48x faster                                        |
| comprehensions           | 16.5 us                                                     | 11.2 us: 1.48x faster                                       |
| json_dumps               | 9.16 ms                                                     | 6.27 ms: 1.46x faster                                       |
| float                    | 61.7 ms                                                     | 43.4 ms: 1.42x faster                                       |
| pyflate                  | 409 ms                                                      | 290 ms: 1.41x faster                                        |
| hexiom                   | 5.74 ms                                                     | 4.07 ms: 1.41x faster                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 41.0 ms: 1.40x faster                                       |
| scimark_sor              | 106 ms                                                      | 76.1 ms: 1.40x faster                                       |
| unpickle_pure_python     | 183 us                                                      | 132 us: 1.39x faster                                        |
| regex_compile            | 106 ms                                                      | 79.3 ms: 1.34x faster                                       |
| mako                     | 9.03 ms                                                     | 6.76 ms: 1.34x faster                                       |
| spectral_norm            | 77.3 ms                                                     | 57.8 ms: 1.34x faster                                       |
| crypto_pyaes             | 62.5 ms                                                     | 47.3 ms: 1.32x faster                                       |
| genshi_text              | 19.8 ms                                                     | 15.1 ms: 1.31x faster                                       |
| pycparser                | 930 ms                                                      | 710 ms: 1.31x faster                                        |
| html5lib                 | 51.0 ms                                                     | 39.2 ms: 1.30x faster                                       |
| pickle_pure_python       | 270 us                                                      | 209 us: 1.29x faster                                        |
| deepcopy_reduce          | 2.20 us                                                     | 1.78 us: 1.24x faster                                       |
| sympy_integrate          | 15.3 ms                                                     | 12.5 ms: 1.22x faster                                       |
| tomli_loads              | 1.67 sec                                                    | 1.37 sec: 1.22x faster                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.00 sec: 1.22x faster                                      |
| dulwich_log              | 50.5 ms                                                     | 41.7 ms: 1.21x faster                                       |
| sympy_sum                | 107 ms                                                      | 88.5 ms: 1.21x faster                                       |
| pprint_safe_repr         | 592 ms                                                      | 492 ms: 1.20x faster                                        |
| sqlite_synth             | 1.91 us                                                     | 1.61 us: 1.19x faster                                       |
| genshi_xml               | 41.0 ms                                                     | 34.5 ms: 1.19x faster                                       |
| regex_v8                 | 15.4 ms                                                     | 13.2 ms: 1.17x faster                                       |
| django_template          | 28.9 ms                                                     | 24.8 ms: 1.17x faster                                       |
| regex_dna                | 136 ms                                                      | 118 ms: 1.16x faster                                        |
| coroutines               | 16.0 ms                                                     | 13.8 ms: 1.16x faster                                       |
| docutils                 | 1.92 sec                                                    | 1.67 sec: 1.15x faster                                      |
| nbody                    | 71.3 ms                                                     | 62.4 ms: 1.14x faster                                       |
| sympy_str                | 194 ms                                                      | 171 ms: 1.14x faster                                        |
| xml_etree_process        | 44.5 ms                                                     | 39.1 ms: 1.14x faster                                       |
| 2to3                     | 246 ms                                                      | 223 ms: 1.10x faster                                        |
| nqueens                  | 66.6 ms                                                     | 60.9 ms: 1.09x faster                                       |
| xml_etree_parse          | 96.8 ms                                                     | 88.6 ms: 1.09x faster                                       |
| scimark_fft              | 187 ms                                                      | 173 ms: 1.09x faster                                        |
| sympy_expand             | 314 ms                                                      | 292 ms: 1.08x faster                                        |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.53 ms: 1.08x faster                                       |
| regex_effbot             | 1.66 ms                                                     | 1.56 ms: 1.06x faster                                       |
| meteor_contest           | 75.9 ms                                                     | 73.7 ms: 1.03x faster                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.4 ms: 1.03x faster                                       |
| fannkuch                 | 256 ms                                                      | 253 ms: 1.01x faster                                        |
| logging_format           | 6.76 us                                                     | 6.88 us: 1.02x slower                                       |
| logging_simple           | 6.22 us                                                     | 6.48 us: 1.04x slower                                       |
| async_generators         | 222 ms                                                      | 235 ms: 1.06x slower                                        |
| json_loads               | 14.0 us                                                     | 14.9 us: 1.06x slower                                       |
| telco                    | 3.94 ms                                                     | 4.60 ms: 1.17x slower                                       |
| python_startup_no_site   | 15.5 ms                                                     | 19.5 ms: 1.26x slower                                       |
| coverage                 | 39.0 ms                                                     | 49.0 ms: 1.26x slower                                       |
| python_startup           | 20.6 ms                                                     | 26.5 ms: 1.28x slower                                       |
| gc_traversal             | 1.41 ms                                                     | 2.15 ms: 1.52x slower                                       |
| create_gc_cycles         | 800 us                                                      | 1.33 ms: 1.67x slower                                       |
| logging_silent           | 94.6 ns                                                     | 317 ns: 3.35x slower                                        |
| Geometric mean           | (ref)                                                       | 1.26x faster                                                |

Benchmark hidden because not significant (3): pidigits, json, xml_etree_generate
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250616-3.14.0b2+-964c29d/bm-20250616-pythonperf1-amd64-python-3.14-3.14.0b2+-964c29d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.282x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: unknown