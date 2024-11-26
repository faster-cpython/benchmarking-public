# Results vs. 3.10.4

- fork: python
- ref: v3.13.0
- machine: linux-aarch64
- commit hash: 60403a5
- commit date: 2024-10-07
- overall geometric mean: 1.297x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 304 ms: 1.26x faster                                     |
| chameleon      | 10.8 ms                                                               | 9.08 ms: 1.19x faster                                    |
| docutils       | 3.53 sec                                                              | 2.89 sec: 1.22x faster                                   |
| html5lib       | 86.5 ms                                                               | 66.4 ms: 1.30x faster                                    |
| tornado_http   | 178 ms                                                                | 128 ms: 1.39x faster                                     |
| Geometric mean | (ref)                                                                 | 1.27x faster                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|-------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 1.11 sec: 2.06x faster                                   |
| async_tree_none         | 950 ms                                                                | 497 ms: 1.91x faster                                     |
| async_tree_memoization  | 1.13 sec                                                              | 651 ms: 1.74x faster                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 766 ms: 1.66x faster                                     |
| Geometric mean          | (ref)                                                                 | 1.84x faster                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| nbody          | 166 ms                                                                | 114 ms: 1.45x faster                                     |
| float          | 135 ms                                                                | 93.3 ms: 1.44x faster                                    |
| pidigits       | 235 ms                                                                | 234 ms: 1.01x faster                                     |
| Geometric mean | (ref)                                                                 | 1.28x faster                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 127 ms: 1.39x faster                                     |
| regex_dna      | 257 ms                                                                | 253 ms: 1.02x faster                                     |
| regex_v8       | 32.2 ms                                                               | 31.8 ms: 1.01x faster                                    |
| regex_effbot   | 4.25 ms                                                               | 4.89 ms: 1.15x slower                                    |
| Geometric mean | (ref)                                                                 | 1.06x faster                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 357 us: 1.48x faster                                     |
| unpickle_pure_python | 366 us                                                                | 251 us: 1.46x faster                                     |
| tomli_loads          | 3.36 sec                                                              | 2.54 sec: 1.32x faster                                   |
| xml_etree_process    | 99.5 ms                                                               | 80.5 ms: 1.24x faster                                    |
| json_dumps           | 16.7 ms                                                               | 13.6 ms: 1.23x faster                                    |
| xml_etree_generate   | 123 ms                                                                | 113 ms: 1.08x faster                                     |
| xml_etree_parse      | 212 ms                                                                | 197 ms: 1.08x faster                                     |
| xml_etree_iterparse  | 156 ms                                                                | 149 ms: 1.04x faster                                     |
| json_loads           | 30.9 us                                                               | 31.7 us: 1.02x slower                                    |
| Geometric mean       | (ref)                                                                 | 1.20x faster                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.73 ms: 1.27x slower                                    |
| python_startup         | 11.2 ms                                                               | 15.4 ms: 1.38x slower                                    |
| Geometric mean         | (ref)                                                                 | 1.32x slower                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.4 ms: 1.42x faster                                    |
| django_template | 53.3 ms                                                               | 41.6 ms: 1.28x faster                                    |
| genshi_text     | 35.2 ms                                                               | 27.7 ms: 1.27x faster                                    |
| genshi_xml      | 69.8 ms                                                               | 60.3 ms: 1.16x faster                                    |
| Geometric mean  | (ref)                                                                 | 1.28x faster                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|--------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 193 us: 3.42x faster                                     |
| deltablue                | 8.94 ms                                                               | 3.82 ms: 2.34x faster                                    |
| async_tree_io            | 2.28 sec                                                              | 1.11 sec: 2.06x faster                                   |
| raytrace                 | 573 ms                                                                | 300 ms: 1.91x faster                                     |
| async_tree_none          | 950 ms                                                                | 497 ms: 1.91x faster                                     |
| bench_mp_pool            | 14.5 ms                                                               | 7.68 ms: 1.89x faster                                    |
| generators               | 68.1 ms                                                               | 37.6 ms: 1.81x faster                                    |
| richards_super           | 107 ms                                                                | 60.1 ms: 1.78x faster                                    |
| chaos                    | 121 ms                                                                | 68.0 ms: 1.78x faster                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.38 ms: 1.74x faster                                    |
| async_tree_memoization   | 1.13 sec                                                              | 651 ms: 1.74x faster                                     |
| richards                 | 91.7 ms                                                               | 53.6 ms: 1.71x faster                                    |
| logging_silent           | 222 ns                                                                | 133 ns: 1.67x faster                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 766 ms: 1.66x faster                                     |
| go                       | 264 ms                                                                | 160 ms: 1.65x faster                                     |
| sqlglot_transpile        | 2.84 ms                                                               | 1.73 ms: 1.64x faster                                    |
| scimark_lu               | 227 ms                                                                | 139 ms: 1.63x faster                                     |
| comprehensions           | 33.1 us                                                               | 20.4 us: 1.63x faster                                    |
| crypto_pyaes             | 134 ms                                                                | 83.7 ms: 1.60x faster                                    |
| scimark_sor              | 246 ms                                                                | 160 ms: 1.54x faster                                     |
| hexiom                   | 10.9 ms                                                               | 7.11 ms: 1.54x faster                                    |
| scimark_monte_carlo      | 128 ms                                                                | 83.6 ms: 1.53x faster                                    |
| pickle_pure_python       | 529 us                                                                | 357 us: 1.48x faster                                     |
| unpickle_pure_python     | 366 us                                                                | 251 us: 1.46x faster                                     |
| nbody                    | 166 ms                                                                | 114 ms: 1.45x faster                                     |
| float                    | 135 ms                                                                | 93.3 ms: 1.44x faster                                    |
| pyflate                  | 795 ms                                                                | 556 ms: 1.43x faster                                     |
| pylint                   | 485 ms                                                                | 342 ms: 1.42x faster                                     |
| mako                     | 18.9 ms                                                               | 13.4 ms: 1.42x faster                                    |
| tornado_http             | 178 ms                                                                | 128 ms: 1.39x faster                                     |
| regex_compile            | 177 ms                                                                | 127 ms: 1.39x faster                                     |
| logging_simple           | 9.78 us                                                               | 7.07 us: 1.38x faster                                    |
| logging_format           | 10.6 us                                                               | 7.82 us: 1.36x faster                                    |
| sqlalchemy_imperative    | 20.5 ms                                                               | 15.1 ms: 1.35x faster                                    |
| pycparser                | 1.69 sec                                                              | 1.27 sec: 1.33x faster                                   |
| tomli_loads              | 3.36 sec                                                              | 2.54 sec: 1.32x faster                                   |
| sqlalchemy_declarative   | 197 ms                                                                | 150 ms: 1.31x faster                                     |
| spectral_norm            | 186 ms                                                                | 143 ms: 1.31x faster                                     |
| coroutines               | 37.2 ms                                                               | 28.5 ms: 1.30x faster                                    |
| html5lib                 | 86.5 ms                                                               | 66.4 ms: 1.30x faster                                    |
| thrift                   | 1.26 ms                                                               | 968 us: 1.30x faster                                     |
| sympy_sum                | 184 ms                                                                | 144 ms: 1.28x faster                                     |
| django_template          | 53.3 ms                                                               | 41.6 ms: 1.28x faster                                    |
| sympy_integrate          | 26.5 ms                                                               | 20.8 ms: 1.27x faster                                    |
| genshi_text              | 35.2 ms                                                               | 27.7 ms: 1.27x faster                                    |
| 2to3                     | 381 ms                                                                | 304 ms: 1.26x faster                                     |
| bench_thread_pool        | 1.59 ms                                                               | 1.27 ms: 1.25x faster                                    |
| pprint_pformat           | 2.36 sec                                                              | 1.90 sec: 1.24x faster                                   |
| sympy_str                | 329 ms                                                                | 264 ms: 1.24x faster                                     |
| pprint_safe_repr         | 1.15 sec                                                              | 926 ms: 1.24x faster                                     |
| xml_etree_process        | 99.5 ms                                                               | 80.5 ms: 1.24x faster                                    |
| sqlglot_normalize        | 156 ms                                                                | 127 ms: 1.23x faster                                     |
| json_dumps               | 16.7 ms                                                               | 13.6 ms: 1.23x faster                                    |
| deepcopy_memo            | 61.7 us                                                               | 50.4 us: 1.22x faster                                    |
| docutils                 | 3.53 sec                                                              | 2.89 sec: 1.22x faster                                   |
| sqlglot_optimize         | 75.4 ms                                                               | 62.2 ms: 1.21x faster                                    |
| chameleon                | 10.8 ms                                                               | 9.08 ms: 1.19x faster                                    |
| sympy_expand             | 543 ms                                                                | 457 ms: 1.19x faster                                     |
| fannkuch                 | 546 ms                                                                | 461 ms: 1.18x faster                                     |
| nqueens                  | 117 ms                                                                | 100 ms: 1.17x faster                                     |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.51 ms: 1.17x faster                                    |
| pathlib                  | 26.3 ms                                                               | 22.7 ms: 1.16x faster                                    |
| genshi_xml               | 69.8 ms                                                               | 60.3 ms: 1.16x faster                                    |
| deepcopy                 | 511 us                                                                | 447 us: 1.14x faster                                     |
| deepcopy_reduce          | 4.60 us                                                               | 4.07 us: 1.13x faster                                    |
| scimark_fft              | 500 ms                                                                | 447 ms: 1.12x faster                                     |
| meteor_contest           | 126 ms                                                                | 114 ms: 1.11x faster                                     |
| mdp                      | 3.70 sec                                                              | 3.34 sec: 1.11x faster                                   |
| xml_etree_generate       | 123 ms                                                                | 113 ms: 1.08x faster                                     |
| xml_etree_parse          | 212 ms                                                                | 197 ms: 1.08x faster                                     |
| xml_etree_iterparse      | 156 ms                                                                | 149 ms: 1.04x faster                                     |
| json                     | 5.88 ms                                                               | 5.73 ms: 1.03x faster                                    |
| regex_dna                | 257 ms                                                                | 253 ms: 1.02x faster                                     |
| regex_v8                 | 32.2 ms                                                               | 31.8 ms: 1.01x faster                                    |
| pidigits                 | 235 ms                                                                | 234 ms: 1.01x faster                                     |
| json_loads               | 30.9 us                                                               | 31.7 us: 1.02x slower                                    |
| async_generators         | 452 ms                                                                | 489 ms: 1.08x slower                                     |
| telco                    | 8.49 ms                                                               | 9.74 ms: 1.15x slower                                    |
| regex_effbot             | 4.25 ms                                                               | 4.89 ms: 1.15x slower                                    |
| coverage                 | 83.6 ms                                                               | 99.1 ms: 1.19x slower                                    |
| mypy2                    | 936 ms                                                                | 1.15 sec: 1.23x slower                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.73 ms: 1.27x slower                                    |
| python_startup           | 11.2 ms                                                               | 15.4 ms: 1.38x slower                                    |
| gc_traversal             | 4.15 ms                                                               | 5.77 ms: 1.39x slower                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.35 ms: 1.48x slower                                    |
| Geometric mean           | (ref)                                                                 | 1.29x faster                                             |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, dulwich_log, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, gevent_hub, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.297x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.26x