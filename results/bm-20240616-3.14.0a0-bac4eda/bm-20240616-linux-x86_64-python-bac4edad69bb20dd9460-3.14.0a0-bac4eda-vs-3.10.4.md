# Results vs. 3.10.4

- fork: python
- ref: bac4edad69bb20dd9460
- machine: linux-x86_64
- commit hash: bac4eda
- commit date: 2024-06-16
- overall geometric mean: 1.385x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.25x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240616-linux-x86_64-python-bac4edad69bb20dd9460-3.14.0a0-bac4eda |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 266 ms: 1.31x faster                                                  |
| docutils       | 3.30 sec                                               | 2.72 sec: 1.21x faster                                                |
| html5lib       | 88.9 ms                                                | 66.4 ms: 1.34x faster                                                 |
| tornado_http   | 136 ms                                                 | 92.1 ms: 1.48x faster                                                 |
| Geometric mean | (ref)                                                  | 1.33x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240616-linux-x86_64-python-bac4edad69bb20dd9460-3.14.0a0-bac4eda |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 362 ms: 2.01x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 458 ms: 1.90x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 952 ms: 1.86x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 603 ms: 1.68x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.86x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240616-linux-x86_64-python-bac4edad69bb20dd9460-3.14.0a0-bac4eda |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 87.0 ms: 1.77x faster                                                 |
| float          | 117 ms                                                 | 77.7 ms: 1.51x faster                                                 |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.39x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240616-linux-x86_64-python-bac4edad69bb20dd9460-3.14.0a0-bac4eda |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 132 ms: 1.43x faster                                                  |
| regex_v8       | 27.8 ms                                                | 23.1 ms: 1.20x faster                                                 |
| regex_dna      | 227 ms                                                 | 218 ms: 1.04x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.50 ms: 1.04x faster                                                 |
| Geometric mean | (ref)                                                  | 1.17x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240616-linux-x86_64-python-bac4edad69bb20dd9460-3.14.0a0-bac4eda |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 302 us: 1.60x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                                  |
| tomli_loads          | 3.14 sec                                               | 2.13 sec: 1.47x faster                                                |
| json_dumps           | 14.2 ms                                                | 10.6 ms: 1.33x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 59.4 ms: 1.33x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 85.3 ms: 1.17x faster                                                 |
| json_loads           | 31.2 us                                                | 28.0 us: 1.11x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 107 ms: 1.08x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 160 ms: 1.05x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.28x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240616-linux-x86_64-python-bac4edad69bb20dd9460-3.14.0a0-bac4eda |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 14.4 ms: 1.01x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.01 ms: 1.18x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240616-linux-x86_64-python-bac4edad69bb20dd9460-3.14.0a0-bac4eda |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.3 ms: 1.49x faster                                                 |
| mako            | 16.3 ms                                                | 11.1 ms: 1.47x faster                                                 |
| genshi_text     | 31.8 ms                                                | 23.2 ms: 1.37x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 51.2 ms: 1.29x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240616-linux-x86_64-python-bac4edad69bb20dd9460-3.14.0a0-bac4eda |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 164 us: 3.32x faster                                                  |
| generators               | 80.1 ms                                                | 28.9 ms: 2.77x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.22 ms: 2.46x faster                                                 |
| async_tree_none          | 728 ms                                                 | 362 ms: 2.01x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 29.5 us: 1.98x faster                                                 |
| chaos                    | 115 ms                                                 | 58.7 ms: 1.97x faster                                                 |
| raytrace                 | 507 ms                                                 | 263 ms: 1.93x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 458 ms: 1.90x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 952 ms: 1.86x faster                                                  |
| deepcopy                 | 479 us                                                 | 260 us: 1.84x faster                                                  |
| logging_silent           | 190 ns                                                 | 105 ns: 1.80x faster                                                  |
| pylint                   | 551 ms                                                 | 308 ms: 1.79x faster                                                  |
| nbody                    | 154 ms                                                 | 87.0 ms: 1.77x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 72.6 ms: 1.76x faster                                                 |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.73x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 68.5 ms: 1.72x faster                                                 |
| djangocms                | 38.4 us                                                | 22.5 us: 1.71x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.14 ms: 1.69x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 603 ms: 1.68x faster                                                  |
| go                       | 240 ms                                                 | 143 ms: 1.68x faster                                                  |
| richards_super           | 94.7 ms                                                | 57.0 ms: 1.66x faster                                                 |
| scimark_sor              | 220 ms                                                 | 134 ms: 1.64x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 302 us: 1.60x faster                                                  |
| richards                 | 79.3 ms                                                | 49.9 ms: 1.59x faster                                                 |
| scimark_lu               | 176 ms                                                 | 113 ms: 1.55x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.69 us: 1.55x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                                  |
| spectral_norm            | 170 ms                                                 | 112 ms: 1.51x faster                                                  |
| float                    | 117 ms                                                 | 77.7 ms: 1.51x faster                                                 |
| pyflate                  | 716 ms                                                 | 480 ms: 1.49x faster                                                  |
| django_template          | 48.2 ms                                                | 32.3 ms: 1.49x faster                                                 |
| tornado_http             | 136 ms                                                 | 92.1 ms: 1.48x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 2.13 sec: 1.47x faster                                                |
| mako                     | 16.3 ms                                                | 11.1 ms: 1.47x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.77 us: 1.44x faster                                                 |
| coroutines               | 35.1 ms                                                | 24.4 ms: 1.44x faster                                                 |
| logging_format           | 9.09 us                                                | 6.33 us: 1.44x faster                                                 |
| regex_compile            | 188 ms                                                 | 132 ms: 1.43x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.51 sec: 1.39x faster                                                |
| pprint_safe_repr         | 1.02 sec                                               | 737 ms: 1.38x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.37x faster                                                |
| genshi_text              | 31.8 ms                                                | 23.2 ms: 1.37x faster                                                 |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.3 ms: 1.35x faster                                                 |
| thrift                   | 1.07 ms                                                | 797 us: 1.35x faster                                                  |
| nqueens                  | 106 ms                                                 | 78.7 ms: 1.34x faster                                                 |
| html5lib                 | 88.9 ms                                                | 66.4 ms: 1.34x faster                                                 |
| json_dumps               | 14.2 ms                                                | 10.6 ms: 1.33x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 59.4 ms: 1.33x faster                                                 |
| 2to3                     | 348 ms                                                 | 266 ms: 1.31x faster                                                  |
| sympy_sum                | 196 ms                                                 | 151 ms: 1.30x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 65.2 ms: 1.29x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 51.2 ms: 1.29x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 20.1 ms: 1.29x faster                                                 |
| fannkuch                 | 532 ms                                                 | 414 ms: 1.28x faster                                                  |
| scimark_fft              | 466 ms                                                 | 365 ms: 1.28x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.09 ms: 1.27x faster                                                 |
| sqlalchemy_declarative   | 172 ms                                                 | 136 ms: 1.27x faster                                                  |
| sympy_str                | 346 ms                                                 | 276 ms: 1.26x faster                                                  |
| pathlib                  | 20.5 ms                                                | 16.3 ms: 1.25x faster                                                 |
| docutils                 | 3.30 sec                                               | 2.72 sec: 1.21x faster                                                |
| sympy_expand             | 566 ms                                                 | 470 ms: 1.20x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 23.1 ms: 1.20x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 825 us: 1.20x faster                                                  |
| xml_etree_generate       | 99.4 ms                                                | 85.3 ms: 1.17x faster                                                 |
| mdp                      | 2.85 sec                                               | 2.52 sec: 1.13x faster                                                |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                  |
| json_loads               | 31.2 us                                                | 28.0 us: 1.11x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 107 ms: 1.08x faster                                                  |
| json                     | 5.69 ms                                                | 5.31 ms: 1.07x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 160 ms: 1.05x faster                                                  |
| regex_dna                | 227 ms                                                 | 218 ms: 1.04x faster                                                  |
| regex_effbot             | 3.63 ms                                                | 3.50 ms: 1.04x faster                                                 |
| sqlite_synth             | 3.02 us                                                | 2.93 us: 1.03x faster                                                 |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                  |
| async_generators         | 444 ms                                                 | 436 ms: 1.02x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                  |
| python_startup           | 14.6 ms                                                | 14.4 ms: 1.01x faster                                                 |
| coverage                 | 79.4 ms                                                | 91.5 ms: 1.15x slower                                                 |
| telco                    | 7.27 ms                                                | 8.48 ms: 1.17x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.01 ms: 1.18x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 4.49 ms: 1.24x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 2.66 ms: 1.64x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.38x faster                                                          |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20240616-3.14.0a0-bac4eda/bm-20240616-linux-x86_64-python-bac4edad69bb20dd9460-3.14.0a0-bac4eda.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.385x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.25x