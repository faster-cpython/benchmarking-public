# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_likely
- machine: linux-aarch64
- commit hash: bad9944
- commit date: 2024-10-18
- overall geometric mean: 1.162x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.37x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 3.53 sec                                                              | 3.58 sec: 1.01x slower                                                  |
| html5lib       | 86.5 ms                                                               | 71.9 ms: 1.20x faster                                                   |
| tornado_http   | 178 ms                                                                | 147 ms: 1.21x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.09x faster                                                            |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 457 ms: 2.08x faster                                                    |
| async_tree_io           | 2.28 sec                                                              | 1.18 sec: 1.93x faster                                                  |
| async_tree_memoization  | 1.13 sec                                                              | 600 ms: 1.89x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 755 ms: 1.69x faster                                                    |
| Geometric mean          | (ref)                                                                 | 1.89x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 115 ms: 1.44x faster                                                    |
| float          | 135 ms                                                                | 97.8 ms: 1.38x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.26x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 31.0 ms: 1.04x faster                                                   |
| regex_dna      | 257 ms                                                                | 254 ms: 1.01x faster                                                    |
| regex_compile  | 177 ms                                                                | 179 ms: 1.02x slower                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.96 ms: 1.17x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 270 us: 1.36x faster                                                    |
| pickle_pure_python   | 529 us                                                                | 392 us: 1.35x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.66 sec: 1.26x faster                                                  |
| xml_etree_process    | 99.5 ms                                                               | 81.2 ms: 1.23x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 14.6 ms: 1.14x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 190 ms: 1.11x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 112 ms: 1.10x faster                                                    |
| unpickle_list        | 6.99 us                                                               | 6.42 us: 1.09x faster                                                   |
| xml_etree_iterparse  | 156 ms                                                                | 150 ms: 1.04x faster                                                    |
| json_loads           | 30.9 us                                                               | 31.6 us: 1.02x slower                                                   |
| pickle_dict          | 35.1 us                                                               | 37.7 us: 1.07x slower                                                   |
| pickle               | 12.5 us                                                               | 13.9 us: 1.12x slower                                                   |
| unpickle             | 17.5 us                                                               | 19.6 us: 1.12x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.09x faster                                                            |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.73 ms: 1.27x slower                                                   |
| python_startup         | 11.2 ms                                                               | 14.5 ms: 1.30x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.28x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.6 ms: 1.40x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 34.1 ms: 1.03x faster                                                   |
| django_template | 53.3 ms                                                               | 52.6 ms: 1.01x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 83.9 ms: 1.20x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.05x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 219 us: 3.02x faster                                                    |
| async_tree_none          | 950 ms                                                                | 457 ms: 2.08x faster                                                    |
| deltablue                | 8.94 ms                                                               | 4.50 ms: 1.99x faster                                                   |
| async_tree_io            | 2.28 sec                                                              | 1.18 sec: 1.93x faster                                                  |
| async_tree_memoization   | 1.13 sec                                                              | 600 ms: 1.89x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 755 ms: 1.69x faster                                                    |
| logging_silent           | 222 ns                                                                | 133 ns: 1.67x faster                                                    |
| raytrace                 | 573 ms                                                                | 352 ms: 1.63x faster                                                    |
| scimark_sor              | 246 ms                                                                | 154 ms: 1.59x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 39.3 us: 1.57x faster                                                   |
| scimark_lu               | 227 ms                                                                | 148 ms: 1.53x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 621 ms: 1.52x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 89.2 ms: 1.50x faster                                                   |
| richards_super           | 107 ms                                                                | 72.2 ms: 1.48x faster                                                   |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.26 sec: 1.45x faster                                                  |
| scimark_monte_carlo      | 128 ms                                                                | 88.7 ms: 1.44x faster                                                   |
| nbody                    | 166 ms                                                                | 115 ms: 1.44x faster                                                    |
| richards                 | 91.7 ms                                                               | 64.6 ms: 1.42x faster                                                   |
| chaos                    | 121 ms                                                                | 85.7 ms: 1.41x faster                                                   |
| go                       | 264 ms                                                                | 187 ms: 1.41x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.71 ms: 1.40x faster                                                   |
| mako                     | 18.9 ms                                                               | 13.6 ms: 1.40x faster                                                   |
| float                    | 135 ms                                                                | 97.8 ms: 1.38x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 270 us: 1.36x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 392 us: 1.35x faster                                                    |
| deepcopy                 | 511 us                                                                | 380 us: 1.34x faster                                                    |
| comprehensions           | 33.1 us                                                               | 24.8 us: 1.34x faster                                                   |
| logging_format           | 10.6 us                                                               | 8.12 us: 1.31x faster                                                   |
| logging_simple           | 9.78 us                                                               | 7.49 us: 1.31x faster                                                   |
| thrift                   | 1.26 ms                                                               | 975 us: 1.29x faster                                                    |
| coroutines               | 37.2 ms                                                               | 28.9 ms: 1.29x faster                                                   |
| sqlglot_transpile        | 2.84 ms                                                               | 2.25 ms: 1.26x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.66 sec: 1.26x faster                                                  |
| pyflate                  | 795 ms                                                                | 642 ms: 1.24x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 81.2 ms: 1.23x faster                                                   |
| tornado_http             | 178 ms                                                                | 147 ms: 1.21x faster                                                    |
| spectral_norm            | 186 ms                                                                | 154 ms: 1.21x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 21.8 ms: 1.21x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 71.9 ms: 1.20x faster                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 3.98 us: 1.15x faster                                                   |
| generators               | 68.1 ms                                                               | 59.1 ms: 1.15x faster                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.38 ms: 1.15x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 14.6 ms: 1.14x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 190 ms: 1.11x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.52 sec: 1.11x faster                                                  |
| xml_etree_generate       | 123 ms                                                                | 112 ms: 1.10x faster                                                    |
| scimark_fft              | 500 ms                                                                | 455 ms: 1.10x faster                                                    |
| unpickle_list            | 6.99 us                                                               | 6.42 us: 1.09x faster                                                   |
| fannkuch                 | 546 ms                                                                | 512 ms: 1.07x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 10.3 ms: 1.06x faster                                                   |
| mdp                      | 3.70 sec                                                              | 3.50 sec: 1.06x faster                                                  |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 7.23 ms: 1.05x faster                                                   |
| json                     | 5.88 ms                                                               | 5.63 ms: 1.04x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 150 ms: 1.04x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 31.0 ms: 1.04x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 34.1 ms: 1.03x faster                                                   |
| sqlite_synth             | 4.12 us                                                               | 4.00 us: 1.03x faster                                                   |
| meteor_contest           | 126 ms                                                                | 124 ms: 1.02x faster                                                    |
| django_template          | 53.3 ms                                                               | 52.6 ms: 1.01x faster                                                   |
| regex_dna                | 257 ms                                                                | 254 ms: 1.01x faster                                                    |
| asyncio_websockets       | 657 ms                                                                | 663 ms: 1.01x slower                                                    |
| docutils                 | 3.53 sec                                                              | 3.58 sec: 1.01x slower                                                  |
| regex_compile            | 177 ms                                                                | 179 ms: 1.02x slower                                                    |
| sqlglot_normalize        | 156 ms                                                                | 159 ms: 1.02x slower                                                    |
| json_loads               | 30.9 us                                                               | 31.6 us: 1.02x slower                                                   |
| nqueens                  | 117 ms                                                                | 124 ms: 1.06x slower                                                    |
| pickle_dict              | 35.1 us                                                               | 37.7 us: 1.07x slower                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 1.23 sec: 1.07x slower                                                  |
| sympy_str                | 329 ms                                                                | 356 ms: 1.08x slower                                                    |
| sympy_expand             | 543 ms                                                                | 589 ms: 1.09x slower                                                    |
| dulwich_log              | 73.5 ms                                                               | 79.9 ms: 1.09x slower                                                   |
| sqlglot_optimize         | 75.4 ms                                                               | 83.1 ms: 1.10x slower                                                   |
| sympy_integrate          | 26.5 ms                                                               | 29.3 ms: 1.10x slower                                                   |
| pprint_pformat           | 2.36 sec                                                              | 2.62 sec: 1.11x slower                                                  |
| pickle                   | 12.5 us                                                               | 13.9 us: 1.12x slower                                                   |
| unpickle                 | 17.5 us                                                               | 19.6 us: 1.12x slower                                                   |
| telco                    | 8.49 ms                                                               | 9.64 ms: 1.14x slower                                                   |
| async_generators         | 452 ms                                                                | 515 ms: 1.14x slower                                                    |
| sympy_sum                | 184 ms                                                                | 214 ms: 1.16x slower                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.96 ms: 1.17x slower                                                   |
| coverage                 | 83.6 ms                                                               | 98.6 ms: 1.18x slower                                                   |
| genshi_xml               | 69.8 ms                                                               | 83.9 ms: 1.20x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.73 ms: 1.27x slower                                                   |
| python_startup           | 11.2 ms                                                               | 14.5 ms: 1.30x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 6.24 ms: 1.50x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 3.73 ms: 1.65x slower                                                   |
| bench_mp_pool            | 14.5 ms                                                               | 2.25 sec: 154.90x slower                                                |
| Geometric mean           | (ref)                                                                 | 1.09x faster                                                            |

Benchmark hidden because not significant (4): pidigits, 2to3, pickle_list, pylint
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (7) of results/bm-20241018-3.14.0a1+-bad9944-JIT/bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx, unpack_sequence

- Geometric mean (including insignificant results): 1.162x faster
# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.37x