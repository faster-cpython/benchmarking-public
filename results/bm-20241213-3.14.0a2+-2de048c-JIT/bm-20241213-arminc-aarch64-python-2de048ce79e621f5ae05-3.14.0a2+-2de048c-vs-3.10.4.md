# Results vs. 3.10.4

- fork: python
- ref: 2de048ce79e621f5ae05
- machine: linux-aarch64
- commit hash: 2de048c
- commit date: 2024-12-13
- overall geometric mean: 1.231x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241213-arminc-aarch64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 318 ms: 1.20x faster                                                     |
| docutils       | 3.53 sec                                                              | 3.20 sec: 1.10x faster                                                   |
| html5lib       | 86.5 ms                                                               | 70.9 ms: 1.22x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.17x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241213-arminc-aarch64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 945 ms: 2.42x faster                                                     |
| async_tree_none         | 950 ms                                                                | 406 ms: 2.34x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 509 ms: 2.23x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 699 ms: 1.82x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.19x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241213-arminc-aarch64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 92.3 ms: 1.46x faster                                                    |
| nbody          | 166 ms                                                                | 117 ms: 1.41x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.26x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241213-arminc-aarch64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 142 ms: 1.24x faster                                                     |
| regex_effbot   | 4.25 ms                                                               | 4.05 ms: 1.05x faster                                                    |
| regex_dna      | 257 ms                                                                | 247 ms: 1.04x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.08x faster                                                             |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241213-arminc-aarch64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 265 us: 1.38x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.51 sec: 1.34x faster                                                   |
| pickle_pure_python   | 529 us                                                                | 415 us: 1.28x faster                                                     |
| xml_etree_process    | 99.5 ms                                                               | 81.2 ms: 1.23x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 179 ms: 1.19x faster                                                     |
| json_dumps           | 16.7 ms                                                               | 14.9 ms: 1.12x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 111 ms: 1.10x faster                                                     |
| xml_etree_iterparse  | 156 ms                                                                | 144 ms: 1.09x faster                                                     |
| json_loads           | 30.9 us                                                               | 32.4 us: 1.05x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.18x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241213-arminc-aarch64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.07 ms: 1.32x slower                                                    |
| python_startup         | 11.2 ms                                                               | 16.3 ms: 1.45x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.38x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241213-arminc-aarch64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.5 ms: 1.40x faster                                                    |
| django_template | 53.3 ms                                                               | 48.0 ms: 1.11x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 32.4 ms: 1.09x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 80.3 ms: 1.15x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.10x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241213-arminc-aarch64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 226 us: 2.92x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 945 ms: 2.42x faster                                                     |
| async_tree_none          | 950 ms                                                                | 406 ms: 2.34x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 509 ms: 2.23x faster                                                     |
| deltablue                | 8.94 ms                                                               | 4.27 ms: 2.10x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 699 ms: 1.82x faster                                                     |
| richards_super           | 107 ms                                                                | 64.6 ms: 1.66x faster                                                    |
| raytrace                 | 573 ms                                                                | 370 ms: 1.55x faster                                                     |
| richards                 | 91.7 ms                                                               | 59.3 ms: 1.55x faster                                                    |
| go                       | 264 ms                                                                | 171 ms: 1.54x faster                                                     |
| scimark_monte_carlo      | 128 ms                                                                | 82.9 ms: 1.54x faster                                                    |
| scimark_sor              | 246 ms                                                                | 163 ms: 1.51x faster                                                     |
| logging_silent           | 222 ns                                                                | 147 ns: 1.51x faster                                                     |
| sqlglot_transpile        | 2.84 ms                                                               | 1.91 ms: 1.49x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 41.6 us: 1.48x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.63 ms: 1.47x faster                                                    |
| scimark_lu               | 227 ms                                                                | 155 ms: 1.46x faster                                                     |
| float                    | 135 ms                                                                | 92.3 ms: 1.46x faster                                                    |
| pylint                   | 485 ms                                                                | 339 ms: 1.43x faster                                                     |
| crypto_pyaes             | 134 ms                                                                | 93.9 ms: 1.43x faster                                                    |
| nbody                    | 166 ms                                                                | 117 ms: 1.41x faster                                                     |
| chaos                    | 121 ms                                                                | 85.9 ms: 1.41x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.5 ms: 1.40x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 265 us: 1.38x faster                                                     |
| spectral_norm            | 186 ms                                                                | 139 ms: 1.34x faster                                                     |
| comprehensions           | 33.1 us                                                               | 24.7 us: 1.34x faster                                                    |
| generators               | 68.1 ms                                                               | 50.7 ms: 1.34x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.51 sec: 1.34x faster                                                   |
| pyflate                  | 795 ms                                                                | 609 ms: 1.30x faster                                                     |
| coroutines               | 37.2 ms                                                               | 28.6 ms: 1.30x faster                                                    |
| sqlalchemy_declarative   | 197 ms                                                                | 152 ms: 1.30x faster                                                     |
| deepcopy                 | 511 us                                                                | 399 us: 1.28x faster                                                     |
| pickle_pure_python       | 529 us                                                                | 415 us: 1.28x faster                                                     |
| sqlalchemy_imperative    | 20.5 ms                                                               | 16.3 ms: 1.26x faster                                                    |
| thrift                   | 1.26 ms                                                               | 1.01 ms: 1.25x faster                                                    |
| regex_compile            | 177 ms                                                                | 142 ms: 1.24x faster                                                     |
| logging_simple           | 9.78 us                                                               | 7.96 us: 1.23x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 81.2 ms: 1.23x faster                                                    |
| logging_format           | 10.6 us                                                               | 8.67 us: 1.22x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 70.9 ms: 1.22x faster                                                    |
| 2to3                     | 381 ms                                                                | 318 ms: 1.20x faster                                                     |
| scimark_fft              | 500 ms                                                                | 419 ms: 1.19x faster                                                     |
| xml_etree_parse          | 212 ms                                                                | 179 ms: 1.19x faster                                                     |
| pycparser                | 1.69 sec                                                              | 1.43 sec: 1.19x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 9.31 ms: 1.17x faster                                                    |
| sympy_sum                | 184 ms                                                                | 158 ms: 1.16x faster                                                     |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.60 ms: 1.16x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.39 ms: 1.15x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 23.3 ms: 1.14x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 23.1 ms: 1.14x faster                                                    |
| sqlglot_normalize        | 156 ms                                                                | 139 ms: 1.12x faster                                                     |
| json_dumps               | 16.7 ms                                                               | 14.9 ms: 1.12x faster                                                    |
| django_template          | 53.3 ms                                                               | 48.0 ms: 1.11x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 4.15 us: 1.11x faster                                                    |
| xml_etree_generate       | 123 ms                                                                | 111 ms: 1.10x faster                                                     |
| docutils                 | 3.53 sec                                                              | 3.20 sec: 1.10x faster                                                   |
| sqlglot_optimize         | 75.4 ms                                                               | 68.4 ms: 1.10x faster                                                    |
| sympy_str                | 329 ms                                                                | 299 ms: 1.10x faster                                                     |
| genshi_text              | 35.2 ms                                                               | 32.4 ms: 1.09x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 144 ms: 1.09x faster                                                     |
| fannkuch                 | 546 ms                                                                | 506 ms: 1.08x faster                                                     |
| sympy_expand             | 543 ms                                                                | 511 ms: 1.06x faster                                                     |
| dulwich_log              | 73.5 ms                                                               | 69.9 ms: 1.05x faster                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.05 ms: 1.05x faster                                                    |
| regex_dna                | 257 ms                                                                | 247 ms: 1.04x faster                                                     |
| mdp                      | 3.70 sec                                                              | 3.56 sec: 1.04x faster                                                   |
| json_loads               | 30.9 us                                                               | 32.4 us: 1.05x slower                                                    |
| nqueens                  | 117 ms                                                                | 130 ms: 1.11x slower                                                     |
| pprint_safe_repr         | 1.15 sec                                                              | 1.27 sec: 1.11x slower                                                   |
| pprint_pformat           | 2.36 sec                                                              | 2.62 sec: 1.11x slower                                                   |
| genshi_xml               | 69.8 ms                                                               | 80.3 ms: 1.15x slower                                                    |
| mypy2                    | 936 ms                                                                | 1.08 sec: 1.15x slower                                                   |
| async_generators         | 452 ms                                                                | 532 ms: 1.18x slower                                                     |
| telco                    | 8.49 ms                                                               | 10.0 ms: 1.18x slower                                                    |
| coverage                 | 83.6 ms                                                               | 107 ms: 1.28x slower                                                     |
| python_startup_no_site   | 6.89 ms                                                               | 9.07 ms: 1.32x slower                                                    |
| python_startup           | 11.2 ms                                                               | 16.3 ms: 1.45x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.66 ms: 1.62x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.94 ms: 1.67x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 1.66 sec: 114.19x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.14x faster                                                             |

Benchmark hidden because not significant (6): meteor_contest, json, regex_v8, sqlite_synth, asyncio_websockets, pidigits
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241213-3.14.0a2+-2de048c-JIT/bm-20241213-arminc-aarch64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.231x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: 1.33x