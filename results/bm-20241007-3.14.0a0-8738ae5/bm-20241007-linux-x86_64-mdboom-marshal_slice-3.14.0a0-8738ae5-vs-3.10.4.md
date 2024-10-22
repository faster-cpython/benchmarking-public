# Results vs. 3.10.4

- fork: mdboom
- ref: marshal_slice
- machine: linux-x86_64
- commit hash: 8738ae5
- commit date: 2024-10-07
- overall geometric mean: 1.38x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 255 ms: 1.37x faster                                           |
| docutils       | 3.30 sec                                               | 2.64 sec: 1.25x faster                                         |
| html5lib       | 88.9 ms                                                | 61.4 ms: 1.45x faster                                          |
| tornado_http   | 136 ms                                                 | 90.2 ms: 1.51x faster                                          |
| Geometric mean | (ref)                                                  | 1.39x faster                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 322 ms: 2.26x faster                                           |
| async_tree_memoization  | 870 ms                                                 | 391 ms: 2.23x faster                                           |
| async_tree_io           | 1.77 sec                                               | 929 ms: 1.90x faster                                           |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 563 ms: 1.80x faster                                           |
| Geometric mean          | (ref)                                                  | 2.04x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 86.9 ms: 1.77x faster                                          |
| float          | 117 ms                                                 | 76.8 ms: 1.52x faster                                          |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                           |
| Geometric mean | (ref)                                                  | 1.40x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.46x faster                                           |
| regex_v8       | 27.8 ms                                                | 25.4 ms: 1.09x faster                                          |
| regex_dna      | 227 ms                                                 | 219 ms: 1.03x faster                                           |
| regex_effbot   | 3.63 ms                                                | 3.69 ms: 1.02x slower                                          |
| Geometric mean | (ref)                                                  | 1.13x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 305 us: 1.59x faster                                           |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                           |
| tomli_loads          | 3.14 sec                                               | 2.09 sec: 1.50x faster                                         |
| json_dumps           | 14.2 ms                                                | 10.3 ms: 1.38x faster                                          |
| xml_etree_process    | 79.1 ms                                                | 59.2 ms: 1.34x faster                                          |
| json_loads           | 31.2 us                                                | 26.9 us: 1.16x faster                                          |
| xml_etree_generate   | 99.4 ms                                                | 86.8 ms: 1.15x faster                                          |
| xml_etree_iterparse  | 115 ms                                                 | 104 ms: 1.11x faster                                           |
| xml_etree_parse      | 168 ms                                                 | 156 ms: 1.07x faster                                           |
| pickle_list          | 5.08 us                                                | 4.96 us: 1.02x faster                                          |
| unpickle_list        | 5.20 us                                                | 5.30 us: 1.02x slower                                          |
| unpickle             | 14.4 us                                                | 15.6 us: 1.08x slower                                          |
| pickle               | 10.7 us                                                | 11.7 us: 1.10x slower                                          |
| pickle_dict          | 29.6 us                                                | 33.4 us: 1.13x slower                                          |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.38x faster                                          |
| python_startup_no_site | 5.93 ms                                                | 7.01 ms: 1.18x slower                                          |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.0 ms: 1.48x faster                                          |
| django_template | 48.2 ms                                                | 33.9 ms: 1.42x faster                                          |
| genshi_text     | 31.8 ms                                                | 22.4 ms: 1.42x faster                                          |
| genshi_xml      | 66.0 ms                                                | 49.6 ms: 1.33x faster                                          |
| Geometric mean  | (ref)                                                  | 1.41x faster                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 161 us: 3.39x faster                                           |
| generators               | 80.1 ms                                                | 27.7 ms: 2.89x faster                                          |
| deltablue                | 7.91 ms                                                | 3.26 ms: 2.43x faster                                          |
| async_tree_none          | 728 ms                                                 | 322 ms: 2.26x faster                                           |
| async_tree_memoization   | 870 ms                                                 | 391 ms: 2.23x faster                                           |
| go                       | 240 ms                                                 | 120 ms: 2.00x faster                                           |
| asyncio_tcp              | 922 ms                                                 | 472 ms: 1.95x faster                                           |
| chaos                    | 115 ms                                                 | 59.8 ms: 1.93x faster                                          |
| deepcopy_memo            | 58.5 us                                                | 30.5 us: 1.92x faster                                          |
| raytrace                 | 507 ms                                                 | 265 ms: 1.92x faster                                           |
| async_tree_io            | 1.77 sec                                               | 929 ms: 1.90x faster                                           |
| logging_silent           | 190 ns                                                 | 101 ns: 1.87x faster                                           |
| deepcopy                 | 479 us                                                 | 263 us: 1.82x faster                                           |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 563 ms: 1.80x faster                                           |
| crypto_pyaes             | 128 ms                                                 | 71.5 ms: 1.79x faster                                          |
| scimark_sor              | 220 ms                                                 | 123 ms: 1.79x faster                                           |
| richards_super           | 94.7 ms                                                | 53.5 ms: 1.77x faster                                          |
| nbody                    | 154 ms                                                 | 86.9 ms: 1.77x faster                                          |
| pylint                   | 551 ms                                                 | 318 ms: 1.74x faster                                           |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.73x faster                                          |
| scimark_monte_carlo      | 118 ms                                                 | 68.2 ms: 1.73x faster                                          |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.68x faster                                          |
| richards                 | 79.3 ms                                                | 47.4 ms: 1.67x faster                                          |
| hexiom                   | 10.4 ms                                                | 6.22 ms: 1.67x faster                                          |
| sqlglot_transpile        | 2.57 ms                                                | 1.59 ms: 1.62x faster                                          |
| pickle_pure_python       | 484 us                                                 | 305 us: 1.59x faster                                           |
| scimark_lu               | 176 ms                                                 | 112 ms: 1.58x faster                                           |
| deepcopy_reduce          | 4.17 us                                                | 2.71 us: 1.54x faster                                          |
| coroutines               | 35.1 ms                                                | 23.0 ms: 1.53x faster                                          |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                           |
| float                    | 117 ms                                                 | 76.8 ms: 1.52x faster                                          |
| tornado_http             | 136 ms                                                 | 90.2 ms: 1.51x faster                                          |
| spectral_norm            | 170 ms                                                 | 113 ms: 1.51x faster                                           |
| pyflate                  | 716 ms                                                 | 476 ms: 1.51x faster                                           |
| tomli_loads              | 3.14 sec                                               | 2.09 sec: 1.50x faster                                         |
| mako                     | 16.3 ms                                                | 11.0 ms: 1.48x faster                                          |
| logging_simple           | 8.30 us                                                | 5.65 us: 1.47x faster                                          |
| regex_compile            | 188 ms                                                 | 129 ms: 1.46x faster                                           |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.77 sec: 1.45x faster                                         |
| logging_format           | 9.09 us                                                | 6.26 us: 1.45x faster                                          |
| html5lib                 | 88.9 ms                                                | 61.4 ms: 1.45x faster                                          |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.42x faster                                         |
| django_template          | 48.2 ms                                                | 33.9 ms: 1.42x faster                                          |
| genshi_text              | 31.8 ms                                                | 22.4 ms: 1.42x faster                                          |
| pprint_safe_repr         | 1.02 sec                                               | 721 ms: 1.41x faster                                           |
| thrift                   | 1.07 ms                                                | 767 us: 1.40x faster                                           |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.39x faster                                         |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.66 ms: 1.39x faster                                          |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.38x faster                                          |
| json_dumps               | 14.2 ms                                                | 10.3 ms: 1.38x faster                                          |
| 2to3                     | 348 ms                                                 | 255 ms: 1.37x faster                                           |
| sympy_sum                | 196 ms                                                 | 146 ms: 1.34x faster                                           |
| fannkuch                 | 532 ms                                                 | 398 ms: 1.34x faster                                           |
| xml_etree_process        | 79.1 ms                                                | 59.2 ms: 1.34x faster                                          |
| genshi_xml               | 66.0 ms                                                | 49.6 ms: 1.33x faster                                          |
| nqueens                  | 106 ms                                                 | 79.7 ms: 1.33x faster                                          |
| sqlglot_normalize        | 143 ms                                                 | 108 ms: 1.32x faster                                           |
| dulwich_log              | 84.3 ms                                                | 64.6 ms: 1.31x faster                                          |
| sympy_integrate          | 25.8 ms                                                | 19.8 ms: 1.31x faster                                          |
| sqlglot_optimize         | 69.2 ms                                                | 53.4 ms: 1.30x faster                                          |
| sympy_str                | 346 ms                                                 | 267 ms: 1.29x faster                                           |
| scimark_fft              | 466 ms                                                 | 360 ms: 1.29x faster                                           |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.29x faster                                          |
| docutils                 | 3.30 sec                                               | 2.64 sec: 1.25x faster                                         |
| sympy_expand             | 566 ms                                                 | 455 ms: 1.24x faster                                           |
| json_loads               | 31.2 us                                                | 26.9 us: 1.16x faster                                          |
| bench_thread_pool        | 986 us                                                 | 853 us: 1.16x faster                                           |
| xml_etree_generate       | 99.4 ms                                                | 86.8 ms: 1.15x faster                                          |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.11x faster                                           |
| json                     | 5.69 ms                                                | 5.12 ms: 1.11x faster                                          |
| xml_etree_iterparse      | 115 ms                                                 | 104 ms: 1.11x faster                                           |
| regex_v8                 | 27.8 ms                                                | 25.4 ms: 1.09x faster                                          |
| xml_etree_parse          | 168 ms                                                 | 156 ms: 1.07x faster                                           |
| sqlite_synth             | 3.02 us                                                | 2.82 us: 1.07x faster                                          |
| mdp                      | 2.85 sec                                               | 2.71 sec: 1.05x faster                                         |
| unpack_sequence          | 60.0 ns                                                | 57.9 ns: 1.04x faster                                          |
| regex_dna                | 227 ms                                                 | 219 ms: 1.03x faster                                           |
| pickle_list              | 5.08 us                                                | 4.96 us: 1.02x faster                                          |
| async_generators         | 444 ms                                                 | 434 ms: 1.02x faster                                           |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                           |
| asyncio_websockets       | 559 ms                                                 | 556 ms: 1.00x faster                                           |
| gc_traversal             | 3.62 ms                                                | 3.61 ms: 1.00x faster                                          |
| regex_effbot             | 3.63 ms                                                | 3.69 ms: 1.02x slower                                          |
| unpickle_list            | 5.20 us                                                | 5.30 us: 1.02x slower                                          |
| coverage                 | 79.4 ms                                                | 84.8 ms: 1.07x slower                                          |
| unpickle                 | 14.4 us                                                | 15.6 us: 1.08x slower                                          |
| create_gc_cycles         | 1.62 ms                                                | 1.77 ms: 1.10x slower                                          |
| pickle                   | 10.7 us                                                | 11.7 us: 1.10x slower                                          |
| telco                    | 7.27 ms                                                | 8.16 ms: 1.12x slower                                          |
| pickle_dict              | 29.6 us                                                | 33.4 us: 1.13x slower                                          |
| python_startup_no_site   | 5.93 ms                                                | 7.01 ms: 1.18x slower                                          |
| bench_mp_pool            | 24.0 ms                                                | 56.0 ms: 2.33x slower                                          |
| Geometric mean           | (ref)                                                  | 1.38x faster                                                   |
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20241007-3.14.0a0-8738ae5/bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.35x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: 1.12x