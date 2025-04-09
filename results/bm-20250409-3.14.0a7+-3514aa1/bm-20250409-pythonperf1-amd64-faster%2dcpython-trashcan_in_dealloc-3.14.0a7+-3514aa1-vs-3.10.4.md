# Results vs. 3.10.4

- fork: faster-cpython
- ref: trashcan_in_dealloc
- machine: windows-amd64
- commit hash: 3514aa1
- commit date: 2025-04-09
- overall geometric mean: 1.303x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 218 ms: 1.13x faster                                                                 |
| docutils       | 1.92 sec                                                    | 1.65 sec: 1.16x faster                                                               |
| html5lib       | 51.0 ms                                                     | 37.8 ms: 1.35x faster                                                                |
| Geometric mean | (ref)                                                       | 1.21x faster                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|-------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 409 ms: 2.71x faster                                                                 |
| async_tree_memoization  | 526 ms                                                      | 203 ms: 2.59x faster                                                                 |
| async_tree_none         | 435 ms                                                      | 178 ms: 2.44x faster                                                                 |
| async_tree_cpu_io_mixed | 638 ms                                                      | 329 ms: 1.94x faster                                                                 |
| Geometric mean          | (ref)                                                       | 2.40x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 42.2 ms: 1.46x faster                                                                |
| nbody          | 71.3 ms                                                     | 61.3 ms: 1.16x faster                                                                |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                                                 |
| Geometric mean | (ref)                                                       | 1.20x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 78.5 ms: 1.35x faster                                                                |
| regex_dna      | 136 ms                                                      | 116 ms: 1.17x faster                                                                 |
| regex_effbot   | 1.66 ms                                                     | 1.45 ms: 1.14x faster                                                                |
| regex_v8       | 15.4 ms                                                     | 14.4 ms: 1.07x faster                                                                |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 132 us: 1.38x faster                                                                 |
| json_dumps           | 9.16 ms                                                     | 6.73 ms: 1.36x faster                                                                |
| pickle_pure_python   | 270 us                                                      | 208 us: 1.29x faster                                                                 |
| tomli_loads          | 1.67 sec                                                    | 1.36 sec: 1.23x faster                                                               |
| xml_etree_process    | 44.5 ms                                                     | 38.8 ms: 1.15x faster                                                                |
| xml_etree_parse      | 96.8 ms                                                     | 90.0 ms: 1.08x faster                                                                |
| xml_etree_generate   | 55.5 ms                                                     | 54.8 ms: 1.01x faster                                                                |
| xml_etree_iterparse  | 65.0 ms                                                     | 64.4 ms: 1.01x faster                                                                |
| json_loads           | 14.0 us                                                     | 14.9 us: 1.07x slower                                                                |
| Geometric mean       | (ref)                                                       | 1.15x faster                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 25.3 ms: 1.23x slower                                                                |
| python_startup_no_site | 15.5 ms                                                     | 19.7 ms: 1.27x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.65 ms: 1.36x faster                                                                |
| genshi_text     | 19.8 ms                                                     | 14.9 ms: 1.33x faster                                                                |
| genshi_xml      | 41.0 ms                                                     | 32.7 ms: 1.26x faster                                                                |
| django_template | 28.9 ms                                                     | 23.9 ms: 1.21x faster                                                                |
| Geometric mean  | (ref)                                                       | 1.29x faster                                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 104 us: 3.22x faster                                                                 |
| async_tree_io            | 1.11 sec                                                    | 409 ms: 2.71x faster                                                                 |
| pathlib                  | 75.7 ms                                                     | 28.4 ms: 2.66x faster                                                                |
| async_tree_memoization   | 526 ms                                                      | 203 ms: 2.59x faster                                                                 |
| async_tree_none          | 435 ms                                                      | 178 ms: 2.44x faster                                                                 |
| mdp                      | 1.78 sec                                                    | 782 ms: 2.28x faster                                                                 |
| deltablue                | 4.19 ms                                                     | 2.11 ms: 1.99x faster                                                                |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 329 ms: 1.94x faster                                                                 |
| go                       | 139 ms                                                      | 75.8 ms: 1.83x faster                                                                |
| pylint                   | 350 ms                                                      | 197 ms: 1.78x faster                                                                 |
| logging_silent           | 94.6 ns                                                     | 54.2 ns: 1.75x faster                                                                |
| generators               | 32.4 ms                                                     | 19.0 ms: 1.71x faster                                                                |
| richards_super           | 52.2 ms                                                     | 30.6 ms: 1.71x faster                                                                |
| chaos                    | 61.7 ms                                                     | 37.4 ms: 1.65x faster                                                                |
| richards                 | 42.4 ms                                                     | 26.7 ms: 1.59x faster                                                                |
| deepcopy_memo            | 28.8 us                                                     | 18.2 us: 1.58x faster                                                                |
| raytrace                 | 273 ms                                                      | 173 ms: 1.58x faster                                                                 |
| scimark_monte_carlo      | 57.3 ms                                                     | 37.8 ms: 1.52x faster                                                                |
| deepcopy                 | 255 us                                                      | 169 us: 1.51x faster                                                                 |
| scimark_lu               | 85.8 ms                                                     | 56.8 ms: 1.51x faster                                                                |
| hexiom                   | 5.74 ms                                                     | 3.90 ms: 1.47x faster                                                                |
| float                    | 61.7 ms                                                     | 42.2 ms: 1.46x faster                                                                |
| scimark_sor              | 106 ms                                                      | 72.7 ms: 1.46x faster                                                                |
| spectral_norm            | 77.3 ms                                                     | 53.7 ms: 1.44x faster                                                                |
| comprehensions           | 16.5 us                                                     | 11.5 us: 1.44x faster                                                                |
| pyflate                  | 409 ms                                                      | 287 ms: 1.42x faster                                                                 |
| unpickle_pure_python     | 183 us                                                      | 132 us: 1.38x faster                                                                 |
| json_dumps               | 9.16 ms                                                     | 6.73 ms: 1.36x faster                                                                |
| mako                     | 9.03 ms                                                     | 6.65 ms: 1.36x faster                                                                |
| regex_compile            | 106 ms                                                      | 78.5 ms: 1.35x faster                                                                |
| html5lib                 | 51.0 ms                                                     | 37.8 ms: 1.35x faster                                                                |
| crypto_pyaes             | 62.5 ms                                                     | 46.8 ms: 1.34x faster                                                                |
| genshi_text              | 19.8 ms                                                     | 14.9 ms: 1.33x faster                                                                |
| pycparser                | 930 ms                                                      | 705 ms: 1.32x faster                                                                 |
| pickle_pure_python       | 270 us                                                      | 208 us: 1.29x faster                                                                 |
| genshi_xml               | 41.0 ms                                                     | 32.7 ms: 1.26x faster                                                                |
| dulwich_log              | 50.5 ms                                                     | 40.5 ms: 1.25x faster                                                                |
| deepcopy_reduce          | 2.20 us                                                     | 1.77 us: 1.24x faster                                                                |
| sympy_integrate          | 15.3 ms                                                     | 12.4 ms: 1.23x faster                                                                |
| tomli_loads              | 1.67 sec                                                    | 1.36 sec: 1.23x faster                                                               |
| sympy_sum                | 107 ms                                                      | 87.2 ms: 1.23x faster                                                                |
| django_template          | 28.9 ms                                                     | 23.9 ms: 1.21x faster                                                                |
| pprint_pformat           | 1.22 sec                                                    | 1.01 sec: 1.21x faster                                                               |
| sqlite_synth             | 1.91 us                                                     | 1.59 us: 1.20x faster                                                                |
| pprint_safe_repr         | 592 ms                                                      | 493 ms: 1.20x faster                                                                 |
| regex_dna                | 136 ms                                                      | 116 ms: 1.17x faster                                                                 |
| docutils                 | 1.92 sec                                                    | 1.65 sec: 1.16x faster                                                               |
| nbody                    | 71.3 ms                                                     | 61.3 ms: 1.16x faster                                                                |
| sympy_str                | 194 ms                                                      | 169 ms: 1.15x faster                                                                 |
| coroutines               | 16.0 ms                                                     | 13.9 ms: 1.15x faster                                                                |
| xml_etree_process        | 44.5 ms                                                     | 38.8 ms: 1.15x faster                                                                |
| regex_effbot             | 1.66 ms                                                     | 1.45 ms: 1.14x faster                                                                |
| bench_thread_pool        | 958 us                                                      | 843 us: 1.14x faster                                                                 |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.41 ms: 1.13x faster                                                                |
| 2to3                     | 246 ms                                                      | 218 ms: 1.13x faster                                                                 |
| nqueens                  | 66.6 ms                                                     | 59.3 ms: 1.12x faster                                                                |
| scimark_fft              | 187 ms                                                      | 169 ms: 1.11x faster                                                                 |
| sympy_expand             | 314 ms                                                      | 289 ms: 1.09x faster                                                                 |
| xml_etree_parse          | 96.8 ms                                                     | 90.0 ms: 1.08x faster                                                                |
| regex_v8                 | 15.4 ms                                                     | 14.4 ms: 1.07x faster                                                                |
| meteor_contest           | 75.9 ms                                                     | 72.5 ms: 1.05x faster                                                                |
| logging_format           | 6.76 us                                                     | 6.64 us: 1.02x faster                                                                |
| logging_simple           | 6.22 us                                                     | 6.12 us: 1.02x faster                                                                |
| xml_etree_generate       | 55.5 ms                                                     | 54.8 ms: 1.01x faster                                                                |
| xml_etree_iterparse      | 65.0 ms                                                     | 64.4 ms: 1.01x faster                                                                |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                                                 |
| fannkuch                 | 256 ms                                                      | 254 ms: 1.01x faster                                                                 |
| async_generators         | 222 ms                                                      | 227 ms: 1.03x slower                                                                 |
| json_loads               | 14.0 us                                                     | 14.9 us: 1.07x slower                                                                |
| telco                    | 3.94 ms                                                     | 4.61 ms: 1.17x slower                                                                |
| python_startup           | 20.6 ms                                                     | 25.3 ms: 1.23x slower                                                                |
| python_startup_no_site   | 15.5 ms                                                     | 19.7 ms: 1.27x slower                                                                |
| coverage                 | 39.0 ms                                                     | 51.3 ms: 1.31x slower                                                                |
| bench_mp_pool            | 62.0 ms                                                     | 86.8 ms: 1.40x slower                                                                |
| gc_traversal             | 1.41 ms                                                     | 2.10 ms: 1.49x slower                                                                |
| create_gc_cycles         | 800 us                                                      | 1.23 ms: 1.53x slower                                                                |
| Geometric mean           | (ref)                                                       | 1.29x faster                                                                         |

Benchmark hidden because not significant (1): json
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250409-3.14.0a7+-3514aa1/bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.303x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: unknown