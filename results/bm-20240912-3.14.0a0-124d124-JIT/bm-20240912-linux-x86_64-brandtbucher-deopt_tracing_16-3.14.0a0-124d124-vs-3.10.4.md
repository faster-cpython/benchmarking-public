# Results vs. 3.10.4

- fork: brandtbucher
- ref: deopt_tracing_16
- machine: linux-x86_64
- commit hash: 124d124
- commit date: 2024-09-12
- overall geometric mean: 1.37x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.23x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 283 ms: 1.23x faster                                                    |
| docutils       | 3.30 sec                                               | 2.97 sec: 1.11x faster                                                  |
| html5lib       | 88.9 ms                                                | 65.1 ms: 1.37x faster                                                   |
| tornado_http   | 136 ms                                                 | 94.7 ms: 1.44x faster                                                   |
| Geometric mean | (ref)                                                  | 1.28x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 314 ms: 2.32x faster                                                    |
| async_tree_memoization  | 870 ms                                                 | 396 ms: 2.20x faster                                                    |
| async_tree_io           | 1.77 sec                                               | 885 ms: 2.00x faster                                                    |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 566 ms: 1.80x faster                                                    |
| Geometric mean          | (ref)                                                  | 2.07x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 81.1 ms: 1.89x faster                                                   |
| float          | 117 ms                                                 | 69.4 ms: 1.69x faster                                                   |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                  | 1.49x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 144 ms: 1.31x faster                                                    |
| regex_v8       | 27.8 ms                                                | 24.0 ms: 1.16x faster                                                   |
| regex_dna      | 227 ms                                                 | 221 ms: 1.03x faster                                                    |
| regex_effbot   | 3.63 ms                                                | 3.78 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                  | 1.10x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.94 sec: 1.62x faster                                                  |
| pickle_pure_python   | 484 us                                                 | 313 us: 1.55x faster                                                    |
| unpickle_pure_python | 331 us                                                 | 217 us: 1.53x faster                                                    |
| xml_etree_process    | 79.1 ms                                                | 54.5 ms: 1.45x faster                                                   |
| json_dumps           | 14.2 ms                                                | 10.1 ms: 1.40x faster                                                   |
| xml_etree_generate   | 99.4 ms                                                | 77.6 ms: 1.28x faster                                                   |
| xml_etree_iterparse  | 115 ms                                                 | 98.7 ms: 1.17x faster                                                   |
| xml_etree_parse      | 168 ms                                                 | 145 ms: 1.16x faster                                                    |
| json_loads           | 31.2 us                                                | 27.4 us: 1.14x faster                                                   |
| unpickle_list        | 5.20 us                                                | 5.12 us: 1.02x faster                                                   |
| unpickle             | 14.4 us                                                | 14.7 us: 1.03x slower                                                   |
| pickle               | 10.7 us                                                | 11.8 us: 1.11x slower                                                   |
| pickle_dict          | 29.6 us                                                | 33.8 us: 1.14x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.20x faster                                                            |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                   |
| python_startup_no_site | 5.93 ms                                                | 7.02 ms: 1.18x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.71 ms: 1.68x faster                                                   |
| django_template | 48.2 ms                                                | 37.4 ms: 1.29x faster                                                   |
| genshi_text     | 31.8 ms                                                | 25.7 ms: 1.24x faster                                                   |
| genshi_xml      | 66.0 ms                                                | 59.8 ms: 1.10x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.31x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 165 us: 3.31x faster                                                    |
| generators               | 80.1 ms                                                | 33.6 ms: 2.38x faster                                                   |
| async_tree_none          | 728 ms                                                 | 314 ms: 2.32x faster                                                    |
| async_tree_memoization   | 870 ms                                                 | 396 ms: 2.20x faster                                                    |
| deltablue                | 7.91 ms                                                | 3.66 ms: 2.16x faster                                                   |
| deepcopy_memo            | 58.5 us                                                | 27.1 us: 2.16x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 885 ms: 2.00x faster                                                    |
| chaos                    | 115 ms                                                 | 58.3 ms: 1.98x faster                                                   |
| crypto_pyaes             | 128 ms                                                 | 65.9 ms: 1.94x faster                                                   |
| nbody                    | 154 ms                                                 | 81.1 ms: 1.89x faster                                                   |
| scimark_sor              | 220 ms                                                 | 117 ms: 1.88x faster                                                    |
| scimark_monte_carlo      | 118 ms                                                 | 63.0 ms: 1.88x faster                                                   |
| richards_super           | 94.7 ms                                                | 51.1 ms: 1.85x faster                                                   |
| logging_silent           | 190 ns                                                 | 102 ns: 1.85x faster                                                    |
| asyncio_tcp              | 922 ms                                                 | 498 ms: 1.85x faster                                                    |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 566 ms: 1.80x faster                                                    |
| deepcopy                 | 479 us                                                 | 268 us: 1.79x faster                                                    |
| raytrace                 | 507 ms                                                 | 286 ms: 1.77x faster                                                    |
| go                       | 240 ms                                                 | 137 ms: 1.75x faster                                                    |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                                   |
| richards                 | 79.3 ms                                                | 46.7 ms: 1.70x faster                                                   |
| float                    | 117 ms                                                 | 69.4 ms: 1.69x faster                                                   |
| mako                     | 16.3 ms                                                | 9.71 ms: 1.68x faster                                                   |
| spectral_norm            | 170 ms                                                 | 102 ms: 1.66x faster                                                    |
| pyflate                  | 716 ms                                                 | 437 ms: 1.64x faster                                                    |
| tomli_loads              | 3.14 sec                                               | 1.94 sec: 1.62x faster                                                  |
| scimark_lu               | 176 ms                                                 | 109 ms: 1.62x faster                                                    |
| sqlglot_parse            | 2.17 ms                                                | 1.37 ms: 1.59x faster                                                   |
| deepcopy_reduce          | 4.17 us                                                | 2.65 us: 1.57x faster                                                   |
| coroutines               | 35.1 ms                                                | 22.7 ms: 1.55x faster                                                   |
| pickle_pure_python       | 484 us                                                 | 313 us: 1.55x faster                                                    |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.53x faster                                                    |
| scimark_fft              | 466 ms                                                 | 306 ms: 1.52x faster                                                    |
| logging_simple           | 8.30 us                                                | 5.52 us: 1.50x faster                                                   |
| logging_format           | 9.09 us                                                | 6.05 us: 1.50x faster                                                   |
| sqlglot_transpile        | 2.57 ms                                                | 1.71 ms: 1.50x faster                                                   |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.33 ms: 1.49x faster                                                   |
| hexiom                   | 10.4 ms                                                | 7.00 ms: 1.49x faster                                                   |
| xml_etree_process        | 79.1 ms                                                | 54.5 ms: 1.45x faster                                                   |
| tornado_http             | 136 ms                                                 | 94.7 ms: 1.44x faster                                                   |
| pylint                   | 551 ms                                                 | 385 ms: 1.43x faster                                                    |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                                  |
| fannkuch                 | 532 ms                                                 | 375 ms: 1.42x faster                                                    |
| json_dumps               | 14.2 ms                                                | 10.1 ms: 1.40x faster                                                   |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                   |
| pprint_safe_repr         | 1.02 sec                                               | 745 ms: 1.37x faster                                                    |
| html5lib                 | 88.9 ms                                                | 65.1 ms: 1.37x faster                                                   |
| thrift                   | 1.07 ms                                                | 791 us: 1.36x faster                                                    |
| pprint_pformat           | 2.10 sec                                               | 1.55 sec: 1.35x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.19 sec: 1.33x faster                                                  |
| regex_compile            | 188 ms                                                 | 144 ms: 1.31x faster                                                    |
| django_template          | 48.2 ms                                                | 37.4 ms: 1.29x faster                                                   |
| xml_etree_generate       | 99.4 ms                                                | 77.6 ms: 1.28x faster                                                   |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.28x faster                                                   |
| dulwich_log              | 84.3 ms                                                | 68.0 ms: 1.24x faster                                                   |
| genshi_text              | 31.8 ms                                                | 25.7 ms: 1.24x faster                                                   |
| 2to3                     | 348 ms                                                 | 283 ms: 1.23x faster                                                    |
| nqueens                  | 106 ms                                                 | 86.5 ms: 1.22x faster                                                   |
| bench_thread_pool        | 986 us                                                 | 833 us: 1.18x faster                                                    |
| sqlglot_normalize        | 143 ms                                                 | 122 ms: 1.17x faster                                                    |
| sqlglot_optimize         | 69.2 ms                                                | 59.1 ms: 1.17x faster                                                   |
| xml_etree_iterparse      | 115 ms                                                 | 98.7 ms: 1.17x faster                                                   |
| xml_etree_parse          | 168 ms                                                 | 145 ms: 1.16x faster                                                    |
| regex_v8                 | 27.8 ms                                                | 24.0 ms: 1.16x faster                                                   |
| json_loads               | 31.2 us                                                | 27.4 us: 1.14x faster                                                   |
| meteor_contest           | 120 ms                                                 | 105 ms: 1.14x faster                                                    |
| sympy_str                | 346 ms                                                 | 307 ms: 1.13x faster                                                    |
| mdp                      | 2.85 sec                                               | 2.54 sec: 1.12x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.97 sec: 1.11x faster                                                  |
| sympy_sum                | 196 ms                                                 | 177 ms: 1.11x faster                                                    |
| json                     | 5.69 ms                                                | 5.14 ms: 1.11x faster                                                   |
| genshi_xml               | 66.0 ms                                                | 59.8 ms: 1.10x faster                                                   |
| sympy_integrate          | 25.8 ms                                                | 23.4 ms: 1.10x faster                                                   |
| sqlite_synth             | 3.02 us                                                | 2.75 us: 1.10x faster                                                   |
| sympy_expand             | 566 ms                                                 | 521 ms: 1.09x faster                                                    |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                    |
| gc_traversal             | 3.62 ms                                                | 3.53 ms: 1.03x faster                                                   |
| regex_dna                | 227 ms                                                 | 221 ms: 1.03x faster                                                    |
| unpickle_list            | 5.20 us                                                | 5.12 us: 1.02x faster                                                   |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                                    |
| unpickle                 | 14.4 us                                                | 14.7 us: 1.03x slower                                                   |
| async_generators         | 444 ms                                                 | 455 ms: 1.03x slower                                                    |
| regex_effbot             | 3.63 ms                                                | 3.78 ms: 1.04x slower                                                   |
| coverage                 | 79.4 ms                                                | 84.6 ms: 1.07x slower                                                   |
| telco                    | 7.27 ms                                                | 7.86 ms: 1.08x slower                                                   |
| create_gc_cycles         | 1.62 ms                                                | 1.76 ms: 1.08x slower                                                   |
| pickle                   | 10.7 us                                                | 11.8 us: 1.11x slower                                                   |
| pickle_dict              | 29.6 us                                                | 33.8 us: 1.14x slower                                                   |
| python_startup_no_site   | 5.93 ms                                                | 7.02 ms: 1.18x slower                                                   |
| unpack_sequence          | 60.0 ns                                                | 110 ns: 1.83x slower                                                    |
| Geometric mean           | (ref)                                                  | 1.37x faster                                                            |

Benchmark hidden because not significant (2): bench_mp_pool, pickle_list
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240912-3.14.0a0-124d124-JIT/bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.23x