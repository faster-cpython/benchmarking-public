# Results vs. 3.10.4

- fork: python
- ref: 800d37feca2e0ea33439
- machine: linux-aarch64
- commit hash: 800d37f
- commit date: 2025-07-19
- overall geometric mean: 1.278x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.40x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 312 ms: 1.22x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.08 sec: 1.14x faster                                                  |
| html5lib       | 86.5 ms                                                               | 65.7 ms: 1.32x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.23x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 880 ms: 2.60x faster                                                    |
| async_tree_none         | 950 ms                                                                | 375 ms: 2.53x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 477 ms: 2.37x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 653 ms: 1.95x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.35x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 82.0 ms: 1.64x faster                                                   |
| nbody          | 166 ms                                                                | 130 ms: 1.28x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.27x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 122 ms: 1.44x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 26.5 ms: 1.21x faster                                                   |
| regex_dna      | 257 ms                                                                | 220 ms: 1.17x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 3.99 ms: 1.07x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.21x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 3.36 sec                                                              | 2.33 sec: 1.44x faster                                                  |
| unpickle_pure_python | 366 us                                                                | 259 us: 1.41x faster                                                    |
| pickle_pure_python   | 529 us                                                                | 410 us: 1.29x faster                                                    |
| xml_etree_process    | 99.5 ms                                                               | 78.2 ms: 1.27x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 13.9 ms: 1.20x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 179 ms: 1.18x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 109 ms: 1.13x faster                                                    |
| unpickle_list        | 6.99 us                                                               | 6.42 us: 1.09x faster                                                   |
| xml_etree_iterparse  | 156 ms                                                                | 144 ms: 1.08x faster                                                    |
| json_loads           | 30.9 us                                                               | 33.1 us: 1.07x slower                                                   |
| unpickle             | 17.5 us                                                               | 18.7 us: 1.07x slower                                                   |
| pickle_dict          | 35.1 us                                                               | 38.7 us: 1.10x slower                                                   |
| pickle_list          | 5.24 us                                                               | 5.80 us: 1.11x slower                                                   |
| pickle               | 12.5 us                                                               | 15.3 us: 1.22x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.10x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.56 ms: 1.24x slower                                                   |
| python_startup         | 11.2 ms                                                               | 15.1 ms: 1.35x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.30x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 12.8 ms: 1.48x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 27.0 ms: 1.30x faster                                                   |
| django_template | 53.3 ms                                                               | 41.3 ms: 1.29x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 64.0 ms: 1.09x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.28x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 210 us: 3.15x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 880 ms: 2.60x faster                                                    |
| async_tree_none          | 950 ms                                                                | 375 ms: 2.53x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 477 ms: 2.37x faster                                                    |
| deltablue                | 8.94 ms                                                               | 3.87 ms: 2.31x faster                                                   |
| mdp                      | 3.70 sec                                                              | 1.71 sec: 2.16x faster                                                  |
| richards                 | 91.7 ms                                                               | 45.5 ms: 2.01x faster                                                   |
| richards_super           | 107 ms                                                                | 53.2 ms: 2.01x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 653 ms: 1.95x faster                                                    |
| generators               | 68.1 ms                                                               | 35.4 ms: 1.92x faster                                                   |
| asyncio_tcp              | 944 ms                                                                | 534 ms: 1.77x faster                                                    |
| chaos                    | 121 ms                                                                | 68.9 ms: 1.76x faster                                                   |
| scimark_sor              | 246 ms                                                                | 143 ms: 1.72x faster                                                    |
| go                       | 264 ms                                                                | 154 ms: 1.72x faster                                                    |
| raytrace                 | 573 ms                                                                | 336 ms: 1.71x faster                                                    |
| logging_silent           | 222 ns                                                                | 134 ns: 1.66x faster                                                    |
| float                    | 135 ms                                                                | 82.0 ms: 1.64x faster                                                   |
| spectral_norm            | 186 ms                                                                | 116 ms: 1.61x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 38.8 us: 1.59x faster                                                   |
| deepcopy                 | 511 us                                                                | 332 us: 1.54x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 85.1 ms: 1.50x faster                                                   |
| scimark_lu               | 227 ms                                                                | 151 ms: 1.50x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.20 sec: 1.49x faster                                                  |
| pylint                   | 485 ms                                                                | 326 ms: 1.49x faster                                                    |
| comprehensions           | 33.1 us                                                               | 22.3 us: 1.49x faster                                                   |
| mako                     | 18.9 ms                                                               | 12.8 ms: 1.48x faster                                                   |
| regex_compile            | 177 ms                                                                | 122 ms: 1.44x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.33 sec: 1.44x faster                                                  |
| hexiom                   | 10.9 ms                                                               | 7.58 ms: 1.44x faster                                                   |
| pyflate                  | 795 ms                                                                | 555 ms: 1.43x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 94.7 ms: 1.41x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 259 us: 1.41x faster                                                    |
| logging_simple           | 9.78 us                                                               | 7.18 us: 1.36x faster                                                   |
| logging_format           | 10.6 us                                                               | 7.87 us: 1.35x faster                                                   |
| dulwich_log              | 73.5 ms                                                               | 55.6 ms: 1.32x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 65.7 ms: 1.32x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 27.0 ms: 1.30x faster                                                   |
| thrift                   | 1.26 ms                                                               | 976 us: 1.29x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 410 us: 1.29x faster                                                    |
| django_template          | 53.3 ms                                                               | 41.3 ms: 1.29x faster                                                   |
| nbody                    | 166 ms                                                                | 130 ms: 1.28x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 78.2 ms: 1.27x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.35 sec: 1.25x faster                                                  |
| deepcopy_reduce          | 4.60 us                                                               | 3.68 us: 1.25x faster                                                   |
| coroutines               | 37.2 ms                                                               | 29.9 ms: 1.24x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 21.5 ms: 1.24x faster                                                   |
| scimark_fft              | 500 ms                                                                | 408 ms: 1.23x faster                                                    |
| 2to3                     | 381 ms                                                                | 312 ms: 1.22x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 26.5 ms: 1.21x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 13.9 ms: 1.20x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 179 ms: 1.18x faster                                                    |
| fannkuch                 | 546 ms                                                                | 461 ms: 1.18x faster                                                    |
| sympy_sum                | 184 ms                                                                | 156 ms: 1.18x faster                                                    |
| regex_dna                | 257 ms                                                                | 220 ms: 1.17x faster                                                    |
| sympy_str                | 329 ms                                                                | 281 ms: 1.17x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.37 ms: 1.16x faster                                                   |
| nqueens                  | 117 ms                                                                | 102 ms: 1.16x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.08 sec: 1.14x faster                                                  |
| pathlib                  | 26.3 ms                                                               | 23.0 ms: 1.14x faster                                                   |
| xml_etree_generate       | 123 ms                                                                | 109 ms: 1.13x faster                                                    |
| meteor_contest           | 126 ms                                                                | 113 ms: 1.11x faster                                                    |
| sympy_expand             | 543 ms                                                                | 489 ms: 1.11x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.77 us: 1.09x faster                                                   |
| genshi_xml               | 69.8 ms                                                               | 64.0 ms: 1.09x faster                                                   |
| unpickle_list            | 6.99 us                                                               | 6.42 us: 1.09x faster                                                   |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 7.02 ms: 1.09x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 144 ms: 1.08x faster                                                    |
| regex_effbot             | 4.25 ms                                                               | 3.99 ms: 1.07x faster                                                   |
| pprint_pformat           | 2.36 sec                                                              | 2.28 sec: 1.04x faster                                                  |
| pprint_safe_repr         | 1.15 sec                                                              | 1.12 sec: 1.02x faster                                                  |
| json                     | 5.88 ms                                                               | 5.80 ms: 1.01x faster                                                   |
| asyncio_websockets       | 657 ms                                                                | 666 ms: 1.01x slower                                                    |
| json_loads               | 30.9 us                                                               | 33.1 us: 1.07x slower                                                   |
| async_generators         | 452 ms                                                                | 485 ms: 1.07x slower                                                    |
| unpickle                 | 17.5 us                                                               | 18.7 us: 1.07x slower                                                   |
| pickle_dict              | 35.1 us                                                               | 38.7 us: 1.10x slower                                                   |
| pickle_list              | 5.24 us                                                               | 5.80 us: 1.11x slower                                                   |
| pickle                   | 12.5 us                                                               | 15.3 us: 1.22x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.56 ms: 1.24x slower                                                   |
| coverage                 | 83.6 ms                                                               | 105 ms: 1.26x slower                                                    |
| python_startup           | 11.2 ms                                                               | 15.1 ms: 1.35x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 6.87 ms: 1.65x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 3.75 ms: 1.66x slower                                                   |
| telco                    | 8.49 ms                                                               | 166 ms: 19.52x slower                                                   |
| bench_mp_pool            | 14.5 ms                                                               | 2.68 sec: 184.54x slower                                                |
| Geometric mean           | (ref)                                                                 | 1.18x faster                                                            |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250719-3.15.0a0-800d37f-JIT/bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.278x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.40x