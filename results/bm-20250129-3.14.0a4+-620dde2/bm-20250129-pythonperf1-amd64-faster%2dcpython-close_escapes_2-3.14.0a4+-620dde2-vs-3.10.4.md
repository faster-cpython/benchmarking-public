# Results vs. 3.10.4

- fork: faster-cpython
- ref: close_escapes_2
- machine: windows-amd64
- commit hash: 620dde2
- commit date: 2025-01-29
- overall geometric mean: 1.172x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 233 ms: 1.05x faster                                                             |
| docutils       | 1.92 sec                                                    | 1.69 sec: 1.13x faster                                                           |
| html5lib       | 51.0 ms                                                     | 39.8 ms: 1.28x faster                                                            |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 431 ms: 2.57x faster                                                             |
| async_tree_memoization  | 526 ms                                                      | 228 ms: 2.31x faster                                                             |
| async_tree_none         | 435 ms                                                      | 193 ms: 2.26x faster                                                             |
| async_tree_cpu_io_mixed | 638 ms                                                      | 349 ms: 1.83x faster                                                             |
| Geometric mean          | (ref)                                                       | 2.22x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 52.6 ms: 1.17x faster                                                            |
| pidigits       | 149 ms                                                      | 147 ms: 1.02x faster                                                             |
| nbody          | 71.3 ms                                                     | 77.1 ms: 1.08x slower                                                            |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 114 ms: 1.19x faster                                                             |
| regex_compile  | 106 ms                                                      | 89.5 ms: 1.18x faster                                                            |
| regex_effbot   | 1.66 ms                                                     | 1.43 ms: 1.16x faster                                                            |
| Geometric mean | (ref)                                                       | 1.13x faster                                                                     |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.81 ms: 1.35x faster                                                            |
| tomli_loads          | 1.67 sec                                                    | 1.44 sec: 1.16x faster                                                           |
| pickle_pure_python   | 270 us                                                      | 238 us: 1.13x faster                                                             |
| unpickle_pure_python | 183 us                                                      | 164 us: 1.12x faster                                                             |
| xml_etree_parse      | 96.8 ms                                                     | 87.5 ms: 1.11x faster                                                            |
| xml_etree_process    | 44.5 ms                                                     | 41.3 ms: 1.08x faster                                                            |
| xml_etree_generate   | 55.5 ms                                                     | 58.6 ms: 1.06x slower                                                            |
| json_loads           | 14.0 us                                                     | 15.4 us: 1.10x slower                                                            |
| Geometric mean       | (ref)                                                       | 1.08x faster                                                                     |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 18.0 ms: 1.16x slower                                                            |
| python_startup         | 20.6 ms                                                     | 24.3 ms: 1.18x slower                                                            |
| Geometric mean         | (ref)                                                       | 1.17x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.88 ms: 1.31x faster                                                            |
| genshi_text     | 19.8 ms                                                     | 16.3 ms: 1.21x faster                                                            |
| genshi_xml      | 41.0 ms                                                     | 36.0 ms: 1.14x faster                                                            |
| django_template | 28.9 ms                                                     | 25.6 ms: 1.13x faster                                                            |
| Geometric mean  | (ref)                                                       | 1.20x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 116 us: 2.90x faster                                                             |
| async_tree_io            | 1.11 sec                                                    | 431 ms: 2.57x faster                                                             |
| async_tree_memoization   | 526 ms                                                      | 228 ms: 2.31x faster                                                             |
| async_tree_none          | 435 ms                                                      | 193 ms: 2.26x faster                                                             |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 349 ms: 1.83x faster                                                             |
| deltablue                | 4.19 ms                                                     | 2.38 ms: 1.76x faster                                                            |
| pylint                   | 350 ms                                                      | 203 ms: 1.73x faster                                                             |
| go                       | 139 ms                                                      | 92.0 ms: 1.51x faster                                                            |
| generators               | 32.4 ms                                                     | 21.6 ms: 1.50x faster                                                            |
| chaos                    | 61.7 ms                                                     | 43.4 ms: 1.42x faster                                                            |
| richards_super           | 52.2 ms                                                     | 37.0 ms: 1.41x faster                                                            |
| logging_silent           | 94.6 ns                                                     | 69.1 ns: 1.37x faster                                                            |
| deepcopy                 | 255 us                                                      | 187 us: 1.36x faster                                                             |
| sqlglot_parse            | 1.22 ms                                                     | 901 us: 1.35x faster                                                             |
| deepcopy_memo            | 28.8 us                                                     | 21.4 us: 1.35x faster                                                            |
| json_dumps               | 9.16 ms                                                     | 6.81 ms: 1.35x faster                                                            |
| raytrace                 | 273 ms                                                      | 203 ms: 1.34x faster                                                             |
| sqlglot_transpile        | 1.48 ms                                                     | 1.12 ms: 1.32x faster                                                            |
| mako                     | 9.03 ms                                                     | 6.88 ms: 1.31x faster                                                            |
| pyflate                  | 409 ms                                                      | 314 ms: 1.30x faster                                                             |
| richards                 | 42.4 ms                                                     | 32.8 ms: 1.30x faster                                                            |
| html5lib                 | 51.0 ms                                                     | 39.8 ms: 1.28x faster                                                            |
| comprehensions           | 16.5 us                                                     | 12.9 us: 1.28x faster                                                            |
| crypto_pyaes             | 62.5 ms                                                     | 49.5 ms: 1.26x faster                                                            |
| pycparser                | 930 ms                                                      | 750 ms: 1.24x faster                                                             |
| scimark_lu               | 85.8 ms                                                     | 70.1 ms: 1.22x faster                                                            |
| hexiom                   | 5.74 ms                                                     | 4.70 ms: 1.22x faster                                                            |
| genshi_text              | 19.8 ms                                                     | 16.3 ms: 1.21x faster                                                            |
| regex_dna                | 136 ms                                                      | 114 ms: 1.19x faster                                                             |
| thrift                   | 617 us                                                      | 519 us: 1.19x faster                                                             |
| regex_compile            | 106 ms                                                      | 89.5 ms: 1.18x faster                                                            |
| sqlite_synth             | 1.91 us                                                     | 1.62 us: 1.18x faster                                                            |
| sympy_sum                | 107 ms                                                      | 90.6 ms: 1.18x faster                                                            |
| float                    | 61.7 ms                                                     | 52.6 ms: 1.17x faster                                                            |
| dulwich_log              | 50.5 ms                                                     | 43.3 ms: 1.17x faster                                                            |
| spectral_norm            | 77.3 ms                                                     | 66.3 ms: 1.17x faster                                                            |
| deepcopy_reduce          | 2.20 us                                                     | 1.90 us: 1.16x faster                                                            |
| tomli_loads              | 1.67 sec                                                    | 1.44 sec: 1.16x faster                                                           |
| regex_effbot             | 1.66 ms                                                     | 1.43 ms: 1.16x faster                                                            |
| scimark_monte_carlo      | 57.3 ms                                                     | 49.7 ms: 1.15x faster                                                            |
| genshi_xml               | 41.0 ms                                                     | 36.0 ms: 1.14x faster                                                            |
| pickle_pure_python       | 270 us                                                      | 238 us: 1.13x faster                                                             |
| docutils                 | 1.92 sec                                                    | 1.69 sec: 1.13x faster                                                           |
| django_template          | 28.9 ms                                                     | 25.6 ms: 1.13x faster                                                            |
| bench_thread_pool        | 958 us                                                      | 854 us: 1.12x faster                                                             |
| unpickle_pure_python     | 183 us                                                      | 164 us: 1.12x faster                                                             |
| sympy_integrate          | 15.3 ms                                                     | 13.7 ms: 1.12x faster                                                            |
| scimark_sor              | 106 ms                                                      | 95.4 ms: 1.11x faster                                                            |
| xml_etree_parse          | 96.8 ms                                                     | 87.5 ms: 1.11x faster                                                            |
| mdp                      | 1.78 sec                                                    | 1.62 sec: 1.10x faster                                                           |
| pprint_pformat           | 1.22 sec                                                    | 1.12 sec: 1.09x faster                                                           |
| sqlglot_optimize         | 39.8 ms                                                     | 36.6 ms: 1.09x faster                                                            |
| sympy_str                | 194 ms                                                      | 180 ms: 1.08x faster                                                             |
| xml_etree_process        | 44.5 ms                                                     | 41.3 ms: 1.08x faster                                                            |
| coroutines               | 16.0 ms                                                     | 15.0 ms: 1.07x faster                                                            |
| pprint_safe_repr         | 592 ms                                                      | 556 ms: 1.06x faster                                                             |
| 2to3                     | 246 ms                                                      | 233 ms: 1.05x faster                                                             |
| sympy_expand             | 314 ms                                                      | 306 ms: 1.03x faster                                                             |
| sqlglot_normalize        | 205 ms                                                      | 200 ms: 1.02x faster                                                             |
| pidigits                 | 149 ms                                                      | 147 ms: 1.02x faster                                                             |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.68 ms: 1.02x faster                                                            |
| nqueens                  | 66.6 ms                                                     | 66.2 ms: 1.01x faster                                                            |
| meteor_contest           | 75.9 ms                                                     | 76.2 ms: 1.00x slower                                                            |
| logging_simple           | 6.22 us                                                     | 6.29 us: 1.01x slower                                                            |
| json                     | 3.14 ms                                                     | 3.18 ms: 1.01x slower                                                            |
| async_generators         | 222 ms                                                      | 225 ms: 1.02x slower                                                             |
| pathlib                  | 75.7 ms                                                     | 77.8 ms: 1.03x slower                                                            |
| xml_etree_generate       | 55.5 ms                                                     | 58.6 ms: 1.06x slower                                                            |
| scimark_fft              | 187 ms                                                      | 199 ms: 1.06x slower                                                             |
| nbody                    | 71.3 ms                                                     | 77.1 ms: 1.08x slower                                                            |
| json_loads               | 14.0 us                                                     | 15.4 us: 1.10x slower                                                            |
| fannkuch                 | 256 ms                                                      | 286 ms: 1.12x slower                                                             |
| python_startup_no_site   | 15.5 ms                                                     | 18.0 ms: 1.16x slower                                                            |
| python_startup           | 20.6 ms                                                     | 24.3 ms: 1.18x slower                                                            |
| telco                    | 3.94 ms                                                     | 4.87 ms: 1.24x slower                                                            |
| coverage                 | 39.0 ms                                                     | 49.2 ms: 1.26x slower                                                            |
| gc_traversal             | 1.41 ms                                                     | 1.97 ms: 1.40x slower                                                            |
| bench_mp_pool            | 62.0 ms                                                     | 87.7 ms: 1.41x slower                                                            |
| create_gc_cycles         | 800 us                                                      | 1.22 ms: 1.52x slower                                                            |
| Geometric mean           | (ref)                                                       | 1.17x faster                                                                     |

Benchmark hidden because not significant (3): xml_etree_iterparse, logging_format, regex_v8
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250129-3.14.0a4+-620dde2/bm-20250129-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.172x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: unknown