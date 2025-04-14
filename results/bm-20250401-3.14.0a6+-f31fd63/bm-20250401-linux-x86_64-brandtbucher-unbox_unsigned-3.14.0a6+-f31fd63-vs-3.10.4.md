# Results vs. 3.10.4

- fork: brandtbucher
- ref: unbox_unsigned
- machine: linux-x86_64
- commit hash: f31fd63
- commit date: 2025-04-01
- overall geometric mean: 1.413x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250401-linux-x86_64-brandtbucher-unbox_unsigned-3.14.0a6+-f31fd63 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 264 ms: 1.32x faster                                                   |
| docutils       | 3.30 sec                                               | 2.65 sec: 1.24x faster                                                 |
| html5lib       | 88.9 ms                                                | 63.8 ms: 1.39x faster                                                  |
| Geometric mean | (ref)                                                  | 1.32x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250401-linux-x86_64-brandtbucher-unbox_unsigned-3.14.0a6+-f31fd63 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 631 ms: 2.80x faster                                                   |
| async_tree_none         | 728 ms                                                 | 266 ms: 2.74x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 322 ms: 2.70x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 494 ms: 2.06x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.55x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250401-linux-x86_64-brandtbucher-unbox_unsigned-3.14.0a6+-f31fd63 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 98.1 ms: 1.56x faster                                                  |
| float          | 117 ms                                                 | 75.0 ms: 1.56x faster                                                  |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                  | 1.36x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250401-linux-x86_64-brandtbucher-unbox_unsigned-3.14.0a6+-f31fd63 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 133 ms: 1.42x faster                                                   |
| regex_v8       | 27.8 ms                                                | 23.5 ms: 1.18x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.30 ms: 1.10x faster                                                  |
| regex_dna      | 227 ms                                                 | 217 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                  | 1.18x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250401-linux-x86_64-brandtbucher-unbox_unsigned-3.14.0a6+-f31fd63 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.88 sec: 1.67x faster                                                 |
| pickle_pure_python   | 484 us                                                 | 333 us: 1.45x faster                                                   |
| unpickle_pure_python | 331 us                                                 | 230 us: 1.44x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 60.0 ms: 1.32x faster                                                  |
| json_dumps           | 14.2 ms                                                | 11.6 ms: 1.23x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                                   |
| xml_etree_iterparse  | 115 ms                                                 | 99.8 ms: 1.16x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 86.1 ms: 1.15x faster                                                  |
| json_loads           | 31.2 us                                                | 32.3 us: 1.03x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.27x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250401-linux-x86_64-brandtbucher-unbox_unsigned-3.14.0a6+-f31fd63 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.2 ms: 1.11x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 8.23 ms: 1.39x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250401-linux-x86_64-brandtbucher-unbox_unsigned-3.14.0a6+-f31fd63 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.7 ms: 1.47x faster                                                  |
| genshi_text     | 31.8 ms                                                | 21.9 ms: 1.45x faster                                                  |
| mako            | 16.3 ms                                                | 12.3 ms: 1.33x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 49.7 ms: 1.33x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250401-linux-x86_64-brandtbucher-unbox_unsigned-3.14.0a6+-f31fd63 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 168 us: 3.23x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 631 ms: 2.80x faster                                                   |
| generators               | 80.1 ms                                                | 28.6 ms: 2.80x faster                                                  |
| async_tree_none          | 728 ms                                                 | 266 ms: 2.74x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 322 ms: 2.70x faster                                                   |
| mdp                      | 2.85 sec                                               | 1.25 sec: 2.27x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.74 ms: 2.12x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 494 ms: 2.06x faster                                                   |
| pylint                   | 551 ms                                                 | 284 ms: 1.94x faster                                                   |
| chaos                    | 115 ms                                                 | 60.0 ms: 1.92x faster                                                  |
| go                       | 240 ms                                                 | 126 ms: 1.91x faster                                                   |
| deepcopy_memo            | 58.5 us                                                | 31.2 us: 1.87x faster                                                  |
| raytrace                 | 507 ms                                                 | 278 ms: 1.83x faster                                                   |
| deepcopy                 | 479 us                                                 | 262 us: 1.83x faster                                                   |
| logging_silent           | 190 ns                                                 | 106 ns: 1.79x faster                                                   |
| richards_super           | 94.7 ms                                                | 53.3 ms: 1.78x faster                                                  |
| spectral_norm            | 170 ms                                                 | 97.4 ms: 1.74x faster                                                  |
| scimark_sor              | 220 ms                                                 | 128 ms: 1.71x faster                                                   |
| scimark_monte_carlo      | 118 ms                                                 | 70.0 ms: 1.69x faster                                                  |
| richards                 | 79.3 ms                                                | 47.1 ms: 1.68x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 1.88 sec: 1.67x faster                                                 |
| comprehensions           | 28.8 us                                                | 17.5 us: 1.64x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.41 ms: 1.62x faster                                                  |
| coroutines               | 35.1 ms                                                | 21.6 ms: 1.62x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 81.7 ms: 1.56x faster                                                  |
| nbody                    | 154 ms                                                 | 98.1 ms: 1.56x faster                                                  |
| float                    | 117 ms                                                 | 75.0 ms: 1.56x faster                                                  |
| pyflate                  | 716 ms                                                 | 474 ms: 1.51x faster                                                   |
| deepcopy_reduce          | 4.17 us                                                | 2.77 us: 1.50x faster                                                  |
| django_template          | 48.2 ms                                                | 32.7 ms: 1.47x faster                                                  |
| genshi_text              | 31.8 ms                                                | 21.9 ms: 1.45x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 333 us: 1.45x faster                                                   |
| unpickle_pure_python     | 331 us                                                 | 230 us: 1.44x faster                                                   |
| logging_simple           | 8.30 us                                                | 5.80 us: 1.43x faster                                                  |
| regex_compile            | 188 ms                                                 | 133 ms: 1.42x faster                                                   |
| logging_format           | 9.09 us                                                | 6.42 us: 1.42x faster                                                  |
| scimark_lu               | 176 ms                                                 | 125 ms: 1.41x faster                                                   |
| dulwich_log              | 84.3 ms                                                | 60.4 ms: 1.40x faster                                                  |
| html5lib                 | 88.9 ms                                                | 63.8 ms: 1.39x faster                                                  |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.2 ms: 1.36x faster                                                  |
| mako                     | 16.3 ms                                                | 12.3 ms: 1.33x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 49.7 ms: 1.33x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.59 sec: 1.33x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.19 sec: 1.32x faster                                                 |
| 2to3                     | 348 ms                                                 | 264 ms: 1.32x faster                                                   |
| xml_etree_process        | 79.1 ms                                                | 60.0 ms: 1.32x faster                                                  |
| pprint_safe_repr         | 1.02 sec                                               | 777 ms: 1.31x faster                                                   |
| sympy_integrate          | 25.8 ms                                                | 19.9 ms: 1.30x faster                                                  |
| sqlalchemy_declarative   | 172 ms                                                 | 133 ms: 1.29x faster                                                   |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.02 ms: 1.29x faster                                                  |
| sympy_sum                | 196 ms                                                 | 153 ms: 1.29x faster                                                   |
| nqueens                  | 106 ms                                                 | 83.2 ms: 1.27x faster                                                  |
| sympy_str                | 346 ms                                                 | 275 ms: 1.26x faster                                                   |
| docutils                 | 3.30 sec                                               | 2.65 sec: 1.24x faster                                                 |
| pathlib                  | 20.5 ms                                                | 16.6 ms: 1.23x faster                                                  |
| json_dumps               | 14.2 ms                                                | 11.6 ms: 1.23x faster                                                  |
| fannkuch                 | 532 ms                                                 | 435 ms: 1.22x faster                                                   |
| scimark_fft              | 466 ms                                                 | 383 ms: 1.22x faster                                                   |
| sympy_expand             | 566 ms                                                 | 467 ms: 1.21x faster                                                   |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                                   |
| regex_v8                 | 27.8 ms                                                | 23.5 ms: 1.18x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 99.8 ms: 1.16x faster                                                  |
| xml_etree_generate       | 99.4 ms                                                | 86.1 ms: 1.15x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 889 us: 1.11x faster                                                   |
| async_generators         | 444 ms                                                 | 400 ms: 1.11x faster                                                   |
| python_startup           | 14.6 ms                                                | 13.2 ms: 1.11x faster                                                  |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.10x faster                                                   |
| regex_effbot             | 3.63 ms                                                | 3.30 ms: 1.10x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 2.81 us: 1.08x faster                                                  |
| regex_dna                | 227 ms                                                 | 217 ms: 1.04x faster                                                   |
| json                     | 5.69 ms                                                | 5.50 ms: 1.03x faster                                                  |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                   |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                   |
| json_loads               | 31.2 us                                                | 32.3 us: 1.03x slower                                                  |
| coverage                 | 79.4 ms                                                | 85.2 ms: 1.07x slower                                                  |
| telco                    | 7.27 ms                                                | 8.01 ms: 1.10x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 4.91 ms: 1.35x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 8.23 ms: 1.39x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 2.49 ms: 1.54x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 84.1 ms: 3.50x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.39x faster                                                           |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250401-3.14.0a6+-f31fd63/bm-20250401-linux-x86_64-brandtbucher-unbox_unsigned-3.14.0a6+-f31fd63.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.413x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.28x