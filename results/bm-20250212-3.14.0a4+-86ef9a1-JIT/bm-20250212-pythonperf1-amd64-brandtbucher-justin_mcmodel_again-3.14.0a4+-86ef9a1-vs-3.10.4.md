# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_mcmodel_again
- machine: windows-amd64
- commit hash: 86ef9a1
- commit date: 2025-02-12
- overall geometric mean: 1.220x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-pythonperf1-amd64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 227 ms: 1.08x faster                                                              |
| docutils       | 1.92 sec                                                    | 1.77 sec: 1.08x faster                                                            |
| html5lib       | 51.0 ms                                                     | 40.1 ms: 1.27x faster                                                             |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-pythonperf1-amd64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 414 ms: 2.68x faster                                                              |
| async_tree_memoization  | 526 ms                                                      | 222 ms: 2.38x faster                                                              |
| async_tree_none         | 435 ms                                                      | 185 ms: 2.35x faster                                                              |
| async_tree_cpu_io_mixed | 638 ms                                                      | 340 ms: 1.87x faster                                                              |
| Geometric mean          | (ref)                                                       | 2.30x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-pythonperf1-amd64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 45.4 ms: 1.36x faster                                                             |
| nbody          | 71.3 ms                                                     | 55.0 ms: 1.30x faster                                                             |
| pidigits       | 149 ms                                                      | 150 ms: 1.01x slower                                                              |
| Geometric mean | (ref)                                                       | 1.21x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-pythonperf1-amd64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 113 ms: 1.21x faster                                                              |
| regex_compile  | 106 ms                                                      | 88.6 ms: 1.20x faster                                                             |
| regex_effbot   | 1.66 ms                                                     | 1.41 ms: 1.18x faster                                                             |
| regex_v8       | 15.4 ms                                                     | 14.2 ms: 1.09x faster                                                             |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-pythonperf1-amd64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.55 ms: 1.40x faster                                                             |
| unpickle_pure_python | 183 us                                                      | 138 us: 1.33x faster                                                              |
| tomli_loads          | 1.67 sec                                                    | 1.33 sec: 1.25x faster                                                            |
| pickle_pure_python   | 270 us                                                      | 220 us: 1.23x faster                                                              |
| xml_etree_process    | 44.5 ms                                                     | 38.1 ms: 1.17x faster                                                             |
| xml_etree_parse      | 96.8 ms                                                     | 89.7 ms: 1.08x faster                                                             |
| xml_etree_generate   | 55.5 ms                                                     | 52.1 ms: 1.07x faster                                                             |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.9 ms: 1.03x faster                                                             |
| json_loads           | 14.0 us                                                     | 15.4 us: 1.10x slower                                                             |
| Geometric mean       | (ref)                                                       | 1.15x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-pythonperf1-amd64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 25.3 ms: 1.23x slower                                                             |
| python_startup_no_site | 15.5 ms                                                     | 19.2 ms: 1.24x slower                                                             |
| Geometric mean         | (ref)                                                       | 1.23x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-pythonperf1-amd64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.89 ms: 1.53x faster                                                             |
| genshi_text     | 19.8 ms                                                     | 15.9 ms: 1.25x faster                                                             |
| genshi_xml      | 41.0 ms                                                     | 34.9 ms: 1.17x faster                                                             |
| django_template | 28.9 ms                                                     | 25.6 ms: 1.13x faster                                                             |
| Geometric mean  | (ref)                                                       | 1.26x faster                                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-pythonperf1-amd64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 111 us: 3.02x faster                                                              |
| async_tree_io            | 1.11 sec                                                    | 414 ms: 2.68x faster                                                              |
| async_tree_memoization   | 526 ms                                                      | 222 ms: 2.38x faster                                                              |
| async_tree_none          | 435 ms                                                      | 185 ms: 2.35x faster                                                              |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 340 ms: 1.87x faster                                                              |
| deltablue                | 4.19 ms                                                     | 2.34 ms: 1.79x faster                                                             |
| pylint                   | 350 ms                                                      | 204 ms: 1.72x faster                                                              |
| logging_silent           | 94.6 ns                                                     | 56.8 ns: 1.66x faster                                                             |
| richards_super           | 52.2 ms                                                     | 32.5 ms: 1.61x faster                                                             |
| generators               | 32.4 ms                                                     | 20.1 ms: 1.61x faster                                                             |
| deepcopy_memo            | 28.8 us                                                     | 18.5 us: 1.55x faster                                                             |
| go                       | 139 ms                                                      | 89.5 ms: 1.55x faster                                                             |
| mako                     | 9.03 ms                                                     | 5.89 ms: 1.53x faster                                                             |
| scimark_lu               | 85.8 ms                                                     | 57.8 ms: 1.48x faster                                                             |
| pyflate                  | 409 ms                                                      | 278 ms: 1.47x faster                                                              |
| richards                 | 42.4 ms                                                     | 28.8 ms: 1.47x faster                                                             |
| chaos                    | 61.7 ms                                                     | 42.0 ms: 1.47x faster                                                             |
| deepcopy                 | 255 us                                                      | 182 us: 1.40x faster                                                              |
| json_dumps               | 9.16 ms                                                     | 6.55 ms: 1.40x faster                                                             |
| raytrace                 | 273 ms                                                      | 196 ms: 1.40x faster                                                              |
| float                    | 61.7 ms                                                     | 45.4 ms: 1.36x faster                                                             |
| comprehensions           | 16.5 us                                                     | 12.3 us: 1.34x faster                                                             |
| spectral_norm            | 77.3 ms                                                     | 57.7 ms: 1.34x faster                                                             |
| sqlglot_parse            | 1.22 ms                                                     | 911 us: 1.33x faster                                                              |
| scimark_monte_carlo      | 57.3 ms                                                     | 43.0 ms: 1.33x faster                                                             |
| unpickle_pure_python     | 183 us                                                      | 138 us: 1.33x faster                                                              |
| scimark_sor              | 106 ms                                                      | 80.3 ms: 1.32x faster                                                             |
| pathlib                  | 75.7 ms                                                     | 57.9 ms: 1.31x faster                                                             |
| sqlglot_transpile        | 1.48 ms                                                     | 1.14 ms: 1.30x faster                                                             |
| nbody                    | 71.3 ms                                                     | 55.0 ms: 1.30x faster                                                             |
| html5lib                 | 51.0 ms                                                     | 40.1 ms: 1.27x faster                                                             |
| crypto_pyaes             | 62.5 ms                                                     | 49.7 ms: 1.26x faster                                                             |
| tomli_loads              | 1.67 sec                                                    | 1.33 sec: 1.25x faster                                                            |
| genshi_text              | 19.8 ms                                                     | 15.9 ms: 1.25x faster                                                             |
| sqlite_synth             | 1.91 us                                                     | 1.54 us: 1.24x faster                                                             |
| coroutines               | 16.0 ms                                                     | 12.9 ms: 1.24x faster                                                             |
| hexiom                   | 5.74 ms                                                     | 4.68 ms: 1.23x faster                                                             |
| pickle_pure_python       | 270 us                                                      | 220 us: 1.23x faster                                                              |
| pycparser                | 930 ms                                                      | 760 ms: 1.22x faster                                                              |
| regex_dna                | 136 ms                                                      | 113 ms: 1.21x faster                                                              |
| regex_compile            | 106 ms                                                      | 88.6 ms: 1.20x faster                                                             |
| regex_effbot             | 1.66 ms                                                     | 1.41 ms: 1.18x faster                                                             |
| thrift                   | 617 us                                                      | 525 us: 1.18x faster                                                              |
| genshi_xml               | 41.0 ms                                                     | 34.9 ms: 1.17x faster                                                             |
| dulwich_log              | 50.5 ms                                                     | 43.0 ms: 1.17x faster                                                             |
| xml_etree_process        | 44.5 ms                                                     | 38.1 ms: 1.17x faster                                                             |
| deepcopy_reduce          | 2.20 us                                                     | 1.91 us: 1.15x faster                                                             |
| scimark_fft              | 187 ms                                                      | 163 ms: 1.15x faster                                                              |
| sympy_sum                | 107 ms                                                      | 93.6 ms: 1.14x faster                                                             |
| django_template          | 28.9 ms                                                     | 25.6 ms: 1.13x faster                                                             |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.44 ms: 1.12x faster                                                             |
| sympy_integrate          | 15.3 ms                                                     | 13.7 ms: 1.11x faster                                                             |
| bench_thread_pool        | 958 us                                                      | 863 us: 1.11x faster                                                              |
| regex_v8                 | 15.4 ms                                                     | 14.2 ms: 1.09x faster                                                             |
| docutils                 | 1.92 sec                                                    | 1.77 sec: 1.08x faster                                                            |
| 2to3                     | 246 ms                                                      | 227 ms: 1.08x faster                                                              |
| xml_etree_parse          | 96.8 ms                                                     | 89.7 ms: 1.08x faster                                                             |
| xml_etree_generate       | 55.5 ms                                                     | 52.1 ms: 1.07x faster                                                             |
| sympy_str                | 194 ms                                                      | 183 ms: 1.06x faster                                                              |
| sqlglot_optimize         | 39.8 ms                                                     | 38.2 ms: 1.04x faster                                                             |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.9 ms: 1.03x faster                                                             |
| mdp                      | 1.78 sec                                                    | 1.75 sec: 1.02x faster                                                            |
| sqlglot_normalize        | 205 ms                                                      | 202 ms: 1.02x faster                                                              |
| logging_format           | 6.76 us                                                     | 6.67 us: 1.01x faster                                                             |
| json                     | 3.14 ms                                                     | 3.10 ms: 1.01x faster                                                             |
| logging_simple           | 6.22 us                                                     | 6.17 us: 1.01x faster                                                             |
| pidigits                 | 149 ms                                                      | 150 ms: 1.01x slower                                                              |
| sympy_expand             | 314 ms                                                      | 320 ms: 1.02x slower                                                              |
| nqueens                  | 66.6 ms                                                     | 67.8 ms: 1.02x slower                                                             |
| pprint_pformat           | 1.22 sec                                                    | 1.29 sec: 1.06x slower                                                            |
| pprint_safe_repr         | 592 ms                                                      | 637 ms: 1.08x slower                                                              |
| meteor_contest           | 75.9 ms                                                     | 82.3 ms: 1.08x slower                                                             |
| json_loads               | 14.0 us                                                     | 15.4 us: 1.10x slower                                                             |
| async_generators         | 222 ms                                                      | 251 ms: 1.13x slower                                                              |
| telco                    | 3.94 ms                                                     | 4.57 ms: 1.16x slower                                                             |
| fannkuch                 | 256 ms                                                      | 298 ms: 1.17x slower                                                              |
| coverage                 | 39.0 ms                                                     | 47.0 ms: 1.21x slower                                                             |
| python_startup           | 20.6 ms                                                     | 25.3 ms: 1.23x slower                                                             |
| python_startup_no_site   | 15.5 ms                                                     | 19.2 ms: 1.24x slower                                                             |
| gc_traversal             | 1.41 ms                                                     | 1.97 ms: 1.40x slower                                                             |
| bench_mp_pool            | 62.0 ms                                                     | 87.9 ms: 1.42x slower                                                             |
| create_gc_cycles         | 800 us                                                      | 1.21 ms: 1.51x slower                                                             |
| Geometric mean           | (ref)                                                       | 1.21x faster                                                                      |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250212-3.14.0a4+-86ef9a1-JIT/bm-20250212-pythonperf1-amd64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.220x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: unknown