# Results vs. 3.10.4

- fork: faster-cpython
- ref: mark_load_fast_defer
- machine: linux-x86_64
- commit hash: 9992ab7
- commit date: 2024-10-09
- overall geometric mean: 1.434x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241009-linux-x86_64-faster%2dcpython-mark_load_fast_defer-3.14.0a0-9992ab7 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 256 ms: 1.36x faster                                                            |
| docutils       | 3.30 sec                                               | 2.66 sec: 1.24x faster                                                          |
| html5lib       | 88.9 ms                                                | 63.2 ms: 1.41x faster                                                           |
| tornado_http   | 136 ms                                                 | 90.8 ms: 1.50x faster                                                           |
| Geometric mean | (ref)                                                  | 1.37x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241009-linux-x86_64-faster%2dcpython-mark_load_fast_defer-3.14.0a0-9992ab7 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 315 ms: 2.31x faster                                                            |
| async_tree_memoization  | 870 ms                                                 | 393 ms: 2.22x faster                                                            |
| async_tree_io           | 1.77 sec                                               | 857 ms: 2.06x faster                                                            |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 567 ms: 1.79x faster                                                            |
| Geometric mean          | (ref)                                                  | 2.09x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241009-linux-x86_64-faster%2dcpython-mark_load_fast_defer-3.14.0a0-9992ab7 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 84.1 ms: 1.83x faster                                                           |
| float          | 117 ms                                                 | 76.6 ms: 1.53x faster                                                           |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                  | 1.42x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241009-linux-x86_64-faster%2dcpython-mark_load_fast_defer-3.14.0a0-9992ab7 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.47x faster                                                            |
| regex_v8       | 27.8 ms                                                | 24.3 ms: 1.14x faster                                                           |
| regex_dna      | 227 ms                                                 | 221 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                  | 1.14x faster                                                                    |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241009-linux-x86_64-faster%2dcpython-mark_load_fast_defer-3.14.0a0-9992ab7 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 303 us: 1.60x faster                                                            |
| unpickle_pure_python | 331 us                                                 | 214 us: 1.54x faster                                                            |
| tomli_loads          | 3.14 sec                                               | 2.11 sec: 1.49x faster                                                          |
| json_dumps           | 14.2 ms                                                | 10.3 ms: 1.37x faster                                                           |
| xml_etree_process    | 79.1 ms                                                | 58.2 ms: 1.36x faster                                                           |
| xml_etree_generate   | 99.4 ms                                                | 84.3 ms: 1.18x faster                                                           |
| json_loads           | 31.2 us                                                | 26.9 us: 1.16x faster                                                           |
| xml_etree_iterparse  | 115 ms                                                 | 103 ms: 1.12x faster                                                            |
| xml_etree_parse      | 168 ms                                                 | 154 ms: 1.09x faster                                                            |
| pickle               | 10.7 us                                                | 11.4 us: 1.07x slower                                                           |
| unpickle             | 14.4 us                                                | 16.6 us: 1.15x slower                                                           |
| pickle_dict          | 29.6 us                                                | 34.4 us: 1.16x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                                    |

Benchmark hidden because not significant (2): unpickle_list, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241009-linux-x86_64-faster%2dcpython-mark_load_fast_defer-3.14.0a0-9992ab7 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                           |
| python_startup_no_site | 5.93 ms                                                | 6.99 ms: 1.18x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.09x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241009-linux-x86_64-faster%2dcpython-mark_load_fast_defer-3.14.0a0-9992ab7 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 21.9 ms: 1.46x faster                                                           |
| mako            | 16.3 ms                                                | 11.3 ms: 1.44x faster                                                           |
| django_template | 48.2 ms                                                | 34.1 ms: 1.41x faster                                                           |
| genshi_xml      | 66.0 ms                                                | 49.1 ms: 1.35x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.41x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241009-linux-x86_64-faster%2dcpython-mark_load_fast_defer-3.14.0a0-9992ab7 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 159 us: 3.43x faster                                                            |
| generators               | 80.1 ms                                                | 27.6 ms: 2.90x faster                                                           |
| deltablue                | 7.91 ms                                                | 3.29 ms: 2.40x faster                                                           |
| async_tree_none          | 728 ms                                                 | 315 ms: 2.31x faster                                                            |
| async_tree_memoization   | 870 ms                                                 | 393 ms: 2.22x faster                                                            |
| async_tree_io            | 1.77 sec                                               | 857 ms: 2.06x faster                                                            |
| go                       | 240 ms                                                 | 120 ms: 2.01x faster                                                            |
| chaos                    | 115 ms                                                 | 59.7 ms: 1.94x faster                                                           |
| asyncio_tcp              | 922 ms                                                 | 479 ms: 1.92x faster                                                            |
| deepcopy_memo            | 58.5 us                                                | 30.5 us: 1.92x faster                                                           |
| raytrace                 | 507 ms                                                 | 266 ms: 1.91x faster                                                            |
| deepcopy                 | 479 us                                                 | 258 us: 1.86x faster                                                            |
| logging_silent           | 190 ns                                                 | 103 ns: 1.85x faster                                                            |
| nbody                    | 154 ms                                                 | 84.1 ms: 1.83x faster                                                           |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 567 ms: 1.79x faster                                                            |
| richards_super           | 94.7 ms                                                | 53.0 ms: 1.79x faster                                                           |
| scimark_sor              | 220 ms                                                 | 124 ms: 1.77x faster                                                            |
| crypto_pyaes             | 128 ms                                                 | 72.3 ms: 1.77x faster                                                           |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                                           |
| scimark_monte_carlo      | 118 ms                                                 | 68.5 ms: 1.73x faster                                                           |
| pylint                   | 551 ms                                                 | 320 ms: 1.72x faster                                                            |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.69x faster                                                           |
| richards                 | 79.3 ms                                                | 46.9 ms: 1.69x faster                                                           |
| hexiom                   | 10.4 ms                                                | 6.16 ms: 1.69x faster                                                           |
| sqlglot_transpile        | 2.57 ms                                                | 1.58 ms: 1.62x faster                                                           |
| pickle_pure_python       | 484 us                                                 | 303 us: 1.60x faster                                                            |
| scimark_lu               | 176 ms                                                 | 111 ms: 1.59x faster                                                            |
| deepcopy_reduce          | 4.17 us                                                | 2.64 us: 1.58x faster                                                           |
| pyflate                  | 716 ms                                                 | 462 ms: 1.55x faster                                                            |
| coroutines               | 35.1 ms                                                | 22.7 ms: 1.54x faster                                                           |
| unpickle_pure_python     | 331 us                                                 | 214 us: 1.54x faster                                                            |
| float                    | 117 ms                                                 | 76.6 ms: 1.53x faster                                                           |
| spectral_norm            | 170 ms                                                 | 113 ms: 1.51x faster                                                            |
| tornado_http             | 136 ms                                                 | 90.8 ms: 1.50x faster                                                           |
| tomli_loads              | 3.14 sec                                               | 2.11 sec: 1.49x faster                                                          |
| logging_simple           | 8.30 us                                                | 5.65 us: 1.47x faster                                                           |
| regex_compile            | 188 ms                                                 | 129 ms: 1.47x faster                                                            |
| genshi_text              | 31.8 ms                                                | 21.9 ms: 1.46x faster                                                           |
| pprint_pformat           | 2.10 sec                                               | 1.46 sec: 1.44x faster                                                          |
| mako                     | 16.3 ms                                                | 11.3 ms: 1.44x faster                                                           |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.79 sec: 1.44x faster                                                          |
| pprint_safe_repr         | 1.02 sec                                               | 710 ms: 1.43x faster                                                            |
| logging_format           | 9.09 us                                                | 6.39 us: 1.42x faster                                                           |
| django_template          | 48.2 ms                                                | 34.1 ms: 1.41x faster                                                           |
| html5lib                 | 88.9 ms                                                | 63.2 ms: 1.41x faster                                                           |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                           |
| thrift                   | 1.07 ms                                                | 778 us: 1.38x faster                                                            |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.37x faster                                                          |
| json_dumps               | 14.2 ms                                                | 10.3 ms: 1.37x faster                                                           |
| 2to3                     | 348 ms                                                 | 256 ms: 1.36x faster                                                            |
| xml_etree_process        | 79.1 ms                                                | 58.2 ms: 1.36x faster                                                           |
| genshi_xml               | 66.0 ms                                                | 49.1 ms: 1.35x faster                                                           |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.81 ms: 1.34x faster                                                           |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.34x faster                                                            |
| sqlglot_normalize        | 143 ms                                                 | 107 ms: 1.34x faster                                                            |
| fannkuch                 | 532 ms                                                 | 399 ms: 1.33x faster                                                            |
| nqueens                  | 106 ms                                                 | 80.0 ms: 1.32x faster                                                           |
| sympy_integrate          | 25.8 ms                                                | 19.5 ms: 1.32x faster                                                           |
| sqlglot_optimize         | 69.2 ms                                                | 52.9 ms: 1.31x faster                                                           |
| dulwich_log              | 84.3 ms                                                | 64.7 ms: 1.30x faster                                                           |
| sympy_str                | 346 ms                                                 | 266 ms: 1.30x faster                                                            |
| scimark_fft              | 466 ms                                                 | 365 ms: 1.28x faster                                                            |
| pathlib                  | 20.5 ms                                                | 16.3 ms: 1.26x faster                                                           |
| unpack_sequence          | 60.0 ns                                                | 48.1 ns: 1.25x faster                                                           |
| bench_thread_pool        | 986 us                                                 | 791 us: 1.25x faster                                                            |
| sympy_expand             | 566 ms                                                 | 456 ms: 1.24x faster                                                            |
| docutils                 | 3.30 sec                                               | 2.66 sec: 1.24x faster                                                          |
| xml_etree_generate       | 99.4 ms                                                | 84.3 ms: 1.18x faster                                                           |
| json                     | 5.69 ms                                                | 4.87 ms: 1.17x faster                                                           |
| json_loads               | 31.2 us                                                | 26.9 us: 1.16x faster                                                           |
| regex_v8                 | 27.8 ms                                                | 24.3 ms: 1.14x faster                                                           |
| xml_etree_iterparse      | 115 ms                                                 | 103 ms: 1.12x faster                                                            |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                            |
| mdp                      | 2.85 sec                                               | 2.58 sec: 1.11x faster                                                          |
| xml_etree_parse          | 168 ms                                                 | 154 ms: 1.09x faster                                                            |
| sqlite_synth             | 3.02 us                                                | 2.88 us: 1.05x faster                                                           |
| regex_dna                | 227 ms                                                 | 221 ms: 1.02x faster                                                            |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                            |
| async_generators         | 444 ms                                                 | 435 ms: 1.02x faster                                                            |
| create_gc_cycles         | 1.62 ms                                                | 1.72 ms: 1.06x slower                                                           |
| pickle                   | 10.7 us                                                | 11.4 us: 1.07x slower                                                           |
| coverage                 | 79.4 ms                                                | 87.2 ms: 1.10x slower                                                           |
| gc_traversal             | 3.62 ms                                                | 4.00 ms: 1.10x slower                                                           |
| unpickle                 | 14.4 us                                                | 16.6 us: 1.15x slower                                                           |
| telco                    | 7.27 ms                                                | 8.40 ms: 1.16x slower                                                           |
| pickle_dict              | 29.6 us                                                | 34.4 us: 1.16x slower                                                           |
| python_startup_no_site   | 5.93 ms                                                | 6.99 ms: 1.18x slower                                                           |
| Geometric mean           | (ref)                                                  | 1.40x faster                                                                    |

Benchmark hidden because not significant (5): unpickle_list, asyncio_websockets, bench_mp_pool, regex_effbot, pickle_list
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20241009-3.14.0a0-9992ab7/bm-20241009-linux-x86_64-faster%2dcpython-mark_load_fast_defer-3.14.0a0-9992ab7.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.434x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: 1.12x