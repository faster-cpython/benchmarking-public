# Results vs. 3.10.4

- fork: python
- ref: v3.14.0a1
- machine: linux-aarch64
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.165x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.37x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| docutils       | 3.53 sec                                                              | 3.61 sec: 1.02x slower                                       |
| html5lib       | 86.5 ms                                                               | 71.8 ms: 1.20x faster                                        |
| tornado_http   | 178 ms                                                                | 147 ms: 1.21x faster                                         |
| Geometric mean | (ref)                                                                 | 1.09x faster                                                 |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 463 ms: 2.05x faster                                         |
| async_tree_io           | 2.28 sec                                                              | 1.19 sec: 1.92x faster                                       |
| async_tree_memoization  | 1.13 sec                                                              | 605 ms: 1.87x faster                                         |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 759 ms: 1.68x faster                                         |
| Geometric mean          | (ref)                                                                 | 1.88x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 116 ms: 1.43x faster                                         |
| float          | 135 ms                                                                | 97.2 ms: 1.39x faster                                        |
| Geometric mean | (ref)                                                                 | 1.26x faster                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_dna      | 257 ms                                                                | 244 ms: 1.06x faster                                         |
| regex_v8       | 32.2 ms                                                               | 31.6 ms: 1.02x faster                                        |
| regex_compile  | 177 ms                                                                | 179 ms: 1.01x slower                                         |
| regex_effbot   | 4.25 ms                                                               | 4.91 ms: 1.16x slower                                        |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 268 us: 1.37x faster                                         |
| pickle_pure_python   | 529 us                                                                | 389 us: 1.36x faster                                         |
| tomli_loads          | 3.36 sec                                                              | 2.65 sec: 1.27x faster                                       |
| xml_etree_process    | 99.5 ms                                                               | 80.4 ms: 1.24x faster                                        |
| json_dumps           | 16.7 ms                                                               | 14.4 ms: 1.16x faster                                        |
| xml_etree_parse      | 212 ms                                                                | 186 ms: 1.14x faster                                         |
| xml_etree_generate   | 123 ms                                                                | 111 ms: 1.10x faster                                         |
| unpickle_list        | 6.99 us                                                               | 6.52 us: 1.07x faster                                        |
| xml_etree_iterparse  | 156 ms                                                                | 151 ms: 1.03x faster                                         |
| pickle_list          | 5.24 us                                                               | 5.12 us: 1.02x faster                                        |
| json_loads           | 30.9 us                                                               | 31.7 us: 1.02x slower                                        |
| pickle_dict          | 35.1 us                                                               | 37.8 us: 1.08x slower                                        |
| unpickle             | 17.5 us                                                               | 19.0 us: 1.09x slower                                        |
| pickle               | 12.5 us                                                               | 13.8 us: 1.10x slower                                        |
| Geometric mean       | (ref)                                                                 | 1.10x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.79 ms: 1.28x slower                                        |
| python_startup         | 11.2 ms                                                               | 14.7 ms: 1.31x slower                                        |
| Geometric mean         | (ref)                                                                 | 1.29x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.2 ms: 1.43x faster                                        |
| genshi_text     | 35.2 ms                                                               | 34.2 ms: 1.03x faster                                        |
| django_template | 53.3 ms                                                               | 52.4 ms: 1.02x faster                                        |
| genshi_xml      | 69.8 ms                                                               | 84.1 ms: 1.20x slower                                        |
| Geometric mean  | (ref)                                                                 | 1.06x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 218 us: 3.04x faster                                         |
| async_tree_none          | 950 ms                                                                | 463 ms: 2.05x faster                                         |
| deltablue                | 8.94 ms                                                               | 4.55 ms: 1.96x faster                                        |
| async_tree_io            | 2.28 sec                                                              | 1.19 sec: 1.92x faster                                       |
| async_tree_memoization   | 1.13 sec                                                              | 605 ms: 1.87x faster                                         |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 759 ms: 1.68x faster                                         |
| logging_silent           | 222 ns                                                                | 134 ns: 1.66x faster                                         |
| raytrace                 | 573 ms                                                                | 349 ms: 1.64x faster                                         |
| scimark_sor              | 246 ms                                                                | 154 ms: 1.60x faster                                         |
| deepcopy_memo            | 61.7 us                                                               | 39.2 us: 1.57x faster                                        |
| scimark_lu               | 227 ms                                                                | 151 ms: 1.50x faster                                         |
| richards_super           | 107 ms                                                                | 71.4 ms: 1.50x faster                                        |
| asyncio_tcp              | 944 ms                                                                | 630 ms: 1.50x faster                                         |
| crypto_pyaes             | 134 ms                                                                | 90.8 ms: 1.48x faster                                        |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.27 sec: 1.44x faster                                       |
| go                       | 264 ms                                                                | 184 ms: 1.44x faster                                         |
| nbody                    | 166 ms                                                                | 116 ms: 1.43x faster                                         |
| mako                     | 18.9 ms                                                               | 13.2 ms: 1.43x faster                                        |
| scimark_monte_carlo      | 128 ms                                                                | 89.5 ms: 1.43x faster                                        |
| richards                 | 91.7 ms                                                               | 64.2 ms: 1.43x faster                                        |
| chaos                    | 121 ms                                                                | 85.0 ms: 1.42x faster                                        |
| sqlglot_parse            | 2.40 ms                                                               | 1.70 ms: 1.41x faster                                        |
| float                    | 135 ms                                                                | 97.2 ms: 1.39x faster                                        |
| unpickle_pure_python     | 366 us                                                                | 268 us: 1.37x faster                                         |
| pickle_pure_python       | 529 us                                                                | 389 us: 1.36x faster                                         |
| deepcopy                 | 511 us                                                                | 377 us: 1.35x faster                                         |
| comprehensions           | 33.1 us                                                               | 24.7 us: 1.34x faster                                        |
| thrift                   | 1.26 ms                                                               | 956 us: 1.32x faster                                         |
| logging_simple           | 9.78 us                                                               | 7.45 us: 1.31x faster                                        |
| logging_format           | 10.6 us                                                               | 8.08 us: 1.31x faster                                        |
| pyflate                  | 795 ms                                                                | 615 ms: 1.29x faster                                         |
| sqlglot_transpile        | 2.84 ms                                                               | 2.20 ms: 1.29x faster                                        |
| coroutines               | 37.2 ms                                                               | 28.9 ms: 1.29x faster                                        |
| tomli_loads              | 3.36 sec                                                              | 2.65 sec: 1.27x faster                                       |
| xml_etree_process        | 99.5 ms                                                               | 80.4 ms: 1.24x faster                                        |
| pathlib                  | 26.3 ms                                                               | 21.6 ms: 1.22x faster                                        |
| tornado_http             | 178 ms                                                                | 147 ms: 1.21x faster                                         |
| spectral_norm            | 186 ms                                                                | 155 ms: 1.21x faster                                         |
| html5lib                 | 86.5 ms                                                               | 71.8 ms: 1.20x faster                                        |
| json_dumps               | 16.7 ms                                                               | 14.4 ms: 1.16x faster                                        |
| bench_thread_pool        | 1.59 ms                                                               | 1.37 ms: 1.16x faster                                        |
| deepcopy_reduce          | 4.60 us                                                               | 3.98 us: 1.15x faster                                        |
| generators               | 68.1 ms                                                               | 59.0 ms: 1.15x faster                                        |
| xml_etree_parse          | 212 ms                                                                | 186 ms: 1.14x faster                                         |
| pycparser                | 1.69 sec                                                              | 1.52 sec: 1.11x faster                                       |
| xml_etree_generate       | 123 ms                                                                | 111 ms: 1.10x faster                                         |
| scimark_fft              | 500 ms                                                                | 454 ms: 1.10x faster                                         |
| fannkuch                 | 546 ms                                                                | 503 ms: 1.08x faster                                         |
| unpickle_list            | 6.99 us                                                               | 6.52 us: 1.07x faster                                        |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 7.16 ms: 1.06x faster                                        |
| hexiom                   | 10.9 ms                                                               | 10.3 ms: 1.06x faster                                        |
| sqlite_synth             | 4.12 us                                                               | 3.89 us: 1.06x faster                                        |
| regex_dna                | 257 ms                                                                | 244 ms: 1.06x faster                                         |
| mdp                      | 3.70 sec                                                              | 3.51 sec: 1.05x faster                                       |
| json                     | 5.88 ms                                                               | 5.67 ms: 1.04x faster                                        |
| genshi_text              | 35.2 ms                                                               | 34.2 ms: 1.03x faster                                        |
| xml_etree_iterparse      | 156 ms                                                                | 151 ms: 1.03x faster                                         |
| meteor_contest           | 126 ms                                                                | 123 ms: 1.03x faster                                         |
| pickle_list              | 5.24 us                                                               | 5.12 us: 1.02x faster                                        |
| regex_v8                 | 32.2 ms                                                               | 31.6 ms: 1.02x faster                                        |
| django_template          | 53.3 ms                                                               | 52.4 ms: 1.02x faster                                        |
| sqlglot_normalize        | 156 ms                                                                | 157 ms: 1.01x slower                                         |
| asyncio_websockets       | 657 ms                                                                | 664 ms: 1.01x slower                                         |
| regex_compile            | 177 ms                                                                | 179 ms: 1.01x slower                                         |
| docutils                 | 3.53 sec                                                              | 3.61 sec: 1.02x slower                                       |
| json_loads               | 30.9 us                                                               | 31.7 us: 1.02x slower                                        |
| pprint_safe_repr         | 1.15 sec                                                              | 1.21 sec: 1.05x slower                                       |
| dulwich_log              | 73.5 ms                                                               | 77.6 ms: 1.06x slower                                        |
| nqueens                  | 117 ms                                                                | 125 ms: 1.06x slower                                         |
| pickle_dict              | 35.1 us                                                               | 37.8 us: 1.08x slower                                        |
| pprint_pformat           | 2.36 sec                                                              | 2.55 sec: 1.08x slower                                       |
| sympy_str                | 329 ms                                                                | 357 ms: 1.09x slower                                         |
| unpickle                 | 17.5 us                                                               | 19.0 us: 1.09x slower                                        |
| sqlglot_optimize         | 75.4 ms                                                               | 82.2 ms: 1.09x slower                                        |
| sympy_expand             | 543 ms                                                                | 594 ms: 1.09x slower                                         |
| pickle                   | 12.5 us                                                               | 13.8 us: 1.10x slower                                        |
| sympy_integrate          | 26.5 ms                                                               | 29.4 ms: 1.11x slower                                        |
| async_generators         | 452 ms                                                                | 507 ms: 1.12x slower                                         |
| telco                    | 8.49 ms                                                               | 9.74 ms: 1.15x slower                                        |
| regex_effbot             | 4.25 ms                                                               | 4.91 ms: 1.16x slower                                        |
| sympy_sum                | 184 ms                                                                | 215 ms: 1.17x slower                                         |
| genshi_xml               | 69.8 ms                                                               | 84.1 ms: 1.20x slower                                        |
| coverage                 | 83.6 ms                                                               | 101 ms: 1.21x slower                                         |
| python_startup_no_site   | 6.89 ms                                                               | 8.79 ms: 1.28x slower                                        |
| python_startup           | 11.2 ms                                                               | 14.7 ms: 1.31x slower                                        |
| gc_traversal             | 4.15 ms                                                               | 6.22 ms: 1.50x slower                                        |
| create_gc_cycles         | 2.26 ms                                                               | 3.67 ms: 1.62x slower                                        |
| bench_mp_pool            | 14.5 ms                                                               | 1.45 sec: 99.81x slower                                      |
| Geometric mean           | (ref)                                                                 | 1.10x faster                                                 |

Benchmark hidden because not significant (3): pidigits, 2to3, pylint
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (7) of results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx, unpack_sequence

- Geometric mean (including insignificant results): 1.165x faster
# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.37x