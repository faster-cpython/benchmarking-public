# Results vs. 3.10.4

- fork: faster-cpython
- ref: use_stackrefs_single
- machine: windows-amd64
- commit hash: 916faf4
- commit date: 2025-03-07
- overall geometric mean: 1.219x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-pythonperf1-amd64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 228 ms: 1.08x faster                                                                  |
| docutils       | 1.92 sec                                                    | 1.69 sec: 1.13x faster                                                                |
| html5lib       | 51.0 ms                                                     | 41.3 ms: 1.24x faster                                                                 |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-pythonperf1-amd64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|-------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 426 ms: 2.60x faster                                                                  |
| async_tree_memoization  | 526 ms                                                      | 220 ms: 2.40x faster                                                                  |
| async_tree_none         | 435 ms                                                      | 190 ms: 2.29x faster                                                                  |
| async_tree_cpu_io_mixed | 638 ms                                                      | 344 ms: 1.85x faster                                                                  |
| Geometric mean          | (ref)                                                       | 2.27x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-pythonperf1-amd64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 47.0 ms: 1.31x faster                                                                 |
| nbody          | 71.3 ms                                                     | 66.2 ms: 1.08x faster                                                                 |
| pidigits       | 149 ms                                                      | 152 ms: 1.02x slower                                                                  |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-pythonperf1-amd64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 86.2 ms: 1.23x faster                                                                 |
| regex_dna      | 136 ms                                                      | 114 ms: 1.20x faster                                                                  |
| regex_effbot   | 1.66 ms                                                     | 1.42 ms: 1.16x faster                                                                 |
| regex_v8       | 15.4 ms                                                     | 14.6 ms: 1.06x faster                                                                 |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-pythonperf1-amd64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.95 ms: 1.32x faster                                                                 |
| unpickle_pure_python | 183 us                                                      | 148 us: 1.24x faster                                                                  |
| pickle_pure_python   | 270 us                                                      | 227 us: 1.19x faster                                                                  |
| tomli_loads          | 1.67 sec                                                    | 1.42 sec: 1.18x faster                                                                |
| xml_etree_process    | 44.5 ms                                                     | 41.7 ms: 1.07x faster                                                                 |
| xml_etree_parse      | 96.8 ms                                                     | 91.9 ms: 1.05x faster                                                                 |
| xml_etree_iterparse  | 65.0 ms                                                     | 66.1 ms: 1.02x slower                                                                 |
| xml_etree_generate   | 55.5 ms                                                     | 58.3 ms: 1.05x slower                                                                 |
| json_loads           | 14.0 us                                                     | 15.1 us: 1.07x slower                                                                 |
| Geometric mean       | (ref)                                                       | 1.09x faster                                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-pythonperf1-amd64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.7 ms: 1.27x slower                                                                 |
| python_startup         | 20.6 ms                                                     | 26.1 ms: 1.27x slower                                                                 |
| Geometric mean         | (ref)                                                       | 1.27x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-pythonperf1-amd64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|-----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 7.04 ms: 1.28x faster                                                                 |
| genshi_text     | 19.8 ms                                                     | 16.9 ms: 1.17x faster                                                                 |
| genshi_xml      | 41.0 ms                                                     | 37.1 ms: 1.11x faster                                                                 |
| django_template | 28.9 ms                                                     | 26.2 ms: 1.10x faster                                                                 |
| Geometric mean  | (ref)                                                       | 1.16x faster                                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-pythonperf1-amd64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|--------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 111 us: 3.02x faster                                                                  |
| async_tree_io            | 1.11 sec                                                    | 426 ms: 2.60x faster                                                                  |
| async_tree_memoization   | 526 ms                                                      | 220 ms: 2.40x faster                                                                  |
| pathlib                  | 75.7 ms                                                     | 32.2 ms: 2.35x faster                                                                 |
| async_tree_none          | 435 ms                                                      | 190 ms: 2.29x faster                                                                  |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 344 ms: 1.85x faster                                                                  |
| deltablue                | 4.19 ms                                                     | 2.27 ms: 1.85x faster                                                                 |
| pylint                   | 350 ms                                                      | 204 ms: 1.72x faster                                                                  |
| generators               | 32.4 ms                                                     | 19.5 ms: 1.66x faster                                                                 |
| logging_silent           | 94.6 ns                                                     | 58.7 ns: 1.61x faster                                                                 |
| go                       | 139 ms                                                      | 87.6 ms: 1.59x faster                                                                 |
| richards_super           | 52.2 ms                                                     | 33.1 ms: 1.58x faster                                                                 |
| deepcopy_memo            | 28.8 us                                                     | 19.4 us: 1.48x faster                                                                 |
| chaos                    | 61.7 ms                                                     | 42.2 ms: 1.46x faster                                                                 |
| richards                 | 42.4 ms                                                     | 29.2 ms: 1.45x faster                                                                 |
| raytrace                 | 273 ms                                                      | 194 ms: 1.41x faster                                                                  |
| scimark_lu               | 85.8 ms                                                     | 61.0 ms: 1.41x faster                                                                 |
| comprehensions           | 16.5 us                                                     | 11.8 us: 1.39x faster                                                                 |
| deepcopy                 | 255 us                                                      | 184 us: 1.39x faster                                                                  |
| spectral_norm            | 77.3 ms                                                     | 56.5 ms: 1.37x faster                                                                 |
| sqlglot_parse            | 1.22 ms                                                     | 891 us: 1.36x faster                                                                  |
| scimark_sor              | 106 ms                                                      | 77.9 ms: 1.36x faster                                                                 |
| pyflate                  | 409 ms                                                      | 306 ms: 1.34x faster                                                                  |
| scimark_monte_carlo      | 57.3 ms                                                     | 43.1 ms: 1.33x faster                                                                 |
| sqlglot_transpile        | 1.48 ms                                                     | 1.12 ms: 1.32x faster                                                                 |
| json_dumps               | 9.16 ms                                                     | 6.95 ms: 1.32x faster                                                                 |
| hexiom                   | 5.74 ms                                                     | 4.36 ms: 1.32x faster                                                                 |
| float                    | 61.7 ms                                                     | 47.0 ms: 1.31x faster                                                                 |
| mako                     | 9.03 ms                                                     | 7.04 ms: 1.28x faster                                                                 |
| crypto_pyaes             | 62.5 ms                                                     | 49.5 ms: 1.26x faster                                                                 |
| pycparser                | 930 ms                                                      | 745 ms: 1.25x faster                                                                  |
| unpickle_pure_python     | 183 us                                                      | 148 us: 1.24x faster                                                                  |
| html5lib                 | 51.0 ms                                                     | 41.3 ms: 1.24x faster                                                                 |
| regex_compile            | 106 ms                                                      | 86.2 ms: 1.23x faster                                                                 |
| sqlite_synth             | 1.91 us                                                     | 1.58 us: 1.21x faster                                                                 |
| regex_dna                | 136 ms                                                      | 114 ms: 1.20x faster                                                                  |
| pickle_pure_python       | 270 us                                                      | 227 us: 1.19x faster                                                                  |
| thrift                   | 617 us                                                      | 522 us: 1.18x faster                                                                  |
| sympy_sum                | 107 ms                                                      | 90.7 ms: 1.18x faster                                                                 |
| tomli_loads              | 1.67 sec                                                    | 1.42 sec: 1.18x faster                                                                |
| coroutines               | 16.0 ms                                                     | 13.6 ms: 1.18x faster                                                                 |
| genshi_text              | 19.8 ms                                                     | 16.9 ms: 1.17x faster                                                                 |
| regex_effbot             | 1.66 ms                                                     | 1.42 ms: 1.16x faster                                                                 |
| dulwich_log              | 50.5 ms                                                     | 43.5 ms: 1.16x faster                                                                 |
| sympy_integrate          | 15.3 ms                                                     | 13.4 ms: 1.14x faster                                                                 |
| docutils                 | 1.92 sec                                                    | 1.69 sec: 1.13x faster                                                                |
| deepcopy_reduce          | 2.20 us                                                     | 1.97 us: 1.12x faster                                                                 |
| sqlglot_optimize         | 39.8 ms                                                     | 35.6 ms: 1.12x faster                                                                 |
| mdp                      | 1.78 sec                                                    | 1.61 sec: 1.11x faster                                                                |
| genshi_xml               | 41.0 ms                                                     | 37.1 ms: 1.11x faster                                                                 |
| django_template          | 28.9 ms                                                     | 26.2 ms: 1.10x faster                                                                 |
| pprint_pformat           | 1.22 sec                                                    | 1.11 sec: 1.10x faster                                                                |
| sympy_str                | 194 ms                                                      | 178 ms: 1.10x faster                                                                  |
| bench_thread_pool        | 958 us                                                      | 876 us: 1.09x faster                                                                  |
| pprint_safe_repr         | 592 ms                                                      | 548 ms: 1.08x faster                                                                  |
| nbody                    | 71.3 ms                                                     | 66.2 ms: 1.08x faster                                                                 |
| 2to3                     | 246 ms                                                      | 228 ms: 1.08x faster                                                                  |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.55 ms: 1.07x faster                                                                 |
| xml_etree_process        | 44.5 ms                                                     | 41.7 ms: 1.07x faster                                                                 |
| regex_v8                 | 15.4 ms                                                     | 14.6 ms: 1.06x faster                                                                 |
| xml_etree_parse          | 96.8 ms                                                     | 91.9 ms: 1.05x faster                                                                 |
| sqlglot_normalize        | 205 ms                                                      | 196 ms: 1.05x faster                                                                  |
| json                     | 3.14 ms                                                     | 3.01 ms: 1.04x faster                                                                 |
| scimark_fft              | 187 ms                                                      | 180 ms: 1.04x faster                                                                  |
| sympy_expand             | 314 ms                                                      | 306 ms: 1.03x faster                                                                  |
| nqueens                  | 66.6 ms                                                     | 65.5 ms: 1.02x faster                                                                 |
| meteor_contest           | 75.9 ms                                                     | 75.6 ms: 1.00x faster                                                                 |
| xml_etree_iterparse      | 65.0 ms                                                     | 66.1 ms: 1.02x slower                                                                 |
| pidigits                 | 149 ms                                                      | 152 ms: 1.02x slower                                                                  |
| async_generators         | 222 ms                                                      | 228 ms: 1.03x slower                                                                  |
| logging_format           | 6.76 us                                                     | 7.06 us: 1.04x slower                                                                 |
| logging_simple           | 6.22 us                                                     | 6.52 us: 1.05x slower                                                                 |
| xml_etree_generate       | 55.5 ms                                                     | 58.3 ms: 1.05x slower                                                                 |
| fannkuch                 | 256 ms                                                      | 274 ms: 1.07x slower                                                                  |
| json_loads               | 14.0 us                                                     | 15.1 us: 1.07x slower                                                                 |
| coverage                 | 39.0 ms                                                     | 47.2 ms: 1.21x slower                                                                 |
| telco                    | 3.94 ms                                                     | 4.96 ms: 1.26x slower                                                                 |
| python_startup_no_site   | 15.5 ms                                                     | 19.7 ms: 1.27x slower                                                                 |
| python_startup           | 20.6 ms                                                     | 26.1 ms: 1.27x slower                                                                 |
| bench_mp_pool            | 62.0 ms                                                     | 87.7 ms: 1.41x slower                                                                 |
| gc_traversal             | 1.41 ms                                                     | 2.04 ms: 1.45x slower                                                                 |
| create_gc_cycles         | 800 us                                                      | 1.25 ms: 1.56x slower                                                                 |
| Geometric mean           | (ref)                                                       | 1.21x faster                                                                          |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250307-3.14.0a5+-916faf4/bm-20250307-pythonperf1-amd64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.219x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown