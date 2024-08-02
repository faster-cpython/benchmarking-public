# Results vs. 3.10.4

- fork: brandtbucher
- ref: no_progress_needed_2
- machine: linux-x86_64
- commit hash: fd96445
- commit date: 2024-07-13
- overall geometric mean: 1.42x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.18x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_2-3.14.0a0-fd96445 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 276 ms: 1.26x faster                                                        |
| docutils       | 3.30 sec                                               | 2.88 sec: 1.15x faster                                                      |
| html5lib       | 88.9 ms                                                | 65.1 ms: 1.37x faster                                                       |
| tornado_http   | 136 ms                                                 | 93.2 ms: 1.46x faster                                                       |
| Geometric mean | (ref)                                                  | 1.30x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_2-3.14.0a0-fd96445 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 330 ms: 2.21x faster                                                        |
| async_tree_memoization  | 870 ms                                                 | 412 ms: 2.11x faster                                                        |
| async_tree_io           | 1.77 sec                                               | 893 ms: 1.98x faster                                                        |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 566 ms: 1.79x faster                                                        |
| Geometric mean          | (ref)                                                  | 2.02x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_2-3.14.0a0-fd96445 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 79.4 ms: 1.93x faster                                                       |
| float          | 117 ms                                                 | 70.8 ms: 1.65x faster                                                       |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                  | 1.49x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_2-3.14.0a0-fd96445 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 137 ms: 1.37x faster                                                        |
| regex_v8       | 27.8 ms                                                | 25.5 ms: 1.09x faster                                                       |
| regex_dna      | 227 ms                                                 | 222 ms: 1.02x faster                                                        |
| regex_effbot   | 3.63 ms                                                | 3.77 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_2-3.14.0a0-fd96445 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.91 sec: 1.64x faster                                                      |
| pickle_pure_python   | 484 us                                                 | 304 us: 1.59x faster                                                        |
| unpickle_pure_python | 331 us                                                 | 215 us: 1.54x faster                                                        |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.36x faster                                                       |
| xml_etree_process    | 79.1 ms                                                | 58.5 ms: 1.35x faster                                                       |
| xml_etree_generate   | 99.4 ms                                                | 83.1 ms: 1.20x faster                                                       |
| xml_etree_iterparse  | 115 ms                                                 | 99.5 ms: 1.16x faster                                                       |
| xml_etree_parse      | 168 ms                                                 | 146 ms: 1.15x faster                                                        |
| json_loads           | 31.2 us                                                | 28.3 us: 1.10x faster                                                       |
| Geometric mean       | (ref)                                                  | 1.33x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_2-3.14.0a0-fd96445 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                       |
| python_startup_no_site | 5.93 ms                                                | 7.15 ms: 1.21x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_2-3.14.0a0-fd96445 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.60 ms: 1.70x faster                                                       |
| django_template | 48.2 ms                                                | 35.8 ms: 1.35x faster                                                       |
| genshi_text     | 31.8 ms                                                | 25.4 ms: 1.25x faster                                                       |
| genshi_xml      | 66.0 ms                                                | 57.0 ms: 1.16x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_2-3.14.0a0-fd96445 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 168 us: 3.23x faster                                                        |
| generators               | 80.1 ms                                                | 29.7 ms: 2.70x faster                                                       |
| deltablue                | 7.91 ms                                                | 3.42 ms: 2.32x faster                                                       |
| async_tree_none          | 728 ms                                                 | 330 ms: 2.21x faster                                                        |
| richards_super           | 94.7 ms                                                | 43.9 ms: 2.16x faster                                                       |
| deepcopy_memo            | 58.5 us                                                | 27.3 us: 2.14x faster                                                       |
| async_tree_memoization   | 870 ms                                                 | 412 ms: 2.11x faster                                                        |
| richards                 | 79.3 ms                                                | 37.7 ms: 2.10x faster                                                       |
| chaos                    | 115 ms                                                 | 57.3 ms: 2.02x faster                                                       |
| async_tree_io            | 1.77 sec                                               | 893 ms: 1.98x faster                                                        |
| scimark_monte_carlo      | 118 ms                                                 | 60.5 ms: 1.95x faster                                                       |
| nbody                    | 154 ms                                                 | 79.4 ms: 1.93x faster                                                       |
| raytrace                 | 507 ms                                                 | 268 ms: 1.89x faster                                                        |
| crypto_pyaes             | 128 ms                                                 | 68.1 ms: 1.88x faster                                                       |
| logging_silent           | 190 ns                                                 | 103 ns: 1.83x faster                                                        |
| asyncio_tcp              | 922 ms                                                 | 505 ms: 1.83x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 566 ms: 1.79x faster                                                        |
| deepcopy                 | 479 us                                                 | 276 us: 1.74x faster                                                        |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.71x faster                                                       |
| sqlglot_parse            | 2.17 ms                                                | 1.27 ms: 1.71x faster                                                       |
| mako                     | 16.3 ms                                                | 9.60 ms: 1.70x faster                                                       |
| scimark_sor              | 220 ms                                                 | 132 ms: 1.67x faster                                                        |
| float                    | 117 ms                                                 | 70.8 ms: 1.65x faster                                                       |
| go                       | 240 ms                                                 | 145 ms: 1.65x faster                                                        |
| pyflate                  | 716 ms                                                 | 433 ms: 1.65x faster                                                        |
| spectral_norm            | 170 ms                                                 | 103 ms: 1.64x faster                                                        |
| tomli_loads              | 3.14 sec                                               | 1.91 sec: 1.64x faster                                                      |
| pylint                   | 551 ms                                                 | 340 ms: 1.62x faster                                                        |
| sqlglot_transpile        | 2.57 ms                                                | 1.61 ms: 1.60x faster                                                       |
| pickle_pure_python       | 484 us                                                 | 304 us: 1.59x faster                                                        |
| hexiom                   | 10.4 ms                                                | 6.69 ms: 1.55x faster                                                       |
| unpickle_pure_python     | 331 us                                                 | 215 us: 1.54x faster                                                        |
| deepcopy_reduce          | 4.17 us                                                | 2.76 us: 1.51x faster                                                       |
| logging_simple           | 8.30 us                                                | 5.52 us: 1.50x faster                                                       |
| scimark_fft              | 466 ms                                                 | 310 ms: 1.50x faster                                                        |
| logging_format           | 9.09 us                                                | 6.08 us: 1.50x faster                                                       |
| coroutines               | 35.1 ms                                                | 23.5 ms: 1.49x faster                                                       |
| fannkuch                 | 532 ms                                                 | 360 ms: 1.48x faster                                                        |
| tornado_http             | 136 ms                                                 | 93.2 ms: 1.46x faster                                                       |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.45 ms: 1.45x faster                                                       |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                                      |
| scimark_lu               | 176 ms                                                 | 126 ms: 1.40x faster                                                        |
| pprint_pformat           | 2.10 sec                                               | 1.51 sec: 1.39x faster                                                      |
| pprint_safe_repr         | 1.02 sec                                               | 733 ms: 1.39x faster                                                        |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                       |
| regex_compile            | 188 ms                                                 | 137 ms: 1.37x faster                                                        |
| html5lib                 | 88.9 ms                                                | 65.1 ms: 1.37x faster                                                       |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.36x faster                                                       |
| xml_etree_process        | 79.1 ms                                                | 58.5 ms: 1.35x faster                                                       |
| django_template          | 48.2 ms                                                | 35.8 ms: 1.35x faster                                                       |
| thrift                   | 1.07 ms                                                | 805 us: 1.33x faster                                                        |
| pycparser                | 1.58 sec                                               | 1.19 sec: 1.33x faster                                                      |
| sqlglot_normalize        | 143 ms                                                 | 111 ms: 1.28x faster                                                        |
| dulwich_log              | 84.3 ms                                                | 66.1 ms: 1.28x faster                                                       |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.28x faster                                                       |
| 2to3                     | 348 ms                                                 | 276 ms: 1.26x faster                                                        |
| genshi_text              | 31.8 ms                                                | 25.4 ms: 1.25x faster                                                       |
| sqlglot_optimize         | 69.2 ms                                                | 55.6 ms: 1.24x faster                                                       |
| nqueens                  | 106 ms                                                 | 86.7 ms: 1.22x faster                                                       |
| dask                     | 441 ms                                                 | 362 ms: 1.22x faster                                                        |
| xml_etree_generate       | 99.4 ms                                                | 83.1 ms: 1.20x faster                                                       |
| bench_thread_pool        | 986 us                                                 | 828 us: 1.19x faster                                                        |
| sympy_str                | 346 ms                                                 | 291 ms: 1.19x faster                                                        |
| sympy_integrate          | 25.8 ms                                                | 21.9 ms: 1.18x faster                                                       |
| sympy_sum                | 196 ms                                                 | 167 ms: 1.18x faster                                                        |
| xml_etree_iterparse      | 115 ms                                                 | 99.5 ms: 1.16x faster                                                       |
| genshi_xml               | 66.0 ms                                                | 57.0 ms: 1.16x faster                                                       |
| xml_etree_parse          | 168 ms                                                 | 146 ms: 1.15x faster                                                        |
| docutils                 | 3.30 sec                                               | 2.88 sec: 1.15x faster                                                      |
| sympy_expand             | 566 ms                                                 | 497 ms: 1.14x faster                                                        |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.12x faster                                                        |
| mdp                      | 2.85 sec                                               | 2.56 sec: 1.11x faster                                                      |
| json_loads               | 31.2 us                                                | 28.3 us: 1.10x faster                                                       |
| json                     | 5.69 ms                                                | 5.18 ms: 1.10x faster                                                       |
| regex_v8                 | 27.8 ms                                                | 25.5 ms: 1.09x faster                                                       |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                                        |
| regex_dna                | 227 ms                                                 | 222 ms: 1.02x faster                                                        |
| gc_traversal             | 3.62 ms                                                | 3.65 ms: 1.01x slower                                                       |
| async_generators         | 444 ms                                                 | 456 ms: 1.03x slower                                                        |
| regex_effbot             | 3.63 ms                                                | 3.77 ms: 1.04x slower                                                       |
| create_gc_cycles         | 1.62 ms                                                | 1.76 ms: 1.09x slower                                                       |
| telco                    | 7.27 ms                                                | 7.97 ms: 1.10x slower                                                       |
| coverage                 | 79.4 ms                                                | 92.2 ms: 1.16x slower                                                       |
| python_startup_no_site   | 5.93 ms                                                | 7.15 ms: 1.21x slower                                                       |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                                |

Benchmark hidden because not significant (2): asyncio_websockets, bench_mp_pool
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240713-3.14.0a0-fd96445-JIT/bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_2-3.14.0a0-fd96445.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.18x