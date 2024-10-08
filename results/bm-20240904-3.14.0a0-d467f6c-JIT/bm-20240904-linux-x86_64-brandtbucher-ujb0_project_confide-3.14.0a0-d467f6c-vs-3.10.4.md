# Results vs. 3.10.4

- fork: brandtbucher
- ref: ujb0_project_confide
- machine: linux-x86_64
- commit hash: d467f6c
- commit date: 2024-09-04
- overall geometric mean: 1.37x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: 1.36x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 294 ms: 1.18x faster                                                        |
| docutils       | 3.30 sec                                               | 3.52 sec: 1.07x slower                                                      |
| html5lib       | 88.9 ms                                                | 74.3 ms: 1.20x faster                                                       |
| tornado_http   | 136 ms                                                 | 118 ms: 1.16x faster                                                        |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 341 ms: 2.14x faster                                                        |
| async_tree_memoization  | 870 ms                                                 | 427 ms: 2.04x faster                                                        |
| async_tree_io           | 1.77 sec                                               | 961 ms: 1.84x faster                                                        |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 572 ms: 1.78x faster                                                        |
| Geometric mean          | (ref)                                                  | 1.94x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 79.9 ms: 1.92x faster                                                       |
| float          | 117 ms                                                 | 68.7 ms: 1.70x faster                                                       |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                  | 1.50x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 152 ms: 1.24x faster                                                        |
| regex_v8       | 27.8 ms                                                | 26.1 ms: 1.06x faster                                                       |
| regex_dna      | 227 ms                                                 | 218 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 193 us: 1.72x faster                                                        |
| pickle_pure_python   | 484 us                                                 | 310 us: 1.56x faster                                                        |
| json_dumps           | 14.2 ms                                                | 9.72 ms: 1.46x faster                                                       |
| tomli_loads          | 3.14 sec                                               | 2.15 sec: 1.46x faster                                                      |
| xml_etree_process    | 79.1 ms                                                | 54.7 ms: 1.45x faster                                                       |
| xml_etree_generate   | 99.4 ms                                                | 80.1 ms: 1.24x faster                                                       |
| xml_etree_iterparse  | 115 ms                                                 | 98.6 ms: 1.17x faster                                                       |
| xml_etree_parse      | 168 ms                                                 | 145 ms: 1.16x faster                                                        |
| json_loads           | 31.2 us                                                | 29.6 us: 1.05x faster                                                       |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.37x faster                                                       |
| python_startup_no_site | 5.93 ms                                                | 7.16 ms: 1.21x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.58 ms: 1.70x faster                                                       |
| genshi_text     | 31.8 ms                                                | 22.7 ms: 1.40x faster                                                       |
| django_template | 48.2 ms                                                | 40.5 ms: 1.19x faster                                                       |
| genshi_xml      | 66.0 ms                                                | 59.2 ms: 1.12x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.33x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 165 us: 3.29x faster                                                        |
| generators               | 80.1 ms                                                | 34.1 ms: 2.35x faster                                                       |
| deepcopy_memo            | 58.5 us                                                | 26.3 us: 2.23x faster                                                       |
| deltablue                | 7.91 ms                                                | 3.56 ms: 2.22x faster                                                       |
| async_tree_none          | 728 ms                                                 | 341 ms: 2.14x faster                                                        |
| scimark_monte_carlo      | 118 ms                                                 | 57.9 ms: 2.04x faster                                                       |
| async_tree_memoization   | 870 ms                                                 | 427 ms: 2.04x faster                                                        |
| richards_super           | 94.7 ms                                                | 47.1 ms: 2.01x faster                                                       |
| crypto_pyaes             | 128 ms                                                 | 66.0 ms: 1.94x faster                                                       |
| logging_silent           | 190 ns                                                 | 98.3 ns: 1.93x faster                                                       |
| chaos                    | 115 ms                                                 | 59.9 ms: 1.93x faster                                                       |
| nbody                    | 154 ms                                                 | 79.9 ms: 1.92x faster                                                       |
| richards                 | 79.3 ms                                                | 41.4 ms: 1.91x faster                                                       |
| async_tree_io            | 1.77 sec                                               | 961 ms: 1.84x faster                                                        |
| scimark_sor              | 220 ms                                                 | 120 ms: 1.83x faster                                                        |
| deepcopy                 | 479 us                                                 | 263 us: 1.82x faster                                                        |
| raytrace                 | 507 ms                                                 | 284 ms: 1.78x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 572 ms: 1.78x faster                                                        |
| asyncio_tcp              | 922 ms                                                 | 530 ms: 1.74x faster                                                        |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.73x faster                                                       |
| unpickle_pure_python     | 331 us                                                 | 193 us: 1.72x faster                                                        |
| float                    | 117 ms                                                 | 68.7 ms: 1.70x faster                                                       |
| mako                     | 16.3 ms                                                | 9.58 ms: 1.70x faster                                                       |
| spectral_norm            | 170 ms                                                 | 101 ms: 1.68x faster                                                        |
| scimark_lu               | 176 ms                                                 | 108 ms: 1.63x faster                                                        |
| pickle_pure_python       | 484 us                                                 | 310 us: 1.56x faster                                                        |
| deepcopy_reduce          | 4.17 us                                                | 2.69 us: 1.55x faster                                                       |
| scimark_fft              | 466 ms                                                 | 307 ms: 1.52x faster                                                        |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.34 ms: 1.49x faster                                                       |
| pyflate                  | 716 ms                                                 | 484 ms: 1.48x faster                                                        |
| coroutines               | 35.1 ms                                                | 23.8 ms: 1.47x faster                                                       |
| pprint_safe_repr         | 1.02 sec                                               | 695 ms: 1.47x faster                                                        |
| json_dumps               | 14.2 ms                                                | 9.72 ms: 1.46x faster                                                       |
| tomli_loads              | 3.14 sec                                               | 2.15 sec: 1.46x faster                                                      |
| xml_etree_process        | 79.1 ms                                                | 54.7 ms: 1.45x faster                                                       |
| pprint_pformat           | 2.10 sec                                               | 1.46 sec: 1.44x faster                                                      |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.83 sec: 1.40x faster                                                      |
| hexiom                   | 10.4 ms                                                | 7.40 ms: 1.40x faster                                                       |
| fannkuch                 | 532 ms                                                 | 380 ms: 1.40x faster                                                        |
| genshi_text              | 31.8 ms                                                | 22.7 ms: 1.40x faster                                                       |
| logging_simple           | 8.30 us                                                | 6.00 us: 1.38x faster                                                       |
| logging_format           | 9.09 us                                                | 6.59 us: 1.38x faster                                                       |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.37x faster                                                       |
| go                       | 240 ms                                                 | 181 ms: 1.33x faster                                                        |
| thrift                   | 1.07 ms                                                | 810 us: 1.32x faster                                                        |
| pathlib                  | 20.5 ms                                                | 15.8 ms: 1.29x faster                                                       |
| nqueens                  | 106 ms                                                 | 84.5 ms: 1.25x faster                                                       |
| xml_etree_generate       | 99.4 ms                                                | 80.1 ms: 1.24x faster                                                       |
| sqlglot_parse            | 2.17 ms                                                | 1.75 ms: 1.24x faster                                                       |
| regex_compile            | 188 ms                                                 | 152 ms: 1.24x faster                                                        |
| html5lib                 | 88.9 ms                                                | 74.3 ms: 1.20x faster                                                       |
| django_template          | 48.2 ms                                                | 40.5 ms: 1.19x faster                                                       |
| 2to3                     | 348 ms                                                 | 294 ms: 1.18x faster                                                        |
| sqlglot_transpile        | 2.57 ms                                                | 2.19 ms: 1.18x faster                                                       |
| xml_etree_iterparse      | 115 ms                                                 | 98.6 ms: 1.17x faster                                                       |
| pycparser                | 1.58 sec                                               | 1.35 sec: 1.17x faster                                                      |
| tornado_http             | 136 ms                                                 | 118 ms: 1.16x faster                                                        |
| xml_etree_parse          | 168 ms                                                 | 145 ms: 1.16x faster                                                        |
| sqlglot_normalize        | 143 ms                                                 | 125 ms: 1.14x faster                                                        |
| pylint                   | 551 ms                                                 | 483 ms: 1.14x faster                                                        |
| genshi_xml               | 66.0 ms                                                | 59.2 ms: 1.12x faster                                                       |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                        |
| bench_thread_pool        | 986 us                                                 | 893 us: 1.10x faster                                                        |
| mdp                      | 2.85 sec                                               | 2.59 sec: 1.10x faster                                                      |
| json                     | 5.69 ms                                                | 5.31 ms: 1.07x faster                                                       |
| regex_v8                 | 27.8 ms                                                | 26.1 ms: 1.06x faster                                                       |
| json_loads               | 31.2 us                                                | 29.6 us: 1.05x faster                                                       |
| regex_dna                | 227 ms                                                 | 218 ms: 1.04x faster                                                        |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                        |
| sqlglot_optimize         | 69.2 ms                                                | 67.6 ms: 1.02x faster                                                       |
| sympy_expand             | 566 ms                                                 | 559 ms: 1.01x faster                                                        |
| async_generators         | 444 ms                                                 | 457 ms: 1.03x slower                                                        |
| bench_mp_pool            | 24.0 ms                                                | 24.9 ms: 1.04x slower                                                       |
| gc_traversal             | 3.62 ms                                                | 3.82 ms: 1.05x slower                                                       |
| sympy_integrate          | 25.8 ms                                                | 27.5 ms: 1.07x slower                                                       |
| docutils                 | 3.30 sec                                               | 3.52 sec: 1.07x slower                                                      |
| telco                    | 7.27 ms                                                | 7.82 ms: 1.08x slower                                                       |
| sympy_sum                | 196 ms                                                 | 217 ms: 1.10x slower                                                        |
| coverage                 | 79.4 ms                                                | 87.9 ms: 1.11x slower                                                       |
| create_gc_cycles         | 1.62 ms                                                | 1.81 ms: 1.12x slower                                                       |
| python_startup_no_site   | 5.93 ms                                                | 7.16 ms: 1.21x slower                                                       |
| Geometric mean           | (ref)                                                  | 1.37x faster                                                                |

Benchmark hidden because not significant (3): sympy_str, asyncio_websockets, regex_effbot
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240904-3.14.0a0-d467f6c-JIT/bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: 1.36x