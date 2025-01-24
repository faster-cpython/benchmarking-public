# Results vs. 3.10.4

- fork: mdboom
- ref: test_without_pgo_wor
- machine: windows-amd64
- commit hash: 71a13ea
- commit date: 2025-01-23
- overall geometric mean: 1.164x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-pythonperf1-amd64-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 235 ms: 1.05x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.71 sec: 1.12x faster                                                      |
| html5lib       | 51.0 ms                                                     | 40.1 ms: 1.27x faster                                                       |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-pythonperf1-amd64-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 419 ms: 2.65x faster                                                        |
| async_tree_none         | 435 ms                                                      | 189 ms: 2.30x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 230 ms: 2.29x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 348 ms: 1.83x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.25x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-pythonperf1-amd64-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 52.4 ms: 1.18x faster                                                       |
| pidigits       | 149 ms                                                      | 147 ms: 1.02x faster                                                        |
| nbody          | 71.3 ms                                                     | 77.5 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-pythonperf1-amd64-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 89.6 ms: 1.18x faster                                                       |
| regex_dna      | 136 ms                                                      | 116 ms: 1.17x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.50 ms: 1.11x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 15.1 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-pythonperf1-amd64-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.83 ms: 1.34x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.44 sec: 1.16x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 165 us: 1.11x faster                                                        |
| pickle_pure_python   | 270 us                                                      | 244 us: 1.10x faster                                                        |
| xml_etree_parse      | 96.8 ms                                                     | 89.7 ms: 1.08x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 43.6 ms: 1.02x faster                                                       |
| json_loads           | 14.0 us                                                     | 14.5 us: 1.03x slower                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 59.9 ms: 1.08x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.07x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-pythonperf1-amd64-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 18.1 ms: 1.17x slower                                                       |
| python_startup         | 20.6 ms                                                     | 24.4 ms: 1.18x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.18x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-pythonperf1-amd64-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 7.07 ms: 1.28x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 16.8 ms: 1.18x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 36.0 ms: 1.14x faster                                                       |
| django_template | 28.9 ms                                                     | 26.1 ms: 1.11x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.17x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-pythonperf1-amd64-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 115 us: 2.93x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 419 ms: 2.65x faster                                                        |
| async_tree_none          | 435 ms                                                      | 189 ms: 2.30x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 230 ms: 2.29x faster                                                        |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 348 ms: 1.83x faster                                                        |
| pylint                   | 350 ms                                                      | 201 ms: 1.74x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.43 ms: 1.72x faster                                                       |
| go                       | 139 ms                                                      | 93.9 ms: 1.48x faster                                                       |
| generators               | 32.4 ms                                                     | 22.4 ms: 1.45x faster                                                       |
| chaos                    | 61.7 ms                                                     | 43.7 ms: 1.41x faster                                                       |
| richards_super           | 52.2 ms                                                     | 37.4 ms: 1.40x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.83 ms: 1.34x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 909 us: 1.34x faster                                                        |
| deepcopy                 | 255 us                                                      | 192 us: 1.33x faster                                                        |
| deepcopy_memo            | 28.8 us                                                     | 21.7 us: 1.33x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.13 ms: 1.31x faster                                                       |
| raytrace                 | 273 ms                                                      | 210 ms: 1.30x faster                                                        |
| logging_silent           | 94.6 ns                                                     | 73.0 ns: 1.30x faster                                                       |
| comprehensions           | 16.5 us                                                     | 12.7 us: 1.30x faster                                                       |
| mako                     | 9.03 ms                                                     | 7.07 ms: 1.28x faster                                                       |
| richards                 | 42.4 ms                                                     | 33.3 ms: 1.27x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 40.1 ms: 1.27x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 49.3 ms: 1.27x faster                                                       |
| pyflate                  | 409 ms                                                      | 323 ms: 1.27x faster                                                        |
| pycparser                | 930 ms                                                      | 746 ms: 1.25x faster                                                        |
| scimark_lu               | 85.8 ms                                                     | 69.4 ms: 1.24x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.72 ms: 1.22x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 41.5 ms: 1.22x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 64.5 ms: 1.20x faster                                                       |
| regex_compile            | 106 ms                                                      | 89.6 ms: 1.18x faster                                                       |
| float                    | 61.7 ms                                                     | 52.4 ms: 1.18x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 16.8 ms: 1.18x faster                                                       |
| regex_dna                | 136 ms                                                      | 116 ms: 1.17x faster                                                        |
| sympy_sum                | 107 ms                                                      | 91.7 ms: 1.17x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.44 sec: 1.16x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 840 us: 1.14x faster                                                        |
| genshi_xml               | 41.0 ms                                                     | 36.0 ms: 1.14x faster                                                       |
| thrift                   | 617 us                                                      | 546 us: 1.13x faster                                                        |
| deepcopy_reduce          | 2.20 us                                                     | 1.95 us: 1.13x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 50.9 ms: 1.13x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.71 sec: 1.12x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.7 ms: 1.12x faster                                                       |
| scimark_sor              | 106 ms                                                      | 95.4 ms: 1.11x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 165 us: 1.11x faster                                                        |
| sqlite_synth             | 1.91 us                                                     | 1.72 us: 1.11x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.50 ms: 1.11x faster                                                       |
| django_template          | 28.9 ms                                                     | 26.1 ms: 1.11x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 244 us: 1.10x faster                                                        |
| mdp                      | 1.78 sec                                                    | 1.62 sec: 1.10x faster                                                      |
| sqlglot_optimize         | 39.8 ms                                                     | 36.8 ms: 1.08x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 89.7 ms: 1.08x faster                                                       |
| sympy_str                | 194 ms                                                      | 181 ms: 1.07x faster                                                        |
| pprint_pformat           | 1.22 sec                                                    | 1.14 sec: 1.07x faster                                                      |
| coroutines               | 16.0 ms                                                     | 15.1 ms: 1.06x faster                                                       |
| 2to3                     | 246 ms                                                      | 235 ms: 1.05x faster                                                        |
| pprint_safe_repr         | 592 ms                                                      | 566 ms: 1.05x faster                                                        |
| json                     | 3.14 ms                                                     | 3.01 ms: 1.04x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 65.2 ms: 1.02x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.67 ms: 1.02x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 15.1 ms: 1.02x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 43.6 ms: 1.02x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 202 ms: 1.02x faster                                                        |
| pidigits                 | 149 ms                                                      | 147 ms: 1.02x faster                                                        |
| sympy_expand             | 314 ms                                                      | 310 ms: 1.02x faster                                                        |
| meteor_contest           | 75.9 ms                                                     | 78.0 ms: 1.03x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.5 us: 1.03x slower                                                       |
| pathlib                  | 75.7 ms                                                     | 78.4 ms: 1.04x slower                                                       |
| logging_format           | 6.76 us                                                     | 7.00 us: 1.04x slower                                                       |
| async_generators         | 222 ms                                                      | 231 ms: 1.04x slower                                                        |
| scimark_fft              | 187 ms                                                      | 195 ms: 1.04x slower                                                        |
| logging_simple           | 6.22 us                                                     | 6.58 us: 1.06x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 59.9 ms: 1.08x slower                                                       |
| nbody                    | 71.3 ms                                                     | 77.5 ms: 1.09x slower                                                       |
| fannkuch                 | 256 ms                                                      | 290 ms: 1.13x slower                                                        |
| python_startup_no_site   | 15.5 ms                                                     | 18.1 ms: 1.17x slower                                                       |
| python_startup           | 20.6 ms                                                     | 24.4 ms: 1.18x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.81 ms: 1.22x slower                                                       |
| coverage                 | 39.0 ms                                                     | 50.4 ms: 1.29x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.97 ms: 1.40x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 88.6 ms: 1.43x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.19 ms: 1.49x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.16x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250123-3.14.0a4+-71a13ea/bm-20250123-pythonperf1-amd64-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.164x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: unknown