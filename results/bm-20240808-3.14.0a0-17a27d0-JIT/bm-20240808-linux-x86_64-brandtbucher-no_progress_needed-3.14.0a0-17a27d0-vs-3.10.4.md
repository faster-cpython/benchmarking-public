# Results vs. 3.10.4

- fork: brandtbucher
- ref: no_progress_needed
- machine: linux-x86_64
- commit hash: 17a27d0
- commit date: 2024-08-08
- overall geometric mean: 1.44x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240808-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-17a27d0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 274 ms: 1.27x faster                                                      |
| docutils       | 3.30 sec                                               | 2.98 sec: 1.11x faster                                                    |
| html5lib       | 88.9 ms                                                | 65.4 ms: 1.36x faster                                                     |
| tornado_http   | 136 ms                                                 | 92.3 ms: 1.48x faster                                                     |
| Geometric mean | (ref)                                                  | 1.30x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240808-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-17a27d0 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 330 ms: 2.21x faster                                                      |
| async_tree_memoization  | 870 ms                                                 | 428 ms: 2.03x faster                                                      |
| async_tree_io           | 1.77 sec                                               | 906 ms: 1.95x faster                                                      |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 566 ms: 1.79x faster                                                      |
| Geometric mean          | (ref)                                                  | 1.99x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240808-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-17a27d0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.1 ms: 1.92x faster                                                     |
| float          | 117 ms                                                 | 70.9 ms: 1.65x faster                                                     |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                  | 1.48x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240808-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-17a27d0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 137 ms: 1.38x faster                                                      |
| regex_v8       | 27.8 ms                                                | 23.9 ms: 1.16x faster                                                     |
| regex_dna      | 227 ms                                                 | 219 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                  | 1.13x faster                                                              |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240808-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-17a27d0 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.90 sec: 1.65x faster                                                    |
| pickle_pure_python   | 484 us                                                 | 299 us: 1.62x faster                                                      |
| unpickle_pure_python | 331 us                                                 | 211 us: 1.57x faster                                                      |
| xml_etree_process    | 79.1 ms                                                | 56.2 ms: 1.41x faster                                                     |
| json_dumps           | 14.2 ms                                                | 10.2 ms: 1.39x faster                                                     |
| xml_etree_generate   | 99.4 ms                                                | 80.3 ms: 1.24x faster                                                     |
| xml_etree_iterparse  | 115 ms                                                 | 98.5 ms: 1.17x faster                                                     |
| xml_etree_parse      | 168 ms                                                 | 147 ms: 1.14x faster                                                      |
| json_loads           | 31.2 us                                                | 28.0 us: 1.12x faster                                                     |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240808-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-17a27d0 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                     |
| python_startup_no_site | 5.93 ms                                                | 7.18 ms: 1.21x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240808-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-17a27d0 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.77 ms: 1.67x faster                                                     |
| django_template | 48.2 ms                                                | 35.8 ms: 1.34x faster                                                     |
| genshi_text     | 31.8 ms                                                | 24.5 ms: 1.30x faster                                                     |
| genshi_xml      | 66.0 ms                                                | 54.5 ms: 1.21x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.37x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240808-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-17a27d0 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 168 us: 3.23x faster                                                      |
| deltablue                | 7.91 ms                                                | 3.08 ms: 2.57x faster                                                     |
| generators               | 80.1 ms                                                | 32.8 ms: 2.44x faster                                                     |
| async_tree_none          | 728 ms                                                 | 330 ms: 2.21x faster                                                      |
| deepcopy_memo            | 58.5 us                                                | 26.7 us: 2.19x faster                                                     |
| richards_super           | 94.7 ms                                                | 45.5 ms: 2.08x faster                                                     |
| async_tree_memoization   | 870 ms                                                 | 428 ms: 2.03x faster                                                      |
| chaos                    | 115 ms                                                 | 57.1 ms: 2.02x faster                                                     |
| richards                 | 79.3 ms                                                | 39.6 ms: 2.00x faster                                                     |
| async_tree_io            | 1.77 sec                                               | 906 ms: 1.95x faster                                                      |
| nbody                    | 154 ms                                                 | 80.1 ms: 1.92x faster                                                     |
| crypto_pyaes             | 128 ms                                                 | 66.7 ms: 1.92x faster                                                     |
| raytrace                 | 507 ms                                                 | 265 ms: 1.91x faster                                                      |
| scimark_sor              | 220 ms                                                 | 115 ms: 1.90x faster                                                      |
| logging_silent           | 190 ns                                                 | 99.8 ns: 1.90x faster                                                     |
| scimark_monte_carlo      | 118 ms                                                 | 62.3 ms: 1.90x faster                                                     |
| asyncio_tcp              | 922 ms                                                 | 504 ms: 1.83x faster                                                      |
| deepcopy                 | 479 us                                                 | 266 us: 1.80x faster                                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 566 ms: 1.79x faster                                                      |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                                     |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.68x faster                                                     |
| mako                     | 16.3 ms                                                | 9.77 ms: 1.67x faster                                                     |
| go                       | 240 ms                                                 | 144 ms: 1.66x faster                                                      |
| float                    | 117 ms                                                 | 70.9 ms: 1.65x faster                                                     |
| tomli_loads              | 3.14 sec                                               | 1.90 sec: 1.65x faster                                                    |
| pyflate                  | 716 ms                                                 | 436 ms: 1.64x faster                                                      |
| scimark_lu               | 176 ms                                                 | 107 ms: 1.64x faster                                                      |
| pickle_pure_python       | 484 us                                                 | 299 us: 1.62x faster                                                      |
| spectral_norm            | 170 ms                                                 | 105 ms: 1.62x faster                                                      |
| deepcopy_reduce          | 4.17 us                                                | 2.63 us: 1.59x faster                                                     |
| sqlglot_transpile        | 2.57 ms                                                | 1.64 ms: 1.57x faster                                                     |
| coroutines               | 35.1 ms                                                | 22.3 ms: 1.57x faster                                                     |
| unpickle_pure_python     | 331 us                                                 | 211 us: 1.57x faster                                                      |
| hexiom                   | 10.4 ms                                                | 6.74 ms: 1.54x faster                                                     |
| logging_simple           | 8.30 us                                                | 5.51 us: 1.51x faster                                                     |
| pylint                   | 551 ms                                                 | 367 ms: 1.50x faster                                                      |
| scimark_fft              | 466 ms                                                 | 312 ms: 1.49x faster                                                      |
| logging_format           | 9.09 us                                                | 6.11 us: 1.49x faster                                                     |
| tornado_http             | 136 ms                                                 | 92.3 ms: 1.48x faster                                                     |
| fannkuch                 | 532 ms                                                 | 366 ms: 1.45x faster                                                      |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.51 ms: 1.44x faster                                                     |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                                    |
| xml_etree_process        | 79.1 ms                                                | 56.2 ms: 1.41x faster                                                     |
| json_dumps               | 14.2 ms                                                | 10.2 ms: 1.39x faster                                                     |
| pprint_safe_repr         | 1.02 sec                                               | 737 ms: 1.38x faster                                                      |
| pprint_pformat           | 2.10 sec                                               | 1.52 sec: 1.38x faster                                                    |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                     |
| regex_compile            | 188 ms                                                 | 137 ms: 1.38x faster                                                      |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.37x faster                                                    |
| html5lib                 | 88.9 ms                                                | 65.4 ms: 1.36x faster                                                     |
| thrift                   | 1.07 ms                                                | 793 us: 1.35x faster                                                      |
| django_template          | 48.2 ms                                                | 35.8 ms: 1.34x faster                                                     |
| genshi_text              | 31.8 ms                                                | 24.5 ms: 1.30x faster                                                     |
| sqlglot_normalize        | 143 ms                                                 | 112 ms: 1.28x faster                                                      |
| 2to3                     | 348 ms                                                 | 274 ms: 1.27x faster                                                      |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                                     |
| nqueens                  | 106 ms                                                 | 84.0 ms: 1.26x faster                                                     |
| xml_etree_generate       | 99.4 ms                                                | 80.3 ms: 1.24x faster                                                     |
| genshi_xml               | 66.0 ms                                                | 54.5 ms: 1.21x faster                                                     |
| sqlglot_optimize         | 69.2 ms                                                | 57.0 ms: 1.21x faster                                                     |
| bench_thread_pool        | 986 us                                                 | 819 us: 1.21x faster                                                      |
| xml_etree_iterparse      | 115 ms                                                 | 98.5 ms: 1.17x faster                                                     |
| sympy_str                | 346 ms                                                 | 297 ms: 1.17x faster                                                      |
| regex_v8                 | 27.8 ms                                                | 23.9 ms: 1.16x faster                                                     |
| sympy_sum                | 196 ms                                                 | 172 ms: 1.15x faster                                                      |
| xml_etree_parse          | 168 ms                                                 | 147 ms: 1.14x faster                                                      |
| sympy_integrate          | 25.8 ms                                                | 22.6 ms: 1.14x faster                                                     |
| meteor_contest           | 120 ms                                                 | 105 ms: 1.13x faster                                                      |
| sympy_expand             | 566 ms                                                 | 501 ms: 1.13x faster                                                      |
| json                     | 5.69 ms                                                | 5.07 ms: 1.12x faster                                                     |
| mdp                      | 2.85 sec                                               | 2.54 sec: 1.12x faster                                                    |
| json_loads               | 31.2 us                                                | 28.0 us: 1.12x faster                                                     |
| docutils                 | 3.30 sec                                               | 2.98 sec: 1.11x faster                                                    |
| regex_dna                | 227 ms                                                 | 219 ms: 1.03x faster                                                      |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                      |
| gc_traversal             | 3.62 ms                                                | 3.65 ms: 1.01x slower                                                     |
| async_generators         | 444 ms                                                 | 454 ms: 1.02x slower                                                      |
| telco                    | 7.27 ms                                                | 7.73 ms: 1.06x slower                                                     |
| create_gc_cycles         | 1.62 ms                                                | 1.77 ms: 1.09x slower                                                     |
| coverage                 | 79.4 ms                                                | 91.6 ms: 1.15x slower                                                     |
| python_startup_no_site   | 5.93 ms                                                | 7.18 ms: 1.21x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.44x faster                                                              |

Benchmark hidden because not significant (3): asyncio_websockets, bench_mp_pool, regex_effbot
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240808-3.14.0a0-17a27d0-JIT/bm-20240808-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-17a27d0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.20x