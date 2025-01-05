# Results vs. 3.10.4

- fork: python
- ref: 0cafa97932c6574734bb
- machine: linux-aarch64
- commit hash: 0cafa97
- commit date: 2025-01-04
- overall geometric mean: 1.224x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 321 ms: 1.19x faster                                                     |
| docutils       | 3.53 sec                                                              | 3.27 sec: 1.08x faster                                                   |
| html5lib       | 86.5 ms                                                               | 69.8 ms: 1.24x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.17x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 917 ms: 2.49x faster                                                     |
| async_tree_none         | 950 ms                                                                | 405 ms: 2.34x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 510 ms: 2.22x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 698 ms: 1.82x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.21x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 89.7 ms: 1.50x faster                                                    |
| nbody          | 166 ms                                                                | 119 ms: 1.39x faster                                                     |
| pidigits       | 235 ms                                                                | 243 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.27x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 142 ms: 1.24x faster                                                     |
| regex_effbot   | 4.25 ms                                                               | 4.03 ms: 1.05x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.07x faster                                                             |

Benchmark hidden because not significant (2): regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 384 us: 1.38x faster                                                     |
| unpickle_pure_python | 366 us                                                                | 266 us: 1.38x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.54 sec: 1.32x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 84.1 ms: 1.18x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 183 ms: 1.16x faster                                                     |
| json_dumps           | 16.7 ms                                                               | 14.6 ms: 1.15x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 143 ms: 1.09x faster                                                     |
| xml_etree_generate   | 123 ms                                                                | 116 ms: 1.06x faster                                                     |
| Geometric mean       | (ref)                                                                 | 1.18x faster                                                             |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.01 ms: 1.31x slower                                                    |
| python_startup         | 11.2 ms                                                               | 16.4 ms: 1.47x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.39x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.7 ms: 1.38x faster                                                    |
| django_template | 53.3 ms                                                               | 48.5 ms: 1.10x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 81.5 ms: 1.17x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.07x faster                                                             |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 224 us: 2.95x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 917 ms: 2.49x faster                                                     |
| async_tree_none          | 950 ms                                                                | 405 ms: 2.34x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 510 ms: 2.22x faster                                                     |
| deltablue                | 8.94 ms                                                               | 4.52 ms: 1.98x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 698 ms: 1.82x faster                                                     |
| richards_super           | 107 ms                                                                | 62.4 ms: 1.72x faster                                                    |
| richards                 | 91.7 ms                                                               | 56.4 ms: 1.62x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 38.4 us: 1.61x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.51 ms: 1.59x faster                                                    |
| scimark_sor              | 246 ms                                                                | 160 ms: 1.54x faster                                                     |
| go                       | 264 ms                                                                | 174 ms: 1.52x faster                                                     |
| raytrace                 | 573 ms                                                                | 378 ms: 1.52x faster                                                     |
| logging_silent           | 222 ns                                                                | 147 ns: 1.51x faster                                                     |
| float                    | 135 ms                                                                | 89.7 ms: 1.50x faster                                                    |
| scimark_lu               | 227 ms                                                                | 152 ms: 1.49x faster                                                     |
| sqlglot_transpile        | 2.84 ms                                                               | 1.91 ms: 1.49x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 88.8 ms: 1.44x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 93.4 ms: 1.44x faster                                                    |
| chaos                    | 121 ms                                                                | 85.6 ms: 1.41x faster                                                    |
| nbody                    | 166 ms                                                                | 119 ms: 1.39x faster                                                     |
| mako                     | 18.9 ms                                                               | 13.7 ms: 1.38x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 384 us: 1.38x faster                                                     |
| unpickle_pure_python     | 366 us                                                                | 266 us: 1.38x faster                                                     |
| pylint                   | 485 ms                                                                | 353 ms: 1.38x faster                                                     |
| generators               | 68.1 ms                                                               | 51.0 ms: 1.33x faster                                                    |
| pyflate                  | 795 ms                                                                | 598 ms: 1.33x faster                                                     |
| tomli_loads              | 3.36 sec                                                              | 2.54 sec: 1.32x faster                                                   |
| spectral_norm            | 186 ms                                                                | 143 ms: 1.30x faster                                                     |
| comprehensions           | 33.1 us                                                               | 25.5 us: 1.30x faster                                                    |
| deepcopy                 | 511 us                                                                | 401 us: 1.27x faster                                                     |
| coroutines               | 37.2 ms                                                               | 29.6 ms: 1.26x faster                                                    |
| regex_compile            | 177 ms                                                                | 142 ms: 1.24x faster                                                     |
| sqlalchemy_declarative   | 197 ms                                                                | 159 ms: 1.24x faster                                                     |
| html5lib                 | 86.5 ms                                                               | 69.8 ms: 1.24x faster                                                    |
| thrift                   | 1.26 ms                                                               | 1.02 ms: 1.24x faster                                                    |
| logging_simple           | 9.78 us                                                               | 8.19 us: 1.19x faster                                                    |
| sqlalchemy_imperative    | 20.5 ms                                                               | 17.2 ms: 1.19x faster                                                    |
| 2to3                     | 381 ms                                                                | 321 ms: 1.19x faster                                                     |
| xml_etree_process        | 99.5 ms                                                               | 84.1 ms: 1.18x faster                                                    |
| logging_format           | 10.6 us                                                               | 9.00 us: 1.18x faster                                                    |
| scimark_fft              | 500 ms                                                                | 425 ms: 1.18x faster                                                     |
| bench_thread_pool        | 1.59 ms                                                               | 1.36 ms: 1.17x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.95 us: 1.16x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 183 ms: 1.16x faster                                                     |
| pathlib                  | 26.3 ms                                                               | 22.8 ms: 1.15x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 14.6 ms: 1.15x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 23.2 ms: 1.14x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.49 sec: 1.14x faster                                                   |
| sympy_sum                | 184 ms                                                                | 163 ms: 1.13x faster                                                     |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.79 ms: 1.12x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 9.81 ms: 1.11x faster                                                    |
| django_template          | 53.3 ms                                                               | 48.5 ms: 1.10x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 143 ms: 1.09x faster                                                     |
| docutils                 | 3.53 sec                                                              | 3.27 sec: 1.08x faster                                                   |
| sqlglot_normalize        | 156 ms                                                                | 145 ms: 1.08x faster                                                     |
| sympy_str                | 329 ms                                                                | 308 ms: 1.07x faster                                                     |
| fannkuch                 | 546 ms                                                                | 514 ms: 1.06x faster                                                     |
| sqlglot_optimize         | 75.4 ms                                                               | 71.3 ms: 1.06x faster                                                    |
| xml_etree_generate       | 123 ms                                                                | 116 ms: 1.06x faster                                                     |
| regex_effbot             | 4.25 ms                                                               | 4.03 ms: 1.05x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 69.9 ms: 1.05x faster                                                    |
| sympy_expand             | 543 ms                                                                | 519 ms: 1.04x faster                                                     |
| mdp                      | 3.70 sec                                                              | 3.61 sec: 1.02x faster                                                   |
| asyncio_websockets       | 657 ms                                                                | 677 ms: 1.03x slower                                                     |
| pidigits                 | 235 ms                                                                | 243 ms: 1.03x slower                                                     |
| pprint_safe_repr         | 1.15 sec                                                              | 1.25 sec: 1.09x slower                                                   |
| pprint_pformat           | 2.36 sec                                                              | 2.58 sec: 1.09x slower                                                   |
| nqueens                  | 117 ms                                                                | 131 ms: 1.11x slower                                                     |
| telco                    | 8.49 ms                                                               | 9.89 ms: 1.16x slower                                                    |
| genshi_xml               | 69.8 ms                                                               | 81.5 ms: 1.17x slower                                                    |
| async_generators         | 452 ms                                                                | 528 ms: 1.17x slower                                                     |
| mypy2                    | 936 ms                                                                | 1.11 sec: 1.19x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 9.01 ms: 1.31x slower                                                    |
| coverage                 | 83.6 ms                                                               | 111 ms: 1.32x slower                                                     |
| python_startup           | 11.2 ms                                                               | 16.4 ms: 1.47x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.71 ms: 1.64x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.91 ms: 1.66x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 1.42 sec: 98.00x slower                                                  |
| Geometric mean           | (ref)                                                                 | 1.13x faster                                                             |

Benchmark hidden because not significant (7): regex_dna, meteor_contest, json, genshi_text, regex_v8, sqlite_synth, json_loads
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250104-3.14.0a3+-0cafa97-JIT/bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.224x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: 1.33x