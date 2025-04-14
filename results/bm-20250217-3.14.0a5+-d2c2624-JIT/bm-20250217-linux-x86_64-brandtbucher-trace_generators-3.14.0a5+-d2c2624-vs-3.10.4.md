# Results vs. 3.10.4

- fork: brandtbucher
- ref: trace_generators
- machine: linux-x86_64
- commit hash: d2c2624
- commit date: 2025-02-17
- overall geometric mean: 1.435x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250217-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-d2c2624 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 265 ms: 1.32x faster                                                     |
| docutils       | 3.30 sec                                               | 2.67 sec: 1.23x faster                                                   |
| html5lib       | 88.9 ms                                                | 62.5 ms: 1.42x faster                                                    |
| Geometric mean | (ref)                                                  | 1.32x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250217-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-d2c2624 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 623 ms: 2.84x faster                                                     |
| async_tree_none         | 728 ms                                                 | 269 ms: 2.70x faster                                                     |
| async_tree_memoization  | 870 ms                                                 | 326 ms: 2.67x faster                                                     |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 493 ms: 2.06x faster                                                     |
| Geometric mean          | (ref)                                                  | 2.55x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250217-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-d2c2624 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 70.8 ms: 1.65x faster                                                    |
| nbody          | 154 ms                                                 | 99.2 ms: 1.55x faster                                                    |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                  | 1.38x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250217-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-d2c2624 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 125 ms: 1.51x faster                                                     |
| regex_effbot   | 3.63 ms                                                | 3.09 ms: 1.18x faster                                                    |
| regex_v8       | 27.8 ms                                                | 23.9 ms: 1.16x faster                                                    |
| regex_dna      | 227 ms                                                 | 207 ms: 1.10x faster                                                     |
| Geometric mean | (ref)                                                  | 1.23x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250217-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-d2c2624 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.85 sec: 1.70x faster                                                   |
| unpickle_pure_python | 331 us                                                 | 211 us: 1.57x faster                                                     |
| pickle_pure_python   | 484 us                                                 | 328 us: 1.48x faster                                                     |
| xml_etree_process    | 79.1 ms                                                | 56.1 ms: 1.41x faster                                                    |
| xml_etree_generate   | 99.4 ms                                                | 79.1 ms: 1.26x faster                                                    |
| xml_etree_parse      | 168 ms                                                 | 139 ms: 1.21x faster                                                     |
| json_dumps           | 14.2 ms                                                | 11.7 ms: 1.21x faster                                                    |
| xml_etree_iterparse  | 115 ms                                                 | 97.0 ms: 1.19x faster                                                    |
| json_loads           | 31.2 us                                                | 28.7 us: 1.09x faster                                                    |
| Geometric mean       | (ref)                                                  | 1.33x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250217-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-d2c2624 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                    |
| python_startup_no_site | 5.93 ms                                                | 7.05 ms: 1.19x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250217-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-d2c2624 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.3 ms: 1.59x faster                                                    |
| django_template | 48.2 ms                                                | 31.8 ms: 1.51x faster                                                    |
| genshi_text     | 31.8 ms                                                | 23.7 ms: 1.34x faster                                                    |
| genshi_xml      | 66.0 ms                                                | 52.2 ms: 1.26x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250217-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-d2c2624 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 164 us: 3.31x faster                                                     |
| async_tree_io            | 1.77 sec                                               | 623 ms: 2.84x faster                                                     |
| async_tree_none          | 728 ms                                                 | 269 ms: 2.70x faster                                                     |
| async_tree_memoization   | 870 ms                                                 | 326 ms: 2.67x faster                                                     |
| deltablue                | 7.91 ms                                                | 3.39 ms: 2.34x faster                                                    |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 493 ms: 2.06x faster                                                     |
| generators               | 80.1 ms                                                | 40.7 ms: 1.97x faster                                                    |
| chaos                    | 115 ms                                                 | 58.9 ms: 1.96x faster                                                    |
| pylint                   | 551 ms                                                 | 282 ms: 1.96x faster                                                     |
| deepcopy_memo            | 58.5 us                                                | 30.3 us: 1.93x faster                                                    |
| go                       | 240 ms                                                 | 125 ms: 1.91x faster                                                     |
| richards_super           | 94.7 ms                                                | 50.4 ms: 1.88x faster                                                    |
| deepcopy                 | 479 us                                                 | 257 us: 1.86x faster                                                     |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.85x faster                                                     |
| logging_silent           | 190 ns                                                 | 104 ns: 1.82x faster                                                     |
| raytrace                 | 507 ms                                                 | 279 ms: 1.82x faster                                                     |
| richards                 | 79.3 ms                                                | 44.1 ms: 1.80x faster                                                    |
| crypto_pyaes             | 128 ms                                                 | 71.7 ms: 1.78x faster                                                    |
| scimark_monte_carlo      | 118 ms                                                 | 66.7 ms: 1.77x faster                                                    |
| spectral_norm            | 170 ms                                                 | 98.0 ms: 1.73x faster                                                    |
| tomli_loads              | 3.14 sec                                               | 1.85 sec: 1.70x faster                                                   |
| sqlglot_parse            | 2.17 ms                                                | 1.30 ms: 1.67x faster                                                    |
| comprehensions           | 28.8 us                                                | 17.3 us: 1.66x faster                                                    |
| float                    | 117 ms                                                 | 70.8 ms: 1.65x faster                                                    |
| sqlglot_transpile        | 2.57 ms                                                | 1.60 ms: 1.61x faster                                                    |
| mako                     | 16.3 ms                                                | 10.3 ms: 1.59x faster                                                    |
| unpickle_pure_python     | 331 us                                                 | 211 us: 1.57x faster                                                     |
| hexiom                   | 10.4 ms                                                | 6.71 ms: 1.55x faster                                                    |
| pyflate                  | 716 ms                                                 | 462 ms: 1.55x faster                                                     |
| nbody                    | 154 ms                                                 | 99.2 ms: 1.55x faster                                                    |
| deepcopy_reduce          | 4.17 us                                                | 2.70 us: 1.55x faster                                                    |
| django_template          | 48.2 ms                                                | 31.8 ms: 1.51x faster                                                    |
| regex_compile            | 188 ms                                                 | 125 ms: 1.51x faster                                                     |
| logging_simple           | 8.30 us                                                | 5.52 us: 1.50x faster                                                    |
| logging_format           | 9.09 us                                                | 6.09 us: 1.49x faster                                                    |
| scimark_lu               | 176 ms                                                 | 118 ms: 1.49x faster                                                     |
| coroutines               | 35.1 ms                                                | 23.7 ms: 1.48x faster                                                    |
| pickle_pure_python       | 484 us                                                 | 328 us: 1.48x faster                                                     |
| scimark_fft              | 466 ms                                                 | 319 ms: 1.46x faster                                                     |
| html5lib                 | 88.9 ms                                                | 62.5 ms: 1.42x faster                                                    |
| thrift                   | 1.07 ms                                                | 759 us: 1.41x faster                                                     |
| xml_etree_process        | 79.1 ms                                                | 56.1 ms: 1.41x faster                                                    |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.60 ms: 1.41x faster                                                    |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.8 ms: 1.39x faster                                                    |
| pprint_safe_repr         | 1.02 sec                                               | 737 ms: 1.38x faster                                                     |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                                   |
| pprint_pformat           | 2.10 sec                                               | 1.56 sec: 1.35x faster                                                   |
| genshi_text              | 31.8 ms                                                | 23.7 ms: 1.34x faster                                                    |
| sqlglot_normalize        | 143 ms                                                 | 107 ms: 1.34x faster                                                     |
| fannkuch                 | 532 ms                                                 | 401 ms: 1.33x faster                                                     |
| 2to3                     | 348 ms                                                 | 265 ms: 1.32x faster                                                     |
| sqlalchemy_declarative   | 172 ms                                                 | 131 ms: 1.32x faster                                                     |
| sympy_sum                | 196 ms                                                 | 150 ms: 1.31x faster                                                     |
| nqueens                  | 106 ms                                                 | 81.3 ms: 1.30x faster                                                    |
| sqlglot_optimize         | 69.2 ms                                                | 53.5 ms: 1.29x faster                                                    |
| sympy_integrate          | 25.8 ms                                                | 20.0 ms: 1.29x faster                                                    |
| sympy_str                | 346 ms                                                 | 272 ms: 1.27x faster                                                     |
| genshi_xml               | 66.0 ms                                                | 52.2 ms: 1.26x faster                                                    |
| xml_etree_generate       | 99.4 ms                                                | 79.1 ms: 1.26x faster                                                    |
| pathlib                  | 20.5 ms                                                | 16.4 ms: 1.25x faster                                                    |
| dulwich_log              | 84.3 ms                                                | 68.0 ms: 1.24x faster                                                    |
| docutils                 | 3.30 sec                                               | 2.67 sec: 1.23x faster                                                   |
| xml_etree_parse          | 168 ms                                                 | 139 ms: 1.21x faster                                                     |
| json_dumps               | 14.2 ms                                                | 11.7 ms: 1.21x faster                                                    |
| sympy_expand             | 566 ms                                                 | 468 ms: 1.21x faster                                                     |
| xml_etree_iterparse      | 115 ms                                                 | 97.0 ms: 1.19x faster                                                    |
| regex_effbot             | 3.63 ms                                                | 3.09 ms: 1.18x faster                                                    |
| regex_v8                 | 27.8 ms                                                | 23.9 ms: 1.16x faster                                                    |
| mdp                      | 2.85 sec                                               | 2.49 sec: 1.14x faster                                                   |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                    |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.11x faster                                                     |
| bench_thread_pool        | 986 us                                                 | 888 us: 1.11x faster                                                     |
| sqlite_synth             | 3.02 us                                                | 2.74 us: 1.10x faster                                                    |
| json                     | 5.69 ms                                                | 5.16 ms: 1.10x faster                                                    |
| regex_dna                | 227 ms                                                 | 207 ms: 1.10x faster                                                     |
| json_loads               | 31.2 us                                                | 28.7 us: 1.09x faster                                                    |
| async_generators         | 444 ms                                                 | 411 ms: 1.08x faster                                                     |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                     |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                     |
| telco                    | 7.27 ms                                                | 7.74 ms: 1.07x slower                                                    |
| coverage                 | 79.4 ms                                                | 89.2 ms: 1.12x slower                                                    |
| python_startup_no_site   | 5.93 ms                                                | 7.05 ms: 1.19x slower                                                    |
| gc_traversal             | 3.62 ms                                                | 4.77 ms: 1.32x slower                                                    |
| create_gc_cycles         | 1.62 ms                                                | 2.47 ms: 1.52x slower                                                    |
| bench_mp_pool            | 24.0 ms                                                | 81.4 ms: 3.39x slower                                                    |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                             |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250217-3.14.0a5+-d2c2624-JIT/bm-20250217-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-d2c2624.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.435x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.28x