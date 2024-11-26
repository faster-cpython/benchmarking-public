# Results vs. 3.10.4

- fork: brandtbucher
- ref: deopt_tracing_32
- machine: linux-x86_64
- commit hash: a7a7e7f
- commit date: 2024-09-13
- overall geometric mean: 1.421x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240913-linux-x86_64-brandtbucher-deopt_tracing_32-3.14.0a0-a7a7e7f |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 279 ms: 1.25x faster                                                    |
| docutils       | 3.30 sec                                               | 2.95 sec: 1.12x faster                                                  |
| html5lib       | 88.9 ms                                                | 64.7 ms: 1.37x faster                                                   |
| tornado_http   | 136 ms                                                 | 94.6 ms: 1.44x faster                                                   |
| Geometric mean | (ref)                                                  | 1.29x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240913-linux-x86_64-brandtbucher-deopt_tracing_32-3.14.0a0-a7a7e7f |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 315 ms: 2.31x faster                                                    |
| async_tree_memoization  | 870 ms                                                 | 394 ms: 2.21x faster                                                    |
| async_tree_io           | 1.77 sec                                               | 852 ms: 2.08x faster                                                    |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 565 ms: 1.80x faster                                                    |
| Geometric mean          | (ref)                                                  | 2.09x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240913-linux-x86_64-brandtbucher-deopt_tracing_32-3.14.0a0-a7a7e7f |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 81.9 ms: 1.87x faster                                                   |
| float          | 117 ms                                                 | 69.4 ms: 1.69x faster                                                   |
| pidigits       | 191 ms                                                 | 185 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                  | 1.48x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240913-linux-x86_64-brandtbucher-deopt_tracing_32-3.14.0a0-a7a7e7f |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 142 ms: 1.33x faster                                                    |
| regex_v8       | 27.8 ms                                                | 25.1 ms: 1.10x faster                                                   |
| regex_dna      | 227 ms                                                 | 221 ms: 1.03x faster                                                    |
| regex_effbot   | 3.63 ms                                                | 3.73 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                  | 1.10x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240913-linux-x86_64-brandtbucher-deopt_tracing_32-3.14.0a0-a7a7e7f |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.92 sec: 1.64x faster                                                  |
| pickle_pure_python   | 484 us                                                 | 304 us: 1.60x faster                                                    |
| unpickle_pure_python | 331 us                                                 | 213 us: 1.55x faster                                                    |
| xml_etree_process    | 79.1 ms                                                | 54.7 ms: 1.45x faster                                                   |
| json_dumps           | 14.2 ms                                                | 10.1 ms: 1.41x faster                                                   |
| xml_etree_generate   | 99.4 ms                                                | 77.5 ms: 1.28x faster                                                   |
| xml_etree_iterparse  | 115 ms                                                 | 99.7 ms: 1.16x faster                                                   |
| json_loads           | 31.2 us                                                | 27.1 us: 1.15x faster                                                   |
| xml_etree_parse      | 168 ms                                                 | 147 ms: 1.15x faster                                                    |
| pickle_list          | 5.08 us                                                | 5.04 us: 1.01x faster                                                   |
| unpickle_list        | 5.20 us                                                | 5.30 us: 1.02x slower                                                   |
| unpickle             | 14.4 us                                                | 15.2 us: 1.05x slower                                                   |
| pickle               | 10.7 us                                                | 11.3 us: 1.06x slower                                                   |
| pickle_dict          | 29.6 us                                                | 33.2 us: 1.12x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.20x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240913-linux-x86_64-brandtbucher-deopt_tracing_32-3.14.0a0-a7a7e7f |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.38x faster                                                   |
| python_startup_no_site | 5.93 ms                                                | 7.08 ms: 1.19x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240913-linux-x86_64-brandtbucher-deopt_tracing_32-3.14.0a0-a7a7e7f |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.79 ms: 1.67x faster                                                   |
| django_template | 48.2 ms                                                | 35.8 ms: 1.34x faster                                                   |
| genshi_text     | 31.8 ms                                                | 25.1 ms: 1.27x faster                                                   |
| genshi_xml      | 66.0 ms                                                | 59.4 ms: 1.11x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.33x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240913-linux-x86_64-brandtbucher-deopt_tracing_32-3.14.0a0-a7a7e7f |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 161 us: 3.37x faster                                                    |
| generators               | 80.1 ms                                                | 33.2 ms: 2.41x faster                                                   |
| async_tree_none          | 728 ms                                                 | 315 ms: 2.31x faster                                                    |
| deltablue                | 7.91 ms                                                | 3.55 ms: 2.23x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 394 ms: 2.21x faster                                                    |
| deepcopy_memo            | 58.5 us                                                | 27.0 us: 2.17x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 852 ms: 2.08x faster                                                    |
| richards_super           | 94.7 ms                                                | 47.3 ms: 2.00x faster                                                   |
| chaos                    | 115 ms                                                 | 58.5 ms: 1.97x faster                                                   |
| crypto_pyaes             | 128 ms                                                 | 65.3 ms: 1.96x faster                                                   |
| richards                 | 79.3 ms                                                | 41.1 ms: 1.93x faster                                                   |
| scimark_monte_carlo      | 118 ms                                                 | 62.6 ms: 1.89x faster                                                   |
| scimark_sor              | 220 ms                                                 | 117 ms: 1.88x faster                                                    |
| nbody                    | 154 ms                                                 | 81.9 ms: 1.87x faster                                                   |
| logging_silent           | 190 ns                                                 | 102 ns: 1.86x faster                                                    |
| asyncio_tcp              | 922 ms                                                 | 498 ms: 1.85x faster                                                    |
| raytrace                 | 507 ms                                                 | 276 ms: 1.84x faster                                                    |
| deepcopy                 | 479 us                                                 | 264 us: 1.82x faster                                                    |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 565 ms: 1.80x faster                                                    |
| go                       | 240 ms                                                 | 135 ms: 1.78x faster                                                    |
| comprehensions           | 28.8 us                                                | 16.4 us: 1.75x faster                                                   |
| spectral_norm            | 170 ms                                                 | 100 ms: 1.69x faster                                                    |
| float                    | 117 ms                                                 | 69.4 ms: 1.69x faster                                                   |
| mako                     | 16.3 ms                                                | 9.79 ms: 1.67x faster                                                   |
| tomli_loads              | 3.14 sec                                               | 1.92 sec: 1.64x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.35 ms: 1.61x faster                                                   |
| pickle_pure_python       | 484 us                                                 | 304 us: 1.60x faster                                                    |
| deepcopy_reduce          | 4.17 us                                                | 2.62 us: 1.59x faster                                                   |
| scimark_lu               | 176 ms                                                 | 111 ms: 1.58x faster                                                    |
| pyflate                  | 716 ms                                                 | 458 ms: 1.56x faster                                                    |
| unpickle_pure_python     | 331 us                                                 | 213 us: 1.55x faster                                                    |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.21 ms: 1.54x faster                                                   |
| scimark_fft              | 466 ms                                                 | 307 ms: 1.52x faster                                                    |
| hexiom                   | 10.4 ms                                                | 6.89 ms: 1.51x faster                                                   |
| sqlglot_transpile        | 2.57 ms                                                | 1.72 ms: 1.50x faster                                                   |
| logging_format           | 9.09 us                                                | 6.10 us: 1.49x faster                                                   |
| logging_simple           | 8.30 us                                                | 5.58 us: 1.49x faster                                                   |
| pylint                   | 551 ms                                                 | 379 ms: 1.45x faster                                                    |
| xml_etree_process        | 79.1 ms                                                | 54.7 ms: 1.45x faster                                                   |
| tornado_http             | 136 ms                                                 | 94.6 ms: 1.44x faster                                                   |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.42x faster                                                  |
| pprint_safe_repr         | 1.02 sec                                               | 720 ms: 1.41x faster                                                    |
| coroutines               | 35.1 ms                                                | 24.9 ms: 1.41x faster                                                   |
| json_dumps               | 14.2 ms                                                | 10.1 ms: 1.41x faster                                                   |
| fannkuch                 | 532 ms                                                 | 380 ms: 1.40x faster                                                    |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.38x faster                                                   |
| html5lib                 | 88.9 ms                                                | 64.7 ms: 1.37x faster                                                   |
| thrift                   | 1.07 ms                                                | 789 us: 1.36x faster                                                    |
| django_template          | 48.2 ms                                                | 35.8 ms: 1.34x faster                                                   |
| regex_compile            | 188 ms                                                 | 142 ms: 1.33x faster                                                    |
| pycparser                | 1.58 sec                                               | 1.21 sec: 1.30x faster                                                  |
| xml_etree_generate       | 99.4 ms                                                | 77.5 ms: 1.28x faster                                                   |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                                   |
| genshi_text              | 31.8 ms                                                | 25.1 ms: 1.27x faster                                                   |
| dulwich_log              | 84.3 ms                                                | 66.7 ms: 1.26x faster                                                   |
| 2to3                     | 348 ms                                                 | 279 ms: 1.25x faster                                                    |
| nqueens                  | 106 ms                                                 | 84.8 ms: 1.25x faster                                                   |
| sqlglot_normalize        | 143 ms                                                 | 115 ms: 1.25x faster                                                    |
| bench_thread_pool        | 986 us                                                 | 835 us: 1.18x faster                                                    |
| sqlglot_optimize         | 69.2 ms                                                | 59.0 ms: 1.17x faster                                                   |
| xml_etree_iterparse      | 115 ms                                                 | 99.7 ms: 1.16x faster                                                   |
| json_loads               | 31.2 us                                                | 27.1 us: 1.15x faster                                                   |
| json                     | 5.69 ms                                                | 4.95 ms: 1.15x faster                                                   |
| xml_etree_parse          | 168 ms                                                 | 147 ms: 1.15x faster                                                    |
| sympy_str                | 346 ms                                                 | 305 ms: 1.13x faster                                                    |
| mdp                      | 2.85 sec                                               | 2.52 sec: 1.13x faster                                                  |
| sympy_sum                | 196 ms                                                 | 174 ms: 1.13x faster                                                    |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                    |
| sympy_integrate          | 25.8 ms                                                | 23.0 ms: 1.12x faster                                                   |
| docutils                 | 3.30 sec                                               | 2.95 sec: 1.12x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 59.4 ms: 1.11x faster                                                   |
| regex_v8                 | 27.8 ms                                                | 25.1 ms: 1.10x faster                                                   |
| sympy_expand             | 566 ms                                                 | 517 ms: 1.09x faster                                                    |
| sqlite_synth             | 3.02 us                                                | 2.77 us: 1.09x faster                                                   |
| pidigits                 | 191 ms                                                 | 185 ms: 1.03x faster                                                    |
| regex_dna                | 227 ms                                                 | 221 ms: 1.03x faster                                                    |
| pickle_list              | 5.08 us                                                | 5.04 us: 1.01x faster                                                   |
| asyncio_websockets       | 559 ms                                                 | 556 ms: 1.01x faster                                                    |
| gc_traversal             | 3.62 ms                                                | 3.65 ms: 1.01x slower                                                   |
| unpickle_list            | 5.20 us                                                | 5.30 us: 1.02x slower                                                   |
| async_generators         | 444 ms                                                 | 455 ms: 1.02x slower                                                    |
| regex_effbot             | 3.63 ms                                                | 3.73 ms: 1.03x slower                                                   |
| unpickle                 | 14.4 us                                                | 15.2 us: 1.05x slower                                                   |
| pickle                   | 10.7 us                                                | 11.3 us: 1.06x slower                                                   |
| create_gc_cycles         | 1.62 ms                                                | 1.77 ms: 1.09x slower                                                   |
| telco                    | 7.27 ms                                                | 7.93 ms: 1.09x slower                                                   |
| pickle_dict              | 29.6 us                                                | 33.2 us: 1.12x slower                                                   |
| coverage                 | 79.4 ms                                                | 89.6 ms: 1.13x slower                                                   |
| python_startup_no_site   | 5.93 ms                                                | 7.08 ms: 1.19x slower                                                   |
| unpack_sequence          | 60.0 ns                                                | 110 ns: 1.84x slower                                                    |
| Geometric mean           | (ref)                                                  | 1.38x faster                                                            |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240913-3.14.0a0-a7a7e7f-JIT/bm-20240913-linux-x86_64-brandtbucher-deopt_tracing_32-3.14.0a0-a7a7e7f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.421x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.22x