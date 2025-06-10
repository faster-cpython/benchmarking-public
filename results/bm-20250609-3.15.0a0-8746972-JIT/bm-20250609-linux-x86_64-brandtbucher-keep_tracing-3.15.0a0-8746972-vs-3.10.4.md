# Results vs. 3.10.4

- fork: brandtbucher
- ref: keep_tracing
- machine: linux-x86_64
- commit hash: 8746972
- commit date: 2025-06-09
- overall geometric mean: 1.317x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250609-linux-x86_64-brandtbucher-keep_tracing-3.15.0a0-8746972 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 262 ms: 1.33x faster                                                |
| docutils       | 3.30 sec                                               | 2.65 sec: 1.24x faster                                              |
| html5lib       | 88.9 ms                                                | 62.3 ms: 1.43x faster                                               |
| Geometric mean | (ref)                                                  | 1.33x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250609-linux-x86_64-brandtbucher-keep_tracing-3.15.0a0-8746972 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 605 ms: 2.92x faster                                                |
| async_tree_memoization  | 870 ms                                                 | 315 ms: 2.76x faster                                                |
| async_tree_none         | 728 ms                                                 | 265 ms: 2.75x faster                                                |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 506 ms: 2.01x faster                                                |
| Geometric mean          | (ref)                                                  | 2.58x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250609-linux-x86_64-brandtbucher-keep_tracing-3.15.0a0-8746972 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 117 ms                                                 | 65.4 ms: 1.79x faster                                               |
| nbody          | 154 ms                                                 | 90.4 ms: 1.70x faster                                               |
| pidigits       | 191 ms                                                 | 191 ms: 1.00x slower                                                |
| Geometric mean | (ref)                                                  | 1.45x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250609-linux-x86_64-brandtbucher-keep_tracing-3.15.0a0-8746972 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.46x faster                                                |
| regex_v8       | 27.8 ms                                                | 22.8 ms: 1.22x faster                                               |
| regex_effbot   | 3.63 ms                                                | 3.49 ms: 1.04x faster                                               |
| regex_dna      | 227 ms                                                 | 219 ms: 1.03x faster                                                |
| Geometric mean | (ref)                                                  | 1.18x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250609-linux-x86_64-brandtbucher-keep_tracing-3.15.0a0-8746972 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.93 sec: 1.63x faster                                              |
| unpickle_pure_python | 331 us                                                 | 205 us: 1.61x faster                                                |
| pickle_pure_python   | 484 us                                                 | 330 us: 1.47x faster                                                |
| xml_etree_process    | 79.1 ms                                                | 56.0 ms: 1.41x faster                                               |
| json_dumps           | 14.2 ms                                                | 11.2 ms: 1.26x faster                                               |
| xml_etree_generate   | 99.4 ms                                                | 80.5 ms: 1.23x faster                                               |
| xml_etree_parse      | 168 ms                                                 | 145 ms: 1.16x faster                                                |
| xml_etree_iterparse  | 115 ms                                                 | 101 ms: 1.15x faster                                                |
| json_loads           | 31.2 us                                                | 28.3 us: 1.10x faster                                               |
| Geometric mean       | (ref)                                                  | 1.32x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250609-linux-x86_64-brandtbucher-keep_tracing-3.15.0a0-8746972 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.2 ms: 1.20x faster                                               |
| python_startup_no_site | 5.93 ms                                                | 6.94 ms: 1.17x slower                                               |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250609-linux-x86_64-brandtbucher-keep_tracing-3.15.0a0-8746972 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.8 ms: 1.52x faster                                               |
| django_template | 48.2 ms                                                | 32.8 ms: 1.47x faster                                               |
| genshi_text     | 31.8 ms                                                | 22.0 ms: 1.44x faster                                               |
| genshi_xml      | 66.0 ms                                                | 51.1 ms: 1.29x faster                                               |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250609-linux-x86_64-brandtbucher-keep_tracing-3.15.0a0-8746972 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 172 us: 3.17x faster                                                |
| async_tree_io            | 1.77 sec                                               | 605 ms: 2.92x faster                                                |
| async_tree_memoization   | 870 ms                                                 | 315 ms: 2.76x faster                                                |
| async_tree_none          | 728 ms                                                 | 265 ms: 2.75x faster                                                |
| generators               | 80.1 ms                                                | 29.7 ms: 2.70x faster                                               |
| deltablue                | 7.91 ms                                                | 3.14 ms: 2.52x faster                                               |
| mdp                      | 2.85 sec                                               | 1.26 sec: 2.25x faster                                              |
| richards_super           | 94.7 ms                                                | 42.4 ms: 2.24x faster                                               |
| richards                 | 79.3 ms                                                | 37.0 ms: 2.15x faster                                               |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 506 ms: 2.01x faster                                                |
| deepcopy_memo            | 58.5 us                                                | 29.8 us: 1.96x faster                                               |
| pylint                   | 551 ms                                                 | 284 ms: 1.94x faster                                                |
| go                       | 240 ms                                                 | 126 ms: 1.91x faster                                                |
| chaos                    | 115 ms                                                 | 62.9 ms: 1.84x faster                                               |
| deepcopy                 | 479 us                                                 | 262 us: 1.83x faster                                                |
| raytrace                 | 507 ms                                                 | 278 ms: 1.83x faster                                                |
| scimark_sor              | 220 ms                                                 | 123 ms: 1.79x faster                                                |
| float                    | 117 ms                                                 | 65.4 ms: 1.79x faster                                               |
| scimark_monte_carlo      | 118 ms                                                 | 67.8 ms: 1.74x faster                                               |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.71x faster                                               |
| nbody                    | 154 ms                                                 | 90.4 ms: 1.70x faster                                               |
| pyflate                  | 716 ms                                                 | 425 ms: 1.69x faster                                                |
| crypto_pyaes             | 128 ms                                                 | 76.7 ms: 1.67x faster                                               |
| tomli_loads              | 3.14 sec                                               | 1.93 sec: 1.63x faster                                              |
| unpickle_pure_python     | 331 us                                                 | 205 us: 1.61x faster                                                |
| spectral_norm            | 170 ms                                                 | 106 ms: 1.61x faster                                                |
| hexiom                   | 10.4 ms                                                | 6.74 ms: 1.54x faster                                               |
| mako                     | 16.3 ms                                                | 10.8 ms: 1.52x faster                                               |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.50x faster                                                |
| deepcopy_reduce          | 4.17 us                                                | 2.82 us: 1.48x faster                                               |
| pickle_pure_python       | 484 us                                                 | 330 us: 1.47x faster                                                |
| django_template          | 48.2 ms                                                | 32.8 ms: 1.47x faster                                               |
| regex_compile            | 188 ms                                                 | 129 ms: 1.46x faster                                                |
| genshi_text              | 31.8 ms                                                | 22.0 ms: 1.44x faster                                               |
| html5lib                 | 88.9 ms                                                | 62.3 ms: 1.43x faster                                               |
| xml_etree_process        | 79.1 ms                                                | 56.0 ms: 1.41x faster                                               |
| coroutines               | 35.1 ms                                                | 25.2 ms: 1.39x faster                                               |
| scimark_fft              | 466 ms                                                 | 339 ms: 1.37x faster                                                |
| dulwich_log              | 84.3 ms                                                | 61.7 ms: 1.37x faster                                               |
| logging_simple           | 8.30 us                                                | 6.09 us: 1.36x faster                                               |
| logging_format           | 9.09 us                                                | 6.79 us: 1.34x faster                                               |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.34x faster                                              |
| 2to3                     | 348 ms                                                 | 262 ms: 1.33x faster                                                |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.91 ms: 1.32x faster                                               |
| sympy_integrate          | 25.8 ms                                                | 19.6 ms: 1.32x faster                                               |
| genshi_xml               | 66.0 ms                                                | 51.1 ms: 1.29x faster                                               |
| sympy_sum                | 196 ms                                                 | 152 ms: 1.29x faster                                                |
| nqueens                  | 106 ms                                                 | 83.0 ms: 1.27x faster                                               |
| fannkuch                 | 532 ms                                                 | 418 ms: 1.27x faster                                                |
| pprint_pformat           | 2.10 sec                                               | 1.66 sec: 1.27x faster                                              |
| json_dumps               | 14.2 ms                                                | 11.2 ms: 1.26x faster                                               |
| sympy_str                | 346 ms                                                 | 275 ms: 1.26x faster                                                |
| docutils                 | 3.30 sec                                               | 2.65 sec: 1.24x faster                                              |
| xml_etree_generate       | 99.4 ms                                                | 80.5 ms: 1.23x faster                                               |
| pprint_safe_repr         | 1.02 sec                                               | 831 ms: 1.22x faster                                                |
| regex_v8                 | 27.8 ms                                                | 22.8 ms: 1.22x faster                                               |
| pathlib                  | 20.5 ms                                                | 17.0 ms: 1.20x faster                                               |
| sympy_expand             | 566 ms                                                 | 472 ms: 1.20x faster                                                |
| python_startup           | 14.6 ms                                                | 12.2 ms: 1.20x faster                                               |
| xml_etree_parse          | 168 ms                                                 | 145 ms: 1.16x faster                                                |
| xml_etree_iterparse      | 115 ms                                                 | 101 ms: 1.15x faster                                                |
| json                     | 5.69 ms                                                | 5.14 ms: 1.11x faster                                               |
| json_loads               | 31.2 us                                                | 28.3 us: 1.10x faster                                               |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.10x faster                                                |
| sqlite_synth             | 3.02 us                                                | 2.81 us: 1.08x faster                                               |
| async_generators         | 444 ms                                                 | 424 ms: 1.05x faster                                                |
| regex_effbot             | 3.63 ms                                                | 3.49 ms: 1.04x faster                                               |
| regex_dna                | 227 ms                                                 | 219 ms: 1.03x faster                                                |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                |
| pidigits                 | 191 ms                                                 | 191 ms: 1.00x slower                                                |
| telco                    | 7.27 ms                                                | 8.07 ms: 1.11x slower                                               |
| python_startup_no_site   | 5.93 ms                                                | 6.94 ms: 1.17x slower                                               |
| gc_traversal             | 3.62 ms                                                | 5.18 ms: 1.43x slower                                               |
| create_gc_cycles         | 1.62 ms                                                | 2.60 ms: 1.60x slower                                               |
| logging_silent           | 190 ns                                                 | 487 ns: 2.57x slower                                                |
| coverage                 | 79.4 ms                                                | 428 ms: 5.39x slower                                                |
| thrift                   | 1.07 ms                                                | 148 ms: 138.34x slower                                              |
| Geometric mean           | (ref)                                                  | 1.30x faster                                                        |
Ignored benchmarks (24) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250609-3.15.0a0-8746972-JIT/bm-20250609-linux-x86_64-brandtbucher-keep_tracing-3.15.0a0-8746972.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.317x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.33x