# Results vs. 3.10.4

- fork: efimov-mikhail
- ref: crash_fix_generators
- machine: linux-x86_64
- commit hash: b94d5c4
- commit date: 2024-10-15
- overall geometric mean: 1.400x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-linux-x86_64-efimov%2dmikhail-crash_fix_generators-3.14.0a0-b94d5c4 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 253 ms: 1.38x faster                                                            |
| docutils       | 3.30 sec                                               | 2.62 sec: 1.26x faster                                                          |
| html5lib       | 88.9 ms                                                | 61.1 ms: 1.45x faster                                                           |
| tornado_http   | 136 ms                                                 | 90.6 ms: 1.51x faster                                                           |
| Geometric mean | (ref)                                                  | 1.40x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-linux-x86_64-efimov%2dmikhail-crash_fix_generators-3.14.0a0-b94d5c4 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 89.4 ms: 1.72x faster                                                           |
| float          | 117 ms                                                 | 78.0 ms: 1.50x faster                                                           |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                  | 1.38x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-linux-x86_64-efimov%2dmikhail-crash_fix_generators-3.14.0a0-b94d5c4 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.47x faster                                                            |
| regex_v8       | 27.8 ms                                                | 24.4 ms: 1.14x faster                                                           |
| regex_dna      | 227 ms                                                 | 212 ms: 1.07x faster                                                            |
| regex_effbot   | 3.63 ms                                                | 3.49 ms: 1.04x faster                                                           |
| Geometric mean | (ref)                                                  | 1.17x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-linux-x86_64-efimov%2dmikhail-crash_fix_generators-3.14.0a0-b94d5c4 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 308 us: 1.57x faster                                                            |
| unpickle_pure_python | 331 us                                                 | 217 us: 1.52x faster                                                            |
| tomli_loads          | 3.14 sec                                               | 2.10 sec: 1.49x faster                                                          |
| xml_etree_process    | 79.1 ms                                                | 59.3 ms: 1.33x faster                                                           |
| json_dumps           | 14.2 ms                                                | 11.2 ms: 1.26x faster                                                           |
| json_loads           | 31.2 us                                                | 26.8 us: 1.16x faster                                                           |
| xml_etree_generate   | 99.4 ms                                                | 85.5 ms: 1.16x faster                                                           |
| xml_etree_iterparse  | 115 ms                                                 | 104 ms: 1.12x faster                                                            |
| xml_etree_parse      | 168 ms                                                 | 156 ms: 1.08x faster                                                            |
| pickle_list          | 5.08 us                                                | 5.06 us: 1.00x faster                                                           |
| unpickle             | 14.4 us                                                | 14.7 us: 1.02x slower                                                           |
| pickle               | 10.7 us                                                | 11.9 us: 1.12x slower                                                           |
| pickle_dict          | 29.6 us                                                | 35.0 us: 1.18x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                                    |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-linux-x86_64-efimov%2dmikhail-crash_fix_generators-3.14.0a0-b94d5c4 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.38x faster                                                           |
| python_startup_no_site | 5.93 ms                                                | 7.03 ms: 1.18x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-linux-x86_64-efimov%2dmikhail-crash_fix_generators-3.14.0a0-b94d5c4 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.3 ms: 1.45x faster                                                           |
| django_template | 48.2 ms                                                | 33.8 ms: 1.43x faster                                                           |
| genshi_text     | 31.8 ms                                                | 22.8 ms: 1.40x faster                                                           |
| genshi_xml      | 66.0 ms                                                | 50.0 ms: 1.32x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-linux-x86_64-efimov%2dmikhail-crash_fix_generators-3.14.0a0-b94d5c4 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 161 us: 3.38x faster                                                            |
| generators               | 80.1 ms                                                | 27.8 ms: 2.88x faster                                                           |
| deltablue                | 7.91 ms                                                | 3.27 ms: 2.42x faster                                                           |
| go                       | 240 ms                                                 | 120 ms: 2.01x faster                                                            |
| asyncio_tcp              | 922 ms                                                 | 480 ms: 1.92x faster                                                            |
| chaos                    | 115 ms                                                 | 60.9 ms: 1.90x faster                                                           |
| raytrace                 | 507 ms                                                 | 268 ms: 1.89x faster                                                            |
| deepcopy_memo            | 58.5 us                                                | 31.2 us: 1.88x faster                                                           |
| logging_silent           | 190 ns                                                 | 104 ns: 1.83x faster                                                            |
| richards_super           | 94.7 ms                                                | 52.1 ms: 1.82x faster                                                           |
| deepcopy                 | 479 us                                                 | 264 us: 1.82x faster                                                            |
| crypto_pyaes             | 128 ms                                                 | 73.2 ms: 1.75x faster                                                           |
| scimark_monte_carlo      | 118 ms                                                 | 67.8 ms: 1.74x faster                                                           |
| pylint                   | 551 ms                                                 | 318 ms: 1.73x faster                                                            |
| scimark_sor              | 220 ms                                                 | 127 ms: 1.73x faster                                                            |
| richards                 | 79.3 ms                                                | 45.9 ms: 1.73x faster                                                           |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                                           |
| nbody                    | 154 ms                                                 | 89.4 ms: 1.72x faster                                                           |
| sqlglot_parse            | 2.17 ms                                                | 1.30 ms: 1.67x faster                                                           |
| hexiom                   | 10.4 ms                                                | 6.31 ms: 1.65x faster                                                           |
| sqlglot_transpile        | 2.57 ms                                                | 1.60 ms: 1.61x faster                                                           |
| pickle_pure_python       | 484 us                                                 | 308 us: 1.57x faster                                                            |
| pyflate                  | 716 ms                                                 | 457 ms: 1.57x faster                                                            |
| deepcopy_reduce          | 4.17 us                                                | 2.70 us: 1.55x faster                                                           |
| scimark_lu               | 176 ms                                                 | 115 ms: 1.54x faster                                                            |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.52x faster                                                            |
| tornado_http             | 136 ms                                                 | 90.6 ms: 1.51x faster                                                           |
| float                    | 117 ms                                                 | 78.0 ms: 1.50x faster                                                           |
| unpack_sequence          | 60.0 ns                                                | 40.0 ns: 1.50x faster                                                           |
| logging_simple           | 8.30 us                                                | 5.55 us: 1.50x faster                                                           |
| tomli_loads              | 3.14 sec                                               | 2.10 sec: 1.49x faster                                                          |
| regex_compile            | 188 ms                                                 | 129 ms: 1.47x faster                                                            |
| coroutines               | 35.1 ms                                                | 24.0 ms: 1.46x faster                                                           |
| html5lib                 | 88.9 ms                                                | 61.1 ms: 1.45x faster                                                           |
| logging_format           | 9.09 us                                                | 6.25 us: 1.45x faster                                                           |
| spectral_norm            | 170 ms                                                 | 117 ms: 1.45x faster                                                            |
| mako                     | 16.3 ms                                                | 11.3 ms: 1.45x faster                                                           |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.79 sec: 1.44x faster                                                          |
| django_template          | 48.2 ms                                                | 33.8 ms: 1.43x faster                                                           |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.42x faster                                                          |
| pprint_safe_repr         | 1.02 sec                                               | 720 ms: 1.41x faster                                                            |
| genshi_text              | 31.8 ms                                                | 22.8 ms: 1.40x faster                                                           |
| thrift                   | 1.07 ms                                                | 770 us: 1.39x faster                                                            |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.38x faster                                                           |
| 2to3                     | 348 ms                                                 | 253 ms: 1.38x faster                                                            |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.70 ms: 1.38x faster                                                           |
| sqlglot_normalize        | 143 ms                                                 | 105 ms: 1.36x faster                                                            |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.35x faster                                                          |
| xml_etree_process        | 79.1 ms                                                | 59.3 ms: 1.33x faster                                                           |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.33x faster                                                            |
| fannkuch                 | 532 ms                                                 | 401 ms: 1.32x faster                                                            |
| genshi_xml               | 66.0 ms                                                | 50.0 ms: 1.32x faster                                                           |
| nqueens                  | 106 ms                                                 | 80.5 ms: 1.32x faster                                                           |
| dulwich_log              | 84.3 ms                                                | 64.7 ms: 1.30x faster                                                           |
| sqlglot_optimize         | 69.2 ms                                                | 53.1 ms: 1.30x faster                                                           |
| sympy_integrate          | 25.8 ms                                                | 19.8 ms: 1.30x faster                                                           |
| scimark_fft              | 466 ms                                                 | 360 ms: 1.30x faster                                                            |
| sympy_str                | 346 ms                                                 | 268 ms: 1.29x faster                                                            |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.29x faster                                                           |
| json_dumps               | 14.2 ms                                                | 11.2 ms: 1.26x faster                                                           |
| docutils                 | 3.30 sec                                               | 2.62 sec: 1.26x faster                                                          |
| sympy_expand             | 566 ms                                                 | 458 ms: 1.23x faster                                                            |
| bench_thread_pool        | 986 us                                                 | 837 us: 1.18x faster                                                            |
| json_loads               | 31.2 us                                                | 26.8 us: 1.16x faster                                                           |
| xml_etree_generate       | 99.4 ms                                                | 85.5 ms: 1.16x faster                                                           |
| mdp                      | 2.85 sec                                               | 2.49 sec: 1.14x faster                                                          |
| regex_v8                 | 27.8 ms                                                | 24.4 ms: 1.14x faster                                                           |
| meteor_contest           | 120 ms                                                 | 105 ms: 1.13x faster                                                            |
| xml_etree_iterparse      | 115 ms                                                 | 104 ms: 1.12x faster                                                            |
| json                     | 5.69 ms                                                | 5.12 ms: 1.11x faster                                                           |
| xml_etree_parse          | 168 ms                                                 | 156 ms: 1.08x faster                                                            |
| regex_dna                | 227 ms                                                 | 212 ms: 1.07x faster                                                            |
| sqlite_synth             | 3.02 us                                                | 2.87 us: 1.05x faster                                                           |
| regex_effbot             | 3.63 ms                                                | 3.49 ms: 1.04x faster                                                           |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                            |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                            |
| async_generators         | 444 ms                                                 | 440 ms: 1.01x faster                                                            |
| pickle_list              | 5.08 us                                                | 5.06 us: 1.00x faster                                                           |
| unpickle                 | 14.4 us                                                | 14.7 us: 1.02x slower                                                           |
| coverage                 | 79.4 ms                                                | 84.2 ms: 1.06x slower                                                           |
| telco                    | 7.27 ms                                                | 7.98 ms: 1.10x slower                                                           |
| create_gc_cycles         | 1.62 ms                                                | 1.79 ms: 1.10x slower                                                           |
| gc_traversal             | 3.62 ms                                                | 4.02 ms: 1.11x slower                                                           |
| pickle                   | 10.7 us                                                | 11.9 us: 1.12x slower                                                           |
| pickle_dict              | 29.6 us                                                | 35.0 us: 1.18x slower                                                           |
| python_startup_no_site   | 5.93 ms                                                | 7.03 ms: 1.18x slower                                                           |
| bench_mp_pool            | 24.0 ms                                                | 56.0 ms: 2.33x slower                                                           |
| Geometric mean           | (ref)                                                  | 1.36x faster                                                                    |

Benchmark hidden because not significant (1): unpickle_list
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of results/bm-20241015-3.14.0a0-b94d5c4/bm-20241015-linux-x86_64-efimov%2dmikhail-crash_fix_generators-3.14.0a0-b94d5c4.json: bpe_tokeniser

- Geometric mean (including insignificant results): 1.400x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.14x