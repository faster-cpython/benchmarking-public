# Results vs. 3.10.4

- fork: brandtbucher
- ref: off_by_one
- machine: linux-x86_64
- commit hash: e099186
- commit date: 2024-09-12
- overall geometric mean: 1.39x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-brandtbucher-off_by_one-3.14.0a0-e099186 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 276 ms: 1.26x faster                                              |
| docutils       | 3.30 sec                                               | 2.93 sec: 1.13x faster                                            |
| html5lib       | 88.9 ms                                                | 62.2 ms: 1.43x faster                                             |
| tornado_http   | 136 ms                                                 | 93.5 ms: 1.46x faster                                             |
| Geometric mean | (ref)                                                  | 1.31x faster                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-brandtbucher-off_by_one-3.14.0a0-e099186 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 315 ms: 2.31x faster                                              |
| async_tree_memoization  | 870 ms                                                 | 395 ms: 2.20x faster                                              |
| async_tree_io           | 1.77 sec                                               | 861 ms: 2.05x faster                                              |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 567 ms: 1.79x faster                                              |
| Geometric mean          | (ref)                                                  | 2.08x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-brandtbucher-off_by_one-3.14.0a0-e099186 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 79.0 ms: 1.94x faster                                             |
| float          | 117 ms                                                 | 69.7 ms: 1.68x faster                                             |
| pidigits       | 191 ms                                                 | 185 ms: 1.03x faster                                              |
| Geometric mean | (ref)                                                  | 1.50x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-brandtbucher-off_by_one-3.14.0a0-e099186 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 139 ms: 1.35x faster                                              |
| regex_v8       | 27.8 ms                                                | 25.1 ms: 1.11x faster                                             |
| regex_dna      | 227 ms                                                 | 217 ms: 1.05x faster                                              |
| regex_effbot   | 3.63 ms                                                | 3.50 ms: 1.04x faster                                             |
| Geometric mean | (ref)                                                  | 1.13x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-brandtbucher-off_by_one-3.14.0a0-e099186 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.93 sec: 1.63x faster                                            |
| pickle_pure_python   | 484 us                                                 | 310 us: 1.56x faster                                              |
| unpickle_pure_python | 331 us                                                 | 214 us: 1.55x faster                                              |
| xml_etree_process    | 79.1 ms                                                | 54.9 ms: 1.44x faster                                             |
| json_dumps           | 14.2 ms                                                | 9.99 ms: 1.42x faster                                             |
| xml_etree_generate   | 99.4 ms                                                | 79.4 ms: 1.25x faster                                             |
| xml_etree_iterparse  | 115 ms                                                 | 98.7 ms: 1.17x faster                                             |
| json_loads           | 31.2 us                                                | 27.1 us: 1.15x faster                                             |
| xml_etree_parse      | 168 ms                                                 | 146 ms: 1.15x faster                                              |
| pickle_list          | 5.08 us                                                | 5.22 us: 1.03x slower                                             |
| unpickle             | 14.4 us                                                | 14.8 us: 1.03x slower                                             |
| pickle               | 10.7 us                                                | 11.9 us: 1.11x slower                                             |
| pickle_dict          | 29.6 us                                                | 35.8 us: 1.21x slower                                             |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                      |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-brandtbucher-off_by_one-3.14.0a0-e099186 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                             |
| python_startup_no_site | 5.93 ms                                                | 7.05 ms: 1.19x slower                                             |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-brandtbucher-off_by_one-3.14.0a0-e099186 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.77 ms: 1.67x faster                                             |
| django_template | 48.2 ms                                                | 36.5 ms: 1.32x faster                                             |
| genshi_text     | 31.8 ms                                                | 25.4 ms: 1.25x faster                                             |
| genshi_xml      | 66.0 ms                                                | 58.6 ms: 1.13x faster                                             |
| Geometric mean  | (ref)                                                  | 1.33x faster                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-brandtbucher-off_by_one-3.14.0a0-e099186 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 165 us: 3.31x faster                                              |
| deltablue                | 7.91 ms                                                | 3.18 ms: 2.48x faster                                             |
| generators               | 80.1 ms                                                | 33.5 ms: 2.39x faster                                             |
| async_tree_none          | 728 ms                                                 | 315 ms: 2.31x faster                                              |
| async_tree_memoization   | 870 ms                                                 | 395 ms: 2.20x faster                                              |
| deepcopy_memo            | 58.5 us                                                | 26.6 us: 2.20x faster                                             |
| richards_super           | 94.7 ms                                                | 44.2 ms: 2.14x faster                                             |
| async_tree_io            | 1.77 sec                                               | 861 ms: 2.05x faster                                              |
| richards                 | 79.3 ms                                                | 38.9 ms: 2.04x faster                                             |
| chaos                    | 115 ms                                                 | 57.7 ms: 2.00x faster                                             |
| nbody                    | 154 ms                                                 | 79.0 ms: 1.94x faster                                             |
| crypto_pyaes             | 128 ms                                                 | 65.9 ms: 1.94x faster                                             |
| scimark_sor              | 220 ms                                                 | 116 ms: 1.90x faster                                              |
| scimark_monte_carlo      | 118 ms                                                 | 62.3 ms: 1.90x faster                                             |
| asyncio_tcp              | 922 ms                                                 | 487 ms: 1.89x faster                                              |
| raytrace                 | 507 ms                                                 | 271 ms: 1.87x faster                                              |
| go                       | 240 ms                                                 | 130 ms: 1.85x faster                                              |
| deepcopy                 | 479 us                                                 | 260 us: 1.84x faster                                              |
| logging_silent           | 190 ns                                                 | 104 ns: 1.83x faster                                              |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 567 ms: 1.79x faster                                              |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.74x faster                                             |
| spectral_norm            | 170 ms                                                 | 98.2 ms: 1.73x faster                                             |
| float                    | 117 ms                                                 | 69.7 ms: 1.68x faster                                             |
| mako                     | 16.3 ms                                                | 9.77 ms: 1.67x faster                                             |
| pyflate                  | 716 ms                                                 | 430 ms: 1.67x faster                                              |
| sqlglot_parse            | 2.17 ms                                                | 1.33 ms: 1.63x faster                                             |
| tomli_loads              | 3.14 sec                                               | 1.93 sec: 1.63x faster                                            |
| scimark_lu               | 176 ms                                                 | 111 ms: 1.59x faster                                              |
| deepcopy_reduce          | 4.17 us                                                | 2.65 us: 1.57x faster                                             |
| pickle_pure_python       | 484 us                                                 | 310 us: 1.56x faster                                              |
| unpickle_pure_python     | 331 us                                                 | 214 us: 1.55x faster                                              |
| sqlglot_transpile        | 2.57 ms                                                | 1.68 ms: 1.53x faster                                             |
| scimark_fft              | 466 ms                                                 | 304 ms: 1.53x faster                                              |
| coroutines               | 35.1 ms                                                | 23.0 ms: 1.53x faster                                             |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.27 ms: 1.51x faster                                             |
| hexiom                   | 10.4 ms                                                | 6.88 ms: 1.51x faster                                             |
| logging_format           | 9.09 us                                                | 6.13 us: 1.48x faster                                             |
| logging_simple           | 8.30 us                                                | 5.62 us: 1.48x faster                                             |
| pylint                   | 551 ms                                                 | 375 ms: 1.47x faster                                              |
| tornado_http             | 136 ms                                                 | 93.5 ms: 1.46x faster                                             |
| xml_etree_process        | 79.1 ms                                                | 54.9 ms: 1.44x faster                                             |
| html5lib                 | 88.9 ms                                                | 62.2 ms: 1.43x faster                                             |
| fannkuch                 | 532 ms                                                 | 372 ms: 1.43x faster                                              |
| pprint_safe_repr         | 1.02 sec                                               | 714 ms: 1.42x faster                                              |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                            |
| json_dumps               | 14.2 ms                                                | 9.99 ms: 1.42x faster                                             |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.42x faster                                            |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                             |
| regex_compile            | 188 ms                                                 | 139 ms: 1.35x faster                                              |
| thrift                   | 1.07 ms                                                | 797 us: 1.34x faster                                              |
| django_template          | 48.2 ms                                                | 36.5 ms: 1.32x faster                                             |
| pycparser                | 1.58 sec                                               | 1.20 sec: 1.31x faster                                            |
| pathlib                  | 20.5 ms                                                | 15.7 ms: 1.30x faster                                             |
| sqlglot_normalize        | 143 ms                                                 | 112 ms: 1.27x faster                                              |
| 2to3                     | 348 ms                                                 | 276 ms: 1.26x faster                                              |
| xml_etree_generate       | 99.4 ms                                                | 79.4 ms: 1.25x faster                                             |
| genshi_text              | 31.8 ms                                                | 25.4 ms: 1.25x faster                                             |
| dulwich_log              | 84.3 ms                                                | 67.6 ms: 1.25x faster                                             |
| nqueens                  | 106 ms                                                 | 85.0 ms: 1.24x faster                                             |
| sqlglot_optimize         | 69.2 ms                                                | 58.0 ms: 1.19x faster                                             |
| bench_thread_pool        | 986 us                                                 | 836 us: 1.18x faster                                              |
| xml_etree_iterparse      | 115 ms                                                 | 98.7 ms: 1.17x faster                                             |
| sympy_str                | 346 ms                                                 | 299 ms: 1.16x faster                                              |
| json_loads               | 31.2 us                                                | 27.1 us: 1.15x faster                                             |
| xml_etree_parse          | 168 ms                                                 | 146 ms: 1.15x faster                                              |
| sympy_sum                | 196 ms                                                 | 172 ms: 1.14x faster                                              |
| sympy_integrate          | 25.8 ms                                                | 22.7 ms: 1.14x faster                                             |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                              |
| genshi_xml               | 66.0 ms                                                | 58.6 ms: 1.13x faster                                             |
| docutils                 | 3.30 sec                                               | 2.93 sec: 1.13x faster                                            |
| mdp                      | 2.85 sec                                               | 2.54 sec: 1.12x faster                                            |
| sympy_expand             | 566 ms                                                 | 505 ms: 1.12x faster                                              |
| regex_v8                 | 27.8 ms                                                | 25.1 ms: 1.11x faster                                             |
| json                     | 5.69 ms                                                | 5.14 ms: 1.11x faster                                             |
| sqlite_synth             | 3.02 us                                                | 2.75 us: 1.10x faster                                             |
| regex_dna                | 227 ms                                                 | 217 ms: 1.05x faster                                              |
| regex_effbot             | 3.63 ms                                                | 3.50 ms: 1.04x faster                                             |
| pidigits                 | 191 ms                                                 | 185 ms: 1.03x faster                                              |
| pickle_list              | 5.08 us                                                | 5.22 us: 1.03x slower                                             |
| unpickle                 | 14.4 us                                                | 14.8 us: 1.03x slower                                             |
| async_generators         | 444 ms                                                 | 460 ms: 1.04x slower                                              |
| coverage                 | 79.4 ms                                                | 85.7 ms: 1.08x slower                                             |
| create_gc_cycles         | 1.62 ms                                                | 1.75 ms: 1.08x slower                                             |
| telco                    | 7.27 ms                                                | 7.87 ms: 1.08x slower                                             |
| gc_traversal             | 3.62 ms                                                | 3.94 ms: 1.09x slower                                             |
| pickle                   | 10.7 us                                                | 11.9 us: 1.11x slower                                             |
| python_startup_no_site   | 5.93 ms                                                | 7.05 ms: 1.19x slower                                             |
| pickle_dict              | 29.6 us                                                | 35.8 us: 1.21x slower                                             |
| unpack_sequence          | 60.0 ns                                                | 105 ns: 1.75x slower                                              |
| Geometric mean           | (ref)                                                  | 1.39x faster                                                      |

Benchmark hidden because not significant (3): asyncio_websockets, bench_mp_pool, unpickle_list
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240912-3.14.0a0-e099186-JIT/bm-20240912-linux-x86_64-brandtbucher-off_by_one-3.14.0a0-e099186.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.21x