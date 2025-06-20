# Results vs. 3.10.4

- fork: faster-cpython
- ref: explicit_check_perio
- machine: windows-amd64
- commit hash: 494c825
- commit date: 2025-06-20
- overall geometric mean: 1.262x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 221 ms: 1.11x faster                                                                 |
| docutils       | 1.92 sec                                                    | 1.63 sec: 1.18x faster                                                               |
| html5lib       | 51.0 ms                                                     | 38.3 ms: 1.33x faster                                                                |
| Geometric mean | (ref)                                                       | 1.20x faster                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|-------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 415 ms: 2.67x faster                                                                 |
| async_tree_memoization  | 526 ms                                                      | 214 ms: 2.46x faster                                                                 |
| async_tree_none         | 435 ms                                                      | 177 ms: 2.46x faster                                                                 |
| async_tree_cpu_io_mixed | 638 ms                                                      | 333 ms: 1.92x faster                                                                 |
| Geometric mean          | (ref)                                                       | 2.36x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 44.5 ms: 1.39x faster                                                                |
| nbody          | 71.3 ms                                                     | 65.2 ms: 1.09x faster                                                                |
| pidigits       | 149 ms                                                      | 146 ms: 1.02x faster                                                                 |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 82.0 ms: 1.29x faster                                                                |
| regex_dna      | 136 ms                                                      | 121 ms: 1.12x faster                                                                 |
| regex_effbot   | 1.66 ms                                                     | 1.52 ms: 1.09x faster                                                                |
| regex_v8       | 15.4 ms                                                     | 14.2 ms: 1.09x faster                                                                |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.24 ms: 1.47x faster                                                                |
| unpickle_pure_python | 183 us                                                      | 138 us: 1.33x faster                                                                 |
| pickle_pure_python   | 270 us                                                      | 219 us: 1.23x faster                                                                 |
| tomli_loads          | 1.67 sec                                                    | 1.43 sec: 1.17x faster                                                               |
| xml_etree_process    | 44.5 ms                                                     | 39.7 ms: 1.12x faster                                                                |
| xml_etree_parse      | 96.8 ms                                                     | 88.4 ms: 1.09x faster                                                                |
| xml_etree_generate   | 55.5 ms                                                     | 57.1 ms: 1.03x slower                                                                |
| json_loads           | 14.0 us                                                     | 14.6 us: 1.04x slower                                                                |
| Geometric mean       | (ref)                                                       | 1.14x faster                                                                         |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.4 ms: 1.25x slower                                                                |
| python_startup         | 20.6 ms                                                     | 26.0 ms: 1.26x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.81 ms: 1.33x faster                                                                |
| genshi_text     | 19.8 ms                                                     | 15.7 ms: 1.26x faster                                                                |
| django_template | 28.9 ms                                                     | 24.4 ms: 1.19x faster                                                                |
| genshi_xml      | 41.0 ms                                                     | 34.7 ms: 1.18x faster                                                                |
| Geometric mean  | (ref)                                                       | 1.24x faster                                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 104 us: 3.22x faster                                                                 |
| async_tree_io            | 1.11 sec                                                    | 415 ms: 2.67x faster                                                                 |
| async_tree_memoization   | 526 ms                                                      | 214 ms: 2.46x faster                                                                 |
| async_tree_none          | 435 ms                                                      | 177 ms: 2.46x faster                                                                 |
| pathlib                  | 75.7 ms                                                     | 31.8 ms: 2.38x faster                                                                |
| mdp                      | 1.78 sec                                                    | 813 ms: 2.19x faster                                                                 |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 333 ms: 1.92x faster                                                                 |
| deltablue                | 4.19 ms                                                     | 2.29 ms: 1.83x faster                                                                |
| go                       | 139 ms                                                      | 77.8 ms: 1.79x faster                                                                |
| pylint                   | 350 ms                                                      | 199 ms: 1.76x faster                                                                 |
| generators               | 32.4 ms                                                     | 19.6 ms: 1.65x faster                                                                |
| richards_super           | 52.2 ms                                                     | 31.9 ms: 1.64x faster                                                                |
| deepcopy_memo            | 28.8 us                                                     | 18.8 us: 1.53x faster                                                                |
| chaos                    | 61.7 ms                                                     | 40.5 ms: 1.52x faster                                                                |
| richards                 | 42.4 ms                                                     | 28.2 ms: 1.51x faster                                                                |
| raytrace                 | 273 ms                                                      | 183 ms: 1.49x faster                                                                 |
| comprehensions           | 16.5 us                                                     | 11.1 us: 1.49x faster                                                                |
| json_dumps               | 9.16 ms                                                     | 6.24 ms: 1.47x faster                                                                |
| deepcopy                 | 255 us                                                      | 176 us: 1.45x faster                                                                 |
| scimark_lu               | 85.8 ms                                                     | 59.9 ms: 1.43x faster                                                                |
| scimark_monte_carlo      | 57.3 ms                                                     | 41.0 ms: 1.40x faster                                                                |
| float                    | 61.7 ms                                                     | 44.5 ms: 1.39x faster                                                                |
| pyflate                  | 409 ms                                                      | 295 ms: 1.39x faster                                                                 |
| hexiom                   | 5.74 ms                                                     | 4.22 ms: 1.36x faster                                                                |
| scimark_sor              | 106 ms                                                      | 78.2 ms: 1.36x faster                                                                |
| html5lib                 | 51.0 ms                                                     | 38.3 ms: 1.33x faster                                                                |
| unpickle_pure_python     | 183 us                                                      | 138 us: 1.33x faster                                                                 |
| mako                     | 9.03 ms                                                     | 6.81 ms: 1.33x faster                                                                |
| pycparser                | 930 ms                                                      | 717 ms: 1.30x faster                                                                 |
| regex_compile            | 106 ms                                                      | 82.0 ms: 1.29x faster                                                                |
| crypto_pyaes             | 62.5 ms                                                     | 48.5 ms: 1.29x faster                                                                |
| genshi_text              | 19.8 ms                                                     | 15.7 ms: 1.26x faster                                                                |
| spectral_norm            | 77.3 ms                                                     | 62.2 ms: 1.24x faster                                                                |
| pickle_pure_python       | 270 us                                                      | 219 us: 1.23x faster                                                                 |
| thrift                   | 617 us                                                      | 501 us: 1.23x faster                                                                 |
| dulwich_log              | 50.5 ms                                                     | 41.6 ms: 1.21x faster                                                                |
| sympy_integrate          | 15.3 ms                                                     | 12.7 ms: 1.21x faster                                                                |
| sympy_sum                | 107 ms                                                      | 88.8 ms: 1.21x faster                                                                |
| sqlite_synth             | 1.91 us                                                     | 1.59 us: 1.20x faster                                                                |
| deepcopy_reduce          | 2.20 us                                                     | 1.85 us: 1.19x faster                                                                |
| django_template          | 28.9 ms                                                     | 24.4 ms: 1.19x faster                                                                |
| genshi_xml               | 41.0 ms                                                     | 34.7 ms: 1.18x faster                                                                |
| docutils                 | 1.92 sec                                                    | 1.63 sec: 1.18x faster                                                               |
| tomli_loads              | 1.67 sec                                                    | 1.43 sec: 1.17x faster                                                               |
| sympy_str                | 194 ms                                                      | 172 ms: 1.13x faster                                                                 |
| regex_dna                | 136 ms                                                      | 121 ms: 1.12x faster                                                                 |
| xml_etree_process        | 44.5 ms                                                     | 39.7 ms: 1.12x faster                                                                |
| 2to3                     | 246 ms                                                      | 221 ms: 1.11x faster                                                                 |
| coroutines               | 16.0 ms                                                     | 14.5 ms: 1.10x faster                                                                |
| pprint_pformat           | 1.22 sec                                                    | 1.11 sec: 1.10x faster                                                               |
| xml_etree_parse          | 96.8 ms                                                     | 88.4 ms: 1.09x faster                                                                |
| nbody                    | 71.3 ms                                                     | 65.2 ms: 1.09x faster                                                                |
| regex_effbot             | 1.66 ms                                                     | 1.52 ms: 1.09x faster                                                                |
| regex_v8                 | 15.4 ms                                                     | 14.2 ms: 1.09x faster                                                                |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.51 ms: 1.09x faster                                                                |
| pprint_safe_repr         | 592 ms                                                      | 548 ms: 1.08x faster                                                                 |
| sympy_expand             | 314 ms                                                      | 292 ms: 1.08x faster                                                                 |
| nqueens                  | 66.6 ms                                                     | 62.1 ms: 1.07x faster                                                                |
| json                     | 3.14 ms                                                     | 3.05 ms: 1.03x faster                                                                |
| scimark_fft              | 187 ms                                                      | 183 ms: 1.02x faster                                                                 |
| pidigits                 | 149 ms                                                      | 146 ms: 1.02x faster                                                                 |
| meteor_contest           | 75.9 ms                                                     | 74.4 ms: 1.02x faster                                                                |
| logging_format           | 6.76 us                                                     | 6.81 us: 1.01x slower                                                                |
| logging_simple           | 6.22 us                                                     | 6.36 us: 1.02x slower                                                                |
| xml_etree_generate       | 55.5 ms                                                     | 57.1 ms: 1.03x slower                                                                |
| fannkuch                 | 256 ms                                                      | 265 ms: 1.04x slower                                                                 |
| json_loads               | 14.0 us                                                     | 14.6 us: 1.04x slower                                                                |
| async_generators         | 222 ms                                                      | 231 ms: 1.04x slower                                                                 |
| telco                    | 3.94 ms                                                     | 4.63 ms: 1.18x slower                                                                |
| coverage                 | 39.0 ms                                                     | 48.7 ms: 1.25x slower                                                                |
| python_startup_no_site   | 15.5 ms                                                     | 19.4 ms: 1.25x slower                                                                |
| python_startup           | 20.6 ms                                                     | 26.0 ms: 1.26x slower                                                                |
| gc_traversal             | 1.41 ms                                                     | 2.14 ms: 1.52x slower                                                                |
| create_gc_cycles         | 800 us                                                      | 1.32 ms: 1.65x slower                                                                |
| logging_silent           | 94.6 ns                                                     | 318 ns: 3.36x slower                                                                 |
| Geometric mean           | (ref)                                                       | 1.24x faster                                                                         |

Benchmark hidden because not significant (1): xml_etree_iterparse
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250620-3.15.0a0-494c825/bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.262x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: unknown