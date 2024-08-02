# Results vs. 3.10.4

- fork: brandtbucher
- ref: invalidate_side_exit
- machine: linux-x86_64
- commit hash: eb895df
- commit date: 2024-07-16
- overall geometric mean: 1.42x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.18x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240716-linux-x86_64-brandtbucher-invalidate_side_exit-3.14.0a0-eb895df |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 271 ms: 1.29x faster                                                        |
| docutils       | 3.30 sec                                               | 2.86 sec: 1.15x faster                                                      |
| html5lib       | 88.9 ms                                                | 65.5 ms: 1.36x faster                                                       |
| tornado_http   | 136 ms                                                 | 93.0 ms: 1.47x faster                                                       |
| Geometric mean | (ref)                                                  | 1.31x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240716-linux-x86_64-brandtbucher-invalidate_side_exit-3.14.0a0-eb895df |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 328 ms: 2.22x faster                                                        |
| async_tree_memoization  | 870 ms                                                 | 412 ms: 2.11x faster                                                        |
| async_tree_io           | 1.77 sec                                               | 886 ms: 2.00x faster                                                        |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 570 ms: 1.78x faster                                                        |
| Geometric mean          | (ref)                                                  | 2.02x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240716-linux-x86_64-brandtbucher-invalidate_side_exit-3.14.0a0-eb895df |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.2 ms: 1.92x faster                                                       |
| float          | 117 ms                                                 | 70.0 ms: 1.67x faster                                                       |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                  | 1.49x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240716-linux-x86_64-brandtbucher-invalidate_side_exit-3.14.0a0-eb895df |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 135 ms: 1.40x faster                                                        |
| regex_v8       | 27.8 ms                                                | 24.9 ms: 1.12x faster                                                       |
| regex_dna      | 227 ms                                                 | 229 ms: 1.01x slower                                                        |
| regex_effbot   | 3.63 ms                                                | 3.71 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240716-linux-x86_64-brandtbucher-invalidate_side_exit-3.14.0a0-eb895df |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 297 us: 1.63x faster                                                        |
| tomli_loads          | 3.14 sec                                               | 1.95 sec: 1.61x faster                                                      |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                                        |
| xml_etree_process    | 79.1 ms                                                | 57.3 ms: 1.38x faster                                                       |
| json_dumps           | 14.2 ms                                                | 10.6 ms: 1.34x faster                                                       |
| xml_etree_generate   | 99.4 ms                                                | 81.2 ms: 1.22x faster                                                       |
| xml_etree_iterparse  | 115 ms                                                 | 99.0 ms: 1.17x faster                                                       |
| json_loads           | 31.2 us                                                | 27.3 us: 1.14x faster                                                       |
| xml_etree_parse      | 168 ms                                                 | 148 ms: 1.14x faster                                                        |
| Geometric mean       | (ref)                                                  | 1.34x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240716-linux-x86_64-brandtbucher-invalidate_side_exit-3.14.0a0-eb895df |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                       |
| python_startup_no_site | 5.93 ms                                                | 7.18 ms: 1.21x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240716-linux-x86_64-brandtbucher-invalidate_side_exit-3.14.0a0-eb895df |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.71 ms: 1.68x faster                                                       |
| django_template | 48.2 ms                                                | 35.9 ms: 1.34x faster                                                       |
| genshi_text     | 31.8 ms                                                | 25.2 ms: 1.26x faster                                                       |
| genshi_xml      | 66.0 ms                                                | 56.7 ms: 1.17x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240716-linux-x86_64-brandtbucher-invalidate_side_exit-3.14.0a0-eb895df |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 170 us: 3.21x faster                                                        |
| generators               | 80.1 ms                                                | 29.5 ms: 2.72x faster                                                       |
| deltablue                | 7.91 ms                                                | 3.48 ms: 2.27x faster                                                       |
| async_tree_none          | 728 ms                                                 | 328 ms: 2.22x faster                                                        |
| async_tree_memoization   | 870 ms                                                 | 412 ms: 2.11x faster                                                        |
| richards_super           | 94.7 ms                                                | 46.5 ms: 2.04x faster                                                       |
| deepcopy_memo            | 58.5 us                                                | 28.8 us: 2.03x faster                                                       |
| async_tree_io            | 1.77 sec                                               | 886 ms: 2.00x faster                                                        |
| chaos                    | 115 ms                                                 | 58.3 ms: 1.98x faster                                                       |
| richards                 | 79.3 ms                                                | 40.6 ms: 1.95x faster                                                       |
| scimark_monte_carlo      | 118 ms                                                 | 60.9 ms: 1.94x faster                                                       |
| nbody                    | 154 ms                                                 | 80.2 ms: 1.92x faster                                                       |
| crypto_pyaes             | 128 ms                                                 | 67.4 ms: 1.90x faster                                                       |
| raytrace                 | 507 ms                                                 | 270 ms: 1.88x faster                                                        |
| asyncio_tcp              | 922 ms                                                 | 504 ms: 1.83x faster                                                        |
| logging_silent           | 190 ns                                                 | 106 ns: 1.79x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 570 ms: 1.78x faster                                                        |
| deepcopy                 | 479 us                                                 | 272 us: 1.76x faster                                                        |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                                       |
| sqlglot_parse            | 2.17 ms                                                | 1.27 ms: 1.71x faster                                                       |
| scimark_sor              | 220 ms                                                 | 129 ms: 1.70x faster                                                        |
| mako                     | 16.3 ms                                                | 9.71 ms: 1.68x faster                                                       |
| float                    | 117 ms                                                 | 70.0 ms: 1.67x faster                                                       |
| spectral_norm            | 170 ms                                                 | 102 ms: 1.67x faster                                                        |
| go                       | 240 ms                                                 | 144 ms: 1.67x faster                                                        |
| pyflate                  | 716 ms                                                 | 432 ms: 1.66x faster                                                        |
| pylint                   | 551 ms                                                 | 334 ms: 1.65x faster                                                        |
| pickle_pure_python       | 484 us                                                 | 297 us: 1.63x faster                                                        |
| sqlglot_transpile        | 2.57 ms                                                | 1.59 ms: 1.62x faster                                                       |
| tomli_loads              | 3.14 sec                                               | 1.95 sec: 1.61x faster                                                      |
| hexiom                   | 10.4 ms                                                | 6.54 ms: 1.59x faster                                                       |
| coroutines               | 35.1 ms                                                | 22.3 ms: 1.57x faster                                                       |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                                        |
| deepcopy_reduce          | 4.17 us                                                | 2.79 us: 1.49x faster                                                       |
| scimark_fft              | 466 ms                                                 | 314 ms: 1.49x faster                                                        |
| logging_simple           | 8.30 us                                                | 5.62 us: 1.48x faster                                                       |
| logging_format           | 9.09 us                                                | 6.17 us: 1.47x faster                                                       |
| tornado_http             | 136 ms                                                 | 93.0 ms: 1.47x faster                                                       |
| fannkuch                 | 532 ms                                                 | 363 ms: 1.46x faster                                                        |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.44 ms: 1.46x faster                                                       |
| pprint_pformat           | 2.10 sec                                               | 1.46 sec: 1.44x faster                                                      |
| scimark_lu               | 176 ms                                                 | 123 ms: 1.43x faster                                                        |
| pycparser                | 1.58 sec                                               | 1.10 sec: 1.43x faster                                                      |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                                      |
| pprint_safe_repr         | 1.02 sec                                               | 719 ms: 1.42x faster                                                        |
| regex_compile            | 188 ms                                                 | 135 ms: 1.40x faster                                                        |
| xml_etree_process        | 79.1 ms                                                | 57.3 ms: 1.38x faster                                                       |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                       |
| html5lib                 | 88.9 ms                                                | 65.5 ms: 1.36x faster                                                       |
| django_template          | 48.2 ms                                                | 35.9 ms: 1.34x faster                                                       |
| thrift                   | 1.07 ms                                                | 798 us: 1.34x faster                                                        |
| json_dumps               | 14.2 ms                                                | 10.6 ms: 1.34x faster                                                       |
| 2to3                     | 348 ms                                                 | 271 ms: 1.29x faster                                                        |
| sqlglot_normalize        | 143 ms                                                 | 112 ms: 1.28x faster                                                        |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                                       |
| genshi_text              | 31.8 ms                                                | 25.2 ms: 1.26x faster                                                       |
| sqlglot_optimize         | 69.2 ms                                                | 55.5 ms: 1.25x faster                                                       |
| dulwich_log              | 84.3 ms                                                | 67.6 ms: 1.25x faster                                                       |
| nqueens                  | 106 ms                                                 | 85.1 ms: 1.24x faster                                                       |
| xml_etree_generate       | 99.4 ms                                                | 81.2 ms: 1.22x faster                                                       |
| dask                     | 441 ms                                                 | 362 ms: 1.22x faster                                                        |
| sympy_sum                | 196 ms                                                 | 165 ms: 1.19x faster                                                        |
| sympy_integrate          | 25.8 ms                                                | 21.7 ms: 1.19x faster                                                       |
| sympy_str                | 346 ms                                                 | 291 ms: 1.19x faster                                                        |
| bench_thread_pool        | 986 us                                                 | 833 us: 1.18x faster                                                        |
| xml_etree_iterparse      | 115 ms                                                 | 99.0 ms: 1.17x faster                                                       |
| genshi_xml               | 66.0 ms                                                | 56.7 ms: 1.17x faster                                                       |
| docutils                 | 3.30 sec                                               | 2.86 sec: 1.15x faster                                                      |
| sympy_expand             | 566 ms                                                 | 494 ms: 1.15x faster                                                        |
| json_loads               | 31.2 us                                                | 27.3 us: 1.14x faster                                                       |
| xml_etree_parse          | 168 ms                                                 | 148 ms: 1.14x faster                                                        |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                        |
| regex_v8                 | 27.8 ms                                                | 24.9 ms: 1.12x faster                                                       |
| json                     | 5.69 ms                                                | 5.19 ms: 1.10x faster                                                       |
| mdp                      | 2.85 sec                                               | 2.68 sec: 1.06x faster                                                      |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                        |
| regex_dna                | 227 ms                                                 | 229 ms: 1.01x slower                                                        |
| regex_effbot             | 3.63 ms                                                | 3.71 ms: 1.02x slower                                                       |
| async_generators         | 444 ms                                                 | 455 ms: 1.03x slower                                                        |
| gc_traversal             | 3.62 ms                                                | 3.74 ms: 1.03x slower                                                       |
| create_gc_cycles         | 1.62 ms                                                | 1.76 ms: 1.09x slower                                                       |
| telco                    | 7.27 ms                                                | 7.96 ms: 1.10x slower                                                       |
| coverage                 | 79.4 ms                                                | 93.8 ms: 1.18x slower                                                       |
| python_startup_no_site   | 5.93 ms                                                | 7.18 ms: 1.21x slower                                                       |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                                |

Benchmark hidden because not significant (2): asyncio_websockets, bench_mp_pool
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240716-3.14.0a0-eb895df-JIT/bm-20240716-linux-x86_64-brandtbucher-invalidate_side_exit-3.14.0a0-eb895df.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.18x