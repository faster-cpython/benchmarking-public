# Results vs. 3.10.4

- fork: python
- ref: 0f866cbfefd797b4dae2
- machine: linux-x86_64
- commit hash: 0f866cb
- commit date: 2025-06-10
- overall geometric mean: 1.463x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 260 ms: 1.34x faster                                                  |
| docutils       | 3.30 sec                                               | 2.64 sec: 1.25x faster                                                |
| html5lib       | 88.9 ms                                                | 61.4 ms: 1.45x faster                                                 |
| Geometric mean | (ref)                                                  | 1.34x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 598 ms: 2.96x faster                                                  |
| async_tree_none         | 728 ms                                                 | 263 ms: 2.77x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 315 ms: 2.76x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 499 ms: 2.04x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.60x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 117 ms                                                 | 65.1 ms: 1.80x faster                                                 |
| nbody          | 154 ms                                                 | 94.5 ms: 1.63x faster                                                 |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.44x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.48x faster                                                  |
| regex_v8       | 27.8 ms                                                | 22.4 ms: 1.24x faster                                                 |
| regex_dna      | 227 ms                                                 | 200 ms: 1.13x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.31 ms: 1.10x faster                                                 |
| Geometric mean | (ref)                                                  | 1.23x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.90 sec: 1.65x faster                                                |
| unpickle_pure_python | 331 us                                                 | 201 us: 1.65x faster                                                  |
| pickle_pure_python   | 484 us                                                 | 322 us: 1.50x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 56.0 ms: 1.41x faster                                                 |
| json_dumps           | 14.2 ms                                                | 11.2 ms: 1.26x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 80.0 ms: 1.24x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 98.5 ms: 1.17x faster                                                 |
| json_loads           | 31.2 us                                                | 28.4 us: 1.10x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.34x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.2 ms: 1.19x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 6.96 ms: 1.17x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.6 ms: 1.54x faster                                                 |
| genshi_text     | 31.8 ms                                                | 21.1 ms: 1.51x faster                                                 |
| django_template | 48.2 ms                                                | 32.5 ms: 1.48x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 49.7 ms: 1.33x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.46x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 171 us: 3.18x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 598 ms: 2.96x faster                                                  |
| async_tree_none          | 728 ms                                                 | 263 ms: 2.77x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 315 ms: 2.76x faster                                                  |
| generators               | 80.1 ms                                                | 31.0 ms: 2.58x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.11 ms: 2.55x faster                                                 |
| richards_super           | 94.7 ms                                                | 39.9 ms: 2.38x faster                                                 |
| richards                 | 79.3 ms                                                | 33.9 ms: 2.34x faster                                                 |
| mdp                      | 2.85 sec                                               | 1.24 sec: 2.29x faster                                                |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 499 ms: 2.04x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 29.5 us: 1.98x faster                                                 |
| go                       | 240 ms                                                 | 122 ms: 1.96x faster                                                  |
| pylint                   | 551 ms                                                 | 283 ms: 1.95x faster                                                  |
| deepcopy                 | 479 us                                                 | 258 us: 1.86x faster                                                  |
| chaos                    | 115 ms                                                 | 62.2 ms: 1.86x faster                                                 |
| raytrace                 | 507 ms                                                 | 275 ms: 1.84x faster                                                  |
| scimark_sor              | 220 ms                                                 | 122 ms: 1.81x faster                                                  |
| float                    | 117 ms                                                 | 65.1 ms: 1.80x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 67.5 ms: 1.75x faster                                                 |
| pyflate                  | 716 ms                                                 | 412 ms: 1.74x faster                                                  |
| djangocms                | 38.4 us                                                | 22.4 us: 1.71x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 75.8 ms: 1.69x faster                                                 |
| comprehensions           | 28.8 us                                                | 17.1 us: 1.68x faster                                                 |
| spectral_norm            | 170 ms                                                 | 101 ms: 1.68x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 1.90 sec: 1.65x faster                                                |
| unpickle_pure_python     | 331 us                                                 | 201 us: 1.65x faster                                                  |
| nbody                    | 154 ms                                                 | 94.5 ms: 1.63x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.52 ms: 1.59x faster                                                 |
| deepcopy_reduce          | 4.17 us                                                | 2.69 us: 1.55x faster                                                 |
| mako                     | 16.3 ms                                                | 10.6 ms: 1.54x faster                                                 |
| genshi_text              | 31.8 ms                                                | 21.1 ms: 1.51x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 322 us: 1.50x faster                                                  |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.50x faster                                                  |
| regex_compile            | 188 ms                                                 | 127 ms: 1.48x faster                                                  |
| django_template          | 48.2 ms                                                | 32.5 ms: 1.48x faster                                                 |
| html5lib                 | 88.9 ms                                                | 61.4 ms: 1.45x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 56.0 ms: 1.41x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.12 sec: 1.41x faster                                                |
| coroutines               | 35.1 ms                                                | 25.1 ms: 1.40x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 60.6 ms: 1.39x faster                                                 |
| scimark_fft              | 466 ms                                                 | 335 ms: 1.39x faster                                                  |
| thrift                   | 1.07 ms                                                | 783 us: 1.37x faster                                                  |
| logging_simple           | 8.30 us                                                | 6.08 us: 1.36x faster                                                 |
| logging_format           | 9.09 us                                                | 6.69 us: 1.36x faster                                                 |
| 2to3                     | 348 ms                                                 | 260 ms: 1.34x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 19.4 ms: 1.33x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 49.7 ms: 1.33x faster                                                 |
| sympy_sum                | 196 ms                                                 | 150 ms: 1.31x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.00 ms: 1.30x faster                                                 |
| fannkuch                 | 532 ms                                                 | 411 ms: 1.29x faster                                                  |
| sympy_str                | 346 ms                                                 | 273 ms: 1.27x faster                                                  |
| nqueens                  | 106 ms                                                 | 83.9 ms: 1.26x faster                                                 |
| json_dumps               | 14.2 ms                                                | 11.2 ms: 1.26x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.68 sec: 1.25x faster                                                |
| docutils                 | 3.30 sec                                               | 2.64 sec: 1.25x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 80.0 ms: 1.24x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 22.4 ms: 1.24x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 825 ms: 1.23x faster                                                  |
| pathlib                  | 20.5 ms                                                | 16.9 ms: 1.21x faster                                                 |
| sympy_expand             | 566 ms                                                 | 468 ms: 1.21x faster                                                  |
| python_startup           | 14.6 ms                                                | 12.2 ms: 1.19x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 98.5 ms: 1.17x faster                                                 |
| regex_dna                | 227 ms                                                 | 200 ms: 1.13x faster                                                  |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                  |
| json_loads               | 31.2 us                                                | 28.4 us: 1.10x faster                                                 |
| regex_effbot             | 3.63 ms                                                | 3.31 ms: 1.10x faster                                                 |
| json                     | 5.69 ms                                                | 5.24 ms: 1.09x faster                                                 |
| sqlite_synth             | 3.02 us                                                | 2.80 us: 1.08x faster                                                 |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                  |
| async_generators         | 444 ms                                                 | 441 ms: 1.01x faster                                                  |
| telco                    | 7.27 ms                                                | 7.92 ms: 1.09x slower                                                 |
| coverage                 | 79.4 ms                                                | 87.7 ms: 1.10x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 6.96 ms: 1.17x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 4.92 ms: 1.36x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 2.59 ms: 1.60x slower                                                 |
| logging_silent           | 190 ns                                                 | 470 ns: 2.48x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.44x faster                                                          |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250610-3.15.0a0-0f866cb-JIT/bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.463x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.35x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.29x

# Memory
- memory change: 1.33x