# Results vs. 3.10.4

- fork: brandtbucher
- ref: keep_stack_pointer
- machine: linux-x86_64
- commit hash: b3d84fd
- commit date: 2025-03-26
- overall geometric mean: 1.437x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 258 ms: 1.35x faster                                                       |
| docutils       | 3.30 sec                                               | 2.63 sec: 1.25x faster                                                     |
| html5lib       | 88.9 ms                                                | 61.7 ms: 1.44x faster                                                      |
| Geometric mean | (ref)                                                  | 1.35x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 612 ms: 2.89x faster                                                       |
| async_tree_none         | 728 ms                                                 | 256 ms: 2.85x faster                                                       |
| async_tree_memoization  | 870 ms                                                 | 310 ms: 2.81x faster                                                       |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 485 ms: 2.10x faster                                                       |
| Geometric mean          | (ref)                                                  | 2.64x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 69.9 ms: 1.67x faster                                                      |
| nbody          | 154 ms                                                 | 97.6 ms: 1.57x faster                                                      |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                  | 1.39x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.49x faster                                                       |
| regex_v8       | 27.8 ms                                                | 23.8 ms: 1.16x faster                                                      |
| regex_effbot   | 3.63 ms                                                | 3.31 ms: 1.10x faster                                                      |
| regex_dna      | 227 ms                                                 | 225 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                  | 1.18x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.94 sec: 1.62x faster                                                     |
| pickle_pure_python   | 484 us                                                 | 314 us: 1.54x faster                                                       |
| unpickle_pure_python | 331 us                                                 | 217 us: 1.52x faster                                                       |
| xml_etree_process    | 79.1 ms                                                | 59.3 ms: 1.33x faster                                                      |
| json_dumps           | 14.2 ms                                                | 11.6 ms: 1.23x faster                                                      |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                                       |
| xml_etree_generate   | 99.4 ms                                                | 84.9 ms: 1.17x faster                                                      |
| xml_etree_iterparse  | 115 ms                                                 | 99.4 ms: 1.16x faster                                                      |
| json_loads           | 31.2 us                                                | 29.9 us: 1.04x faster                                                      |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.3 ms: 1.09x faster                                                      |
| python_startup_no_site | 5.93 ms                                                | 8.28 ms: 1.40x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.3 ms: 1.54x faster                                                      |
| genshi_text     | 31.8 ms                                                | 21.1 ms: 1.51x faster                                                      |
| mako            | 16.3 ms                                                | 11.2 ms: 1.46x faster                                                      |
| genshi_xml      | 66.0 ms                                                | 48.5 ms: 1.36x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.47x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 160 us: 3.41x faster                                                       |
| async_tree_io            | 1.77 sec                                               | 612 ms: 2.89x faster                                                       |
| async_tree_none          | 728 ms                                                 | 256 ms: 2.85x faster                                                       |
| generators               | 80.1 ms                                                | 28.4 ms: 2.82x faster                                                      |
| async_tree_memoization   | 870 ms                                                 | 310 ms: 2.81x faster                                                       |
| deltablue                | 7.91 ms                                                | 3.15 ms: 2.52x faster                                                      |
| go                       | 240 ms                                                 | 114 ms: 2.10x faster                                                       |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 485 ms: 2.10x faster                                                       |
| deepcopy_memo            | 58.5 us                                                | 29.0 us: 2.02x faster                                                      |
| chaos                    | 115 ms                                                 | 58.2 ms: 1.98x faster                                                      |
| pylint                   | 551 ms                                                 | 280 ms: 1.97x faster                                                       |
| logging_silent           | 190 ns                                                 | 97.5 ns: 1.95x faster                                                      |
| raytrace                 | 507 ms                                                 | 265 ms: 1.91x faster                                                       |
| richards_super           | 94.7 ms                                                | 50.6 ms: 1.87x faster                                                      |
| deepcopy                 | 479 us                                                 | 257 us: 1.87x faster                                                       |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.85x faster                                                       |
| richards                 | 79.3 ms                                                | 43.9 ms: 1.81x faster                                                      |
| scimark_monte_carlo      | 118 ms                                                 | 66.9 ms: 1.77x faster                                                      |
| crypto_pyaes             | 128 ms                                                 | 73.1 ms: 1.75x faster                                                      |
| spectral_norm            | 170 ms                                                 | 97.6 ms: 1.74x faster                                                      |
| comprehensions           | 28.8 us                                                | 17.0 us: 1.69x faster                                                      |
| float                    | 117 ms                                                 | 69.9 ms: 1.67x faster                                                      |
| hexiom                   | 10.4 ms                                                | 6.27 ms: 1.66x faster                                                      |
| tomli_loads              | 3.14 sec                                               | 1.94 sec: 1.62x faster                                                     |
| nbody                    | 154 ms                                                 | 97.6 ms: 1.57x faster                                                      |
| pyflate                  | 716 ms                                                 | 456 ms: 1.57x faster                                                       |
| deepcopy_reduce          | 4.17 us                                                | 2.69 us: 1.55x faster                                                      |
| pickle_pure_python       | 484 us                                                 | 314 us: 1.54x faster                                                       |
| django_template          | 48.2 ms                                                | 31.3 ms: 1.54x faster                                                      |
| scimark_lu               | 176 ms                                                 | 115 ms: 1.53x faster                                                       |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.52x faster                                                       |
| genshi_text              | 31.8 ms                                                | 21.1 ms: 1.51x faster                                                      |
| logging_simple           | 8.30 us                                                | 5.50 us: 1.51x faster                                                      |
| coroutines               | 35.1 ms                                                | 23.3 ms: 1.51x faster                                                      |
| regex_compile            | 188 ms                                                 | 127 ms: 1.49x faster                                                       |
| logging_format           | 9.09 us                                                | 6.19 us: 1.47x faster                                                      |
| mako                     | 16.3 ms                                                | 11.2 ms: 1.46x faster                                                      |
| html5lib                 | 88.9 ms                                                | 61.7 ms: 1.44x faster                                                      |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.42x faster                                                     |
| pprint_safe_repr         | 1.02 sec                                               | 723 ms: 1.41x faster                                                       |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.39x faster                                                     |
| thrift                   | 1.07 ms                                                | 779 us: 1.38x faster                                                       |
| genshi_xml               | 66.0 ms                                                | 48.5 ms: 1.36x faster                                                      |
| dulwich_log              | 84.3 ms                                                | 62.3 ms: 1.35x faster                                                      |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.78 ms: 1.35x faster                                                      |
| 2to3                     | 348 ms                                                 | 258 ms: 1.35x faster                                                       |
| xml_etree_process        | 79.1 ms                                                | 59.3 ms: 1.33x faster                                                      |
| scimark_fft              | 466 ms                                                 | 349 ms: 1.33x faster                                                       |
| sqlalchemy_declarative   | 172 ms                                                 | 132 ms: 1.30x faster                                                       |
| sympy_integrate          | 25.8 ms                                                | 20.0 ms: 1.29x faster                                                      |
| nqueens                  | 106 ms                                                 | 82.3 ms: 1.29x faster                                                      |
| sympy_str                | 346 ms                                                 | 272 ms: 1.27x faster                                                       |
| sqlalchemy_imperative    | 23.3 ms                                                | 18.4 ms: 1.27x faster                                                      |
| sympy_sum                | 196 ms                                                 | 155 ms: 1.27x faster                                                       |
| docutils                 | 3.30 sec                                               | 2.63 sec: 1.25x faster                                                     |
| fannkuch                 | 532 ms                                                 | 425 ms: 1.25x faster                                                       |
| sympy_expand             | 566 ms                                                 | 459 ms: 1.23x faster                                                       |
| pathlib                  | 20.5 ms                                                | 16.7 ms: 1.23x faster                                                      |
| json_dumps               | 14.2 ms                                                | 11.6 ms: 1.23x faster                                                      |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                                       |
| xml_etree_generate       | 99.4 ms                                                | 84.9 ms: 1.17x faster                                                      |
| regex_v8                 | 27.8 ms                                                | 23.8 ms: 1.16x faster                                                      |
| xml_etree_iterparse      | 115 ms                                                 | 99.4 ms: 1.16x faster                                                      |
| mdp                      | 2.85 sec                                               | 2.50 sec: 1.14x faster                                                     |
| async_generators         | 444 ms                                                 | 395 ms: 1.12x faster                                                       |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.11x faster                                                       |
| bench_thread_pool        | 986 us                                                 | 889 us: 1.11x faster                                                       |
| regex_effbot             | 3.63 ms                                                | 3.31 ms: 1.10x faster                                                      |
| python_startup           | 14.6 ms                                                | 13.3 ms: 1.09x faster                                                      |
| sqlite_synth             | 3.02 us                                                | 2.81 us: 1.08x faster                                                      |
| json                     | 5.69 ms                                                | 5.30 ms: 1.07x faster                                                      |
| json_loads               | 31.2 us                                                | 29.9 us: 1.04x faster                                                      |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                       |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                       |
| regex_dna                | 227 ms                                                 | 225 ms: 1.01x faster                                                       |
| telco                    | 7.27 ms                                                | 7.81 ms: 1.07x slower                                                      |
| coverage                 | 79.4 ms                                                | 92.6 ms: 1.17x slower                                                      |
| gc_traversal             | 3.62 ms                                                | 4.79 ms: 1.32x slower                                                      |
| python_startup_no_site   | 5.93 ms                                                | 8.28 ms: 1.40x slower                                                      |
| create_gc_cycles         | 1.62 ms                                                | 2.46 ms: 1.52x slower                                                      |
| bench_mp_pool            | 24.0 ms                                                | 85.3 ms: 3.55x slower                                                      |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                               |
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250326-3.14.0a6+-b3d84fd/bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.437x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.29x

# Memory
- memory change: 1.28x