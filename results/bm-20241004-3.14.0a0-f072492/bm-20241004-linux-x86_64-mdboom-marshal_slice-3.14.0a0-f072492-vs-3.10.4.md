# Results vs. 3.10.4

- fork: mdboom
- ref: marshal_slice
- machine: linux-x86_64
- commit hash: f072492
- commit date: 2024-10-04
- overall geometric mean: 1.38x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 257 ms: 1.35x faster                                           |
| docutils       | 3.30 sec                                               | 2.63 sec: 1.25x faster                                         |
| html5lib       | 88.9 ms                                                | 62.3 ms: 1.43x faster                                          |
| tornado_http   | 136 ms                                                 | 91.1 ms: 1.50x faster                                          |
| Geometric mean | (ref)                                                  | 1.38x faster                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 310 ms: 2.35x faster                                           |
| async_tree_memoization  | 870 ms                                                 | 398 ms: 2.18x faster                                           |
| async_tree_io           | 1.77 sec                                               | 888 ms: 1.99x faster                                           |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 570 ms: 1.78x faster                                           |
| Geometric mean          | (ref)                                                  | 2.06x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 89.0 ms: 1.72x faster                                          |
| float          | 117 ms                                                 | 77.5 ms: 1.51x faster                                          |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                           |
| Geometric mean | (ref)                                                  | 1.38x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.46x faster                                           |
| regex_v8       | 27.8 ms                                                | 25.1 ms: 1.11x faster                                          |
| regex_effbot   | 3.63 ms                                                | 3.54 ms: 1.03x faster                                          |
| Geometric mean | (ref)                                                  | 1.14x faster                                                   |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 306 us: 1.58x faster                                           |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                           |
| tomli_loads          | 3.14 sec                                               | 2.07 sec: 1.51x faster                                         |
| json_dumps           | 14.2 ms                                                | 10.3 ms: 1.38x faster                                          |
| xml_etree_process    | 79.1 ms                                                | 59.0 ms: 1.34x faster                                          |
| json_loads           | 31.2 us                                                | 26.9 us: 1.16x faster                                          |
| xml_etree_generate   | 99.4 ms                                                | 86.3 ms: 1.15x faster                                          |
| xml_etree_iterparse  | 115 ms                                                 | 105 ms: 1.10x faster                                           |
| xml_etree_parse      | 168 ms                                                 | 156 ms: 1.08x faster                                           |
| unpickle             | 14.4 us                                                | 15.1 us: 1.05x slower                                          |
| pickle               | 10.7 us                                                | 11.4 us: 1.07x slower                                          |
| pickle_dict          | 29.6 us                                                | 34.2 us: 1.15x slower                                          |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                   |

Benchmark hidden because not significant (2): pickle_list, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.2 ms: 1.31x faster                                          |
| python_startup_no_site | 5.93 ms                                                | 7.38 ms: 1.24x slower                                          |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.2 ms: 1.45x faster                                          |
| django_template | 48.2 ms                                                | 33.8 ms: 1.43x faster                                          |
| genshi_text     | 31.8 ms                                                | 22.5 ms: 1.42x faster                                          |
| genshi_xml      | 66.0 ms                                                | 50.1 ms: 1.32x faster                                          |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 158 us: 3.45x faster                                           |
| generators               | 80.1 ms                                                | 28.1 ms: 2.85x faster                                          |
| deltablue                | 7.91 ms                                                | 3.28 ms: 2.41x faster                                          |
| async_tree_none          | 728 ms                                                 | 310 ms: 2.35x faster                                           |
| async_tree_memoization   | 870 ms                                                 | 398 ms: 2.18x faster                                           |
| go                       | 240 ms                                                 | 119 ms: 2.01x faster                                           |
| async_tree_io            | 1.77 sec                                               | 888 ms: 1.99x faster                                           |
| deepcopy_memo            | 58.5 us                                                | 29.5 us: 1.98x faster                                          |
| asyncio_tcp              | 922 ms                                                 | 471 ms: 1.96x faster                                           |
| chaos                    | 115 ms                                                 | 59.1 ms: 1.95x faster                                          |
| raytrace                 | 507 ms                                                 | 267 ms: 1.90x faster                                           |
| crypto_pyaes             | 128 ms                                                 | 69.9 ms: 1.83x faster                                          |
| deepcopy                 | 479 us                                                 | 262 us: 1.83x faster                                           |
| logging_silent           | 190 ns                                                 | 104 ns: 1.82x faster                                           |
| richards_super           | 94.7 ms                                                | 52.6 ms: 1.80x faster                                          |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 570 ms: 1.78x faster                                           |
| scimark_sor              | 220 ms                                                 | 125 ms: 1.76x faster                                           |
| pylint                   | 551 ms                                                 | 316 ms: 1.74x faster                                           |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.73x faster                                          |
| nbody                    | 154 ms                                                 | 89.0 ms: 1.72x faster                                          |
| scimark_monte_carlo      | 118 ms                                                 | 69.0 ms: 1.71x faster                                          |
| richards                 | 79.3 ms                                                | 46.3 ms: 1.71x faster                                          |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.69x faster                                          |
| hexiom                   | 10.4 ms                                                | 6.27 ms: 1.66x faster                                          |
| sqlglot_transpile        | 2.57 ms                                                | 1.58 ms: 1.63x faster                                          |
| pickle_pure_python       | 484 us                                                 | 306 us: 1.58x faster                                           |
| scimark_lu               | 176 ms                                                 | 113 ms: 1.56x faster                                           |
| spectral_norm            | 170 ms                                                 | 110 ms: 1.54x faster                                           |
| deepcopy_reduce          | 4.17 us                                                | 2.70 us: 1.54x faster                                          |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                           |
| coroutines               | 35.1 ms                                                | 23.2 ms: 1.51x faster                                          |
| tomli_loads              | 3.14 sec                                               | 2.07 sec: 1.51x faster                                         |
| float                    | 117 ms                                                 | 77.5 ms: 1.51x faster                                          |
| tornado_http             | 136 ms                                                 | 91.1 ms: 1.50x faster                                          |
| pyflate                  | 716 ms                                                 | 479 ms: 1.49x faster                                           |
| logging_simple           | 8.30 us                                                | 5.58 us: 1.49x faster                                          |
| regex_compile            | 188 ms                                                 | 129 ms: 1.46x faster                                           |
| logging_format           | 9.09 us                                                | 6.22 us: 1.46x faster                                          |
| mako                     | 16.3 ms                                                | 11.2 ms: 1.45x faster                                          |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.78 sec: 1.44x faster                                         |
| pprint_safe_repr         | 1.02 sec                                               | 712 ms: 1.43x faster                                           |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.43x faster                                         |
| html5lib                 | 88.9 ms                                                | 62.3 ms: 1.43x faster                                          |
| django_template          | 48.2 ms                                                | 33.8 ms: 1.43x faster                                          |
| genshi_text              | 31.8 ms                                                | 22.5 ms: 1.42x faster                                          |
| pycparser                | 1.58 sec                                               | 1.12 sec: 1.41x faster                                         |
| thrift                   | 1.07 ms                                                | 767 us: 1.40x faster                                           |
| json_dumps               | 14.2 ms                                                | 10.3 ms: 1.38x faster                                          |
| sqlglot_normalize        | 143 ms                                                 | 105 ms: 1.36x faster                                           |
| 2to3                     | 348 ms                                                 | 257 ms: 1.35x faster                                           |
| fannkuch                 | 532 ms                                                 | 396 ms: 1.34x faster                                           |
| xml_etree_process        | 79.1 ms                                                | 59.0 ms: 1.34x faster                                          |
| nqueens                  | 106 ms                                                 | 79.2 ms: 1.34x faster                                          |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.33x faster                                           |
| dulwich_log              | 84.3 ms                                                | 63.9 ms: 1.32x faster                                          |
| genshi_xml               | 66.0 ms                                                | 50.1 ms: 1.32x faster                                          |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.92 ms: 1.32x faster                                          |
| python_startup           | 14.6 ms                                                | 11.2 ms: 1.31x faster                                          |
| sqlglot_optimize         | 69.2 ms                                                | 53.2 ms: 1.30x faster                                          |
| sympy_integrate          | 25.8 ms                                                | 19.9 ms: 1.30x faster                                          |
| sympy_str                | 346 ms                                                 | 268 ms: 1.29x faster                                           |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.28x faster                                          |
| docutils                 | 3.30 sec                                               | 2.63 sec: 1.25x faster                                         |
| sympy_expand             | 566 ms                                                 | 455 ms: 1.24x faster                                           |
| scimark_fft              | 466 ms                                                 | 376 ms: 1.24x faster                                           |
| json_loads               | 31.2 us                                                | 26.9 us: 1.16x faster                                          |
| bench_thread_pool        | 986 us                                                 | 851 us: 1.16x faster                                           |
| xml_etree_generate       | 99.4 ms                                                | 86.3 ms: 1.15x faster                                          |
| json                     | 5.69 ms                                                | 5.03 ms: 1.13x faster                                          |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                           |
| mdp                      | 2.85 sec                                               | 2.52 sec: 1.13x faster                                         |
| unpack_sequence          | 60.0 ns                                                | 53.3 ns: 1.13x faster                                          |
| regex_v8                 | 27.8 ms                                                | 25.1 ms: 1.11x faster                                          |
| xml_etree_iterparse      | 115 ms                                                 | 105 ms: 1.10x faster                                           |
| sqlite_synth             | 3.02 us                                                | 2.80 us: 1.08x faster                                          |
| xml_etree_parse          | 168 ms                                                 | 156 ms: 1.08x faster                                           |
| regex_effbot             | 3.63 ms                                                | 3.54 ms: 1.03x faster                                          |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                           |
| async_generators         | 444 ms                                                 | 435 ms: 1.02x faster                                           |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                           |
| gc_traversal             | 3.62 ms                                                | 3.68 ms: 1.02x slower                                          |
| unpickle                 | 14.4 us                                                | 15.1 us: 1.05x slower                                          |
| pickle                   | 10.7 us                                                | 11.4 us: 1.07x slower                                          |
| coverage                 | 79.4 ms                                                | 85.2 ms: 1.07x slower                                          |
| create_gc_cycles         | 1.62 ms                                                | 1.75 ms: 1.08x slower                                          |
| telco                    | 7.27 ms                                                | 8.04 ms: 1.11x slower                                          |
| pickle_dict              | 29.6 us                                                | 34.2 us: 1.15x slower                                          |
| python_startup_no_site   | 5.93 ms                                                | 7.38 ms: 1.24x slower                                          |
| bench_mp_pool            | 24.0 ms                                                | 60.3 ms: 2.51x slower                                          |
| Geometric mean           | (ref)                                                  | 1.38x faster                                                   |

Benchmark hidden because not significant (3): regex_dna, pickle_list, unpickle_list
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20241004-3.14.0a0-f072492/bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.12x