# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_up_11_12
- machine: linux-x86_64
- commit hash: c4993c9
- commit date: 2025-03-26
- overall geometric mean: 1.434x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-linux-x86_64-brandtbucher-jit_up_11_12-3.14.0a6+-c4993c9 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 263 ms: 1.32x faster                                                 |
| docutils       | 3.30 sec                                               | 2.71 sec: 1.21x faster                                               |
| html5lib       | 88.9 ms                                                | 62.7 ms: 1.42x faster                                                |
| Geometric mean | (ref)                                                  | 1.32x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-linux-x86_64-brandtbucher-jit_up_11_12-3.14.0a6+-c4993c9 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 616 ms: 2.87x faster                                                 |
| async_tree_none         | 728 ms                                                 | 261 ms: 2.79x faster                                                 |
| async_tree_memoization  | 870 ms                                                 | 316 ms: 2.75x faster                                                 |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 493 ms: 2.06x faster                                                 |
| Geometric mean          | (ref)                                                  | 2.60x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-linux-x86_64-brandtbucher-jit_up_11_12-3.14.0a6+-c4993c9 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 117 ms                                                 | 65.5 ms: 1.79x faster                                                |
| nbody          | 154 ms                                                 | 87.9 ms: 1.75x faster                                                |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                  | 1.48x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-linux-x86_64-brandtbucher-jit_up_11_12-3.14.0a6+-c4993c9 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.47x faster                                                 |
| regex_v8       | 27.8 ms                                                | 23.9 ms: 1.16x faster                                                |
| regex_effbot   | 3.63 ms                                                | 3.54 ms: 1.02x faster                                                |
| regex_dna      | 227 ms                                                 | 228 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.15x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-linux-x86_64-brandtbucher-jit_up_11_12-3.14.0a6+-c4993c9 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.84 sec: 1.70x faster                                               |
| unpickle_pure_python | 331 us                                                 | 212 us: 1.56x faster                                                 |
| pickle_pure_python   | 484 us                                                 | 327 us: 1.48x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 56.9 ms: 1.39x faster                                                |
| xml_etree_generate   | 99.4 ms                                                | 80.3 ms: 1.24x faster                                                |
| json_dumps           | 14.2 ms                                                | 11.5 ms: 1.23x faster                                                |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.20x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 98.5 ms: 1.17x faster                                                |
| json_loads           | 31.2 us                                                | 29.9 us: 1.04x faster                                                |
| Geometric mean       | (ref)                                                  | 1.32x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-linux-x86_64-brandtbucher-jit_up_11_12-3.14.0a6+-c4993c9 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.12x faster                                                |
| python_startup_no_site | 5.93 ms                                                | 8.17 ms: 1.38x slower                                                |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-linux-x86_64-brandtbucher-jit_up_11_12-3.14.0a6+-c4993c9 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.0 ms: 1.48x faster                                                |
| django_template | 48.2 ms                                                | 32.5 ms: 1.48x faster                                                |
| genshi_text     | 31.8 ms                                                | 21.6 ms: 1.47x faster                                                |
| genshi_xml      | 66.0 ms                                                | 50.4 ms: 1.31x faster                                                |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-linux-x86_64-brandtbucher-jit_up_11_12-3.14.0a6+-c4993c9 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 170 us: 3.19x faster                                                 |
| async_tree_io            | 1.77 sec                                               | 616 ms: 2.87x faster                                                 |
| async_tree_none          | 728 ms                                                 | 261 ms: 2.79x faster                                                 |
| generators               | 80.1 ms                                                | 28.8 ms: 2.78x faster                                                |
| async_tree_memoization   | 870 ms                                                 | 316 ms: 2.75x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.05 ms: 2.59x faster                                                |
| richards_super           | 94.7 ms                                                | 44.2 ms: 2.14x faster                                                |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 493 ms: 2.06x faster                                                 |
| richards                 | 79.3 ms                                                | 39.0 ms: 2.03x faster                                                |
| deepcopy_memo            | 58.5 us                                                | 29.5 us: 1.98x faster                                                |
| pylint                   | 551 ms                                                 | 281 ms: 1.96x faster                                                 |
| chaos                    | 115 ms                                                 | 60.0 ms: 1.92x faster                                                |
| logging_silent           | 190 ns                                                 | 98.8 ns: 1.92x faster                                                |
| raytrace                 | 507 ms                                                 | 269 ms: 1.89x faster                                                 |
| go                       | 240 ms                                                 | 129 ms: 1.86x faster                                                 |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.85x faster                                                 |
| deepcopy                 | 479 us                                                 | 265 us: 1.81x faster                                                 |
| spectral_norm            | 170 ms                                                 | 94.6 ms: 1.80x faster                                                |
| float                    | 117 ms                                                 | 65.5 ms: 1.79x faster                                                |
| nbody                    | 154 ms                                                 | 87.9 ms: 1.75x faster                                                |
| scimark_monte_carlo      | 118 ms                                                 | 68.4 ms: 1.73x faster                                                |
| tomli_loads              | 3.14 sec                                               | 1.84 sec: 1.70x faster                                               |
| crypto_pyaes             | 128 ms                                                 | 75.9 ms: 1.68x faster                                                |
| pyflate                  | 716 ms                                                 | 451 ms: 1.59x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 212 us: 1.56x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.79 ms: 1.53x faster                                                |
| deepcopy_reduce          | 4.17 us                                                | 2.73 us: 1.53x faster                                                |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.52x faster                                                 |
| comprehensions           | 28.8 us                                                | 18.9 us: 1.52x faster                                                |
| scimark_fft              | 466 ms                                                 | 312 ms: 1.49x faster                                                 |
| coroutines               | 35.1 ms                                                | 23.6 ms: 1.49x faster                                                |
| mako                     | 16.3 ms                                                | 11.0 ms: 1.48x faster                                                |
| django_template          | 48.2 ms                                                | 32.5 ms: 1.48x faster                                                |
| pickle_pure_python       | 484 us                                                 | 327 us: 1.48x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.62 us: 1.48x faster                                                |
| genshi_text              | 31.8 ms                                                | 21.6 ms: 1.47x faster                                                |
| regex_compile            | 188 ms                                                 | 128 ms: 1.47x faster                                                 |
| logging_format           | 9.09 us                                                | 6.19 us: 1.47x faster                                                |
| html5lib                 | 88.9 ms                                                | 62.7 ms: 1.42x faster                                                |
| dulwich_log              | 84.3 ms                                                | 60.4 ms: 1.40x faster                                                |
| xml_etree_process        | 79.1 ms                                                | 56.9 ms: 1.39x faster                                                |
| thrift                   | 1.07 ms                                                | 780 us: 1.37x faster                                                 |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.2 ms: 1.36x faster                                                |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.76 ms: 1.36x faster                                                |
| pprint_safe_repr         | 1.02 sec                                               | 752 ms: 1.35x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.33x faster                                               |
| 2to3                     | 348 ms                                                 | 263 ms: 1.32x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.59 sec: 1.32x faster                                               |
| genshi_xml               | 66.0 ms                                                | 50.4 ms: 1.31x faster                                                |
| sympy_sum                | 196 ms                                                 | 153 ms: 1.28x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 20.2 ms: 1.28x faster                                                |
| sqlalchemy_declarative   | 172 ms                                                 | 135 ms: 1.28x faster                                                 |
| nqueens                  | 106 ms                                                 | 83.9 ms: 1.26x faster                                                |
| sympy_str                | 346 ms                                                 | 277 ms: 1.25x faster                                                 |
| fannkuch                 | 532 ms                                                 | 426 ms: 1.25x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 80.3 ms: 1.24x faster                                                |
| json_dumps               | 14.2 ms                                                | 11.5 ms: 1.23x faster                                                |
| pathlib                  | 20.5 ms                                                | 16.8 ms: 1.21x faster                                                |
| docutils                 | 3.30 sec                                               | 2.71 sec: 1.21x faster                                               |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.20x faster                                                 |
| sympy_expand             | 566 ms                                                 | 479 ms: 1.18x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 98.5 ms: 1.17x faster                                                |
| regex_v8                 | 27.8 ms                                                | 23.9 ms: 1.16x faster                                                |
| mdp                      | 2.85 sec                                               | 2.50 sec: 1.14x faster                                               |
| bench_thread_pool        | 986 us                                                 | 884 us: 1.12x faster                                                 |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.12x faster                                                |
| sqlite_synth             | 3.02 us                                                | 2.73 us: 1.11x faster                                                |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                                 |
| json                     | 5.69 ms                                                | 5.30 ms: 1.07x faster                                                |
| async_generators         | 444 ms                                                 | 415 ms: 1.07x faster                                                 |
| json_loads               | 31.2 us                                                | 29.9 us: 1.04x faster                                                |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                 |
| regex_effbot             | 3.63 ms                                                | 3.54 ms: 1.02x faster                                                |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                 |
| regex_dna                | 227 ms                                                 | 228 ms: 1.01x slower                                                 |
| telco                    | 7.27 ms                                                | 7.87 ms: 1.08x slower                                                |
| coverage                 | 79.4 ms                                                | 86.2 ms: 1.08x slower                                                |
| gc_traversal             | 3.62 ms                                                | 4.75 ms: 1.31x slower                                                |
| python_startup_no_site   | 5.93 ms                                                | 8.17 ms: 1.38x slower                                                |
| create_gc_cycles         | 1.62 ms                                                | 2.47 ms: 1.53x slower                                                |
| bench_mp_pool            | 24.0 ms                                                | 83.0 ms: 3.46x slower                                                |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                         |
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250326-3.14.0a6+-c4993c9-JIT/bm-20250326-linux-x86_64-brandtbucher-jit_up_11_12-3.14.0a6+-c4993c9.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.434x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.29x