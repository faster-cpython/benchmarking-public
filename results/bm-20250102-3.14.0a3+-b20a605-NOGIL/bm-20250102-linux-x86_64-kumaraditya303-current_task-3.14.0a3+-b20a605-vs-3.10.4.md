# Results vs. 3.10.4

- fork: kumaraditya303
- ref: current_task
- machine: linux-x86_64
- commit hash: b20a605
- commit date: 2025-01-02
- overall geometric mean: 1.127x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.50x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 346 ms: 1.01x faster                                                   |
| docutils       | 3.30 sec                                               | 2.96 sec: 1.11x faster                                                 |
| html5lib       | 88.9 ms                                                | 87.3 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 724 ms: 2.44x faster                                                   |
| async_tree_none         | 728 ms                                                 | 335 ms: 2.17x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 431 ms: 2.02x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 578 ms: 1.76x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.08x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 135 ms: 1.14x faster                                                   |
| float          | 117 ms                                                 | 107 ms: 1.09x faster                                                   |
| pidigits       | 191 ms                                                 | 181 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 164 ms: 1.15x faster                                                   |
| regex_effbot   | 3.63 ms                                                | 3.33 ms: 1.09x faster                                                  |
| regex_v8       | 27.8 ms                                                | 26.2 ms: 1.06x faster                                                  |
| regex_dna      | 227 ms                                                 | 226 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.48 sec: 1.26x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 96.2 ms: 1.20x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 149 ms: 1.13x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 72.4 ms: 1.09x faster                                                  |
| json_dumps           | 14.2 ms                                                | 13.2 ms: 1.08x faster                                                  |
| json_loads           | 31.2 us                                                | 29.4 us: 1.06x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 313 us: 1.06x faster                                                   |
| xml_etree_generate   | 99.4 ms                                                | 96.2 ms: 1.03x faster                                                  |
| pickle_pure_python   | 484 us                                                 | 475 us: 1.02x faster                                                   |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 15.5 ms: 1.06x slower                                                  |
| python_startup_no_site | 5.93 ms                                                | 9.60 ms: 1.62x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.31x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 30.3 ms: 1.05x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 63.1 ms: 1.05x faster                                                  |
| django_template | 48.2 ms                                                | 46.9 ms: 1.03x faster                                                  |
| mako            | 16.3 ms                                                | 18.2 ms: 1.11x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 208 us: 2.61x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 724 ms: 2.44x faster                                                   |
| async_tree_none          | 728 ms                                                 | 335 ms: 2.17x faster                                                   |
| generators               | 80.1 ms                                                | 36.9 ms: 2.17x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 431 ms: 2.02x faster                                                   |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 578 ms: 1.76x faster                                                   |
| pylint                   | 551 ms                                                 | 340 ms: 1.62x faster                                                   |
| deepcopy                 | 479 us                                                 | 316 us: 1.52x faster                                                   |
| deepcopy_memo            | 58.5 us                                                | 40.2 us: 1.45x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 91.9 ms: 1.39x faster                                                  |
| spectral_norm            | 170 ms                                                 | 125 ms: 1.36x faster                                                   |
| coroutines               | 35.1 ms                                                | 26.7 ms: 1.31x faster                                                  |
| richards_super           | 94.7 ms                                                | 73.9 ms: 1.28x faster                                                  |
| richards                 | 79.3 ms                                                | 62.5 ms: 1.27x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 2.48 sec: 1.26x faster                                                 |
| deepcopy_reduce          | 4.17 us                                                | 3.36 us: 1.24x faster                                                  |
| chaos                    | 115 ms                                                 | 93.4 ms: 1.24x faster                                                  |
| pathlib                  | 20.5 ms                                                | 17.0 ms: 1.21x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 96.2 ms: 1.20x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.36 sec: 1.16x faster                                                 |
| regex_compile            | 188 ms                                                 | 164 ms: 1.15x faster                                                   |
| scimark_lu               | 176 ms                                                 | 155 ms: 1.14x faster                                                   |
| nbody                    | 154 ms                                                 | 135 ms: 1.14x faster                                                   |
| comprehensions           | 28.8 us                                                | 25.4 us: 1.13x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 149 ms: 1.13x faster                                                   |
| deltablue                | 7.91 ms                                                | 7.04 ms: 1.12x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 75.1 ms: 1.12x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 105 ms: 1.12x faster                                                   |
| scimark_fft              | 466 ms                                                 | 419 ms: 1.11x faster                                                   |
| docutils                 | 3.30 sec                                               | 2.96 sec: 1.11x faster                                                 |
| sqlglot_normalize        | 143 ms                                                 | 129 ms: 1.11x faster                                                   |
| hexiom                   | 10.4 ms                                                | 9.49 ms: 1.10x faster                                                  |
| float                    | 117 ms                                                 | 107 ms: 1.09x faster                                                   |
| xml_etree_process        | 79.1 ms                                                | 72.4 ms: 1.09x faster                                                  |
| regex_effbot             | 3.63 ms                                                | 3.33 ms: 1.09x faster                                                  |
| pyflate                  | 716 ms                                                 | 659 ms: 1.09x faster                                                   |
| logging_silent           | 190 ns                                                 | 175 ns: 1.08x faster                                                   |
| go                       | 240 ms                                                 | 222 ms: 1.08x faster                                                   |
| json_dumps               | 14.2 ms                                                | 13.2 ms: 1.08x faster                                                  |
| raytrace                 | 507 ms                                                 | 471 ms: 1.08x faster                                                   |
| sympy_sum                | 196 ms                                                 | 183 ms: 1.08x faster                                                   |
| json                     | 5.69 ms                                                | 5.31 ms: 1.07x faster                                                  |
| sqlglot_optimize         | 69.2 ms                                                | 64.9 ms: 1.07x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 2.84 us: 1.06x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 6.08 ms: 1.06x faster                                                  |
| json_loads               | 31.2 us                                                | 29.4 us: 1.06x faster                                                  |
| pprint_safe_repr         | 1.02 sec                                               | 958 ms: 1.06x faster                                                   |
| regex_v8                 | 27.8 ms                                                | 26.2 ms: 1.06x faster                                                  |
| logging_simple           | 8.30 us                                                | 7.84 us: 1.06x faster                                                  |
| thrift                   | 1.07 ms                                                | 1.01 ms: 1.06x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 313 us: 1.06x faster                                                   |
| nqueens                  | 106 ms                                                 | 100 ms: 1.05x faster                                                   |
| pidigits                 | 191 ms                                                 | 181 ms: 1.05x faster                                                   |
| sympy_integrate          | 25.8 ms                                                | 24.5 ms: 1.05x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 2.00 sec: 1.05x faster                                                 |
| genshi_text              | 31.8 ms                                                | 30.3 ms: 1.05x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 63.1 ms: 1.05x faster                                                  |
| scimark_sor              | 220 ms                                                 | 211 ms: 1.04x faster                                                   |
| sympy_str                | 346 ms                                                 | 334 ms: 1.04x faster                                                   |
| logging_format           | 9.09 us                                                | 8.79 us: 1.03x faster                                                  |
| xml_etree_generate       | 99.4 ms                                                | 96.2 ms: 1.03x faster                                                  |
| django_template          | 48.2 ms                                                | 46.9 ms: 1.03x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 475 us: 1.02x faster                                                   |
| html5lib                 | 88.9 ms                                                | 87.3 ms: 1.02x faster                                                  |
| sympy_expand             | 566 ms                                                 | 556 ms: 1.02x faster                                                   |
| sqlglot_transpile        | 2.57 ms                                                | 2.54 ms: 1.01x faster                                                  |
| fannkuch                 | 532 ms                                                 | 525 ms: 1.01x faster                                                   |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                   |
| 2to3                     | 348 ms                                                 | 346 ms: 1.01x faster                                                   |
| regex_dna                | 227 ms                                                 | 226 ms: 1.00x faster                                                   |
| sqlglot_parse            | 2.17 ms                                                | 2.19 ms: 1.01x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 3.67 ms: 1.01x slower                                                  |
| sqlalchemy_declarative   | 172 ms                                                 | 181 ms: 1.05x slower                                                   |
| mdp                      | 2.85 sec                                               | 3.03 sec: 1.06x slower                                                 |
| python_startup           | 14.6 ms                                                | 15.5 ms: 1.06x slower                                                  |
| meteor_contest           | 120 ms                                                 | 131 ms: 1.10x slower                                                   |
| mako                     | 16.3 ms                                                | 18.2 ms: 1.11x slower                                                  |
| async_generators         | 444 ms                                                 | 497 ms: 1.12x slower                                                   |
| telco                    | 7.27 ms                                                | 9.14 ms: 1.26x slower                                                  |
| coverage                 | 79.4 ms                                                | 102 ms: 1.28x slower                                                   |
| create_gc_cycles         | 1.62 ms                                                | 2.34 ms: 1.44x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 9.60 ms: 1.62x slower                                                  |
| bench_thread_pool        | 986 us                                                 | 3.56 ms: 3.61x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 95.3 ms: 3.97x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.09x faster                                                           |

Benchmark hidden because not significant (1): sqlalchemy_imperative
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250102-3.14.0a3+-b20a605-NOGIL/bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.127x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.50x