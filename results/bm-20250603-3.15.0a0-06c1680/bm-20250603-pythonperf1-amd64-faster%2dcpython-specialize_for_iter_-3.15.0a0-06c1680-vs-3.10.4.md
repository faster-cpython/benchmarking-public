# Results vs. 3.10.4

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: windows-amd64
- commit hash: 06c1680
- commit date: 2025-06-03
- overall geometric mean: 1.175x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250603-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 219 ms: 1.12x faster                                                                 |
| docutils       | 1.92 sec                                                    | 1.64 sec: 1.17x faster                                                               |
| html5lib       | 51.0 ms                                                     | 38.1 ms: 1.34x faster                                                                |
| Geometric mean | (ref)                                                       | 1.21x faster                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250603-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|-------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 394 ms: 2.81x faster                                                                 |
| async_tree_memoization  | 526 ms                                                      | 204 ms: 2.57x faster                                                                 |
| async_tree_none         | 435 ms                                                      | 170 ms: 2.55x faster                                                                 |
| async_tree_cpu_io_mixed | 638 ms                                                      | 329 ms: 1.94x faster                                                                 |
| Geometric mean          | (ref)                                                       | 2.45x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250603-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 43.9 ms: 1.41x faster                                                                |
| nbody          | 71.3 ms                                                     | 60.9 ms: 1.17x faster                                                                |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                                                 |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250603-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 79.6 ms: 1.33x faster                                                                |
| regex_dna      | 136 ms                                                      | 120 ms: 1.14x faster                                                                 |
| regex_v8       | 15.4 ms                                                     | 14.0 ms: 1.11x faster                                                                |
| regex_effbot   | 1.66 ms                                                     | 1.55 ms: 1.07x faster                                                                |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250603-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.30 ms: 1.45x faster                                                                |
| unpickle_pure_python | 183 us                                                      | 132 us: 1.38x faster                                                                 |
| pickle_pure_python   | 270 us                                                      | 208 us: 1.30x faster                                                                 |
| tomli_loads          | 1.67 sec                                                    | 1.34 sec: 1.25x faster                                                               |
| xml_etree_process    | 44.5 ms                                                     | 39.4 ms: 1.13x faster                                                                |
| xml_etree_parse      | 96.8 ms                                                     | 89.5 ms: 1.08x faster                                                                |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.3 ms: 1.03x faster                                                                |
| json_loads           | 14.0 us                                                     | 14.2 us: 1.01x slower                                                                |
| Geometric mean       | (ref)                                                       | 1.17x faster                                                                         |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250603-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 25.7 ms: 1.25x slower                                                                |
| python_startup_no_site | 15.5 ms                                                     | 19.5 ms: 1.26x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250603-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.54 ms: 1.38x faster                                                                |
| genshi_text     | 19.8 ms                                                     | 15.1 ms: 1.31x faster                                                                |
| genshi_xml      | 41.0 ms                                                     | 34.3 ms: 1.20x faster                                                                |
| django_template | 28.9 ms                                                     | 24.3 ms: 1.19x faster                                                                |
| Geometric mean  | (ref)                                                       | 1.27x faster                                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250603-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 103 us: 3.25x faster                                                                 |
| async_tree_io            | 1.11 sec                                                    | 394 ms: 2.81x faster                                                                 |
| async_tree_memoization   | 526 ms                                                      | 204 ms: 2.57x faster                                                                 |
| async_tree_none          | 435 ms                                                      | 170 ms: 2.55x faster                                                                 |
| pathlib                  | 75.7 ms                                                     | 31.4 ms: 2.41x faster                                                                |
| mdp                      | 1.78 sec                                                    | 806 ms: 2.21x faster                                                                 |
| deltablue                | 4.19 ms                                                     | 2.14 ms: 1.96x faster                                                                |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 329 ms: 1.94x faster                                                                 |
| go                       | 139 ms                                                      | 73.9 ms: 1.88x faster                                                                |
| pylint                   | 350 ms                                                      | 197 ms: 1.78x faster                                                                 |
| richards_super           | 52.2 ms                                                     | 31.1 ms: 1.68x faster                                                                |
| generators               | 32.4 ms                                                     | 19.3 ms: 1.68x faster                                                                |
| chaos                    | 61.7 ms                                                     | 37.8 ms: 1.63x faster                                                                |
| deepcopy_memo            | 28.8 us                                                     | 17.7 us: 1.62x faster                                                                |
| raytrace                 | 273 ms                                                      | 179 ms: 1.53x faster                                                                 |
| richards                 | 42.4 ms                                                     | 27.8 ms: 1.53x faster                                                                |
| deepcopy                 | 255 us                                                      | 169 us: 1.51x faster                                                                 |
| comprehensions           | 16.5 us                                                     | 11.0 us: 1.51x faster                                                                |
| pyflate                  | 409 ms                                                      | 277 ms: 1.48x faster                                                                 |
| json_dumps               | 9.16 ms                                                     | 6.30 ms: 1.45x faster                                                                |
| scimark_lu               | 85.8 ms                                                     | 59.1 ms: 1.45x faster                                                                |
| scimark_sor              | 106 ms                                                      | 73.2 ms: 1.45x faster                                                                |
| hexiom                   | 5.74 ms                                                     | 3.99 ms: 1.44x faster                                                                |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.6 ms: 1.41x faster                                                                |
| float                    | 61.7 ms                                                     | 43.9 ms: 1.41x faster                                                                |
| unpickle_pure_python     | 183 us                                                      | 132 us: 1.38x faster                                                                 |
| mako                     | 9.03 ms                                                     | 6.54 ms: 1.38x faster                                                                |
| spectral_norm            | 77.3 ms                                                     | 56.6 ms: 1.37x faster                                                                |
| crypto_pyaes             | 62.5 ms                                                     | 46.5 ms: 1.34x faster                                                                |
| html5lib                 | 51.0 ms                                                     | 38.1 ms: 1.34x faster                                                                |
| regex_compile            | 106 ms                                                      | 79.6 ms: 1.33x faster                                                                |
| pycparser                | 930 ms                                                      | 702 ms: 1.32x faster                                                                 |
| genshi_text              | 19.8 ms                                                     | 15.1 ms: 1.31x faster                                                                |
| pickle_pure_python       | 270 us                                                      | 208 us: 1.30x faster                                                                 |
| tomli_loads              | 1.67 sec                                                    | 1.34 sec: 1.25x faster                                                               |
| dulwich_log              | 50.5 ms                                                     | 40.8 ms: 1.24x faster                                                                |
| sympy_integrate          | 15.3 ms                                                     | 12.4 ms: 1.24x faster                                                                |
| sympy_sum                | 107 ms                                                      | 87.2 ms: 1.23x faster                                                                |
| deepcopy_reduce          | 2.20 us                                                     | 1.81 us: 1.22x faster                                                                |
| sqlite_synth             | 1.91 us                                                     | 1.58 us: 1.21x faster                                                                |
| genshi_xml               | 41.0 ms                                                     | 34.3 ms: 1.20x faster                                                                |
| django_template          | 28.9 ms                                                     | 24.3 ms: 1.19x faster                                                                |
| docutils                 | 1.92 sec                                                    | 1.64 sec: 1.17x faster                                                               |
| nbody                    | 71.3 ms                                                     | 60.9 ms: 1.17x faster                                                                |
| sympy_str                | 194 ms                                                      | 167 ms: 1.16x faster                                                                 |
| coroutines               | 16.0 ms                                                     | 13.8 ms: 1.16x faster                                                                |
| regex_dna                | 136 ms                                                      | 120 ms: 1.14x faster                                                                 |
| xml_etree_process        | 44.5 ms                                                     | 39.4 ms: 1.13x faster                                                                |
| 2to3                     | 246 ms                                                      | 219 ms: 1.12x faster                                                                 |
| nqueens                  | 66.6 ms                                                     | 59.5 ms: 1.12x faster                                                                |
| pprint_pformat           | 1.22 sec                                                    | 1.10 sec: 1.11x faster                                                               |
| regex_v8                 | 15.4 ms                                                     | 14.0 ms: 1.11x faster                                                                |
| sympy_expand             | 314 ms                                                      | 285 ms: 1.10x faster                                                                 |
| pprint_safe_repr         | 592 ms                                                      | 540 ms: 1.10x faster                                                                 |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.51 ms: 1.08x faster                                                                |
| xml_etree_parse          | 96.8 ms                                                     | 89.5 ms: 1.08x faster                                                                |
| scimark_fft              | 187 ms                                                      | 175 ms: 1.07x faster                                                                 |
| regex_effbot             | 1.66 ms                                                     | 1.55 ms: 1.07x faster                                                                |
| meteor_contest           | 75.9 ms                                                     | 72.7 ms: 1.04x faster                                                                |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.3 ms: 1.03x faster                                                                |
| fannkuch                 | 256 ms                                                      | 250 ms: 1.02x faster                                                                 |
| json                     | 3.14 ms                                                     | 3.09 ms: 1.02x faster                                                                |
| logging_format           | 6.76 us                                                     | 6.70 us: 1.01x faster                                                                |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                                                 |
| json_loads               | 14.0 us                                                     | 14.2 us: 1.01x slower                                                                |
| async_generators         | 222 ms                                                      | 233 ms: 1.05x slower                                                                 |
| telco                    | 3.94 ms                                                     | 4.66 ms: 1.18x slower                                                                |
| python_startup           | 20.6 ms                                                     | 25.7 ms: 1.25x slower                                                                |
| python_startup_no_site   | 15.5 ms                                                     | 19.5 ms: 1.26x slower                                                                |
| gc_traversal             | 1.41 ms                                                     | 2.14 ms: 1.52x slower                                                                |
| create_gc_cycles         | 800 us                                                      | 1.33 ms: 1.66x slower                                                                |
| logging_silent           | 94.6 ns                                                     | 310 ns: 3.28x slower                                                                 |
| coverage                 | 39.0 ms                                                     | 289 ms: 7.42x slower                                                                 |
| thrift                   | 617 us                                                      | 94.3 ms: 152.81x slower                                                              |
| Geometric mean           | (ref)                                                       | 1.15x faster                                                                         |

Benchmark hidden because not significant (2): logging_simple, xml_etree_generate
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250603-3.15.0a0-06c1680/bm-20250603-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.175x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: unknown