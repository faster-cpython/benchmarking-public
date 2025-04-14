# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_build_and_iter
- machine: linux-x86_64
- commit hash: 488d5b8
- commit date: 2025-03-27
- overall geometric mean: 1.437x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250327-linux-x86_64-brandtbucher-jit_build_and_iter-3.14.0a6+-488d5b8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 264 ms: 1.32x faster                                                       |
| docutils       | 3.30 sec                                               | 2.69 sec: 1.23x faster                                                     |
| html5lib       | 88.9 ms                                                | 63.5 ms: 1.40x faster                                                      |
| Geometric mean | (ref)                                                  | 1.31x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250327-linux-x86_64-brandtbucher-jit_build_and_iter-3.14.0a6+-488d5b8 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 623 ms: 2.84x faster                                                       |
| async_tree_none         | 728 ms                                                 | 265 ms: 2.75x faster                                                       |
| async_tree_memoization  | 870 ms                                                 | 316 ms: 2.75x faster                                                       |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 492 ms: 2.07x faster                                                       |
| Geometric mean          | (ref)                                                  | 2.58x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250327-linux-x86_64-brandtbucher-jit_build_and_iter-3.14.0a6+-488d5b8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 65.7 ms: 1.78x faster                                                      |
| nbody          | 154 ms                                                 | 88.4 ms: 1.74x faster                                                      |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                  | 1.47x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250327-linux-x86_64-brandtbucher-jit_build_and_iter-3.14.0a6+-488d5b8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.47x faster                                                       |
| regex_v8       | 27.8 ms                                                | 23.7 ms: 1.17x faster                                                      |
| regex_effbot   | 3.63 ms                                                | 3.20 ms: 1.14x faster                                                      |
| regex_dna      | 227 ms                                                 | 217 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                  | 1.20x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250327-linux-x86_64-brandtbucher-jit_build_and_iter-3.14.0a6+-488d5b8 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.87 sec: 1.68x faster                                                     |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                                       |
| pickle_pure_python   | 484 us                                                 | 325 us: 1.49x faster                                                       |
| xml_etree_process    | 79.1 ms                                                | 56.6 ms: 1.40x faster                                                      |
| xml_etree_generate   | 99.4 ms                                                | 80.7 ms: 1.23x faster                                                      |
| json_dumps           | 14.2 ms                                                | 11.6 ms: 1.22x faster                                                      |
| xml_etree_parse      | 168 ms                                                 | 139 ms: 1.20x faster                                                       |
| xml_etree_iterparse  | 115 ms                                                 | 97.9 ms: 1.18x faster                                                      |
| json_loads           | 31.2 us                                                | 29.7 us: 1.05x faster                                                      |
| Geometric mean       | (ref)                                                  | 1.32x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250327-linux-x86_64-brandtbucher-jit_build_and_iter-3.14.0a6+-488d5b8 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.2 ms: 1.11x faster                                                      |
| python_startup_no_site | 5.93 ms                                                | 8.24 ms: 1.39x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250327-linux-x86_64-brandtbucher-jit_build_and_iter-3.14.0a6+-488d5b8 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.2 ms: 1.49x faster                                                      |
| genshi_text     | 31.8 ms                                                | 21.4 ms: 1.49x faster                                                      |
| mako            | 16.3 ms                                                | 11.0 ms: 1.49x faster                                                      |
| genshi_xml      | 66.0 ms                                                | 49.7 ms: 1.33x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250327-linux-x86_64-brandtbucher-jit_build_and_iter-3.14.0a6+-488d5b8 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.27x faster                                                       |
| async_tree_io            | 1.77 sec                                               | 623 ms: 2.84x faster                                                       |
| generators               | 80.1 ms                                                | 28.6 ms: 2.80x faster                                                      |
| async_tree_none          | 728 ms                                                 | 265 ms: 2.75x faster                                                       |
| async_tree_memoization   | 870 ms                                                 | 316 ms: 2.75x faster                                                       |
| deltablue                | 7.91 ms                                                | 3.07 ms: 2.58x faster                                                      |
| richards_super           | 94.7 ms                                                | 41.6 ms: 2.27x faster                                                      |
| richards                 | 79.3 ms                                                | 36.2 ms: 2.19x faster                                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 492 ms: 2.07x faster                                                       |
| deepcopy_memo            | 58.5 us                                                | 29.2 us: 2.00x faster                                                      |
| pylint                   | 551 ms                                                 | 282 ms: 1.96x faster                                                       |
| chaos                    | 115 ms                                                 | 59.8 ms: 1.93x faster                                                      |
| logging_silent           | 190 ns                                                 | 100 ns: 1.90x faster                                                       |
| go                       | 240 ms                                                 | 129 ms: 1.86x faster                                                       |
| raytrace                 | 507 ms                                                 | 273 ms: 1.86x faster                                                       |
| deepcopy                 | 479 us                                                 | 263 us: 1.82x faster                                                       |
| scimark_sor              | 220 ms                                                 | 121 ms: 1.81x faster                                                       |
| spectral_norm            | 170 ms                                                 | 95.2 ms: 1.78x faster                                                      |
| float                    | 117 ms                                                 | 65.7 ms: 1.78x faster                                                      |
| nbody                    | 154 ms                                                 | 88.4 ms: 1.74x faster                                                      |
| scimark_monte_carlo      | 118 ms                                                 | 68.3 ms: 1.73x faster                                                      |
| tomli_loads              | 3.14 sec                                               | 1.87 sec: 1.68x faster                                                     |
| pyflate                  | 716 ms                                                 | 427 ms: 1.68x faster                                                       |
| crypto_pyaes             | 128 ms                                                 | 79.3 ms: 1.61x faster                                                      |
| deepcopy_reduce          | 4.17 us                                                | 2.71 us: 1.54x faster                                                      |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                                       |
| comprehensions           | 28.8 us                                                | 18.8 us: 1.53x faster                                                      |
| hexiom                   | 10.4 ms                                                | 6.88 ms: 1.51x faster                                                      |
| coroutines               | 35.1 ms                                                | 23.3 ms: 1.50x faster                                                      |
| scimark_lu               | 176 ms                                                 | 118 ms: 1.50x faster                                                       |
| django_template          | 48.2 ms                                                | 32.2 ms: 1.49x faster                                                      |
| pickle_pure_python       | 484 us                                                 | 325 us: 1.49x faster                                                       |
| genshi_text              | 31.8 ms                                                | 21.4 ms: 1.49x faster                                                      |
| mako                     | 16.3 ms                                                | 11.0 ms: 1.49x faster                                                      |
| scimark_fft              | 466 ms                                                 | 314 ms: 1.48x faster                                                       |
| logging_simple           | 8.30 us                                                | 5.65 us: 1.47x faster                                                      |
| regex_compile            | 188 ms                                                 | 129 ms: 1.47x faster                                                       |
| logging_format           | 9.09 us                                                | 6.27 us: 1.45x faster                                                      |
| html5lib                 | 88.9 ms                                                | 63.5 ms: 1.40x faster                                                      |
| xml_etree_process        | 79.1 ms                                                | 56.6 ms: 1.40x faster                                                      |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.67 ms: 1.39x faster                                                      |
| dulwich_log              | 84.3 ms                                                | 60.9 ms: 1.38x faster                                                      |
| thrift                   | 1.07 ms                                                | 776 us: 1.38x faster                                                       |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.37x faster                                                     |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.3 ms: 1.35x faster                                                      |
| genshi_xml               | 66.0 ms                                                | 49.7 ms: 1.33x faster                                                      |
| 2to3                     | 348 ms                                                 | 264 ms: 1.32x faster                                                       |
| sqlalchemy_declarative   | 172 ms                                                 | 134 ms: 1.29x faster                                                       |
| pprint_pformat           | 2.10 sec                                               | 1.64 sec: 1.29x faster                                                     |
| sympy_integrate          | 25.8 ms                                                | 20.1 ms: 1.28x faster                                                      |
| sympy_sum                | 196 ms                                                 | 153 ms: 1.28x faster                                                       |
| pprint_safe_repr         | 1.02 sec                                               | 804 ms: 1.27x faster                                                       |
| fannkuch                 | 532 ms                                                 | 420 ms: 1.26x faster                                                       |
| sympy_str                | 346 ms                                                 | 275 ms: 1.26x faster                                                       |
| nqueens                  | 106 ms                                                 | 84.4 ms: 1.25x faster                                                      |
| xml_etree_generate       | 99.4 ms                                                | 80.7 ms: 1.23x faster                                                      |
| docutils                 | 3.30 sec                                               | 2.69 sec: 1.23x faster                                                     |
| json_dumps               | 14.2 ms                                                | 11.6 ms: 1.22x faster                                                      |
| pathlib                  | 20.5 ms                                                | 16.9 ms: 1.21x faster                                                      |
| xml_etree_parse          | 168 ms                                                 | 139 ms: 1.20x faster                                                       |
| sympy_expand             | 566 ms                                                 | 476 ms: 1.19x faster                                                       |
| xml_etree_iterparse      | 115 ms                                                 | 97.9 ms: 1.18x faster                                                      |
| regex_v8                 | 27.8 ms                                                | 23.7 ms: 1.17x faster                                                      |
| mdp                      | 2.85 sec                                               | 2.49 sec: 1.14x faster                                                     |
| regex_effbot             | 3.63 ms                                                | 3.20 ms: 1.14x faster                                                      |
| bench_thread_pool        | 986 us                                                 | 882 us: 1.12x faster                                                       |
| sqlite_synth             | 3.02 us                                                | 2.73 us: 1.11x faster                                                      |
| python_startup           | 14.6 ms                                                | 13.2 ms: 1.11x faster                                                      |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.09x faster                                                       |
| async_generators         | 444 ms                                                 | 412 ms: 1.08x faster                                                       |
| json                     | 5.69 ms                                                | 5.29 ms: 1.08x faster                                                      |
| json_loads               | 31.2 us                                                | 29.7 us: 1.05x faster                                                      |
| regex_dna                | 227 ms                                                 | 217 ms: 1.05x faster                                                       |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                       |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                       |
| telco                    | 7.27 ms                                                | 7.82 ms: 1.08x slower                                                      |
| coverage                 | 79.4 ms                                                | 88.9 ms: 1.12x slower                                                      |
| gc_traversal             | 3.62 ms                                                | 4.83 ms: 1.33x slower                                                      |
| python_startup_no_site   | 5.93 ms                                                | 8.24 ms: 1.39x slower                                                      |
| create_gc_cycles         | 1.62 ms                                                | 2.49 ms: 1.53x slower                                                      |
| bench_mp_pool            | 24.0 ms                                                | 83.5 ms: 3.48x slower                                                      |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                               |
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250327-3.14.0a6+-488d5b8-JIT/bm-20250327-linux-x86_64-brandtbucher-jit_build_and_iter-3.14.0a6+-488d5b8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.437x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.29x