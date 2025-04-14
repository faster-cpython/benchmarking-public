# Results vs. 3.10.4

- fork: python
- ref: fecf8bc8f2fd09a9a4c5
- machine: windows-amd64
- commit hash: fecf8bc
- commit date: 2025-02-28
- overall geometric mean: 1.223x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf1-amd64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 227 ms: 1.09x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.66 sec: 1.16x faster                                                      |
| html5lib       | 51.0 ms                                                     | 40.2 ms: 1.27x faster                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf1-amd64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 417 ms: 2.66x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 217 ms: 2.42x faster                                                        |
| async_tree_none         | 435 ms                                                      | 185 ms: 2.35x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 340 ms: 1.87x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.31x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf1-amd64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 46.2 ms: 1.33x faster                                                       |
| pidigits       | 149 ms                                                      | 150 ms: 1.01x slower                                                        |
| nbody          | 71.3 ms                                                     | 72.7 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf1-amd64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 86.9 ms: 1.22x faster                                                       |
| regex_dna      | 136 ms                                                      | 119 ms: 1.15x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.48 ms: 1.12x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.9 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                       | 1.13x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf1-amd64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.76 ms: 1.36x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 150 us: 1.22x faster                                                        |
| pickle_pure_python   | 270 us                                                      | 227 us: 1.19x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.42 sec: 1.18x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 40.3 ms: 1.10x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 89.1 ms: 1.09x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.0 ms: 1.05x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 57.2 ms: 1.03x slower                                                       |
| json_loads           | 14.0 us                                                     | 14.6 us: 1.04x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf1-amd64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 25.0 ms: 1.21x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 19.0 ms: 1.23x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.22x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf1-amd64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.68 ms: 1.35x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 17.1 ms: 1.16x faster                                                       |
| django_template | 28.9 ms                                                     | 25.2 ms: 1.15x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 37.3 ms: 1.10x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.19x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf1-amd64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 106 us: 3.17x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 417 ms: 2.66x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 217 ms: 2.42x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 31.8 ms: 2.38x faster                                                       |
| async_tree_none          | 435 ms                                                      | 185 ms: 2.35x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.22 ms: 1.89x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 340 ms: 1.87x faster                                                        |
| pylint                   | 350 ms                                                      | 198 ms: 1.77x faster                                                        |
| generators               | 32.4 ms                                                     | 19.6 ms: 1.65x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 59.6 ns: 1.59x faster                                                       |
| go                       | 139 ms                                                      | 87.6 ms: 1.59x faster                                                       |
| richards_super           | 52.2 ms                                                     | 34.0 ms: 1.54x faster                                                       |
| chaos                    | 61.7 ms                                                     | 41.5 ms: 1.49x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.4 us: 1.45x faster                                                       |
| richards                 | 42.4 ms                                                     | 29.8 ms: 1.42x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 20.3 us: 1.42x faster                                                       |
| raytrace                 | 273 ms                                                      | 193 ms: 1.41x faster                                                        |
| deepcopy                 | 255 us                                                      | 184 us: 1.39x faster                                                        |
| sqlglot_parse            | 1.22 ms                                                     | 883 us: 1.38x faster                                                        |
| json_dumps               | 9.16 ms                                                     | 6.76 ms: 1.36x faster                                                       |
| mako                     | 9.03 ms                                                     | 6.68 ms: 1.35x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.09 ms: 1.35x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 63.6 ms: 1.35x faster                                                       |
| float                    | 61.7 ms                                                     | 46.2 ms: 1.33x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.36 ms: 1.32x faster                                                       |
| pyflate                  | 409 ms                                                      | 311 ms: 1.31x faster                                                        |
| html5lib                 | 51.0 ms                                                     | 40.2 ms: 1.27x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 45.2 ms: 1.27x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 61.3 ms: 1.26x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 50.2 ms: 1.25x faster                                                       |
| scimark_sor              | 106 ms                                                      | 85.4 ms: 1.24x faster                                                       |
| pycparser                | 930 ms                                                      | 752 ms: 1.24x faster                                                        |
| unpickle_pure_python     | 183 us                                                      | 150 us: 1.22x faster                                                        |
| regex_compile            | 106 ms                                                      | 86.9 ms: 1.22x faster                                                       |
| thrift                   | 617 us                                                      | 512 us: 1.21x faster                                                        |
| sympy_sum                | 107 ms                                                      | 88.9 ms: 1.20x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.59 us: 1.20x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.4 ms: 1.20x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 42.3 ms: 1.19x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 227 us: 1.19x faster                                                        |
| tomli_loads              | 1.67 sec                                                    | 1.42 sec: 1.18x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 17.1 ms: 1.16x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.66 sec: 1.16x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.92 us: 1.15x faster                                                       |
| regex_dna                | 136 ms                                                      | 119 ms: 1.15x faster                                                        |
| sympy_integrate          | 15.3 ms                                                     | 13.3 ms: 1.15x faster                                                       |
| django_template          | 28.9 ms                                                     | 25.2 ms: 1.15x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 35.1 ms: 1.13x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.58 sec: 1.13x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.48 ms: 1.12x faster                                                       |
| sympy_str                | 194 ms                                                      | 174 ms: 1.12x faster                                                        |
| bench_thread_pool        | 958 us                                                      | 856 us: 1.12x faster                                                        |
| xml_etree_process        | 44.5 ms                                                     | 40.3 ms: 1.10x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 37.3 ms: 1.10x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.12 sec: 1.09x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 89.1 ms: 1.09x faster                                                       |
| 2to3                     | 246 ms                                                      | 227 ms: 1.09x faster                                                        |
| sqlglot_normalize        | 205 ms                                                      | 191 ms: 1.07x faster                                                        |
| pprint_safe_repr         | 592 ms                                                      | 555 ms: 1.07x faster                                                        |
| nqueens                  | 66.6 ms                                                     | 62.6 ms: 1.06x faster                                                       |
| sympy_expand             | 314 ms                                                      | 298 ms: 1.06x faster                                                        |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.0 ms: 1.05x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 14.9 ms: 1.04x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.65 ms: 1.03x faster                                                       |
| pidigits                 | 149 ms                                                      | 150 ms: 1.01x slower                                                        |
| logging_format           | 6.76 us                                                     | 6.85 us: 1.01x slower                                                       |
| scimark_fft              | 187 ms                                                      | 190 ms: 1.01x slower                                                        |
| nbody                    | 71.3 ms                                                     | 72.7 ms: 1.02x slower                                                       |
| meteor_contest           | 75.9 ms                                                     | 77.9 ms: 1.03x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.40 us: 1.03x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 57.2 ms: 1.03x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.6 us: 1.04x slower                                                       |
| fannkuch                 | 256 ms                                                      | 276 ms: 1.08x slower                                                        |
| telco                    | 3.94 ms                                                     | 4.77 ms: 1.21x slower                                                       |
| python_startup           | 20.6 ms                                                     | 25.0 ms: 1.21x slower                                                       |
| coverage                 | 39.0 ms                                                     | 47.5 ms: 1.22x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 19.0 ms: 1.23x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 86.5 ms: 1.39x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.04 ms: 1.45x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.22 ms: 1.53x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.22x faster                                                                |

Benchmark hidden because not significant (2): json, async_generators
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250228-3.14.0a5+-fecf8bc/bm-20250228-pythonperf1-amd64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.223x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: unknown