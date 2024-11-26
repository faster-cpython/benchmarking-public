# Results vs. 3.10.4

- fork: faster-cpython
- ref: fix_decref_and_reuse
- machine: linux-x86_64
- commit hash: 07df2d0
- commit date: 2024-10-14
- overall geometric mean: 1.391x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241014-linux-x86_64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 255 ms: 1.37x faster                                                            |
| docutils       | 3.30 sec                                               | 2.62 sec: 1.26x faster                                                          |
| html5lib       | 88.9 ms                                                | 62.1 ms: 1.43x faster                                                           |
| tornado_http   | 136 ms                                                 | 90.4 ms: 1.51x faster                                                           |
| Geometric mean | (ref)                                                  | 1.39x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241014-linux-x86_64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 94.2 ms: 1.63x faster                                                           |
| float          | 117 ms                                                 | 78.3 ms: 1.50x faster                                                           |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241014-linux-x86_64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.46x faster                                                            |
| regex_v8       | 27.8 ms                                                | 25.0 ms: 1.11x faster                                                           |
| regex_dna      | 227 ms                                                 | 221 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                  | 1.14x faster                                                                    |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241014-linux-x86_64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 313 us: 1.55x faster                                                            |
| unpickle_pure_python | 331 us                                                 | 222 us: 1.49x faster                                                            |
| tomli_loads          | 3.14 sec                                               | 2.13 sec: 1.47x faster                                                          |
| xml_etree_process    | 79.1 ms                                                | 59.8 ms: 1.32x faster                                                           |
| json_dumps           | 14.2 ms                                                | 11.2 ms: 1.26x faster                                                           |
| json_loads           | 31.2 us                                                | 26.8 us: 1.16x faster                                                           |
| xml_etree_generate   | 99.4 ms                                                | 86.3 ms: 1.15x faster                                                           |
| xml_etree_iterparse  | 115 ms                                                 | 105 ms: 1.10x faster                                                            |
| xml_etree_parse      | 168 ms                                                 | 157 ms: 1.07x faster                                                            |
| pickle_list          | 5.08 us                                                | 5.11 us: 1.01x slower                                                           |
| unpickle             | 14.4 us                                                | 14.9 us: 1.03x slower                                                           |
| unpickle_list        | 5.20 us                                                | 5.43 us: 1.04x slower                                                           |
| pickle               | 10.7 us                                                | 11.9 us: 1.11x slower                                                           |
| pickle_dict          | 29.6 us                                                | 35.0 us: 1.18x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.14x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241014-linux-x86_64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                           |
| python_startup_no_site | 5.93 ms                                                | 7.02 ms: 1.18x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241014-linux-x86_64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.4 ms: 1.43x faster                                                           |
| django_template | 48.2 ms                                                | 34.1 ms: 1.41x faster                                                           |
| genshi_text     | 31.8 ms                                                | 23.0 ms: 1.39x faster                                                           |
| genshi_xml      | 66.0 ms                                                | 51.9 ms: 1.27x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.37x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241014-linux-x86_64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 160 us: 3.41x faster                                                            |
| generators               | 80.1 ms                                                | 28.0 ms: 2.86x faster                                                           |
| deltablue                | 7.91 ms                                                | 3.31 ms: 2.39x faster                                                           |
| go                       | 240 ms                                                 | 122 ms: 1.97x faster                                                            |
| asyncio_tcp              | 922 ms                                                 | 480 ms: 1.92x faster                                                            |
| chaos                    | 115 ms                                                 | 61.0 ms: 1.89x faster                                                           |
| deepcopy_memo            | 58.5 us                                                | 31.2 us: 1.87x faster                                                           |
| raytrace                 | 507 ms                                                 | 271 ms: 1.87x faster                                                            |
| deepcopy                 | 479 us                                                 | 261 us: 1.84x faster                                                            |
| richards_super           | 94.7 ms                                                | 53.0 ms: 1.79x faster                                                           |
| logging_silent           | 190 ns                                                 | 109 ns: 1.74x faster                                                            |
| pylint                   | 551 ms                                                 | 318 ms: 1.74x faster                                                            |
| scimark_sor              | 220 ms                                                 | 127 ms: 1.73x faster                                                            |
| crypto_pyaes             | 128 ms                                                 | 74.1 ms: 1.73x faster                                                           |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.71x faster                                                           |
| scimark_monte_carlo      | 118 ms                                                 | 69.7 ms: 1.70x faster                                                           |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.68x faster                                                           |
| richards                 | 79.3 ms                                                | 47.3 ms: 1.68x faster                                                           |
| nbody                    | 154 ms                                                 | 94.2 ms: 1.63x faster                                                           |
| hexiom                   | 10.4 ms                                                | 6.38 ms: 1.63x faster                                                           |
| sqlglot_transpile        | 2.57 ms                                                | 1.59 ms: 1.61x faster                                                           |
| deepcopy_reduce          | 4.17 us                                                | 2.68 us: 1.56x faster                                                           |
| pyflate                  | 716 ms                                                 | 462 ms: 1.55x faster                                                            |
| pickle_pure_python       | 484 us                                                 | 313 us: 1.55x faster                                                            |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.52x faster                                                            |
| tornado_http             | 136 ms                                                 | 90.4 ms: 1.51x faster                                                           |
| coroutines               | 35.1 ms                                                | 23.4 ms: 1.50x faster                                                           |
| float                    | 117 ms                                                 | 78.3 ms: 1.50x faster                                                           |
| spectral_norm            | 170 ms                                                 | 114 ms: 1.49x faster                                                            |
| unpickle_pure_python     | 331 us                                                 | 222 us: 1.49x faster                                                            |
| logging_simple           | 8.30 us                                                | 5.62 us: 1.48x faster                                                           |
| tomli_loads              | 3.14 sec                                               | 2.13 sec: 1.47x faster                                                          |
| regex_compile            | 188 ms                                                 | 129 ms: 1.46x faster                                                            |
| logging_format           | 9.09 us                                                | 6.26 us: 1.45x faster                                                           |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.79 sec: 1.44x faster                                                          |
| html5lib                 | 88.9 ms                                                | 62.1 ms: 1.43x faster                                                           |
| mako                     | 16.3 ms                                                | 11.4 ms: 1.43x faster                                                           |
| django_template          | 48.2 ms                                                | 34.1 ms: 1.41x faster                                                           |
| pprint_pformat           | 2.10 sec                                               | 1.49 sec: 1.41x faster                                                          |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.40x faster                                                          |
| pprint_safe_repr         | 1.02 sec                                               | 729 ms: 1.40x faster                                                            |
| genshi_text              | 31.8 ms                                                | 23.0 ms: 1.39x faster                                                           |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                           |
| thrift                   | 1.07 ms                                                | 779 us: 1.38x faster                                                            |
| 2to3                     | 348 ms                                                 | 255 ms: 1.37x faster                                                            |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.76 ms: 1.36x faster                                                           |
| sqlglot_normalize        | 143 ms                                                 | 106 ms: 1.34x faster                                                            |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.34x faster                                                            |
| xml_etree_process        | 79.1 ms                                                | 59.8 ms: 1.32x faster                                                           |
| dulwich_log              | 84.3 ms                                                | 64.2 ms: 1.31x faster                                                           |
| sympy_integrate          | 25.8 ms                                                | 19.8 ms: 1.30x faster                                                           |
| nqueens                  | 106 ms                                                 | 81.4 ms: 1.30x faster                                                           |
| sqlglot_optimize         | 69.2 ms                                                | 53.4 ms: 1.30x faster                                                           |
| fannkuch                 | 532 ms                                                 | 411 ms: 1.29x faster                                                            |
| sympy_str                | 346 ms                                                 | 268 ms: 1.29x faster                                                            |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                                           |
| genshi_xml               | 66.0 ms                                                | 51.9 ms: 1.27x faster                                                           |
| scimark_fft              | 466 ms                                                 | 367 ms: 1.27x faster                                                            |
| unpack_sequence          | 60.0 ns                                                | 47.4 ns: 1.27x faster                                                           |
| json_dumps               | 14.2 ms                                                | 11.2 ms: 1.26x faster                                                           |
| docutils                 | 3.30 sec                                               | 2.62 sec: 1.26x faster                                                          |
| sympy_expand             | 566 ms                                                 | 455 ms: 1.24x faster                                                            |
| bench_thread_pool        | 986 us                                                 | 838 us: 1.18x faster                                                            |
| json_loads               | 31.2 us                                                | 26.8 us: 1.16x faster                                                           |
| xml_etree_generate       | 99.4 ms                                                | 86.3 ms: 1.15x faster                                                           |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.12x faster                                                            |
| mdp                      | 2.85 sec                                               | 2.53 sec: 1.12x faster                                                          |
| json                     | 5.69 ms                                                | 5.09 ms: 1.12x faster                                                           |
| regex_v8                 | 27.8 ms                                                | 25.0 ms: 1.11x faster                                                           |
| xml_etree_iterparse      | 115 ms                                                 | 105 ms: 1.10x faster                                                            |
| xml_etree_parse          | 168 ms                                                 | 157 ms: 1.07x faster                                                            |
| sqlite_synth             | 3.02 us                                                | 2.85 us: 1.06x faster                                                           |
| regex_dna                | 227 ms                                                 | 221 ms: 1.02x faster                                                            |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                                            |
| async_generators         | 444 ms                                                 | 438 ms: 1.01x faster                                                            |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                                            |
| pickle_list              | 5.08 us                                                | 5.11 us: 1.01x slower                                                           |
| unpickle                 | 14.4 us                                                | 14.9 us: 1.03x slower                                                           |
| unpickle_list            | 5.20 us                                                | 5.43 us: 1.04x slower                                                           |
| coverage                 | 79.4 ms                                                | 85.0 ms: 1.07x slower                                                           |
| gc_traversal             | 3.62 ms                                                | 3.89 ms: 1.07x slower                                                           |
| create_gc_cycles         | 1.62 ms                                                | 1.78 ms: 1.10x slower                                                           |
| telco                    | 7.27 ms                                                | 8.00 ms: 1.10x slower                                                           |
| pickle                   | 10.7 us                                                | 11.9 us: 1.11x slower                                                           |
| pickle_dict              | 29.6 us                                                | 35.0 us: 1.18x slower                                                           |
| python_startup_no_site   | 5.93 ms                                                | 7.02 ms: 1.18x slower                                                           |
| bench_mp_pool            | 24.0 ms                                                | 56.2 ms: 2.34x slower                                                           |
| Geometric mean           | (ref)                                                  | 1.35x faster                                                                    |

Benchmark hidden because not significant (1): regex_effbot
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of results/bm-20241014-3.14.0a0-07df2d0/bm-20241014-linux-x86_64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0.json: bpe_tokeniser

- Geometric mean (including insignificant results): 1.391x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.29x

# Memory
- memory change: 1.14x