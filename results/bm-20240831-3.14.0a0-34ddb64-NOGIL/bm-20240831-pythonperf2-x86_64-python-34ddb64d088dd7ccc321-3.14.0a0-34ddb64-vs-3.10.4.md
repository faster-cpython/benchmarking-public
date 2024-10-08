# Results vs. 3.10.4

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: linux-x86_64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.10x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.06x slower
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 437 ms: 1.25x slower                                                        |
| docutils       | 3.41 sec                                                     | 3.44 sec: 1.01x slower                                                      |
| html5lib       | 94.6 ms                                                      | 107 ms: 1.13x slower                                                        |
| tornado_http   | 157 ms                                                       | 169 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                        | 1.11x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 963 ms: 1.66x faster                                                        |
| async_tree_none         | 692 ms                                                       | 421 ms: 1.64x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 524 ms: 1.56x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 686 ms: 1.37x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.55x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 271 ms                                                       | 250 ms: 1.08x faster                                                        |
| float          | 111 ms                                                       | 145 ms: 1.30x slower                                                        |
| nbody          | 134 ms                                                       | 195 ms: 1.45x slower                                                        |
| Geometric mean | (ref)                                                        | 1.20x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 261 ms                                                       | 241 ms: 1.09x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 27.3 ms: 1.01x slower                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.54 ms: 1.15x slower                                                       |
| regex_compile  | 190 ms                                                       | 231 ms: 1.21x slower                                                        |
| Geometric mean | (ref)                                                        | 1.07x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 160 ms                                                       | 137 ms: 1.17x faster                                                        |
| json_loads           | 30.3 us                                                      | 29.5 us: 1.03x faster                                                       |
| json_dumps           | 14.5 ms                                                      | 14.2 ms: 1.02x faster                                                       |
| tomli_loads          | 2.92 sec                                                     | 3.38 sec: 1.16x slower                                                      |
| xml_etree_process    | 75.9 ms                                                      | 96.7 ms: 1.27x slower                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 118 ms: 1.28x slower                                                        |
| pickle_pure_python   | 455 us                                                       | 593 us: 1.30x slower                                                        |
| unpickle_pure_python | 312 us                                                       | 417 us: 1.34x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.12x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 17.4 ms: 1.51x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 12.0 ms: 1.63x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.57x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 63.3 ms                                                      | 83.9 ms: 1.33x slower                                                       |
| django_template | 50.2 ms                                                      | 68.9 ms: 1.37x slower                                                       |
| genshi_text     | 31.4 ms                                                      | 43.6 ms: 1.39x slower                                                       |
| mako            | 14.7 ms                                                      | 21.9 ms: 1.49x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.39x slower                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 279 us: 1.92x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 451 ms: 1.73x faster                                                        |
| async_tree_io            | 1.60 sec                                                     | 963 ms: 1.66x faster                                                        |
| async_tree_none          | 692 ms                                                       | 421 ms: 1.64x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.90 sec: 1.63x faster                                                      |
| async_tree_memoization   | 819 ms                                                       | 524 ms: 1.56x faster                                                        |
| generators               | 57.3 ms                                                      | 41.3 ms: 1.39x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 686 ms: 1.37x faster                                                        |
| pylint                   | 566 ms                                                       | 441 ms: 1.28x faster                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 5.06 ms: 1.26x faster                                                       |
| xml_etree_parse          | 160 ms                                                       | 137 ms: 1.17x faster                                                        |
| gc_traversal             | 3.42 ms                                                      | 2.99 ms: 1.14x faster                                                       |
| regex_dna                | 261 ms                                                       | 241 ms: 1.09x faster                                                        |
| pidigits                 | 271 ms                                                       | 250 ms: 1.08x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 19.9 ms: 1.07x faster                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 1.67 ms: 1.06x faster                                                       |
| coroutines               | 30.3 ms                                                      | 29.2 ms: 1.04x faster                                                       |
| json_loads               | 30.3 us                                                      | 29.5 us: 1.03x faster                                                       |
| deepcopy                 | 468 us                                                       | 455 us: 1.03x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 14.2 ms: 1.02x faster                                                       |
| asyncio_websockets       | 390 ms                                                       | 385 ms: 1.01x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 27.3 ms: 1.01x slower                                                       |
| crypto_pyaes             | 119 ms                                                       | 120 ms: 1.01x slower                                                        |
| docutils                 | 3.41 sec                                                     | 3.44 sec: 1.01x slower                                                      |
| pyflate                  | 733 ms                                                       | 771 ms: 1.05x slower                                                        |
| json                     | 5.86 ms                                                      | 6.19 ms: 1.06x slower                                                       |
| pycparser                | 1.67 sec                                                     | 1.77 sec: 1.06x slower                                                      |
| deepcopy_memo            | 49.8 us                                                      | 53.4 us: 1.07x slower                                                       |
| tornado_http             | 157 ms                                                       | 169 ms: 1.07x slower                                                        |
| mdp                      | 3.01 sec                                                     | 3.24 sec: 1.08x slower                                                      |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 5.57 ms: 1.10x slower                                                       |
| scimark_fft              | 361 ms                                                       | 399 ms: 1.10x slower                                                        |
| richards                 | 75.1 ms                                                      | 83.2 ms: 1.11x slower                                                       |
| go                       | 262 ms                                                       | 291 ms: 1.11x slower                                                        |
| comprehensions           | 26.7 us                                                      | 29.7 us: 1.11x slower                                                       |
| deltablue                | 7.50 ms                                                      | 8.35 ms: 1.11x slower                                                       |
| dulwich_log              | 81.1 ms                                                      | 90.5 ms: 1.12x slower                                                       |
| richards_super           | 90.6 ms                                                      | 101 ms: 1.12x slower                                                        |
| html5lib                 | 94.6 ms                                                      | 107 ms: 1.13x slower                                                        |
| sympy_integrate          | 28.2 ms                                                      | 32.1 ms: 1.14x slower                                                       |
| logging_silent           | 167 ns                                                       | 191 ns: 1.14x slower                                                        |
| nqueens                  | 115 ms                                                       | 132 ms: 1.15x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.54 ms: 1.15x slower                                                       |
| chaos                    | 109 ms                                                       | 125 ms: 1.15x slower                                                        |
| tomli_loads              | 2.92 sec                                                     | 3.38 sec: 1.16x slower                                                      |
| thrift                   | 1.18 ms                                                      | 1.37 ms: 1.16x slower                                                       |
| fannkuch                 | 483 ms                                                       | 571 ms: 1.18x slower                                                        |
| async_generators         | 421 ms                                                       | 501 ms: 1.19x slower                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 4.83 us: 1.21x slower                                                       |
| regex_compile            | 190 ms                                                       | 231 ms: 1.21x slower                                                        |
| spectral_norm            | 139 ms                                                       | 170 ms: 1.22x slower                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 134 ms: 1.24x slower                                                        |
| meteor_contest           | 138 ms                                                       | 172 ms: 1.25x slower                                                        |
| 2to3                     | 350 ms                                                       | 437 ms: 1.25x slower                                                        |
| raytrace                 | 489 ms                                                       | 611 ms: 1.25x slower                                                        |
| hexiom                   | 9.42 ms                                                      | 11.9 ms: 1.26x slower                                                       |
| sympy_str                | 360 ms                                                       | 455 ms: 1.26x slower                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 3.39 ms: 1.27x slower                                                       |
| xml_etree_process        | 75.9 ms                                                      | 96.7 ms: 1.27x slower                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 118 ms: 1.28x slower                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 2.87 ms: 1.28x slower                                                       |
| logging_format           | 9.64 us                                                      | 12.5 us: 1.29x slower                                                       |
| float                    | 111 ms                                                       | 145 ms: 1.30x slower                                                        |
| pickle_pure_python       | 455 us                                                       | 593 us: 1.30x slower                                                        |
| logging_simple           | 8.88 us                                                      | 11.6 us: 1.31x slower                                                       |
| genshi_xml               | 63.3 ms                                                      | 83.9 ms: 1.33x slower                                                       |
| sqlglot_normalize        | 144 ms                                                       | 192 ms: 1.33x slower                                                        |
| unpickle_pure_python     | 312 us                                                       | 417 us: 1.34x slower                                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 95.9 ms: 1.37x slower                                                       |
| sympy_sum                | 193 ms                                                       | 264 ms: 1.37x slower                                                        |
| django_template          | 50.2 ms                                                      | 68.9 ms: 1.37x slower                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 1.44 sec: 1.37x slower                                                      |
| sympy_expand             | 600 ms                                                       | 827 ms: 1.38x slower                                                        |
| scimark_sor              | 180 ms                                                       | 250 ms: 1.39x slower                                                        |
| pprint_pformat           | 2.15 sec                                                     | 2.99 sec: 1.39x slower                                                      |
| genshi_text              | 31.4 ms                                                      | 43.6 ms: 1.39x slower                                                       |
| scimark_lu               | 167 ms                                                       | 237 ms: 1.42x slower                                                        |
| nbody                    | 134 ms                                                       | 195 ms: 1.45x slower                                                        |
| telco                    | 7.23 ms                                                      | 10.6 ms: 1.47x slower                                                       |
| mako                     | 14.7 ms                                                      | 21.9 ms: 1.49x slower                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 1.73 ms: 1.51x slower                                                       |
| python_startup           | 11.5 ms                                                      | 17.4 ms: 1.51x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 12.0 ms: 1.63x slower                                                       |
| coverage                 | 63.3 ms                                                      | 109 ms: 1.72x slower                                                        |
| Geometric mean           | (ref)                                                        | 1.10x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240831-3.14.0a0-34ddb64-NOGIL/bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.09x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: 1.30x