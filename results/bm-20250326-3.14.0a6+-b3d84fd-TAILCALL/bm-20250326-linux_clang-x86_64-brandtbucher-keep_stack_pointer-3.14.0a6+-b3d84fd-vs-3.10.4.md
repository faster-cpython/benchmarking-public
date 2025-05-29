# Results vs. 3.10.4

- fork: brandtbucher
- ref: keep_stack_pointer
- machine: linux-x86_64
- commit hash: b3d84fd
- commit date: 2025-03-26
- overall geometric mean: 1.494x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.36x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 248 ms: 1.40x faster                                                       |
| docutils       | 3.30 sec                                               | 2.55 sec: 1.29x faster                                                     |
| html5lib       | 88.9 ms                                                | 57.7 ms: 1.54x faster                                                      |
| Geometric mean | (ref)                                                  | 1.41x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 600 ms: 2.95x faster                                                       |
| async_tree_none         | 728 ms                                                 | 249 ms: 2.92x faster                                                       |
| async_tree_memoization  | 870 ms                                                 | 305 ms: 2.85x faster                                                       |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 497 ms: 2.04x faster                                                       |
| Geometric mean          | (ref)                                                  | 2.66x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 81.2 ms: 1.89x faster                                                      |
| float          | 117 ms                                                 | 68.1 ms: 1.72x faster                                                      |
| pidigits       | 191 ms                                                 | 202 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                  | 1.45x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 125 ms: 1.51x faster                                                       |
| regex_dna      | 227 ms                                                 | 183 ms: 1.24x faster                                                       |
| regex_v8       | 27.8 ms                                                | 23.0 ms: 1.21x faster                                                      |
| regex_effbot   | 3.63 ms                                                | 3.07 ms: 1.18x faster                                                      |
| Geometric mean | (ref)                                                  | 1.28x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.87 sec: 1.67x faster                                                     |
| pickle_pure_python   | 484 us                                                 | 304 us: 1.59x faster                                                       |
| unpickle_pure_python | 331 us                                                 | 214 us: 1.54x faster                                                       |
| xml_etree_process    | 79.1 ms                                                | 58.9 ms: 1.34x faster                                                      |
| xml_etree_iterparse  | 115 ms                                                 | 101 ms: 1.14x faster                                                       |
| json_dumps           | 14.2 ms                                                | 12.4 ms: 1.14x faster                                                      |
| xml_etree_generate   | 99.4 ms                                                | 87.9 ms: 1.13x faster                                                      |
| json_loads           | 31.2 us                                                | 29.0 us: 1.08x faster                                                      |
| xml_etree_parse      | 168 ms                                                 | 158 ms: 1.07x faster                                                       |
| Geometric mean       | (ref)                                                  | 1.28x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                      |
| python_startup_no_site | 5.93 ms                                                | 8.12 ms: 1.37x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 30.7 ms: 1.57x faster                                                      |
| genshi_text     | 31.8 ms                                                | 20.4 ms: 1.56x faster                                                      |
| mako            | 16.3 ms                                                | 11.6 ms: 1.41x faster                                                      |
| genshi_xml      | 66.0 ms                                                | 46.9 ms: 1.41x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.49x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 154 us: 3.53x faster                                                       |
| async_tree_io            | 1.77 sec                                               | 600 ms: 2.95x faster                                                       |
| async_tree_none          | 728 ms                                                 | 249 ms: 2.92x faster                                                       |
| generators               | 80.1 ms                                                | 27.7 ms: 2.89x faster                                                      |
| async_tree_memoization   | 870 ms                                                 | 305 ms: 2.85x faster                                                       |
| deltablue                | 7.91 ms                                                | 2.93 ms: 2.70x faster                                                      |
| go                       | 240 ms                                                 | 109 ms: 2.20x faster                                                       |
| chaos                    | 115 ms                                                 | 54.1 ms: 2.13x faster                                                      |
| logging_silent           | 190 ns                                                 | 89.0 ns: 2.13x faster                                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 497 ms: 2.04x faster                                                       |
| scimark_sor              | 220 ms                                                 | 108 ms: 2.04x faster                                                       |
| pylint                   | 551 ms                                                 | 272 ms: 2.03x faster                                                       |
| spectral_norm            | 170 ms                                                 | 83.9 ms: 2.03x faster                                                      |
| raytrace                 | 507 ms                                                 | 250 ms: 2.02x faster                                                       |
| deepcopy_memo            | 58.5 us                                                | 28.9 us: 2.02x faster                                                      |
| richards_super           | 94.7 ms                                                | 48.1 ms: 1.97x faster                                                      |
| deepcopy                 | 479 us                                                 | 245 us: 1.96x faster                                                       |
| scimark_monte_carlo      | 118 ms                                                 | 60.6 ms: 1.95x faster                                                      |
| richards                 | 79.3 ms                                                | 41.5 ms: 1.91x faster                                                      |
| nbody                    | 154 ms                                                 | 81.2 ms: 1.89x faster                                                      |
| comprehensions           | 28.8 us                                                | 15.6 us: 1.84x faster                                                      |
| hexiom                   | 10.4 ms                                                | 5.74 ms: 1.81x faster                                                      |
| crypto_pyaes             | 128 ms                                                 | 71.0 ms: 1.80x faster                                                      |
| pyflate                  | 716 ms                                                 | 411 ms: 1.74x faster                                                       |
| float                    | 117 ms                                                 | 68.1 ms: 1.72x faster                                                      |
| tomli_loads              | 3.14 sec                                               | 1.87 sec: 1.67x faster                                                     |
| scimark_lu               | 176 ms                                                 | 107 ms: 1.65x faster                                                       |
| deepcopy_reduce          | 4.17 us                                                | 2.59 us: 1.61x faster                                                      |
| coroutines               | 35.1 ms                                                | 22.0 ms: 1.60x faster                                                      |
| pickle_pure_python       | 484 us                                                 | 304 us: 1.59x faster                                                       |
| django_template          | 48.2 ms                                                | 30.7 ms: 1.57x faster                                                      |
| genshi_text              | 31.8 ms                                                | 20.4 ms: 1.56x faster                                                      |
| scimark_fft              | 466 ms                                                 | 301 ms: 1.55x faster                                                       |
| unpickle_pure_python     | 331 us                                                 | 214 us: 1.54x faster                                                       |
| html5lib                 | 88.9 ms                                                | 57.7 ms: 1.54x faster                                                      |
| logging_simple           | 8.30 us                                                | 5.42 us: 1.53x faster                                                      |
| logging_format           | 9.09 us                                                | 5.98 us: 1.52x faster                                                      |
| regex_compile            | 188 ms                                                 | 125 ms: 1.51x faster                                                       |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.30 ms: 1.51x faster                                                      |
| dulwich_log              | 84.3 ms                                                | 57.4 ms: 1.47x faster                                                      |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.3 ms: 1.43x faster                                                      |
| thrift                   | 1.07 ms                                                | 754 us: 1.42x faster                                                       |
| pycparser                | 1.58 sec                                               | 1.11 sec: 1.42x faster                                                     |
| mako                     | 16.3 ms                                                | 11.6 ms: 1.41x faster                                                      |
| genshi_xml               | 66.0 ms                                                | 46.9 ms: 1.41x faster                                                      |
| 2to3                     | 348 ms                                                 | 248 ms: 1.40x faster                                                       |
| pprint_pformat           | 2.10 sec                                               | 1.51 sec: 1.40x faster                                                     |
| sympy_integrate          | 25.8 ms                                                | 18.7 ms: 1.38x faster                                                      |
| pprint_safe_repr         | 1.02 sec                                               | 738 ms: 1.38x faster                                                       |
| pathlib                  | 20.5 ms                                                | 14.9 ms: 1.38x faster                                                      |
| nqueens                  | 106 ms                                                 | 77.4 ms: 1.37x faster                                                      |
| sympy_sum                | 196 ms                                                 | 145 ms: 1.36x faster                                                       |
| sqlalchemy_declarative   | 172 ms                                                 | 127 ms: 1.35x faster                                                       |
| xml_etree_process        | 79.1 ms                                                | 58.9 ms: 1.34x faster                                                      |
| sympy_str                | 346 ms                                                 | 262 ms: 1.32x faster                                                       |
| fannkuch                 | 532 ms                                                 | 407 ms: 1.31x faster                                                       |
| docutils                 | 3.30 sec                                               | 2.55 sec: 1.29x faster                                                     |
| sympy_expand             | 566 ms                                                 | 445 ms: 1.27x faster                                                       |
| regex_dna                | 227 ms                                                 | 183 ms: 1.24x faster                                                       |
| regex_v8                 | 27.8 ms                                                | 23.0 ms: 1.21x faster                                                      |
| bench_thread_pool        | 986 us                                                 | 834 us: 1.18x faster                                                       |
| regex_effbot             | 3.63 ms                                                | 3.07 ms: 1.18x faster                                                      |
| async_generators         | 444 ms                                                 | 383 ms: 1.16x faster                                                       |
| xml_etree_iterparse      | 115 ms                                                 | 101 ms: 1.14x faster                                                       |
| json_dumps               | 14.2 ms                                                | 12.4 ms: 1.14x faster                                                      |
| xml_etree_generate       | 99.4 ms                                                | 87.9 ms: 1.13x faster                                                      |
| python_startup           | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                      |
| sqlite_synth             | 3.02 us                                                | 2.69 us: 1.13x faster                                                      |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                       |
| json_loads               | 31.2 us                                                | 29.0 us: 1.08x faster                                                      |
| json                     | 5.69 ms                                                | 5.29 ms: 1.08x faster                                                      |
| xml_etree_parse          | 168 ms                                                 | 158 ms: 1.07x faster                                                       |
| mdp                      | 2.85 sec                                               | 2.72 sec: 1.05x faster                                                     |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                       |
| coverage                 | 79.4 ms                                                | 81.0 ms: 1.02x slower                                                      |
| telco                    | 7.27 ms                                                | 7.45 ms: 1.03x slower                                                      |
| pidigits                 | 191 ms                                                 | 202 ms: 1.06x slower                                                       |
| python_startup_no_site   | 5.93 ms                                                | 8.12 ms: 1.37x slower                                                      |
| gc_traversal             | 3.62 ms                                                | 4.96 ms: 1.37x slower                                                      |
| create_gc_cycles         | 1.62 ms                                                | 2.55 ms: 1.57x slower                                                      |
| bench_mp_pool            | 24.0 ms                                                | 81.1 ms: 3.38x slower                                                      |
| Geometric mean           | (ref)                                                  | 1.47x faster                                                               |
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250326-3.14.0a6+-b3d84fd-CLANG/bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.494x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.39x
- 95% likely to have a speedup of 1.38x
- 99% likely to have a speedup of 1.36x

# Memory
- memory change: 1.28x