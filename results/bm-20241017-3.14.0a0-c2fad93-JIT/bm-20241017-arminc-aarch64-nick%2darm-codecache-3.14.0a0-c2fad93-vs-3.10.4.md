# Results vs. 3.10.4

- fork: nick-arm
- ref: codecache
- machine: linux-aarch64
- commit hash: c2fad93
- commit date: 2024-10-17
- overall geometric mean: 1.10x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.39x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 375 ms: 1.02x faster                                             |
| docutils       | 3.53 sec                                                              | 3.67 sec: 1.04x slower                                           |
| html5lib       | 86.5 ms                                                               | 71.1 ms: 1.22x faster                                            |
| tornado_http   | 178 ms                                                                | 146 ms: 1.22x faster                                             |
| Geometric mean | (ref)                                                                 | 1.10x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|-------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 455 ms: 2.09x faster                                             |
| async_tree_memoization  | 1.13 sec                                                              | 582 ms: 1.95x faster                                             |
| async_tree_io           | 2.28 sec                                                              | 1.20 sec: 1.91x faster                                           |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 757 ms: 1.68x faster                                             |
| Geometric mean          | (ref)                                                                 | 1.90x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 110 ms: 1.51x faster                                             |
| float          | 135 ms                                                                | 93.8 ms: 1.44x faster                                            |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                     |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_dna      | 257 ms                                                                | 247 ms: 1.04x faster                                             |
| regex_v8       | 32.2 ms                                                               | 31.5 ms: 1.02x faster                                            |
| regex_effbot   | 4.25 ms                                                               | 4.90 ms: 1.15x slower                                            |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                     |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 267 us: 1.37x faster                                             |
| pickle_pure_python   | 529 us                                                                | 388 us: 1.36x faster                                             |
| tomli_loads          | 3.36 sec                                                              | 2.64 sec: 1.27x faster                                           |
| json_dumps           | 16.7 ms                                                               | 13.4 ms: 1.25x faster                                            |
| xml_etree_process    | 99.5 ms                                                               | 80.5 ms: 1.24x faster                                            |
| xml_etree_parse      | 212 ms                                                                | 188 ms: 1.13x faster                                             |
| xml_etree_generate   | 123 ms                                                                | 112 ms: 1.10x faster                                             |
| unpickle_list        | 6.99 us                                                               | 6.60 us: 1.06x faster                                            |
| xml_etree_iterparse  | 156 ms                                                                | 151 ms: 1.03x faster                                             |
| pickle_list          | 5.24 us                                                               | 5.21 us: 1.01x faster                                            |
| json_loads           | 30.9 us                                                               | 31.2 us: 1.01x slower                                            |
| pickle_dict          | 35.1 us                                                               | 38.2 us: 1.09x slower                                            |
| unpickle             | 17.5 us                                                               | 19.2 us: 1.10x slower                                            |
| pickle               | 12.5 us                                                               | 13.8 us: 1.11x slower                                            |
| Geometric mean       | (ref)                                                                 | 1.10x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.76 ms: 1.27x slower                                            |
| python_startup         | 11.2 ms                                                               | 14.7 ms: 1.32x slower                                            |
| Geometric mean         | (ref)                                                                 | 1.29x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 12.9 ms: 1.46x faster                                            |
| django_template | 53.3 ms                                                               | 52.3 ms: 1.02x faster                                            |
| genshi_xml      | 69.8 ms                                                               | 85.1 ms: 1.22x slower                                            |
| Geometric mean  | (ref)                                                                 | 1.05x faster                                                     |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|--------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 207 us: 3.20x faster                                             |
| async_tree_none          | 950 ms                                                                | 455 ms: 2.09x faster                                             |
| deltablue                | 8.94 ms                                                               | 4.47 ms: 2.00x faster                                            |
| async_tree_memoization   | 1.13 sec                                                              | 582 ms: 1.95x faster                                             |
| async_tree_io            | 2.28 sec                                                              | 1.20 sec: 1.91x faster                                           |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 757 ms: 1.68x faster                                             |
| raytrace                 | 573 ms                                                                | 347 ms: 1.65x faster                                             |
| logging_silent           | 222 ns                                                                | 135 ns: 1.64x faster                                             |
| deepcopy_memo            | 61.7 us                                                               | 37.7 us: 1.64x faster                                            |
| scimark_sor              | 246 ms                                                                | 152 ms: 1.62x faster                                             |
| scimark_lu               | 227 ms                                                                | 149 ms: 1.52x faster                                             |
| asyncio_tcp              | 944 ms                                                                | 623 ms: 1.52x faster                                             |
| crypto_pyaes             | 134 ms                                                                | 88.5 ms: 1.51x faster                                            |
| nbody                    | 166 ms                                                                | 110 ms: 1.51x faster                                             |
| mako                     | 18.9 ms                                                               | 12.9 ms: 1.46x faster                                            |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.28 sec: 1.44x faster                                           |
| float                    | 135 ms                                                                | 93.8 ms: 1.44x faster                                            |
| sqlglot_parse            | 2.40 ms                                                               | 1.69 ms: 1.42x faster                                            |
| chaos                    | 121 ms                                                                | 86.0 ms: 1.41x faster                                            |
| scimark_monte_carlo      | 128 ms                                                                | 90.9 ms: 1.41x faster                                            |
| richards_super           | 107 ms                                                                | 76.3 ms: 1.40x faster                                            |
| go                       | 264 ms                                                                | 189 ms: 1.40x faster                                             |
| unpickle_pure_python     | 366 us                                                                | 267 us: 1.37x faster                                             |
| pickle_pure_python       | 529 us                                                                | 388 us: 1.36x faster                                             |
| richards                 | 91.7 ms                                                               | 68.8 ms: 1.33x faster                                            |
| comprehensions           | 33.1 us                                                               | 24.9 us: 1.33x faster                                            |
| thrift                   | 1.26 ms                                                               | 958 us: 1.32x faster                                             |
| coroutines               | 37.2 ms                                                               | 28.5 ms: 1.31x faster                                            |
| sqlglot_transpile        | 2.84 ms                                                               | 2.20 ms: 1.29x faster                                            |
| logging_format           | 10.6 us                                                               | 8.22 us: 1.29x faster                                            |
| deepcopy                 | 511 us                                                                | 397 us: 1.29x faster                                             |
| logging_simple           | 9.78 us                                                               | 7.62 us: 1.28x faster                                            |
| pyflate                  | 795 ms                                                                | 621 ms: 1.28x faster                                             |
| tomli_loads              | 3.36 sec                                                              | 2.64 sec: 1.27x faster                                           |
| json_dumps               | 16.7 ms                                                               | 13.4 ms: 1.25x faster                                            |
| xml_etree_process        | 99.5 ms                                                               | 80.5 ms: 1.24x faster                                            |
| spectral_norm            | 186 ms                                                                | 152 ms: 1.23x faster                                             |
| tornado_http             | 178 ms                                                                | 146 ms: 1.22x faster                                             |
| pathlib                  | 26.3 ms                                                               | 21.6 ms: 1.22x faster                                            |
| html5lib                 | 86.5 ms                                                               | 71.1 ms: 1.22x faster                                            |
| deepcopy_reduce          | 4.60 us                                                               | 3.83 us: 1.20x faster                                            |
| generators               | 68.1 ms                                                               | 59.3 ms: 1.15x faster                                            |
| pycparser                | 1.69 sec                                                              | 1.48 sec: 1.14x faster                                           |
| bench_thread_pool        | 1.59 ms                                                               | 1.40 ms: 1.13x faster                                            |
| scimark_fft              | 500 ms                                                                | 443 ms: 1.13x faster                                             |
| xml_etree_parse          | 212 ms                                                                | 188 ms: 1.13x faster                                             |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.80 ms: 1.12x faster                                            |
| xml_etree_generate       | 123 ms                                                                | 112 ms: 1.10x faster                                             |
| sqlite_synth             | 4.12 us                                                               | 3.83 us: 1.07x faster                                            |
| json                     | 5.88 ms                                                               | 5.53 ms: 1.06x faster                                            |
| unpickle_list            | 6.99 us                                                               | 6.60 us: 1.06x faster                                            |
| mdp                      | 3.70 sec                                                              | 3.49 sec: 1.06x faster                                           |
| hexiom                   | 10.9 ms                                                               | 10.4 ms: 1.05x faster                                            |
| fannkuch                 | 546 ms                                                                | 519 ms: 1.05x faster                                             |
| regex_dna                | 257 ms                                                                | 247 ms: 1.04x faster                                             |
| xml_etree_iterparse      | 156 ms                                                                | 151 ms: 1.03x faster                                             |
| django_template          | 53.3 ms                                                               | 52.3 ms: 1.02x faster                                            |
| regex_v8                 | 32.2 ms                                                               | 31.5 ms: 1.02x faster                                            |
| 2to3                     | 381 ms                                                                | 375 ms: 1.02x faster                                             |
| meteor_contest           | 126 ms                                                                | 125 ms: 1.01x faster                                             |
| sqlglot_normalize        | 156 ms                                                                | 154 ms: 1.01x faster                                             |
| pickle_list              | 5.24 us                                                               | 5.21 us: 1.01x faster                                            |
| asyncio_websockets       | 657 ms                                                                | 663 ms: 1.01x slower                                             |
| json_loads               | 30.9 us                                                               | 31.2 us: 1.01x slower                                            |
| nqueens                  | 117 ms                                                                | 121 ms: 1.03x slower                                             |
| docutils                 | 3.53 sec                                                              | 3.67 sec: 1.04x slower                                           |
| sqlglot_optimize         | 75.4 ms                                                               | 79.2 ms: 1.05x slower                                            |
| dulwich_log              | 73.5 ms                                                               | 77.3 ms: 1.05x slower                                            |
| pprint_safe_repr         | 1.15 sec                                                              | 1.22 sec: 1.06x slower                                           |
| sympy_str                | 329 ms                                                                | 355 ms: 1.08x slower                                             |
| pickle_dict              | 35.1 us                                                               | 38.2 us: 1.09x slower                                            |
| sympy_integrate          | 26.5 ms                                                               | 28.9 ms: 1.09x slower                                            |
| sympy_expand             | 543 ms                                                                | 593 ms: 1.09x slower                                             |
| unpickle                 | 17.5 us                                                               | 19.2 us: 1.10x slower                                            |
| pprint_pformat           | 2.36 sec                                                              | 2.60 sec: 1.10x slower                                           |
| pickle                   | 12.5 us                                                               | 13.8 us: 1.11x slower                                            |
| telco                    | 8.49 ms                                                               | 9.53 ms: 1.12x slower                                            |
| async_generators         | 452 ms                                                                | 510 ms: 1.13x slower                                             |
| sympy_sum                | 184 ms                                                                | 210 ms: 1.14x slower                                             |
| regex_effbot             | 4.25 ms                                                               | 4.90 ms: 1.15x slower                                            |
| genshi_xml               | 69.8 ms                                                               | 85.1 ms: 1.22x slower                                            |
| coverage                 | 83.6 ms                                                               | 103 ms: 1.23x slower                                             |
| python_startup_no_site   | 6.89 ms                                                               | 8.76 ms: 1.27x slower                                            |
| python_startup           | 11.2 ms                                                               | 14.7 ms: 1.32x slower                                            |
| gc_traversal             | 4.15 ms                                                               | 6.17 ms: 1.48x slower                                            |
| create_gc_cycles         | 2.26 ms                                                               | 3.58 ms: 1.58x slower                                            |
| bench_mp_pool            | 14.5 ms                                                               | 3.29 sec: 226.14x slower                                         |
| Geometric mean           | (ref)                                                                 | 1.10x faster                                                     |

Benchmark hidden because not significant (4): genshi_text, pylint, regex_compile, pidigits
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (7) of results/bm-20241017-3.14.0a0-c2fad93-JIT/bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx, unpack_sequence

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.39x