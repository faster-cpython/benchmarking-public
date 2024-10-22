# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: deferred_globals_fin
- machine: darwin-arm64
- commit hash: bfd4400
- commit date: 2024-08-28
- overall geometric mean: 1.29x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: 0.59x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-darwin-arm64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 163 ms: 1.17x faster                                                            |
| docutils       | 1.73 sec                                               | 1.48 sec: 1.17x faster                                                          |
| html5lib       | 42.4 ms                                                | 31.6 ms: 1.34x faster                                                           |
| Geometric mean | (ref)                                                  | 1.19x faster                                                                    |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-darwin-arm64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 196 ms: 1.98x faster                                                            |
| async_tree_memoization  | 474 ms                                                 | 242 ms: 1.95x faster                                                            |
| async_tree_io           | 980 ms                                                 | 547 ms: 1.79x faster                                                            |
| async_tree_cpu_io_mixed | 649 ms                                                 | 453 ms: 1.43x faster                                                            |
| Geometric mean          | (ref)                                                  | 1.77x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-darwin-arm64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 59.4 ms: 1.57x faster                                                           |
| float          | 69.0 ms                                                | 48.4 ms: 1.43x faster                                                           |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                  | 1.31x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-darwin-arm64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 68.5 ms: 1.39x faster                                                           |
| regex_dna      | 174 ms                                                 | 146 ms: 1.19x faster                                                            |
| regex_v8       | 17.1 ms                                                | 16.6 ms: 1.04x faster                                                           |
| regex_effbot   | 2.46 ms                                                | 2.50 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                  | 1.14x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-darwin-arm64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 184 us: 1.52x faster                                                            |
| unpickle_pure_python | 194 us                                                 | 144 us: 1.36x faster                                                            |
| json_dumps           | 8.11 ms                                                | 6.52 ms: 1.24x faster                                                           |
| xml_etree_process    | 46.5 ms                                                | 38.3 ms: 1.21x faster                                                           |
| tomli_loads          | 1.71 sec                                               | 1.50 sec: 1.14x faster                                                          |
| xml_etree_generate   | 53.5 ms                                                | 53.4 ms: 1.00x faster                                                           |
| xml_etree_iterparse  | 72.1 ms                                                | 74.3 ms: 1.03x slower                                                           |
| json_loads           | 16.4 us                                                | 17.3 us: 1.05x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.14x faster                                                                    |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-darwin-arm64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 16.4 ms: 1.51x slower                                                           |
| python_startup_no_site | 7.91 ms                                                | 13.4 ms: 1.69x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.60x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-darwin-arm64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 7.16 ms: 1.38x faster                                                           |
| django_template | 26.4 ms                                                | 19.8 ms: 1.33x faster                                                           |
| genshi_text     | 17.3 ms                                                | 14.2 ms: 1.22x faster                                                           |
| genshi_xml      | 33.8 ms                                                | 30.7 ms: 1.10x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.25x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-darwin-arm64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 95.6 us: 3.38x faster                                                           |
| deltablue                | 4.91 ms                                                | 2.12 ms: 2.32x faster                                                           |
| deepcopy_memo            | 34.7 us                                                | 17.1 us: 2.03x faster                                                           |
| raytrace                 | 301 ms                                                 | 149 ms: 2.02x faster                                                            |
| async_tree_none          | 388 ms                                                 | 196 ms: 1.98x faster                                                            |
| async_tree_memoization   | 474 ms                                                 | 242 ms: 1.95x faster                                                            |
| logging_silent           | 117 ns                                                 | 60.4 ns: 1.94x faster                                                           |
| deepcopy                 | 272 us                                                 | 146 us: 1.86x faster                                                            |
| chaos                    | 65.8 ms                                                | 36.2 ms: 1.82x faster                                                           |
| async_tree_io            | 980 ms                                                 | 547 ms: 1.79x faster                                                            |
| richards_super           | 57.8 ms                                                | 34.6 ms: 1.67x faster                                                           |
| sqlglot_parse            | 1.24 ms                                                | 744 us: 1.67x faster                                                            |
| sqlglot_transpile        | 1.44 ms                                                | 907 us: 1.59x faster                                                            |
| asyncio_tcp              | 659 ms                                                 | 418 ms: 1.58x faster                                                            |
| generators               | 32.3 ms                                                | 20.6 ms: 1.57x faster                                                           |
| nbody                    | 93.0 ms                                                | 59.4 ms: 1.57x faster                                                           |
| go                       | 151 ms                                                 | 97.2 ms: 1.55x faster                                                           |
| richards                 | 48.7 ms                                                | 31.4 ms: 1.55x faster                                                           |
| comprehensions           | 16.9 us                                                | 11.0 us: 1.53x faster                                                           |
| deepcopy_reduce          | 2.33 us                                                | 1.52 us: 1.53x faster                                                           |
| hexiom                   | 6.19 ms                                                | 4.06 ms: 1.53x faster                                                           |
| scimark_lu               | 103 ms                                                 | 67.5 ms: 1.52x faster                                                           |
| pickle_pure_python       | 281 us                                                 | 184 us: 1.52x faster                                                            |
| pylint                   | 277 ms                                                 | 182 ms: 1.52x faster                                                            |
| scimark_monte_carlo      | 65.6 ms                                                | 43.5 ms: 1.51x faster                                                           |
| logging_simple           | 4.45 us                                                | 3.06 us: 1.46x faster                                                           |
| logging_format           | 4.83 us                                                | 3.37 us: 1.43x faster                                                           |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 453 ms: 1.43x faster                                                            |
| float                    | 69.0 ms                                                | 48.4 ms: 1.43x faster                                                           |
| spectral_norm            | 94.8 ms                                                | 66.5 ms: 1.43x faster                                                           |
| crypto_pyaes             | 71.8 ms                                                | 51.1 ms: 1.41x faster                                                           |
| regex_compile            | 95.3 ms                                                | 68.5 ms: 1.39x faster                                                           |
| mako                     | 9.87 ms                                                | 7.16 ms: 1.38x faster                                                           |
| pycparser                | 877 ms                                                 | 639 ms: 1.37x faster                                                            |
| scimark_sor              | 128 ms                                                 | 93.7 ms: 1.37x faster                                                           |
| unpickle_pure_python     | 194 us                                                 | 144 us: 1.36x faster                                                            |
| pprint_safe_repr         | 641 ms                                                 | 475 ms: 1.35x faster                                                            |
| pprint_pformat           | 1.30 sec                                               | 969 ms: 1.35x faster                                                            |
| html5lib                 | 42.4 ms                                                | 31.6 ms: 1.34x faster                                                           |
| django_template          | 26.4 ms                                                | 19.8 ms: 1.33x faster                                                           |
| thrift                   | 572 us                                                 | 430 us: 1.33x faster                                                            |
| pyflate                  | 427 ms                                                 | 322 ms: 1.33x faster                                                            |
| dulwich_log              | 35.3 ms                                                | 26.9 ms: 1.31x faster                                                           |
| sympy_sum                | 92.2 ms                                                | 70.8 ms: 1.30x faster                                                           |
| coroutines               | 20.7 ms                                                | 16.1 ms: 1.29x faster                                                           |
| sympy_integrate          | 13.1 ms                                                | 10.5 ms: 1.26x faster                                                           |
| json_dumps               | 8.11 ms                                                | 6.52 ms: 1.24x faster                                                           |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.30 sec: 1.24x faster                                                          |
| sympy_str                | 165 ms                                                 | 135 ms: 1.23x faster                                                            |
| genshi_text              | 17.3 ms                                                | 14.2 ms: 1.22x faster                                                           |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.80 ms: 1.22x faster                                                           |
| xml_etree_process        | 46.5 ms                                                | 38.3 ms: 1.21x faster                                                           |
| scimark_fft              | 224 ms                                                 | 186 ms: 1.21x faster                                                            |
| nqueens                  | 63.8 ms                                                | 53.1 ms: 1.20x faster                                                           |
| regex_dna                | 174 ms                                                 | 146 ms: 1.19x faster                                                            |
| bench_thread_pool        | 527 us                                                 | 449 us: 1.18x faster                                                            |
| 2to3                     | 192 ms                                                 | 163 ms: 1.17x faster                                                            |
| docutils                 | 1.73 sec                                               | 1.48 sec: 1.17x faster                                                          |
| sympy_expand             | 269 ms                                                 | 231 ms: 1.16x faster                                                            |
| sqlglot_optimize         | 36.8 ms                                                | 31.8 ms: 1.16x faster                                                           |
| fannkuch                 | 303 ms                                                 | 262 ms: 1.15x faster                                                            |
| tomli_loads              | 1.71 sec                                               | 1.50 sec: 1.14x faster                                                          |
| mdp                      | 1.63 sec                                               | 1.44 sec: 1.13x faster                                                          |
| sqlglot_normalize        | 190 ms                                                 | 172 ms: 1.11x faster                                                            |
| genshi_xml               | 33.8 ms                                                | 30.7 ms: 1.10x faster                                                           |
| meteor_contest           | 77.7 ms                                                | 71.8 ms: 1.08x faster                                                           |
| pathlib                  | 24.5 ms                                                | 23.3 ms: 1.05x faster                                                           |
| regex_v8                 | 17.1 ms                                                | 16.6 ms: 1.04x faster                                                           |
| json                     | 3.08 ms                                                | 3.01 ms: 1.03x faster                                                           |
| asyncio_websockets       | 410 ms                                                 | 408 ms: 1.00x faster                                                            |
| pidigits                 | 282 ms                                                 | 282 ms: 1.00x faster                                                            |
| xml_etree_generate       | 53.5 ms                                                | 53.4 ms: 1.00x faster                                                           |
| regex_effbot             | 2.46 ms                                                | 2.50 ms: 1.02x slower                                                           |
| xml_etree_iterparse      | 72.1 ms                                                | 74.3 ms: 1.03x slower                                                           |
| create_gc_cycles         | 860 us                                                 | 886 us: 1.03x slower                                                            |
| gc_traversal             | 2.36 ms                                                | 2.45 ms: 1.04x slower                                                           |
| json_loads               | 16.4 us                                                | 17.3 us: 1.05x slower                                                           |
| coverage                 | 41.5 ms                                                | 44.9 ms: 1.08x slower                                                           |
| async_generators         | 231 ms                                                 | 279 ms: 1.21x slower                                                            |
| bench_mp_pool            | 37.4 ms                                                | 48.6 ms: 1.30x slower                                                           |
| telco                    | 3.49 ms                                                | 4.67 ms: 1.34x slower                                                           |
| python_startup           | 10.9 ms                                                | 16.4 ms: 1.51x slower                                                           |
| python_startup_no_site   | 7.91 ms                                                | 13.4 ms: 1.69x slower                                                           |
| Geometric mean           | (ref)                                                  | 1.29x faster                                                                    |

Benchmark hidden because not significant (2): tornado_http, xml_etree_parse
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20240828-3.14.0a0-bfd4400/bm-20240828-darwin-arm64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: 0.59x