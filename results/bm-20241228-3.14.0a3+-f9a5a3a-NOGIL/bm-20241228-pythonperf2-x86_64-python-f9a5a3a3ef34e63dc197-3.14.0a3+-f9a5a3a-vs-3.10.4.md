# Results vs. 3.10.4

- fork: python
- ref: f9a5a3a3ef34e63dc197
- machine: linux-x86_64
- commit hash: f9a5a3a
- commit date: 2024-12-28
- overall geometric mean: 1.048x faster
- HPT reliability: 99.84%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.52x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 382 ms: 1.09x slower                                                         |
| docutils       | 3.41 sec                                                     | 3.11 sec: 1.10x faster                                                       |
| html5lib       | 94.6 ms                                                      | 93.1 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 774 ms: 2.07x faster                                                         |
| async_tree_none         | 692 ms                                                       | 354 ms: 1.96x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 440 ms: 1.86x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 608 ms: 1.54x faster                                                         |
| Geometric mean          | (ref)                                                        | 1.84x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 271 ms                                                       | 247 ms: 1.10x faster                                                         |
| nbody          | 134 ms                                                       | 130 ms: 1.03x faster                                                         |
| float          | 111 ms                                                       | 109 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 173 ms: 1.10x faster                                                         |
| regex_dna      | 261 ms                                                       | 248 ms: 1.05x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 26.7 ms: 1.02x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.30 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 110 ms                                                       | 93.6 ms: 1.18x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 136 ms: 1.18x faster                                                         |
| json_loads           | 30.3 us                                                      | 26.8 us: 1.13x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.61 sec: 1.12x faster                                                       |
| json_dumps           | 14.5 ms                                                      | 14.2 ms: 1.03x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 74.7 ms: 1.02x faster                                                        |
| unpickle_pure_python | 312 us                                                       | 323 us: 1.04x slower                                                         |
| xml_etree_generate   | 92.3 ms                                                      | 98.6 ms: 1.07x slower                                                        |
| pickle_pure_python   | 455 us                                                       | 506 us: 1.11x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.05x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 12.0 ms: 1.64x slower                                                        |
| python_startup         | 11.5 ms                                                      | 19.2 ms: 1.67x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.65x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 31.4 ms                                                      | 33.0 ms: 1.05x slower                                                        |
| genshi_xml      | 63.3 ms                                                      | 67.6 ms: 1.07x slower                                                        |
| django_template | 50.2 ms                                                      | 53.6 ms: 1.07x slower                                                        |
| mako            | 14.7 ms                                                      | 19.5 ms: 1.32x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.12x slower                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 229 us: 2.34x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 774 ms: 2.07x faster                                                         |
| async_tree_none          | 692 ms                                                       | 354 ms: 1.96x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 440 ms: 1.86x faster                                                         |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 608 ms: 1.54x faster                                                         |
| generators               | 57.3 ms                                                      | 38.2 ms: 1.50x faster                                                        |
| pylint                   | 566 ms                                                       | 382 ms: 1.48x faster                                                         |
| deepcopy                 | 468 us                                                       | 346 us: 1.35x faster                                                         |
| spectral_norm            | 139 ms                                                       | 103 ms: 1.35x faster                                                         |
| coroutines               | 30.3 ms                                                      | 23.2 ms: 1.31x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 39.3 us: 1.27x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 17.1 ms: 1.25x faster                                                        |
| scimark_lu               | 167 ms                                                       | 135 ms: 1.24x faster                                                         |
| crypto_pyaes             | 119 ms                                                       | 99.8 ms: 1.19x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 93.6 ms: 1.18x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 136 ms: 1.18x faster                                                         |
| pycparser                | 1.67 sec                                                     | 1.42 sec: 1.18x faster                                                       |
| richards_super           | 90.6 ms                                                      | 79.0 ms: 1.15x faster                                                        |
| chaos                    | 109 ms                                                       | 94.9 ms: 1.14x faster                                                        |
| pyflate                  | 733 ms                                                       | 646 ms: 1.13x faster                                                         |
| json_loads               | 30.3 us                                                      | 26.8 us: 1.13x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.65 us: 1.13x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.61 sec: 1.12x faster                                                       |
| regex_compile            | 190 ms                                                       | 173 ms: 1.10x faster                                                         |
| docutils                 | 3.41 sec                                                     | 3.11 sec: 1.10x faster                                                       |
| pidigits                 | 271 ms                                                       | 247 ms: 1.10x faster                                                         |
| json                     | 5.86 ms                                                      | 5.43 ms: 1.08x faster                                                        |
| go                       | 262 ms                                                       | 244 ms: 1.07x faster                                                         |
| deepcopy_reduce          | 4.01 us                                                      | 3.75 us: 1.07x faster                                                        |
| regex_dna                | 261 ms                                                       | 248 ms: 1.05x faster                                                         |
| richards                 | 75.1 ms                                                      | 71.4 ms: 1.05x faster                                                        |
| deltablue                | 7.50 ms                                                      | 7.13 ms: 1.05x faster                                                        |
| thrift                   | 1.18 ms                                                      | 1.12 ms: 1.05x faster                                                        |
| sympy_sum                | 193 ms                                                       | 185 ms: 1.04x faster                                                         |
| dulwich_log              | 81.1 ms                                                      | 78.2 ms: 1.04x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.90 sec: 1.03x faster                                                       |
| scimark_fft              | 361 ms                                                       | 350 ms: 1.03x faster                                                         |
| logging_silent           | 167 ns                                                       | 162 ns: 1.03x faster                                                         |
| nbody                    | 134 ms                                                       | 130 ms: 1.03x faster                                                         |
| json_dumps               | 14.5 ms                                                      | 14.2 ms: 1.03x faster                                                        |
| nqueens                  | 115 ms                                                       | 112 ms: 1.02x faster                                                         |
| float                    | 111 ms                                                       | 109 ms: 1.02x faster                                                         |
| asyncio_websockets       | 390 ms                                                       | 383 ms: 1.02x faster                                                         |
| xml_etree_process        | 75.9 ms                                                      | 74.7 ms: 1.02x faster                                                        |
| raytrace                 | 489 ms                                                       | 481 ms: 1.02x faster                                                         |
| html5lib                 | 94.6 ms                                                      | 93.1 ms: 1.02x faster                                                        |
| logging_simple           | 8.88 us                                                      | 8.74 us: 1.02x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 26.7 ms: 1.02x faster                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 1.03 sec: 1.02x faster                                                       |
| sympy_str                | 360 ms                                                       | 358 ms: 1.00x faster                                                         |
| pprint_pformat           | 2.15 sec                                                     | 2.14 sec: 1.00x faster                                                       |
| sympy_expand             | 600 ms                                                       | 598 ms: 1.00x faster                                                         |
| comprehensions           | 26.7 us                                                      | 27.0 us: 1.01x slower                                                        |
| sqlglot_normalize        | 144 ms                                                       | 146 ms: 1.01x slower                                                         |
| sympy_integrate          | 28.2 ms                                                      | 28.6 ms: 1.01x slower                                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 72.1 ms: 1.03x slower                                                        |
| unpickle_pure_python     | 312 us                                                       | 323 us: 1.04x slower                                                         |
| fannkuch                 | 483 ms                                                       | 504 ms: 1.04x slower                                                         |
| sqlglot_transpile        | 2.68 ms                                                      | 2.82 ms: 1.05x slower                                                        |
| genshi_text              | 31.4 ms                                                      | 33.0 ms: 1.05x slower                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 2.36 ms: 1.06x slower                                                        |
| sqlalchemy_declarative   | 190 ms                                                       | 200 ms: 1.06x slower                                                         |
| scimark_sor              | 180 ms                                                       | 192 ms: 1.07x slower                                                         |
| genshi_xml               | 63.3 ms                                                      | 67.6 ms: 1.07x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.30 ms: 1.07x slower                                                        |
| django_template          | 50.2 ms                                                      | 53.6 ms: 1.07x slower                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 98.6 ms: 1.07x slower                                                        |
| 2to3                     | 350 ms                                                       | 382 ms: 1.09x slower                                                         |
| pickle_pure_python       | 455 us                                                       | 506 us: 1.11x slower                                                         |
| gc_traversal             | 3.42 ms                                                      | 3.82 ms: 1.12x slower                                                        |
| meteor_contest           | 138 ms                                                       | 155 ms: 1.12x slower                                                         |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 5.78 ms: 1.14x slower                                                        |
| async_generators         | 421 ms                                                       | 515 ms: 1.22x slower                                                         |
| telco                    | 7.23 ms                                                      | 9.18 ms: 1.27x slower                                                        |
| mako                     | 14.7 ms                                                      | 19.5 ms: 1.32x slower                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 1.56 ms: 1.37x slower                                                        |
| mypy2                    | 933 ms                                                       | 1.31 sec: 1.40x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.72 ms: 1.54x slower                                                        |
| coverage                 | 63.3 ms                                                      | 103 ms: 1.62x slower                                                         |
| python_startup_no_site   | 7.33 ms                                                      | 12.0 ms: 1.64x slower                                                        |
| python_startup           | 11.5 ms                                                      | 19.2 ms: 1.67x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 52.3 ms: 8.21x slower                                                        |
| Geometric mean           | (ref)                                                        | 1.02x faster                                                                 |

Benchmark hidden because not significant (4): scimark_monte_carlo, hexiom, logging_format, sqlalchemy_imperative
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241228-3.14.0a3+-f9a5a3a-NOGIL/bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.048x faster

# HPT report

- Reliability score: 99.84% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.52x