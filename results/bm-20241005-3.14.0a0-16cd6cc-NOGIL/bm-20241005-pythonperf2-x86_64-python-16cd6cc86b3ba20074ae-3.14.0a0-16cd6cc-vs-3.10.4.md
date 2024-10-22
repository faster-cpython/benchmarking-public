# Results vs. 3.10.4

- fork: python
- ref: 16cd6cc86b3ba20074ae
- machine: linux-x86_64
- commit hash: 16cd6cc
- commit date: 2024-10-05
- overall geometric mean: 1.11x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.05x slower
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 421 ms: 1.20x slower                                                        |
| docutils       | 3.41 sec                                                     | 3.38 sec: 1.01x faster                                                      |
| html5lib       | 94.6 ms                                                      | 105 ms: 1.11x slower                                                        |
| tornado_http   | 157 ms                                                       | 166 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                        | 1.09x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 939 ms: 1.70x faster                                                        |
| async_tree_none         | 692 ms                                                       | 422 ms: 1.64x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 519 ms: 1.58x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 681 ms: 1.38x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.57x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 271 ms                                                       | 250 ms: 1.09x faster                                                        |
| float          | 111 ms                                                       | 141 ms: 1.27x slower                                                        |
| nbody          | 134 ms                                                       | 193 ms: 1.44x slower                                                        |
| Geometric mean | (ref)                                                        | 1.19x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 261 ms                                                       | 246 ms: 1.06x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 27.0 ms: 1.00x faster                                                       |
| regex_compile  | 190 ms                                                       | 223 ms: 1.17x slower                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.66 ms: 1.19x slower                                                       |
| Geometric mean | (ref)                                                        | 1.07x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 160 ms                                                       | 138 ms: 1.16x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 13.7 ms: 1.06x faster                                                       |
| json_loads           | 30.3 us                                                      | 29.5 us: 1.03x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 108 ms: 1.02x faster                                                        |
| pickle               | 9.89 us                                                      | 9.98 us: 1.01x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 30.9 us: 1.05x slower                                                       |
| pickle_list          | 4.12 us                                                      | 4.40 us: 1.07x slower                                                       |
| unpickle_list        | 4.65 us                                                      | 5.22 us: 1.12x slower                                                       |
| tomli_loads          | 2.92 sec                                                     | 3.31 sec: 1.14x slower                                                      |
| xml_etree_process    | 75.9 ms                                                      | 89.3 ms: 1.18x slower                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 111 ms: 1.20x slower                                                        |
| unpickle             | 13.5 us                                                      | 17.1 us: 1.27x slower                                                       |
| pickle_pure_python   | 455 us                                                       | 579 us: 1.27x slower                                                        |
| unpickle_pure_python | 312 us                                                       | 399 us: 1.28x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.09x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 17.4 ms: 1.51x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 11.8 ms: 1.60x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.56x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 63.3 ms                                                      | 81.0 ms: 1.28x slower                                                       |
| django_template | 50.2 ms                                                      | 65.4 ms: 1.30x slower                                                       |
| genshi_text     | 31.4 ms                                                      | 42.0 ms: 1.34x slower                                                       |
| mako            | 14.7 ms                                                      | 21.3 ms: 1.45x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.34x slower                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 258 us: 2.08x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 455 ms: 1.71x faster                                                        |
| async_tree_io            | 1.60 sec                                                     | 939 ms: 1.70x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.83 sec: 1.69x faster                                                      |
| async_tree_none          | 692 ms                                                       | 422 ms: 1.64x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 519 ms: 1.58x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 681 ms: 1.38x faster                                                        |
| generators               | 57.3 ms                                                      | 42.1 ms: 1.36x faster                                                       |
| pylint                   | 566 ms                                                       | 430 ms: 1.32x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 138 ms: 1.16x faster                                                        |
| coroutines               | 30.3 ms                                                      | 26.9 ms: 1.13x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 19.2 ms: 1.11x faster                                                       |
| deepcopy                 | 468 us                                                       | 423 us: 1.11x faster                                                        |
| pidigits                 | 271 ms                                                       | 250 ms: 1.09x faster                                                        |
| gc_traversal             | 3.42 ms                                                      | 3.19 ms: 1.07x faster                                                       |
| regex_dna                | 261 ms                                                       | 246 ms: 1.06x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 13.7 ms: 1.06x faster                                                       |
| asyncio_websockets       | 390 ms                                                       | 377 ms: 1.04x faster                                                        |
| json_loads               | 30.3 us                                                      | 29.5 us: 1.03x faster                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 1.72 ms: 1.03x faster                                                       |
| xml_etree_iterparse      | 110 ms                                                       | 108 ms: 1.02x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 49.0 us: 1.02x faster                                                       |
| docutils                 | 3.41 sec                                                     | 3.38 sec: 1.01x faster                                                      |
| sqlite_synth             | 2.99 us                                                      | 2.98 us: 1.00x faster                                                       |
| regex_v8                 | 27.2 ms                                                      | 27.0 ms: 1.00x faster                                                       |
| pickle                   | 9.89 us                                                      | 9.98 us: 1.01x slower                                                       |
| json                     | 5.86 ms                                                      | 5.94 ms: 1.01x slower                                                       |
| pycparser                | 1.67 sec                                                     | 1.70 sec: 1.01x slower                                                      |
| pyflate                  | 733 ms                                                       | 754 ms: 1.03x slower                                                        |
| pickle_dict              | 29.5 us                                                      | 30.9 us: 1.05x slower                                                       |
| tornado_http             | 157 ms                                                       | 166 ms: 1.06x slower                                                        |
| mdp                      | 3.01 sec                                                     | 3.19 sec: 1.06x slower                                                      |
| scimark_fft              | 361 ms                                                       | 384 ms: 1.06x slower                                                        |
| pickle_list              | 4.12 us                                                      | 4.40 us: 1.07x slower                                                       |
| richards_super           | 90.6 ms                                                      | 97.8 ms: 1.08x slower                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 5.48 ms: 1.08x slower                                                       |
| logging_silent           | 167 ns                                                       | 181 ns: 1.08x slower                                                        |
| deltablue                | 7.50 ms                                                      | 8.13 ms: 1.08x slower                                                       |
| richards                 | 75.1 ms                                                      | 81.6 ms: 1.09x slower                                                       |
| dulwich_log              | 81.1 ms                                                      | 89.2 ms: 1.10x slower                                                       |
| comprehensions           | 26.7 us                                                      | 29.5 us: 1.10x slower                                                       |
| chaos                    | 109 ms                                                       | 121 ms: 1.11x slower                                                        |
| html5lib                 | 94.6 ms                                                      | 105 ms: 1.11x slower                                                        |
| go                       | 262 ms                                                       | 292 ms: 1.12x slower                                                        |
| nqueens                  | 115 ms                                                       | 128 ms: 1.12x slower                                                        |
| unpickle_list            | 4.65 us                                                      | 5.22 us: 1.12x slower                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 4.55 us: 1.14x slower                                                       |
| tomli_loads              | 2.92 sec                                                     | 3.31 sec: 1.14x slower                                                      |
| async_generators         | 421 ms                                                       | 479 ms: 1.14x slower                                                        |
| thrift                   | 1.18 ms                                                      | 1.34 ms: 1.14x slower                                                       |
| sympy_integrate          | 28.2 ms                                                      | 32.4 ms: 1.15x slower                                                       |
| spectral_norm            | 139 ms                                                       | 161 ms: 1.15x slower                                                        |
| regex_compile            | 190 ms                                                       | 223 ms: 1.17x slower                                                        |
| xml_etree_process        | 75.9 ms                                                      | 89.3 ms: 1.18x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.66 ms: 1.19x slower                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 111 ms: 1.20x slower                                                        |
| 2to3                     | 350 ms                                                       | 421 ms: 1.20x slower                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 130 ms: 1.21x slower                                                        |
| fannkuch                 | 483 ms                                                       | 583 ms: 1.21x slower                                                        |
| hexiom                   | 9.42 ms                                                      | 11.4 ms: 1.21x slower                                                       |
| raytrace                 | 489 ms                                                       | 596 ms: 1.22x slower                                                        |
| sympy_str                | 360 ms                                                       | 445 ms: 1.24x slower                                                        |
| meteor_contest           | 138 ms                                                       | 171 ms: 1.24x slower                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 3.34 ms: 1.24x slower                                                       |
| sqlglot_normalize        | 144 ms                                                       | 179 ms: 1.25x slower                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 2.82 ms: 1.26x slower                                                       |
| float                    | 111 ms                                                       | 141 ms: 1.27x slower                                                        |
| unpickle                 | 13.5 us                                                      | 17.1 us: 1.27x slower                                                       |
| pickle_pure_python       | 455 us                                                       | 579 us: 1.27x slower                                                        |
| logging_simple           | 8.88 us                                                      | 11.3 us: 1.27x slower                                                       |
| genshi_xml               | 63.3 ms                                                      | 81.0 ms: 1.28x slower                                                       |
| unpickle_pure_python     | 312 us                                                       | 399 us: 1.28x slower                                                        |
| logging_format           | 9.64 us                                                      | 12.4 us: 1.28x slower                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 1.35 sec: 1.28x slower                                                      |
| sqlglot_optimize         | 70.1 ms                                                      | 90.1 ms: 1.28x slower                                                       |
| pprint_pformat           | 2.15 sec                                                     | 2.79 sec: 1.29x slower                                                      |
| scimark_lu               | 167 ms                                                       | 216 ms: 1.29x slower                                                        |
| django_template          | 50.2 ms                                                      | 65.4 ms: 1.30x slower                                                       |
| genshi_text              | 31.4 ms                                                      | 42.0 ms: 1.34x slower                                                       |
| sympy_expand             | 600 ms                                                       | 805 ms: 1.34x slower                                                        |
| sympy_sum                | 193 ms                                                       | 259 ms: 1.34x slower                                                        |
| scimark_sor              | 180 ms                                                       | 247 ms: 1.37x slower                                                        |
| telco                    | 7.23 ms                                                      | 10.2 ms: 1.41x slower                                                       |
| nbody                    | 134 ms                                                       | 193 ms: 1.44x slower                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 1.65 ms: 1.44x slower                                                       |
| mako                     | 14.7 ms                                                      | 21.3 ms: 1.45x slower                                                       |
| python_startup           | 11.5 ms                                                      | 17.4 ms: 1.51x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 11.8 ms: 1.60x slower                                                       |
| coverage                 | 63.3 ms                                                      | 105 ms: 1.66x slower                                                        |
| unpack_sequence          | 59.9 ns                                                      | 136 ns: 2.26x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 34.0 ms: 5.34x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.11x slower                                                                |

Benchmark hidden because not significant (1): crypto_pyaes
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20241005-3.14.0a0-16cd6cc-NOGIL/bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: 1.30x