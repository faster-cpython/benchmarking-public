# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_cached_consts
- machine: linux-x86_64
- commit hash: 4953e8a
- commit date: 2025-03-28
- overall geometric mean: 1.453x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250328-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-4953e8a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 261 ms: 1.33x faster                                                      |
| docutils       | 3.30 sec                                               | 2.66 sec: 1.24x faster                                                    |
| html5lib       | 88.9 ms                                                | 61.7 ms: 1.44x faster                                                     |
| Geometric mean | (ref)                                                  | 1.34x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250328-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-4953e8a |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 612 ms: 2.89x faster                                                      |
| async_tree_none         | 728 ms                                                 | 256 ms: 2.84x faster                                                      |
| async_tree_memoization  | 870 ms                                                 | 316 ms: 2.76x faster                                                      |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 488 ms: 2.08x faster                                                      |
| Geometric mean          | (ref)                                                  | 2.62x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250328-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-4953e8a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 64.6 ms: 1.81x faster                                                     |
| nbody          | 154 ms                                                 | 88.7 ms: 1.73x faster                                                     |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                  | 1.48x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250328-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-4953e8a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.48x faster                                                      |
| regex_v8       | 27.8 ms                                                | 23.1 ms: 1.20x faster                                                     |
| regex_effbot   | 3.63 ms                                                | 3.16 ms: 1.15x faster                                                     |
| regex_dna      | 227 ms                                                 | 217 ms: 1.05x faster                                                      |
| Geometric mean | (ref)                                                  | 1.21x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250328-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-4953e8a |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.85 sec: 1.69x faster                                                    |
| unpickle_pure_python | 331 us                                                 | 212 us: 1.56x faster                                                      |
| pickle_pure_python   | 484 us                                                 | 322 us: 1.50x faster                                                      |
| xml_etree_process    | 79.1 ms                                                | 55.4 ms: 1.43x faster                                                     |
| xml_etree_generate   | 99.4 ms                                                | 79.2 ms: 1.26x faster                                                     |
| json_dumps           | 14.2 ms                                                | 11.6 ms: 1.22x faster                                                     |
| xml_etree_parse      | 168 ms                                                 | 140 ms: 1.20x faster                                                      |
| xml_etree_iterparse  | 115 ms                                                 | 97.4 ms: 1.19x faster                                                     |
| json_loads           | 31.2 us                                                | 29.7 us: 1.05x faster                                                     |
| Geometric mean       | (ref)                                                  | 1.33x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250328-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-4953e8a |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.11x faster                                                     |
| python_startup_no_site | 5.93 ms                                                | 8.19 ms: 1.38x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250328-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-4953e8a |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 20.8 ms: 1.53x faster                                                     |
| django_template | 48.2 ms                                                | 31.6 ms: 1.52x faster                                                     |
| mako            | 16.3 ms                                                | 10.9 ms: 1.49x faster                                                     |
| genshi_xml      | 66.0 ms                                                | 49.7 ms: 1.33x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.47x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250328-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-4953e8a |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 172 us: 3.16x faster                                                      |
| async_tree_io            | 1.77 sec                                               | 612 ms: 2.89x faster                                                      |
| generators               | 80.1 ms                                                | 28.1 ms: 2.85x faster                                                     |
| async_tree_none          | 728 ms                                                 | 256 ms: 2.84x faster                                                      |
| async_tree_memoization   | 870 ms                                                 | 316 ms: 2.76x faster                                                      |
| deltablue                | 7.91 ms                                                | 2.99 ms: 2.65x faster                                                     |
| richards_super           | 94.7 ms                                                | 39.7 ms: 2.38x faster                                                     |
| richards                 | 79.3 ms                                                | 34.9 ms: 2.27x faster                                                     |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 488 ms: 2.08x faster                                                      |
| deepcopy_memo            | 58.5 us                                                | 29.5 us: 1.98x faster                                                     |
| pylint                   | 551 ms                                                 | 280 ms: 1.97x faster                                                      |
| chaos                    | 115 ms                                                 | 59.0 ms: 1.96x faster                                                     |
| logging_silent           | 190 ns                                                 | 97.4 ns: 1.95x faster                                                     |
| raytrace                 | 507 ms                                                 | 266 ms: 1.90x faster                                                      |
| go                       | 240 ms                                                 | 126 ms: 1.90x faster                                                      |
| deepcopy                 | 479 us                                                 | 254 us: 1.88x faster                                                      |
| scimark_sor              | 220 ms                                                 | 117 ms: 1.87x faster                                                      |
| float                    | 117 ms                                                 | 64.6 ms: 1.81x faster                                                     |
| spectral_norm            | 170 ms                                                 | 93.9 ms: 1.81x faster                                                     |
| scimark_monte_carlo      | 118 ms                                                 | 66.8 ms: 1.77x faster                                                     |
| nbody                    | 154 ms                                                 | 88.7 ms: 1.73x faster                                                     |
| tomli_loads              | 3.14 sec                                               | 1.85 sec: 1.69x faster                                                    |
| pyflate                  | 716 ms                                                 | 433 ms: 1.65x faster                                                      |
| crypto_pyaes             | 128 ms                                                 | 78.7 ms: 1.62x faster                                                     |
| hexiom                   | 10.4 ms                                                | 6.64 ms: 1.57x faster                                                     |
| unpickle_pure_python     | 331 us                                                 | 212 us: 1.56x faster                                                      |
| deepcopy_reduce          | 4.17 us                                                | 2.69 us: 1.55x faster                                                     |
| genshi_text              | 31.8 ms                                                | 20.8 ms: 1.53x faster                                                     |
| django_template          | 48.2 ms                                                | 31.6 ms: 1.52x faster                                                     |
| comprehensions           | 28.8 us                                                | 19.0 us: 1.51x faster                                                     |
| coroutines               | 35.1 ms                                                | 23.3 ms: 1.51x faster                                                     |
| scimark_fft              | 466 ms                                                 | 309 ms: 1.51x faster                                                      |
| pickle_pure_python       | 484 us                                                 | 322 us: 1.50x faster                                                      |
| mako                     | 16.3 ms                                                | 10.9 ms: 1.49x faster                                                     |
| regex_compile            | 188 ms                                                 | 127 ms: 1.48x faster                                                      |
| scimark_lu               | 176 ms                                                 | 119 ms: 1.48x faster                                                      |
| logging_simple           | 8.30 us                                                | 5.62 us: 1.48x faster                                                     |
| logging_format           | 9.09 us                                                | 6.20 us: 1.47x faster                                                     |
| html5lib                 | 88.9 ms                                                | 61.7 ms: 1.44x faster                                                     |
| xml_etree_process        | 79.1 ms                                                | 55.4 ms: 1.43x faster                                                     |
| pycparser                | 1.58 sec                                               | 1.12 sec: 1.41x faster                                                    |
| thrift                   | 1.07 ms                                                | 764 us: 1.40x faster                                                      |
| dulwich_log              | 84.3 ms                                                | 60.4 ms: 1.40x faster                                                     |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.9 ms: 1.38x faster                                                     |
| pprint_pformat           | 2.10 sec                                               | 1.54 sec: 1.36x faster                                                    |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.76 ms: 1.36x faster                                                     |
| pprint_safe_repr         | 1.02 sec                                               | 758 ms: 1.34x faster                                                      |
| 2to3                     | 348 ms                                                 | 261 ms: 1.33x faster                                                      |
| genshi_xml               | 66.0 ms                                                | 49.7 ms: 1.33x faster                                                     |
| sqlalchemy_declarative   | 172 ms                                                 | 133 ms: 1.30x faster                                                      |
| sympy_sum                | 196 ms                                                 | 152 ms: 1.30x faster                                                      |
| sympy_integrate          | 25.8 ms                                                | 20.1 ms: 1.28x faster                                                     |
| sympy_str                | 346 ms                                                 | 273 ms: 1.26x faster                                                      |
| fannkuch                 | 532 ms                                                 | 423 ms: 1.26x faster                                                      |
| xml_etree_generate       | 99.4 ms                                                | 79.2 ms: 1.26x faster                                                     |
| nqueens                  | 106 ms                                                 | 84.4 ms: 1.25x faster                                                     |
| docutils                 | 3.30 sec                                               | 2.66 sec: 1.24x faster                                                    |
| pathlib                  | 20.5 ms                                                | 16.6 ms: 1.23x faster                                                     |
| json_dumps               | 14.2 ms                                                | 11.6 ms: 1.22x faster                                                     |
| regex_v8                 | 27.8 ms                                                | 23.1 ms: 1.20x faster                                                     |
| sympy_expand             | 566 ms                                                 | 470 ms: 1.20x faster                                                      |
| xml_etree_parse          | 168 ms                                                 | 140 ms: 1.20x faster                                                      |
| xml_etree_iterparse      | 115 ms                                                 | 97.4 ms: 1.19x faster                                                     |
| mdp                      | 2.85 sec                                               | 2.48 sec: 1.15x faster                                                    |
| regex_effbot             | 3.63 ms                                                | 3.16 ms: 1.15x faster                                                     |
| sqlite_synth             | 3.02 us                                                | 2.69 us: 1.12x faster                                                     |
| bench_thread_pool        | 986 us                                                 | 879 us: 1.12x faster                                                      |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.11x faster                                                     |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                      |
| json                     | 5.69 ms                                                | 5.26 ms: 1.08x faster                                                     |
| async_generators         | 444 ms                                                 | 419 ms: 1.06x faster                                                      |
| json_loads               | 31.2 us                                                | 29.7 us: 1.05x faster                                                     |
| regex_dna                | 227 ms                                                 | 217 ms: 1.05x faster                                                      |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                      |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                      |
| coverage                 | 79.4 ms                                                | 84.8 ms: 1.07x slower                                                     |
| telco                    | 7.27 ms                                                | 7.85 ms: 1.08x slower                                                     |
| gc_traversal             | 3.62 ms                                                | 4.99 ms: 1.38x slower                                                     |
| python_startup_no_site   | 5.93 ms                                                | 8.19 ms: 1.38x slower                                                     |
| create_gc_cycles         | 1.62 ms                                                | 2.50 ms: 1.54x slower                                                     |
| bench_mp_pool            | 24.0 ms                                                | 82.5 ms: 3.44x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                              |
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250328-3.14.0a6+-4953e8a-JIT/bm-20250328-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-4953e8a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.453x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.35x
- 95% likely to have a speedup of 1.34x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.29x