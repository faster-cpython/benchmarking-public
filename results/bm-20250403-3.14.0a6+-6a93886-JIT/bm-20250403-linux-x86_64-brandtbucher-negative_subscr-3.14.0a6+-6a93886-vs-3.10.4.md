# Results vs. 3.10.4

- fork: brandtbucher
- ref: negative_subscr
- machine: linux-x86_64
- commit hash: 6a93886
- commit date: 2025-04-03
- overall geometric mean: 1.471x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.33x faster
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 254 ms: 1.37x faster                                                    |
| docutils       | 3.30 sec                                               | 2.67 sec: 1.23x faster                                                  |
| html5lib       | 88.9 ms                                                | 61.0 ms: 1.46x faster                                                   |
| Geometric mean | (ref)                                                  | 1.35x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 615 ms: 2.88x faster                                                    |
| async_tree_none         | 728 ms                                                 | 259 ms: 2.82x faster                                                    |
| async_tree_memoization  | 870 ms                                                 | 311 ms: 2.80x faster                                                    |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 488 ms: 2.08x faster                                                    |
| Geometric mean          | (ref)                                                  | 2.62x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 117 ms                                                 | 62.0 ms: 1.89x faster                                                   |
| nbody          | 154 ms                                                 | 89.7 ms: 1.71x faster                                                   |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                  | 1.49x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 126 ms: 1.50x faster                                                    |
| regex_v8       | 27.8 ms                                                | 24.0 ms: 1.16x faster                                                   |
| regex_effbot   | 3.63 ms                                                | 3.26 ms: 1.11x faster                                                   |
| regex_dna      | 227 ms                                                 | 210 ms: 1.08x faster                                                    |
| Geometric mean | (ref)                                                  | 1.20x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.84 sec: 1.71x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 206 us: 1.60x faster                                                    |
| pickle_pure_python   | 484 us                                                 | 317 us: 1.53x faster                                                    |
| xml_etree_process    | 79.1 ms                                                | 56.4 ms: 1.40x faster                                                   |
| xml_etree_generate   | 99.4 ms                                                | 79.4 ms: 1.25x faster                                                   |
| json_dumps           | 14.2 ms                                                | 11.5 ms: 1.23x faster                                                   |
| xml_etree_parse      | 168 ms                                                 | 139 ms: 1.21x faster                                                    |
| xml_etree_iterparse  | 115 ms                                                 | 98.0 ms: 1.18x faster                                                   |
| json_loads           | 31.2 us                                                | 29.8 us: 1.05x faster                                                   |
| Geometric mean       | (ref)                                                  | 1.33x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.2 ms: 1.10x faster                                                   |
| python_startup_no_site | 5.93 ms                                                | 8.23 ms: 1.39x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 21.1 ms: 1.51x faster                                                   |
| django_template | 48.2 ms                                                | 32.2 ms: 1.50x faster                                                   |
| mako            | 16.3 ms                                                | 11.0 ms: 1.49x faster                                                   |
| genshi_xml      | 66.0 ms                                                | 48.8 ms: 1.35x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.46x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.26x faster                                                    |
| async_tree_io            | 1.77 sec                                               | 615 ms: 2.88x faster                                                    |
| async_tree_none          | 728 ms                                                 | 259 ms: 2.82x faster                                                    |
| async_tree_memoization   | 870 ms                                                 | 311 ms: 2.80x faster                                                    |
| generators               | 80.1 ms                                                | 29.6 ms: 2.70x faster                                                   |
| deltablue                | 7.91 ms                                                | 3.03 ms: 2.61x faster                                                   |
| richards_super           | 94.7 ms                                                | 39.8 ms: 2.38x faster                                                   |
| mdp                      | 2.85 sec                                               | 1.22 sec: 2.34x faster                                                  |
| richards                 | 79.3 ms                                                | 34.7 ms: 2.29x faster                                                   |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 488 ms: 2.08x faster                                                    |
| deepcopy_memo            | 58.5 us                                                | 29.0 us: 2.02x faster                                                   |
| chaos                    | 115 ms                                                 | 57.7 ms: 2.00x faster                                                   |
| logging_silent           | 190 ns                                                 | 94.9 ns: 2.00x faster                                                   |
| pylint                   | 551 ms                                                 | 281 ms: 1.97x faster                                                    |
| go                       | 240 ms                                                 | 124 ms: 1.94x faster                                                    |
| raytrace                 | 507 ms                                                 | 264 ms: 1.92x faster                                                    |
| deepcopy                 | 479 us                                                 | 252 us: 1.90x faster                                                    |
| float                    | 117 ms                                                 | 62.0 ms: 1.89x faster                                                   |
| scimark_sor              | 220 ms                                                 | 117 ms: 1.88x faster                                                    |
| scimark_monte_carlo      | 118 ms                                                 | 65.8 ms: 1.80x faster                                                   |
| spectral_norm            | 170 ms                                                 | 96.9 ms: 1.75x faster                                                   |
| pyflate                  | 716 ms                                                 | 416 ms: 1.72x faster                                                    |
| nbody                    | 154 ms                                                 | 89.7 ms: 1.71x faster                                                   |
| tomli_loads              | 3.14 sec                                               | 1.84 sec: 1.71x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 75.0 ms: 1.70x faster                                                   |
| unpickle_pure_python     | 331 us                                                 | 206 us: 1.60x faster                                                    |
| deepcopy_reduce          | 4.17 us                                                | 2.62 us: 1.59x faster                                                   |
| comprehensions           | 28.8 us                                                | 18.2 us: 1.58x faster                                                   |
| hexiom                   | 10.4 ms                                                | 6.76 ms: 1.54x faster                                                   |
| pickle_pure_python       | 484 us                                                 | 317 us: 1.53x faster                                                    |
| scimark_fft              | 466 ms                                                 | 307 ms: 1.52x faster                                                    |
| genshi_text              | 31.8 ms                                                | 21.1 ms: 1.51x faster                                                   |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.50x faster                                                    |
| django_template          | 48.2 ms                                                | 32.2 ms: 1.50x faster                                                   |
| regex_compile            | 188 ms                                                 | 126 ms: 1.50x faster                                                    |
| logging_simple           | 8.30 us                                                | 5.56 us: 1.49x faster                                                   |
| mako                     | 16.3 ms                                                | 11.0 ms: 1.49x faster                                                   |
| coroutines               | 35.1 ms                                                | 23.7 ms: 1.48x faster                                                   |
| logging_format           | 9.09 us                                                | 6.22 us: 1.46x faster                                                   |
| html5lib                 | 88.9 ms                                                | 61.0 ms: 1.46x faster                                                   |
| xml_etree_process        | 79.1 ms                                                | 56.4 ms: 1.40x faster                                                   |
| dulwich_log              | 84.3 ms                                                | 60.5 ms: 1.39x faster                                                   |
| pycparser                | 1.58 sec                                               | 1.14 sec: 1.38x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.70 ms: 1.38x faster                                                   |
| 2to3                     | 348 ms                                                 | 254 ms: 1.37x faster                                                    |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.2 ms: 1.36x faster                                                   |
| genshi_xml               | 66.0 ms                                                | 48.8 ms: 1.35x faster                                                   |
| pprint_pformat           | 2.10 sec                                               | 1.56 sec: 1.35x faster                                                  |
| pprint_safe_repr         | 1.02 sec                                               | 761 ms: 1.34x faster                                                    |
| fannkuch                 | 532 ms                                                 | 403 ms: 1.32x faster                                                    |
| sympy_integrate          | 25.8 ms                                                | 19.6 ms: 1.32x faster                                                   |
| sympy_sum                | 196 ms                                                 | 151 ms: 1.30x faster                                                    |
| nqueens                  | 106 ms                                                 | 81.6 ms: 1.30x faster                                                   |
| sqlalchemy_declarative   | 172 ms                                                 | 133 ms: 1.29x faster                                                    |
| sympy_str                | 346 ms                                                 | 272 ms: 1.27x faster                                                    |
| xml_etree_generate       | 99.4 ms                                                | 79.4 ms: 1.25x faster                                                   |
| docutils                 | 3.30 sec                                               | 2.67 sec: 1.23x faster                                                  |
| json_dumps               | 14.2 ms                                                | 11.5 ms: 1.23x faster                                                   |
| pathlib                  | 20.5 ms                                                | 16.8 ms: 1.22x faster                                                   |
| xml_etree_parse          | 168 ms                                                 | 139 ms: 1.21x faster                                                    |
| sympy_expand             | 566 ms                                                 | 472 ms: 1.20x faster                                                    |
| xml_etree_iterparse      | 115 ms                                                 | 98.0 ms: 1.18x faster                                                   |
| regex_v8                 | 27.8 ms                                                | 24.0 ms: 1.16x faster                                                   |
| regex_effbot             | 3.63 ms                                                | 3.26 ms: 1.11x faster                                                   |
| bench_thread_pool        | 986 us                                                 | 887 us: 1.11x faster                                                    |
| python_startup           | 14.6 ms                                                | 13.2 ms: 1.10x faster                                                   |
| sqlite_synth             | 3.02 us                                                | 2.74 us: 1.10x faster                                                   |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                                    |
| async_generators         | 444 ms                                                 | 410 ms: 1.08x faster                                                    |
| regex_dna                | 227 ms                                                 | 210 ms: 1.08x faster                                                    |
| json                     | 5.69 ms                                                | 5.30 ms: 1.07x faster                                                   |
| json_loads               | 31.2 us                                                | 29.8 us: 1.05x faster                                                   |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                    |
| asyncio_websockets       | 559 ms                                                 | 554 ms: 1.01x faster                                                    |
| coverage                 | 79.4 ms                                                | 85.1 ms: 1.07x slower                                                   |
| telco                    | 7.27 ms                                                | 7.82 ms: 1.08x slower                                                   |
| gc_traversal             | 3.62 ms                                                | 4.89 ms: 1.35x slower                                                   |
| python_startup_no_site   | 5.93 ms                                                | 8.23 ms: 1.39x slower                                                   |
| create_gc_cycles         | 1.62 ms                                                | 2.50 ms: 1.54x slower                                                   |
| bench_mp_pool            | 24.0 ms                                                | 83.4 ms: 3.47x slower                                                   |
| Geometric mean           | (ref)                                                  | 1.44x faster                                                            |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250403-3.14.0a6+-6a93886-JIT/bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.471x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.36x
- 95% likely to have a speedup of 1.35x
- 99% likely to have a speedup of 1.33x

# Memory
- memory change: 1.30x