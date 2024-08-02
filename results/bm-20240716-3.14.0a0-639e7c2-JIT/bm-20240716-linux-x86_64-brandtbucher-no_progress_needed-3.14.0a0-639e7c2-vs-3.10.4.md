# Results vs. 3.10.4

- fork: brandtbucher
- ref: no_progress_needed
- machine: linux-x86_64
- commit hash: 639e7c2
- commit date: 2024-07-16
- overall geometric mean: 1.43x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240716-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-639e7c2 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 276 ms: 1.26x faster                                                      |
| docutils       | 3.30 sec                                               | 2.92 sec: 1.13x faster                                                    |
| html5lib       | 88.9 ms                                                | 66.4 ms: 1.34x faster                                                     |
| tornado_http   | 136 ms                                                 | 92.2 ms: 1.48x faster                                                     |
| Geometric mean | (ref)                                                  | 1.30x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240716-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-639e7c2 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 323 ms: 2.25x faster                                                      |
| async_tree_memoization  | 870 ms                                                 | 406 ms: 2.14x faster                                                      |
| async_tree_io           | 1.77 sec                                               | 830 ms: 2.13x faster                                                      |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 559 ms: 1.82x faster                                                      |
| Geometric mean          | (ref)                                                  | 2.08x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240716-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-639e7c2 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.8 ms: 1.90x faster                                                     |
| float          | 117 ms                                                 | 69.9 ms: 1.68x faster                                                     |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                  | 1.48x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240716-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-639e7c2 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 138 ms: 1.36x faster                                                      |
| regex_v8       | 27.8 ms                                                | 23.9 ms: 1.16x faster                                                     |
| regex_dna      | 227 ms                                                 | 230 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                  | 1.12x faster                                                              |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240716-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-639e7c2 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.90 sec: 1.65x faster                                                    |
| pickle_pure_python   | 484 us                                                 | 301 us: 1.61x faster                                                      |
| unpickle_pure_python | 331 us                                                 | 214 us: 1.55x faster                                                      |
| xml_etree_process    | 79.1 ms                                                | 57.2 ms: 1.38x faster                                                     |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.37x faster                                                     |
| xml_etree_generate   | 99.4 ms                                                | 81.0 ms: 1.23x faster                                                     |
| xml_etree_iterparse  | 115 ms                                                 | 99.1 ms: 1.17x faster                                                     |
| xml_etree_parse      | 168 ms                                                 | 150 ms: 1.12x faster                                                      |
| json_loads           | 31.2 us                                                | 27.8 us: 1.12x faster                                                     |
| Geometric mean       | (ref)                                                  | 1.34x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240716-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-639e7c2 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                     |
| python_startup_no_site | 5.93 ms                                                | 7.15 ms: 1.21x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240716-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-639e7c2 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.73 ms: 1.68x faster                                                     |
| django_template | 48.2 ms                                                | 35.1 ms: 1.37x faster                                                     |
| genshi_text     | 31.8 ms                                                | 25.1 ms: 1.27x faster                                                     |
| genshi_xml      | 66.0 ms                                                | 57.3 ms: 1.15x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240716-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-639e7c2 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 170 us: 3.21x faster                                                      |
| generators               | 80.1 ms                                                | 29.6 ms: 2.70x faster                                                     |
| richards_super           | 94.7 ms                                                | 40.9 ms: 2.32x faster                                                     |
| deltablue                | 7.91 ms                                                | 3.43 ms: 2.31x faster                                                     |
| async_tree_none          | 728 ms                                                 | 323 ms: 2.25x faster                                                      |
| richards                 | 79.3 ms                                                | 35.7 ms: 2.22x faster                                                     |
| deepcopy_memo            | 58.5 us                                                | 27.3 us: 2.14x faster                                                     |
| async_tree_memoization   | 870 ms                                                 | 406 ms: 2.14x faster                                                      |
| async_tree_io            | 1.77 sec                                               | 830 ms: 2.13x faster                                                      |
| chaos                    | 115 ms                                                 | 57.7 ms: 2.00x faster                                                     |
| nbody                    | 154 ms                                                 | 80.8 ms: 1.90x faster                                                     |
| crypto_pyaes             | 128 ms                                                 | 67.3 ms: 1.90x faster                                                     |
| raytrace                 | 507 ms                                                 | 269 ms: 1.88x faster                                                      |
| scimark_monte_carlo      | 118 ms                                                 | 63.0 ms: 1.88x faster                                                     |
| asyncio_tcp              | 922 ms                                                 | 503 ms: 1.83x faster                                                      |
| deepcopy                 | 479 us                                                 | 263 us: 1.82x faster                                                      |
| logging_silent           | 190 ns                                                 | 104 ns: 1.82x faster                                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 559 ms: 1.82x faster                                                      |
| scimark_sor              | 220 ms                                                 | 126 ms: 1.75x faster                                                      |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                                     |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.68x faster                                                     |
| mako                     | 16.3 ms                                                | 9.73 ms: 1.68x faster                                                     |
| float                    | 117 ms                                                 | 69.9 ms: 1.68x faster                                                     |
| go                       | 240 ms                                                 | 144 ms: 1.67x faster                                                      |
| spectral_norm            | 170 ms                                                 | 102 ms: 1.66x faster                                                      |
| tomli_loads              | 3.14 sec                                               | 1.90 sec: 1.65x faster                                                    |
| pickle_pure_python       | 484 us                                                 | 301 us: 1.61x faster                                                      |
| deepcopy_reduce          | 4.17 us                                                | 2.63 us: 1.58x faster                                                     |
| pyflate                  | 716 ms                                                 | 454 ms: 1.58x faster                                                      |
| sqlglot_transpile        | 2.57 ms                                                | 1.64 ms: 1.57x faster                                                     |
| pylint                   | 551 ms                                                 | 352 ms: 1.57x faster                                                      |
| unpickle_pure_python     | 331 us                                                 | 214 us: 1.55x faster                                                      |
| coroutines               | 35.1 ms                                                | 22.7 ms: 1.55x faster                                                     |
| hexiom                   | 10.4 ms                                                | 6.77 ms: 1.54x faster                                                     |
| scimark_fft              | 466 ms                                                 | 309 ms: 1.51x faster                                                      |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.29 ms: 1.51x faster                                                     |
| logging_simple           | 8.30 us                                                | 5.51 us: 1.51x faster                                                     |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.50x faster                                                      |
| logging_format           | 9.09 us                                                | 6.10 us: 1.49x faster                                                     |
| tornado_http             | 136 ms                                                 | 92.2 ms: 1.48x faster                                                     |
| fannkuch                 | 532 ms                                                 | 364 ms: 1.46x faster                                                      |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                                    |
| pprint_safe_repr         | 1.02 sec                                               | 735 ms: 1.39x faster                                                      |
| pycparser                | 1.58 sec                                               | 1.14 sec: 1.39x faster                                                    |
| pprint_pformat           | 2.10 sec                                               | 1.52 sec: 1.38x faster                                                    |
| xml_etree_process        | 79.1 ms                                                | 57.2 ms: 1.38x faster                                                     |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                     |
| django_template          | 48.2 ms                                                | 35.1 ms: 1.37x faster                                                     |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.37x faster                                                     |
| regex_compile            | 188 ms                                                 | 138 ms: 1.36x faster                                                      |
| thrift                   | 1.07 ms                                                | 798 us: 1.34x faster                                                      |
| html5lib                 | 88.9 ms                                                | 66.4 ms: 1.34x faster                                                     |
| sqlglot_normalize        | 143 ms                                                 | 111 ms: 1.28x faster                                                      |
| dulwich_log              | 84.3 ms                                                | 65.9 ms: 1.28x faster                                                     |
| genshi_text              | 31.8 ms                                                | 25.1 ms: 1.27x faster                                                     |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                                     |
| 2to3                     | 348 ms                                                 | 276 ms: 1.26x faster                                                      |
| dask                     | 441 ms                                                 | 359 ms: 1.23x faster                                                      |
| xml_etree_generate       | 99.4 ms                                                | 81.0 ms: 1.23x faster                                                     |
| nqueens                  | 106 ms                                                 | 86.8 ms: 1.22x faster                                                     |
| sqlglot_optimize         | 69.2 ms                                                | 56.8 ms: 1.22x faster                                                     |
| bench_thread_pool        | 986 us                                                 | 825 us: 1.20x faster                                                      |
| sympy_str                | 346 ms                                                 | 289 ms: 1.20x faster                                                      |
| sympy_integrate          | 25.8 ms                                                | 21.8 ms: 1.18x faster                                                     |
| sympy_sum                | 196 ms                                                 | 166 ms: 1.18x faster                                                      |
| xml_etree_iterparse      | 115 ms                                                 | 99.1 ms: 1.17x faster                                                     |
| regex_v8                 | 27.8 ms                                                | 23.9 ms: 1.16x faster                                                     |
| genshi_xml               | 66.0 ms                                                | 57.3 ms: 1.15x faster                                                     |
| sympy_expand             | 566 ms                                                 | 495 ms: 1.14x faster                                                      |
| docutils                 | 3.30 sec                                               | 2.92 sec: 1.13x faster                                                    |
| xml_etree_parse          | 168 ms                                                 | 150 ms: 1.12x faster                                                      |
| json_loads               | 31.2 us                                                | 27.8 us: 1.12x faster                                                     |
| json                     | 5.69 ms                                                | 5.13 ms: 1.11x faster                                                     |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.09x faster                                                      |
| mdp                      | 2.85 sec                                               | 2.77 sec: 1.03x faster                                                    |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                      |
| gc_traversal             | 3.62 ms                                                | 3.55 ms: 1.02x faster                                                     |
| regex_dna                | 227 ms                                                 | 230 ms: 1.02x slower                                                      |
| async_generators         | 444 ms                                                 | 458 ms: 1.03x slower                                                      |
| create_gc_cycles         | 1.62 ms                                                | 1.74 ms: 1.07x slower                                                     |
| telco                    | 7.27 ms                                                | 8.03 ms: 1.11x slower                                                     |
| coverage                 | 79.4 ms                                                | 94.8 ms: 1.19x slower                                                     |
| python_startup_no_site   | 5.93 ms                                                | 7.15 ms: 1.21x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                              |

Benchmark hidden because not significant (3): asyncio_websockets, bench_mp_pool, regex_effbot
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240716-3.14.0a0-639e7c2-JIT/bm-20240716-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-639e7c2.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.19x