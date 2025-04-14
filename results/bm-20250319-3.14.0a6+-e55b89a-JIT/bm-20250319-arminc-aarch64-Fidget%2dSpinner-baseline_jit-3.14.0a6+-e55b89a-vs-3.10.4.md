# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: baseline_jit
- machine: linux-aarch64
- commit hash: e55b89a
- commit date: 2025-03-19
- overall geometric mean: 1.279x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250319-arminc-aarch64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 307 ms: 1.24x faster                                                       |
| docutils       | 3.53 sec                                                              | 3.10 sec: 1.14x faster                                                     |
| html5lib       | 86.5 ms                                                               | 66.9 ms: 1.29x faster                                                      |
| Geometric mean | (ref)                                                                 | 1.22x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250319-arminc-aarch64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|-------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 902 ms: 2.53x faster                                                       |
| async_tree_none         | 950 ms                                                                | 394 ms: 2.41x faster                                                       |
| async_tree_memoization  | 1.13 sec                                                              | 485 ms: 2.34x faster                                                       |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 668 ms: 1.90x faster                                                       |
| Geometric mean          | (ref)                                                                 | 2.28x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250319-arminc-aarch64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 89.9 ms: 1.50x faster                                                      |
| nbody          | 166 ms                                                                | 127 ms: 1.31x faster                                                       |
| Geometric mean | (ref)                                                                 | 1.25x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250319-arminc-aarch64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 132 ms: 1.34x faster                                                       |
| regex_v8       | 32.2 ms                                                               | 27.5 ms: 1.17x faster                                                      |
| regex_dna      | 257 ms                                                                | 247 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                                 | 1.14x faster                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250319-arminc-aarch64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 3.36 sec                                                              | 2.41 sec: 1.39x faster                                                     |
| pickle_pure_python   | 529 us                                                                | 400 us: 1.32x faster                                                       |
| unpickle_pure_python | 366 us                                                                | 293 us: 1.25x faster                                                       |
| xml_etree_parse      | 212 ms                                                                | 174 ms: 1.22x faster                                                       |
| xml_etree_process    | 99.5 ms                                                               | 82.4 ms: 1.21x faster                                                      |
| json_dumps           | 16.7 ms                                                               | 14.0 ms: 1.20x faster                                                      |
| xml_etree_iterparse  | 156 ms                                                                | 141 ms: 1.10x faster                                                       |
| xml_etree_generate   | 123 ms                                                                | 114 ms: 1.08x faster                                                       |
| json_loads           | 30.9 us                                                               | 34.0 us: 1.10x slower                                                      |
| Geometric mean       | (ref)                                                                 | 1.18x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250319-arminc-aarch64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 16.3 ms: 1.45x slower                                                      |
| python_startup_no_site | 6.89 ms                                                               | 10.2 ms: 1.48x slower                                                      |
| Geometric mean         | (ref)                                                                 | 1.47x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250319-arminc-aarch64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 53.3 ms                                                               | 40.9 ms: 1.30x faster                                                      |
| genshi_text     | 35.2 ms                                                               | 27.6 ms: 1.27x faster                                                      |
| mako            | 18.9 ms                                                               | 15.0 ms: 1.26x faster                                                      |
| genshi_xml      | 69.8 ms                                                               | 61.4 ms: 1.14x faster                                                      |
| Geometric mean  | (ref)                                                                 | 1.24x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250319-arminc-aarch64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|--------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 216 us: 3.06x faster                                                       |
| async_tree_io            | 2.28 sec                                                              | 902 ms: 2.53x faster                                                       |
| async_tree_none          | 950 ms                                                                | 394 ms: 2.41x faster                                                       |
| async_tree_memoization   | 1.13 sec                                                              | 485 ms: 2.34x faster                                                       |
| deltablue                | 8.94 ms                                                               | 4.34 ms: 2.06x faster                                                      |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 668 ms: 1.90x faster                                                       |
| generators               | 68.1 ms                                                               | 36.3 ms: 1.87x faster                                                      |
| richards_super           | 107 ms                                                                | 61.4 ms: 1.75x faster                                                      |
| raytrace                 | 573 ms                                                                | 329 ms: 1.74x faster                                                       |
| richards                 | 91.7 ms                                                               | 53.6 ms: 1.71x faster                                                      |
| go                       | 264 ms                                                                | 156 ms: 1.69x faster                                                       |
| logging_silent           | 222 ns                                                                | 131 ns: 1.69x faster                                                       |
| scimark_sor              | 246 ms                                                                | 152 ms: 1.62x faster                                                       |
| deepcopy_memo            | 61.7 us                                                               | 38.3 us: 1.61x faster                                                      |
| chaos                    | 121 ms                                                                | 75.5 ms: 1.60x faster                                                      |
| pylint                   | 485 ms                                                                | 319 ms: 1.52x faster                                                       |
| scimark_lu               | 227 ms                                                                | 150 ms: 1.52x faster                                                       |
| deepcopy                 | 511 us                                                                | 340 us: 1.50x faster                                                       |
| float                    | 135 ms                                                                | 89.9 ms: 1.50x faster                                                      |
| spectral_norm            | 186 ms                                                                | 131 ms: 1.43x faster                                                       |
| crypto_pyaes             | 134 ms                                                                | 94.3 ms: 1.42x faster                                                      |
| logging_simple           | 9.78 us                                                               | 6.98 us: 1.40x faster                                                      |
| tomli_loads              | 3.36 sec                                                              | 2.41 sec: 1.39x faster                                                     |
| scimark_monte_carlo      | 128 ms                                                                | 91.9 ms: 1.39x faster                                                      |
| logging_format           | 10.6 us                                                               | 7.80 us: 1.36x faster                                                      |
| regex_compile            | 177 ms                                                                | 132 ms: 1.34x faster                                                       |
| dulwich_log              | 73.5 ms                                                               | 55.1 ms: 1.33x faster                                                      |
| pyflate                  | 795 ms                                                                | 597 ms: 1.33x faster                                                       |
| thrift                   | 1.26 ms                                                               | 949 us: 1.33x faster                                                       |
| pickle_pure_python       | 529 us                                                                | 400 us: 1.32x faster                                                       |
| nbody                    | 166 ms                                                                | 127 ms: 1.31x faster                                                       |
| django_template          | 53.3 ms                                                               | 40.9 ms: 1.30x faster                                                      |
| sqlalchemy_declarative   | 197 ms                                                                | 152 ms: 1.30x faster                                                       |
| deepcopy_reduce          | 4.60 us                                                               | 3.55 us: 1.29x faster                                                      |
| html5lib                 | 86.5 ms                                                               | 66.9 ms: 1.29x faster                                                      |
| genshi_text              | 35.2 ms                                                               | 27.6 ms: 1.27x faster                                                      |
| mako                     | 18.9 ms                                                               | 15.0 ms: 1.26x faster                                                      |
| pycparser                | 1.69 sec                                                              | 1.34 sec: 1.26x faster                                                     |
| coroutines               | 37.2 ms                                                               | 29.4 ms: 1.26x faster                                                      |
| sympy_sum                | 184 ms                                                                | 147 ms: 1.25x faster                                                       |
| sqlalchemy_imperative    | 20.5 ms                                                               | 16.4 ms: 1.25x faster                                                      |
| hexiom                   | 10.9 ms                                                               | 8.74 ms: 1.25x faster                                                      |
| unpickle_pure_python     | 366 us                                                                | 293 us: 1.25x faster                                                       |
| 2to3                     | 381 ms                                                                | 307 ms: 1.24x faster                                                       |
| xml_etree_parse          | 212 ms                                                                | 174 ms: 1.22x faster                                                       |
| xml_etree_process        | 99.5 ms                                                               | 82.4 ms: 1.21x faster                                                      |
| sympy_integrate          | 26.5 ms                                                               | 22.1 ms: 1.20x faster                                                      |
| comprehensions           | 33.1 us                                                               | 27.7 us: 1.20x faster                                                      |
| json_dumps               | 16.7 ms                                                               | 14.0 ms: 1.20x faster                                                      |
| scimark_fft              | 500 ms                                                                | 422 ms: 1.19x faster                                                       |
| sympy_str                | 329 ms                                                                | 277 ms: 1.19x faster                                                       |
| pathlib                  | 26.3 ms                                                               | 22.2 ms: 1.18x faster                                                      |
| regex_v8                 | 32.2 ms                                                               | 27.5 ms: 1.17x faster                                                      |
| pprint_pformat           | 2.36 sec                                                              | 2.04 sec: 1.16x faster                                                     |
| bench_thread_pool        | 1.59 ms                                                               | 1.38 ms: 1.15x faster                                                      |
| docutils                 | 3.53 sec                                                              | 3.10 sec: 1.14x faster                                                     |
| genshi_xml               | 69.8 ms                                                               | 61.4 ms: 1.14x faster                                                      |
| pprint_safe_repr         | 1.15 sec                                                              | 1.01 sec: 1.14x faster                                                     |
| sympy_expand             | 543 ms                                                                | 488 ms: 1.11x faster                                                       |
| nqueens                  | 117 ms                                                                | 106 ms: 1.11x faster                                                       |
| xml_etree_iterparse      | 156 ms                                                                | 141 ms: 1.10x faster                                                       |
| mdp                      | 3.70 sec                                                              | 3.35 sec: 1.10x faster                                                     |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 7.00 ms: 1.09x faster                                                      |
| xml_etree_generate       | 123 ms                                                                | 114 ms: 1.08x faster                                                       |
| sqlite_synth             | 4.12 us                                                               | 3.83 us: 1.07x faster                                                      |
| meteor_contest           | 126 ms                                                                | 118 ms: 1.07x faster                                                       |
| regex_dna                | 257 ms                                                                | 247 ms: 1.04x faster                                                       |
| fannkuch                 | 546 ms                                                                | 528 ms: 1.03x faster                                                       |
| asyncio_websockets       | 657 ms                                                                | 668 ms: 1.02x slower                                                       |
| async_generators         | 452 ms                                                                | 470 ms: 1.04x slower                                                       |
| json_loads               | 30.9 us                                                               | 34.0 us: 1.10x slower                                                      |
| coverage                 | 83.6 ms                                                               | 98.3 ms: 1.18x slower                                                      |
| telco                    | 8.49 ms                                                               | 10.4 ms: 1.22x slower                                                      |
| python_startup           | 11.2 ms                                                               | 16.3 ms: 1.45x slower                                                      |
| python_startup_no_site   | 6.89 ms                                                               | 10.2 ms: 1.48x slower                                                      |
| gc_traversal             | 4.15 ms                                                               | 6.61 ms: 1.59x slower                                                      |
| create_gc_cycles         | 2.26 ms                                                               | 3.67 ms: 1.62x slower                                                      |
| bench_mp_pool            | 14.5 ms                                                               | 2.37 sec: 162.97x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.19x faster                                                               |

Benchmark hidden because not significant (3): regex_effbot, pidigits, json
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250319-3.14.0a6+-e55b89a-JIT/bm-20250319-arminc-aarch64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.279x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: 1.32x