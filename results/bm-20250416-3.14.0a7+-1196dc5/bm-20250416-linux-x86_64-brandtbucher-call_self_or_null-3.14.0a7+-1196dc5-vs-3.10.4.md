# Results vs. 3.10.4

- fork: brandtbucher
- ref: call_self_or_null
- machine: linux-x86_64
- commit hash: 1196dc5
- commit date: 2025-04-16
- overall geometric mean: 1.452x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250416-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-1196dc5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 250 ms: 1.40x faster                                                      |
| docutils       | 3.30 sec                                               | 2.59 sec: 1.27x faster                                                    |
| html5lib       | 88.9 ms                                                | 62.6 ms: 1.42x faster                                                     |
| Geometric mean | (ref)                                                  | 1.36x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250416-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-1196dc5 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 624 ms: 2.83x faster                                                      |
| async_tree_none         | 728 ms                                                 | 263 ms: 2.76x faster                                                      |
| async_tree_memoization  | 870 ms                                                 | 318 ms: 2.73x faster                                                      |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 485 ms: 2.10x faster                                                      |
| Geometric mean          | (ref)                                                  | 2.59x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250416-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-1196dc5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 73.0 ms: 1.60x faster                                                     |
| nbody          | 154 ms                                                 | 96.6 ms: 1.59x faster                                                     |
| pidigits       | 191 ms                                                 | 194 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                  | 1.36x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250416-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-1196dc5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.49x faster                                                      |
| regex_v8       | 27.8 ms                                                | 22.6 ms: 1.23x faster                                                     |
| regex_effbot   | 3.63 ms                                                | 3.25 ms: 1.12x faster                                                     |
| regex_dna      | 227 ms                                                 | 212 ms: 1.07x faster                                                      |
| Geometric mean | (ref)                                                  | 1.22x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250416-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-1196dc5 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.96 sec: 1.60x faster                                                    |
| pickle_pure_python   | 484 us                                                 | 318 us: 1.52x faster                                                      |
| unpickle_pure_python | 331 us                                                 | 231 us: 1.43x faster                                                      |
| xml_etree_process    | 79.1 ms                                                | 58.7 ms: 1.35x faster                                                     |
| json_dumps           | 14.2 ms                                                | 11.4 ms: 1.24x faster                                                     |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                                      |
| xml_etree_generate   | 99.4 ms                                                | 84.1 ms: 1.18x faster                                                     |
| xml_etree_iterparse  | 115 ms                                                 | 98.7 ms: 1.17x faster                                                     |
| json_loads           | 31.2 us                                                | 29.4 us: 1.06x faster                                                     |
| Geometric mean       | (ref)                                                  | 1.29x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250416-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-1196dc5 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.2 ms: 1.10x faster                                                     |
| python_startup_no_site | 5.93 ms                                                | 8.24 ms: 1.39x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250416-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-1196dc5 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.6 ms: 1.52x faster                                                     |
| mako            | 16.3 ms                                                | 11.0 ms: 1.49x faster                                                     |
| genshi_text     | 31.8 ms                                                | 21.8 ms: 1.46x faster                                                     |
| genshi_xml      | 66.0 ms                                                | 49.1 ms: 1.35x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250416-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-1196dc5 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 166 us: 3.28x faster                                                      |
| async_tree_io            | 1.77 sec                                               | 624 ms: 2.83x faster                                                      |
| async_tree_none          | 728 ms                                                 | 263 ms: 2.76x faster                                                      |
| generators               | 80.1 ms                                                | 29.3 ms: 2.74x faster                                                     |
| async_tree_memoization   | 870 ms                                                 | 318 ms: 2.73x faster                                                      |
| mdp                      | 2.85 sec                                               | 1.20 sec: 2.37x faster                                                    |
| deltablue                | 7.91 ms                                                | 3.40 ms: 2.33x faster                                                     |
| go                       | 240 ms                                                 | 113 ms: 2.13x faster                                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 485 ms: 2.10x faster                                                      |
| deepcopy_memo            | 58.5 us                                                | 28.4 us: 2.06x faster                                                     |
| pylint                   | 551 ms                                                 | 278 ms: 1.98x faster                                                      |
| richards_super           | 94.7 ms                                                | 48.3 ms: 1.96x faster                                                     |
| logging_silent           | 190 ns                                                 | 98.5 ns: 1.93x faster                                                     |
| deepcopy                 | 479 us                                                 | 249 us: 1.92x faster                                                      |
| chaos                    | 115 ms                                                 | 60.7 ms: 1.90x faster                                                     |
| richards                 | 79.3 ms                                                | 42.2 ms: 1.88x faster                                                     |
| scimark_sor              | 220 ms                                                 | 118 ms: 1.86x faster                                                      |
| scimark_monte_carlo      | 118 ms                                                 | 65.6 ms: 1.80x faster                                                     |
| crypto_pyaes             | 128 ms                                                 | 72.8 ms: 1.76x faster                                                     |
| raytrace                 | 507 ms                                                 | 293 ms: 1.73x faster                                                      |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                                     |
| hexiom                   | 10.4 ms                                                | 6.24 ms: 1.67x faster                                                     |
| spectral_norm            | 170 ms                                                 | 103 ms: 1.65x faster                                                      |
| float                    | 117 ms                                                 | 73.0 ms: 1.60x faster                                                     |
| tomli_loads              | 3.14 sec                                               | 1.96 sec: 1.60x faster                                                    |
| nbody                    | 154 ms                                                 | 96.6 ms: 1.59x faster                                                     |
| deepcopy_reduce          | 4.17 us                                                | 2.63 us: 1.59x faster                                                     |
| pyflate                  | 716 ms                                                 | 452 ms: 1.58x faster                                                      |
| pickle_pure_python       | 484 us                                                 | 318 us: 1.52x faster                                                      |
| django_template          | 48.2 ms                                                | 31.6 ms: 1.52x faster                                                     |
| scimark_lu               | 176 ms                                                 | 118 ms: 1.49x faster                                                      |
| mako                     | 16.3 ms                                                | 11.0 ms: 1.49x faster                                                     |
| regex_compile            | 188 ms                                                 | 127 ms: 1.49x faster                                                      |
| logging_format           | 9.09 us                                                | 6.12 us: 1.49x faster                                                     |
| logging_simple           | 8.30 us                                                | 5.62 us: 1.48x faster                                                     |
| genshi_text              | 31.8 ms                                                | 21.8 ms: 1.46x faster                                                     |
| coroutines               | 35.1 ms                                                | 24.2 ms: 1.45x faster                                                     |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.43x faster                                                    |
| unpickle_pure_python     | 331 us                                                 | 231 us: 1.43x faster                                                      |
| html5lib                 | 88.9 ms                                                | 62.6 ms: 1.42x faster                                                     |
| dulwich_log              | 84.3 ms                                                | 60.0 ms: 1.41x faster                                                     |
| pprint_safe_repr         | 1.02 sec                                               | 726 ms: 1.40x faster                                                      |
| 2to3                     | 348 ms                                                 | 250 ms: 1.40x faster                                                      |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.8 ms: 1.39x faster                                                     |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.74 ms: 1.36x faster                                                     |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.35x faster                                                    |
| xml_etree_process        | 79.1 ms                                                | 58.7 ms: 1.35x faster                                                     |
| genshi_xml               | 66.0 ms                                                | 49.1 ms: 1.35x faster                                                     |
| sympy_integrate          | 25.8 ms                                                | 19.4 ms: 1.33x faster                                                     |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.33x faster                                                      |
| scimark_fft              | 466 ms                                                 | 355 ms: 1.31x faster                                                      |
| sqlalchemy_declarative   | 172 ms                                                 | 132 ms: 1.31x faster                                                      |
| sympy_str                | 346 ms                                                 | 265 ms: 1.30x faster                                                      |
| nqueens                  | 106 ms                                                 | 81.3 ms: 1.30x faster                                                     |
| fannkuch                 | 532 ms                                                 | 415 ms: 1.28x faster                                                      |
| docutils                 | 3.30 sec                                               | 2.59 sec: 1.27x faster                                                    |
| sympy_expand             | 566 ms                                                 | 448 ms: 1.26x faster                                                      |
| json_dumps               | 14.2 ms                                                | 11.4 ms: 1.24x faster                                                     |
| regex_v8                 | 27.8 ms                                                | 22.6 ms: 1.23x faster                                                     |
| pathlib                  | 20.5 ms                                                | 16.9 ms: 1.21x faster                                                     |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                                      |
| xml_etree_generate       | 99.4 ms                                                | 84.1 ms: 1.18x faster                                                     |
| xml_etree_iterparse      | 115 ms                                                 | 98.7 ms: 1.17x faster                                                     |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.12x faster                                                      |
| regex_effbot             | 3.63 ms                                                | 3.25 ms: 1.12x faster                                                     |
| bench_thread_pool        | 986 us                                                 | 886 us: 1.11x faster                                                      |
| async_generators         | 444 ms                                                 | 400 ms: 1.11x faster                                                      |
| python_startup           | 14.6 ms                                                | 13.2 ms: 1.10x faster                                                     |
| json                     | 5.69 ms                                                | 5.25 ms: 1.08x faster                                                     |
| sqlite_synth             | 3.02 us                                                | 2.80 us: 1.08x faster                                                     |
| regex_dna                | 227 ms                                                 | 212 ms: 1.07x faster                                                      |
| json_loads               | 31.2 us                                                | 29.4 us: 1.06x faster                                                     |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                      |
| pidigits                 | 191 ms                                                 | 194 ms: 1.02x slower                                                      |
| telco                    | 7.27 ms                                                | 7.79 ms: 1.07x slower                                                     |
| coverage                 | 79.4 ms                                                | 86.3 ms: 1.09x slower                                                     |
| python_startup_no_site   | 5.93 ms                                                | 8.24 ms: 1.39x slower                                                     |
| gc_traversal             | 3.62 ms                                                | 5.05 ms: 1.39x slower                                                     |
| create_gc_cycles         | 1.62 ms                                                | 2.48 ms: 1.53x slower                                                     |
| bench_mp_pool            | 24.0 ms                                                | 81.7 ms: 3.40x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                              |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250416-3.14.0a7+-1196dc5/bm-20250416-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-1196dc5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.452x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.36x
- 95% likely to have a speedup of 1.34x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: 1.28x