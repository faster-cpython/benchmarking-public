# Results vs. 3.10.4

- fork: brandtbucher
- ref: no_progress_needed
- machine: linux-x86_64
- commit hash: a4c1908
- commit date: 2024-07-13
- overall geometric mean: 1.43x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.18x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 275 ms: 1.27x faster                                                      |
| docutils       | 3.30 sec                                               | 2.92 sec: 1.13x faster                                                    |
| html5lib       | 88.9 ms                                                | 63.6 ms: 1.40x faster                                                     |
| tornado_http   | 136 ms                                                 | 92.2 ms: 1.48x faster                                                     |
| Geometric mean | (ref)                                                  | 1.31x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 327 ms: 2.22x faster                                                      |
| async_tree_memoization  | 870 ms                                                 | 411 ms: 2.11x faster                                                      |
| async_tree_io           | 1.77 sec                                               | 845 ms: 2.09x faster                                                      |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 569 ms: 1.78x faster                                                      |
| Geometric mean          | (ref)                                                  | 2.05x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.5 ms: 1.91x faster                                                     |
| float          | 117 ms                                                 | 69.5 ms: 1.69x faster                                                     |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                  | 1.49x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 137 ms: 1.37x faster                                                      |
| regex_v8       | 27.8 ms                                                | 25.4 ms: 1.09x faster                                                     |
| regex_dna      | 227 ms                                                 | 228 ms: 1.01x slower                                                      |
| regex_effbot   | 3.63 ms                                                | 3.75 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                  | 1.10x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.87 sec: 1.68x faster                                                    |
| pickle_pure_python   | 484 us                                                 | 308 us: 1.57x faster                                                      |
| unpickle_pure_python | 331 us                                                 | 213 us: 1.55x faster                                                      |
| xml_etree_process    | 79.1 ms                                                | 57.6 ms: 1.37x faster                                                     |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                     |
| xml_etree_generate   | 99.4 ms                                                | 81.9 ms: 1.21x faster                                                     |
| xml_etree_iterparse  | 115 ms                                                 | 98.4 ms: 1.17x faster                                                     |
| xml_etree_parse      | 168 ms                                                 | 148 ms: 1.14x faster                                                      |
| json_loads           | 31.2 us                                                | 27.6 us: 1.13x faster                                                     |
| Geometric mean       | (ref)                                                  | 1.34x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.38x faster                                                     |
| python_startup_no_site | 5.93 ms                                                | 7.13 ms: 1.20x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.0 ms: 1.63x faster                                                     |
| django_template | 48.2 ms                                                | 34.9 ms: 1.38x faster                                                     |
| genshi_text     | 31.8 ms                                                | 25.9 ms: 1.23x faster                                                     |
| genshi_xml      | 66.0 ms                                                | 58.7 ms: 1.12x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.33x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 169 us: 3.22x faster                                                      |
| generators               | 80.1 ms                                                | 29.8 ms: 2.69x faster                                                     |
| richards_super           | 94.7 ms                                                | 40.8 ms: 2.32x faster                                                     |
| deltablue                | 7.91 ms                                                | 3.45 ms: 2.29x faster                                                     |
| async_tree_none          | 728 ms                                                 | 327 ms: 2.22x faster                                                      |
| richards                 | 79.3 ms                                                | 35.9 ms: 2.21x faster                                                     |
| deepcopy_memo            | 58.5 us                                                | 27.1 us: 2.16x faster                                                     |
| async_tree_memoization   | 870 ms                                                 | 411 ms: 2.11x faster                                                      |
| async_tree_io            | 1.77 sec                                               | 845 ms: 2.09x faster                                                      |
| chaos                    | 115 ms                                                 | 57.8 ms: 2.00x faster                                                     |
| crypto_pyaes             | 128 ms                                                 | 66.6 ms: 1.92x faster                                                     |
| nbody                    | 154 ms                                                 | 80.5 ms: 1.91x faster                                                     |
| scimark_monte_carlo      | 118 ms                                                 | 62.4 ms: 1.89x faster                                                     |
| logging_silent           | 190 ns                                                 | 101 ns: 1.87x faster                                                      |
| raytrace                 | 507 ms                                                 | 273 ms: 1.86x faster                                                      |
| asyncio_tcp              | 922 ms                                                 | 507 ms: 1.82x faster                                                      |
| deepcopy                 | 479 us                                                 | 265 us: 1.81x faster                                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 569 ms: 1.78x faster                                                      |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                                     |
| scimark_sor              | 220 ms                                                 | 128 ms: 1.72x faster                                                      |
| float                    | 117 ms                                                 | 69.5 ms: 1.69x faster                                                     |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.68x faster                                                     |
| tomli_loads              | 3.14 sec                                               | 1.87 sec: 1.68x faster                                                    |
| go                       | 240 ms                                                 | 145 ms: 1.66x faster                                                      |
| pyflate                  | 716 ms                                                 | 437 ms: 1.64x faster                                                      |
| spectral_norm            | 170 ms                                                 | 104 ms: 1.64x faster                                                      |
| mako                     | 16.3 ms                                                | 10.0 ms: 1.63x faster                                                     |
| pickle_pure_python       | 484 us                                                 | 308 us: 1.57x faster                                                      |
| sqlglot_transpile        | 2.57 ms                                                | 1.64 ms: 1.57x faster                                                     |
| pylint                   | 551 ms                                                 | 351 ms: 1.57x faster                                                      |
| deepcopy_reduce          | 4.17 us                                                | 2.68 us: 1.55x faster                                                     |
| unpickle_pure_python     | 331 us                                                 | 213 us: 1.55x faster                                                      |
| hexiom                   | 10.4 ms                                                | 6.73 ms: 1.55x faster                                                     |
| logging_simple           | 8.30 us                                                | 5.45 us: 1.52x faster                                                     |
| coroutines               | 35.1 ms                                                | 23.3 ms: 1.51x faster                                                     |
| logging_format           | 9.09 us                                                | 6.04 us: 1.50x faster                                                     |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.31 ms: 1.50x faster                                                     |
| scimark_fft              | 466 ms                                                 | 311 ms: 1.50x faster                                                      |
| scimark_lu               | 176 ms                                                 | 119 ms: 1.48x faster                                                      |
| fannkuch                 | 532 ms                                                 | 359 ms: 1.48x faster                                                      |
| tornado_http             | 136 ms                                                 | 92.2 ms: 1.48x faster                                                     |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                                    |
| html5lib                 | 88.9 ms                                                | 63.6 ms: 1.40x faster                                                     |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.38x faster                                                     |
| django_template          | 48.2 ms                                                | 34.9 ms: 1.38x faster                                                     |
| pprint_pformat           | 2.10 sec                                               | 1.53 sec: 1.38x faster                                                    |
| pprint_safe_repr         | 1.02 sec                                               | 740 ms: 1.38x faster                                                      |
| xml_etree_process        | 79.1 ms                                                | 57.6 ms: 1.37x faster                                                     |
| regex_compile            | 188 ms                                                 | 137 ms: 1.37x faster                                                      |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                     |
| pycparser                | 1.58 sec                                               | 1.19 sec: 1.32x faster                                                    |
| thrift                   | 1.07 ms                                                | 812 us: 1.32x faster                                                      |
| dulwich_log              | 84.3 ms                                                | 65.2 ms: 1.29x faster                                                     |
| sqlglot_normalize        | 143 ms                                                 | 112 ms: 1.28x faster                                                      |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.27x faster                                                     |
| 2to3                     | 348 ms                                                 | 275 ms: 1.27x faster                                                      |
| genshi_text              | 31.8 ms                                                | 25.9 ms: 1.23x faster                                                     |
| sqlglot_optimize         | 69.2 ms                                                | 56.2 ms: 1.23x faster                                                     |
| nqueens                  | 106 ms                                                 | 86.5 ms: 1.22x faster                                                     |
| dask                     | 441 ms                                                 | 361 ms: 1.22x faster                                                      |
| xml_etree_generate       | 99.4 ms                                                | 81.9 ms: 1.21x faster                                                     |
| sympy_str                | 346 ms                                                 | 289 ms: 1.20x faster                                                      |
| bench_thread_pool        | 986 us                                                 | 827 us: 1.19x faster                                                      |
| sympy_integrate          | 25.8 ms                                                | 21.7 ms: 1.19x faster                                                     |
| sympy_sum                | 196 ms                                                 | 166 ms: 1.18x faster                                                      |
| xml_etree_iterparse      | 115 ms                                                 | 98.4 ms: 1.17x faster                                                     |
| sympy_expand             | 566 ms                                                 | 494 ms: 1.15x faster                                                      |
| xml_etree_parse          | 168 ms                                                 | 148 ms: 1.14x faster                                                      |
| json_loads               | 31.2 us                                                | 27.6 us: 1.13x faster                                                     |
| docutils                 | 3.30 sec                                               | 2.92 sec: 1.13x faster                                                    |
| genshi_xml               | 66.0 ms                                                | 58.7 ms: 1.12x faster                                                     |
| mdp                      | 2.85 sec                                               | 2.54 sec: 1.12x faster                                                    |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                      |
| json                     | 5.69 ms                                                | 5.17 ms: 1.10x faster                                                     |
| regex_v8                 | 27.8 ms                                                | 25.4 ms: 1.09x faster                                                     |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                      |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                                      |
| regex_dna                | 227 ms                                                 | 228 ms: 1.01x slower                                                      |
| async_generators         | 444 ms                                                 | 452 ms: 1.02x slower                                                      |
| regex_effbot             | 3.63 ms                                                | 3.75 ms: 1.03x slower                                                     |
| gc_traversal             | 3.62 ms                                                | 3.85 ms: 1.06x slower                                                     |
| telco                    | 7.27 ms                                                | 7.88 ms: 1.08x slower                                                     |
| create_gc_cycles         | 1.62 ms                                                | 1.78 ms: 1.10x slower                                                     |
| coverage                 | 79.4 ms                                                | 92.2 ms: 1.16x slower                                                     |
| python_startup_no_site   | 5.93 ms                                                | 7.13 ms: 1.20x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                              |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240713-3.14.0a0-a4c1908-JIT/bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.18x