# Results vs. 3.10.4

- fork: brandtbucher
- ref: inline_class_call_de
- machine: linux-x86_64
- commit hash: 5287d32
- commit date: 2024-06-06
- overall geometric mean: 1.34x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240606-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5287d32 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 280 ms: 1.25x faster                                                        |
| docutils       | 3.30 sec                                               | 2.96 sec: 1.11x faster                                                      |
| html5lib       | 88.9 ms                                                | 68.8 ms: 1.29x faster                                                       |
| tornado_http   | 136 ms                                                 | 98.7 ms: 1.38x faster                                                       |
| Geometric mean | (ref)                                                  | 1.25x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240606-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5287d32 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 380 ms: 1.92x faster                                                        |
| async_tree_memoization  | 870 ms                                                 | 478 ms: 1.82x faster                                                        |
| async_tree_io           | 1.77 sec                                               | 981 ms: 1.80x faster                                                        |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 633 ms: 1.61x faster                                                        |
| Geometric mean          | (ref)                                                  | 1.78x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240606-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5287d32 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.4 ms: 1.91x faster                                                       |
| float          | 117 ms                                                 | 73.6 ms: 1.59x faster                                                       |
| pidigits       | 191 ms                                                 | 189 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.45x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240606-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5287d32 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 139 ms: 1.36x faster                                                        |
| regex_v8       | 27.8 ms                                                | 25.9 ms: 1.07x faster                                                       |
| regex_dna      | 227 ms                                                 | 229 ms: 1.01x slower                                                        |
| regex_effbot   | 3.63 ms                                                | 4.00 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240606-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5287d32 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.95 sec: 1.61x faster                                                      |
| pickle_pure_python   | 484 us                                                 | 303 us: 1.60x faster                                                        |
| unpickle_pure_python | 331 us                                                 | 222 us: 1.49x faster                                                        |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                       |
| xml_etree_process    | 79.1 ms                                                | 58.1 ms: 1.36x faster                                                       |
| xml_etree_generate   | 99.4 ms                                                | 82.3 ms: 1.21x faster                                                       |
| xml_etree_iterparse  | 115 ms                                                 | 101 ms: 1.14x faster                                                        |
| xml_etree_parse      | 168 ms                                                 | 148 ms: 1.14x faster                                                        |
| json_loads           | 31.2 us                                                | 29.0 us: 1.08x faster                                                       |
| pickle_list          | 5.08 us                                                | 5.24 us: 1.03x slower                                                       |
| unpickle_list        | 5.20 us                                                | 5.41 us: 1.04x slower                                                       |
| unpickle             | 14.4 us                                                | 15.1 us: 1.05x slower                                                       |
| pickle               | 10.7 us                                                | 12.1 us: 1.14x slower                                                       |
| pickle_dict          | 29.6 us                                                | 35.7 us: 1.21x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240606-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5287d32 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.2 ms: 1.30x faster                                                       |
| python_startup_no_site | 5.93 ms                                                | 7.64 ms: 1.29x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.00x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240606-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5287d32 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.1 ms: 1.61x faster                                                       |
| django_template | 48.2 ms                                                | 36.6 ms: 1.32x faster                                                       |
| genshi_text     | 31.8 ms                                                | 25.2 ms: 1.26x faster                                                       |
| genshi_xml      | 66.0 ms                                                | 58.6 ms: 1.13x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.32x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240606-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5287d32 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 171 us: 3.19x faster                                                        |
| generators               | 80.1 ms                                                | 30.7 ms: 2.61x faster                                                       |
| deltablue                | 7.91 ms                                                | 3.71 ms: 2.13x faster                                                       |
| richards_super           | 94.7 ms                                                | 47.8 ms: 1.98x faster                                                       |
| chaos                    | 115 ms                                                 | 59.6 ms: 1.94x faster                                                       |
| async_tree_none          | 728 ms                                                 | 380 ms: 1.92x faster                                                        |
| nbody                    | 154 ms                                                 | 80.4 ms: 1.91x faster                                                       |
| richards                 | 79.3 ms                                                | 41.7 ms: 1.90x faster                                                       |
| crypto_pyaes             | 128 ms                                                 | 67.5 ms: 1.89x faster                                                       |
| scimark_monte_carlo      | 118 ms                                                 | 62.7 ms: 1.89x faster                                                       |
| async_tree_memoization   | 870 ms                                                 | 478 ms: 1.82x faster                                                        |
| raytrace                 | 507 ms                                                 | 279 ms: 1.81x faster                                                        |
| async_tree_io            | 1.77 sec                                               | 981 ms: 1.80x faster                                                        |
| asyncio_tcp              | 922 ms                                                 | 522 ms: 1.77x faster                                                        |
| logging_silent           | 190 ns                                                 | 108 ns: 1.75x faster                                                        |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                                       |
| spectral_norm            | 170 ms                                                 | 100 ms: 1.69x faster                                                        |
| scimark_sor              | 220 ms                                                 | 134 ms: 1.64x faster                                                        |
| sqlglot_parse            | 2.17 ms                                                | 1.32 ms: 1.64x faster                                                       |
| pyflate                  | 716 ms                                                 | 439 ms: 1.63x faster                                                        |
| go                       | 240 ms                                                 | 148 ms: 1.62x faster                                                        |
| mako                     | 16.3 ms                                                | 10.1 ms: 1.61x faster                                                       |
| tomli_loads              | 3.14 sec                                               | 1.95 sec: 1.61x faster                                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 633 ms: 1.61x faster                                                        |
| pickle_pure_python       | 484 us                                                 | 303 us: 1.60x faster                                                        |
| float                    | 117 ms                                                 | 73.6 ms: 1.59x faster                                                       |
| coroutines               | 35.1 ms                                                | 22.5 ms: 1.56x faster                                                       |
| sqlglot_transpile        | 2.57 ms                                                | 1.65 ms: 1.56x faster                                                       |
| hexiom                   | 10.4 ms                                                | 6.67 ms: 1.56x faster                                                       |
| pylint                   | 551 ms                                                 | 354 ms: 1.56x faster                                                        |
| deepcopy_memo            | 58.5 us                                                | 38.8 us: 1.51x faster                                                       |
| fannkuch                 | 532 ms                                                 | 354 ms: 1.50x faster                                                        |
| unpickle_pure_python     | 331 us                                                 | 222 us: 1.49x faster                                                        |
| scimark_fft              | 466 ms                                                 | 315 ms: 1.48x faster                                                        |
| logging_simple           | 8.30 us                                                | 5.62 us: 1.48x faster                                                       |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.39 ms: 1.48x faster                                                       |
| pprint_pformat           | 2.10 sec                                               | 1.44 sec: 1.46x faster                                                      |
| logging_format           | 9.09 us                                                | 6.30 us: 1.44x faster                                                       |
| pprint_safe_repr         | 1.02 sec                                               | 711 ms: 1.43x faster                                                        |
| scimark_lu               | 176 ms                                                 | 125 ms: 1.41x faster                                                        |
| tornado_http             | 136 ms                                                 | 98.7 ms: 1.38x faster                                                       |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.86 sec: 1.38x faster                                                      |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                       |
| xml_etree_process        | 79.1 ms                                                | 58.1 ms: 1.36x faster                                                       |
| regex_compile            | 188 ms                                                 | 139 ms: 1.36x faster                                                        |
| django_template          | 48.2 ms                                                | 36.6 ms: 1.32x faster                                                       |
| thrift                   | 1.07 ms                                                | 818 us: 1.31x faster                                                        |
| python_startup           | 14.6 ms                                                | 11.2 ms: 1.30x faster                                                       |
| pycparser                | 1.58 sec                                               | 1.22 sec: 1.29x faster                                                      |
| html5lib                 | 88.9 ms                                                | 68.8 ms: 1.29x faster                                                       |
| deepcopy                 | 479 us                                                 | 374 us: 1.28x faster                                                        |
| genshi_text              | 31.8 ms                                                | 25.2 ms: 1.26x faster                                                       |
| deepcopy_reduce          | 4.17 us                                                | 3.31 us: 1.26x faster                                                       |
| sqlglot_normalize        | 143 ms                                                 | 114 ms: 1.25x faster                                                        |
| pathlib                  | 20.5 ms                                                | 16.4 ms: 1.25x faster                                                       |
| 2to3                     | 348 ms                                                 | 280 ms: 1.25x faster                                                        |
| nqueens                  | 106 ms                                                 | 86.6 ms: 1.22x faster                                                       |
| dulwich_log              | 84.3 ms                                                | 69.5 ms: 1.21x faster                                                       |
| sqlglot_optimize         | 69.2 ms                                                | 57.2 ms: 1.21x faster                                                       |
| xml_etree_generate       | 99.4 ms                                                | 82.3 ms: 1.21x faster                                                       |
| dask                     | 441 ms                                                 | 379 ms: 1.16x faster                                                        |
| xml_etree_iterparse      | 115 ms                                                 | 101 ms: 1.14x faster                                                        |
| sympy_integrate          | 25.8 ms                                                | 22.6 ms: 1.14x faster                                                       |
| sympy_str                | 346 ms                                                 | 304 ms: 1.14x faster                                                        |
| xml_etree_parse          | 168 ms                                                 | 148 ms: 1.14x faster                                                        |
| sympy_sum                | 196 ms                                                 | 174 ms: 1.13x faster                                                        |
| genshi_xml               | 66.0 ms                                                | 58.6 ms: 1.13x faster                                                       |
| bench_thread_pool        | 986 us                                                 | 883 us: 1.12x faster                                                        |
| docutils                 | 3.30 sec                                               | 2.96 sec: 1.11x faster                                                      |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                        |
| sympy_expand             | 566 ms                                                 | 511 ms: 1.11x faster                                                        |
| mdp                      | 2.85 sec                                               | 2.65 sec: 1.08x faster                                                      |
| json_loads               | 31.2 us                                                | 29.0 us: 1.08x faster                                                       |
| regex_v8                 | 27.8 ms                                                | 25.9 ms: 1.07x faster                                                       |
| sqlite_synth             | 3.02 us                                                | 2.84 us: 1.06x faster                                                       |
| json                     | 5.69 ms                                                | 5.39 ms: 1.06x faster                                                       |
| pidigits                 | 191 ms                                                 | 189 ms: 1.01x faster                                                        |
| regex_dna                | 227 ms                                                 | 229 ms: 1.01x slower                                                        |
| asyncio_websockets       | 559 ms                                                 | 567 ms: 1.02x slower                                                        |
| pickle_list              | 5.08 us                                                | 5.24 us: 1.03x slower                                                       |
| unpickle_list            | 5.20 us                                                | 5.41 us: 1.04x slower                                                       |
| unpickle                 | 14.4 us                                                | 15.1 us: 1.05x slower                                                       |
| async_generators         | 444 ms                                                 | 468 ms: 1.06x slower                                                        |
| gc_traversal             | 3.62 ms                                                | 3.94 ms: 1.09x slower                                                       |
| regex_effbot             | 3.63 ms                                                | 4.00 ms: 1.10x slower                                                       |
| telco                    | 7.27 ms                                                | 8.04 ms: 1.11x slower                                                       |
| create_gc_cycles         | 1.62 ms                                                | 1.81 ms: 1.11x slower                                                       |
| pickle                   | 10.7 us                                                | 12.1 us: 1.14x slower                                                       |
| coverage                 | 79.4 ms                                                | 93.6 ms: 1.18x slower                                                       |
| pickle_dict              | 29.6 us                                                | 35.7 us: 1.21x slower                                                       |
| python_startup_no_site   | 5.93 ms                                                | 7.64 ms: 1.29x slower                                                       |
| Geometric mean           | (ref)                                                  | 1.34x faster                                                                |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240606-3.14.0a0-5287d32-JIT/bm-20240606-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5287d32.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.21x