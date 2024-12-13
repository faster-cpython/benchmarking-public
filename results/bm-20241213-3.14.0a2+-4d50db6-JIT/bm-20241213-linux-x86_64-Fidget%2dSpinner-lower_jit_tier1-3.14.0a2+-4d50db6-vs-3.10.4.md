# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: lower_jit_tier1
- machine: linux-x86_64
- commit hash: 4d50db6
- commit date: 2024-12-13
- overall geometric mean: 1.426x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241213-linux-x86_64-Fidget%2dSpinner-lower_jit_tier1-3.14.0a2+-4d50db6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 260 ms: 1.34x faster                                                        |
| docutils       | 3.30 sec                                               | 2.73 sec: 1.21x faster                                                      |
| html5lib       | 88.9 ms                                                | 64.2 ms: 1.38x faster                                                       |
| Geometric mean | (ref)                                                  | 1.31x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241213-linux-x86_64-Fidget%2dSpinner-lower_jit_tier1-3.14.0a2+-4d50db6 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 617 ms: 2.87x faster                                                        |
| async_tree_none         | 728 ms                                                 | 267 ms: 2.73x faster                                                        |
| async_tree_memoization  | 870 ms                                                 | 335 ms: 2.60x faster                                                        |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 493 ms: 2.06x faster                                                        |
| Geometric mean          | (ref)                                                  | 2.54x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241213-linux-x86_64-Fidget%2dSpinner-lower_jit_tier1-3.14.0a2+-4d50db6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 83.6 ms: 1.84x faster                                                       |
| float          | 117 ms                                                 | 72.8 ms: 1.61x faster                                                       |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                  | 1.45x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241213-linux-x86_64-Fidget%2dSpinner-lower_jit_tier1-3.14.0a2+-4d50db6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.46x faster                                                        |
| regex_effbot   | 3.63 ms                                                | 3.21 ms: 1.13x faster                                                       |
| regex_v8       | 27.8 ms                                                | 25.2 ms: 1.10x faster                                                       |
| regex_dna      | 227 ms                                                 | 211 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                  | 1.18x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241213-linux-x86_64-Fidget%2dSpinner-lower_jit_tier1-3.14.0a2+-4d50db6 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 194 us: 1.71x faster                                                        |
| tomli_loads          | 3.14 sec                                               | 1.93 sec: 1.63x faster                                                      |
| pickle_pure_python   | 484 us                                                 | 316 us: 1.53x faster                                                        |
| xml_etree_process    | 79.1 ms                                                | 54.6 ms: 1.45x faster                                                       |
| xml_etree_generate   | 99.4 ms                                                | 77.3 ms: 1.29x faster                                                       |
| json_dumps           | 14.2 ms                                                | 11.1 ms: 1.27x faster                                                       |
| xml_etree_parse      | 168 ms                                                 | 137 ms: 1.23x faster                                                        |
| xml_etree_iterparse  | 115 ms                                                 | 94.7 ms: 1.22x faster                                                       |
| json_loads           | 31.2 us                                                | 26.0 us: 1.20x faster                                                       |
| Geometric mean       | (ref)                                                  | 1.38x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241213-linux-x86_64-Fidget%2dSpinner-lower_jit_tier1-3.14.0a2+-4d50db6 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                       |
| python_startup_no_site | 5.93 ms                                                | 7.06 ms: 1.19x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241213-linux-x86_64-Fidget%2dSpinner-lower_jit_tier1-3.14.0a2+-4d50db6 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.95 ms: 1.64x faster                                                       |
| django_template | 48.2 ms                                                | 34.2 ms: 1.41x faster                                                       |
| genshi_text     | 31.8 ms                                                | 23.7 ms: 1.34x faster                                                       |
| genshi_xml      | 66.0 ms                                                | 56.2 ms: 1.18x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.38x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241213-linux-x86_64-Fidget%2dSpinner-lower_jit_tier1-3.14.0a2+-4d50db6 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 168 us: 3.24x faster                                                        |
| async_tree_io            | 1.77 sec                                               | 617 ms: 2.87x faster                                                        |
| async_tree_none          | 728 ms                                                 | 267 ms: 2.73x faster                                                        |
| async_tree_memoization   | 870 ms                                                 | 335 ms: 2.60x faster                                                        |
| deltablue                | 7.91 ms                                                | 3.28 ms: 2.41x faster                                                       |
| generators               | 80.1 ms                                                | 34.2 ms: 2.34x faster                                                       |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 493 ms: 2.06x faster                                                        |
| deepcopy_memo            | 58.5 us                                                | 29.4 us: 1.99x faster                                                       |
| chaos                    | 115 ms                                                 | 59.7 ms: 1.93x faster                                                       |
| go                       | 240 ms                                                 | 125 ms: 1.92x faster                                                        |
| pylint                   | 551 ms                                                 | 293 ms: 1.88x faster                                                        |
| scimark_monte_carlo      | 118 ms                                                 | 62.8 ms: 1.88x faster                                                       |
| scimark_sor              | 220 ms                                                 | 118 ms: 1.86x faster                                                        |
| crypto_pyaes             | 128 ms                                                 | 69.1 ms: 1.85x faster                                                       |
| nbody                    | 154 ms                                                 | 83.6 ms: 1.84x faster                                                       |
| richards_super           | 94.7 ms                                                | 52.3 ms: 1.81x faster                                                       |
| raytrace                 | 507 ms                                                 | 282 ms: 1.79x faster                                                        |
| deepcopy                 | 479 us                                                 | 268 us: 1.79x faster                                                        |
| richards                 | 79.3 ms                                                | 45.6 ms: 1.74x faster                                                       |
| logging_silent           | 190 ns                                                 | 111 ns: 1.71x faster                                                        |
| unpickle_pure_python     | 331 us                                                 | 194 us: 1.71x faster                                                        |
| djangocms                | 38.4 us                                                | 22.6 us: 1.70x faster                                                       |
| comprehensions           | 28.8 us                                                | 17.1 us: 1.68x faster                                                       |
| sqlglot_parse            | 2.17 ms                                                | 1.30 ms: 1.67x faster                                                       |
| mako                     | 16.3 ms                                                | 9.95 ms: 1.64x faster                                                       |
| pyflate                  | 716 ms                                                 | 438 ms: 1.64x faster                                                        |
| tomli_loads              | 3.14 sec                                               | 1.93 sec: 1.63x faster                                                      |
| float                    | 117 ms                                                 | 72.8 ms: 1.61x faster                                                       |
| sqlglot_transpile        | 2.57 ms                                                | 1.62 ms: 1.59x faster                                                       |
| deepcopy_reduce          | 4.17 us                                                | 2.67 us: 1.56x faster                                                       |
| scimark_lu               | 176 ms                                                 | 113 ms: 1.56x faster                                                        |
| pickle_pure_python       | 484 us                                                 | 316 us: 1.53x faster                                                        |
| spectral_norm            | 170 ms                                                 | 113 ms: 1.50x faster                                                        |
| hexiom                   | 10.4 ms                                                | 6.93 ms: 1.50x faster                                                       |
| coroutines               | 35.1 ms                                                | 23.9 ms: 1.47x faster                                                       |
| regex_compile            | 188 ms                                                 | 129 ms: 1.46x faster                                                        |
| xml_etree_process        | 79.1 ms                                                | 54.6 ms: 1.45x faster                                                       |
| logging_simple           | 8.30 us                                                | 5.78 us: 1.44x faster                                                       |
| logging_format           | 9.09 us                                                | 6.35 us: 1.43x faster                                                       |
| django_template          | 48.2 ms                                                | 34.2 ms: 1.41x faster                                                       |
| scimark_fft              | 466 ms                                                 | 333 ms: 1.40x faster                                                        |
| thrift                   | 1.07 ms                                                | 770 us: 1.39x faster                                                        |
| fannkuch                 | 532 ms                                                 | 382 ms: 1.39x faster                                                        |
| html5lib                 | 88.9 ms                                                | 64.2 ms: 1.38x faster                                                       |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.9 ms: 1.38x faster                                                       |
| pprint_pformat           | 2.10 sec                                               | 1.54 sec: 1.36x faster                                                      |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.76 ms: 1.36x faster                                                       |
| pprint_safe_repr         | 1.02 sec                                               | 755 ms: 1.35x faster                                                        |
| genshi_text              | 31.8 ms                                                | 23.7 ms: 1.34x faster                                                       |
| 2to3                     | 348 ms                                                 | 260 ms: 1.34x faster                                                        |
| sqlalchemy_declarative   | 172 ms                                                 | 129 ms: 1.33x faster                                                        |
| sqlglot_normalize        | 143 ms                                                 | 109 ms: 1.31x faster                                                        |
| pycparser                | 1.58 sec                                               | 1.20 sec: 1.31x faster                                                      |
| xml_etree_generate       | 99.4 ms                                                | 77.3 ms: 1.29x faster                                                       |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.27x faster                                                       |
| json_dumps               | 14.2 ms                                                | 11.1 ms: 1.27x faster                                                       |
| sqlglot_optimize         | 69.2 ms                                                | 55.0 ms: 1.26x faster                                                       |
| sympy_sum                | 196 ms                                                 | 157 ms: 1.25x faster                                                        |
| sympy_integrate          | 25.8 ms                                                | 20.8 ms: 1.24x faster                                                       |
| xml_etree_parse          | 168 ms                                                 | 137 ms: 1.23x faster                                                        |
| dulwich_log              | 84.3 ms                                                | 68.9 ms: 1.22x faster                                                       |
| xml_etree_iterparse      | 115 ms                                                 | 94.7 ms: 1.22x faster                                                       |
| nqueens                  | 106 ms                                                 | 87.3 ms: 1.21x faster                                                       |
| docutils                 | 3.30 sec                                               | 2.73 sec: 1.21x faster                                                      |
| sympy_str                | 346 ms                                                 | 287 ms: 1.21x faster                                                        |
| json_loads               | 31.2 us                                                | 26.0 us: 1.20x faster                                                       |
| json                     | 5.69 ms                                                | 4.76 ms: 1.20x faster                                                       |
| genshi_xml               | 66.0 ms                                                | 56.2 ms: 1.18x faster                                                       |
| sympy_expand             | 566 ms                                                 | 484 ms: 1.17x faster                                                        |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                       |
| regex_effbot             | 3.63 ms                                                | 3.21 ms: 1.13x faster                                                       |
| bench_thread_pool        | 986 us                                                 | 884 us: 1.12x faster                                                        |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                        |
| regex_v8                 | 27.8 ms                                                | 25.2 ms: 1.10x faster                                                       |
| sqlite_synth             | 3.02 us                                                | 2.77 us: 1.09x faster                                                       |
| regex_dna                | 227 ms                                                 | 211 ms: 1.07x faster                                                        |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                        |
| mdp                      | 2.85 sec                                               | 2.81 sec: 1.01x faster                                                      |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                        |
| async_generators         | 444 ms                                                 | 446 ms: 1.00x slower                                                        |
| telco                    | 7.27 ms                                                | 7.46 ms: 1.03x slower                                                       |
| coverage                 | 79.4 ms                                                | 82.9 ms: 1.04x slower                                                       |
| mypy2                    | 894 ms                                                 | 965 ms: 1.08x slower                                                        |
| python_startup_no_site   | 5.93 ms                                                | 7.06 ms: 1.19x slower                                                       |
| gc_traversal             | 3.62 ms                                                | 4.77 ms: 1.32x slower                                                       |
| create_gc_cycles         | 1.62 ms                                                | 2.44 ms: 1.51x slower                                                       |
| bench_mp_pool            | 24.0 ms                                                | 81.3 ms: 3.38x slower                                                       |
| Geometric mean           | (ref)                                                  | 1.40x faster                                                                |
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241213-3.14.0a2+-4d50db6-JIT/bm-20241213-linux-x86_64-Fidget%2dSpinner-lower_jit_tier1-3.14.0a2+-4d50db6.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.426x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.29x