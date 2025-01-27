# Results vs. 3.10.4

- fork: faster-cpython
- ref: remove_most_conditio
- machine: linux-x86_64
- commit hash: 1e0f842
- commit date: 2025-01-24
- overall geometric mean: 1.186x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: 1.54x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 336 ms: 1.04x faster                                                                   |
| docutils       | 3.41 sec                                                     | 2.99 sec: 1.14x faster                                                                 |
| html5lib       | 94.6 ms                                                      | 74.2 ms: 1.28x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.15x faster                                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|-------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 616 ms: 2.60x faster                                                                   |
| async_tree_none         | 692 ms                                                       | 295 ms: 2.34x faster                                                                   |
| async_tree_memoization  | 819 ms                                                       | 364 ms: 2.25x faster                                                                   |
| async_tree_cpu_io_mixed | 936 ms                                                       | 532 ms: 1.76x faster                                                                   |
| Geometric mean          | (ref)                                                        | 2.22x faster                                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 75.0 ms: 1.48x faster                                                                  |
| pidigits       | 271 ms                                                       | 249 ms: 1.09x faster                                                                   |
| nbody          | 134 ms                                                       | 138 ms: 1.03x slower                                                                   |
| Geometric mean | (ref)                                                        | 1.16x faster                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 156 ms: 1.22x faster                                                                   |
| regex_dna      | 261 ms                                                       | 241 ms: 1.08x faster                                                                   |
| regex_v8       | 27.2 ms                                                      | 25.3 ms: 1.08x faster                                                                  |
| regex_effbot   | 3.09 ms                                                      | 3.16 ms: 1.02x slower                                                                  |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 242 us: 1.29x faster                                                                   |
| xml_etree_iterparse  | 110 ms                                                       | 89.3 ms: 1.24x faster                                                                  |
| tomli_loads          | 2.92 sec                                                     | 2.41 sec: 1.21x faster                                                                 |
| pickle_pure_python   | 455 us                                                       | 380 us: 1.20x faster                                                                   |
| xml_etree_parse      | 160 ms                                                       | 137 ms: 1.17x faster                                                                   |
| json_loads           | 30.3 us                                                      | 27.7 us: 1.09x faster                                                                  |
| json_dumps           | 14.5 ms                                                      | 13.5 ms: 1.08x faster                                                                  |
| xml_etree_process    | 75.9 ms                                                      | 72.4 ms: 1.05x faster                                                                  |
| xml_etree_generate   | 92.3 ms                                                      | 100 ms: 1.09x slower                                                                   |
| Geometric mean       | (ref)                                                        | 1.13x faster                                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 11.8 ms: 1.60x slower                                                                  |
| python_startup         | 11.5 ms                                                      | 18.6 ms: 1.62x slower                                                                  |
| Geometric mean         | (ref)                                                        | 1.61x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| genshi_text     | 31.4 ms                                                      | 29.0 ms: 1.08x faster                                                                  |
| django_template | 50.2 ms                                                      | 47.2 ms: 1.06x faster                                                                  |
| genshi_xml      | 63.3 ms                                                      | 62.4 ms: 1.01x faster                                                                  |
| mako            | 14.7 ms                                                      | 18.0 ms: 1.22x slower                                                                  |
| Geometric mean  | (ref)                                                        | 1.01x slower                                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|--------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_io            | 1.60 sec                                                     | 616 ms: 2.60x faster                                                                   |
| typing_runtime_protocols | 537 us                                                       | 221 us: 2.43x faster                                                                   |
| async_tree_none          | 692 ms                                                       | 295 ms: 2.34x faster                                                                   |
| async_tree_memoization   | 819 ms                                                       | 364 ms: 2.25x faster                                                                   |
| generators               | 57.3 ms                                                      | 31.1 ms: 1.84x faster                                                                  |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 532 ms: 1.76x faster                                                                   |
| go                       | 262 ms                                                       | 151 ms: 1.73x faster                                                                   |
| deltablue                | 7.50 ms                                                      | 4.51 ms: 1.66x faster                                                                  |
| logging_silent           | 167 ns                                                       | 103 ns: 1.63x faster                                                                   |
| pylint                   | 566 ms                                                       | 355 ms: 1.60x faster                                                                   |
| chaos                    | 109 ms                                                       | 71.3 ms: 1.52x faster                                                                  |
| scimark_sor              | 180 ms                                                       | 121 ms: 1.49x faster                                                                   |
| float                    | 111 ms                                                       | 75.0 ms: 1.48x faster                                                                  |
| pyflate                  | 733 ms                                                       | 496 ms: 1.48x faster                                                                   |
| raytrace                 | 489 ms                                                       | 342 ms: 1.43x faster                                                                   |
| scimark_lu               | 167 ms                                                       | 120 ms: 1.39x faster                                                                   |
| coroutines               | 30.3 ms                                                      | 21.8 ms: 1.39x faster                                                                  |
| sqlglot_parse            | 2.24 ms                                                      | 1.62 ms: 1.38x faster                                                                  |
| deepcopy                 | 468 us                                                       | 341 us: 1.37x faster                                                                   |
| spectral_norm            | 139 ms                                                       | 102 ms: 1.37x faster                                                                   |
| richards_super           | 90.6 ms                                                      | 67.3 ms: 1.35x faster                                                                  |
| deepcopy_memo            | 49.8 us                                                      | 37.4 us: 1.33x faster                                                                  |
| pathlib                  | 21.4 ms                                                      | 16.3 ms: 1.31x faster                                                                  |
| hexiom                   | 9.42 ms                                                      | 7.21 ms: 1.31x faster                                                                  |
| pycparser                | 1.67 sec                                                     | 1.29 sec: 1.30x faster                                                                 |
| unpickle_pure_python     | 312 us                                                       | 242 us: 1.29x faster                                                                   |
| richards                 | 75.1 ms                                                      | 58.5 ms: 1.28x faster                                                                  |
| crypto_pyaes             | 119 ms                                                       | 92.9 ms: 1.28x faster                                                                  |
| sqlglot_transpile        | 2.68 ms                                                      | 2.09 ms: 1.28x faster                                                                  |
| html5lib                 | 94.6 ms                                                      | 74.2 ms: 1.28x faster                                                                  |
| comprehensions           | 26.7 us                                                      | 21.2 us: 1.26x faster                                                                  |
| logging_simple           | 8.88 us                                                      | 7.16 us: 1.24x faster                                                                  |
| xml_etree_iterparse      | 110 ms                                                       | 89.3 ms: 1.24x faster                                                                  |
| scimark_monte_carlo      | 107 ms                                                       | 87.9 ms: 1.22x faster                                                                  |
| regex_compile            | 190 ms                                                       | 156 ms: 1.22x faster                                                                   |
| logging_format           | 9.64 us                                                      | 7.95 us: 1.21x faster                                                                  |
| tomli_loads              | 2.92 sec                                                     | 2.41 sec: 1.21x faster                                                                 |
| pickle_pure_python       | 455 us                                                       | 380 us: 1.20x faster                                                                   |
| xml_etree_parse          | 160 ms                                                       | 137 ms: 1.17x faster                                                                   |
| pprint_safe_repr         | 1.05 sec                                                     | 900 ms: 1.17x faster                                                                   |
| dulwich_log              | 81.1 ms                                                      | 70.0 ms: 1.16x faster                                                                  |
| pprint_pformat           | 2.15 sec                                                     | 1.86 sec: 1.16x faster                                                                 |
| sqlite_synth             | 2.99 us                                                      | 2.59 us: 1.15x faster                                                                  |
| docutils                 | 3.41 sec                                                     | 2.99 sec: 1.14x faster                                                                 |
| thrift                   | 1.18 ms                                                      | 1.04 ms: 1.13x faster                                                                  |
| sqlglot_normalize        | 144 ms                                                       | 131 ms: 1.10x faster                                                                   |
| deepcopy_reduce          | 4.01 us                                                      | 3.65 us: 1.10x faster                                                                  |
| sqlalchemy_imperative    | 22.7 ms                                                      | 20.7 ms: 1.10x faster                                                                  |
| json_loads               | 30.3 us                                                      | 27.7 us: 1.09x faster                                                                  |
| sympy_sum                | 193 ms                                                       | 177 ms: 1.09x faster                                                                   |
| pidigits                 | 271 ms                                                       | 249 ms: 1.09x faster                                                                   |
| regex_dna                | 261 ms                                                       | 241 ms: 1.08x faster                                                                   |
| genshi_text              | 31.4 ms                                                      | 29.0 ms: 1.08x faster                                                                  |
| mdp                      | 3.01 sec                                                     | 2.77 sec: 1.08x faster                                                                 |
| json_dumps               | 14.5 ms                                                      | 13.5 ms: 1.08x faster                                                                  |
| regex_v8                 | 27.2 ms                                                      | 25.3 ms: 1.08x faster                                                                  |
| sqlalchemy_declarative   | 190 ms                                                       | 177 ms: 1.07x faster                                                                   |
| sqlglot_optimize         | 70.1 ms                                                      | 65.9 ms: 1.06x faster                                                                  |
| django_template          | 50.2 ms                                                      | 47.2 ms: 1.06x faster                                                                  |
| json                     | 5.86 ms                                                      | 5.54 ms: 1.06x faster                                                                  |
| sympy_str                | 360 ms                                                       | 341 ms: 1.06x faster                                                                   |
| xml_etree_process        | 75.9 ms                                                      | 72.4 ms: 1.05x faster                                                                  |
| sympy_expand             | 600 ms                                                       | 575 ms: 1.04x faster                                                                   |
| 2to3                     | 350 ms                                                       | 336 ms: 1.04x faster                                                                   |
| scimark_fft              | 361 ms                                                       | 347 ms: 1.04x faster                                                                   |
| sympy_integrate          | 28.2 ms                                                      | 27.2 ms: 1.03x faster                                                                  |
| nqueens                  | 115 ms                                                       | 111 ms: 1.03x faster                                                                   |
| asyncio_websockets       | 390 ms                                                       | 380 ms: 1.03x faster                                                                   |
| fannkuch                 | 483 ms                                                       | 475 ms: 1.02x faster                                                                   |
| genshi_xml               | 63.3 ms                                                      | 62.4 ms: 1.01x faster                                                                  |
| regex_effbot             | 3.09 ms                                                      | 3.16 ms: 1.02x slower                                                                  |
| nbody                    | 134 ms                                                       | 138 ms: 1.03x slower                                                                   |
| xml_etree_generate       | 92.3 ms                                                      | 100 ms: 1.09x slower                                                                   |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 5.66 ms: 1.11x slower                                                                  |
| async_generators         | 421 ms                                                       | 469 ms: 1.12x slower                                                                   |
| meteor_contest           | 138 ms                                                       | 155 ms: 1.12x slower                                                                   |
| create_gc_cycles         | 1.76 ms                                                      | 2.02 ms: 1.15x slower                                                                  |
| gc_traversal             | 3.42 ms                                                      | 4.05 ms: 1.19x slower                                                                  |
| mako                     | 14.7 ms                                                      | 18.0 ms: 1.22x slower                                                                  |
| telco                    | 7.23 ms                                                      | 9.13 ms: 1.26x slower                                                                  |
| bench_thread_pool        | 1.14 ms                                                      | 1.47 ms: 1.28x slower                                                                  |
| coverage                 | 63.3 ms                                                      | 100 ms: 1.59x slower                                                                   |
| python_startup_no_site   | 7.33 ms                                                      | 11.8 ms: 1.60x slower                                                                  |
| python_startup           | 11.5 ms                                                      | 18.6 ms: 1.62x slower                                                                  |
| bench_mp_pool            | 6.37 ms                                                      | 48.8 ms: 7.66x slower                                                                  |
| Geometric mean           | (ref)                                                        | 1.15x faster                                                                           |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250124-3.14.0a4+-1e0f842-NOGIL/bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.186x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: 1.54x