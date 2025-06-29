# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_up_12_11
- machine: linux-x86_64
- commit hash: af1f59b
- commit date: 2025-06-29
- overall geometric mean: 1.488x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.33x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_11-3.15.0a0-af1f59b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 259 ms: 1.34x faster                                                |
| docutils       | 3.30 sec                                               | 2.64 sec: 1.25x faster                                              |
| html5lib       | 88.9 ms                                                | 61.5 ms: 1.44x faster                                               |
| Geometric mean | (ref)                                                  | 1.34x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_11-3.15.0a0-af1f59b |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 601 ms: 2.94x faster                                                |
| async_tree_none         | 728 ms                                                 | 260 ms: 2.80x faster                                                |
| async_tree_memoization  | 870 ms                                                 | 311 ms: 2.79x faster                                                |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 502 ms: 2.03x faster                                                |
| Geometric mean          | (ref)                                                  | 2.61x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_11-3.15.0a0-af1f59b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 117 ms                                                 | 65.7 ms: 1.78x faster                                               |
| nbody          | 154 ms                                                 | 100 ms: 1.53x faster                                                |
| pidigits       | 191 ms                                                 | 193 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                  | 1.39x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_11-3.15.0a0-af1f59b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.49x faster                                                |
| regex_v8       | 27.8 ms                                                | 24.0 ms: 1.16x faster                                               |
| regex_effbot   | 3.63 ms                                                | 3.41 ms: 1.06x faster                                               |
| regex_dna      | 227 ms                                                 | 215 ms: 1.05x faster                                                |
| Geometric mean | (ref)                                                  | 1.18x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_11-3.15.0a0-af1f59b |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 189 us: 1.75x faster                                                |
| tomli_loads          | 3.14 sec                                               | 1.81 sec: 1.74x faster                                              |
| pickle_pure_python   | 484 us                                                 | 320 us: 1.52x faster                                                |
| xml_etree_process    | 79.1 ms                                                | 55.4 ms: 1.43x faster                                               |
| json_dumps           | 14.2 ms                                                | 11.1 ms: 1.28x faster                                               |
| xml_etree_generate   | 99.4 ms                                                | 79.7 ms: 1.25x faster                                               |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                                |
| xml_etree_iterparse  | 115 ms                                                 | 99.0 ms: 1.17x faster                                               |
| json_loads           | 31.2 us                                                | 28.1 us: 1.11x faster                                               |
| Geometric mean       | (ref)                                                  | 1.36x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_11-3.15.0a0-af1f59b |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.2 ms: 1.19x faster                                               |
| python_startup_no_site | 5.93 ms                                                | 6.95 ms: 1.17x slower                                               |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_11-3.15.0a0-af1f59b |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.6 ms: 1.54x faster                                               |
| genshi_text     | 31.8 ms                                                | 21.5 ms: 1.48x faster                                               |
| django_template | 48.2 ms                                                | 32.9 ms: 1.46x faster                                               |
| genshi_xml      | 66.0 ms                                                | 49.7 ms: 1.33x faster                                               |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_11-3.15.0a0-af1f59b |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.25x faster                                                |
| async_tree_io            | 1.77 sec                                               | 601 ms: 2.94x faster                                                |
| async_tree_none          | 728 ms                                                 | 260 ms: 2.80x faster                                                |
| async_tree_memoization   | 870 ms                                                 | 311 ms: 2.79x faster                                                |
| richards_super           | 94.7 ms                                                | 35.7 ms: 2.66x faster                                               |
| generators               | 80.1 ms                                                | 30.6 ms: 2.62x faster                                               |
| richards                 | 79.3 ms                                                | 30.3 ms: 2.61x faster                                               |
| deltablue                | 7.91 ms                                                | 3.03 ms: 2.61x faster                                               |
| mdp                      | 2.85 sec                                               | 1.23 sec: 2.32x faster                                              |
| go                       | 240 ms                                                 | 115 ms: 2.08x faster                                                |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 502 ms: 2.03x faster                                                |
| deepcopy_memo            | 58.5 us                                                | 29.5 us: 1.98x faster                                               |
| pylint                   | 551 ms                                                 | 283 ms: 1.95x faster                                                |
| spectral_norm            | 170 ms                                                 | 88.7 ms: 1.91x faster                                               |
| chaos                    | 115 ms                                                 | 61.6 ms: 1.87x faster                                               |
| raytrace                 | 507 ms                                                 | 273 ms: 1.86x faster                                                |
| deepcopy                 | 479 us                                                 | 258 us: 1.85x faster                                                |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.84x faster                                                |
| logging_silent           | 190 ns                                                 | 103 ns: 1.83x faster                                                |
| scimark_monte_carlo      | 118 ms                                                 | 66.0 ms: 1.79x faster                                               |
| float                    | 117 ms                                                 | 65.7 ms: 1.78x faster                                               |
| pyflate                  | 716 ms                                                 | 403 ms: 1.78x faster                                                |
| comprehensions           | 28.8 us                                                | 16.2 us: 1.77x faster                                               |
| unpickle_pure_python     | 331 us                                                 | 189 us: 1.75x faster                                                |
| tomli_loads              | 3.14 sec                                               | 1.81 sec: 1.74x faster                                              |
| djangocms                | 38.4 us                                                | 22.6 us: 1.70x faster                                               |
| crypto_pyaes             | 128 ms                                                 | 75.7 ms: 1.69x faster                                               |
| hexiom                   | 10.4 ms                                                | 6.17 ms: 1.69x faster                                               |
| mako                     | 16.3 ms                                                | 10.6 ms: 1.54x faster                                               |
| nbody                    | 154 ms                                                 | 100 ms: 1.53x faster                                                |
| deepcopy_reduce          | 4.17 us                                                | 2.74 us: 1.52x faster                                               |
| pickle_pure_python       | 484 us                                                 | 320 us: 1.52x faster                                                |
| scimark_fft              | 466 ms                                                 | 311 ms: 1.50x faster                                                |
| logging_simple           | 8.30 us                                                | 5.57 us: 1.49x faster                                               |
| regex_compile            | 188 ms                                                 | 127 ms: 1.49x faster                                                |
| scimark_lu               | 176 ms                                                 | 119 ms: 1.48x faster                                                |
| genshi_text              | 31.8 ms                                                | 21.5 ms: 1.48x faster                                               |
| django_template          | 48.2 ms                                                | 32.9 ms: 1.46x faster                                               |
| logging_format           | 9.09 us                                                | 6.27 us: 1.45x faster                                               |
| html5lib                 | 88.9 ms                                                | 61.5 ms: 1.44x faster                                               |
| pprint_pformat           | 2.10 sec                                               | 1.46 sec: 1.44x faster                                              |
| xml_etree_process        | 79.1 ms                                                | 55.4 ms: 1.43x faster                                               |
| dulwich_log              | 84.3 ms                                                | 59.3 ms: 1.42x faster                                               |
| coroutines               | 35.1 ms                                                | 24.7 ms: 1.42x faster                                               |
| pprint_safe_repr         | 1.02 sec                                               | 720 ms: 1.41x faster                                                |
| thrift                   | 1.07 ms                                                | 768 us: 1.40x faster                                                |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.37x faster                                              |
| 2to3                     | 348 ms                                                 | 259 ms: 1.34x faster                                                |
| fannkuch                 | 532 ms                                                 | 397 ms: 1.34x faster                                                |
| sympy_integrate          | 25.8 ms                                                | 19.3 ms: 1.33x faster                                               |
| genshi_xml               | 66.0 ms                                                | 49.7 ms: 1.33x faster                                               |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.87 ms: 1.33x faster                                               |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.32x faster                                                |
| nqueens                  | 106 ms                                                 | 82.1 ms: 1.29x faster                                               |
| json_dumps               | 14.2 ms                                                | 11.1 ms: 1.28x faster                                               |
| sympy_str                | 346 ms                                                 | 272 ms: 1.27x faster                                                |
| docutils                 | 3.30 sec                                               | 2.64 sec: 1.25x faster                                              |
| xml_etree_generate       | 99.4 ms                                                | 79.7 ms: 1.25x faster                                               |
| sympy_expand             | 566 ms                                                 | 465 ms: 1.22x faster                                                |
| python_startup           | 14.6 ms                                                | 12.2 ms: 1.19x faster                                               |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                                |
| xml_etree_iterparse      | 115 ms                                                 | 99.0 ms: 1.17x faster                                               |
| pathlib                  | 20.5 ms                                                | 17.5 ms: 1.17x faster                                               |
| regex_v8                 | 27.8 ms                                                | 24.0 ms: 1.16x faster                                               |
| meteor_contest           | 120 ms                                                 | 105 ms: 1.14x faster                                                |
| json_loads               | 31.2 us                                                | 28.1 us: 1.11x faster                                               |
| json                     | 5.69 ms                                                | 5.21 ms: 1.09x faster                                               |
| sqlite_synth             | 3.02 us                                                | 2.80 us: 1.08x faster                                               |
| regex_effbot             | 3.63 ms                                                | 3.41 ms: 1.06x faster                                               |
| regex_dna                | 227 ms                                                 | 215 ms: 1.05x faster                                                |
| async_generators         | 444 ms                                                 | 430 ms: 1.03x faster                                                |
| asyncio_websockets       | 559 ms                                                 | 554 ms: 1.01x faster                                                |
| pidigits                 | 191 ms                                                 | 193 ms: 1.01x slower                                                |
| telco                    | 7.27 ms                                                | 7.74 ms: 1.06x slower                                               |
| coverage                 | 79.4 ms                                                | 88.1 ms: 1.11x slower                                               |
| python_startup_no_site   | 5.93 ms                                                | 6.95 ms: 1.17x slower                                               |
| gc_traversal             | 3.62 ms                                                | 4.76 ms: 1.31x slower                                               |
| create_gc_cycles         | 1.62 ms                                                | 2.57 ms: 1.59x slower                                               |
| Geometric mean           | (ref)                                                  | 1.49x faster                                                        |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250629-3.15.0a0-af1f59b-JIT/bm-20250629-linux-x86_64-brandtbucher-jit_up_12_11-3.15.0a0-af1f59b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.488x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.39x
- 95% likely to have a speedup of 1.36x
- 99% likely to have a speedup of 1.33x

# Memory
- memory change: 1.33x