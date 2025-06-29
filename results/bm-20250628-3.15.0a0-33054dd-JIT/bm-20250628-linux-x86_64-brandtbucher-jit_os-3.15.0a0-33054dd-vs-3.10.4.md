# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_os
- machine: linux-x86_64
- commit hash: 33054dd
- commit date: 2025-06-28
- overall geometric mean: 1.488x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.34x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-linux-x86_64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 260 ms: 1.34x faster                                          |
| docutils       | 3.30 sec                                               | 2.62 sec: 1.26x faster                                        |
| html5lib       | 88.9 ms                                                | 62.0 ms: 1.43x faster                                         |
| Geometric mean | (ref)                                                  | 1.34x faster                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-linux-x86_64-brandtbucher-jit_os-3.15.0a0-33054dd |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 601 ms: 2.94x faster                                          |
| async_tree_memoization  | 870 ms                                                 | 312 ms: 2.79x faster                                          |
| async_tree_none         | 728 ms                                                 | 262 ms: 2.78x faster                                          |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 492 ms: 2.07x faster                                          |
| Geometric mean          | (ref)                                                  | 2.62x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-linux-x86_64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 117 ms                                                 | 65.2 ms: 1.80x faster                                         |
| nbody          | 154 ms                                                 | 97.9 ms: 1.57x faster                                         |
| pidigits       | 191 ms                                                 | 188 ms: 1.01x faster                                          |
| Geometric mean | (ref)                                                  | 1.42x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-linux-x86_64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.49x faster                                          |
| regex_v8       | 27.8 ms                                                | 22.4 ms: 1.24x faster                                         |
| regex_effbot   | 3.63 ms                                                | 3.25 ms: 1.12x faster                                         |
| regex_dna      | 227 ms                                                 | 207 ms: 1.09x faster                                          |
| Geometric mean | (ref)                                                  | 1.23x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-linux-x86_64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.83 sec: 1.72x faster                                        |
| unpickle_pure_python | 331 us                                                 | 194 us: 1.70x faster                                          |
| pickle_pure_python   | 484 us                                                 | 319 us: 1.52x faster                                          |
| xml_etree_process    | 79.1 ms                                                | 55.3 ms: 1.43x faster                                         |
| json_dumps           | 14.2 ms                                                | 11.1 ms: 1.28x faster                                         |
| xml_etree_generate   | 99.4 ms                                                | 79.9 ms: 1.24x faster                                         |
| xml_etree_parse      | 168 ms                                                 | 140 ms: 1.20x faster                                          |
| xml_etree_iterparse  | 115 ms                                                 | 99.0 ms: 1.17x faster                                         |
| json_loads           | 31.2 us                                                | 28.5 us: 1.10x faster                                         |
| Geometric mean       | (ref)                                                  | 1.36x faster                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-linux-x86_64-brandtbucher-jit_os-3.15.0a0-33054dd |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.2 ms: 1.19x faster                                         |
| python_startup_no_site | 5.93 ms                                                | 6.96 ms: 1.17x slower                                         |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-linux-x86_64-brandtbucher-jit_os-3.15.0a0-33054dd |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.5 ms: 1.55x faster                                         |
| django_template | 48.2 ms                                                | 32.4 ms: 1.49x faster                                         |
| genshi_text     | 31.8 ms                                                | 21.8 ms: 1.46x faster                                         |
| genshi_xml      | 66.0 ms                                                | 49.7 ms: 1.33x faster                                         |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-linux-x86_64-brandtbucher-jit_os-3.15.0a0-33054dd |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 166 us: 3.28x faster                                          |
| async_tree_io            | 1.77 sec                                               | 601 ms: 2.94x faster                                          |
| async_tree_memoization   | 870 ms                                                 | 312 ms: 2.79x faster                                          |
| async_tree_none          | 728 ms                                                 | 262 ms: 2.78x faster                                          |
| generators               | 80.1 ms                                                | 30.4 ms: 2.63x faster                                         |
| deltablue                | 7.91 ms                                                | 3.03 ms: 2.61x faster                                         |
| richards_super           | 94.7 ms                                                | 37.8 ms: 2.51x faster                                         |
| richards                 | 79.3 ms                                                | 32.1 ms: 2.47x faster                                         |
| mdp                      | 2.85 sec                                               | 1.23 sec: 2.32x faster                                        |
| go                       | 240 ms                                                 | 115 ms: 2.08x faster                                          |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 492 ms: 2.07x faster                                          |
| deepcopy_memo            | 58.5 us                                                | 29.5 us: 1.98x faster                                         |
| pylint                   | 551 ms                                                 | 282 ms: 1.96x faster                                          |
| chaos                    | 115 ms                                                 | 61.6 ms: 1.87x faster                                         |
| deepcopy                 | 479 us                                                 | 257 us: 1.86x faster                                          |
| scimark_sor              | 220 ms                                                 | 118 ms: 1.86x faster                                          |
| spectral_norm            | 170 ms                                                 | 91.8 ms: 1.85x faster                                         |
| raytrace                 | 507 ms                                                 | 274 ms: 1.85x faster                                          |
| logging_silent           | 190 ns                                                 | 105 ns: 1.81x faster                                          |
| scimark_monte_carlo      | 118 ms                                                 | 65.5 ms: 1.81x faster                                         |
| float                    | 117 ms                                                 | 65.2 ms: 1.80x faster                                         |
| pyflate                  | 716 ms                                                 | 411 ms: 1.74x faster                                          |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                         |
| crypto_pyaes             | 128 ms                                                 | 74.4 ms: 1.72x faster                                         |
| tomli_loads              | 3.14 sec                                               | 1.83 sec: 1.72x faster                                        |
| unpickle_pure_python     | 331 us                                                 | 194 us: 1.70x faster                                          |
| djangocms                | 38.4 us                                                | 22.8 us: 1.68x faster                                         |
| hexiom                   | 10.4 ms                                                | 6.23 ms: 1.67x faster                                         |
| nbody                    | 154 ms                                                 | 97.9 ms: 1.57x faster                                         |
| deepcopy_reduce          | 4.17 us                                                | 2.68 us: 1.56x faster                                         |
| mako                     | 16.3 ms                                                | 10.5 ms: 1.55x faster                                         |
| pickle_pure_python       | 484 us                                                 | 319 us: 1.52x faster                                          |
| scimark_fft              | 466 ms                                                 | 312 ms: 1.49x faster                                          |
| regex_compile            | 188 ms                                                 | 127 ms: 1.49x faster                                          |
| pprint_pformat           | 2.10 sec                                               | 1.41 sec: 1.49x faster                                        |
| django_template          | 48.2 ms                                                | 32.4 ms: 1.49x faster                                         |
| scimark_lu               | 176 ms                                                 | 119 ms: 1.48x faster                                          |
| logging_simple           | 8.30 us                                                | 5.64 us: 1.47x faster                                         |
| genshi_text              | 31.8 ms                                                | 21.8 ms: 1.46x faster                                         |
| pprint_safe_repr         | 1.02 sec                                               | 702 ms: 1.45x faster                                          |
| logging_format           | 9.09 us                                                | 6.29 us: 1.45x faster                                         |
| html5lib                 | 88.9 ms                                                | 62.0 ms: 1.43x faster                                         |
| xml_etree_process        | 79.1 ms                                                | 55.3 ms: 1.43x faster                                         |
| dulwich_log              | 84.3 ms                                                | 59.1 ms: 1.43x faster                                         |
| pycparser                | 1.58 sec                                               | 1.11 sec: 1.41x faster                                        |
| thrift                   | 1.07 ms                                                | 769 us: 1.39x faster                                          |
| coroutines               | 35.1 ms                                                | 25.5 ms: 1.37x faster                                         |
| fannkuch                 | 532 ms                                                 | 393 ms: 1.35x faster                                          |
| 2to3                     | 348 ms                                                 | 260 ms: 1.34x faster                                          |
| sympy_integrate          | 25.8 ms                                                | 19.3 ms: 1.34x faster                                         |
| genshi_xml               | 66.0 ms                                                | 49.7 ms: 1.33x faster                                         |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.32x faster                                          |
| nqueens                  | 106 ms                                                 | 82.6 ms: 1.28x faster                                         |
| json_dumps               | 14.2 ms                                                | 11.1 ms: 1.28x faster                                         |
| sympy_str                | 346 ms                                                 | 270 ms: 1.28x faster                                          |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.07 ms: 1.28x faster                                         |
| docutils                 | 3.30 sec                                               | 2.62 sec: 1.26x faster                                        |
| xml_etree_generate       | 99.4 ms                                                | 79.9 ms: 1.24x faster                                         |
| regex_v8                 | 27.8 ms                                                | 22.4 ms: 1.24x faster                                         |
| sympy_expand             | 566 ms                                                 | 465 ms: 1.22x faster                                          |
| pathlib                  | 20.5 ms                                                | 17.0 ms: 1.20x faster                                         |
| xml_etree_parse          | 168 ms                                                 | 140 ms: 1.20x faster                                          |
| python_startup           | 14.6 ms                                                | 12.2 ms: 1.19x faster                                         |
| xml_etree_iterparse      | 115 ms                                                 | 99.0 ms: 1.17x faster                                         |
| meteor_contest           | 120 ms                                                 | 105 ms: 1.14x faster                                          |
| regex_effbot             | 3.63 ms                                                | 3.25 ms: 1.12x faster                                         |
| json_loads               | 31.2 us                                                | 28.5 us: 1.10x faster                                         |
| regex_dna                | 227 ms                                                 | 207 ms: 1.09x faster                                          |
| sqlite_synth             | 3.02 us                                                | 2.80 us: 1.08x faster                                         |
| json                     | 5.69 ms                                                | 5.30 ms: 1.07x faster                                         |
| async_generators         | 444 ms                                                 | 431 ms: 1.03x faster                                          |
| pidigits                 | 191 ms                                                 | 188 ms: 1.01x faster                                          |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                          |
| telco                    | 7.27 ms                                                | 7.61 ms: 1.05x slower                                         |
| coverage                 | 79.4 ms                                                | 87.9 ms: 1.11x slower                                         |
| python_startup_no_site   | 5.93 ms                                                | 6.96 ms: 1.17x slower                                         |
| gc_traversal             | 3.62 ms                                                | 5.09 ms: 1.40x slower                                         |
| create_gc_cycles         | 1.62 ms                                                | 2.59 ms: 1.60x slower                                         |
| Geometric mean           | (ref)                                                  | 1.49x faster                                                  |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250628-3.15.0a0-33054dd-JIT/bm-20250628-linux-x86_64-brandtbucher-jit_os-3.15.0a0-33054dd.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.488x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.39x
- 95% likely to have a speedup of 1.38x
- 99% likely to have a speedup of 1.34x

# Memory
- memory change: 1.33x