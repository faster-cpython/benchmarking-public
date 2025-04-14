# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_up_11_6
- machine: linux-x86_64
- commit hash: a0aff13
- commit date: 2025-03-29
- overall geometric mean: 1.436x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-linux-x86_64-brandtbucher-jit_up_11_6-3.14.0a6+-a0aff13 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 265 ms: 1.32x faster                                                |
| docutils       | 3.30 sec                                               | 2.71 sec: 1.22x faster                                              |
| html5lib       | 88.9 ms                                                | 61.9 ms: 1.44x faster                                               |
| Geometric mean | (ref)                                                  | 1.32x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-linux-x86_64-brandtbucher-jit_up_11_6-3.14.0a6+-a0aff13 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 617 ms: 2.87x faster                                                |
| async_tree_none         | 728 ms                                                 | 260 ms: 2.80x faster                                                |
| async_tree_memoization  | 870 ms                                                 | 316 ms: 2.75x faster                                                |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 490 ms: 2.07x faster                                                |
| Geometric mean          | (ref)                                                  | 2.60x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-linux-x86_64-brandtbucher-jit_up_11_6-3.14.0a6+-a0aff13 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 117 ms                                                 | 65.7 ms: 1.78x faster                                               |
| nbody          | 154 ms                                                 | 86.8 ms: 1.77x faster                                               |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                |
| Geometric mean | (ref)                                                  | 1.48x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-linux-x86_64-brandtbucher-jit_up_11_6-3.14.0a6+-a0aff13 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.47x faster                                                |
| regex_v8       | 27.8 ms                                                | 23.6 ms: 1.18x faster                                               |
| regex_effbot   | 3.63 ms                                                | 3.36 ms: 1.08x faster                                               |
| regex_dna      | 227 ms                                                 | 226 ms: 1.00x faster                                                |
| Geometric mean | (ref)                                                  | 1.17x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-linux-x86_64-brandtbucher-jit_up_11_6-3.14.0a6+-a0aff13 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.88 sec: 1.67x faster                                              |
| unpickle_pure_python | 331 us                                                 | 211 us: 1.56x faster                                                |
| pickle_pure_python   | 484 us                                                 | 326 us: 1.49x faster                                                |
| xml_etree_process    | 79.1 ms                                                | 56.9 ms: 1.39x faster                                               |
| xml_etree_generate   | 99.4 ms                                                | 80.6 ms: 1.23x faster                                               |
| json_dumps           | 14.2 ms                                                | 11.6 ms: 1.22x faster                                               |
| xml_etree_parse      | 168 ms                                                 | 139 ms: 1.21x faster                                                |
| xml_etree_iterparse  | 115 ms                                                 | 98.0 ms: 1.18x faster                                               |
| json_loads           | 31.2 us                                                | 30.1 us: 1.04x faster                                               |
| Geometric mean       | (ref)                                                  | 1.32x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-linux-x86_64-brandtbucher-jit_up_11_6-3.14.0a6+-a0aff13 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.11x faster                                               |
| python_startup_no_site | 5.93 ms                                                | 8.19 ms: 1.38x slower                                               |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-linux-x86_64-brandtbucher-jit_up_11_6-3.14.0a6+-a0aff13 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.0 ms: 1.50x faster                                               |
| mako            | 16.3 ms                                                | 11.0 ms: 1.49x faster                                               |
| genshi_text     | 31.8 ms                                                | 21.7 ms: 1.47x faster                                               |
| genshi_xml      | 66.0 ms                                                | 50.2 ms: 1.32x faster                                               |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-linux-x86_64-brandtbucher-jit_up_11_6-3.14.0a6+-a0aff13 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 169 us: 3.22x faster                                                |
| async_tree_io            | 1.77 sec                                               | 617 ms: 2.87x faster                                                |
| async_tree_none          | 728 ms                                                 | 260 ms: 2.80x faster                                                |
| generators               | 80.1 ms                                                | 28.8 ms: 2.78x faster                                               |
| async_tree_memoization   | 870 ms                                                 | 316 ms: 2.75x faster                                                |
| deltablue                | 7.91 ms                                                | 3.07 ms: 2.58x faster                                               |
| richards_super           | 94.7 ms                                                | 42.8 ms: 2.21x faster                                               |
| richards                 | 79.3 ms                                                | 37.7 ms: 2.10x faster                                               |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 490 ms: 2.07x faster                                                |
| deepcopy_memo            | 58.5 us                                                | 29.1 us: 2.01x faster                                               |
| pylint                   | 551 ms                                                 | 284 ms: 1.94x faster                                                |
| chaos                    | 115 ms                                                 | 60.0 ms: 1.92x faster                                               |
| logging_silent           | 190 ns                                                 | 99.6 ns: 1.90x faster                                               |
| raytrace                 | 507 ms                                                 | 268 ms: 1.89x faster                                                |
| go                       | 240 ms                                                 | 130 ms: 1.85x faster                                                |
| scimark_sor              | 220 ms                                                 | 121 ms: 1.82x faster                                                |
| deepcopy                 | 479 us                                                 | 264 us: 1.81x faster                                                |
| float                    | 117 ms                                                 | 65.7 ms: 1.78x faster                                               |
| nbody                    | 154 ms                                                 | 86.8 ms: 1.77x faster                                               |
| spectral_norm            | 170 ms                                                 | 96.6 ms: 1.76x faster                                               |
| scimark_monte_carlo      | 118 ms                                                 | 68.6 ms: 1.72x faster                                               |
| crypto_pyaes             | 128 ms                                                 | 75.8 ms: 1.69x faster                                               |
| tomli_loads              | 3.14 sec                                               | 1.88 sec: 1.67x faster                                              |
| pyflate                  | 716 ms                                                 | 458 ms: 1.57x faster                                                |
| unpickle_pure_python     | 331 us                                                 | 211 us: 1.56x faster                                                |
| deepcopy_reduce          | 4.17 us                                                | 2.73 us: 1.53x faster                                               |
| comprehensions           | 28.8 us                                                | 19.0 us: 1.51x faster                                               |
| hexiom                   | 10.4 ms                                                | 6.88 ms: 1.51x faster                                               |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.50x faster                                                |
| django_template          | 48.2 ms                                                | 32.0 ms: 1.50x faster                                               |
| scimark_fft              | 466 ms                                                 | 311 ms: 1.50x faster                                                |
| pickle_pure_python       | 484 us                                                 | 326 us: 1.49x faster                                                |
| mako                     | 16.3 ms                                                | 11.0 ms: 1.49x faster                                               |
| coroutines               | 35.1 ms                                                | 23.8 ms: 1.48x faster                                               |
| logging_simple           | 8.30 us                                                | 5.65 us: 1.47x faster                                               |
| genshi_text              | 31.8 ms                                                | 21.7 ms: 1.47x faster                                               |
| regex_compile            | 188 ms                                                 | 129 ms: 1.47x faster                                                |
| logging_format           | 9.09 us                                                | 6.26 us: 1.45x faster                                               |
| html5lib                 | 88.9 ms                                                | 61.9 ms: 1.44x faster                                               |
| xml_etree_process        | 79.1 ms                                                | 56.9 ms: 1.39x faster                                               |
| dulwich_log              | 84.3 ms                                                | 60.7 ms: 1.39x faster                                               |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.68 ms: 1.38x faster                                               |
| pprint_safe_repr         | 1.02 sec                                               | 738 ms: 1.38x faster                                                |
| thrift                   | 1.07 ms                                                | 780 us: 1.37x faster                                                |
| pprint_pformat           | 2.10 sec                                               | 1.55 sec: 1.36x faster                                              |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.2 ms: 1.36x faster                                               |
| pycparser                | 1.58 sec                                               | 1.19 sec: 1.32x faster                                              |
| genshi_xml               | 66.0 ms                                                | 50.2 ms: 1.32x faster                                               |
| 2to3                     | 348 ms                                                 | 265 ms: 1.32x faster                                                |
| sympy_sum                | 196 ms                                                 | 154 ms: 1.27x faster                                                |
| sympy_integrate          | 25.8 ms                                                | 20.3 ms: 1.27x faster                                               |
| sqlalchemy_declarative   | 172 ms                                                 | 136 ms: 1.26x faster                                                |
| fannkuch                 | 532 ms                                                 | 424 ms: 1.25x faster                                                |
| sympy_str                | 346 ms                                                 | 277 ms: 1.25x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 80.6 ms: 1.23x faster                                               |
| json_dumps               | 14.2 ms                                                | 11.6 ms: 1.22x faster                                               |
| nqueens                  | 106 ms                                                 | 86.7 ms: 1.22x faster                                               |
| pathlib                  | 20.5 ms                                                | 16.8 ms: 1.22x faster                                               |
| docutils                 | 3.30 sec                                               | 2.71 sec: 1.22x faster                                              |
| xml_etree_parse          | 168 ms                                                 | 139 ms: 1.21x faster                                                |
| sympy_expand             | 566 ms                                                 | 474 ms: 1.19x faster                                                |
| regex_v8                 | 27.8 ms                                                | 23.6 ms: 1.18x faster                                               |
| xml_etree_iterparse      | 115 ms                                                 | 98.0 ms: 1.18x faster                                               |
| mdp                      | 2.85 sec                                               | 2.51 sec: 1.14x faster                                              |
| sqlite_synth             | 3.02 us                                                | 2.71 us: 1.12x faster                                               |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.11x faster                                               |
| bench_thread_pool        | 986 us                                                 | 887 us: 1.11x faster                                                |
| meteor_contest           | 120 ms                                                 | 110 ms: 1.09x faster                                                |
| regex_effbot             | 3.63 ms                                                | 3.36 ms: 1.08x faster                                               |
| async_generators         | 444 ms                                                 | 415 ms: 1.07x faster                                                |
| json                     | 5.69 ms                                                | 5.40 ms: 1.05x faster                                               |
| json_loads               | 31.2 us                                                | 30.1 us: 1.04x faster                                               |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                |
| regex_dna                | 227 ms                                                 | 226 ms: 1.00x faster                                                |
| telco                    | 7.27 ms                                                | 7.86 ms: 1.08x slower                                               |
| coverage                 | 79.4 ms                                                | 86.2 ms: 1.08x slower                                               |
| gc_traversal             | 3.62 ms                                                | 4.65 ms: 1.28x slower                                               |
| python_startup_no_site   | 5.93 ms                                                | 8.19 ms: 1.38x slower                                               |
| create_gc_cycles         | 1.62 ms                                                | 2.47 ms: 1.52x slower                                               |
| bench_mp_pool            | 24.0 ms                                                | 83.1 ms: 3.46x slower                                               |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                        |
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250329-3.14.0a6+-a0aff13-JIT/bm-20250329-linux-x86_64-brandtbucher-jit_up_11_6-3.14.0a6+-a0aff13.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.436x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.29x