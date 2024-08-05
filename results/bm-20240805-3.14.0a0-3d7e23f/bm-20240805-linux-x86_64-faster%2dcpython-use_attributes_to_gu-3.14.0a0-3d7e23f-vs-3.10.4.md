# Results vs. 3.10.4

- fork: faster-cpython
- ref: use_attributes_to_gu
- machine: linux-x86_64
- commit hash: 3d7e23f
- commit date: 2024-08-05
- overall geometric mean: 1.43x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240805-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-3d7e23f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 263 ms: 1.33x faster                                                            |
| docutils       | 3.30 sec                                               | 2.74 sec: 1.20x faster                                                          |
| html5lib       | 88.9 ms                                                | 66.0 ms: 1.35x faster                                                           |
| tornado_http   | 136 ms                                                 | 89.7 ms: 1.52x faster                                                           |
| Geometric mean | (ref)                                                  | 1.34x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240805-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-3d7e23f |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 323 ms: 2.25x faster                                                            |
| async_tree_memoization  | 870 ms                                                 | 417 ms: 2.09x faster                                                            |
| async_tree_io           | 1.77 sec                                               | 899 ms: 1.97x faster                                                            |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 558 ms: 1.82x faster                                                            |
| Geometric mean          | (ref)                                                  | 2.02x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240805-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-3d7e23f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 86.2 ms: 1.78x faster                                                           |
| float          | 117 ms                                                 | 77.8 ms: 1.51x faster                                                           |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                  | 1.40x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240805-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-3d7e23f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 132 ms: 1.43x faster                                                            |
| regex_v8       | 27.8 ms                                                | 25.8 ms: 1.08x faster                                                           |
| regex_dna      | 227 ms                                                 | 229 ms: 1.01x slower                                                            |
| regex_effbot   | 3.63 ms                                                | 3.87 ms: 1.07x slower                                                           |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240805-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-3d7e23f |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 302 us: 1.61x faster                                                            |
| unpickle_pure_python | 331 us                                                 | 211 us: 1.57x faster                                                            |
| tomli_loads          | 3.14 sec                                               | 2.03 sec: 1.55x faster                                                          |
| xml_etree_process    | 79.1 ms                                                | 59.4 ms: 1.33x faster                                                           |
| json_dumps           | 14.2 ms                                                | 10.7 ms: 1.33x faster                                                           |
| xml_etree_generate   | 99.4 ms                                                | 85.5 ms: 1.16x faster                                                           |
| json_loads           | 31.2 us                                                | 27.8 us: 1.12x faster                                                           |
| xml_etree_iterparse  | 115 ms                                                 | 105 ms: 1.10x faster                                                            |
| xml_etree_parse      | 168 ms                                                 | 156 ms: 1.08x faster                                                            |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240805-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-3d7e23f |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                           |
| python_startup_no_site | 5.93 ms                                                | 7.07 ms: 1.19x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240805-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-3d7e23f |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.3 ms: 1.45x faster                                                           |
| django_template | 48.2 ms                                                | 34.3 ms: 1.40x faster                                                           |
| genshi_text     | 31.8 ms                                                | 23.1 ms: 1.38x faster                                                           |
| genshi_xml      | 66.0 ms                                                | 52.5 ms: 1.26x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.37x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240805-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-3d7e23f |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 163 us: 3.34x faster                                                            |
| generators               | 80.1 ms                                                | 27.8 ms: 2.88x faster                                                           |
| deltablue                | 7.91 ms                                                | 3.19 ms: 2.48x faster                                                           |
| async_tree_none          | 728 ms                                                 | 323 ms: 2.25x faster                                                            |
| async_tree_memoization   | 870 ms                                                 | 417 ms: 2.09x faster                                                            |
| go                       | 240 ms                                                 | 117 ms: 2.06x faster                                                            |
| deepcopy_memo            | 58.5 us                                                | 28.6 us: 2.04x faster                                                           |
| chaos                    | 115 ms                                                 | 57.7 ms: 2.00x faster                                                           |
| raytrace                 | 507 ms                                                 | 257 ms: 1.97x faster                                                            |
| async_tree_io            | 1.77 sec                                               | 899 ms: 1.97x faster                                                            |
| logging_silent           | 190 ns                                                 | 98.0 ns: 1.94x faster                                                           |
| asyncio_tcp              | 922 ms                                                 | 485 ms: 1.90x faster                                                            |
| richards_super           | 94.7 ms                                                | 51.6 ms: 1.84x faster                                                           |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 558 ms: 1.82x faster                                                            |
| deepcopy                 | 479 us                                                 | 263 us: 1.82x faster                                                            |
| nbody                    | 154 ms                                                 | 86.2 ms: 1.78x faster                                                           |
| crypto_pyaes             | 128 ms                                                 | 72.2 ms: 1.77x faster                                                           |
| scimark_monte_carlo      | 118 ms                                                 | 66.8 ms: 1.77x faster                                                           |
| scimark_sor              | 220 ms                                                 | 125 ms: 1.76x faster                                                            |
| pylint                   | 551 ms                                                 | 317 ms: 1.74x faster                                                            |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.73x faster                                                           |
| richards                 | 79.3 ms                                                | 45.9 ms: 1.73x faster                                                           |
| sqlglot_parse            | 2.17 ms                                                | 1.27 ms: 1.71x faster                                                           |
| hexiom                   | 10.4 ms                                                | 6.18 ms: 1.68x faster                                                           |
| sqlglot_transpile        | 2.57 ms                                                | 1.56 ms: 1.65x faster                                                           |
| pickle_pure_python       | 484 us                                                 | 302 us: 1.61x faster                                                            |
| unpickle_pure_python     | 331 us                                                 | 211 us: 1.57x faster                                                            |
| scimark_lu               | 176 ms                                                 | 113 ms: 1.57x faster                                                            |
| tomli_loads              | 3.14 sec                                               | 2.03 sec: 1.55x faster                                                          |
| deepcopy_reduce          | 4.17 us                                                | 2.71 us: 1.54x faster                                                           |
| tornado_http             | 136 ms                                                 | 89.7 ms: 1.52x faster                                                           |
| pyflate                  | 716 ms                                                 | 473 ms: 1.51x faster                                                            |
| spectral_norm            | 170 ms                                                 | 112 ms: 1.51x faster                                                            |
| logging_simple           | 8.30 us                                                | 5.51 us: 1.51x faster                                                           |
| coroutines               | 35.1 ms                                                | 23.3 ms: 1.51x faster                                                           |
| float                    | 117 ms                                                 | 77.8 ms: 1.51x faster                                                           |
| logging_format           | 9.09 us                                                | 6.14 us: 1.48x faster                                                           |
| mako                     | 16.3 ms                                                | 11.3 ms: 1.45x faster                                                           |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.79 sec: 1.44x faster                                                          |
| regex_compile            | 188 ms                                                 | 132 ms: 1.43x faster                                                            |
| django_template          | 48.2 ms                                                | 34.3 ms: 1.40x faster                                                           |
| pprint_pformat           | 2.10 sec                                               | 1.50 sec: 1.40x faster                                                          |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                           |
| pprint_safe_repr         | 1.02 sec                                               | 737 ms: 1.38x faster                                                            |
| genshi_text              | 31.8 ms                                                | 23.1 ms: 1.38x faster                                                           |
| thrift                   | 1.07 ms                                                | 781 us: 1.37x faster                                                            |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.37x faster                                                          |
| html5lib                 | 88.9 ms                                                | 66.0 ms: 1.35x faster                                                           |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.81 ms: 1.34x faster                                                           |
| sqlglot_normalize        | 143 ms                                                 | 106 ms: 1.34x faster                                                            |
| nqueens                  | 106 ms                                                 | 79.3 ms: 1.33x faster                                                           |
| xml_etree_process        | 79.1 ms                                                | 59.4 ms: 1.33x faster                                                           |
| json_dumps               | 14.2 ms                                                | 10.7 ms: 1.33x faster                                                           |
| 2to3                     | 348 ms                                                 | 263 ms: 1.33x faster                                                            |
| sympy_integrate          | 25.8 ms                                                | 19.5 ms: 1.32x faster                                                           |
| sympy_sum                | 196 ms                                                 | 150 ms: 1.31x faster                                                            |
| fannkuch                 | 532 ms                                                 | 408 ms: 1.30x faster                                                            |
| sqlglot_optimize         | 69.2 ms                                                | 53.1 ms: 1.30x faster                                                           |
| pathlib                  | 20.5 ms                                                | 15.7 ms: 1.30x faster                                                           |
| scimark_fft              | 466 ms                                                 | 358 ms: 1.30x faster                                                            |
| sympy_str                | 346 ms                                                 | 271 ms: 1.28x faster                                                            |
| genshi_xml               | 66.0 ms                                                | 52.5 ms: 1.26x faster                                                           |
| bench_thread_pool        | 986 us                                                 | 785 us: 1.26x faster                                                            |
| dask                     | 441 ms                                                 | 353 ms: 1.25x faster                                                            |
| sympy_expand             | 566 ms                                                 | 456 ms: 1.24x faster                                                            |
| docutils                 | 3.30 sec                                               | 2.74 sec: 1.20x faster                                                          |
| xml_etree_generate       | 99.4 ms                                                | 85.5 ms: 1.16x faster                                                           |
| json_loads               | 31.2 us                                                | 27.8 us: 1.12x faster                                                           |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                            |
| xml_etree_iterparse      | 115 ms                                                 | 105 ms: 1.10x faster                                                            |
| json                     | 5.69 ms                                                | 5.16 ms: 1.10x faster                                                           |
| regex_v8                 | 27.8 ms                                                | 25.8 ms: 1.08x faster                                                           |
| xml_etree_parse          | 168 ms                                                 | 156 ms: 1.08x faster                                                            |
| mdp                      | 2.85 sec                                               | 2.69 sec: 1.06x faster                                                          |
| async_generators         | 444 ms                                                 | 435 ms: 1.02x faster                                                            |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                            |
| regex_dna                | 227 ms                                                 | 229 ms: 1.01x slower                                                            |
| gc_traversal             | 3.62 ms                                                | 3.75 ms: 1.04x slower                                                           |
| regex_effbot             | 3.63 ms                                                | 3.87 ms: 1.07x slower                                                           |
| create_gc_cycles         | 1.62 ms                                                | 1.75 ms: 1.08x slower                                                           |
| telco                    | 7.27 ms                                                | 8.12 ms: 1.12x slower                                                           |
| coverage                 | 79.4 ms                                                | 90.3 ms: 1.14x slower                                                           |
| python_startup_no_site   | 5.93 ms                                                | 7.07 ms: 1.19x slower                                                           |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                                    |

Benchmark hidden because not significant (2): bench_mp_pool, asyncio_websockets
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240805-3.14.0a0-3d7e23f/bm-20240805-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-3d7e23f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.12x