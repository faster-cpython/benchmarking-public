# Results vs. 3.10.4

- fork: brandtbucher
- ref: no_trace_too_short
- machine: linux-x86_64
- commit hash: ea1e85d
- commit date: 2024-06-06
- overall geometric mean: 1.33x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-ea1e85d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 281 ms: 1.24x faster                                                      |
| docutils       | 3.30 sec                                               | 2.93 sec: 1.12x faster                                                    |
| html5lib       | 88.9 ms                                                | 68.7 ms: 1.29x faster                                                     |
| tornado_http   | 136 ms                                                 | 97.1 ms: 1.40x faster                                                     |
| Geometric mean | (ref)                                                  | 1.26x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-ea1e85d |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 376 ms: 1.94x faster                                                      |
| async_tree_memoization  | 870 ms                                                 | 481 ms: 1.81x faster                                                      |
| async_tree_io           | 1.77 sec                                               | 979 ms: 1.81x faster                                                      |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 637 ms: 1.59x faster                                                      |
| Geometric mean          | (ref)                                                  | 1.78x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-ea1e85d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.5 ms: 1.91x faster                                                     |
| float          | 117 ms                                                 | 72.1 ms: 1.62x faster                                                     |
| pidigits       | 191 ms                                                 | 188 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.46x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-ea1e85d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 138 ms: 1.37x faster                                                      |
| regex_v8       | 27.8 ms                                                | 24.1 ms: 1.15x faster                                                     |
| regex_dna      | 227 ms                                                 | 226 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                  | 1.12x faster                                                              |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-ea1e85d |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.96 sec: 1.60x faster                                                    |
| pickle_pure_python   | 484 us                                                 | 303 us: 1.60x faster                                                      |
| unpickle_pure_python | 331 us                                                 | 222 us: 1.49x faster                                                      |
| xml_etree_process    | 79.1 ms                                                | 58.0 ms: 1.36x faster                                                     |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                     |
| xml_etree_generate   | 99.4 ms                                                | 81.4 ms: 1.22x faster                                                     |
| xml_etree_iterparse  | 115 ms                                                 | 102 ms: 1.13x faster                                                      |
| xml_etree_parse      | 168 ms                                                 | 150 ms: 1.12x faster                                                      |
| json_loads           | 31.2 us                                                | 29.0 us: 1.07x faster                                                     |
| unpickle             | 14.4 us                                                | 14.9 us: 1.03x slower                                                     |
| pickle_list          | 5.08 us                                                | 5.34 us: 1.05x slower                                                     |
| pickle               | 10.7 us                                                | 12.1 us: 1.14x slower                                                     |
| pickle_dict          | 29.6 us                                                | 36.3 us: 1.23x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                              |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-ea1e85d |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.1 ms: 1.31x faster                                                     |
| python_startup_no_site | 5.93 ms                                                | 7.60 ms: 1.28x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-ea1e85d |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.99 ms: 1.63x faster                                                     |
| django_template | 48.2 ms                                                | 36.2 ms: 1.33x faster                                                     |
| genshi_text     | 31.8 ms                                                | 25.0 ms: 1.27x faster                                                     |
| genshi_xml      | 66.0 ms                                                | 59.8 ms: 1.10x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.32x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-ea1e85d |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 170 us: 3.19x faster                                                      |
| deltablue                | 7.91 ms                                                | 3.78 ms: 2.09x faster                                                     |
| richards_super           | 94.7 ms                                                | 47.9 ms: 1.98x faster                                                     |
| chaos                    | 115 ms                                                 | 59.3 ms: 1.95x faster                                                     |
| async_tree_none          | 728 ms                                                 | 376 ms: 1.94x faster                                                      |
| richards                 | 79.3 ms                                                | 41.5 ms: 1.91x faster                                                     |
| nbody                    | 154 ms                                                 | 80.5 ms: 1.91x faster                                                     |
| crypto_pyaes             | 128 ms                                                 | 68.4 ms: 1.87x faster                                                     |
| scimark_monte_carlo      | 118 ms                                                 | 63.3 ms: 1.87x faster                                                     |
| raytrace                 | 507 ms                                                 | 278 ms: 1.82x faster                                                      |
| async_tree_memoization   | 870 ms                                                 | 481 ms: 1.81x faster                                                      |
| async_tree_io            | 1.77 sec                                               | 979 ms: 1.81x faster                                                      |
| logging_silent           | 190 ns                                                 | 107 ns: 1.77x faster                                                      |
| asyncio_tcp              | 922 ms                                                 | 523 ms: 1.76x faster                                                      |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                                     |
| spectral_norm            | 170 ms                                                 | 101 ms: 1.68x faster                                                      |
| sqlglot_parse            | 2.17 ms                                                | 1.30 ms: 1.67x faster                                                     |
| mako                     | 16.3 ms                                                | 9.99 ms: 1.63x faster                                                     |
| float                    | 117 ms                                                 | 72.1 ms: 1.62x faster                                                     |
| generators               | 80.1 ms                                                | 49.4 ms: 1.62x faster                                                     |
| go                       | 240 ms                                                 | 149 ms: 1.61x faster                                                      |
| scimark_sor              | 220 ms                                                 | 137 ms: 1.60x faster                                                      |
| tomli_loads              | 3.14 sec                                               | 1.96 sec: 1.60x faster                                                    |
| pickle_pure_python       | 484 us                                                 | 303 us: 1.60x faster                                                      |
| pyflate                  | 716 ms                                                 | 449 ms: 1.59x faster                                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 637 ms: 1.59x faster                                                      |
| sqlglot_transpile        | 2.57 ms                                                | 1.63 ms: 1.57x faster                                                     |
| hexiom                   | 10.4 ms                                                | 6.64 ms: 1.57x faster                                                     |
| coroutines               | 35.1 ms                                                | 22.7 ms: 1.55x faster                                                     |
| pylint                   | 551 ms                                                 | 357 ms: 1.54x faster                                                      |
| deepcopy_memo            | 58.5 us                                                | 38.4 us: 1.52x faster                                                     |
| fannkuch                 | 532 ms                                                 | 355 ms: 1.50x faster                                                      |
| unpickle_pure_python     | 331 us                                                 | 222 us: 1.49x faster                                                      |
| logging_simple           | 8.30 us                                                | 5.65 us: 1.47x faster                                                     |
| logging_format           | 9.09 us                                                | 6.22 us: 1.46x faster                                                     |
| pprint_pformat           | 2.10 sec                                               | 1.45 sec: 1.45x faster                                                    |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.48 ms: 1.45x faster                                                     |
| scimark_fft              | 466 ms                                                 | 327 ms: 1.43x faster                                                      |
| pprint_safe_repr         | 1.02 sec                                               | 714 ms: 1.43x faster                                                      |
| scimark_lu               | 176 ms                                                 | 125 ms: 1.41x faster                                                      |
| tornado_http             | 136 ms                                                 | 97.1 ms: 1.40x faster                                                     |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.87 sec: 1.38x faster                                                    |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.37x faster                                                    |
| regex_compile            | 188 ms                                                 | 138 ms: 1.37x faster                                                      |
| xml_etree_process        | 79.1 ms                                                | 58.0 ms: 1.36x faster                                                     |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                     |
| django_template          | 48.2 ms                                                | 36.2 ms: 1.33x faster                                                     |
| python_startup           | 14.6 ms                                                | 11.1 ms: 1.31x faster                                                     |
| thrift                   | 1.07 ms                                                | 824 us: 1.30x faster                                                      |
| html5lib                 | 88.9 ms                                                | 68.7 ms: 1.29x faster                                                     |
| deepcopy                 | 479 us                                                 | 372 us: 1.29x faster                                                      |
| genshi_text              | 31.8 ms                                                | 25.0 ms: 1.27x faster                                                     |
| sqlglot_normalize        | 143 ms                                                 | 114 ms: 1.25x faster                                                      |
| pathlib                  | 20.5 ms                                                | 16.4 ms: 1.24x faster                                                     |
| 2to3                     | 348 ms                                                 | 281 ms: 1.24x faster                                                      |
| deepcopy_reduce          | 4.17 us                                                | 3.38 us: 1.24x faster                                                     |
| dulwich_log              | 84.3 ms                                                | 68.9 ms: 1.22x faster                                                     |
| xml_etree_generate       | 99.4 ms                                                | 81.4 ms: 1.22x faster                                                     |
| nqueens                  | 106 ms                                                 | 86.9 ms: 1.22x faster                                                     |
| sqlglot_optimize         | 69.2 ms                                                | 57.3 ms: 1.21x faster                                                     |
| dask                     | 441 ms                                                 | 378 ms: 1.17x faster                                                      |
| regex_v8                 | 27.8 ms                                                | 24.1 ms: 1.15x faster                                                     |
| sympy_sum                | 196 ms                                                 | 171 ms: 1.15x faster                                                      |
| sympy_str                | 346 ms                                                 | 302 ms: 1.15x faster                                                      |
| sympy_integrate          | 25.8 ms                                                | 22.6 ms: 1.14x faster                                                     |
| xml_etree_iterparse      | 115 ms                                                 | 102 ms: 1.13x faster                                                      |
| docutils                 | 3.30 sec                                               | 2.93 sec: 1.12x faster                                                    |
| bench_thread_pool        | 986 us                                                 | 878 us: 1.12x faster                                                      |
| xml_etree_parse          | 168 ms                                                 | 150 ms: 1.12x faster                                                      |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                      |
| sympy_expand             | 566 ms                                                 | 511 ms: 1.11x faster                                                      |
| genshi_xml               | 66.0 ms                                                | 59.8 ms: 1.10x faster                                                     |
| mdp                      | 2.85 sec                                               | 2.58 sec: 1.10x faster                                                    |
| json_loads               | 31.2 us                                                | 29.0 us: 1.07x faster                                                     |
| sqlite_synth             | 3.02 us                                                | 2.84 us: 1.07x faster                                                     |
| json                     | 5.69 ms                                                | 5.43 ms: 1.05x faster                                                     |
| pidigits                 | 191 ms                                                 | 188 ms: 1.01x faster                                                      |
| regex_dna                | 227 ms                                                 | 226 ms: 1.00x faster                                                      |
| asyncio_websockets       | 559 ms                                                 | 567 ms: 1.02x slower                                                      |
| unpickle                 | 14.4 us                                                | 14.9 us: 1.03x slower                                                     |
| async_generators         | 444 ms                                                 | 462 ms: 1.04x slower                                                      |
| pickle_list              | 5.08 us                                                | 5.34 us: 1.05x slower                                                     |
| gc_traversal             | 3.62 ms                                                | 3.84 ms: 1.06x slower                                                     |
| create_gc_cycles         | 1.62 ms                                                | 1.80 ms: 1.11x slower                                                     |
| telco                    | 7.27 ms                                                | 8.14 ms: 1.12x slower                                                     |
| pickle                   | 10.7 us                                                | 12.1 us: 1.14x slower                                                     |
| coverage                 | 79.4 ms                                                | 92.9 ms: 1.17x slower                                                     |
| pickle_dict              | 29.6 us                                                | 36.3 us: 1.23x slower                                                     |
| python_startup_no_site   | 5.93 ms                                                | 7.60 ms: 1.28x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.33x faster                                                              |

Benchmark hidden because not significant (3): bench_mp_pool, unpickle_list, regex_effbot
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240606-3.14.0a0-ea1e85d-JIT/bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-ea1e85d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.21x