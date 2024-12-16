# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: trace_function_entry
- machine: darwin-arm64
- commit hash: fcc6f57
- commit date: 2024-12-16
- overall geometric mean: 1.268x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: 1.36x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241216-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 171 ms: 1.12x faster                                                             |
| docutils       | 1.73 sec                                               | 1.45 sec: 1.19x faster                                                           |
| html5lib       | 42.4 ms                                                | 33.0 ms: 1.28x faster                                                            |
| Geometric mean | (ref)                                                  | 1.20x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241216-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io           | 980 ms                                                 | 376 ms: 2.61x faster                                                             |
| async_tree_memoization  | 474 ms                                                 | 201 ms: 2.36x faster                                                             |
| async_tree_none         | 388 ms                                                 | 167 ms: 2.33x faster                                                             |
| async_tree_cpu_io_mixed | 649 ms                                                 | 419 ms: 1.55x faster                                                             |
| Geometric mean          | (ref)                                                  | 2.17x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241216-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 63.7 ms: 1.46x faster                                                            |
| float          | 69.0 ms                                                | 50.5 ms: 1.37x faster                                                            |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                                             |
| Geometric mean | (ref)                                                  | 1.26x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241216-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 69.8 ms: 1.36x faster                                                            |
| regex_dna      | 174 ms                                                 | 136 ms: 1.29x faster                                                             |
| regex_effbot   | 2.46 ms                                                | 2.03 ms: 1.21x faster                                                            |
| regex_v8       | 17.1 ms                                                | 15.9 ms: 1.08x faster                                                            |
| Geometric mean | (ref)                                                  | 1.23x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241216-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_pure_python | 194 us                                                 | 127 us: 1.54x faster                                                             |
| pickle_pure_python   | 281 us                                                 | 190 us: 1.48x faster                                                             |
| tomli_loads          | 1.71 sec                                               | 1.21 sec: 1.42x faster                                                           |
| xml_etree_process    | 46.5 ms                                                | 35.1 ms: 1.32x faster                                                            |
| json_dumps           | 8.11 ms                                                | 7.16 ms: 1.13x faster                                                            |
| xml_etree_generate   | 53.5 ms                                                | 49.0 ms: 1.09x faster                                                            |
| xml_etree_parse      | 108 ms                                                 | 102 ms: 1.06x faster                                                             |
| json_loads           | 16.4 us                                                | 16.5 us: 1.01x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.21x faster                                                                     |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241216-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 21.6 ms: 1.98x slower                                                            |
| python_startup_no_site | 7.91 ms                                                | 16.6 ms: 2.09x slower                                                            |
| Geometric mean         | (ref)                                                  | 2.04x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241216-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.26 ms: 1.58x faster                                                            |
| django_template | 26.4 ms                                                | 21.1 ms: 1.25x faster                                                            |
| genshi_text     | 17.3 ms                                                | 14.5 ms: 1.20x faster                                                            |
| genshi_xml      | 33.8 ms                                                | 30.7 ms: 1.10x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.27x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241216-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 100 us: 3.23x faster                                                             |
| async_tree_io            | 980 ms                                                 | 376 ms: 2.61x faster                                                             |
| async_tree_memoization   | 474 ms                                                 | 201 ms: 2.36x faster                                                             |
| async_tree_none          | 388 ms                                                 | 167 ms: 2.33x faster                                                             |
| deltablue                | 4.91 ms                                                | 2.56 ms: 1.92x faster                                                            |
| deepcopy_memo            | 34.7 us                                                | 18.3 us: 1.90x faster                                                            |
| deepcopy                 | 272 us                                                 | 153 us: 1.77x faster                                                             |
| raytrace                 | 301 ms                                                 | 173 ms: 1.74x faster                                                             |
| pylint                   | 277 ms                                                 | 162 ms: 1.71x faster                                                             |
| asyncio_websockets       | 410 ms                                                 | 242 ms: 1.70x faster                                                             |
| go                       | 151 ms                                                 | 89.3 ms: 1.69x faster                                                            |
| chaos                    | 65.8 ms                                                | 40.2 ms: 1.64x faster                                                            |
| logging_silent           | 117 ns                                                 | 71.9 ns: 1.63x faster                                                            |
| mako                     | 9.87 ms                                                | 6.26 ms: 1.58x faster                                                            |
| richards_super           | 57.8 ms                                                | 37.3 ms: 1.55x faster                                                            |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 419 ms: 1.55x faster                                                             |
| unpickle_pure_python     | 194 us                                                 | 127 us: 1.54x faster                                                             |
| spectral_norm            | 94.8 ms                                                | 63.0 ms: 1.50x faster                                                            |
| pickle_pure_python       | 281 us                                                 | 190 us: 1.48x faster                                                             |
| scimark_monte_carlo      | 65.6 ms                                                | 44.8 ms: 1.46x faster                                                            |
| nbody                    | 93.0 ms                                                | 63.7 ms: 1.46x faster                                                            |
| richards                 | 48.7 ms                                                | 33.6 ms: 1.45x faster                                                            |
| deepcopy_reduce          | 2.33 us                                                | 1.61 us: 1.44x faster                                                            |
| sqlglot_parse            | 1.24 ms                                                | 867 us: 1.43x faster                                                             |
| tomli_loads              | 1.71 sec                                               | 1.21 sec: 1.42x faster                                                           |
| sqlglot_transpile        | 1.44 ms                                                | 1.04 ms: 1.38x faster                                                            |
| generators               | 32.3 ms                                                | 23.4 ms: 1.38x faster                                                            |
| pyflate                  | 427 ms                                                 | 310 ms: 1.38x faster                                                             |
| scimark_lu               | 103 ms                                                 | 74.7 ms: 1.38x faster                                                            |
| float                    | 69.0 ms                                                | 50.5 ms: 1.37x faster                                                            |
| regex_compile            | 95.3 ms                                                | 69.8 ms: 1.36x faster                                                            |
| hexiom                   | 6.19 ms                                                | 4.58 ms: 1.35x faster                                                            |
| crypto_pyaes             | 71.8 ms                                                | 53.9 ms: 1.33x faster                                                            |
| xml_etree_process        | 46.5 ms                                                | 35.1 ms: 1.32x faster                                                            |
| scimark_sor              | 128 ms                                                 | 97.3 ms: 1.32x faster                                                            |
| thrift                   | 572 us                                                 | 435 us: 1.32x faster                                                             |
| pprint_pformat           | 1.30 sec                                               | 991 ms: 1.32x faster                                                             |
| logging_simple           | 4.45 us                                                | 3.39 us: 1.31x faster                                                            |
| pprint_safe_repr         | 641 ms                                                 | 489 ms: 1.31x faster                                                             |
| scimark_fft              | 224 ms                                                 | 172 ms: 1.31x faster                                                             |
| sqlalchemy_imperative    | 8.86 ms                                                | 6.79 ms: 1.31x faster                                                            |
| logging_format           | 4.83 us                                                | 3.70 us: 1.30x faster                                                            |
| comprehensions           | 16.9 us                                                | 13.0 us: 1.30x faster                                                            |
| pycparser                | 877 ms                                                 | 681 ms: 1.29x faster                                                             |
| regex_dna                | 174 ms                                                 | 136 ms: 1.29x faster                                                             |
| html5lib                 | 42.4 ms                                                | 33.0 ms: 1.28x faster                                                            |
| sympy_sum                | 92.2 ms                                                | 73.5 ms: 1.25x faster                                                            |
| django_template          | 26.4 ms                                                | 21.1 ms: 1.25x faster                                                            |
| sqlalchemy_declarative   | 73.3 ms                                                | 59.0 ms: 1.24x faster                                                            |
| regex_effbot             | 2.46 ms                                                | 2.03 ms: 1.21x faster                                                            |
| genshi_text              | 17.3 ms                                                | 14.5 ms: 1.20x faster                                                            |
| dulwich_log              | 35.3 ms                                                | 29.6 ms: 1.19x faster                                                            |
| docutils                 | 1.73 sec                                               | 1.45 sec: 1.19x faster                                                           |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.88 ms: 1.19x faster                                                            |
| coroutines               | 20.7 ms                                                | 17.7 ms: 1.17x faster                                                            |
| sympy_str                | 165 ms                                                 | 143 ms: 1.16x faster                                                             |
| mypy2                    | 607 ms                                                 | 525 ms: 1.16x faster                                                             |
| json_dumps               | 8.11 ms                                                | 7.16 ms: 1.13x faster                                                            |
| sympy_integrate          | 13.1 ms                                                | 11.6 ms: 1.13x faster                                                            |
| fannkuch                 | 303 ms                                                 | 270 ms: 1.12x faster                                                             |
| 2to3                     | 192 ms                                                 | 171 ms: 1.12x faster                                                             |
| sympy_expand             | 269 ms                                                 | 242 ms: 1.11x faster                                                             |
| nqueens                  | 63.8 ms                                                | 57.8 ms: 1.10x faster                                                            |
| genshi_xml               | 33.8 ms                                                | 30.7 ms: 1.10x faster                                                            |
| sqlglot_optimize         | 36.8 ms                                                | 33.6 ms: 1.09x faster                                                            |
| xml_etree_generate       | 53.5 ms                                                | 49.0 ms: 1.09x faster                                                            |
| pathlib                  | 24.5 ms                                                | 22.5 ms: 1.09x faster                                                            |
| meteor_contest           | 77.7 ms                                                | 71.7 ms: 1.08x faster                                                            |
| mdp                      | 1.63 sec                                               | 1.50 sec: 1.08x faster                                                           |
| regex_v8                 | 17.1 ms                                                | 15.9 ms: 1.08x faster                                                            |
| json                     | 3.08 ms                                                | 2.89 ms: 1.07x faster                                                            |
| bench_thread_pool        | 527 us                                                 | 497 us: 1.06x faster                                                             |
| xml_etree_parse          | 108 ms                                                 | 102 ms: 1.06x faster                                                             |
| sqlglot_normalize        | 190 ms                                                 | 182 ms: 1.04x faster                                                             |
| pidigits                 | 282 ms                                                 | 283 ms: 1.00x slower                                                             |
| json_loads               | 16.4 us                                                | 16.5 us: 1.01x slower                                                            |
| sqlite_synth             | 1.46 us                                                | 1.55 us: 1.06x slower                                                            |
| coverage                 | 41.5 ms                                                | 44.2 ms: 1.07x slower                                                            |
| async_generators         | 231 ms                                                 | 282 ms: 1.22x slower                                                             |
| telco                    | 3.49 ms                                                | 4.51 ms: 1.29x slower                                                            |
| gc_traversal             | 2.36 ms                                                | 3.07 ms: 1.30x slower                                                            |
| create_gc_cycles         | 860 us                                                 | 1.26 ms: 1.47x slower                                                            |
| bench_mp_pool            | 37.4 ms                                                | 63.7 ms: 1.70x slower                                                            |
| python_startup           | 10.9 ms                                                | 21.6 ms: 1.98x slower                                                            |
| python_startup_no_site   | 7.91 ms                                                | 16.6 ms: 2.09x slower                                                            |
| Geometric mean           | (ref)                                                  | 1.26x faster                                                                     |

Benchmark hidden because not significant (1): xml_etree_iterparse
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (19) of results/bm-20241216-3.14.0a2+-fcc6f57-JIT/bm-20241216-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.268x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: 1.36x