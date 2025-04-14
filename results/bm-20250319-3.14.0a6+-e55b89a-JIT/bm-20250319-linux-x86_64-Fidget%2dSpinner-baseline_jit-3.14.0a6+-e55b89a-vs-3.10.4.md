# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: baseline_jit
- machine: linux-x86_64
- commit hash: e55b89a
- commit date: 2025-03-19
- overall geometric mean: 1.416x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250319-linux-x86_64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 260 ms: 1.34x faster                                                     |
| docutils       | 3.30 sec                                               | 2.66 sec: 1.24x faster                                                   |
| html5lib       | 88.9 ms                                                | 63.4 ms: 1.40x faster                                                    |
| Geometric mean | (ref)                                                  | 1.33x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250319-linux-x86_64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 617 ms: 2.86x faster                                                     |
| async_tree_none         | 728 ms                                                 | 261 ms: 2.79x faster                                                     |
| async_tree_memoization  | 870 ms                                                 | 319 ms: 2.73x faster                                                     |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 498 ms: 2.04x faster                                                     |
| Geometric mean          | (ref)                                                  | 2.58x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250319-linux-x86_64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 91.1 ms: 1.68x faster                                                    |
| float          | 117 ms                                                 | 72.2 ms: 1.62x faster                                                    |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                  | 1.41x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250319-linux-x86_64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.47x faster                                                     |
| regex_v8       | 27.8 ms                                                | 23.9 ms: 1.16x faster                                                    |
| regex_effbot   | 3.63 ms                                                | 3.21 ms: 1.13x faster                                                    |
| regex_dna      | 227 ms                                                 | 216 ms: 1.05x faster                                                     |
| Geometric mean | (ref)                                                  | 1.19x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250319-linux-x86_64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.83 sec: 1.72x faster                                                   |
| pickle_pure_python   | 484 us                                                 | 320 us: 1.51x faster                                                     |
| unpickle_pure_python | 331 us                                                 | 235 us: 1.41x faster                                                     |
| xml_etree_process    | 79.1 ms                                                | 60.4 ms: 1.31x faster                                                    |
| json_dumps           | 14.2 ms                                                | 11.4 ms: 1.24x faster                                                    |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                                     |
| xml_etree_iterparse  | 115 ms                                                 | 97.4 ms: 1.19x faster                                                    |
| xml_etree_generate   | 99.4 ms                                                | 85.4 ms: 1.16x faster                                                    |
| json_loads           | 31.2 us                                                | 29.9 us: 1.04x faster                                                    |
| Geometric mean       | (ref)                                                  | 1.29x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250319-linux-x86_64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.11x faster                                                    |
| python_startup_no_site | 5.93 ms                                                | 8.18 ms: 1.38x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250319-linux-x86_64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.9 ms: 1.51x faster                                                    |
| genshi_text     | 31.8 ms                                                | 21.5 ms: 1.48x faster                                                    |
| mako            | 16.3 ms                                                | 11.8 ms: 1.39x faster                                                    |
| genshi_xml      | 66.0 ms                                                | 49.3 ms: 1.34x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250319-linux-x86_64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 172 us: 3.16x faster                                                     |
| async_tree_io            | 1.77 sec                                               | 617 ms: 2.86x faster                                                     |
| generators               | 80.1 ms                                                | 28.6 ms: 2.80x faster                                                    |
| async_tree_none          | 728 ms                                                 | 261 ms: 2.79x faster                                                     |
| async_tree_memoization   | 870 ms                                                 | 319 ms: 2.73x faster                                                     |
| deltablue                | 7.91 ms                                                | 3.36 ms: 2.35x faster                                                    |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 498 ms: 2.04x faster                                                     |
| deepcopy_memo            | 58.5 us                                                | 29.4 us: 1.99x faster                                                    |
| pylint                   | 551 ms                                                 | 279 ms: 1.98x faster                                                     |
| logging_silent           | 190 ns                                                 | 97.0 ns: 1.96x faster                                                    |
| go                       | 240 ms                                                 | 125 ms: 1.93x faster                                                     |
| chaos                    | 115 ms                                                 | 60.5 ms: 1.91x faster                                                    |
| raytrace                 | 507 ms                                                 | 268 ms: 1.89x faster                                                     |
| deepcopy                 | 479 us                                                 | 256 us: 1.87x faster                                                     |
| richards_super           | 94.7 ms                                                | 50.5 ms: 1.87x faster                                                    |
| scimark_sor              | 220 ms                                                 | 118 ms: 1.86x faster                                                     |
| richards                 | 79.3 ms                                                | 44.1 ms: 1.80x faster                                                    |
| tomli_loads              | 3.14 sec                                               | 1.83 sec: 1.72x faster                                                   |
| scimark_monte_carlo      | 118 ms                                                 | 69.4 ms: 1.70x faster                                                    |
| nbody                    | 154 ms                                                 | 91.1 ms: 1.68x faster                                                    |
| spectral_norm            | 170 ms                                                 | 104 ms: 1.63x faster                                                     |
| float                    | 117 ms                                                 | 72.2 ms: 1.62x faster                                                    |
| crypto_pyaes             | 128 ms                                                 | 79.7 ms: 1.60x faster                                                    |
| deepcopy_reduce          | 4.17 us                                                | 2.70 us: 1.54x faster                                                    |
| pickle_pure_python       | 484 us                                                 | 320 us: 1.51x faster                                                     |
| django_template          | 48.2 ms                                                | 31.9 ms: 1.51x faster                                                    |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.51x faster                                                     |
| logging_simple           | 8.30 us                                                | 5.55 us: 1.50x faster                                                    |
| logging_format           | 9.09 us                                                | 6.10 us: 1.49x faster                                                    |
| scimark_fft              | 466 ms                                                 | 313 ms: 1.49x faster                                                     |
| genshi_text              | 31.8 ms                                                | 21.5 ms: 1.48x faster                                                    |
| regex_compile            | 188 ms                                                 | 128 ms: 1.47x faster                                                     |
| pyflate                  | 716 ms                                                 | 487 ms: 1.47x faster                                                     |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.50 ms: 1.44x faster                                                    |
| coroutines               | 35.1 ms                                                | 24.4 ms: 1.44x faster                                                    |
| dulwich_log              | 84.3 ms                                                | 59.8 ms: 1.41x faster                                                    |
| unpickle_pure_python     | 331 us                                                 | 235 us: 1.41x faster                                                     |
| hexiom                   | 10.4 ms                                                | 7.41 ms: 1.40x faster                                                    |
| html5lib                 | 88.9 ms                                                | 63.4 ms: 1.40x faster                                                    |
| thrift                   | 1.07 ms                                                | 771 us: 1.39x faster                                                     |
| mako                     | 16.3 ms                                                | 11.8 ms: 1.39x faster                                                    |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.9 ms: 1.38x faster                                                    |
| pprint_pformat           | 2.10 sec                                               | 1.53 sec: 1.38x faster                                                   |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                                   |
| 2to3                     | 348 ms                                                 | 260 ms: 1.34x faster                                                     |
| pprint_safe_repr         | 1.02 sec                                               | 759 ms: 1.34x faster                                                     |
| comprehensions           | 28.8 us                                                | 21.5 us: 1.34x faster                                                    |
| genshi_xml               | 66.0 ms                                                | 49.3 ms: 1.34x faster                                                    |
| xml_etree_process        | 79.1 ms                                                | 60.4 ms: 1.31x faster                                                    |
| sympy_sum                | 196 ms                                                 | 150 ms: 1.31x faster                                                     |
| sqlalchemy_declarative   | 172 ms                                                 | 133 ms: 1.30x faster                                                     |
| sympy_integrate          | 25.8 ms                                                | 20.2 ms: 1.28x faster                                                    |
| sympy_str                | 346 ms                                                 | 274 ms: 1.26x faster                                                     |
| json_dumps               | 14.2 ms                                                | 11.4 ms: 1.24x faster                                                    |
| nqueens                  | 106 ms                                                 | 85.4 ms: 1.24x faster                                                    |
| docutils                 | 3.30 sec                                               | 2.66 sec: 1.24x faster                                                   |
| pathlib                  | 20.5 ms                                                | 16.8 ms: 1.21x faster                                                    |
| fannkuch                 | 532 ms                                                 | 438 ms: 1.21x faster                                                     |
| sympy_expand             | 566 ms                                                 | 471 ms: 1.20x faster                                                     |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                                     |
| xml_etree_iterparse      | 115 ms                                                 | 97.4 ms: 1.19x faster                                                    |
| xml_etree_generate       | 99.4 ms                                                | 85.4 ms: 1.16x faster                                                    |
| regex_v8                 | 27.8 ms                                                | 23.9 ms: 1.16x faster                                                    |
| mdp                      | 2.85 sec                                               | 2.48 sec: 1.15x faster                                                   |
| regex_effbot             | 3.63 ms                                                | 3.21 ms: 1.13x faster                                                    |
| bench_thread_pool        | 986 us                                                 | 880 us: 1.12x faster                                                     |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.11x faster                                                    |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                     |
| sqlite_synth             | 3.02 us                                                | 2.78 us: 1.09x faster                                                    |
| async_generators         | 444 ms                                                 | 411 ms: 1.08x faster                                                     |
| json                     | 5.69 ms                                                | 5.34 ms: 1.07x faster                                                    |
| regex_dna                | 227 ms                                                 | 216 ms: 1.05x faster                                                     |
| json_loads               | 31.2 us                                                | 29.9 us: 1.04x faster                                                    |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                                     |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                     |
| telco                    | 7.27 ms                                                | 8.16 ms: 1.12x slower                                                    |
| coverage                 | 79.4 ms                                                | 91.5 ms: 1.15x slower                                                    |
| gc_traversal             | 3.62 ms                                                | 4.98 ms: 1.38x slower                                                    |
| python_startup_no_site   | 5.93 ms                                                | 8.18 ms: 1.38x slower                                                    |
| create_gc_cycles         | 1.62 ms                                                | 2.47 ms: 1.53x slower                                                    |
| bench_mp_pool            | 24.0 ms                                                | 82.9 ms: 3.45x slower                                                    |
| Geometric mean           | (ref)                                                  | 1.39x faster                                                             |
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250319-3.14.0a6+-e55b89a-JIT/bm-20250319-linux-x86_64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.416x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.29x

# Memory
- memory change: 1.28x