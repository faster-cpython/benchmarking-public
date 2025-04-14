# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_guard_dict_tuple
- machine: linux-x86_64
- commit hash: 99d6288
- commit date: 2025-04-01
- overall geometric mean: 1.472x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.33x faster
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250401-linux-x86_64-brandtbucher-jit_guard_dict_tuple-3.14.0a6+-99d6288 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 258 ms: 1.35x faster                                                         |
| docutils       | 3.30 sec                                               | 2.68 sec: 1.23x faster                                                       |
| html5lib       | 88.9 ms                                                | 61.0 ms: 1.46x faster                                                        |
| Geometric mean | (ref)                                                  | 1.34x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250401-linux-x86_64-brandtbucher-jit_guard_dict_tuple-3.14.0a6+-99d6288 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 613 ms: 2.89x faster                                                         |
| async_tree_none         | 728 ms                                                 | 259 ms: 2.82x faster                                                         |
| async_tree_memoization  | 870 ms                                                 | 311 ms: 2.80x faster                                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 490 ms: 2.07x faster                                                         |
| Geometric mean          | (ref)                                                  | 2.62x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250401-linux-x86_64-brandtbucher-jit_guard_dict_tuple-3.14.0a6+-99d6288 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 61.6 ms: 1.90x faster                                                        |
| nbody          | 154 ms                                                 | 84.0 ms: 1.83x faster                                                        |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                  | 1.53x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250401-linux-x86_64-brandtbucher-jit_guard_dict_tuple-3.14.0a6+-99d6288 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.48x faster                                                         |
| regex_v8       | 27.8 ms                                                | 23.1 ms: 1.20x faster                                                        |
| regex_effbot   | 3.63 ms                                                | 3.15 ms: 1.15x faster                                                        |
| regex_dna      | 227 ms                                                 | 205 ms: 1.11x faster                                                         |
| Geometric mean | (ref)                                                  | 1.23x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250401-linux-x86_64-brandtbucher-jit_guard_dict_tuple-3.14.0a6+-99d6288 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.83 sec: 1.72x faster                                                       |
| unpickle_pure_python | 331 us                                                 | 209 us: 1.58x faster                                                         |
| pickle_pure_python   | 484 us                                                 | 320 us: 1.51x faster                                                         |
| xml_etree_process    | 79.1 ms                                                | 56.5 ms: 1.40x faster                                                        |
| xml_etree_generate   | 99.4 ms                                                | 79.6 ms: 1.25x faster                                                        |
| json_dumps           | 14.2 ms                                                | 11.5 ms: 1.23x faster                                                        |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                                         |
| xml_etree_iterparse  | 115 ms                                                 | 98.2 ms: 1.18x faster                                                        |
| json_loads           | 31.2 us                                                | 29.7 us: 1.05x faster                                                        |
| Geometric mean       | (ref)                                                  | 1.33x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250401-linux-x86_64-brandtbucher-jit_guard_dict_tuple-3.14.0a6+-99d6288 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.2 ms: 1.11x faster                                                        |
| python_startup_no_site | 5.93 ms                                                | 8.21 ms: 1.38x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250401-linux-x86_64-brandtbucher-jit_guard_dict_tuple-3.14.0a6+-99d6288 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.8 ms: 1.52x faster                                                        |
| mako            | 16.3 ms                                                | 10.9 ms: 1.49x faster                                                        |
| genshi_text     | 31.8 ms                                                | 21.4 ms: 1.49x faster                                                        |
| genshi_xml      | 66.0 ms                                                | 49.3 ms: 1.34x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.46x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250401-linux-x86_64-brandtbucher-jit_guard_dict_tuple-3.14.0a6+-99d6288 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 169 us: 3.23x faster                                                         |
| async_tree_io            | 1.77 sec                                               | 613 ms: 2.89x faster                                                         |
| async_tree_none          | 728 ms                                                 | 259 ms: 2.82x faster                                                         |
| async_tree_memoization   | 870 ms                                                 | 311 ms: 2.80x faster                                                         |
| generators               | 80.1 ms                                                | 29.7 ms: 2.70x faster                                                        |
| deltablue                | 7.91 ms                                                | 3.11 ms: 2.55x faster                                                        |
| richards_super           | 94.7 ms                                                | 39.6 ms: 2.39x faster                                                        |
| mdp                      | 2.85 sec                                               | 1.22 sec: 2.33x faster                                                       |
| richards                 | 79.3 ms                                                | 34.9 ms: 2.27x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 490 ms: 2.07x faster                                                         |
| chaos                    | 115 ms                                                 | 57.0 ms: 2.03x faster                                                        |
| deepcopy_memo            | 58.5 us                                                | 29.2 us: 2.00x faster                                                        |
| pylint                   | 551 ms                                                 | 280 ms: 1.97x faster                                                         |
| raytrace                 | 507 ms                                                 | 260 ms: 1.95x faster                                                         |
| go                       | 240 ms                                                 | 125 ms: 1.92x faster                                                         |
| float                    | 117 ms                                                 | 61.6 ms: 1.90x faster                                                        |
| logging_silent           | 190 ns                                                 | 100 ns: 1.89x faster                                                         |
| deepcopy                 | 479 us                                                 | 254 us: 1.89x faster                                                         |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.84x faster                                                         |
| nbody                    | 154 ms                                                 | 84.0 ms: 1.83x faster                                                        |
| scimark_monte_carlo      | 118 ms                                                 | 65.6 ms: 1.80x faster                                                        |
| crypto_pyaes             | 128 ms                                                 | 74.0 ms: 1.73x faster                                                        |
| tomli_loads              | 3.14 sec                                               | 1.83 sec: 1.72x faster                                                       |
| spectral_norm            | 170 ms                                                 | 99.1 ms: 1.71x faster                                                        |
| pyflate                  | 716 ms                                                 | 442 ms: 1.62x faster                                                         |
| unpickle_pure_python     | 331 us                                                 | 209 us: 1.58x faster                                                         |
| comprehensions           | 28.8 us                                                | 18.3 us: 1.57x faster                                                        |
| deepcopy_reduce          | 4.17 us                                                | 2.68 us: 1.56x faster                                                        |
| hexiom                   | 10.4 ms                                                | 6.72 ms: 1.55x faster                                                        |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.52x faster                                                         |
| django_template          | 48.2 ms                                                | 31.8 ms: 1.52x faster                                                        |
| scimark_fft              | 466 ms                                                 | 307 ms: 1.52x faster                                                         |
| pickle_pure_python       | 484 us                                                 | 320 us: 1.51x faster                                                         |
| mako                     | 16.3 ms                                                | 10.9 ms: 1.49x faster                                                        |
| genshi_text              | 31.8 ms                                                | 21.4 ms: 1.49x faster                                                        |
| coroutines               | 35.1 ms                                                | 23.6 ms: 1.49x faster                                                        |
| regex_compile            | 188 ms                                                 | 127 ms: 1.48x faster                                                         |
| logging_simple           | 8.30 us                                                | 5.65 us: 1.47x faster                                                        |
| html5lib                 | 88.9 ms                                                | 61.0 ms: 1.46x faster                                                        |
| logging_format           | 9.09 us                                                | 6.30 us: 1.44x faster                                                        |
| pycparser                | 1.58 sec                                               | 1.12 sec: 1.41x faster                                                       |
| xml_etree_process        | 79.1 ms                                                | 56.5 ms: 1.40x faster                                                        |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.63 ms: 1.40x faster                                                        |
| dulwich_log              | 84.3 ms                                                | 60.6 ms: 1.39x faster                                                        |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.0 ms: 1.37x faster                                                        |
| pprint_pformat           | 2.10 sec                                               | 1.54 sec: 1.36x faster                                                       |
| pprint_safe_repr         | 1.02 sec                                               | 751 ms: 1.36x faster                                                         |
| 2to3                     | 348 ms                                                 | 258 ms: 1.35x faster                                                         |
| genshi_xml               | 66.0 ms                                                | 49.3 ms: 1.34x faster                                                        |
| sympy_integrate          | 25.8 ms                                                | 19.7 ms: 1.31x faster                                                        |
| sympy_sum                | 196 ms                                                 | 151 ms: 1.30x faster                                                         |
| sqlalchemy_declarative   | 172 ms                                                 | 133 ms: 1.30x faster                                                         |
| fannkuch                 | 532 ms                                                 | 414 ms: 1.29x faster                                                         |
| nqueens                  | 106 ms                                                 | 82.8 ms: 1.28x faster                                                        |
| sympy_str                | 346 ms                                                 | 271 ms: 1.27x faster                                                         |
| xml_etree_generate       | 99.4 ms                                                | 79.6 ms: 1.25x faster                                                        |
| docutils                 | 3.30 sec                                               | 2.68 sec: 1.23x faster                                                       |
| json_dumps               | 14.2 ms                                                | 11.5 ms: 1.23x faster                                                        |
| pathlib                  | 20.5 ms                                                | 16.6 ms: 1.23x faster                                                        |
| sympy_expand             | 566 ms                                                 | 471 ms: 1.20x faster                                                         |
| regex_v8                 | 27.8 ms                                                | 23.1 ms: 1.20x faster                                                        |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                                         |
| xml_etree_iterparse      | 115 ms                                                 | 98.2 ms: 1.18x faster                                                        |
| regex_effbot             | 3.63 ms                                                | 3.15 ms: 1.15x faster                                                        |
| bench_thread_pool        | 986 us                                                 | 887 us: 1.11x faster                                                         |
| sqlite_synth             | 3.02 us                                                | 2.72 us: 1.11x faster                                                        |
| python_startup           | 14.6 ms                                                | 13.2 ms: 1.11x faster                                                        |
| regex_dna                | 227 ms                                                 | 205 ms: 1.11x faster                                                         |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                         |
| json                     | 5.69 ms                                                | 5.28 ms: 1.08x faster                                                        |
| async_generators         | 444 ms                                                 | 413 ms: 1.07x faster                                                         |
| json_loads               | 31.2 us                                                | 29.7 us: 1.05x faster                                                        |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                                         |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                         |
| telco                    | 7.27 ms                                                | 7.86 ms: 1.08x slower                                                        |
| coverage                 | 79.4 ms                                                | 86.0 ms: 1.08x slower                                                        |
| gc_traversal             | 3.62 ms                                                | 4.99 ms: 1.38x slower                                                        |
| python_startup_no_site   | 5.93 ms                                                | 8.21 ms: 1.38x slower                                                        |
| create_gc_cycles         | 1.62 ms                                                | 2.49 ms: 1.54x slower                                                        |
| bench_mp_pool            | 24.0 ms                                                | 83.4 ms: 3.47x slower                                                        |
| Geometric mean           | (ref)                                                  | 1.44x faster                                                                 |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250401-3.14.0a6+-99d6288-JIT/bm-20250401-linux-x86_64-brandtbucher-jit_guard_dict_tuple-3.14.0a6+-99d6288.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.472x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.37x
- 95% likely to have a speedup of 1.36x
- 99% likely to have a speedup of 1.33x

# Memory
- memory change: 1.30x