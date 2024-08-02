# Results vs. 3.10.4

- fork: brandtbucher
- ref: no_progress_needed
- machine: linux-x86_64
- commit hash: 62e781e
- commit date: 2024-07-29
- overall geometric mean: 1.42x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-62e781e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 282 ms: 1.24x faster                                                      |
| docutils       | 3.30 sec                                               | 2.99 sec: 1.10x faster                                                    |
| html5lib       | 88.9 ms                                                | 67.3 ms: 1.32x faster                                                     |
| tornado_http   | 136 ms                                                 | 92.8 ms: 1.47x faster                                                     |
| Geometric mean | (ref)                                                  | 1.28x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-62e781e |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 325 ms: 2.24x faster                                                      |
| async_tree_memoization  | 870 ms                                                 | 427 ms: 2.04x faster                                                      |
| async_tree_io           | 1.77 sec                                               | 907 ms: 1.95x faster                                                      |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 559 ms: 1.82x faster                                                      |
| Geometric mean          | (ref)                                                  | 2.01x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-62e781e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.0 ms: 1.92x faster                                                     |
| float          | 117 ms                                                 | 70.5 ms: 1.66x faster                                                     |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                  | 1.48x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-62e781e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 143 ms: 1.32x faster                                                      |
| regex_v8       | 27.8 ms                                                | 25.5 ms: 1.09x faster                                                     |
| regex_dna      | 227 ms                                                 | 229 ms: 1.01x slower                                                      |
| regex_effbot   | 3.63 ms                                                | 3.79 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                  | 1.08x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-62e781e |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.91 sec: 1.65x faster                                                    |
| pickle_pure_python   | 484 us                                                 | 303 us: 1.60x faster                                                      |
| unpickle_pure_python | 331 us                                                 | 213 us: 1.56x faster                                                      |
| xml_etree_process    | 79.1 ms                                                | 56.2 ms: 1.41x faster                                                     |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                     |
| xml_etree_generate   | 99.4 ms                                                | 79.8 ms: 1.25x faster                                                     |
| xml_etree_iterparse  | 115 ms                                                 | 99.4 ms: 1.16x faster                                                     |
| xml_etree_parse      | 168 ms                                                 | 146 ms: 1.15x faster                                                      |
| json_loads           | 31.2 us                                                | 28.3 us: 1.10x faster                                                     |
| Geometric mean       | (ref)                                                  | 1.34x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-62e781e |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                     |
| python_startup_no_site | 5.93 ms                                                | 7.11 ms: 1.20x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-62e781e |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.77 ms: 1.67x faster                                                     |
| django_template | 48.2 ms                                                | 35.6 ms: 1.35x faster                                                     |
| genshi_text     | 31.8 ms                                                | 24.2 ms: 1.32x faster                                                     |
| genshi_xml      | 66.0 ms                                                | 52.8 ms: 1.25x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.39x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-62e781e |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.26x faster                                                      |
| deltablue                | 7.91 ms                                                | 3.02 ms: 2.62x faster                                                     |
| generators               | 80.1 ms                                                | 32.8 ms: 2.44x faster                                                     |
| async_tree_none          | 728 ms                                                 | 325 ms: 2.24x faster                                                      |
| deepcopy_memo            | 58.5 us                                                | 26.9 us: 2.18x faster                                                     |
| async_tree_memoization   | 870 ms                                                 | 427 ms: 2.04x faster                                                      |
| chaos                    | 115 ms                                                 | 57.9 ms: 1.99x faster                                                     |
| async_tree_io            | 1.77 sec                                               | 907 ms: 1.95x faster                                                      |
| richards_super           | 94.7 ms                                                | 48.7 ms: 1.95x faster                                                     |
| crypto_pyaes             | 128 ms                                                 | 65.9 ms: 1.94x faster                                                     |
| logging_silent           | 190 ns                                                 | 98.4 ns: 1.93x faster                                                     |
| nbody                    | 154 ms                                                 | 80.0 ms: 1.92x faster                                                     |
| raytrace                 | 507 ms                                                 | 267 ms: 1.90x faster                                                      |
| scimark_monte_carlo      | 118 ms                                                 | 62.3 ms: 1.90x faster                                                     |
| richards                 | 79.3 ms                                                | 42.3 ms: 1.87x faster                                                     |
| asyncio_tcp              | 922 ms                                                 | 506 ms: 1.82x faster                                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 559 ms: 1.82x faster                                                      |
| deepcopy                 | 479 us                                                 | 268 us: 1.79x faster                                                      |
| scimark_sor              | 220 ms                                                 | 123 ms: 1.78x faster                                                      |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                                     |
| mako                     | 16.3 ms                                                | 9.77 ms: 1.67x faster                                                     |
| spectral_norm            | 170 ms                                                 | 102 ms: 1.66x faster                                                      |
| float                    | 117 ms                                                 | 70.5 ms: 1.66x faster                                                     |
| tomli_loads              | 3.14 sec                                               | 1.91 sec: 1.65x faster                                                    |
| go                       | 240 ms                                                 | 146 ms: 1.64x faster                                                      |
| sqlglot_parse            | 2.17 ms                                                | 1.32 ms: 1.64x faster                                                     |
| pyflate                  | 716 ms                                                 | 440 ms: 1.63x faster                                                      |
| pickle_pure_python       | 484 us                                                 | 303 us: 1.60x faster                                                      |
| unpickle_pure_python     | 331 us                                                 | 213 us: 1.56x faster                                                      |
| deepcopy_reduce          | 4.17 us                                                | 2.68 us: 1.55x faster                                                     |
| coroutines               | 35.1 ms                                                | 22.8 ms: 1.54x faster                                                     |
| sqlglot_transpile        | 2.57 ms                                                | 1.68 ms: 1.53x faster                                                     |
| scimark_fft              | 466 ms                                                 | 304 ms: 1.53x faster                                                      |
| logging_simple           | 8.30 us                                                | 5.43 us: 1.53x faster                                                     |
| logging_format           | 9.09 us                                                | 5.96 us: 1.53x faster                                                     |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.27 ms: 1.52x faster                                                     |
| pylint                   | 551 ms                                                 | 368 ms: 1.50x faster                                                      |
| scimark_lu               | 176 ms                                                 | 118 ms: 1.50x faster                                                      |
| tornado_http             | 136 ms                                                 | 92.8 ms: 1.47x faster                                                     |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                                    |
| fannkuch                 | 532 ms                                                 | 375 ms: 1.42x faster                                                      |
| xml_etree_process        | 79.1 ms                                                | 56.2 ms: 1.41x faster                                                     |
| pprint_safe_repr         | 1.02 sec                                               | 728 ms: 1.40x faster                                                      |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                     |
| pprint_pformat           | 2.10 sec                                               | 1.51 sec: 1.39x faster                                                    |
| thrift                   | 1.07 ms                                                | 787 us: 1.36x faster                                                      |
| django_template          | 48.2 ms                                                | 35.6 ms: 1.35x faster                                                     |
| hexiom                   | 10.4 ms                                                | 7.68 ms: 1.35x faster                                                     |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                     |
| html5lib                 | 88.9 ms                                                | 67.3 ms: 1.32x faster                                                     |
| regex_compile            | 188 ms                                                 | 143 ms: 1.32x faster                                                      |
| genshi_text              | 31.8 ms                                                | 24.2 ms: 1.32x faster                                                     |
| pycparser                | 1.58 sec                                               | 1.22 sec: 1.30x faster                                                    |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.28x faster                                                     |
| sqlglot_normalize        | 143 ms                                                 | 113 ms: 1.26x faster                                                      |
| genshi_xml               | 66.0 ms                                                | 52.8 ms: 1.25x faster                                                     |
| xml_etree_generate       | 99.4 ms                                                | 79.8 ms: 1.25x faster                                                     |
| nqueens                  | 106 ms                                                 | 85.4 ms: 1.24x faster                                                     |
| 2to3                     | 348 ms                                                 | 282 ms: 1.24x faster                                                      |
| dask                     | 441 ms                                                 | 363 ms: 1.21x faster                                                      |
| bench_thread_pool        | 986 us                                                 | 818 us: 1.21x faster                                                      |
| sqlglot_optimize         | 69.2 ms                                                | 58.3 ms: 1.19x faster                                                     |
| xml_etree_iterparse      | 115 ms                                                 | 99.4 ms: 1.16x faster                                                     |
| xml_etree_parse          | 168 ms                                                 | 146 ms: 1.15x faster                                                      |
| sympy_str                | 346 ms                                                 | 306 ms: 1.13x faster                                                      |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.12x faster                                                      |
| sympy_integrate          | 25.8 ms                                                | 23.0 ms: 1.12x faster                                                     |
| sympy_sum                | 196 ms                                                 | 176 ms: 1.11x faster                                                      |
| mdp                      | 2.85 sec                                               | 2.56 sec: 1.11x faster                                                    |
| json                     | 5.69 ms                                                | 5.13 ms: 1.11x faster                                                     |
| sympy_expand             | 566 ms                                                 | 511 ms: 1.11x faster                                                      |
| docutils                 | 3.30 sec                                               | 2.99 sec: 1.10x faster                                                    |
| json_loads               | 31.2 us                                                | 28.3 us: 1.10x faster                                                     |
| regex_v8                 | 27.8 ms                                                | 25.5 ms: 1.09x faster                                                     |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                      |
| gc_traversal             | 3.62 ms                                                | 3.56 ms: 1.02x faster                                                     |
| regex_dna                | 227 ms                                                 | 229 ms: 1.01x slower                                                      |
| async_generators         | 444 ms                                                 | 458 ms: 1.03x slower                                                      |
| regex_effbot             | 3.63 ms                                                | 3.79 ms: 1.04x slower                                                     |
| telco                    | 7.27 ms                                                | 7.76 ms: 1.07x slower                                                     |
| create_gc_cycles         | 1.62 ms                                                | 1.74 ms: 1.07x slower                                                     |
| coverage                 | 79.4 ms                                                | 90.4 ms: 1.14x slower                                                     |
| python_startup_no_site   | 5.93 ms                                                | 7.11 ms: 1.20x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                              |

Benchmark hidden because not significant (2): asyncio_websockets, bench_mp_pool
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240729-3.14.0a0-62e781e-JIT/bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-62e781e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.20x