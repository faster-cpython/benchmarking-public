# Results vs. 3.10.4

- fork: python
- ref: 61b35f74aa4a6ac60663
- machine: windows-amd64
- commit hash: 61b35f7
- commit date: 2025-01-18
- overall geometric mean: 1.236x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 229 ms: 1.07x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.75 sec: 1.10x faster                                                      |
| html5lib       | 51.0 ms                                                     | 38.7 ms: 1.32x faster                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 410 ms: 2.70x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 227 ms: 2.31x faster                                                        |
| async_tree_none         | 435 ms                                                      | 190 ms: 2.29x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 349 ms: 1.83x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.26x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 39.2 ms: 1.58x faster                                                       |
| nbody          | 71.3 ms                                                     | 57.9 ms: 1.23x faster                                                       |
| pidigits       | 149 ms                                                      | 146 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                       | 1.25x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 81.3 ms: 1.30x faster                                                       |
| regex_dna      | 136 ms                                                      | 112 ms: 1.22x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.41 ms: 1.18x faster                                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 114 us: 1.61x faster                                                        |
| json_dumps           | 9.16 ms                                                     | 6.48 ms: 1.41x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.20 sec: 1.39x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 216 us: 1.25x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 37.0 ms: 1.20x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 50.6 ms: 1.10x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 88.4 ms: 1.10x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 59.8 ms: 1.09x faster                                                       |
| unpickle             | 9.09 us                                                     | 8.83 us: 1.03x faster                                                       |
| json_loads           | 14.0 us                                                     | 14.7 us: 1.05x slower                                                       |
| pickle_dict          | 17.2 us                                                     | 18.2 us: 1.06x slower                                                       |
| pickle               | 6.85 us                                                     | 7.84 us: 1.15x slower                                                       |
| pickle_list          | 2.75 us                                                     | 3.24 us: 1.18x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.11x faster                                                                |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 17.9 ms: 1.15x slower                                                       |
| python_startup         | 20.6 ms                                                     | 24.1 ms: 1.17x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.16x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.10 ms: 1.77x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 18.7 ms: 1.06x faster                                                       |
| django_template | 28.9 ms                                                     | 27.6 ms: 1.05x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 45.9 ms: 1.12x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.15x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 113 us: 2.98x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 410 ms: 2.70x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 227 ms: 2.31x faster                                                        |
| async_tree_none          | 435 ms                                                      | 190 ms: 2.29x faster                                                        |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 349 ms: 1.83x faster                                                        |
| mako                     | 9.03 ms                                                     | 5.10 ms: 1.77x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.43 ms: 1.72x faster                                                       |
| scimark_sor              | 106 ms                                                      | 62.5 ms: 1.70x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 17.3 us: 1.66x faster                                                       |
| pylint                   | 350 ms                                                      | 211 ms: 1.66x faster                                                        |
| spectral_norm            | 77.3 ms                                                     | 47.0 ms: 1.64x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 114 us: 1.61x faster                                                        |
| float                    | 61.7 ms                                                     | 39.2 ms: 1.58x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 60.1 ns: 1.57x faster                                                       |
| pyflate                  | 409 ms                                                      | 268 ms: 1.53x faster                                                        |
| crypto_pyaes             | 62.5 ms                                                     | 41.3 ms: 1.51x faster                                                       |
| chaos                    | 61.7 ms                                                     | 41.0 ms: 1.50x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 38.1 ms: 1.50x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 57.3 ms: 1.50x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.42 sec: 1.48x faster                                                      |
| go                       | 139 ms                                                      | 94.2 ms: 1.47x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 853 us: 1.42x faster                                                        |
| json_dumps               | 9.16 ms                                                     | 6.48 ms: 1.41x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.20 sec: 1.39x faster                                                      |
| comprehensions           | 16.5 us                                                     | 12.0 us: 1.38x faster                                                       |
| deepcopy                 | 255 us                                                      | 188 us: 1.36x faster                                                        |
| sqlglot_transpile        | 1.48 ms                                                     | 1.10 ms: 1.34x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 38.7 ms: 1.32x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.08 ms: 1.31x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 561 ms: 1.31x faster                                                        |
| regex_compile            | 106 ms                                                      | 81.3 ms: 1.30x faster                                                       |
| generators               | 32.4 ms                                                     | 25.0 ms: 1.30x faster                                                       |
| pycparser                | 930 ms                                                      | 721 ms: 1.29x faster                                                        |
| richards_super           | 52.2 ms                                                     | 40.7 ms: 1.28x faster                                                       |
| raytrace                 | 273 ms                                                      | 213 ms: 1.28x faster                                                        |
| scimark_fft              | 187 ms                                                      | 149 ms: 1.26x faster                                                        |
| pickle_pure_python       | 270 us                                                      | 216 us: 1.25x faster                                                        |
| dulwich_log              | 50.5 ms                                                     | 40.5 ms: 1.25x faster                                                       |
| nbody                    | 71.3 ms                                                     | 57.9 ms: 1.23x faster                                                       |
| regex_dna                | 136 ms                                                      | 112 ms: 1.22x faster                                                        |
| sqlite_synth             | 1.91 us                                                     | 1.57 us: 1.22x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.01 sec: 1.21x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 37.0 ms: 1.20x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 501 ms: 1.18x faster                                                        |
| regex_effbot             | 1.66 ms                                                     | 1.41 ms: 1.18x faster                                                       |
| richards                 | 42.4 ms                                                     | 36.1 ms: 1.17x faster                                                       |
| sympy_sum                | 107 ms                                                      | 91.1 ms: 1.17x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.89 us: 1.16x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 831 us: 1.15x faster                                                        |
| hexiom                   | 5.74 ms                                                     | 5.08 ms: 1.13x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 13.6 ms: 1.12x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.60 sec: 1.12x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 50.6 ms: 1.10x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.75 sec: 1.10x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 88.4 ms: 1.10x faster                                                       |
| sympy_str                | 194 ms                                                      | 178 ms: 1.09x faster                                                        |
| fannkuch                 | 256 ms                                                      | 235 ms: 1.09x faster                                                        |
| xml_etree_iterparse      | 65.0 ms                                                     | 59.8 ms: 1.09x faster                                                       |
| thrift                   | 617 us                                                      | 570 us: 1.08x faster                                                        |
| 2to3                     | 246 ms                                                      | 229 ms: 1.07x faster                                                        |
| coroutines               | 16.0 ms                                                     | 15.1 ms: 1.06x faster                                                       |
| json                     | 3.14 ms                                                     | 2.96 ms: 1.06x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 18.7 ms: 1.06x faster                                                       |
| django_template          | 28.9 ms                                                     | 27.6 ms: 1.05x faster                                                       |
| sympy_expand             | 314 ms                                                      | 304 ms: 1.03x faster                                                        |
| nqueens                  | 66.6 ms                                                     | 64.5 ms: 1.03x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 38.6 ms: 1.03x faster                                                       |
| unpickle                 | 9.09 us                                                     | 8.83 us: 1.03x faster                                                       |
| pidigits                 | 149 ms                                                      | 146 ms: 1.02x faster                                                        |
| meteor_contest           | 75.9 ms                                                     | 74.9 ms: 1.01x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.87 us: 1.02x slower                                                       |
| sqlglot_normalize        | 205 ms                                                      | 209 ms: 1.02x slower                                                        |
| logging_simple           | 6.22 us                                                     | 6.43 us: 1.03x slower                                                       |
| pathlib                  | 75.7 ms                                                     | 78.5 ms: 1.04x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.7 us: 1.05x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 18.2 us: 1.06x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.38 ms: 1.11x slower                                                       |
| async_generators         | 222 ms                                                      | 248 ms: 1.12x slower                                                        |
| genshi_xml               | 41.0 ms                                                     | 45.9 ms: 1.12x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.84 us: 1.15x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 17.9 ms: 1.15x slower                                                       |
| python_startup           | 20.6 ms                                                     | 24.1 ms: 1.17x slower                                                       |
| pickle_list              | 2.75 us                                                     | 3.24 us: 1.18x slower                                                       |
| unpack_sequence          | 39.6 ns                                                     | 49.0 ns: 1.24x slower                                                       |
| coverage                 | 39.0 ms                                                     | 50.6 ms: 1.30x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 87.7 ms: 1.41x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.99 ms: 1.41x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.21 ms: 1.51x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.21x faster                                                                |

Benchmark hidden because not significant (2): unpickle_list, regex_v8
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (12) of results/bm-20250118-3.14.0a4+-61b35f7-JIT/bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.236x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: unknown