# Results vs. 3.10.4

- fork: brandtbucher
- ref: unbox
- machine: linux-x86_64
- commit hash: c912ef1
- commit date: 2025-04-01
- overall geometric mean: 1.424x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 261 ms: 1.33x faster                                          |
| docutils       | 3.30 sec                                               | 2.65 sec: 1.24x faster                                        |
| html5lib       | 88.9 ms                                                | 63.9 ms: 1.39x faster                                         |
| Geometric mean | (ref)                                                  | 1.32x faster                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 634 ms: 2.79x faster                                          |
| async_tree_none         | 728 ms                                                 | 268 ms: 2.72x faster                                          |
| async_tree_memoization  | 870 ms                                                 | 324 ms: 2.69x faster                                          |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 495 ms: 2.05x faster                                          |
| Geometric mean          | (ref)                                                  | 2.54x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 117 ms                                                 | 75.4 ms: 1.55x faster                                         |
| nbody          | 154 ms                                                 | 102 ms: 1.51x faster                                          |
| pidigits       | 191 ms                                                 | 189 ms: 1.01x faster                                          |
| Geometric mean | (ref)                                                  | 1.33x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 131 ms: 1.44x faster                                          |
| regex_v8       | 27.8 ms                                                | 24.6 ms: 1.13x faster                                         |
| regex_effbot   | 3.63 ms                                                | 3.44 ms: 1.06x faster                                         |
| regex_dna      | 227 ms                                                 | 217 ms: 1.04x faster                                          |
| Geometric mean | (ref)                                                  | 1.16x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.88 sec: 1.67x faster                                        |
| pickle_pure_python   | 484 us                                                 | 326 us: 1.49x faster                                          |
| unpickle_pure_python | 331 us                                                 | 226 us: 1.46x faster                                          |
| xml_etree_process    | 79.1 ms                                                | 59.8 ms: 1.32x faster                                         |
| json_dumps           | 14.2 ms                                                | 11.6 ms: 1.22x faster                                         |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                          |
| xml_etree_generate   | 99.4 ms                                                | 85.1 ms: 1.17x faster                                         |
| xml_etree_iterparse  | 115 ms                                                 | 99.6 ms: 1.16x faster                                         |
| json_loads           | 31.2 us                                                | 32.0 us: 1.02x slower                                         |
| Geometric mean       | (ref)                                                  | 1.28x faster                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.2 ms: 1.11x faster                                         |
| python_startup_no_site | 5.93 ms                                                | 8.22 ms: 1.39x slower                                         |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.5 ms: 1.48x faster                                         |
| genshi_text     | 31.8 ms                                                | 21.9 ms: 1.46x faster                                         |
| mako            | 16.3 ms                                                | 12.0 ms: 1.36x faster                                         |
| genshi_xml      | 66.0 ms                                                | 50.4 ms: 1.31x faster                                         |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 166 us: 3.29x faster                                          |
| async_tree_io            | 1.77 sec                                               | 634 ms: 2.79x faster                                          |
| generators               | 80.1 ms                                                | 29.0 ms: 2.76x faster                                         |
| async_tree_none          | 728 ms                                                 | 268 ms: 2.72x faster                                          |
| async_tree_memoization   | 870 ms                                                 | 324 ms: 2.69x faster                                          |
| deltablue                | 7.91 ms                                                | 3.33 ms: 2.38x faster                                         |
| mdp                      | 2.85 sec                                               | 1.24 sec: 2.29x faster                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 495 ms: 2.05x faster                                          |
| chaos                    | 115 ms                                                 | 57.2 ms: 2.02x faster                                         |
| go                       | 240 ms                                                 | 120 ms: 2.01x faster                                          |
| pylint                   | 551 ms                                                 | 282 ms: 1.96x faster                                          |
| logging_silent           | 190 ns                                                 | 97.7 ns: 1.94x faster                                         |
| deepcopy_memo            | 58.5 us                                                | 30.8 us: 1.90x faster                                         |
| raytrace                 | 507 ms                                                 | 270 ms: 1.87x faster                                          |
| spectral_norm            | 170 ms                                                 | 91.1 ms: 1.87x faster                                         |
| scimark_sor              | 220 ms                                                 | 118 ms: 1.86x faster                                          |
| deepcopy                 | 479 us                                                 | 263 us: 1.82x faster                                          |
| richards_super           | 94.7 ms                                                | 52.5 ms: 1.80x faster                                         |
| scimark_monte_carlo      | 118 ms                                                 | 67.9 ms: 1.74x faster                                         |
| richards                 | 79.3 ms                                                | 46.1 ms: 1.72x faster                                         |
| hexiom                   | 10.4 ms                                                | 6.08 ms: 1.71x faster                                         |
| tomli_loads              | 3.14 sec                                               | 1.88 sec: 1.67x faster                                        |
| comprehensions           | 28.8 us                                                | 17.3 us: 1.67x faster                                         |
| coroutines               | 35.1 ms                                                | 21.8 ms: 1.61x faster                                         |
| float                    | 117 ms                                                 | 75.4 ms: 1.55x faster                                         |
| crypto_pyaes             | 128 ms                                                 | 82.8 ms: 1.54x faster                                         |
| deepcopy_reduce          | 4.17 us                                                | 2.72 us: 1.53x faster                                         |
| nbody                    | 154 ms                                                 | 102 ms: 1.51x faster                                          |
| pyflate                  | 716 ms                                                 | 476 ms: 1.50x faster                                          |
| pickle_pure_python       | 484 us                                                 | 326 us: 1.49x faster                                          |
| django_template          | 48.2 ms                                                | 32.5 ms: 1.48x faster                                         |
| unpickle_pure_python     | 331 us                                                 | 226 us: 1.46x faster                                          |
| genshi_text              | 31.8 ms                                                | 21.9 ms: 1.46x faster                                         |
| logging_simple           | 8.30 us                                                | 5.71 us: 1.45x faster                                         |
| logging_format           | 9.09 us                                                | 6.26 us: 1.45x faster                                         |
| regex_compile            | 188 ms                                                 | 131 ms: 1.44x faster                                          |
| dulwich_log              | 84.3 ms                                                | 59.4 ms: 1.42x faster                                         |
| scimark_lu               | 176 ms                                                 | 126 ms: 1.40x faster                                          |
| html5lib                 | 88.9 ms                                                | 63.9 ms: 1.39x faster                                         |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.0 ms: 1.38x faster                                         |
| mako                     | 16.3 ms                                                | 12.0 ms: 1.36x faster                                         |
| pprint_pformat           | 2.10 sec                                               | 1.57 sec: 1.34x faster                                        |
| pprint_safe_repr         | 1.02 sec                                               | 762 ms: 1.34x faster                                          |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.34x faster                                        |
| 2to3                     | 348 ms                                                 | 261 ms: 1.33x faster                                          |
| xml_etree_process        | 79.1 ms                                                | 59.8 ms: 1.32x faster                                         |
| genshi_xml               | 66.0 ms                                                | 50.4 ms: 1.31x faster                                         |
| sympy_integrate          | 25.8 ms                                                | 19.7 ms: 1.31x faster                                         |
| sqlalchemy_declarative   | 172 ms                                                 | 132 ms: 1.30x faster                                          |
| sympy_sum                | 196 ms                                                 | 152 ms: 1.29x faster                                          |
| sympy_str                | 346 ms                                                 | 273 ms: 1.27x faster                                          |
| nqueens                  | 106 ms                                                 | 83.5 ms: 1.27x faster                                         |
| fannkuch                 | 532 ms                                                 | 426 ms: 1.25x faster                                          |
| docutils                 | 3.30 sec                                               | 2.65 sec: 1.24x faster                                        |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.29 ms: 1.22x faster                                         |
| pathlib                  | 20.5 ms                                                | 16.7 ms: 1.22x faster                                         |
| json_dumps               | 14.2 ms                                                | 11.6 ms: 1.22x faster                                         |
| sympy_expand             | 566 ms                                                 | 466 ms: 1.22x faster                                          |
| scimark_fft              | 466 ms                                                 | 384 ms: 1.21x faster                                          |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                          |
| xml_etree_generate       | 99.4 ms                                                | 85.1 ms: 1.17x faster                                         |
| xml_etree_iterparse      | 115 ms                                                 | 99.6 ms: 1.16x faster                                         |
| regex_v8                 | 27.8 ms                                                | 24.6 ms: 1.13x faster                                         |
| bench_thread_pool        | 986 us                                                 | 884 us: 1.12x faster                                          |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.11x faster                                          |
| async_generators         | 444 ms                                                 | 399 ms: 1.11x faster                                          |
| python_startup           | 14.6 ms                                                | 13.2 ms: 1.11x faster                                         |
| sqlite_synth             | 3.02 us                                                | 2.82 us: 1.07x faster                                         |
| regex_effbot             | 3.63 ms                                                | 3.44 ms: 1.06x faster                                         |
| regex_dna                | 227 ms                                                 | 217 ms: 1.04x faster                                          |
| json                     | 5.69 ms                                                | 5.47 ms: 1.04x faster                                         |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                          |
| pidigits                 | 191 ms                                                 | 189 ms: 1.01x faster                                          |
| json_loads               | 31.2 us                                                | 32.0 us: 1.02x slower                                         |
| coverage                 | 79.4 ms                                                | 84.6 ms: 1.06x slower                                         |
| telco                    | 7.27 ms                                                | 8.07 ms: 1.11x slower                                         |
| gc_traversal             | 3.62 ms                                                | 4.99 ms: 1.38x slower                                         |
| python_startup_no_site   | 5.93 ms                                                | 8.22 ms: 1.39x slower                                         |
| create_gc_cycles         | 1.62 ms                                                | 2.47 ms: 1.53x slower                                         |
| bench_mp_pool            | 24.0 ms                                                | 83.7 ms: 3.48x slower                                         |
| Geometric mean           | (ref)                                                  | 1.40x faster                                                  |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.424x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.29x

# Memory
- memory change: 1.28x