# Results vs. 3.10.4

- fork: python
- ref: 2a66dd33dfc0b845042d
- machine: linux-aarch64
- commit hash: 2a66dd3
- commit date: 2024-12-20
- overall geometric mean: 1.224x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 321 ms: 1.19x faster                                                     |
| docutils       | 3.53 sec                                                              | 3.26 sec: 1.08x faster                                                   |
| html5lib       | 86.5 ms                                                               | 71.4 ms: 1.21x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.16x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 962 ms: 2.38x faster                                                     |
| async_tree_none         | 950 ms                                                                | 428 ms: 2.22x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 535 ms: 2.12x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 703 ms: 1.81x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.12x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 93.3 ms: 1.44x faster                                                    |
| nbody          | 166 ms                                                                | 120 ms: 1.38x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.25x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 142 ms: 1.25x faster                                                     |
| regex_effbot   | 4.25 ms                                                               | 4.04 ms: 1.05x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 31.3 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.07x faster                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 265 us: 1.38x faster                                                     |
| pickle_pure_python   | 529 us                                                                | 393 us: 1.35x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.54 sec: 1.32x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 81.3 ms: 1.22x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 182 ms: 1.16x faster                                                     |
| json_dumps           | 16.7 ms                                                               | 14.6 ms: 1.14x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 113 ms: 1.09x faster                                                     |
| xml_etree_iterparse  | 156 ms                                                                | 144 ms: 1.08x faster                                                     |
| json_loads           | 30.9 us                                                               | 32.0 us: 1.04x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.18x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.12 ms: 1.32x slower                                                    |
| python_startup         | 11.2 ms                                                               | 16.4 ms: 1.46x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.39x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.5 ms: 1.40x faster                                                    |
| django_template | 53.3 ms                                                               | 47.8 ms: 1.12x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 33.1 ms: 1.06x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 83.4 ms: 1.19x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.09x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 212 us: 3.12x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 962 ms: 2.38x faster                                                     |
| async_tree_none          | 950 ms                                                                | 428 ms: 2.22x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 535 ms: 2.12x faster                                                     |
| deltablue                | 8.94 ms                                                               | 4.44 ms: 2.01x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 703 ms: 1.81x faster                                                     |
| richards_super           | 107 ms                                                                | 60.8 ms: 1.76x faster                                                    |
| richards                 | 91.7 ms                                                               | 56.3 ms: 1.63x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 38.7 us: 1.59x faster                                                    |
| scimark_sor              | 246 ms                                                                | 158 ms: 1.56x faster                                                     |
| raytrace                 | 573 ms                                                                | 369 ms: 1.55x faster                                                     |
| sqlglot_parse            | 2.40 ms                                                               | 1.55 ms: 1.55x faster                                                    |
| go                       | 264 ms                                                                | 171 ms: 1.55x faster                                                     |
| logging_silent           | 222 ns                                                                | 144 ns: 1.54x faster                                                     |
| scimark_monte_carlo      | 128 ms                                                                | 83.6 ms: 1.53x faster                                                    |
| scimark_lu               | 227 ms                                                                | 155 ms: 1.47x faster                                                     |
| sqlglot_transpile        | 2.84 ms                                                               | 1.94 ms: 1.47x faster                                                    |
| pylint                   | 485 ms                                                                | 336 ms: 1.44x faster                                                     |
| float                    | 135 ms                                                                | 93.3 ms: 1.44x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 93.2 ms: 1.44x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.5 ms: 1.40x faster                                                    |
| chaos                    | 121 ms                                                                | 87.5 ms: 1.38x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 265 us: 1.38x faster                                                     |
| nbody                    | 166 ms                                                                | 120 ms: 1.38x faster                                                     |
| pickle_pure_python       | 529 us                                                                | 393 us: 1.35x faster                                                     |
| pyflate                  | 795 ms                                                                | 592 ms: 1.34x faster                                                     |
| deepcopy                 | 511 us                                                                | 385 us: 1.33x faster                                                     |
| comprehensions           | 33.1 us                                                               | 25.0 us: 1.33x faster                                                    |
| spectral_norm            | 186 ms                                                                | 141 ms: 1.33x faster                                                     |
| tomli_loads              | 3.36 sec                                                              | 2.54 sec: 1.32x faster                                                   |
| generators               | 68.1 ms                                                               | 51.9 ms: 1.31x faster                                                    |
| coroutines               | 37.2 ms                                                               | 29.2 ms: 1.27x faster                                                    |
| sqlalchemy_declarative   | 197 ms                                                                | 156 ms: 1.27x faster                                                     |
| regex_compile            | 177 ms                                                                | 142 ms: 1.25x faster                                                     |
| thrift                   | 1.26 ms                                                               | 1.02 ms: 1.23x faster                                                    |
| logging_simple           | 9.78 us                                                               | 7.93 us: 1.23x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 81.3 ms: 1.22x faster                                                    |
| logging_format           | 10.6 us                                                               | 8.73 us: 1.21x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 71.4 ms: 1.21x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 21.9 ms: 1.20x faster                                                    |
| scimark_fft              | 500 ms                                                                | 418 ms: 1.20x faster                                                     |
| 2to3                     | 381 ms                                                                | 321 ms: 1.19x faster                                                     |
| sqlalchemy_imperative    | 20.5 ms                                                               | 17.4 ms: 1.18x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.93 us: 1.17x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 182 ms: 1.16x faster                                                     |
| pycparser                | 1.69 sec                                                              | 1.46 sec: 1.16x faster                                                   |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.63 ms: 1.15x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 14.6 ms: 1.14x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 9.59 ms: 1.14x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.42 ms: 1.12x faster                                                    |
| django_template          | 53.3 ms                                                               | 47.8 ms: 1.12x faster                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 68.2 ms: 1.11x faster                                                    |
| sqlglot_normalize        | 156 ms                                                                | 142 ms: 1.10x faster                                                     |
| xml_etree_generate       | 123 ms                                                                | 113 ms: 1.09x faster                                                     |
| docutils                 | 3.53 sec                                                              | 3.26 sec: 1.08x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 24.5 ms: 1.08x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 144 ms: 1.08x faster                                                     |
| sympy_sum                | 184 ms                                                                | 171 ms: 1.08x faster                                                     |
| genshi_text              | 35.2 ms                                                               | 33.1 ms: 1.06x faster                                                    |
| sympy_str                | 329 ms                                                                | 311 ms: 1.06x faster                                                     |
| sympy_expand             | 543 ms                                                                | 514 ms: 1.06x faster                                                     |
| regex_effbot             | 4.25 ms                                                               | 4.04 ms: 1.05x faster                                                    |
| fannkuch                 | 546 ms                                                                | 524 ms: 1.04x faster                                                     |
| mdp                      | 3.70 sec                                                              | 3.57 sec: 1.04x faster                                                   |
| regex_v8                 | 32.2 ms                                                               | 31.3 ms: 1.03x faster                                                    |
| asyncio_websockets       | 657 ms                                                                | 671 ms: 1.02x slower                                                     |
| json_loads               | 30.9 us                                                               | 32.0 us: 1.04x slower                                                    |
| nqueens                  | 117 ms                                                                | 129 ms: 1.09x slower                                                     |
| pprint_safe_repr         | 1.15 sec                                                              | 1.26 sec: 1.10x slower                                                   |
| pprint_pformat           | 2.36 sec                                                              | 2.65 sec: 1.12x slower                                                   |
| telco                    | 8.49 ms                                                               | 9.82 ms: 1.16x slower                                                    |
| mypy2                    | 936 ms                                                                | 1.09 sec: 1.16x slower                                                   |
| genshi_xml               | 69.8 ms                                                               | 83.4 ms: 1.19x slower                                                    |
| async_generators         | 452 ms                                                                | 543 ms: 1.20x slower                                                     |
| coverage                 | 83.6 ms                                                               | 103 ms: 1.23x slower                                                     |
| python_startup_no_site   | 6.89 ms                                                               | 9.12 ms: 1.32x slower                                                    |
| python_startup           | 11.2 ms                                                               | 16.4 ms: 1.46x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.68 ms: 1.63x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 7.13 ms: 1.72x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 1.37 sec: 94.22x slower                                                  |
| Geometric mean           | (ref)                                                                 | 1.14x faster                                                             |

Benchmark hidden because not significant (6): sqlite_synth, dulwich_log, json, meteor_contest, regex_dna, pidigits
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241220-3.14.0a3+-2a66dd3-JIT/bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.224x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: 1.33x