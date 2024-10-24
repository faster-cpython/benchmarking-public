# Results vs. 3.10.4

- fork: faster-cpython
- ref: binary_subscr_getite
- machine: linux-x86_64
- commit hash: 71920f1
- commit date: 2024-07-30
- overall geometric mean: 1.43x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240730-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-71920f1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 273 ms: 1.28x faster                                                            |
| docutils       | 3.30 sec                                               | 2.91 sec: 1.13x faster                                                          |
| html5lib       | 88.9 ms                                                | 65.7 ms: 1.35x faster                                                           |
| tornado_http   | 136 ms                                                 | 92.2 ms: 1.48x faster                                                           |
| Geometric mean | (ref)                                                  | 1.30x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240730-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-71920f1 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 326 ms: 2.23x faster                                                            |
| async_tree_memoization  | 870 ms                                                 | 417 ms: 2.09x faster                                                            |
| async_tree_io           | 1.77 sec                                               | 913 ms: 1.94x faster                                                            |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 560 ms: 1.81x faster                                                            |
| Geometric mean          | (ref)                                                  | 2.01x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240730-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-71920f1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 79.5 ms: 1.93x faster                                                           |
| float          | 117 ms                                                 | 70.8 ms: 1.65x faster                                                           |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                            |
| Geometric mean | (ref)                                                  | 1.49x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240730-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-71920f1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 133 ms: 1.41x faster                                                            |
| regex_v8       | 27.8 ms                                                | 25.4 ms: 1.10x faster                                                           |
| regex_dna      | 227 ms                                                 | 221 ms: 1.02x faster                                                            |
| regex_effbot   | 3.63 ms                                                | 3.69 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                  | 1.12x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240730-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-71920f1 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 294 us: 1.65x faster                                                            |
| tomli_loads          | 3.14 sec                                               | 1.93 sec: 1.63x faster                                                          |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                                            |
| xml_etree_process    | 79.1 ms                                                | 56.6 ms: 1.40x faster                                                           |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                           |
| xml_etree_generate   | 99.4 ms                                                | 79.7 ms: 1.25x faster                                                           |
| xml_etree_iterparse  | 115 ms                                                 | 99.5 ms: 1.16x faster                                                           |
| xml_etree_parse      | 168 ms                                                 | 148 ms: 1.14x faster                                                            |
| json_loads           | 31.2 us                                                | 28.1 us: 1.11x faster                                                           |
| Geometric mean       | (ref)                                                  | 1.34x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240730-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-71920f1 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                           |
| python_startup_no_site | 5.93 ms                                                | 7.16 ms: 1.21x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240730-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-71920f1 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.93 ms: 1.64x faster                                                           |
| django_template | 48.2 ms                                                | 35.6 ms: 1.35x faster                                                           |
| genshi_text     | 31.8 ms                                                | 24.7 ms: 1.29x faster                                                           |
| genshi_xml      | 66.0 ms                                                | 53.9 ms: 1.23x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.37x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240730-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-71920f1 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 170 us: 3.20x faster                                                            |
| generators               | 80.1 ms                                                | 32.9 ms: 2.44x faster                                                           |
| async_tree_none          | 728 ms                                                 | 326 ms: 2.23x faster                                                            |
| deltablue                | 7.91 ms                                                | 3.57 ms: 2.22x faster                                                           |
| async_tree_memoization   | 870 ms                                                 | 417 ms: 2.09x faster                                                            |
| deepcopy_memo            | 58.5 us                                                | 28.4 us: 2.06x faster                                                           |
| richards_super           | 94.7 ms                                                | 47.1 ms: 2.01x faster                                                           |
| chaos                    | 115 ms                                                 | 57.8 ms: 2.00x faster                                                           |
| crypto_pyaes             | 128 ms                                                 | 65.8 ms: 1.94x faster                                                           |
| scimark_monte_carlo      | 118 ms                                                 | 60.9 ms: 1.94x faster                                                           |
| async_tree_io            | 1.77 sec                                               | 913 ms: 1.94x faster                                                            |
| nbody                    | 154 ms                                                 | 79.5 ms: 1.93x faster                                                           |
| scimark_sor              | 220 ms                                                 | 114 ms: 1.93x faster                                                            |
| richards                 | 79.3 ms                                                | 41.2 ms: 1.93x faster                                                           |
| raytrace                 | 507 ms                                                 | 267 ms: 1.90x faster                                                            |
| asyncio_tcp              | 922 ms                                                 | 505 ms: 1.83x faster                                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 560 ms: 1.81x faster                                                            |
| logging_silent           | 190 ns                                                 | 105 ns: 1.81x faster                                                            |
| comprehensions           | 28.8 us                                                | 16.4 us: 1.75x faster                                                           |
| deepcopy                 | 479 us                                                 | 279 us: 1.72x faster                                                            |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.69x faster                                                           |
| float                    | 117 ms                                                 | 70.8 ms: 1.65x faster                                                           |
| pickle_pure_python       | 484 us                                                 | 294 us: 1.65x faster                                                            |
| go                       | 240 ms                                                 | 146 ms: 1.65x faster                                                            |
| mako                     | 16.3 ms                                                | 9.93 ms: 1.64x faster                                                           |
| spectral_norm            | 170 ms                                                 | 104 ms: 1.64x faster                                                            |
| scimark_lu               | 176 ms                                                 | 108 ms: 1.63x faster                                                            |
| tomli_loads              | 3.14 sec                                               | 1.93 sec: 1.63x faster                                                          |
| pyflate                  | 716 ms                                                 | 449 ms: 1.60x faster                                                            |
| sqlglot_transpile        | 2.57 ms                                                | 1.62 ms: 1.59x faster                                                           |
| coroutines               | 35.1 ms                                                | 22.5 ms: 1.56x faster                                                           |
| pylint                   | 551 ms                                                 | 354 ms: 1.56x faster                                                            |
| hexiom                   | 10.4 ms                                                | 6.70 ms: 1.55x faster                                                           |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.19 ms: 1.55x faster                                                           |
| scimark_fft              | 466 ms                                                 | 303 ms: 1.54x faster                                                            |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                                            |
| deepcopy_reduce          | 4.17 us                                                | 2.73 us: 1.53x faster                                                           |
| logging_simple           | 8.30 us                                                | 5.45 us: 1.52x faster                                                           |
| logging_format           | 9.09 us                                                | 6.00 us: 1.51x faster                                                           |
| tornado_http             | 136 ms                                                 | 92.2 ms: 1.48x faster                                                           |
| fannkuch                 | 532 ms                                                 | 370 ms: 1.44x faster                                                            |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                                          |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.42x faster                                                          |
| regex_compile            | 188 ms                                                 | 133 ms: 1.41x faster                                                            |
| pprint_safe_repr         | 1.02 sec                                               | 725 ms: 1.40x faster                                                            |
| xml_etree_process        | 79.1 ms                                                | 56.6 ms: 1.40x faster                                                           |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                           |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                           |
| django_template          | 48.2 ms                                                | 35.6 ms: 1.35x faster                                                           |
| html5lib                 | 88.9 ms                                                | 65.7 ms: 1.35x faster                                                           |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.33x faster                                                          |
| thrift                   | 1.07 ms                                                | 811 us: 1.32x faster                                                            |
| genshi_text              | 31.8 ms                                                | 24.7 ms: 1.29x faster                                                           |
| 2to3                     | 348 ms                                                 | 273 ms: 1.28x faster                                                            |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                                           |
| sqlglot_normalize        | 143 ms                                                 | 113 ms: 1.27x faster                                                            |
| xml_etree_generate       | 99.4 ms                                                | 79.7 ms: 1.25x faster                                                           |
| sqlglot_optimize         | 69.2 ms                                                | 55.7 ms: 1.24x faster                                                           |
| nqueens                  | 106 ms                                                 | 85.8 ms: 1.23x faster                                                           |
| genshi_xml               | 66.0 ms                                                | 53.9 ms: 1.23x faster                                                           |
| dask                     | 441 ms                                                 | 365 ms: 1.21x faster                                                            |
| bench_thread_pool        | 986 us                                                 | 819 us: 1.20x faster                                                            |
| xml_etree_iterparse      | 115 ms                                                 | 99.5 ms: 1.16x faster                                                           |
| sympy_sum                | 196 ms                                                 | 170 ms: 1.16x faster                                                            |
| sympy_str                | 346 ms                                                 | 299 ms: 1.15x faster                                                            |
| sympy_integrate          | 25.8 ms                                                | 22.5 ms: 1.15x faster                                                           |
| meteor_contest           | 120 ms                                                 | 105 ms: 1.14x faster                                                            |
| xml_etree_parse          | 168 ms                                                 | 148 ms: 1.14x faster                                                            |
| docutils                 | 3.30 sec                                               | 2.91 sec: 1.13x faster                                                          |
| sympy_expand             | 566 ms                                                 | 507 ms: 1.11x faster                                                            |
| json                     | 5.69 ms                                                | 5.12 ms: 1.11x faster                                                           |
| json_loads               | 31.2 us                                                | 28.1 us: 1.11x faster                                                           |
| regex_v8                 | 27.8 ms                                                | 25.4 ms: 1.10x faster                                                           |
| mdp                      | 2.85 sec                                               | 2.71 sec: 1.05x faster                                                          |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                            |
| regex_dna                | 227 ms                                                 | 221 ms: 1.02x faster                                                            |
| asyncio_websockets       | 559 ms                                                 | 556 ms: 1.00x faster                                                            |
| gc_traversal             | 3.62 ms                                                | 3.67 ms: 1.01x slower                                                           |
| async_generators         | 444 ms                                                 | 450 ms: 1.02x slower                                                            |
| regex_effbot             | 3.63 ms                                                | 3.69 ms: 1.02x slower                                                           |
| create_gc_cycles         | 1.62 ms                                                | 1.75 ms: 1.08x slower                                                           |
| telco                    | 7.27 ms                                                | 7.96 ms: 1.10x slower                                                           |
| coverage                 | 79.4 ms                                                | 90.9 ms: 1.14x slower                                                           |
| python_startup_no_site   | 5.93 ms                                                | 7.16 ms: 1.21x slower                                                           |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                                    |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240730-3.14.0a0-71920f1-JIT/bm-20240730-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-71920f1.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.20x