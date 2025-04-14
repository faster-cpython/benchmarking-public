# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_up_10_8
- machine: linux-x86_64
- commit hash: a00e400
- commit date: 2025-03-28
- overall geometric mean: 1.430x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250328-linux-x86_64-brandtbucher-jit_up_10_8-3.14.0a6+-a00e400 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 266 ms: 1.31x faster                                                |
| docutils       | 3.30 sec                                               | 2.70 sec: 1.22x faster                                              |
| html5lib       | 88.9 ms                                                | 62.5 ms: 1.42x faster                                               |
| Geometric mean | (ref)                                                  | 1.31x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250328-linux-x86_64-brandtbucher-jit_up_10_8-3.14.0a6+-a00e400 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 621 ms: 2.85x faster                                                |
| async_tree_none         | 728 ms                                                 | 262 ms: 2.78x faster                                                |
| async_tree_memoization  | 870 ms                                                 | 317 ms: 2.74x faster                                                |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 493 ms: 2.06x faster                                                |
| Geometric mean          | (ref)                                                  | 2.59x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250328-linux-x86_64-brandtbucher-jit_up_10_8-3.14.0a6+-a00e400 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 117 ms                                                 | 65.4 ms: 1.79x faster                                               |
| nbody          | 154 ms                                                 | 87.3 ms: 1.76x faster                                               |
| pidigits       | 191 ms                                                 | 185 ms: 1.03x faster                                                |
| Geometric mean | (ref)                                                  | 1.48x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250328-linux-x86_64-brandtbucher-jit_up_10_8-3.14.0a6+-a00e400 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.47x faster                                                |
| regex_v8       | 27.8 ms                                                | 24.0 ms: 1.16x faster                                               |
| regex_effbot   | 3.63 ms                                                | 3.54 ms: 1.02x faster                                               |
| Geometric mean | (ref)                                                  | 1.15x faster                                                        |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250328-linux-x86_64-brandtbucher-jit_up_10_8-3.14.0a6+-a00e400 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.89 sec: 1.66x faster                                              |
| unpickle_pure_python | 331 us                                                 | 212 us: 1.56x faster                                                |
| pickle_pure_python   | 484 us                                                 | 325 us: 1.49x faster                                                |
| xml_etree_process    | 79.1 ms                                                | 56.5 ms: 1.40x faster                                               |
| xml_etree_generate   | 99.4 ms                                                | 80.2 ms: 1.24x faster                                               |
| json_dumps           | 14.2 ms                                                | 11.7 ms: 1.21x faster                                               |
| xml_etree_parse      | 168 ms                                                 | 139 ms: 1.21x faster                                                |
| xml_etree_iterparse  | 115 ms                                                 | 98.0 ms: 1.18x faster                                               |
| json_loads           | 31.2 us                                                | 30.0 us: 1.04x faster                                               |
| Geometric mean       | (ref)                                                  | 1.32x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250328-linux-x86_64-brandtbucher-jit_up_10_8-3.14.0a6+-a00e400 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.2 ms: 1.11x faster                                               |
| python_startup_no_site | 5.93 ms                                                | 8.23 ms: 1.39x slower                                               |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250328-linux-x86_64-brandtbucher-jit_up_10_8-3.14.0a6+-a00e400 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.2 ms: 1.50x faster                                               |
| mako            | 16.3 ms                                                | 11.0 ms: 1.49x faster                                               |
| genshi_text     | 31.8 ms                                                | 21.6 ms: 1.47x faster                                               |
| genshi_xml      | 66.0 ms                                                | 50.0 ms: 1.32x faster                                               |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250328-linux-x86_64-brandtbucher-jit_up_10_8-3.14.0a6+-a00e400 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 169 us: 3.23x faster                                                |
| async_tree_io            | 1.77 sec                                               | 621 ms: 2.85x faster                                                |
| async_tree_none          | 728 ms                                                 | 262 ms: 2.78x faster                                                |
| async_tree_memoization   | 870 ms                                                 | 317 ms: 2.74x faster                                                |
| generators               | 80.1 ms                                                | 29.4 ms: 2.73x faster                                               |
| deltablue                | 7.91 ms                                                | 3.05 ms: 2.59x faster                                               |
| richards_super           | 94.7 ms                                                | 42.9 ms: 2.21x faster                                               |
| richards                 | 79.3 ms                                                | 37.0 ms: 2.14x faster                                               |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 493 ms: 2.06x faster                                                |
| deepcopy_memo            | 58.5 us                                                | 29.1 us: 2.01x faster                                               |
| pylint                   | 551 ms                                                 | 284 ms: 1.94x faster                                                |
| logging_silent           | 190 ns                                                 | 99.5 ns: 1.91x faster                                               |
| chaos                    | 115 ms                                                 | 60.6 ms: 1.91x faster                                               |
| raytrace                 | 507 ms                                                 | 268 ms: 1.89x faster                                                |
| go                       | 240 ms                                                 | 129 ms: 1.86x faster                                                |
| deepcopy                 | 479 us                                                 | 261 us: 1.83x faster                                                |
| scimark_sor              | 220 ms                                                 | 120 ms: 1.83x faster                                                |
| float                    | 117 ms                                                 | 65.4 ms: 1.79x faster                                               |
| nbody                    | 154 ms                                                 | 87.3 ms: 1.76x faster                                               |
| spectral_norm            | 170 ms                                                 | 98.8 ms: 1.72x faster                                               |
| scimark_monte_carlo      | 118 ms                                                 | 68.8 ms: 1.72x faster                                               |
| crypto_pyaes             | 128 ms                                                 | 75.2 ms: 1.70x faster                                               |
| tomli_loads              | 3.14 sec                                               | 1.89 sec: 1.66x faster                                              |
| pyflate                  | 716 ms                                                 | 447 ms: 1.60x faster                                                |
| unpickle_pure_python     | 331 us                                                 | 212 us: 1.56x faster                                                |
| comprehensions           | 28.8 us                                                | 18.5 us: 1.56x faster                                               |
| deepcopy_reduce          | 4.17 us                                                | 2.70 us: 1.54x faster                                               |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.51x faster                                                |
| django_template          | 48.2 ms                                                | 32.2 ms: 1.50x faster                                               |
| pickle_pure_python       | 484 us                                                 | 325 us: 1.49x faster                                                |
| mako                     | 16.3 ms                                                | 11.0 ms: 1.49x faster                                               |
| coroutines               | 35.1 ms                                                | 23.6 ms: 1.48x faster                                               |
| logging_simple           | 8.30 us                                                | 5.63 us: 1.47x faster                                               |
| genshi_text              | 31.8 ms                                                | 21.6 ms: 1.47x faster                                               |
| hexiom                   | 10.4 ms                                                | 7.07 ms: 1.47x faster                                               |
| regex_compile            | 188 ms                                                 | 129 ms: 1.47x faster                                                |
| scimark_fft              | 466 ms                                                 | 318 ms: 1.46x faster                                                |
| logging_format           | 9.09 us                                                | 6.21 us: 1.46x faster                                               |
| html5lib                 | 88.9 ms                                                | 62.5 ms: 1.42x faster                                               |
| xml_etree_process        | 79.1 ms                                                | 56.5 ms: 1.40x faster                                               |
| dulwich_log              | 84.3 ms                                                | 60.6 ms: 1.39x faster                                               |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.79 ms: 1.35x faster                                               |
| thrift                   | 1.07 ms                                                | 796 us: 1.35x faster                                                |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.34x faster                                              |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.5 ms: 1.34x faster                                               |
| genshi_xml               | 66.0 ms                                                | 50.0 ms: 1.32x faster                                               |
| pprint_safe_repr         | 1.02 sec                                               | 774 ms: 1.32x faster                                                |
| 2to3                     | 348 ms                                                 | 266 ms: 1.31x faster                                                |
| pprint_pformat           | 2.10 sec                                               | 1.63 sec: 1.29x faster                                              |
| sympy_integrate          | 25.8 ms                                                | 20.3 ms: 1.27x faster                                               |
| sqlalchemy_declarative   | 172 ms                                                 | 136 ms: 1.26x faster                                                |
| sympy_sum                | 196 ms                                                 | 156 ms: 1.26x faster                                                |
| fannkuch                 | 532 ms                                                 | 426 ms: 1.25x faster                                                |
| sympy_str                | 346 ms                                                 | 279 ms: 1.24x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 80.2 ms: 1.24x faster                                               |
| pathlib                  | 20.5 ms                                                | 16.8 ms: 1.22x faster                                               |
| docutils                 | 3.30 sec                                               | 2.70 sec: 1.22x faster                                              |
| nqueens                  | 106 ms                                                 | 87.5 ms: 1.21x faster                                               |
| json_dumps               | 14.2 ms                                                | 11.7 ms: 1.21x faster                                               |
| xml_etree_parse          | 168 ms                                                 | 139 ms: 1.21x faster                                                |
| sympy_expand             | 566 ms                                                 | 478 ms: 1.18x faster                                                |
| xml_etree_iterparse      | 115 ms                                                 | 98.0 ms: 1.18x faster                                               |
| regex_v8                 | 27.8 ms                                                | 24.0 ms: 1.16x faster                                               |
| mdp                      | 2.85 sec                                               | 2.50 sec: 1.14x faster                                              |
| sqlite_synth             | 3.02 us                                                | 2.73 us: 1.11x faster                                               |
| python_startup           | 14.6 ms                                                | 13.2 ms: 1.11x faster                                               |
| bench_thread_pool        | 986 us                                                 | 892 us: 1.11x faster                                                |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                                |
| json                     | 5.69 ms                                                | 5.29 ms: 1.08x faster                                               |
| async_generators         | 444 ms                                                 | 419 ms: 1.06x faster                                                |
| json_loads               | 31.2 us                                                | 30.0 us: 1.04x faster                                               |
| pidigits                 | 191 ms                                                 | 185 ms: 1.03x faster                                                |
| regex_effbot             | 3.63 ms                                                | 3.54 ms: 1.02x faster                                               |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                |
| telco                    | 7.27 ms                                                | 7.78 ms: 1.07x slower                                               |
| coverage                 | 79.4 ms                                                | 86.0 ms: 1.08x slower                                               |
| gc_traversal             | 3.62 ms                                                | 4.91 ms: 1.36x slower                                               |
| python_startup_no_site   | 5.93 ms                                                | 8.23 ms: 1.39x slower                                               |
| create_gc_cycles         | 1.62 ms                                                | 2.49 ms: 1.54x slower                                               |
| bench_mp_pool            | 24.0 ms                                                | 83.5 ms: 3.48x slower                                               |
| Geometric mean           | (ref)                                                  | 1.40x faster                                                        |

Benchmark hidden because not significant (1): regex_dna
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250328-3.14.0a6+-a00e400-JIT/bm-20250328-linux-x86_64-brandtbucher-jit_up_10_8-3.14.0a6+-a00e400.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.430x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.30x