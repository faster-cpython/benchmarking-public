# Results vs. 3.10.4

- fork: python
- ref: b3c18bfd828ba90b9c71
- machine: windows-amd64
- commit hash: b3c18bf
- commit date: 2025-03-03
- overall geometric mean: 1.204x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250303-pythonperf1-amd64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 230 ms: 1.07x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.73 sec: 1.11x faster                                                      |
| html5lib       | 51.0 ms                                                     | 40.9 ms: 1.25x faster                                                       |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250303-pythonperf1-amd64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 418 ms: 2.65x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 219 ms: 2.40x faster                                                        |
| async_tree_none         | 435 ms                                                      | 187 ms: 2.32x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 343 ms: 1.86x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.29x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250303-pythonperf1-amd64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 47.4 ms: 1.30x faster                                                       |
| pidigits       | 149 ms                                                      | 154 ms: 1.03x slower                                                        |
| nbody          | 71.3 ms                                                     | 73.5 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250303-pythonperf1-amd64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 87.3 ms: 1.22x faster                                                       |
| regex_dna      | 136 ms                                                      | 118 ms: 1.15x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.50 ms: 1.11x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.9 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                       | 1.13x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250303-pythonperf1-amd64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.90 ms: 1.33x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 154 us: 1.19x faster                                                        |
| pickle_pure_python   | 270 us                                                      | 234 us: 1.15x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.45 sec: 1.15x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 41.3 ms: 1.08x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 91.0 ms: 1.06x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 58.6 ms: 1.06x slower                                                       |
| json_loads           | 14.0 us                                                     | 14.8 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.09x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250303-pythonperf1-amd64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 26.1 ms: 1.27x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 20.0 ms: 1.29x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.28x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250303-pythonperf1-amd64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 7.17 ms: 1.26x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 16.5 ms: 1.20x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 36.0 ms: 1.14x faster                                                       |
| django_template | 28.9 ms                                                     | 25.6 ms: 1.13x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.18x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250303-pythonperf1-amd64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 109 us: 3.08x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 418 ms: 2.65x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 219 ms: 2.40x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 32.0 ms: 2.36x faster                                                       |
| async_tree_none          | 435 ms                                                      | 187 ms: 2.32x faster                                                        |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 343 ms: 1.86x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.31 ms: 1.82x faster                                                       |
| pylint                   | 350 ms                                                      | 201 ms: 1.74x faster                                                        |
| generators               | 32.4 ms                                                     | 19.6 ms: 1.65x faster                                                       |
| go                       | 139 ms                                                      | 88.9 ms: 1.56x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 63.0 ns: 1.50x faster                                                       |
| chaos                    | 61.7 ms                                                     | 41.7 ms: 1.48x faster                                                       |
| richards_super           | 52.2 ms                                                     | 35.5 ms: 1.47x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.4 us: 1.45x faster                                                       |
| raytrace                 | 273 ms                                                      | 195 ms: 1.40x faster                                                        |
| deepcopy_memo            | 28.8 us                                                     | 21.0 us: 1.37x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 887 us: 1.37x faster                                                        |
| richards                 | 42.4 ms                                                     | 31.3 ms: 1.36x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.10 ms: 1.35x faster                                                       |
| deepcopy                 | 255 us                                                      | 191 us: 1.34x faster                                                        |
| json_dumps               | 9.16 ms                                                     | 6.90 ms: 1.33x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.40 ms: 1.31x faster                                                       |
| float                    | 61.7 ms                                                     | 47.4 ms: 1.30x faster                                                       |
| pyflate                  | 409 ms                                                      | 317 ms: 1.29x faster                                                        |
| spectral_norm            | 77.3 ms                                                     | 60.0 ms: 1.29x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 67.2 ms: 1.28x faster                                                       |
| mako                     | 9.03 ms                                                     | 7.17 ms: 1.26x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 40.9 ms: 1.25x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 50.6 ms: 1.23x faster                                                       |
| pycparser                | 930 ms                                                      | 755 ms: 1.23x faster                                                        |
| regex_compile            | 106 ms                                                      | 87.3 ms: 1.22x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 47.2 ms: 1.21x faster                                                       |
| thrift                   | 617 us                                                      | 512 us: 1.21x faster                                                        |
| sqlite_synth             | 1.91 us                                                     | 1.60 us: 1.20x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 16.5 ms: 1.20x faster                                                       |
| sympy_sum                | 107 ms                                                      | 89.5 ms: 1.20x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 154 us: 1.19x faster                                                        |
| coroutines               | 16.0 ms                                                     | 13.5 ms: 1.18x faster                                                       |
| scimark_sor              | 106 ms                                                      | 89.9 ms: 1.18x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 43.4 ms: 1.16x faster                                                       |
| regex_dna                | 136 ms                                                      | 118 ms: 1.15x faster                                                        |
| pickle_pure_python       | 270 us                                                      | 234 us: 1.15x faster                                                        |
| tomli_loads              | 1.67 sec                                                    | 1.45 sec: 1.15x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 36.0 ms: 1.14x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 13.5 ms: 1.14x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.57 sec: 1.13x faster                                                      |
| django_template          | 28.9 ms                                                     | 25.6 ms: 1.13x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 35.4 ms: 1.12x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.73 sec: 1.11x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 863 us: 1.11x faster                                                        |
| regex_effbot             | 1.66 ms                                                     | 1.50 ms: 1.11x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.99 us: 1.11x faster                                                       |
| sympy_str                | 194 ms                                                      | 176 ms: 1.10x faster                                                        |
| pprint_pformat           | 1.22 sec                                                    | 1.13 sec: 1.08x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 41.3 ms: 1.08x faster                                                       |
| 2to3                     | 246 ms                                                      | 230 ms: 1.07x faster                                                        |
| xml_etree_parse          | 96.8 ms                                                     | 91.0 ms: 1.06x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 62.8 ms: 1.06x faster                                                       |
| sympy_expand             | 314 ms                                                      | 297 ms: 1.06x faster                                                        |
| pprint_safe_repr         | 592 ms                                                      | 561 ms: 1.05x faster                                                        |
| sqlglot_normalize        | 205 ms                                                      | 196 ms: 1.05x faster                                                        |
| regex_v8                 | 15.4 ms                                                     | 14.9 ms: 1.04x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.67 ms: 1.02x faster                                                       |
| json                     | 3.14 ms                                                     | 3.10 ms: 1.01x faster                                                       |
| async_generators         | 222 ms                                                      | 224 ms: 1.01x slower                                                        |
| meteor_contest           | 75.9 ms                                                     | 77.6 ms: 1.02x slower                                                       |
| pidigits                 | 149 ms                                                      | 154 ms: 1.03x slower                                                        |
| scimark_fft              | 187 ms                                                      | 193 ms: 1.03x slower                                                        |
| nbody                    | 71.3 ms                                                     | 73.5 ms: 1.03x slower                                                       |
| logging_format           | 6.76 us                                                     | 7.09 us: 1.05x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.54 us: 1.05x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 58.6 ms: 1.06x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.8 us: 1.06x slower                                                       |
| fannkuch                 | 256 ms                                                      | 285 ms: 1.11x slower                                                        |
| coverage                 | 39.0 ms                                                     | 47.0 ms: 1.21x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.90 ms: 1.24x slower                                                       |
| python_startup           | 20.6 ms                                                     | 26.1 ms: 1.27x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 20.0 ms: 1.29x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 87.5 ms: 1.41x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.07 ms: 1.47x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.24 ms: 1.55x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.20x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250303-3.14.0a5+-b3c18bf/bm-20250303-pythonperf1-amd64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.204x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown