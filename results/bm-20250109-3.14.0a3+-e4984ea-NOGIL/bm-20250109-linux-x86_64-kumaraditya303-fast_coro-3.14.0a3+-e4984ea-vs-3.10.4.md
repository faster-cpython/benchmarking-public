# Results vs. 3.10.4

- fork: kumaraditya303
- ref: fast_coro
- machine: linux-x86_64
- commit hash: e4984ea
- commit date: 2025-01-09
- overall geometric mean: 1.133x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.50x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 342 ms: 1.02x faster                                                |
| docutils       | 3.30 sec                                               | 3.01 sec: 1.10x faster                                              |
| html5lib       | 88.9 ms                                                | 84.9 ms: 1.05x faster                                               |
| Geometric mean | (ref)                                                  | 1.05x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 732 ms: 2.42x faster                                                |
| async_tree_none         | 728 ms                                                 | 341 ms: 2.13x faster                                                |
| async_tree_memoization  | 870 ms                                                 | 435 ms: 2.00x faster                                                |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 587 ms: 1.73x faster                                                |
| Geometric mean          | (ref)                                                  | 2.06x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 135 ms: 1.14x faster                                                |
| float          | 117 ms                                                 | 103 ms: 1.13x faster                                                |
| pidigits       | 191 ms                                                 | 181 ms: 1.05x faster                                                |
| Geometric mean | (ref)                                                  | 1.11x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 161 ms: 1.17x faster                                                |
| regex_v8       | 27.8 ms                                                | 25.3 ms: 1.10x faster                                               |
| regex_dna      | 227 ms                                                 | 233 ms: 1.03x slower                                                |
| Geometric mean | (ref)                                                  | 1.06x faster                                                        |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.35 sec: 1.33x faster                                              |
| xml_etree_iterparse  | 115 ms                                                 | 96.3 ms: 1.20x faster                                               |
| xml_etree_parse      | 168 ms                                                 | 148 ms: 1.13x faster                                                |
| unpickle_pure_python | 331 us                                                 | 309 us: 1.07x faster                                                |
| xml_etree_process    | 79.1 ms                                                | 74.2 ms: 1.07x faster                                               |
| json_dumps           | 14.2 ms                                                | 13.4 ms: 1.06x faster                                               |
| json_loads           | 31.2 us                                                | 29.7 us: 1.05x faster                                               |
| pickle_pure_python   | 484 us                                                 | 468 us: 1.03x faster                                                |
| xml_etree_generate   | 99.4 ms                                                | 100.0 ms: 1.01x slower                                              |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 15.6 ms: 1.07x slower                                               |
| python_startup_no_site | 5.93 ms                                                | 9.65 ms: 1.63x slower                                               |
| Geometric mean         | (ref)                                                  | 1.32x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 30.2 ms: 1.05x faster                                               |
| genshi_xml      | 66.0 ms                                                | 63.1 ms: 1.05x faster                                               |
| django_template | 48.2 ms                                                | 46.6 ms: 1.03x faster                                               |
| mako            | 16.3 ms                                                | 18.1 ms: 1.11x slower                                               |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 208 us: 2.61x faster                                                |
| async_tree_io            | 1.77 sec                                               | 732 ms: 2.42x faster                                                |
| generators               | 80.1 ms                                                | 36.9 ms: 2.17x faster                                               |
| async_tree_none          | 728 ms                                                 | 341 ms: 2.13x faster                                                |
| async_tree_memoization   | 870 ms                                                 | 435 ms: 2.00x faster                                                |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 587 ms: 1.73x faster                                                |
| pylint                   | 551 ms                                                 | 339 ms: 1.63x faster                                                |
| deepcopy                 | 479 us                                                 | 317 us: 1.51x faster                                                |
| deepcopy_memo            | 58.5 us                                                | 40.3 us: 1.45x faster                                               |
| crypto_pyaes             | 128 ms                                                 | 91.8 ms: 1.39x faster                                               |
| coroutines               | 35.1 ms                                                | 25.4 ms: 1.38x faster                                               |
| spectral_norm            | 170 ms                                                 | 125 ms: 1.36x faster                                                |
| richards_super           | 94.7 ms                                                | 70.9 ms: 1.34x faster                                               |
| tomli_loads              | 3.14 sec                                               | 2.35 sec: 1.33x faster                                              |
| richards                 | 79.3 ms                                                | 62.3 ms: 1.27x faster                                               |
| chaos                    | 115 ms                                                 | 92.1 ms: 1.25x faster                                               |
| deepcopy_reduce          | 4.17 us                                                | 3.34 us: 1.25x faster                                               |
| scimark_sor              | 220 ms                                                 | 183 ms: 1.20x faster                                                |
| pathlib                  | 20.5 ms                                                | 17.0 ms: 1.20x faster                                               |
| xml_etree_iterparse      | 115 ms                                                 | 96.3 ms: 1.20x faster                                               |
| pycparser                | 1.58 sec                                               | 1.34 sec: 1.18x faster                                              |
| regex_compile            | 188 ms                                                 | 161 ms: 1.17x faster                                                |
| scimark_monte_carlo      | 118 ms                                                 | 102 ms: 1.16x faster                                                |
| deltablue                | 7.91 ms                                                | 6.85 ms: 1.16x faster                                               |
| hexiom                   | 10.4 ms                                                | 9.06 ms: 1.15x faster                                               |
| nbody                    | 154 ms                                                 | 135 ms: 1.14x faster                                                |
| float                    | 117 ms                                                 | 103 ms: 1.13x faster                                                |
| xml_etree_parse          | 168 ms                                                 | 148 ms: 1.13x faster                                                |
| go                       | 240 ms                                                 | 212 ms: 1.13x faster                                                |
| pyflate                  | 716 ms                                                 | 636 ms: 1.13x faster                                                |
| dulwich_log              | 84.3 ms                                                | 74.9 ms: 1.13x faster                                               |
| comprehensions           | 28.8 us                                                | 25.6 us: 1.12x faster                                               |
| scimark_lu               | 176 ms                                                 | 158 ms: 1.12x faster                                                |
| scimark_fft              | 466 ms                                                 | 418 ms: 1.11x faster                                                |
| logging_silent           | 190 ns                                                 | 171 ns: 1.11x faster                                                |
| sqlglot_normalize        | 143 ms                                                 | 130 ms: 1.10x faster                                                |
| sqlite_synth             | 3.02 us                                                | 2.75 us: 1.10x faster                                               |
| regex_v8                 | 27.8 ms                                                | 25.3 ms: 1.10x faster                                               |
| docutils                 | 3.30 sec                                               | 3.01 sec: 1.10x faster                                              |
| nqueens                  | 106 ms                                                 | 97.8 ms: 1.08x faster                                               |
| raytrace                 | 507 ms                                                 | 469 ms: 1.08x faster                                                |
| pprint_safe_repr         | 1.02 sec                                               | 949 ms: 1.07x faster                                                |
| logging_simple           | 8.30 us                                                | 7.74 us: 1.07x faster                                               |
| sympy_sum                | 196 ms                                                 | 184 ms: 1.07x faster                                                |
| pprint_pformat           | 2.10 sec                                               | 1.97 sec: 1.07x faster                                              |
| unpickle_pure_python     | 331 us                                                 | 309 us: 1.07x faster                                                |
| thrift                   | 1.07 ms                                                | 1.00 ms: 1.07x faster                                               |
| xml_etree_process        | 79.1 ms                                                | 74.2 ms: 1.07x faster                                               |
| sqlglot_optimize         | 69.2 ms                                                | 65.1 ms: 1.06x faster                                               |
| sympy_integrate          | 25.8 ms                                                | 24.3 ms: 1.06x faster                                               |
| json_dumps               | 14.2 ms                                                | 13.4 ms: 1.06x faster                                               |
| logging_format           | 9.09 us                                                | 8.57 us: 1.06x faster                                               |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 6.13 ms: 1.06x faster                                               |
| json                     | 5.69 ms                                                | 5.40 ms: 1.05x faster                                               |
| genshi_text              | 31.8 ms                                                | 30.2 ms: 1.05x faster                                               |
| pidigits                 | 191 ms                                                 | 181 ms: 1.05x faster                                                |
| json_loads               | 31.2 us                                                | 29.7 us: 1.05x faster                                               |
| genshi_xml               | 66.0 ms                                                | 63.1 ms: 1.05x faster                                               |
| html5lib                 | 88.9 ms                                                | 84.9 ms: 1.05x faster                                               |
| sympy_str                | 346 ms                                                 | 333 ms: 1.04x faster                                                |
| pickle_pure_python       | 484 us                                                 | 468 us: 1.03x faster                                                |
| django_template          | 48.2 ms                                                | 46.6 ms: 1.03x faster                                               |
| fannkuch                 | 532 ms                                                 | 514 ms: 1.03x faster                                                |
| sqlglot_transpile        | 2.57 ms                                                | 2.51 ms: 1.03x faster                                               |
| 2to3                     | 348 ms                                                 | 342 ms: 1.02x faster                                                |
| sympy_expand             | 566 ms                                                 | 555 ms: 1.02x faster                                                |
| asyncio_websockets       | 559 ms                                                 | 550 ms: 1.01x faster                                                |
| sqlglot_parse            | 2.17 ms                                                | 2.16 ms: 1.01x faster                                               |
| xml_etree_generate       | 99.4 ms                                                | 100.0 ms: 1.01x slower                                              |
| regex_dna                | 227 ms                                                 | 233 ms: 1.03x slower                                                |
| mdp                      | 2.85 sec                                               | 3.01 sec: 1.06x slower                                              |
| sqlalchemy_declarative   | 172 ms                                                 | 182 ms: 1.06x slower                                                |
| python_startup           | 14.6 ms                                                | 15.6 ms: 1.07x slower                                               |
| meteor_contest           | 120 ms                                                 | 133 ms: 1.11x slower                                                |
| mako                     | 16.3 ms                                                | 18.1 ms: 1.11x slower                                               |
| async_generators         | 444 ms                                                 | 496 ms: 1.12x slower                                                |
| gc_traversal             | 3.62 ms                                                | 4.08 ms: 1.13x slower                                               |
| coverage                 | 79.4 ms                                                | 102 ms: 1.28x slower                                                |
| telco                    | 7.27 ms                                                | 9.32 ms: 1.28x slower                                               |
| create_gc_cycles         | 1.62 ms                                                | 2.38 ms: 1.47x slower                                               |
| python_startup_no_site   | 5.93 ms                                                | 9.65 ms: 1.63x slower                                               |
| bench_thread_pool        | 986 us                                                 | 3.56 ms: 3.61x slower                                               |
| bench_mp_pool            | 24.0 ms                                                | 95.3 ms: 3.97x slower                                               |
| Geometric mean           | (ref)                                                  | 1.10x faster                                                        |

Benchmark hidden because not significant (2): regex_effbot, sqlalchemy_imperative
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250109-3.14.0a3+-e4984ea-NOGIL/bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.133x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.50x