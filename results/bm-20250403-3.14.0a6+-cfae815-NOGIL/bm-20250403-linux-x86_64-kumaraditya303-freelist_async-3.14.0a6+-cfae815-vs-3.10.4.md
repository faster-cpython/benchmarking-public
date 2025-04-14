# Results vs. 3.10.4

- fork: kumaraditya303
- ref: freelist_async
- machine: linux-x86_64
- commit hash: cfae815
- commit date: 2025-04-03
- overall geometric mean: 1.339x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: 1.53x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 287 ms: 1.22x faster                                                     |
| docutils       | 3.30 sec                                               | 2.77 sec: 1.19x faster                                                   |
| html5lib       | 88.9 ms                                                | 66.5 ms: 1.34x faster                                                    |
| Geometric mean | (ref)                                                  | 1.25x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 542 ms: 3.26x faster                                                     |
| async_tree_none         | 728 ms                                                 | 262 ms: 2.78x faster                                                     |
| async_tree_memoization  | 870 ms                                                 | 328 ms: 2.65x faster                                                     |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 487 ms: 2.09x faster                                                     |
| Geometric mean          | (ref)                                                  | 2.66x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 68.5 ms: 1.71x faster                                                    |
| nbody          | 154 ms                                                 | 119 ms: 1.29x faster                                                     |
| pidigits       | 191 ms                                                 | 189 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                  | 1.31x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 143 ms: 1.32x faster                                                     |
| regex_v8       | 27.8 ms                                                | 22.0 ms: 1.26x faster                                                    |
| regex_effbot   | 3.63 ms                                                | 3.32 ms: 1.09x faster                                                    |
| regex_dna      | 227 ms                                                 | 211 ms: 1.07x faster                                                     |
| Geometric mean | (ref)                                                  | 1.18x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.15 sec: 1.46x faster                                                   |
| pickle_pure_python   | 484 us                                                 | 336 us: 1.44x faster                                                     |
| unpickle_pure_python | 331 us                                                 | 236 us: 1.40x faster                                                     |
| xml_etree_iterparse  | 115 ms                                                 | 93.9 ms: 1.23x faster                                                    |
| xml_etree_process    | 79.1 ms                                                | 65.5 ms: 1.21x faster                                                    |
| xml_etree_parse      | 168 ms                                                 | 148 ms: 1.13x faster                                                     |
| json_dumps           | 14.2 ms                                                | 12.8 ms: 1.11x faster                                                    |
| xml_etree_generate   | 99.4 ms                                                | 93.4 ms: 1.06x faster                                                    |
| json_loads           | 31.2 us                                                | 32.1 us: 1.03x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.21x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 15.6 ms: 1.07x slower                                                    |
| python_startup_no_site | 5.93 ms                                                | 10.9 ms: 1.84x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.40x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 38.2 ms: 1.26x faster                                                    |
| genshi_text     | 31.8 ms                                                | 27.1 ms: 1.18x faster                                                    |
| genshi_xml      | 66.0 ms                                                | 58.0 ms: 1.14x faster                                                    |
| mako            | 16.3 ms                                                | 15.7 ms: 1.04x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.15x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io            | 1.77 sec                                               | 542 ms: 3.26x faster                                                     |
| typing_runtime_protocols | 544 us                                                 | 195 us: 2.80x faster                                                     |
| async_tree_none          | 728 ms                                                 | 262 ms: 2.78x faster                                                     |
| generators               | 80.1 ms                                                | 29.6 ms: 2.71x faster                                                    |
| async_tree_memoization   | 870 ms                                                 | 328 ms: 2.65x faster                                                     |
| deltablue                | 7.91 ms                                                | 3.60 ms: 2.20x faster                                                    |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 487 ms: 2.09x faster                                                     |
| mdp                      | 2.85 sec                                               | 1.37 sec: 2.08x faster                                                   |
| go                       | 240 ms                                                 | 129 ms: 1.87x faster                                                     |
| logging_silent           | 190 ns                                                 | 103 ns: 1.84x faster                                                     |
| pylint                   | 551 ms                                                 | 307 ms: 1.80x faster                                                     |
| gc_traversal             | 3.62 ms                                                | 2.03 ms: 1.78x faster                                                    |
| chaos                    | 115 ms                                                 | 65.0 ms: 1.78x faster                                                    |
| scimark_sor              | 220 ms                                                 | 127 ms: 1.73x faster                                                     |
| float                    | 117 ms                                                 | 68.5 ms: 1.71x faster                                                    |
| deepcopy_memo            | 58.5 us                                                | 35.2 us: 1.66x faster                                                    |
| raytrace                 | 507 ms                                                 | 308 ms: 1.64x faster                                                     |
| deepcopy                 | 479 us                                                 | 292 us: 1.64x faster                                                     |
| richards_super           | 94.7 ms                                                | 59.0 ms: 1.61x faster                                                    |
| spectral_norm            | 170 ms                                                 | 109 ms: 1.56x faster                                                     |
| richards                 | 79.3 ms                                                | 51.5 ms: 1.54x faster                                                    |
| pyflate                  | 716 ms                                                 | 469 ms: 1.53x faster                                                     |
| scimark_monte_carlo      | 118 ms                                                 | 78.7 ms: 1.50x faster                                                    |
| comprehensions           | 28.8 us                                                | 19.2 us: 1.50x faster                                                    |
| crypto_pyaes             | 128 ms                                                 | 86.1 ms: 1.48x faster                                                    |
| tomli_loads              | 3.14 sec                                               | 2.15 sec: 1.46x faster                                                   |
| coroutines               | 35.1 ms                                                | 24.2 ms: 1.45x faster                                                    |
| hexiom                   | 10.4 ms                                                | 7.17 ms: 1.45x faster                                                    |
| pickle_pure_python       | 484 us                                                 | 336 us: 1.44x faster                                                     |
| unpickle_pure_python     | 331 us                                                 | 236 us: 1.40x faster                                                     |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                                   |
| deepcopy_reduce          | 4.17 us                                                | 3.10 us: 1.35x faster                                                    |
| dulwich_log              | 84.3 ms                                                | 62.7 ms: 1.35x faster                                                    |
| html5lib                 | 88.9 ms                                                | 66.5 ms: 1.34x faster                                                    |
| scimark_lu               | 176 ms                                                 | 132 ms: 1.33x faster                                                     |
| regex_compile            | 188 ms                                                 | 143 ms: 1.32x faster                                                     |
| logging_simple           | 8.30 us                                                | 6.41 us: 1.29x faster                                                    |
| nbody                    | 154 ms                                                 | 119 ms: 1.29x faster                                                     |
| pprint_safe_repr         | 1.02 sec                                               | 801 ms: 1.27x faster                                                     |
| pprint_pformat           | 2.10 sec                                               | 1.66 sec: 1.27x faster                                                   |
| regex_v8                 | 27.8 ms                                                | 22.0 ms: 1.26x faster                                                    |
| django_template          | 48.2 ms                                                | 38.2 ms: 1.26x faster                                                    |
| scimark_fft              | 466 ms                                                 | 371 ms: 1.25x faster                                                     |
| logging_format           | 9.09 us                                                | 7.26 us: 1.25x faster                                                    |
| xml_etree_iterparse      | 115 ms                                                 | 93.9 ms: 1.23x faster                                                    |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.28 ms: 1.23x faster                                                    |
| pathlib                  | 20.5 ms                                                | 16.7 ms: 1.23x faster                                                    |
| 2to3                     | 348 ms                                                 | 287 ms: 1.22x faster                                                     |
| xml_etree_process        | 79.1 ms                                                | 65.5 ms: 1.21x faster                                                    |
| docutils                 | 3.30 sec                                               | 2.77 sec: 1.19x faster                                                   |
| nqueens                  | 106 ms                                                 | 89.3 ms: 1.18x faster                                                    |
| genshi_text              | 31.8 ms                                                | 27.1 ms: 1.18x faster                                                    |
| sympy_integrate          | 25.8 ms                                                | 22.4 ms: 1.15x faster                                                    |
| sqlalchemy_imperative    | 23.3 ms                                                | 20.5 ms: 1.14x faster                                                    |
| genshi_xml               | 66.0 ms                                                | 58.0 ms: 1.14x faster                                                    |
| xml_etree_parse          | 168 ms                                                 | 148 ms: 1.13x faster                                                     |
| sympy_sum                | 196 ms                                                 | 173 ms: 1.13x faster                                                     |
| sympy_str                | 346 ms                                                 | 309 ms: 1.12x faster                                                     |
| json_dumps               | 14.2 ms                                                | 12.8 ms: 1.11x faster                                                    |
| fannkuch                 | 532 ms                                                 | 482 ms: 1.10x faster                                                     |
| regex_effbot             | 3.63 ms                                                | 3.32 ms: 1.09x faster                                                    |
| sqlalchemy_declarative   | 172 ms                                                 | 158 ms: 1.09x faster                                                     |
| sqlite_synth             | 3.02 us                                                | 2.78 us: 1.09x faster                                                    |
| sympy_expand             | 566 ms                                                 | 520 ms: 1.09x faster                                                     |
| regex_dna                | 227 ms                                                 | 211 ms: 1.07x faster                                                     |
| xml_etree_generate       | 99.4 ms                                                | 93.4 ms: 1.06x faster                                                    |
| async_generators         | 444 ms                                                 | 419 ms: 1.06x faster                                                     |
| mako                     | 16.3 ms                                                | 15.7 ms: 1.04x faster                                                    |
| json                     | 5.69 ms                                                | 5.56 ms: 1.02x faster                                                    |
| asyncio_websockets       | 559 ms                                                 | 550 ms: 1.02x faster                                                     |
| pidigits                 | 191 ms                                                 | 189 ms: 1.01x faster                                                     |
| json_loads               | 31.2 us                                                | 32.1 us: 1.03x slower                                                    |
| create_gc_cycles         | 1.62 ms                                                | 1.69 ms: 1.04x slower                                                    |
| python_startup           | 14.6 ms                                                | 15.6 ms: 1.07x slower                                                    |
| meteor_contest           | 120 ms                                                 | 133 ms: 1.11x slower                                                     |
| telco                    | 7.27 ms                                                | 9.18 ms: 1.26x slower                                                    |
| coverage                 | 79.4 ms                                                | 119 ms: 1.49x slower                                                     |
| python_startup_no_site   | 5.93 ms                                                | 10.9 ms: 1.84x slower                                                    |
| bench_thread_pool        | 986 us                                                 | 3.25 ms: 3.30x slower                                                    |
| bench_mp_pool            | 24.0 ms                                                | 90.1 ms: 3.75x slower                                                    |
| Geometric mean           | (ref)                                                  | 1.29x faster                                                             |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250403-3.14.0a6+-cfae815-NOGIL/bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.339x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: 1.53x