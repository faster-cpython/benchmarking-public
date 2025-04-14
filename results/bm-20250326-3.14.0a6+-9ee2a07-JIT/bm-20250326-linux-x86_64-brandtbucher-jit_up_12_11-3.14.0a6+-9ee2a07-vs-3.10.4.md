# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_up_12_11
- machine: linux-x86_64
- commit hash: 9ee2a07
- commit date: 2025-03-26
- overall geometric mean: 1.438x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-linux-x86_64-brandtbucher-jit_up_12_11-3.14.0a6+-9ee2a07 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 264 ms: 1.32x faster                                                 |
| docutils       | 3.30 sec                                               | 2.69 sec: 1.23x faster                                               |
| html5lib       | 88.9 ms                                                | 62.3 ms: 1.43x faster                                                |
| Geometric mean | (ref)                                                  | 1.32x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-linux-x86_64-brandtbucher-jit_up_12_11-3.14.0a6+-9ee2a07 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 619 ms: 2.86x faster                                                 |
| async_tree_memoization  | 870 ms                                                 | 317 ms: 2.74x faster                                                 |
| async_tree_none         | 728 ms                                                 | 266 ms: 2.74x faster                                                 |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 494 ms: 2.06x faster                                                 |
| Geometric mean          | (ref)                                                  | 2.58x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-linux-x86_64-brandtbucher-jit_up_12_11-3.14.0a6+-9ee2a07 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 117 ms                                                 | 65.4 ms: 1.79x faster                                                |
| nbody          | 154 ms                                                 | 87.9 ms: 1.75x faster                                                |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                  | 1.48x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-linux-x86_64-brandtbucher-jit_up_12_11-3.14.0a6+-9ee2a07 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.47x faster                                                 |
| regex_v8       | 27.8 ms                                                | 23.9 ms: 1.16x faster                                                |
| regex_effbot   | 3.63 ms                                                | 3.48 ms: 1.04x faster                                                |
| Geometric mean | (ref)                                                  | 1.16x faster                                                         |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-linux-x86_64-brandtbucher-jit_up_12_11-3.14.0a6+-9ee2a07 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.88 sec: 1.67x faster                                               |
| unpickle_pure_python | 331 us                                                 | 212 us: 1.56x faster                                                 |
| pickle_pure_python   | 484 us                                                 | 321 us: 1.51x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 57.0 ms: 1.39x faster                                                |
| xml_etree_generate   | 99.4 ms                                                | 80.5 ms: 1.23x faster                                                |
| json_dumps           | 14.2 ms                                                | 11.5 ms: 1.23x faster                                                |
| xml_etree_parse      | 168 ms                                                 | 139 ms: 1.21x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 97.2 ms: 1.19x faster                                                |
| json_loads           | 31.2 us                                                | 29.9 us: 1.04x faster                                                |
| Geometric mean       | (ref)                                                  | 1.32x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-linux-x86_64-brandtbucher-jit_up_12_11-3.14.0a6+-9ee2a07 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.11x faster                                                |
| python_startup_no_site | 5.93 ms                                                | 8.18 ms: 1.38x slower                                                |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-linux-x86_64-brandtbucher-jit_up_12_11-3.14.0a6+-9ee2a07 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 21.3 ms: 1.50x faster                                                |
| mako            | 16.3 ms                                                | 11.0 ms: 1.49x faster                                                |
| django_template | 48.2 ms                                                | 32.4 ms: 1.48x faster                                                |
| genshi_xml      | 66.0 ms                                                | 50.4 ms: 1.31x faster                                                |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-linux-x86_64-brandtbucher-jit_up_12_11-3.14.0a6+-9ee2a07 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 168 us: 3.23x faster                                                 |
| async_tree_io            | 1.77 sec                                               | 619 ms: 2.86x faster                                                 |
| generators               | 80.1 ms                                                | 28.9 ms: 2.77x faster                                                |
| async_tree_memoization   | 870 ms                                                 | 317 ms: 2.74x faster                                                 |
| async_tree_none          | 728 ms                                                 | 266 ms: 2.74x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.05 ms: 2.60x faster                                                |
| richards_super           | 94.7 ms                                                | 40.6 ms: 2.33x faster                                                |
| richards                 | 79.3 ms                                                | 35.9 ms: 2.21x faster                                                |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 494 ms: 2.06x faster                                                 |
| deepcopy_memo            | 58.5 us                                                | 29.0 us: 2.02x faster                                                |
| pylint                   | 551 ms                                                 | 282 ms: 1.96x faster                                                 |
| chaos                    | 115 ms                                                 | 59.9 ms: 1.93x faster                                                |
| logging_silent           | 190 ns                                                 | 98.4 ns: 1.93x faster                                                |
| raytrace                 | 507 ms                                                 | 268 ms: 1.89x faster                                                 |
| deepcopy                 | 479 us                                                 | 261 us: 1.84x faster                                                 |
| scimark_sor              | 220 ms                                                 | 120 ms: 1.83x faster                                                 |
| spectral_norm            | 170 ms                                                 | 93.0 ms: 1.83x faster                                                |
| go                       | 240 ms                                                 | 133 ms: 1.80x faster                                                 |
| float                    | 117 ms                                                 | 65.4 ms: 1.79x faster                                                |
| scimark_monte_carlo      | 118 ms                                                 | 67.6 ms: 1.75x faster                                                |
| nbody                    | 154 ms                                                 | 87.9 ms: 1.75x faster                                                |
| tomli_loads              | 3.14 sec                                               | 1.88 sec: 1.67x faster                                               |
| crypto_pyaes             | 128 ms                                                 | 78.6 ms: 1.63x faster                                                |
| pyflate                  | 716 ms                                                 | 443 ms: 1.62x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 212 us: 1.56x faster                                                 |
| comprehensions           | 28.8 us                                                | 19.0 us: 1.52x faster                                                |
| deepcopy_reduce          | 4.17 us                                                | 2.75 us: 1.52x faster                                                |
| pickle_pure_python       | 484 us                                                 | 321 us: 1.51x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.90 ms: 1.51x faster                                                |
| coroutines               | 35.1 ms                                                | 23.3 ms: 1.50x faster                                                |
| scimark_lu               | 176 ms                                                 | 118 ms: 1.50x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.54 us: 1.50x faster                                                |
| genshi_text              | 31.8 ms                                                | 21.3 ms: 1.50x faster                                                |
| scimark_fft              | 466 ms                                                 | 312 ms: 1.49x faster                                                 |
| mako                     | 16.3 ms                                                | 11.0 ms: 1.49x faster                                                |
| django_template          | 48.2 ms                                                | 32.4 ms: 1.48x faster                                                |
| regex_compile            | 188 ms                                                 | 128 ms: 1.47x faster                                                 |
| logging_format           | 9.09 us                                                | 6.22 us: 1.46x faster                                                |
| html5lib                 | 88.9 ms                                                | 62.3 ms: 1.43x faster                                                |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.63 ms: 1.40x faster                                                |
| xml_etree_process        | 79.1 ms                                                | 57.0 ms: 1.39x faster                                                |
| dulwich_log              | 84.3 ms                                                | 60.8 ms: 1.39x faster                                                |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.2 ms: 1.36x faster                                                |
| thrift                   | 1.07 ms                                                | 792 us: 1.35x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.57 sec: 1.34x faster                                               |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.33x faster                                               |
| 2to3                     | 348 ms                                                 | 264 ms: 1.32x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 50.4 ms: 1.31x faster                                                |
| pprint_safe_repr         | 1.02 sec                                               | 777 ms: 1.31x faster                                                 |
| sympy_sum                | 196 ms                                                 | 152 ms: 1.29x faster                                                 |
| sqlalchemy_declarative   | 172 ms                                                 | 133 ms: 1.29x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 20.1 ms: 1.28x faster                                                |
| fannkuch                 | 532 ms                                                 | 419 ms: 1.27x faster                                                 |
| nqueens                  | 106 ms                                                 | 84.1 ms: 1.26x faster                                                |
| sympy_str                | 346 ms                                                 | 276 ms: 1.25x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 80.5 ms: 1.23x faster                                                |
| json_dumps               | 14.2 ms                                                | 11.5 ms: 1.23x faster                                                |
| docutils                 | 3.30 sec                                               | 2.69 sec: 1.23x faster                                               |
| pathlib                  | 20.5 ms                                                | 16.8 ms: 1.22x faster                                                |
| xml_etree_parse          | 168 ms                                                 | 139 ms: 1.21x faster                                                 |
| sympy_expand             | 566 ms                                                 | 474 ms: 1.19x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 97.2 ms: 1.19x faster                                                |
| regex_v8                 | 27.8 ms                                                | 23.9 ms: 1.16x faster                                                |
| mdp                      | 2.85 sec                                               | 2.51 sec: 1.13x faster                                               |
| bench_thread_pool        | 986 us                                                 | 883 us: 1.12x faster                                                 |
| sqlite_synth             | 3.02 us                                                | 2.71 us: 1.12x faster                                                |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.11x faster                                                |
| meteor_contest           | 120 ms                                                 | 110 ms: 1.09x faster                                                 |
| json                     | 5.69 ms                                                | 5.28 ms: 1.08x faster                                                |
| async_generators         | 444 ms                                                 | 415 ms: 1.07x faster                                                 |
| json_loads               | 31.2 us                                                | 29.9 us: 1.04x faster                                                |
| regex_effbot             | 3.63 ms                                                | 3.48 ms: 1.04x faster                                                |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                 |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                 |
| telco                    | 7.27 ms                                                | 7.77 ms: 1.07x slower                                                |
| coverage                 | 79.4 ms                                                | 85.7 ms: 1.08x slower                                                |
| gc_traversal             | 3.62 ms                                                | 4.80 ms: 1.33x slower                                                |
| python_startup_no_site   | 5.93 ms                                                | 8.18 ms: 1.38x slower                                                |
| create_gc_cycles         | 1.62 ms                                                | 2.47 ms: 1.52x slower                                                |
| bench_mp_pool            | 24.0 ms                                                | 82.7 ms: 3.44x slower                                                |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                         |

Benchmark hidden because not significant (1): regex_dna
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250326-3.14.0a6+-9ee2a07-JIT/bm-20250326-linux-x86_64-brandtbucher-jit_up_12_11-3.14.0a6+-9ee2a07.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.438x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.29x

# Memory
- memory change: 1.30x