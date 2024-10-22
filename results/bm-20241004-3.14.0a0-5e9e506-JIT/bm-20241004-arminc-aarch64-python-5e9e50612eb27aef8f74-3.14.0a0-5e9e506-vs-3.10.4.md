# Results vs. 3.10.4

- fork: python
- ref: 5e9e50612eb27aef8f74
- machine: linux-aarch64
- commit hash: 5e9e506
- commit date: 2024-10-04
- overall geometric mean: 1.10x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.36x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 386 ms: 1.01x slower                                                    |
| docutils       | 3.53 sec                                                              | 3.71 sec: 1.05x slower                                                  |
| html5lib       | 86.5 ms                                                               | 71.9 ms: 1.20x faster                                                   |
| tornado_http   | 178 ms                                                                | 148 ms: 1.21x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.08x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 459 ms: 2.07x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 582 ms: 1.95x faster                                                    |
| async_tree_io           | 2.28 sec                                                              | 1.20 sec: 1.91x faster                                                  |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 765 ms: 1.66x faster                                                    |
| Geometric mean          | (ref)                                                                 | 1.89x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 111 ms: 1.50x faster                                                    |
| float          | 135 ms                                                                | 94.3 ms: 1.43x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 30.9 ms: 1.04x faster                                                   |
| regex_dna      | 257 ms                                                                | 255 ms: 1.01x faster                                                    |
| regex_compile  | 177 ms                                                                | 180 ms: 1.02x slower                                                    |
| regex_effbot   | 4.25 ms                                                               | 5.00 ms: 1.18x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 267 us: 1.37x faster                                                    |
| pickle_pure_python   | 529 us                                                                | 393 us: 1.35x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.65 sec: 1.27x faster                                                  |
| json_dumps           | 16.7 ms                                                               | 13.6 ms: 1.23x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 81.3 ms: 1.22x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 188 ms: 1.12x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 112 ms: 1.09x faster                                                    |
| unpickle_list        | 6.99 us                                                               | 6.56 us: 1.07x faster                                                   |
| xml_etree_iterparse  | 156 ms                                                                | 152 ms: 1.03x faster                                                    |
| pickle_list          | 5.24 us                                                               | 5.29 us: 1.01x slower                                                   |
| json_loads           | 30.9 us                                                               | 31.6 us: 1.02x slower                                                   |
| pickle_dict          | 35.1 us                                                               | 37.7 us: 1.08x slower                                                   |
| pickle               | 12.5 us                                                               | 13.7 us: 1.10x slower                                                   |
| unpickle             | 17.5 us                                                               | 19.3 us: 1.10x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.09x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.73 ms: 1.27x slower                                                   |
| python_startup         | 11.2 ms                                                               | 14.6 ms: 1.30x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.28x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.0 ms: 1.46x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 34.4 ms: 1.02x faster                                                   |
| django_template | 53.3 ms                                                               | 52.2 ms: 1.02x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 84.4 ms: 1.21x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.06x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 211 us: 3.14x faster                                                    |
| async_tree_none          | 950 ms                                                                | 459 ms: 2.07x faster                                                    |
| deltablue                | 8.94 ms                                                               | 4.40 ms: 2.03x faster                                                   |
| async_tree_memoization   | 1.13 sec                                                              | 582 ms: 1.95x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.20 sec: 1.91x faster                                                  |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 765 ms: 1.66x faster                                                    |
| logging_silent           | 222 ns                                                                | 134 ns: 1.66x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 37.6 us: 1.64x faster                                                   |
| raytrace                 | 573 ms                                                                | 351 ms: 1.63x faster                                                    |
| scimark_sor              | 246 ms                                                                | 153 ms: 1.61x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 603 ms: 1.56x faster                                                    |
| scimark_lu               | 227 ms                                                                | 151 ms: 1.50x faster                                                    |
| nbody                    | 166 ms                                                                | 111 ms: 1.50x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 89.8 ms: 1.49x faster                                                   |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.24 sec: 1.47x faster                                                  |
| mako                     | 18.9 ms                                                               | 13.0 ms: 1.46x faster                                                   |
| go                       | 264 ms                                                                | 184 ms: 1.44x faster                                                    |
| richards_super           | 107 ms                                                                | 74.9 ms: 1.43x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 89.5 ms: 1.43x faster                                                   |
| float                    | 135 ms                                                                | 94.3 ms: 1.43x faster                                                   |
| sqlglot_parse            | 2.40 ms                                                               | 1.69 ms: 1.42x faster                                                   |
| chaos                    | 121 ms                                                                | 87.0 ms: 1.39x faster                                                   |
| richards                 | 91.7 ms                                                               | 66.2 ms: 1.39x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 267 us: 1.37x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 393 us: 1.35x faster                                                    |
| comprehensions           | 33.1 us                                                               | 25.0 us: 1.33x faster                                                   |
| thrift                   | 1.26 ms                                                               | 955 us: 1.32x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 2.17 ms: 1.31x faster                                                   |
| coroutines               | 37.2 ms                                                               | 28.8 ms: 1.29x faster                                                   |
| pyflate                  | 795 ms                                                                | 616 ms: 1.29x faster                                                    |
| logging_format           | 10.6 us                                                               | 8.34 us: 1.27x faster                                                   |
| logging_simple           | 9.78 us                                                               | 7.70 us: 1.27x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.65 sec: 1.27x faster                                                  |
| deepcopy                 | 511 us                                                                | 407 us: 1.25x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 13.6 ms: 1.23x faster                                                   |
| spectral_norm            | 186 ms                                                                | 152 ms: 1.22x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 81.3 ms: 1.22x faster                                                   |
| tornado_http             | 178 ms                                                                | 148 ms: 1.21x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 21.9 ms: 1.20x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 71.9 ms: 1.20x faster                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 3.94 us: 1.17x faster                                                   |
| generators               | 68.1 ms                                                               | 59.1 ms: 1.15x faster                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.39 ms: 1.14x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 188 ms: 1.12x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.51 sec: 1.12x faster                                                  |
| scimark_fft              | 500 ms                                                                | 446 ms: 1.12x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.91 ms: 1.10x faster                                                   |
| xml_etree_generate       | 123 ms                                                                | 112 ms: 1.09x faster                                                    |
| fannkuch                 | 546 ms                                                                | 503 ms: 1.08x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 10.2 ms: 1.07x faster                                                   |
| unpickle_list            | 6.99 us                                                               | 6.56 us: 1.07x faster                                                   |
| sqlite_synth             | 4.12 us                                                               | 3.89 us: 1.06x faster                                                   |
| mdp                      | 3.70 sec                                                              | 3.51 sec: 1.05x faster                                                  |
| regex_v8                 | 32.2 ms                                                               | 30.9 ms: 1.04x faster                                                   |
| json                     | 5.88 ms                                                               | 5.72 ms: 1.03x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 152 ms: 1.03x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 34.4 ms: 1.02x faster                                                   |
| django_template          | 53.3 ms                                                               | 52.2 ms: 1.02x faster                                                   |
| regex_dna                | 257 ms                                                                | 255 ms: 1.01x faster                                                    |
| pickle_list              | 5.24 us                                                               | 5.29 us: 1.01x slower                                                   |
| 2to3                     | 381 ms                                                                | 386 ms: 1.01x slower                                                    |
| asyncio_websockets       | 657 ms                                                                | 665 ms: 1.01x slower                                                    |
| json_loads               | 30.9 us                                                               | 31.6 us: 1.02x slower                                                   |
| regex_compile            | 177 ms                                                                | 180 ms: 1.02x slower                                                    |
| docutils                 | 3.53 sec                                                              | 3.71 sec: 1.05x slower                                                  |
| nqueens                  | 117 ms                                                                | 125 ms: 1.07x slower                                                    |
| pickle_dict              | 35.1 us                                                               | 37.7 us: 1.08x slower                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 1.24 sec: 1.08x slower                                                  |
| dulwich_log              | 73.5 ms                                                               | 80.1 ms: 1.09x slower                                                   |
| sympy_str                | 329 ms                                                                | 359 ms: 1.09x slower                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 82.8 ms: 1.10x slower                                                   |
| pickle                   | 12.5 us                                                               | 13.7 us: 1.10x slower                                                   |
| sympy_expand             | 543 ms                                                                | 597 ms: 1.10x slower                                                    |
| sympy_integrate          | 26.5 ms                                                               | 29.2 ms: 1.10x slower                                                   |
| unpickle                 | 17.5 us                                                               | 19.3 us: 1.10x slower                                                   |
| pprint_pformat           | 2.36 sec                                                              | 2.63 sec: 1.11x slower                                                  |
| async_generators         | 452 ms                                                                | 508 ms: 1.12x slower                                                    |
| telco                    | 8.49 ms                                                               | 9.78 ms: 1.15x slower                                                   |
| sympy_sum                | 184 ms                                                                | 214 ms: 1.16x slower                                                    |
| regex_effbot             | 4.25 ms                                                               | 5.00 ms: 1.18x slower                                                   |
| coverage                 | 83.6 ms                                                               | 99.7 ms: 1.19x slower                                                   |
| genshi_xml               | 69.8 ms                                                               | 84.4 ms: 1.21x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.73 ms: 1.27x slower                                                   |
| python_startup           | 11.2 ms                                                               | 14.6 ms: 1.30x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 6.11 ms: 1.47x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 3.57 ms: 1.58x slower                                                   |
| bench_mp_pool            | 14.5 ms                                                               | 1.43 sec: 98.64x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.10x faster                                                            |

Benchmark hidden because not significant (4): meteor_contest, pidigits, sqlglot_normalize, pylint
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (7) of results/bm-20241004-3.14.0a0-5e9e506-JIT/bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx, unpack_sequence

# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.36x