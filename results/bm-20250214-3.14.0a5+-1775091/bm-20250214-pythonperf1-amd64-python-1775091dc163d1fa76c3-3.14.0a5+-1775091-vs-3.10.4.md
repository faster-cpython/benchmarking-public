# Results vs. 3.10.4

- fork: python
- ref: 1775091dc163d1fa76c3
- machine: windows-amd64
- commit hash: 1775091
- commit date: 2025-02-14
- overall geometric mean: 1.240x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250214-pythonperf1-amd64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 221 ms: 1.11x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.64 sec: 1.17x faster                                                      |
| html5lib       | 51.0 ms                                                     | 38.6 ms: 1.32x faster                                                       |
| Geometric mean | (ref)                                                       | 1.20x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250214-pythonperf1-amd64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 415 ms: 2.67x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 222 ms: 2.37x faster                                                        |
| async_tree_none         | 435 ms                                                      | 190 ms: 2.29x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 343 ms: 1.86x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.28x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250214-pythonperf1-amd64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 44.7 ms: 1.38x faster                                                       |
| nbody          | 71.3 ms                                                     | 69.7 ms: 1.02x faster                                                       |
| pidigits       | 149 ms                                                      | 150 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250214-pythonperf1-amd64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 84.2 ms: 1.26x faster                                                       |
| regex_dna      | 136 ms                                                      | 115 ms: 1.19x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.46 ms: 1.14x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.3 ms: 1.08x faster                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250214-pythonperf1-amd64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.69 ms: 1.37x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 143 us: 1.28x faster                                                        |
| pickle_pure_python   | 270 us                                                      | 221 us: 1.22x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.37 sec: 1.22x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 39.8 ms: 1.12x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 90.2 ms: 1.07x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.0 ms: 1.03x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 56.5 ms: 1.02x slower                                                       |
| json_loads           | 14.0 us                                                     | 15.4 us: 1.10x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.13x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250214-pythonperf1-amd64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 24.5 ms: 1.19x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 18.8 ms: 1.21x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.20x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250214-pythonperf1-amd64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.63 ms: 1.36x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 17.0 ms: 1.17x faster                                                       |
| django_template | 28.9 ms                                                     | 25.1 ms: 1.15x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 36.5 ms: 1.13x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.20x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250214-pythonperf1-amd64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 111 us: 3.03x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 415 ms: 2.67x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 29.4 ms: 2.58x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 222 ms: 2.37x faster                                                        |
| async_tree_none          | 435 ms                                                      | 190 ms: 2.29x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.16 ms: 1.94x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 343 ms: 1.86x faster                                                        |
| pylint                   | 350 ms                                                      | 197 ms: 1.77x faster                                                        |
| generators               | 32.4 ms                                                     | 19.6 ms: 1.65x faster                                                       |
| go                       | 139 ms                                                      | 84.4 ms: 1.65x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 57.5 ns: 1.65x faster                                                       |
| richards_super           | 52.2 ms                                                     | 33.4 ms: 1.56x faster                                                       |
| chaos                    | 61.7 ms                                                     | 41.7 ms: 1.48x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.2 us: 1.48x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 19.5 us: 1.47x faster                                                       |
| richards                 | 42.4 ms                                                     | 29.4 ms: 1.44x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 59.9 ms: 1.43x faster                                                       |
| raytrace                 | 273 ms                                                      | 194 ms: 1.41x faster                                                        |
| sqlglot_parse            | 1.22 ms                                                     | 870 us: 1.40x faster                                                        |
| float                    | 61.7 ms                                                     | 44.7 ms: 1.38x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.19 ms: 1.37x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.08 ms: 1.37x faster                                                       |
| pyflate                  | 409 ms                                                      | 299 ms: 1.37x faster                                                        |
| json_dumps               | 9.16 ms                                                     | 6.69 ms: 1.37x faster                                                       |
| mako                     | 9.03 ms                                                     | 6.63 ms: 1.36x faster                                                       |
| deepcopy                 | 255 us                                                      | 188 us: 1.36x faster                                                        |
| html5lib                 | 51.0 ms                                                     | 38.6 ms: 1.32x faster                                                       |
| pycparser                | 930 ms                                                      | 724 ms: 1.29x faster                                                        |
| unpickle_pure_python     | 183 us                                                      | 143 us: 1.28x faster                                                        |
| spectral_norm            | 77.3 ms                                                     | 60.6 ms: 1.27x faster                                                       |
| scimark_sor              | 106 ms                                                      | 83.9 ms: 1.26x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 49.6 ms: 1.26x faster                                                       |
| regex_compile            | 106 ms                                                      | 84.2 ms: 1.26x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 45.7 ms: 1.25x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 41.2 ms: 1.23x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 221 us: 1.22x faster                                                        |
| tomli_loads              | 1.67 sec                                                    | 1.37 sec: 1.22x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.57 us: 1.21x faster                                                       |
| thrift                   | 617 us                                                      | 510 us: 1.21x faster                                                        |
| mdp                      | 1.78 sec                                                    | 1.48 sec: 1.21x faster                                                      |
| coroutines               | 16.0 ms                                                     | 13.3 ms: 1.20x faster                                                       |
| sympy_sum                | 107 ms                                                      | 89.2 ms: 1.20x faster                                                       |
| regex_dna                | 136 ms                                                      | 115 ms: 1.19x faster                                                        |
| docutils                 | 1.92 sec                                                    | 1.64 sec: 1.17x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 17.0 ms: 1.17x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 13.2 ms: 1.16x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.91 us: 1.15x faster                                                       |
| django_template          | 28.9 ms                                                     | 25.1 ms: 1.15x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 837 us: 1.14x faster                                                        |
| pprint_pformat           | 1.22 sec                                                    | 1.07 sec: 1.14x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.46 ms: 1.14x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 35.1 ms: 1.13x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 36.5 ms: 1.13x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 39.8 ms: 1.12x faster                                                       |
| sympy_str                | 194 ms                                                      | 174 ms: 1.11x faster                                                        |
| 2to3                     | 246 ms                                                      | 221 ms: 1.11x faster                                                        |
| pprint_safe_repr         | 592 ms                                                      | 539 ms: 1.10x faster                                                        |
| regex_v8                 | 15.4 ms                                                     | 14.3 ms: 1.08x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 62.0 ms: 1.08x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 90.2 ms: 1.07x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 191 ms: 1.07x faster                                                        |
| sympy_expand             | 314 ms                                                      | 297 ms: 1.06x faster                                                        |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.57 ms: 1.06x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.0 ms: 1.03x faster                                                       |
| nbody                    | 71.3 ms                                                     | 69.7 ms: 1.02x faster                                                       |
| async_generators         | 222 ms                                                      | 219 ms: 1.01x faster                                                        |
| json                     | 3.14 ms                                                     | 3.10 ms: 1.01x faster                                                       |
| pidigits                 | 149 ms                                                      | 150 ms: 1.01x slower                                                        |
| xml_etree_generate       | 55.5 ms                                                     | 56.5 ms: 1.02x slower                                                       |
| json_loads               | 14.0 us                                                     | 15.4 us: 1.10x slower                                                       |
| fannkuch                 | 256 ms                                                      | 281 ms: 1.10x slower                                                        |
| telco                    | 3.94 ms                                                     | 4.66 ms: 1.18x slower                                                       |
| python_startup           | 20.6 ms                                                     | 24.5 ms: 1.19x slower                                                       |
| coverage                 | 39.0 ms                                                     | 46.9 ms: 1.20x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 18.8 ms: 1.21x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 84.2 ms: 1.36x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.98 ms: 1.41x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.22 ms: 1.53x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.23x faster                                                                |

Benchmark hidden because not significant (4): meteor_contest, scimark_fft, logging_format, logging_simple
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250214-3.14.0a5+-1775091/bm-20250214-pythonperf1-amd64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.240x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: unknown