# Results vs. 3.10.4

- fork: python
- ref: e0bc9d2a0c448cf46df2
- machine: linux-x86_64
- commit hash: e0bc9d2
- commit date: 2025-03-11
- overall geometric mean: 1.450x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250311-linux-x86_64-python-e0bc9d2a0c448cf46df2-3.14.0a5+-e0bc9d2 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 260 ms: 1.34x faster                                                   |
| docutils       | 3.30 sec                                               | 2.69 sec: 1.23x faster                                                 |
| html5lib       | 88.9 ms                                                | 61.6 ms: 1.44x faster                                                  |
| Geometric mean | (ref)                                                  | 1.33x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250311-linux-x86_64-python-e0bc9d2a0c448cf46df2-3.14.0a5+-e0bc9d2 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 612 ms: 2.89x faster                                                   |
| async_tree_none         | 728 ms                                                 | 259 ms: 2.81x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 319 ms: 2.73x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 492 ms: 2.07x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.60x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250311-linux-x86_64-python-e0bc9d2a0c448cf46df2-3.14.0a5+-e0bc9d2 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 117 ms                                                 | 64.6 ms: 1.81x faster                                                  |
| nbody          | 154 ms                                                 | 87.5 ms: 1.75x faster                                                  |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                  | 1.48x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250311-linux-x86_64-python-e0bc9d2a0c448cf46df2-3.14.0a5+-e0bc9d2 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 126 ms: 1.49x faster                                                   |
| regex_v8       | 27.8 ms                                                | 23.5 ms: 1.18x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.50 ms: 1.04x faster                                                  |
| regex_dna      | 227 ms                                                 | 225 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.17x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250311-linux-x86_64-python-e0bc9d2a0c448cf46df2-3.14.0a5+-e0bc9d2 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.83 sec: 1.71x faster                                                 |
| unpickle_pure_python | 331 us                                                 | 212 us: 1.56x faster                                                   |
| pickle_pure_python   | 484 us                                                 | 319 us: 1.52x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 55.2 ms: 1.43x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 79.0 ms: 1.26x faster                                                  |
| json_dumps           | 14.2 ms                                                | 11.4 ms: 1.25x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 139 ms: 1.21x faster                                                   |
| xml_etree_iterparse  | 115 ms                                                 | 97.6 ms: 1.18x faster                                                  |
| json_loads           | 31.2 us                                                | 29.8 us: 1.05x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.34x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250311-linux-x86_64-python-e0bc9d2a0c448cf46df2-3.14.0a5+-e0bc9d2 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.11x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 8.21 ms: 1.38x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250311-linux-x86_64-python-e0bc9d2a0c448cf46df2-3.14.0a5+-e0bc9d2 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.2 ms: 1.55x faster                                                  |
| genshi_text     | 31.8 ms                                                | 21.4 ms: 1.49x faster                                                  |
| mako            | 16.3 ms                                                | 11.0 ms: 1.49x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 49.8 ms: 1.33x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.46x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250311-linux-x86_64-python-e0bc9d2a0c448cf46df2-3.14.0a5+-e0bc9d2 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 166 us: 3.29x faster                                                   |
| generators               | 80.1 ms                                                | 27.5 ms: 2.91x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 612 ms: 2.89x faster                                                   |
| async_tree_none          | 728 ms                                                 | 259 ms: 2.81x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 319 ms: 2.73x faster                                                   |
| deltablue                | 7.91 ms                                                | 3.02 ms: 2.62x faster                                                  |
| richards_super           | 94.7 ms                                                | 40.8 ms: 2.32x faster                                                  |
| richards                 | 79.3 ms                                                | 35.5 ms: 2.23x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 492 ms: 2.07x faster                                                   |
| logging_silent           | 190 ns                                                 | 94.7 ns: 2.00x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 29.5 us: 1.98x faster                                                  |
| pylint                   | 551 ms                                                 | 280 ms: 1.97x faster                                                   |
| chaos                    | 115 ms                                                 | 58.9 ms: 1.96x faster                                                  |
| raytrace                 | 507 ms                                                 | 266 ms: 1.90x faster                                                   |
| go                       | 240 ms                                                 | 127 ms: 1.89x faster                                                   |
| deepcopy                 | 479 us                                                 | 256 us: 1.87x faster                                                   |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.85x faster                                                   |
| spectral_norm            | 170 ms                                                 | 93.2 ms: 1.82x faster                                                  |
| float                    | 117 ms                                                 | 64.6 ms: 1.81x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 67.2 ms: 1.76x faster                                                  |
| nbody                    | 154 ms                                                 | 87.5 ms: 1.75x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 1.83 sec: 1.71x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 79.3 ms: 1.61x faster                                                  |
| pyflate                  | 716 ms                                                 | 447 ms: 1.60x faster                                                   |
| deepcopy_reduce          | 4.17 us                                                | 2.65 us: 1.57x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.64 ms: 1.57x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 212 us: 1.56x faster                                                   |
| django_template          | 48.2 ms                                                | 31.2 ms: 1.55x faster                                                  |
| comprehensions           | 28.8 us                                                | 18.8 us: 1.53x faster                                                  |
| scimark_lu               | 176 ms                                                 | 115 ms: 1.53x faster                                                   |
| pickle_pure_python       | 484 us                                                 | 319 us: 1.52x faster                                                   |
| scimark_fft              | 466 ms                                                 | 308 ms: 1.51x faster                                                   |
| regex_compile            | 188 ms                                                 | 126 ms: 1.49x faster                                                   |
| coroutines               | 35.1 ms                                                | 23.5 ms: 1.49x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.58 us: 1.49x faster                                                  |
| genshi_text              | 31.8 ms                                                | 21.4 ms: 1.49x faster                                                  |
| mako                     | 16.3 ms                                                | 11.0 ms: 1.49x faster                                                  |
| logging_format           | 9.09 us                                                | 6.17 us: 1.47x faster                                                  |
| html5lib                 | 88.9 ms                                                | 61.6 ms: 1.44x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 55.2 ms: 1.43x faster                                                  |
| thrift                   | 1.07 ms                                                | 770 us: 1.39x faster                                                   |
| dulwich_log              | 84.3 ms                                                | 60.7 ms: 1.39x faster                                                  |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.9 ms: 1.38x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.70 ms: 1.38x faster                                                  |
| pprint_safe_repr         | 1.02 sec                                               | 745 ms: 1.37x faster                                                   |
| pprint_pformat           | 2.10 sec                                               | 1.54 sec: 1.36x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.35x faster                                                 |
| 2to3                     | 348 ms                                                 | 260 ms: 1.34x faster                                                   |
| genshi_xml               | 66.0 ms                                                | 49.8 ms: 1.33x faster                                                  |
| sqlalchemy_declarative   | 172 ms                                                 | 132 ms: 1.31x faster                                                   |
| sympy_sum                | 196 ms                                                 | 151 ms: 1.30x faster                                                   |
| sympy_integrate          | 25.8 ms                                                | 20.2 ms: 1.28x faster                                                  |
| sympy_str                | 346 ms                                                 | 273 ms: 1.27x faster                                                   |
| nqueens                  | 106 ms                                                 | 83.6 ms: 1.27x faster                                                  |
| fannkuch                 | 532 ms                                                 | 421 ms: 1.26x faster                                                   |
| xml_etree_generate       | 99.4 ms                                                | 79.0 ms: 1.26x faster                                                  |
| pathlib                  | 20.5 ms                                                | 16.3 ms: 1.25x faster                                                  |
| json_dumps               | 14.2 ms                                                | 11.4 ms: 1.25x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.69 sec: 1.23x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 139 ms: 1.21x faster                                                   |
| sympy_expand             | 566 ms                                                 | 469 ms: 1.21x faster                                                   |
| xml_etree_iterparse      | 115 ms                                                 | 97.6 ms: 1.18x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 23.5 ms: 1.18x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.46 sec: 1.16x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 876 us: 1.13x faster                                                   |
| sqlite_synth             | 3.02 us                                                | 2.72 us: 1.11x faster                                                  |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.11x faster                                                  |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                                   |
| async_generators         | 444 ms                                                 | 411 ms: 1.08x faster                                                   |
| json                     | 5.69 ms                                                | 5.33 ms: 1.07x faster                                                  |
| json_loads               | 31.2 us                                                | 29.8 us: 1.05x faster                                                  |
| regex_effbot             | 3.63 ms                                                | 3.50 ms: 1.04x faster                                                  |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                   |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                   |
| regex_dna                | 227 ms                                                 | 225 ms: 1.01x faster                                                   |
| coverage                 | 79.4 ms                                                | 85.4 ms: 1.07x slower                                                  |
| telco                    | 7.27 ms                                                | 7.92 ms: 1.09x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 8.21 ms: 1.38x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 5.05 ms: 1.39x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 2.49 ms: 1.54x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 83.2 ms: 3.47x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                           |
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250311-3.14.0a5+-e0bc9d2-JIT/bm-20250311-linux-x86_64-python-e0bc9d2a0c448cf46df2-3.14.0a5+-e0bc9d2.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.450x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.29x