# Results vs. 3.10.4

- fork: python
- ref: c419af9e277bea7dd78f
- machine: linux-x86_64
- commit hash: c419af9
- commit date: 2025-06-28
- overall geometric mean: 1.491x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.34x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 258 ms: 1.35x faster                                                  |
| docutils       | 3.30 sec                                               | 2.62 sec: 1.26x faster                                                |
| html5lib       | 88.9 ms                                                | 61.3 ms: 1.45x faster                                                 |
| Geometric mean | (ref)                                                  | 1.35x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 604 ms: 2.93x faster                                                  |
| async_tree_none         | 728 ms                                                 | 261 ms: 2.79x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 314 ms: 2.77x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 499 ms: 2.04x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.61x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 117 ms                                                 | 65.3 ms: 1.79x faster                                                 |
| nbody          | 154 ms                                                 | 93.4 ms: 1.64x faster                                                 |
| pidigits       | 191 ms                                                 | 188 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.44x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 126 ms: 1.50x faster                                                  |
| regex_v8       | 27.8 ms                                                | 21.9 ms: 1.27x faster                                                 |
| regex_effbot   | 3.63 ms                                                | 3.18 ms: 1.14x faster                                                 |
| regex_dna      | 227 ms                                                 | 202 ms: 1.12x faster                                                  |
| Geometric mean | (ref)                                                  | 1.25x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.81 sec: 1.73x faster                                                |
| unpickle_pure_python | 331 us                                                 | 193 us: 1.72x faster                                                  |
| pickle_pure_python   | 484 us                                                 | 318 us: 1.52x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 55.6 ms: 1.42x faster                                                 |
| json_dumps           | 14.2 ms                                                | 11.0 ms: 1.29x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 79.6 ms: 1.25x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 98.2 ms: 1.18x faster                                                 |
| json_loads           | 31.2 us                                                | 28.1 us: 1.11x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.36x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.2 ms: 1.20x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 6.94 ms: 1.17x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.5 ms: 1.56x faster                                                 |
| genshi_text     | 31.8 ms                                                | 21.4 ms: 1.49x faster                                                 |
| django_template | 48.2 ms                                                | 32.5 ms: 1.48x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 50.1 ms: 1.32x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.46x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 170 us: 3.20x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 604 ms: 2.93x faster                                                  |
| async_tree_none          | 728 ms                                                 | 261 ms: 2.79x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 314 ms: 2.77x faster                                                  |
| generators               | 80.1 ms                                                | 30.2 ms: 2.65x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.05 ms: 2.60x faster                                                 |
| richards_super           | 94.7 ms                                                | 37.9 ms: 2.50x faster                                                 |
| richards                 | 79.3 ms                                                | 32.2 ms: 2.46x faster                                                 |
| mdp                      | 2.85 sec                                               | 1.23 sec: 2.31x faster                                                |
| go                       | 240 ms                                                 | 115 ms: 2.09x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 499 ms: 2.04x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 29.5 us: 1.98x faster                                                 |
| pylint                   | 551 ms                                                 | 281 ms: 1.96x faster                                                  |
| chaos                    | 115 ms                                                 | 60.1 ms: 1.92x faster                                                 |
| logging_silent           | 190 ns                                                 | 101 ns: 1.88x faster                                                  |
| raytrace                 | 507 ms                                                 | 271 ms: 1.87x faster                                                  |
| deepcopy                 | 479 us                                                 | 258 us: 1.86x faster                                                  |
| spectral_norm            | 170 ms                                                 | 92.2 ms: 1.84x faster                                                 |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.84x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 65.2 ms: 1.81x faster                                                 |
| float                    | 117 ms                                                 | 65.3 ms: 1.79x faster                                                 |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.74x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 1.81 sec: 1.73x faster                                                |
| djangocms                | 38.4 us                                                | 22.3 us: 1.72x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 193 us: 1.72x faster                                                  |
| pyflate                  | 716 ms                                                 | 418 ms: 1.71x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 75.5 ms: 1.69x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.24 ms: 1.67x faster                                                 |
| nbody                    | 154 ms                                                 | 93.4 ms: 1.64x faster                                                 |
| mako                     | 16.3 ms                                                | 10.5 ms: 1.56x faster                                                 |
| deepcopy_reduce          | 4.17 us                                                | 2.68 us: 1.56x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 318 us: 1.52x faster                                                  |
| scimark_fft              | 466 ms                                                 | 311 ms: 1.50x faster                                                  |
| regex_compile            | 188 ms                                                 | 126 ms: 1.50x faster                                                  |
| scimark_lu               | 176 ms                                                 | 118 ms: 1.49x faster                                                  |
| genshi_text              | 31.8 ms                                                | 21.4 ms: 1.49x faster                                                 |
| django_template          | 48.2 ms                                                | 32.5 ms: 1.48x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.61 us: 1.48x faster                                                 |
| logging_format           | 9.09 us                                                | 6.24 us: 1.46x faster                                                 |
| html5lib                 | 88.9 ms                                                | 61.3 ms: 1.45x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 712 ms: 1.43x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.11 sec: 1.42x faster                                                |
| xml_etree_process        | 79.1 ms                                                | 55.6 ms: 1.42x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 59.3 ms: 1.42x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.50 sec: 1.40x faster                                                |
| coroutines               | 35.1 ms                                                | 25.0 ms: 1.40x faster                                                 |
| thrift                   | 1.07 ms                                                | 774 us: 1.38x faster                                                  |
| 2to3                     | 348 ms                                                 | 258 ms: 1.35x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 19.2 ms: 1.34x faster                                                 |
| fannkuch                 | 532 ms                                                 | 400 ms: 1.33x faster                                                  |
| sympy_sum                | 196 ms                                                 | 149 ms: 1.32x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.90 ms: 1.32x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 50.1 ms: 1.32x faster                                                 |
| nqueens                  | 106 ms                                                 | 82.1 ms: 1.29x faster                                                 |
| json_dumps               | 14.2 ms                                                | 11.0 ms: 1.29x faster                                                 |
| sympy_str                | 346 ms                                                 | 271 ms: 1.27x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 21.9 ms: 1.27x faster                                                 |
| docutils                 | 3.30 sec                                               | 2.62 sec: 1.26x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 79.6 ms: 1.25x faster                                                 |
| sympy_expand             | 566 ms                                                 | 466 ms: 1.22x faster                                                  |
| python_startup           | 14.6 ms                                                | 12.2 ms: 1.20x faster                                                 |
| pathlib                  | 20.5 ms                                                | 17.2 ms: 1.19x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 98.2 ms: 1.18x faster                                                 |
| regex_effbot             | 3.63 ms                                                | 3.18 ms: 1.14x faster                                                 |
| regex_dna                | 227 ms                                                 | 202 ms: 1.12x faster                                                  |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.11x faster                                                  |
| json_loads               | 31.2 us                                                | 28.1 us: 1.11x faster                                                 |
| json                     | 5.69 ms                                                | 5.17 ms: 1.10x faster                                                 |
| sqlite_synth             | 3.02 us                                                | 2.79 us: 1.09x faster                                                 |
| async_generators         | 444 ms                                                 | 432 ms: 1.03x faster                                                  |
| pidigits                 | 191 ms                                                 | 188 ms: 1.01x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 554 ms: 1.01x faster                                                  |
| telco                    | 7.27 ms                                                | 7.65 ms: 1.05x slower                                                 |
| coverage                 | 79.4 ms                                                | 87.2 ms: 1.10x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 6.94 ms: 1.17x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 4.96 ms: 1.37x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 2.59 ms: 1.60x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.49x faster                                                          |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250628-3.15.0a0-c419af9-JIT/bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.491x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.40x
- 95% likely to have a speedup of 1.38x
- 99% likely to have a speedup of 1.34x

# Memory
- memory change: 1.33x