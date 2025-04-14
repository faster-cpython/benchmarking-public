# Results vs. 3.10.4

- fork: python
- ref: 52b5eb95b770fa00ebbd
- machine: linux-x86_64
- commit hash: 52b5eb9
- commit date: 2025-03-26
- overall geometric mean: 1.436x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-linux-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 258 ms: 1.35x faster                                                   |
| docutils       | 3.30 sec                                               | 2.63 sec: 1.25x faster                                                 |
| html5lib       | 88.9 ms                                                | 61.9 ms: 1.44x faster                                                  |
| Geometric mean | (ref)                                                  | 1.34x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-linux-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 612 ms: 2.89x faster                                                   |
| async_tree_none         | 728 ms                                                 | 257 ms: 2.84x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 311 ms: 2.80x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 487 ms: 2.09x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.63x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-linux-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 117 ms                                                 | 70.5 ms: 1.66x faster                                                  |
| nbody          | 154 ms                                                 | 97.3 ms: 1.58x faster                                                  |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                  | 1.39x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-linux-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.49x faster                                                   |
| regex_v8       | 27.8 ms                                                | 23.0 ms: 1.21x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.47 ms: 1.05x faster                                                  |
| regex_dna      | 227 ms                                                 | 224 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.17x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-linux-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.97 sec: 1.60x faster                                                 |
| pickle_pure_python   | 484 us                                                 | 319 us: 1.52x faster                                                   |
| unpickle_pure_python | 331 us                                                 | 218 us: 1.51x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 59.3 ms: 1.33x faster                                                  |
| json_dumps           | 14.2 ms                                                | 11.7 ms: 1.21x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 142 ms: 1.19x faster                                                   |
| xml_etree_generate   | 99.4 ms                                                | 85.2 ms: 1.17x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 99.0 ms: 1.17x faster                                                  |
| json_loads           | 31.2 us                                                | 30.0 us: 1.04x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.29x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-linux-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.11x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 8.19 ms: 1.38x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-linux-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.0 ms: 1.51x faster                                                  |
| genshi_text     | 31.8 ms                                                | 21.4 ms: 1.49x faster                                                  |
| mako            | 16.3 ms                                                | 11.3 ms: 1.45x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 50.0 ms: 1.32x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-linux-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 161 us: 3.37x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 612 ms: 2.89x faster                                                   |
| async_tree_none          | 728 ms                                                 | 257 ms: 2.84x faster                                                   |
| generators               | 80.1 ms                                                | 28.6 ms: 2.80x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 311 ms: 2.80x faster                                                   |
| deltablue                | 7.91 ms                                                | 3.16 ms: 2.51x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 487 ms: 2.09x faster                                                   |
| go                       | 240 ms                                                 | 117 ms: 2.05x faster                                                   |
| pylint                   | 551 ms                                                 | 276 ms: 1.99x faster                                                   |
| deepcopy_memo            | 58.5 us                                                | 29.3 us: 1.99x faster                                                  |
| chaos                    | 115 ms                                                 | 58.8 ms: 1.96x faster                                                  |
| raytrace                 | 507 ms                                                 | 265 ms: 1.91x faster                                                   |
| logging_silent           | 190 ns                                                 | 99.9 ns: 1.90x faster                                                  |
| richards_super           | 94.7 ms                                                | 51.0 ms: 1.86x faster                                                  |
| deepcopy                 | 479 us                                                 | 259 us: 1.85x faster                                                   |
| scimark_sor              | 220 ms                                                 | 120 ms: 1.83x faster                                                   |
| richards                 | 79.3 ms                                                | 44.5 ms: 1.78x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 68.0 ms: 1.74x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 74.5 ms: 1.72x faster                                                  |
| spectral_norm            | 170 ms                                                 | 99.0 ms: 1.72x faster                                                  |
| comprehensions           | 28.8 us                                                | 16.9 us: 1.70x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.25 ms: 1.66x faster                                                  |
| float                    | 117 ms                                                 | 70.5 ms: 1.66x faster                                                  |
| pyflate                  | 716 ms                                                 | 442 ms: 1.62x faster                                                   |
| tomli_loads              | 3.14 sec                                               | 1.97 sec: 1.60x faster                                                 |
| nbody                    | 154 ms                                                 | 97.3 ms: 1.58x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.69 us: 1.55x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 319 us: 1.52x faster                                                   |
| unpickle_pure_python     | 331 us                                                 | 218 us: 1.51x faster                                                   |
| django_template          | 48.2 ms                                                | 32.0 ms: 1.51x faster                                                  |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.51x faster                                                   |
| coroutines               | 35.1 ms                                                | 23.5 ms: 1.49x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.56 us: 1.49x faster                                                  |
| regex_compile            | 188 ms                                                 | 127 ms: 1.49x faster                                                   |
| genshi_text              | 31.8 ms                                                | 21.4 ms: 1.49x faster                                                  |
| logging_format           | 9.09 us                                                | 6.16 us: 1.48x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 58.1 ms: 1.45x faster                                                  |
| mako                     | 16.3 ms                                                | 11.3 ms: 1.45x faster                                                  |
| html5lib                 | 88.9 ms                                                | 61.9 ms: 1.44x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.49 sec: 1.41x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 727 ms: 1.40x faster                                                   |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.7 ms: 1.39x faster                                                  |
| thrift                   | 1.07 ms                                                | 772 us: 1.39x faster                                                   |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.72 ms: 1.37x faster                                                  |
| 2to3                     | 348 ms                                                 | 258 ms: 1.35x faster                                                   |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.34x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 59.3 ms: 1.33x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 19.5 ms: 1.32x faster                                                  |
| sympy_sum                | 196 ms                                                 | 149 ms: 1.32x faster                                                   |
| genshi_xml               | 66.0 ms                                                | 50.0 ms: 1.32x faster                                                  |
| sqlalchemy_declarative   | 172 ms                                                 | 131 ms: 1.32x faster                                                   |
| scimark_fft              | 466 ms                                                 | 355 ms: 1.31x faster                                                   |
| sympy_str                | 346 ms                                                 | 268 ms: 1.29x faster                                                   |
| nqueens                  | 106 ms                                                 | 82.7 ms: 1.28x faster                                                  |
| fannkuch                 | 532 ms                                                 | 418 ms: 1.27x faster                                                   |
| docutils                 | 3.30 sec                                               | 2.63 sec: 1.25x faster                                                 |
| sympy_expand             | 566 ms                                                 | 458 ms: 1.24x faster                                                   |
| pathlib                  | 20.5 ms                                                | 16.7 ms: 1.22x faster                                                  |
| json_dumps               | 14.2 ms                                                | 11.7 ms: 1.21x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 23.0 ms: 1.21x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 142 ms: 1.19x faster                                                   |
| xml_etree_generate       | 99.4 ms                                                | 85.2 ms: 1.17x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 99.0 ms: 1.17x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.48 sec: 1.15x faster                                                 |
| async_generators         | 444 ms                                                 | 389 ms: 1.14x faster                                                   |
| bench_thread_pool        | 986 us                                                 | 870 us: 1.13x faster                                                   |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                   |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.11x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 2.75 us: 1.10x faster                                                  |
| json                     | 5.69 ms                                                | 5.32 ms: 1.07x faster                                                  |
| regex_effbot             | 3.63 ms                                                | 3.47 ms: 1.05x faster                                                  |
| json_loads               | 31.2 us                                                | 30.0 us: 1.04x faster                                                  |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                   |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                   |
| regex_dna                | 227 ms                                                 | 224 ms: 1.01x faster                                                   |
| telco                    | 7.27 ms                                                | 7.93 ms: 1.09x slower                                                  |
| coverage                 | 79.4 ms                                                | 91.9 ms: 1.16x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 4.84 ms: 1.34x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 8.19 ms: 1.38x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 2.50 ms: 1.54x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 82.9 ms: 3.45x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                           |
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250326-3.14.0a6+-52b5eb9/bm-20250326-linux-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.436x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.28x