# Results vs. 3.10.4

- fork: tomasr8
- ref: jit_contains_op_set_
- machine: linux-x86_64
- commit hash: 52c1a54
- commit date: 2025-04-03
- overall geometric mean: 1.465x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.33x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-tomasr8-jit_contains_op_set_-3.14.0a6+-52c1a54 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 253 ms: 1.37x faster                                                    |
| docutils       | 3.30 sec                                               | 2.67 sec: 1.23x faster                                                  |
| html5lib       | 88.9 ms                                                | 61.9 ms: 1.44x faster                                                   |
| Geometric mean | (ref)                                                  | 1.35x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-tomasr8-jit_contains_op_set_-3.14.0a6+-52c1a54 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 608 ms: 2.91x faster                                                    |
| async_tree_memoization  | 870 ms                                                 | 311 ms: 2.80x faster                                                    |
| async_tree_none         | 728 ms                                                 | 262 ms: 2.78x faster                                                    |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 477 ms: 2.13x faster                                                    |
| Geometric mean          | (ref)                                                  | 2.63x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-tomasr8-jit_contains_op_set_-3.14.0a6+-52c1a54 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 117 ms                                                 | 64.8 ms: 1.81x faster                                                   |
| nbody          | 154 ms                                                 | 89.2 ms: 1.72x faster                                                   |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                  | 1.47x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-tomasr8-jit_contains_op_set_-3.14.0a6+-52c1a54 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 126 ms: 1.50x faster                                                    |
| regex_v8       | 27.8 ms                                                | 24.0 ms: 1.16x faster                                                   |
| regex_effbot   | 3.63 ms                                                | 3.36 ms: 1.08x faster                                                   |
| regex_dna      | 227 ms                                                 | 216 ms: 1.05x faster                                                    |
| Geometric mean | (ref)                                                  | 1.18x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-tomasr8-jit_contains_op_set_-3.14.0a6+-52c1a54 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.85 sec: 1.70x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 213 us: 1.55x faster                                                    |
| pickle_pure_python   | 484 us                                                 | 324 us: 1.49x faster                                                    |
| xml_etree_process    | 79.1 ms                                                | 55.4 ms: 1.43x faster                                                   |
| xml_etree_generate   | 99.4 ms                                                | 79.6 ms: 1.25x faster                                                   |
| json_dumps           | 14.2 ms                                                | 11.6 ms: 1.22x faster                                                   |
| xml_etree_parse      | 168 ms                                                 | 140 ms: 1.20x faster                                                    |
| xml_etree_iterparse  | 115 ms                                                 | 97.2 ms: 1.19x faster                                                   |
| json_loads           | 31.2 us                                                | 29.6 us: 1.06x faster                                                   |
| Geometric mean       | (ref)                                                  | 1.33x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-tomasr8-jit_contains_op_set_-3.14.0a6+-52c1a54 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.2 ms: 1.11x faster                                                   |
| python_startup_no_site | 5.93 ms                                                | 8.20 ms: 1.38x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-tomasr8-jit_contains_op_set_-3.14.0a6+-52c1a54 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.9 ms: 1.51x faster                                                   |
| genshi_text     | 31.8 ms                                                | 21.2 ms: 1.50x faster                                                   |
| mako            | 16.3 ms                                                | 10.9 ms: 1.50x faster                                                   |
| genshi_xml      | 66.0 ms                                                | 48.8 ms: 1.35x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.46x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-tomasr8-jit_contains_op_set_-3.14.0a6+-52c1a54 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 164 us: 3.31x faster                                                    |
| async_tree_io            | 1.77 sec                                               | 608 ms: 2.91x faster                                                    |
| async_tree_memoization   | 870 ms                                                 | 311 ms: 2.80x faster                                                    |
| async_tree_none          | 728 ms                                                 | 262 ms: 2.78x faster                                                    |
| generators               | 80.1 ms                                                | 29.6 ms: 2.70x faster                                                   |
| deltablue                | 7.91 ms                                                | 3.02 ms: 2.62x faster                                                   |
| mdp                      | 2.85 sec                                               | 1.21 sec: 2.35x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 477 ms: 2.13x faster                                                    |
| richards_super           | 94.7 ms                                                | 45.3 ms: 2.09x faster                                                   |
| richards                 | 79.3 ms                                                | 38.4 ms: 2.07x faster                                                   |
| deepcopy_memo            | 58.5 us                                                | 28.6 us: 2.04x faster                                                   |
| chaos                    | 115 ms                                                 | 56.9 ms: 2.03x faster                                                   |
| pylint                   | 551 ms                                                 | 280 ms: 1.97x faster                                                    |
| go                       | 240 ms                                                 | 122 ms: 1.97x faster                                                    |
| logging_silent           | 190 ns                                                 | 97.5 ns: 1.95x faster                                                   |
| raytrace                 | 507 ms                                                 | 261 ms: 1.94x faster                                                    |
| deepcopy                 | 479 us                                                 | 250 us: 1.92x faster                                                    |
| scimark_sor              | 220 ms                                                 | 116 ms: 1.89x faster                                                    |
| float                    | 117 ms                                                 | 64.8 ms: 1.81x faster                                                   |
| scimark_monte_carlo      | 118 ms                                                 | 66.4 ms: 1.78x faster                                                   |
| nbody                    | 154 ms                                                 | 89.2 ms: 1.72x faster                                                   |
| crypto_pyaes             | 128 ms                                                 | 75.2 ms: 1.70x faster                                                   |
| tomli_loads              | 3.14 sec                                               | 1.85 sec: 1.70x faster                                                  |
| spectral_norm            | 170 ms                                                 | 101 ms: 1.68x faster                                                    |
| pyflate                  | 716 ms                                                 | 432 ms: 1.66x faster                                                    |
| deepcopy_reduce          | 4.17 us                                                | 2.64 us: 1.58x faster                                                   |
| comprehensions           | 28.8 us                                                | 18.3 us: 1.57x faster                                                   |
| unpickle_pure_python     | 331 us                                                 | 213 us: 1.55x faster                                                    |
| hexiom                   | 10.4 ms                                                | 6.71 ms: 1.55x faster                                                   |
| scimark_lu               | 176 ms                                                 | 115 ms: 1.53x faster                                                    |
| scimark_fft              | 466 ms                                                 | 307 ms: 1.52x faster                                                    |
| django_template          | 48.2 ms                                                | 31.9 ms: 1.51x faster                                                   |
| genshi_text              | 31.8 ms                                                | 21.2 ms: 1.50x faster                                                   |
| regex_compile            | 188 ms                                                 | 126 ms: 1.50x faster                                                    |
| mako                     | 16.3 ms                                                | 10.9 ms: 1.50x faster                                                   |
| pickle_pure_python       | 484 us                                                 | 324 us: 1.49x faster                                                    |
| logging_simple           | 8.30 us                                                | 5.71 us: 1.46x faster                                                   |
| coroutines               | 35.1 ms                                                | 24.3 ms: 1.44x faster                                                   |
| html5lib                 | 88.9 ms                                                | 61.9 ms: 1.44x faster                                                   |
| logging_format           | 9.09 us                                                | 6.33 us: 1.44x faster                                                   |
| xml_etree_process        | 79.1 ms                                                | 55.4 ms: 1.43x faster                                                   |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.58 ms: 1.41x faster                                                   |
| dulwich_log              | 84.3 ms                                                | 60.8 ms: 1.39x faster                                                   |
| pprint_safe_repr         | 1.02 sec                                               | 735 ms: 1.39x faster                                                    |
| pprint_pformat           | 2.10 sec                                               | 1.52 sec: 1.38x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.14 sec: 1.38x faster                                                  |
| 2to3                     | 348 ms                                                 | 253 ms: 1.37x faster                                                    |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.2 ms: 1.35x faster                                                   |
| genshi_xml               | 66.0 ms                                                | 48.8 ms: 1.35x faster                                                   |
| sympy_integrate          | 25.8 ms                                                | 19.6 ms: 1.32x faster                                                   |
| sympy_sum                | 196 ms                                                 | 151 ms: 1.30x faster                                                    |
| sqlalchemy_declarative   | 172 ms                                                 | 133 ms: 1.30x faster                                                    |
| fannkuch                 | 532 ms                                                 | 414 ms: 1.29x faster                                                    |
| sympy_str                | 346 ms                                                 | 272 ms: 1.27x faster                                                    |
| nqueens                  | 106 ms                                                 | 83.2 ms: 1.27x faster                                                   |
| xml_etree_generate       | 99.4 ms                                                | 79.6 ms: 1.25x faster                                                   |
| docutils                 | 3.30 sec                                               | 2.67 sec: 1.23x faster                                                  |
| json_dumps               | 14.2 ms                                                | 11.6 ms: 1.22x faster                                                   |
| xml_etree_parse          | 168 ms                                                 | 140 ms: 1.20x faster                                                    |
| sympy_expand             | 566 ms                                                 | 472 ms: 1.20x faster                                                    |
| pathlib                  | 20.5 ms                                                | 17.1 ms: 1.20x faster                                                   |
| xml_etree_iterparse      | 115 ms                                                 | 97.2 ms: 1.19x faster                                                   |
| regex_v8                 | 27.8 ms                                                | 24.0 ms: 1.16x faster                                                   |
| bench_thread_pool        | 986 us                                                 | 885 us: 1.11x faster                                                    |
| python_startup           | 14.6 ms                                                | 13.2 ms: 1.11x faster                                                   |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                    |
| sqlite_synth             | 3.02 us                                                | 2.74 us: 1.10x faster                                                   |
| regex_effbot             | 3.63 ms                                                | 3.36 ms: 1.08x faster                                                   |
| json                     | 5.69 ms                                                | 5.31 ms: 1.07x faster                                                   |
| async_generators         | 444 ms                                                 | 417 ms: 1.06x faster                                                    |
| json_loads               | 31.2 us                                                | 29.6 us: 1.06x faster                                                   |
| regex_dna                | 227 ms                                                 | 216 ms: 1.05x faster                                                    |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                    |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                    |
| telco                    | 7.27 ms                                                | 7.82 ms: 1.08x slower                                                   |
| coverage                 | 79.4 ms                                                | 88.4 ms: 1.11x slower                                                   |
| gc_traversal             | 3.62 ms                                                | 4.76 ms: 1.31x slower                                                   |
| python_startup_no_site   | 5.93 ms                                                | 8.20 ms: 1.38x slower                                                   |
| create_gc_cycles         | 1.62 ms                                                | 2.44 ms: 1.51x slower                                                   |
| bench_mp_pool            | 24.0 ms                                                | 82.3 ms: 3.43x slower                                                   |
| Geometric mean           | (ref)                                                  | 1.44x faster                                                            |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250403-3.14.0a6+-52c1a54-JIT/bm-20250403-linux-x86_64-tomasr8-jit_contains_op_set_-3.14.0a6+-52c1a54.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.465x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.37x
- 95% likely to have a speedup of 1.36x
- 99% likely to have a speedup of 1.33x

# Memory
- memory change: 1.29x