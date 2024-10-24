# Results vs. 3.10.4

- fork: faster-cpython
- ref: specialize_shadowed_
- machine: linux-x86_64
- commit hash: 975089f
- commit date: 2024-08-21
- overall geometric mean: 1.43x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240821-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-975089f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 255 ms: 1.37x faster                                                            |
| docutils       | 3.30 sec                                               | 2.70 sec: 1.22x faster                                                          |
| html5lib       | 88.9 ms                                                | 66.2 ms: 1.34x faster                                                           |
| tornado_http   | 136 ms                                                 | 90.1 ms: 1.51x faster                                                           |
| Geometric mean | (ref)                                                  | 1.36x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240821-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-975089f |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 324 ms: 2.25x faster                                                            |
| async_tree_memoization  | 870 ms                                                 | 392 ms: 2.22x faster                                                            |
| async_tree_io           | 1.77 sec                                               | 927 ms: 1.91x faster                                                            |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 558 ms: 1.82x faster                                                            |
| Geometric mean          | (ref)                                                  | 2.04x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240821-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-975089f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 86.8 ms: 1.77x faster                                                           |
| float          | 117 ms                                                 | 77.7 ms: 1.51x faster                                                           |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                  | 1.40x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240821-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-975089f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.47x faster                                                            |
| regex_v8       | 27.8 ms                                                | 23.7 ms: 1.17x faster                                                           |
| regex_dna      | 227 ms                                                 | 225 ms: 1.01x faster                                                            |
| regex_effbot   | 3.63 ms                                                | 3.69 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                  | 1.14x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240821-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-975089f |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 302 us: 1.61x faster                                                            |
| unpickle_pure_python | 331 us                                                 | 211 us: 1.57x faster                                                            |
| tomli_loads          | 3.14 sec                                               | 2.08 sec: 1.51x faster                                                          |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.36x faster                                                           |
| xml_etree_process    | 79.1 ms                                                | 58.6 ms: 1.35x faster                                                           |
| xml_etree_generate   | 99.4 ms                                                | 84.4 ms: 1.18x faster                                                           |
| json_loads           | 31.2 us                                                | 28.6 us: 1.09x faster                                                           |
| xml_etree_iterparse  | 115 ms                                                 | 106 ms: 1.09x faster                                                            |
| xml_etree_parse      | 168 ms                                                 | 156 ms: 1.08x faster                                                            |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240821-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-975089f |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                           |
| python_startup_no_site | 5.93 ms                                                | 7.05 ms: 1.19x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240821-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-975089f |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 33.6 ms: 1.43x faster                                                           |
| mako            | 16.3 ms                                                | 11.4 ms: 1.43x faster                                                           |
| genshi_text     | 31.8 ms                                                | 22.6 ms: 1.41x faster                                                           |
| genshi_xml      | 66.0 ms                                                | 50.5 ms: 1.31x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.39x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240821-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-975089f |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 159 us: 3.43x faster                                                            |
| generators               | 80.1 ms                                                | 27.9 ms: 2.87x faster                                                           |
| deltablue                | 7.91 ms                                                | 3.20 ms: 2.47x faster                                                           |
| async_tree_none          | 728 ms                                                 | 324 ms: 2.25x faster                                                            |
| async_tree_memoization   | 870 ms                                                 | 392 ms: 2.22x faster                                                            |
| deepcopy_memo            | 58.5 us                                                | 29.6 us: 1.98x faster                                                           |
| chaos                    | 115 ms                                                 | 58.7 ms: 1.97x faster                                                           |
| raytrace                 | 507 ms                                                 | 260 ms: 1.95x faster                                                            |
| asyncio_tcp              | 922 ms                                                 | 477 ms: 1.93x faster                                                            |
| logging_silent           | 190 ns                                                 | 99.3 ns: 1.91x faster                                                           |
| async_tree_io            | 1.77 sec                                               | 927 ms: 1.91x faster                                                            |
| deepcopy                 | 479 us                                                 | 260 us: 1.84x faster                                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 558 ms: 1.82x faster                                                            |
| richards_super           | 94.7 ms                                                | 52.0 ms: 1.82x faster                                                           |
| scimark_sor              | 220 ms                                                 | 124 ms: 1.77x faster                                                            |
| nbody                    | 154 ms                                                 | 86.8 ms: 1.77x faster                                                           |
| crypto_pyaes             | 128 ms                                                 | 72.6 ms: 1.76x faster                                                           |
| scimark_monte_carlo      | 118 ms                                                 | 67.8 ms: 1.74x faster                                                           |
| pylint                   | 551 ms                                                 | 319 ms: 1.73x faster                                                            |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.73x faster                                                           |
| richards                 | 79.3 ms                                                | 46.1 ms: 1.72x faster                                                           |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.69x faster                                                           |
| hexiom                   | 10.4 ms                                                | 6.22 ms: 1.67x faster                                                           |
| sqlglot_transpile        | 2.57 ms                                                | 1.57 ms: 1.64x faster                                                           |
| pickle_pure_python       | 484 us                                                 | 302 us: 1.61x faster                                                            |
| scimark_lu               | 176 ms                                                 | 112 ms: 1.57x faster                                                            |
| unpickle_pure_python     | 331 us                                                 | 211 us: 1.57x faster                                                            |
| deepcopy_reduce          | 4.17 us                                                | 2.66 us: 1.57x faster                                                           |
| pyflate                  | 716 ms                                                 | 470 ms: 1.52x faster                                                            |
| tornado_http             | 136 ms                                                 | 90.1 ms: 1.51x faster                                                           |
| tomli_loads              | 3.14 sec                                               | 2.08 sec: 1.51x faster                                                          |
| spectral_norm            | 170 ms                                                 | 113 ms: 1.51x faster                                                            |
| float                    | 117 ms                                                 | 77.7 ms: 1.51x faster                                                           |
| coroutines               | 35.1 ms                                                | 23.3 ms: 1.51x faster                                                           |
| logging_simple           | 8.30 us                                                | 5.54 us: 1.50x faster                                                           |
| go                       | 240 ms                                                 | 161 ms: 1.49x faster                                                            |
| logging_format           | 9.09 us                                                | 6.12 us: 1.49x faster                                                           |
| regex_compile            | 188 ms                                                 | 128 ms: 1.47x faster                                                            |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.79 sec: 1.44x faster                                                          |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.43x faster                                                          |
| django_template          | 48.2 ms                                                | 33.6 ms: 1.43x faster                                                           |
| mako                     | 16.3 ms                                                | 11.4 ms: 1.43x faster                                                           |
| pprint_safe_repr         | 1.02 sec                                               | 717 ms: 1.42x faster                                                            |
| genshi_text              | 31.8 ms                                                | 22.6 ms: 1.41x faster                                                           |
| thrift                   | 1.07 ms                                                | 766 us: 1.40x faster                                                            |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                           |
| pycparser                | 1.58 sec                                               | 1.14 sec: 1.38x faster                                                          |
| 2to3                     | 348 ms                                                 | 255 ms: 1.37x faster                                                            |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.36x faster                                                           |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.78 ms: 1.35x faster                                                           |
| xml_etree_process        | 79.1 ms                                                | 58.6 ms: 1.35x faster                                                           |
| html5lib                 | 88.9 ms                                                | 66.2 ms: 1.34x faster                                                           |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.34x faster                                                            |
| sqlglot_normalize        | 143 ms                                                 | 107 ms: 1.33x faster                                                            |
| sympy_integrate          | 25.8 ms                                                | 19.4 ms: 1.33x faster                                                           |
| fannkuch                 | 532 ms                                                 | 404 ms: 1.32x faster                                                            |
| genshi_xml               | 66.0 ms                                                | 50.5 ms: 1.31x faster                                                           |
| nqueens                  | 106 ms                                                 | 81.3 ms: 1.30x faster                                                           |
| sqlglot_optimize         | 69.2 ms                                                | 53.3 ms: 1.30x faster                                                           |
| sympy_str                | 346 ms                                                 | 268 ms: 1.29x faster                                                            |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.28x faster                                                           |
| scimark_fft              | 466 ms                                                 | 364 ms: 1.28x faster                                                            |
| bench_thread_pool        | 986 us                                                 | 783 us: 1.26x faster                                                            |
| sympy_expand             | 566 ms                                                 | 456 ms: 1.24x faster                                                            |
| docutils                 | 3.30 sec                                               | 2.70 sec: 1.22x faster                                                          |
| xml_etree_generate       | 99.4 ms                                                | 84.4 ms: 1.18x faster                                                           |
| regex_v8                 | 27.8 ms                                                | 23.7 ms: 1.17x faster                                                           |
| mdp                      | 2.85 sec                                               | 2.52 sec: 1.13x faster                                                          |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                            |
| json_loads               | 31.2 us                                                | 28.6 us: 1.09x faster                                                           |
| xml_etree_iterparse      | 115 ms                                                 | 106 ms: 1.09x faster                                                            |
| xml_etree_parse          | 168 ms                                                 | 156 ms: 1.08x faster                                                            |
| json                     | 5.69 ms                                                | 5.35 ms: 1.06x faster                                                           |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                            |
| async_generators         | 444 ms                                                 | 435 ms: 1.02x faster                                                            |
| regex_dna                | 227 ms                                                 | 225 ms: 1.01x faster                                                            |
| regex_effbot             | 3.63 ms                                                | 3.69 ms: 1.02x slower                                                           |
| gc_traversal             | 3.62 ms                                                | 3.86 ms: 1.06x slower                                                           |
| coverage                 | 79.4 ms                                                | 85.3 ms: 1.07x slower                                                           |
| create_gc_cycles         | 1.62 ms                                                | 1.76 ms: 1.08x slower                                                           |
| telco                    | 7.27 ms                                                | 8.12 ms: 1.12x slower                                                           |
| python_startup_no_site   | 5.93 ms                                                | 7.05 ms: 1.19x slower                                                           |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                                    |

Benchmark hidden because not significant (2): asyncio_websockets, bench_mp_pool
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240821-3.14.0a0-975089f/bm-20240821-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-975089f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.13x