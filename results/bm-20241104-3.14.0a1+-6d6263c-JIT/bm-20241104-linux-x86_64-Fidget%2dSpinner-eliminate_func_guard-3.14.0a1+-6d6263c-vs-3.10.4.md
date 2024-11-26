# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: eliminate_func_guard
- machine: linux-x86_64
- commit hash: 6d6263c
- commit date: 2024-11-04
- overall geometric mean: 1.382x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241104-linux-x86_64-Fidget%2dSpinner-eliminate_func_guard-3.14.0a1+-6d6263c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 280 ms: 1.25x faster                                                             |
| docutils       | 3.30 sec                                               | 2.95 sec: 1.12x faster                                                           |
| html5lib       | 88.9 ms                                                | 67.0 ms: 1.33x faster                                                            |
| tornado_http   | 136 ms                                                 | 94.9 ms: 1.44x faster                                                            |
| Geometric mean | (ref)                                                  | 1.28x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241104-linux-x86_64-Fidget%2dSpinner-eliminate_func_guard-3.14.0a1+-6d6263c |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 331 ms: 2.20x faster                                                             |
| async_tree_memoization  | 870 ms                                                 | 419 ms: 2.08x faster                                                             |
| async_tree_io           | 1.77 sec                                               | 863 ms: 2.05x faster                                                             |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 572 ms: 1.78x faster                                                             |
| Geometric mean          | (ref)                                                  | 2.02x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241104-linux-x86_64-Fidget%2dSpinner-eliminate_func_guard-3.14.0a1+-6d6263c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 82.7 ms: 1.86x faster                                                            |
| float          | 117 ms                                                 | 76.1 ms: 1.54x faster                                                            |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                             |
| Geometric mean | (ref)                                                  | 1.43x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241104-linux-x86_64-Fidget%2dSpinner-eliminate_func_guard-3.14.0a1+-6d6263c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 140 ms: 1.35x faster                                                             |
| regex_v8       | 27.8 ms                                                | 25.3 ms: 1.10x faster                                                            |
| regex_dna      | 227 ms                                                 | 220 ms: 1.03x faster                                                             |
| regex_effbot   | 3.63 ms                                                | 3.81 ms: 1.05x slower                                                            |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241104-linux-x86_64-Fidget%2dSpinner-eliminate_func_guard-3.14.0a1+-6d6263c |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.95 sec: 1.61x faster                                                           |
| unpickle_pure_python | 331 us                                                 | 217 us: 1.52x faster                                                             |
| pickle_pure_python   | 484 us                                                 | 325 us: 1.49x faster                                                             |
| xml_etree_process    | 79.1 ms                                                | 56.2 ms: 1.41x faster                                                            |
| json_dumps           | 14.2 ms                                                | 11.1 ms: 1.28x faster                                                            |
| xml_etree_generate   | 99.4 ms                                                | 79.0 ms: 1.26x faster                                                            |
| json_loads           | 31.2 us                                                | 26.8 us: 1.16x faster                                                            |
| xml_etree_iterparse  | 115 ms                                                 | 100 ms: 1.15x faster                                                             |
| xml_etree_parse      | 168 ms                                                 | 147 ms: 1.14x faster                                                             |
| Geometric mean       | (ref)                                                  | 1.33x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241104-linux-x86_64-Fidget%2dSpinner-eliminate_func_guard-3.14.0a1+-6d6263c |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.7 ms: 1.14x faster                                                            |
| python_startup_no_site | 5.93 ms                                                | 7.11 ms: 1.20x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241104-linux-x86_64-Fidget%2dSpinner-eliminate_func_guard-3.14.0a1+-6d6263c |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.2 ms: 1.60x faster                                                            |
| django_template | 48.2 ms                                                | 36.2 ms: 1.33x faster                                                            |
| genshi_text     | 31.8 ms                                                | 24.7 ms: 1.29x faster                                                            |
| genshi_xml      | 66.0 ms                                                | 58.6 ms: 1.13x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.33x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241104-linux-x86_64-Fidget%2dSpinner-eliminate_func_guard-3.14.0a1+-6d6263c |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.25x faster                                                             |
| deltablue                | 7.91 ms                                                | 3.30 ms: 2.40x faster                                                            |
| generators               | 80.1 ms                                                | 35.4 ms: 2.26x faster                                                            |
| async_tree_none          | 728 ms                                                 | 331 ms: 2.20x faster                                                             |
| async_tree_memoization   | 870 ms                                                 | 419 ms: 2.08x faster                                                             |
| async_tree_io            | 1.77 sec                                               | 863 ms: 2.05x faster                                                             |
| deepcopy_memo            | 58.5 us                                                | 29.6 us: 1.97x faster                                                            |
| richards_super           | 94.7 ms                                                | 48.2 ms: 1.96x faster                                                            |
| chaos                    | 115 ms                                                 | 59.7 ms: 1.93x faster                                                            |
| richards                 | 79.3 ms                                                | 41.9 ms: 1.89x faster                                                            |
| crypto_pyaes             | 128 ms                                                 | 68.1 ms: 1.88x faster                                                            |
| logging_silent           | 190 ns                                                 | 101 ns: 1.88x faster                                                             |
| nbody                    | 154 ms                                                 | 82.7 ms: 1.86x faster                                                            |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.84x faster                                                             |
| scimark_monte_carlo      | 118 ms                                                 | 64.8 ms: 1.82x faster                                                            |
| raytrace                 | 507 ms                                                 | 280 ms: 1.81x faster                                                             |
| go                       | 240 ms                                                 | 133 ms: 1.80x faster                                                             |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 572 ms: 1.78x faster                                                             |
| deepcopy                 | 479 us                                                 | 271 us: 1.77x faster                                                             |
| comprehensions           | 28.8 us                                                | 17.3 us: 1.66x faster                                                            |
| sqlglot_parse            | 2.17 ms                                                | 1.34 ms: 1.62x faster                                                            |
| tomli_loads              | 3.14 sec                                               | 1.95 sec: 1.61x faster                                                           |
| mako                     | 16.3 ms                                                | 10.2 ms: 1.60x faster                                                            |
| pyflate                  | 716 ms                                                 | 458 ms: 1.56x faster                                                             |
| deepcopy_reduce          | 4.17 us                                                | 2.69 us: 1.55x faster                                                            |
| scimark_lu               | 176 ms                                                 | 114 ms: 1.54x faster                                                             |
| float                    | 117 ms                                                 | 76.1 ms: 1.54x faster                                                            |
| sqlglot_transpile        | 2.57 ms                                                | 1.69 ms: 1.53x faster                                                            |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.52x faster                                                             |
| coroutines               | 35.1 ms                                                | 23.3 ms: 1.51x faster                                                            |
| pickle_pure_python       | 484 us                                                 | 325 us: 1.49x faster                                                             |
| logging_format           | 9.09 us                                                | 6.13 us: 1.48x faster                                                            |
| spectral_norm            | 170 ms                                                 | 115 ms: 1.48x faster                                                             |
| logging_simple           | 8.30 us                                                | 5.64 us: 1.47x faster                                                            |
| hexiom                   | 10.4 ms                                                | 7.06 ms: 1.47x faster                                                            |
| scimark_fft              | 466 ms                                                 | 320 ms: 1.46x faster                                                             |
| pylint                   | 551 ms                                                 | 379 ms: 1.45x faster                                                             |
| tornado_http             | 136 ms                                                 | 94.9 ms: 1.44x faster                                                            |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.42x faster                                                           |
| pprint_safe_repr         | 1.02 sec                                               | 721 ms: 1.41x faster                                                             |
| xml_etree_process        | 79.1 ms                                                | 56.2 ms: 1.41x faster                                                            |
| thrift                   | 1.07 ms                                                | 784 us: 1.37x faster                                                             |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                                           |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.78 ms: 1.35x faster                                                            |
| regex_compile            | 188 ms                                                 | 140 ms: 1.35x faster                                                             |
| django_template          | 48.2 ms                                                | 36.2 ms: 1.33x faster                                                            |
| html5lib                 | 88.9 ms                                                | 67.0 ms: 1.33x faster                                                            |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.6 ms: 1.32x faster                                                            |
| fannkuch                 | 532 ms                                                 | 404 ms: 1.32x faster                                                             |
| genshi_text              | 31.8 ms                                                | 24.7 ms: 1.29x faster                                                            |
| json_dumps               | 14.2 ms                                                | 11.1 ms: 1.28x faster                                                            |
| pathlib                  | 20.5 ms                                                | 16.2 ms: 1.26x faster                                                            |
| xml_etree_generate       | 99.4 ms                                                | 79.0 ms: 1.26x faster                                                            |
| sqlglot_normalize        | 143 ms                                                 | 115 ms: 1.25x faster                                                             |
| dulwich_log              | 84.3 ms                                                | 67.7 ms: 1.25x faster                                                            |
| 2to3                     | 348 ms                                                 | 280 ms: 1.25x faster                                                             |
| nqueens                  | 106 ms                                                 | 87.9 ms: 1.20x faster                                                            |
| sqlalchemy_declarative   | 172 ms                                                 | 147 ms: 1.17x faster                                                             |
| json_loads               | 31.2 us                                                | 26.8 us: 1.16x faster                                                            |
| sqlglot_optimize         | 69.2 ms                                                | 59.7 ms: 1.16x faster                                                            |
| xml_etree_iterparse      | 115 ms                                                 | 100 ms: 1.15x faster                                                             |
| json                     | 5.69 ms                                                | 4.96 ms: 1.15x faster                                                            |
| python_startup           | 14.6 ms                                                | 12.7 ms: 1.14x faster                                                            |
| xml_etree_parse          | 168 ms                                                 | 147 ms: 1.14x faster                                                             |
| sympy_str                | 346 ms                                                 | 303 ms: 1.14x faster                                                             |
| genshi_xml               | 66.0 ms                                                | 58.6 ms: 1.13x faster                                                            |
| sympy_expand             | 566 ms                                                 | 504 ms: 1.12x faster                                                             |
| sympy_sum                | 196 ms                                                 | 176 ms: 1.12x faster                                                             |
| mdp                      | 2.85 sec                                               | 2.55 sec: 1.12x faster                                                           |
| docutils                 | 3.30 sec                                               | 2.95 sec: 1.12x faster                                                           |
| bench_thread_pool        | 986 us                                                 | 888 us: 1.11x faster                                                             |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                             |
| sympy_integrate          | 25.8 ms                                                | 23.5 ms: 1.10x faster                                                            |
| regex_v8                 | 27.8 ms                                                | 25.3 ms: 1.10x faster                                                            |
| sqlite_synth             | 3.02 us                                                | 2.80 us: 1.08x faster                                                            |
| regex_dna                | 227 ms                                                 | 220 ms: 1.03x faster                                                             |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                             |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                                             |
| async_generators         | 444 ms                                                 | 448 ms: 1.01x slower                                                             |
| regex_effbot             | 3.63 ms                                                | 3.81 ms: 1.05x slower                                                            |
| telco                    | 7.27 ms                                                | 7.68 ms: 1.06x slower                                                            |
| coverage                 | 79.4 ms                                                | 84.8 ms: 1.07x slower                                                            |
| python_startup_no_site   | 5.93 ms                                                | 7.11 ms: 1.20x slower                                                            |
| gc_traversal             | 3.62 ms                                                | 4.57 ms: 1.26x slower                                                            |
| create_gc_cycles         | 1.62 ms                                                | 2.67 ms: 1.65x slower                                                            |
| bench_mp_pool            | 24.0 ms                                                | 84.4 ms: 3.51x slower                                                            |
| Geometric mean           | (ref)                                                  | 1.36x faster                                                                     |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (9) of results/bm-20241104-3.14.0a1+-6d6263c-JIT/bm-20241104-linux-x86_64-Fidget%2dSpinner-eliminate_func_guard-3.14.0a1+-6d6263c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.382x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.33x