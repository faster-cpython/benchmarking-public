# Results vs. 3.10.4

- fork: python
- ref: db6f5e193315a3bbfa7b
- machine: linux-x86_64
- commit hash: db6f5e1
- commit date: 2024-08-13
- overall geometric mean: 1.11x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x slower
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-pythonperf2-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 437 ms: 1.25x slower                                                        |
| docutils       | 3.41 sec                                                     | 3.51 sec: 1.03x slower                                                      |
| html5lib       | 94.6 ms                                                      | 109 ms: 1.16x slower                                                        |
| tornado_http   | 157 ms                                                       | 166 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                        | 1.12x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-pythonperf2-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 948 ms: 1.69x faster                                                        |
| async_tree_none         | 692 ms                                                       | 419 ms: 1.65x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 521 ms: 1.57x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 683 ms: 1.37x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.57x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-pythonperf2-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                        |
| float          | 111 ms                                                       | 146 ms: 1.31x slower                                                        |
| nbody          | 134 ms                                                       | 201 ms: 1.50x slower                                                        |
| Geometric mean | (ref)                                                        | 1.22x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-pythonperf2-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 261 ms                                                       | 237 ms: 1.10x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 26.9 ms: 1.01x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.48 ms: 1.13x slower                                                       |
| regex_compile  | 190 ms                                                       | 233 ms: 1.22x slower                                                        |
| Geometric mean | (ref)                                                        | 1.05x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-pythonperf2-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 160 ms                                                       | 136 ms: 1.17x faster                                                        |
| json_loads           | 30.3 us                                                      | 29.7 us: 1.02x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 109 ms: 1.01x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 3.41 sec: 1.17x slower                                                      |
| xml_etree_process    | 75.9 ms                                                      | 97.6 ms: 1.29x slower                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 119 ms: 1.29x slower                                                        |
| unpickle_pure_python | 312 us                                                       | 406 us: 1.30x slower                                                        |
| pickle_pure_python   | 455 us                                                       | 598 us: 1.31x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.12x slower                                                                |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-pythonperf2-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 17.1 ms: 1.49x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 11.8 ms: 1.61x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.55x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-pythonperf2-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 63.3 ms                                                      | 85.5 ms: 1.35x slower                                                       |
| django_template | 50.2 ms                                                      | 69.3 ms: 1.38x slower                                                       |
| genshi_text     | 31.4 ms                                                      | 44.1 ms: 1.40x slower                                                       |
| mako            | 14.7 ms                                                      | 22.2 ms: 1.51x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.41x slower                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-pythonperf2-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 282 us: 1.90x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 448 ms: 1.74x faster                                                        |
| async_tree_io            | 1.60 sec                                                     | 948 ms: 1.69x faster                                                        |
| async_tree_none          | 692 ms                                                       | 419 ms: 1.65x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.90 sec: 1.63x faster                                                      |
| async_tree_memoization   | 819 ms                                                       | 521 ms: 1.57x faster                                                        |
| generators               | 57.3 ms                                                      | 41.3 ms: 1.39x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 683 ms: 1.37x faster                                                        |
| pylint                   | 566 ms                                                       | 435 ms: 1.30x faster                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 4.94 ms: 1.29x faster                                                       |
| gc_traversal             | 3.42 ms                                                      | 2.79 ms: 1.22x faster                                                       |
| xml_etree_parse          | 160 ms                                                       | 136 ms: 1.17x faster                                                        |
| regex_dna                | 261 ms                                                       | 237 ms: 1.10x faster                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 1.61 ms: 1.10x faster                                                       |
| pidigits                 | 271 ms                                                       | 251 ms: 1.08x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 19.8 ms: 1.08x faster                                                       |
| coroutines               | 30.3 ms                                                      | 29.3 ms: 1.04x faster                                                       |
| deepcopy                 | 468 us                                                       | 453 us: 1.03x faster                                                        |
| asyncio_websockets       | 390 ms                                                       | 381 ms: 1.02x faster                                                        |
| json_loads               | 30.3 us                                                      | 29.7 us: 1.02x faster                                                       |
| xml_etree_iterparse      | 110 ms                                                       | 109 ms: 1.01x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 26.9 ms: 1.01x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 122 ms: 1.02x slower                                                        |
| docutils                 | 3.41 sec                                                     | 3.51 sec: 1.03x slower                                                      |
| json                     | 5.86 ms                                                      | 6.16 ms: 1.05x slower                                                       |
| deepcopy_memo            | 49.8 us                                                      | 52.3 us: 1.05x slower                                                       |
| pyflate                  | 733 ms                                                       | 774 ms: 1.06x slower                                                        |
| pycparser                | 1.67 sec                                                     | 1.77 sec: 1.06x slower                                                      |
| tornado_http             | 157 ms                                                       | 166 ms: 1.06x slower                                                        |
| mdp                      | 3.01 sec                                                     | 3.25 sec: 1.08x slower                                                      |
| richards_super           | 90.6 ms                                                      | 99.3 ms: 1.10x slower                                                       |
| richards                 | 75.1 ms                                                      | 82.7 ms: 1.10x slower                                                       |
| deltablue                | 7.50 ms                                                      | 8.31 ms: 1.11x slower                                                       |
| logging_silent           | 167 ns                                                       | 186 ns: 1.11x slower                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 5.72 ms: 1.13x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.48 ms: 1.13x slower                                                       |
| comprehensions           | 26.7 us                                                      | 30.2 us: 1.13x slower                                                       |
| scimark_fft              | 361 ms                                                       | 413 ms: 1.14x slower                                                        |
| nqueens                  | 115 ms                                                       | 133 ms: 1.15x slower                                                        |
| html5lib                 | 94.6 ms                                                      | 109 ms: 1.16x slower                                                        |
| sympy_integrate          | 28.2 ms                                                      | 32.6 ms: 1.16x slower                                                       |
| chaos                    | 109 ms                                                       | 127 ms: 1.17x slower                                                        |
| tomli_loads              | 2.92 sec                                                     | 3.41 sec: 1.17x slower                                                      |
| thrift                   | 1.18 ms                                                      | 1.38 ms: 1.18x slower                                                       |
| fannkuch                 | 483 ms                                                       | 583 ms: 1.21x slower                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 4.85 us: 1.21x slower                                                       |
| regex_compile            | 190 ms                                                       | 233 ms: 1.22x slower                                                        |
| spectral_norm            | 139 ms                                                       | 171 ms: 1.23x slower                                                        |
| async_generators         | 421 ms                                                       | 521 ms: 1.24x slower                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 134 ms: 1.25x slower                                                        |
| raytrace                 | 489 ms                                                       | 610 ms: 1.25x slower                                                        |
| 2to3                     | 350 ms                                                       | 437 ms: 1.25x slower                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 3.39 ms: 1.27x slower                                                       |
| sympy_str                | 360 ms                                                       | 456 ms: 1.27x slower                                                        |
| hexiom                   | 9.42 ms                                                      | 11.9 ms: 1.27x slower                                                       |
| meteor_contest           | 138 ms                                                       | 176 ms: 1.27x slower                                                        |
| go                       | 262 ms                                                       | 333 ms: 1.27x slower                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 2.87 ms: 1.28x slower                                                       |
| xml_etree_process        | 75.9 ms                                                      | 97.6 ms: 1.29x slower                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 119 ms: 1.29x slower                                                        |
| unpickle_pure_python     | 312 us                                                       | 406 us: 1.30x slower                                                        |
| logging_format           | 9.64 us                                                      | 12.6 us: 1.31x slower                                                       |
| logging_simple           | 8.88 us                                                      | 11.6 us: 1.31x slower                                                       |
| float                    | 111 ms                                                       | 146 ms: 1.31x slower                                                        |
| pickle_pure_python       | 455 us                                                       | 598 us: 1.31x slower                                                        |
| sqlglot_normalize        | 144 ms                                                       | 189 ms: 1.32x slower                                                        |
| genshi_xml               | 63.3 ms                                                      | 85.5 ms: 1.35x slower                                                       |
| sqlglot_optimize         | 70.1 ms                                                      | 95.4 ms: 1.36x slower                                                       |
| sympy_expand             | 600 ms                                                       | 823 ms: 1.37x slower                                                        |
| sympy_sum                | 193 ms                                                       | 265 ms: 1.37x slower                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 1.45 sec: 1.38x slower                                                      |
| django_template          | 50.2 ms                                                      | 69.3 ms: 1.38x slower                                                       |
| pprint_pformat           | 2.15 sec                                                     | 3.00 sec: 1.39x slower                                                      |
| genshi_text              | 31.4 ms                                                      | 44.1 ms: 1.40x slower                                                       |
| scimark_sor              | 180 ms                                                       | 256 ms: 1.42x slower                                                        |
| telco                    | 7.23 ms                                                      | 10.6 ms: 1.46x slower                                                       |
| scimark_lu               | 167 ms                                                       | 248 ms: 1.49x slower                                                        |
| python_startup           | 11.5 ms                                                      | 17.1 ms: 1.49x slower                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 1.70 ms: 1.49x slower                                                       |
| nbody                    | 134 ms                                                       | 201 ms: 1.50x slower                                                        |
| mako                     | 14.7 ms                                                      | 22.2 ms: 1.51x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 11.8 ms: 1.61x slower                                                       |
| coverage                 | 63.3 ms                                                      | 109 ms: 1.72x slower                                                        |
| Geometric mean           | (ref)                                                        | 1.11x slower                                                                |

Benchmark hidden because not significant (1): json_dumps
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240813-3.14.0a0-db6f5e1-NOGIL/bm-20240813-pythonperf2-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.11x
- 95% likely to have a slowdown of 1.10x
- 99% likely to have a slowdown of 1.08x

# Memory
- memory change: 1.31x