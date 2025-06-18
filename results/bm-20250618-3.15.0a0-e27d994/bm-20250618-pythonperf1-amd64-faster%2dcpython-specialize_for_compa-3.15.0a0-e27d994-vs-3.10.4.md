# Results vs. 3.10.4

- fork: faster-cpython
- ref: specialize_for_compa
- machine: windows-amd64
- commit hash: e27d994
- commit date: 2025-06-18
- overall geometric mean: 1.268x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250618-pythonperf1-amd64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 221 ms: 1.11x faster                                                                 |
| docutils       | 1.92 sec                                                    | 1.63 sec: 1.18x faster                                                               |
| html5lib       | 51.0 ms                                                     | 38.4 ms: 1.33x faster                                                                |
| Geometric mean | (ref)                                                       | 1.20x faster                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250618-pythonperf1-amd64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|-------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 397 ms: 2.79x faster                                                                 |
| async_tree_none         | 435 ms                                                      | 171 ms: 2.55x faster                                                                 |
| async_tree_memoization  | 526 ms                                                      | 208 ms: 2.53x faster                                                                 |
| async_tree_cpu_io_mixed | 638 ms                                                      | 329 ms: 1.94x faster                                                                 |
| Geometric mean          | (ref)                                                       | 2.43x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250618-pythonperf1-amd64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 44.5 ms: 1.39x faster                                                                |
| nbody          | 71.3 ms                                                     | 64.7 ms: 1.10x faster                                                                |
| pidigits       | 149 ms                                                      | 146 ms: 1.02x faster                                                                 |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250618-pythonperf1-amd64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 80.8 ms: 1.31x faster                                                                |
| regex_dna      | 136 ms                                                      | 120 ms: 1.14x faster                                                                 |
| regex_v8       | 15.4 ms                                                     | 14.1 ms: 1.09x faster                                                                |
| regex_effbot   | 1.66 ms                                                     | 1.54 ms: 1.08x faster                                                                |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250618-pythonperf1-amd64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.23 ms: 1.47x faster                                                                |
| unpickle_pure_python | 183 us                                                      | 134 us: 1.36x faster                                                                 |
| pickle_pure_python   | 270 us                                                      | 213 us: 1.27x faster                                                                 |
| tomli_loads          | 1.67 sec                                                    | 1.43 sec: 1.17x faster                                                               |
| xml_etree_process    | 44.5 ms                                                     | 39.6 ms: 1.12x faster                                                                |
| xml_etree_parse      | 96.8 ms                                                     | 89.2 ms: 1.09x faster                                                                |
| json_loads           | 14.0 us                                                     | 14.2 us: 1.01x slower                                                                |
| xml_etree_generate   | 55.5 ms                                                     | 56.6 ms: 1.02x slower                                                                |
| Geometric mean       | (ref)                                                       | 1.15x faster                                                                         |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250618-pythonperf1-amd64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.3 ms: 1.25x slower                                                                |
| python_startup         | 20.6 ms                                                     | 25.8 ms: 1.25x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250618-pythonperf1-amd64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.59 ms: 1.37x faster                                                                |
| genshi_text     | 19.8 ms                                                     | 15.3 ms: 1.29x faster                                                                |
| django_template | 28.9 ms                                                     | 24.0 ms: 1.21x faster                                                                |
| genshi_xml      | 41.0 ms                                                     | 34.3 ms: 1.20x faster                                                                |
| Geometric mean  | (ref)                                                       | 1.26x faster                                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250618-pythonperf1-amd64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 103 us: 3.27x faster                                                                 |
| async_tree_io            | 1.11 sec                                                    | 397 ms: 2.79x faster                                                                 |
| async_tree_none          | 435 ms                                                      | 171 ms: 2.55x faster                                                                 |
| async_tree_memoization   | 526 ms                                                      | 208 ms: 2.53x faster                                                                 |
| pathlib                  | 75.7 ms                                                     | 31.7 ms: 2.39x faster                                                                |
| mdp                      | 1.78 sec                                                    | 813 ms: 2.19x faster                                                                 |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 329 ms: 1.94x faster                                                                 |
| deltablue                | 4.19 ms                                                     | 2.23 ms: 1.88x faster                                                                |
| go                       | 139 ms                                                      | 77.4 ms: 1.80x faster                                                                |
| pylint                   | 350 ms                                                      | 198 ms: 1.77x faster                                                                 |
| generators               | 32.4 ms                                                     | 19.5 ms: 1.66x faster                                                                |
| richards_super           | 52.2 ms                                                     | 31.6 ms: 1.65x faster                                                                |
| deepcopy_memo            | 28.8 us                                                     | 18.1 us: 1.59x faster                                                                |
| richards                 | 42.4 ms                                                     | 27.7 ms: 1.53x faster                                                                |
| comprehensions           | 16.5 us                                                     | 10.9 us: 1.52x faster                                                                |
| deepcopy                 | 255 us                                                      | 168 us: 1.52x faster                                                                 |
| raytrace                 | 273 ms                                                      | 182 ms: 1.50x faster                                                                 |
| chaos                    | 61.7 ms                                                     | 41.6 ms: 1.48x faster                                                                |
| json_dumps               | 9.16 ms                                                     | 6.23 ms: 1.47x faster                                                                |
| scimark_lu               | 85.8 ms                                                     | 59.6 ms: 1.44x faster                                                                |
| pyflate                  | 409 ms                                                      | 295 ms: 1.39x faster                                                                 |
| float                    | 61.7 ms                                                     | 44.5 ms: 1.39x faster                                                                |
| hexiom                   | 5.74 ms                                                     | 4.19 ms: 1.37x faster                                                                |
| mako                     | 9.03 ms                                                     | 6.59 ms: 1.37x faster                                                                |
| unpickle_pure_python     | 183 us                                                      | 134 us: 1.36x faster                                                                 |
| scimark_sor              | 106 ms                                                      | 78.4 ms: 1.35x faster                                                                |
| scimark_monte_carlo      | 57.3 ms                                                     | 42.8 ms: 1.34x faster                                                                |
| html5lib                 | 51.0 ms                                                     | 38.4 ms: 1.33x faster                                                                |
| crypto_pyaes             | 62.5 ms                                                     | 47.3 ms: 1.32x faster                                                                |
| regex_compile            | 106 ms                                                      | 80.8 ms: 1.31x faster                                                                |
| pycparser                | 930 ms                                                      | 715 ms: 1.30x faster                                                                 |
| genshi_text              | 19.8 ms                                                     | 15.3 ms: 1.29x faster                                                                |
| pickle_pure_python       | 270 us                                                      | 213 us: 1.27x faster                                                                 |
| thrift                   | 617 us                                                      | 492 us: 1.26x faster                                                                 |
| dulwich_log              | 50.5 ms                                                     | 40.9 ms: 1.23x faster                                                                |
| sympy_sum                | 107 ms                                                      | 87.5 ms: 1.22x faster                                                                |
| sympy_integrate          | 15.3 ms                                                     | 12.5 ms: 1.22x faster                                                                |
| deepcopy_reduce          | 2.20 us                                                     | 1.82 us: 1.21x faster                                                                |
| sqlite_synth             | 1.91 us                                                     | 1.58 us: 1.21x faster                                                                |
| django_template          | 28.9 ms                                                     | 24.0 ms: 1.21x faster                                                                |
| spectral_norm            | 77.3 ms                                                     | 64.3 ms: 1.20x faster                                                                |
| genshi_xml               | 41.0 ms                                                     | 34.3 ms: 1.20x faster                                                                |
| docutils                 | 1.92 sec                                                    | 1.63 sec: 1.18x faster                                                               |
| tomli_loads              | 1.67 sec                                                    | 1.43 sec: 1.17x faster                                                               |
| sympy_str                | 194 ms                                                      | 170 ms: 1.14x faster                                                                 |
| regex_dna                | 136 ms                                                      | 120 ms: 1.14x faster                                                                 |
| xml_etree_process        | 44.5 ms                                                     | 39.6 ms: 1.12x faster                                                                |
| coroutines               | 16.0 ms                                                     | 14.3 ms: 1.12x faster                                                                |
| 2to3                     | 246 ms                                                      | 221 ms: 1.11x faster                                                                 |
| nbody                    | 71.3 ms                                                     | 64.7 ms: 1.10x faster                                                                |
| pprint_pformat           | 1.22 sec                                                    | 1.11 sec: 1.10x faster                                                               |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.49 ms: 1.10x faster                                                                |
| pprint_safe_repr         | 592 ms                                                      | 541 ms: 1.09x faster                                                                 |
| regex_v8                 | 15.4 ms                                                     | 14.1 ms: 1.09x faster                                                                |
| xml_etree_parse          | 96.8 ms                                                     | 89.2 ms: 1.09x faster                                                                |
| nqueens                  | 66.6 ms                                                     | 61.7 ms: 1.08x faster                                                                |
| sympy_expand             | 314 ms                                                      | 292 ms: 1.08x faster                                                                 |
| regex_effbot             | 1.66 ms                                                     | 1.54 ms: 1.08x faster                                                                |
| meteor_contest           | 75.9 ms                                                     | 72.5 ms: 1.05x faster                                                                |
| pidigits                 | 149 ms                                                      | 146 ms: 1.02x faster                                                                 |
| json                     | 3.14 ms                                                     | 3.10 ms: 1.01x faster                                                                |
| scimark_fft              | 187 ms                                                      | 188 ms: 1.00x slower                                                                 |
| json_loads               | 14.0 us                                                     | 14.2 us: 1.01x slower                                                                |
| xml_etree_generate       | 55.5 ms                                                     | 56.6 ms: 1.02x slower                                                                |
| logging_format           | 6.76 us                                                     | 7.06 us: 1.04x slower                                                                |
| async_generators         | 222 ms                                                      | 233 ms: 1.05x slower                                                                 |
| fannkuch                 | 256 ms                                                      | 269 ms: 1.05x slower                                                                 |
| logging_simple           | 6.22 us                                                     | 6.56 us: 1.05x slower                                                                |
| telco                    | 3.94 ms                                                     | 4.63 ms: 1.17x slower                                                                |
| python_startup_no_site   | 15.5 ms                                                     | 19.3 ms: 1.25x slower                                                                |
| python_startup           | 20.6 ms                                                     | 25.8 ms: 1.25x slower                                                                |
| coverage                 | 39.0 ms                                                     | 51.5 ms: 1.32x slower                                                                |
| gc_traversal             | 1.41 ms                                                     | 2.12 ms: 1.50x slower                                                                |
| create_gc_cycles         | 800 us                                                      | 1.32 ms: 1.66x slower                                                                |
| logging_silent           | 94.6 ns                                                     | 329 ns: 3.48x slower                                                                 |
| Geometric mean           | (ref)                                                       | 1.24x faster                                                                         |

Benchmark hidden because not significant (1): xml_etree_iterparse
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250618-3.15.0a0-e27d994/bm-20250618-pythonperf1-amd64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.268x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: unknown