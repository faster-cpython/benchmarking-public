# Results vs. 3.10.4

- fork: faster-cpython
- ref: trashcan_in_dealloc
- machine: windows-amd64
- commit hash: 8aa20f2
- commit date: 2025-04-09
- overall geometric mean: 1.299x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 217 ms: 1.13x faster                                                                 |
| docutils       | 1.92 sec                                                    | 1.63 sec: 1.18x faster                                                               |
| html5lib       | 51.0 ms                                                     | 38.1 ms: 1.34x faster                                                                |
| Geometric mean | (ref)                                                       | 1.21x faster                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|-------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 406 ms: 2.73x faster                                                                 |
| async_tree_memoization  | 526 ms                                                      | 203 ms: 2.60x faster                                                                 |
| async_tree_none         | 435 ms                                                      | 177 ms: 2.46x faster                                                                 |
| async_tree_cpu_io_mixed | 638 ms                                                      | 328 ms: 1.94x faster                                                                 |
| Geometric mean          | (ref)                                                       | 2.41x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 41.9 ms: 1.47x faster                                                                |
| nbody          | 71.3 ms                                                     | 61.8 ms: 1.15x faster                                                                |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                                                 |
| Geometric mean | (ref)                                                       | 1.20x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 79.2 ms: 1.34x faster                                                                |
| regex_dna      | 136 ms                                                      | 116 ms: 1.17x faster                                                                 |
| regex_effbot   | 1.66 ms                                                     | 1.48 ms: 1.12x faster                                                                |
| regex_v8       | 15.4 ms                                                     | 13.8 ms: 1.12x faster                                                                |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 131 us: 1.40x faster                                                                 |
| json_dumps           | 9.16 ms                                                     | 6.81 ms: 1.35x faster                                                                |
| pickle_pure_python   | 270 us                                                      | 207 us: 1.30x faster                                                                 |
| tomli_loads          | 1.67 sec                                                    | 1.34 sec: 1.25x faster                                                               |
| xml_etree_process    | 44.5 ms                                                     | 39.3 ms: 1.13x faster                                                                |
| xml_etree_parse      | 96.8 ms                                                     | 89.5 ms: 1.08x faster                                                                |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.0 ms: 1.03x faster                                                                |
| xml_etree_generate   | 55.5 ms                                                     | 55.8 ms: 1.01x slower                                                                |
| json_loads           | 14.0 us                                                     | 15.2 us: 1.08x slower                                                                |
| Geometric mean       | (ref)                                                       | 1.15x faster                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 25.0 ms: 1.21x slower                                                                |
| python_startup_no_site | 15.5 ms                                                     | 19.5 ms: 1.26x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.24x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.50 ms: 1.39x faster                                                                |
| genshi_text     | 19.8 ms                                                     | 15.3 ms: 1.29x faster                                                                |
| genshi_xml      | 41.0 ms                                                     | 33.6 ms: 1.22x faster                                                                |
| django_template | 28.9 ms                                                     | 24.0 ms: 1.20x faster                                                                |
| Geometric mean  | (ref)                                                       | 1.27x faster                                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 106 us: 3.17x faster                                                                 |
| async_tree_io            | 1.11 sec                                                    | 406 ms: 2.73x faster                                                                 |
| pathlib                  | 75.7 ms                                                     | 28.5 ms: 2.66x faster                                                                |
| async_tree_memoization   | 526 ms                                                      | 203 ms: 2.60x faster                                                                 |
| async_tree_none          | 435 ms                                                      | 177 ms: 2.46x faster                                                                 |
| mdp                      | 1.78 sec                                                    | 797 ms: 2.23x faster                                                                 |
| deltablue                | 4.19 ms                                                     | 2.11 ms: 1.99x faster                                                                |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 328 ms: 1.94x faster                                                                 |
| go                       | 139 ms                                                      | 75.5 ms: 1.84x faster                                                                |
| pylint                   | 350 ms                                                      | 197 ms: 1.78x faster                                                                 |
| logging_silent           | 94.6 ns                                                     | 54.5 ns: 1.74x faster                                                                |
| generators               | 32.4 ms                                                     | 18.8 ms: 1.72x faster                                                                |
| richards_super           | 52.2 ms                                                     | 30.5 ms: 1.71x faster                                                                |
| chaos                    | 61.7 ms                                                     | 37.8 ms: 1.63x faster                                                                |
| deepcopy_memo            | 28.8 us                                                     | 17.8 us: 1.62x faster                                                                |
| richards                 | 42.4 ms                                                     | 26.7 ms: 1.59x faster                                                                |
| raytrace                 | 273 ms                                                      | 174 ms: 1.57x faster                                                                 |
| scimark_monte_carlo      | 57.3 ms                                                     | 38.1 ms: 1.50x faster                                                                |
| scimark_lu               | 85.8 ms                                                     | 57.4 ms: 1.49x faster                                                                |
| deepcopy                 | 255 us                                                      | 171 us: 1.49x faster                                                                 |
| float                    | 61.7 ms                                                     | 41.9 ms: 1.47x faster                                                                |
| comprehensions           | 16.5 us                                                     | 11.3 us: 1.46x faster                                                                |
| hexiom                   | 5.74 ms                                                     | 3.98 ms: 1.44x faster                                                                |
| scimark_sor              | 106 ms                                                      | 73.8 ms: 1.44x faster                                                                |
| pyflate                  | 409 ms                                                      | 288 ms: 1.42x faster                                                                 |
| unpickle_pure_python     | 183 us                                                      | 131 us: 1.40x faster                                                                 |
| mako                     | 9.03 ms                                                     | 6.50 ms: 1.39x faster                                                                |
| json_dumps               | 9.16 ms                                                     | 6.81 ms: 1.35x faster                                                                |
| regex_compile            | 106 ms                                                      | 79.2 ms: 1.34x faster                                                                |
| html5lib                 | 51.0 ms                                                     | 38.1 ms: 1.34x faster                                                                |
| spectral_norm            | 77.3 ms                                                     | 58.0 ms: 1.33x faster                                                                |
| pycparser                | 930 ms                                                      | 705 ms: 1.32x faster                                                                 |
| crypto_pyaes             | 62.5 ms                                                     | 47.6 ms: 1.32x faster                                                                |
| pickle_pure_python       | 270 us                                                      | 207 us: 1.30x faster                                                                 |
| genshi_text              | 19.8 ms                                                     | 15.3 ms: 1.29x faster                                                                |
| tomli_loads              | 1.67 sec                                                    | 1.34 sec: 1.25x faster                                                               |
| dulwich_log              | 50.5 ms                                                     | 41.0 ms: 1.23x faster                                                                |
| deepcopy_reduce          | 2.20 us                                                     | 1.81 us: 1.22x faster                                                                |
| genshi_xml               | 41.0 ms                                                     | 33.6 ms: 1.22x faster                                                                |
| sympy_integrate          | 15.3 ms                                                     | 12.5 ms: 1.22x faster                                                                |
| sqlite_synth             | 1.91 us                                                     | 1.58 us: 1.21x faster                                                                |
| coroutines               | 16.0 ms                                                     | 13.2 ms: 1.21x faster                                                                |
| pprint_pformat           | 1.22 sec                                                    | 1.01 sec: 1.21x faster                                                               |
| pprint_safe_repr         | 592 ms                                                      | 490 ms: 1.21x faster                                                                 |
| sympy_sum                | 107 ms                                                      | 88.8 ms: 1.21x faster                                                                |
| django_template          | 28.9 ms                                                     | 24.0 ms: 1.20x faster                                                                |
| docutils                 | 1.92 sec                                                    | 1.63 sec: 1.18x faster                                                               |
| regex_dna                | 136 ms                                                      | 116 ms: 1.17x faster                                                                 |
| nbody                    | 71.3 ms                                                     | 61.8 ms: 1.15x faster                                                                |
| sympy_str                | 194 ms                                                      | 171 ms: 1.14x faster                                                                 |
| 2to3                     | 246 ms                                                      | 217 ms: 1.13x faster                                                                 |
| bench_thread_pool        | 958 us                                                      | 844 us: 1.13x faster                                                                 |
| xml_etree_process        | 44.5 ms                                                     | 39.3 ms: 1.13x faster                                                                |
| regex_effbot             | 1.66 ms                                                     | 1.48 ms: 1.12x faster                                                                |
| regex_v8                 | 15.4 ms                                                     | 13.8 ms: 1.12x faster                                                                |
| nqueens                  | 66.6 ms                                                     | 60.6 ms: 1.10x faster                                                                |
| xml_etree_parse          | 96.8 ms                                                     | 89.5 ms: 1.08x faster                                                                |
| sympy_expand             | 314 ms                                                      | 291 ms: 1.08x faster                                                                 |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.55 ms: 1.07x faster                                                                |
| meteor_contest           | 75.9 ms                                                     | 72.3 ms: 1.05x faster                                                                |
| scimark_fft              | 187 ms                                                      | 179 ms: 1.05x faster                                                                 |
| logging_format           | 6.76 us                                                     | 6.51 us: 1.04x faster                                                                |
| logging_simple           | 6.22 us                                                     | 6.01 us: 1.03x faster                                                                |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.0 ms: 1.03x faster                                                                |
| fannkuch                 | 256 ms                                                      | 248 ms: 1.03x faster                                                                 |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                                                 |
| xml_etree_generate       | 55.5 ms                                                     | 55.8 ms: 1.01x slower                                                                |
| async_generators         | 222 ms                                                      | 226 ms: 1.02x slower                                                                 |
| json_loads               | 14.0 us                                                     | 15.2 us: 1.08x slower                                                                |
| telco                    | 3.94 ms                                                     | 4.64 ms: 1.18x slower                                                                |
| python_startup           | 20.6 ms                                                     | 25.0 ms: 1.21x slower                                                                |
| python_startup_no_site   | 15.5 ms                                                     | 19.5 ms: 1.26x slower                                                                |
| coverage                 | 39.0 ms                                                     | 49.8 ms: 1.28x slower                                                                |
| bench_mp_pool            | 62.0 ms                                                     | 86.4 ms: 1.39x slower                                                                |
| gc_traversal             | 1.41 ms                                                     | 2.10 ms: 1.49x slower                                                                |
| create_gc_cycles         | 800 us                                                      | 1.23 ms: 1.54x slower                                                                |
| Geometric mean           | (ref)                                                       | 1.29x faster                                                                         |

Benchmark hidden because not significant (1): json
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250409-3.14.0a7+-8aa20f2/bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.299x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: unknown