# Results vs. 3.10.4

- fork: python
- ref: 79b7cab50a3292a1c014
- machine: windows-amd64
- commit hash: 79b7cab
- commit date: 2024-12-07
- overall geometric mean: 1.256x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 217 ms: 1.13x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.71 sec: 1.12x faster                                                      |
| html5lib       | 51.0 ms                                                     | 38.6 ms: 1.32x faster                                                       |
| Geometric mean | (ref)                                                       | 1.19x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 396 ms: 2.80x faster                                                        |
| async_tree_none         | 435 ms                                                      | 182 ms: 2.39x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 221 ms: 2.39x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 359 ms: 1.78x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.31x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 53.5 ms: 1.33x faster                                                       |
| float          | 61.7 ms                                                     | 48.8 ms: 1.26x faster                                                       |
| pidigits       | 149 ms                                                      | 146 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                       | 1.20x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 81.3 ms: 1.30x faster                                                       |
| regex_dna      | 136 ms                                                      | 114 ms: 1.19x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.43 ms: 1.16x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 18.4 ms: 1.19x slower                                                       |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 111 us: 1.66x faster                                                        |
| json_dumps           | 9.16 ms                                                     | 6.50 ms: 1.41x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 203 us: 1.33x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.30 sec: 1.29x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 35.3 ms: 1.26x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 84.4 ms: 1.15x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 57.5 ms: 1.13x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 50.4 ms: 1.10x faster                                                       |
| json_loads           | 14.0 us                                                     | 14.5 us: 1.04x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.24x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 23.5 ms: 1.14x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 17.8 ms: 1.15x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.15x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.17 ms: 1.75x faster                                                       |
| django_template | 28.9 ms                                                     | 26.1 ms: 1.11x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 18.1 ms: 1.10x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 45.9 ms: 1.12x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.17x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 111 us: 3.02x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 396 ms: 2.80x faster                                                        |
| async_tree_none          | 435 ms                                                      | 182 ms: 2.39x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 221 ms: 2.39x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.29 ms: 1.82x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 359 ms: 1.78x faster                                                        |
| pylint                   | 350 ms                                                      | 199 ms: 1.76x faster                                                        |
| mako                     | 9.03 ms                                                     | 5.17 ms: 1.75x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 16.7 us: 1.73x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 56.4 ns: 1.68x faster                                                       |
| scimark_sor              | 106 ms                                                      | 64.1 ms: 1.66x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 111 us: 1.66x faster                                                        |
| scimark_lu               | 85.8 ms                                                     | 54.1 ms: 1.59x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 36.2 ms: 1.58x faster                                                       |
| go                       | 139 ms                                                      | 89.7 ms: 1.55x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 41.1 ms: 1.52x faster                                                       |
| chaos                    | 61.7 ms                                                     | 40.8 ms: 1.51x faster                                                       |
| pyflate                  | 409 ms                                                      | 287 ms: 1.42x faster                                                        |
| spectral_norm            | 77.3 ms                                                     | 54.7 ms: 1.41x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.7 us: 1.41x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.50 ms: 1.41x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 864 us: 1.41x faster                                                        |
| generators               | 32.4 ms                                                     | 23.7 ms: 1.36x faster                                                       |
| pycparser                | 930 ms                                                      | 690 ms: 1.35x faster                                                        |
| sqlglot_transpile        | 1.48 ms                                                     | 1.10 ms: 1.34x faster                                                       |
| raytrace                 | 273 ms                                                      | 204 ms: 1.34x faster                                                        |
| deepcopy                 | 255 us                                                      | 191 us: 1.34x faster                                                        |
| nbody                    | 71.3 ms                                                     | 53.5 ms: 1.33x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 203 us: 1.33x faster                                                        |
| richards_super           | 52.2 ms                                                     | 39.4 ms: 1.32x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 38.6 ms: 1.32x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 933 ms: 1.31x faster                                                        |
| regex_compile            | 106 ms                                                      | 81.3 ms: 1.30x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.30 sec: 1.29x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 462 ms: 1.28x faster                                                        |
| float                    | 61.7 ms                                                     | 48.8 ms: 1.26x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 35.3 ms: 1.26x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 40.7 ms: 1.24x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.21 ms: 1.23x faster                                                       |
| scimark_fft              | 187 ms                                                      | 153 ms: 1.23x faster                                                        |
| sqlite_synth             | 1.91 us                                                     | 1.57 us: 1.22x faster                                                       |
| richards                 | 42.4 ms                                                     | 35.2 ms: 1.21x faster                                                       |
| thrift                   | 617 us                                                      | 517 us: 1.20x faster                                                        |
| regex_dna                | 136 ms                                                      | 114 ms: 1.19x faster                                                        |
| coroutines               | 16.0 ms                                                     | 13.5 ms: 1.18x faster                                                       |
| sympy_sum                | 107 ms                                                      | 90.7 ms: 1.18x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 815 us: 1.18x faster                                                        |
| deepcopy_reduce          | 2.20 us                                                     | 1.88 us: 1.17x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.43 ms: 1.16x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.95 ms: 1.16x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 84.4 ms: 1.15x faster                                                       |
| 2to3                     | 246 ms                                                      | 217 ms: 1.13x faster                                                        |
| sympy_integrate          | 15.3 ms                                                     | 13.5 ms: 1.13x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 57.5 ms: 1.13x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.71 sec: 1.12x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.59 sec: 1.12x faster                                                      |
| django_template          | 28.9 ms                                                     | 26.1 ms: 1.11x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 50.4 ms: 1.10x faster                                                       |
| sympy_str                | 194 ms                                                      | 177 ms: 1.10x faster                                                        |
| genshi_text              | 19.8 ms                                                     | 18.1 ms: 1.10x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 62.6 ms: 1.06x faster                                                       |
| fannkuch                 | 256 ms                                                      | 240 ms: 1.06x faster                                                        |
| meteor_contest           | 75.9 ms                                                     | 72.6 ms: 1.05x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 38.3 ms: 1.04x faster                                                       |
| sympy_expand             | 314 ms                                                      | 303 ms: 1.04x faster                                                        |
| pidigits                 | 149 ms                                                      | 146 ms: 1.02x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 74.3 ms: 1.02x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.66 us: 1.01x faster                                                       |
| logging_simple           | 6.22 us                                                     | 6.27 us: 1.01x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.5 us: 1.04x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.34 ms: 1.10x slower                                                       |
| genshi_xml               | 41.0 ms                                                     | 45.9 ms: 1.12x slower                                                       |
| python_startup           | 20.6 ms                                                     | 23.5 ms: 1.14x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 17.8 ms: 1.15x slower                                                       |
| async_generators         | 222 ms                                                      | 262 ms: 1.18x slower                                                        |
| regex_v8                 | 15.4 ms                                                     | 18.4 ms: 1.19x slower                                                       |
| coverage                 | 39.0 ms                                                     | 46.8 ms: 1.20x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 81.8 ms: 1.32x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.90 ms: 1.35x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.09 ms: 1.36x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.25x faster                                                                |

Benchmark hidden because not significant (2): json, sqlglot_normalize
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241207-3.14.0a2+-79b7cab-JIT/bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.256x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: unknown