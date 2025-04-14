# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_binary_op_extend
- machine: linux-x86_64
- commit hash: edbf7ef
- commit date: 2025-03-17
- overall geometric mean: 1.437x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250317-linux-x86_64-brandtbucher-jit_binary_op_extend-3.14.0a6+-edbf7ef |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 263 ms: 1.33x faster                                                         |
| docutils       | 3.30 sec                                               | 2.69 sec: 1.23x faster                                                       |
| html5lib       | 88.9 ms                                                | 62.6 ms: 1.42x faster                                                        |
| Geometric mean | (ref)                                                  | 1.32x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250317-linux-x86_64-brandtbucher-jit_binary_op_extend-3.14.0a6+-edbf7ef |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 612 ms: 2.89x faster                                                         |
| async_tree_none         | 728 ms                                                 | 259 ms: 2.81x faster                                                         |
| async_tree_memoization  | 870 ms                                                 | 317 ms: 2.74x faster                                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 493 ms: 2.06x faster                                                         |
| Geometric mean          | (ref)                                                  | 2.60x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250317-linux-x86_64-brandtbucher-jit_binary_op_extend-3.14.0a6+-edbf7ef |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 65.1 ms: 1.80x faster                                                        |
| nbody          | 154 ms                                                 | 87.9 ms: 1.75x faster                                                        |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                  | 1.48x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250317-linux-x86_64-brandtbucher-jit_binary_op_extend-3.14.0a6+-edbf7ef |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.47x faster                                                         |
| regex_v8       | 27.8 ms                                                | 24.2 ms: 1.15x faster                                                        |
| regex_effbot   | 3.63 ms                                                | 3.34 ms: 1.09x faster                                                        |
| regex_dna      | 227 ms                                                 | 225 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                  | 1.17x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250317-linux-x86_64-brandtbucher-jit_binary_op_extend-3.14.0a6+-edbf7ef |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.88 sec: 1.67x faster                                                       |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                                         |
| pickle_pure_python   | 484 us                                                 | 323 us: 1.50x faster                                                         |
| xml_etree_process    | 79.1 ms                                                | 56.6 ms: 1.40x faster                                                        |
| xml_etree_generate   | 99.4 ms                                                | 80.0 ms: 1.24x faster                                                        |
| json_dumps           | 14.2 ms                                                | 11.6 ms: 1.22x faster                                                        |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                                         |
| xml_etree_iterparse  | 115 ms                                                 | 98.3 ms: 1.17x faster                                                        |
| json_loads           | 31.2 us                                                | 29.9 us: 1.04x faster                                                        |
| Geometric mean       | (ref)                                                  | 1.32x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250317-linux-x86_64-brandtbucher-jit_binary_op_extend-3.14.0a6+-edbf7ef |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.11x faster                                                        |
| python_startup_no_site | 5.93 ms                                                | 8.18 ms: 1.38x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250317-linux-x86_64-brandtbucher-jit_binary_op_extend-3.14.0a6+-edbf7ef |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.1 ms: 1.50x faster                                                        |
| genshi_text     | 31.8 ms                                                | 21.5 ms: 1.48x faster                                                        |
| mako            | 16.3 ms                                                | 11.2 ms: 1.46x faster                                                        |
| genshi_xml      | 66.0 ms                                                | 51.2 ms: 1.29x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250317-linux-x86_64-brandtbucher-jit_binary_op_extend-3.14.0a6+-edbf7ef |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 170 us: 3.21x faster                                                         |
| async_tree_io            | 1.77 sec                                               | 612 ms: 2.89x faster                                                         |
| async_tree_none          | 728 ms                                                 | 259 ms: 2.81x faster                                                         |
| generators               | 80.1 ms                                                | 28.7 ms: 2.79x faster                                                        |
| async_tree_memoization   | 870 ms                                                 | 317 ms: 2.74x faster                                                         |
| deltablue                | 7.91 ms                                                | 3.06 ms: 2.59x faster                                                        |
| richards_super           | 94.7 ms                                                | 40.7 ms: 2.33x faster                                                        |
| richards                 | 79.3 ms                                                | 35.4 ms: 2.24x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 493 ms: 2.06x faster                                                         |
| deepcopy_memo            | 58.5 us                                                | 29.9 us: 1.96x faster                                                        |
| pylint                   | 551 ms                                                 | 282 ms: 1.95x faster                                                         |
| chaos                    | 115 ms                                                 | 60.2 ms: 1.92x faster                                                        |
| logging_silent           | 190 ns                                                 | 99.2 ns: 1.91x faster                                                        |
| raytrace                 | 507 ms                                                 | 267 ms: 1.90x faster                                                         |
| go                       | 240 ms                                                 | 129 ms: 1.85x faster                                                         |
| deepcopy                 | 479 us                                                 | 260 us: 1.84x faster                                                         |
| scimark_sor              | 220 ms                                                 | 120 ms: 1.83x faster                                                         |
| float                    | 117 ms                                                 | 65.1 ms: 1.80x faster                                                        |
| spectral_norm            | 170 ms                                                 | 95.8 ms: 1.77x faster                                                        |
| nbody                    | 154 ms                                                 | 87.9 ms: 1.75x faster                                                        |
| scimark_monte_carlo      | 118 ms                                                 | 69.1 ms: 1.71x faster                                                        |
| tomli_loads              | 3.14 sec                                               | 1.88 sec: 1.67x faster                                                       |
| crypto_pyaes             | 128 ms                                                 | 78.1 ms: 1.64x faster                                                        |
| pyflate                  | 716 ms                                                 | 449 ms: 1.60x faster                                                         |
| hexiom                   | 10.4 ms                                                | 6.74 ms: 1.54x faster                                                        |
| comprehensions           | 28.8 us                                                | 18.8 us: 1.53x faster                                                        |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                                         |
| deepcopy_reduce          | 4.17 us                                                | 2.73 us: 1.53x faster                                                        |
| django_template          | 48.2 ms                                                | 32.1 ms: 1.50x faster                                                        |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.50x faster                                                         |
| coroutines               | 35.1 ms                                                | 23.4 ms: 1.50x faster                                                        |
| pickle_pure_python       | 484 us                                                 | 323 us: 1.50x faster                                                         |
| logging_simple           | 8.30 us                                                | 5.55 us: 1.50x faster                                                        |
| genshi_text              | 31.8 ms                                                | 21.5 ms: 1.48x faster                                                        |
| scimark_fft              | 466 ms                                                 | 315 ms: 1.48x faster                                                         |
| logging_format           | 9.09 us                                                | 6.16 us: 1.48x faster                                                        |
| regex_compile            | 188 ms                                                 | 128 ms: 1.47x faster                                                         |
| mako                     | 16.3 ms                                                | 11.2 ms: 1.46x faster                                                        |
| html5lib                 | 88.9 ms                                                | 62.6 ms: 1.42x faster                                                        |
| xml_etree_process        | 79.1 ms                                                | 56.6 ms: 1.40x faster                                                        |
| dulwich_log              | 84.3 ms                                                | 60.8 ms: 1.39x faster                                                        |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.38x faster                                                       |
| thrift                   | 1.07 ms                                                | 781 us: 1.37x faster                                                         |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.1 ms: 1.37x faster                                                        |
| pprint_pformat           | 2.10 sec                                               | 1.56 sec: 1.35x faster                                                       |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.84 ms: 1.34x faster                                                        |
| 2to3                     | 348 ms                                                 | 263 ms: 1.33x faster                                                         |
| pprint_safe_repr         | 1.02 sec                                               | 768 ms: 1.33x faster                                                         |
| sympy_sum                | 196 ms                                                 | 152 ms: 1.30x faster                                                         |
| sqlalchemy_declarative   | 172 ms                                                 | 133 ms: 1.29x faster                                                         |
| genshi_xml               | 66.0 ms                                                | 51.2 ms: 1.29x faster                                                        |
| sympy_integrate          | 25.8 ms                                                | 20.3 ms: 1.27x faster                                                        |
| fannkuch                 | 532 ms                                                 | 423 ms: 1.26x faster                                                         |
| sympy_str                | 346 ms                                                 | 277 ms: 1.25x faster                                                         |
| xml_etree_generate       | 99.4 ms                                                | 80.0 ms: 1.24x faster                                                        |
| nqueens                  | 106 ms                                                 | 85.6 ms: 1.24x faster                                                        |
| docutils                 | 3.30 sec                                               | 2.69 sec: 1.23x faster                                                       |
| json_dumps               | 14.2 ms                                                | 11.6 ms: 1.22x faster                                                        |
| pathlib                  | 20.5 ms                                                | 16.8 ms: 1.22x faster                                                        |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                                         |
| sympy_expand             | 566 ms                                                 | 477 ms: 1.19x faster                                                         |
| xml_etree_iterparse      | 115 ms                                                 | 98.3 ms: 1.17x faster                                                        |
| regex_v8                 | 27.8 ms                                                | 24.2 ms: 1.15x faster                                                        |
| mdp                      | 2.85 sec                                               | 2.50 sec: 1.14x faster                                                       |
| bench_thread_pool        | 986 us                                                 | 885 us: 1.11x faster                                                         |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.11x faster                                                        |
| sqlite_synth             | 3.02 us                                                | 2.73 us: 1.11x faster                                                        |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                         |
| regex_effbot             | 3.63 ms                                                | 3.34 ms: 1.09x faster                                                        |
| json                     | 5.69 ms                                                | 5.37 ms: 1.06x faster                                                        |
| async_generators         | 444 ms                                                 | 425 ms: 1.04x faster                                                         |
| json_loads               | 31.2 us                                                | 29.9 us: 1.04x faster                                                        |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                         |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                         |
| regex_dna                | 227 ms                                                 | 225 ms: 1.01x faster                                                         |
| coverage                 | 79.4 ms                                                | 84.4 ms: 1.06x slower                                                        |
| telco                    | 7.27 ms                                                | 7.82 ms: 1.08x slower                                                        |
| gc_traversal             | 3.62 ms                                                | 4.97 ms: 1.37x slower                                                        |
| python_startup_no_site   | 5.93 ms                                                | 8.18 ms: 1.38x slower                                                        |
| create_gc_cycles         | 1.62 ms                                                | 2.50 ms: 1.54x slower                                                        |
| bench_mp_pool            | 24.0 ms                                                | 83.0 ms: 3.46x slower                                                        |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                                 |
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250317-3.14.0a6+-edbf7ef-JIT/bm-20250317-linux-x86_64-brandtbucher-jit_binary_op_extend-3.14.0a6+-edbf7ef.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.437x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.29x

# Memory
- memory change: 1.29x