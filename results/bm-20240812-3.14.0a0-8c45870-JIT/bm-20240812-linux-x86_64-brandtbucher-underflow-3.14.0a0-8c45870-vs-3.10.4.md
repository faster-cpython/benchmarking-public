# Results vs. 3.10.4

- fork: brandtbucher
- ref: underflow
- machine: linux-x86_64
- commit hash: 8c45870
- commit date: 2024-08-12
- overall geometric mean: 1.41x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240812-linux-x86_64-brandtbucher-underflow-3.14.0a0-8c45870 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 280 ms: 1.24x faster                                             |
| html5lib       | 88.9 ms                                                | 68.6 ms: 1.30x faster                                            |
| tornado_http   | 136 ms                                                 | 96.9 ms: 1.41x faster                                            |
| Geometric mean | (ref)                                                  | 1.23x faster                                                     |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240812-linux-x86_64-brandtbucher-underflow-3.14.0a0-8c45870 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 324 ms: 2.25x faster                                             |
| async_tree_memoization  | 870 ms                                                 | 425 ms: 2.05x faster                                             |
| async_tree_io           | 1.77 sec                                               | 902 ms: 1.96x faster                                             |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 566 ms: 1.79x faster                                             |
| Geometric mean          | (ref)                                                  | 2.01x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240812-linux-x86_64-brandtbucher-underflow-3.14.0a0-8c45870 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 82.3 ms: 1.87x faster                                            |
| float          | 117 ms                                                 | 70.7 ms: 1.66x faster                                            |
| pidigits       | 191 ms                                                 | 188 ms: 1.01x faster                                             |
| Geometric mean | (ref)                                                  | 1.46x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240812-linux-x86_64-brandtbucher-underflow-3.14.0a0-8c45870 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 146 ms: 1.29x faster                                             |
| regex_v8       | 27.8 ms                                                | 24.6 ms: 1.13x faster                                            |
| regex_dna      | 227 ms                                                 | 210 ms: 1.08x faster                                             |
| Geometric mean | (ref)                                                  | 1.12x faster                                                     |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240812-linux-x86_64-brandtbucher-underflow-3.14.0a0-8c45870 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 194 us: 1.71x faster                                             |
| pickle_pure_python   | 484 us                                                 | 304 us: 1.60x faster                                             |
| tomli_loads          | 3.14 sec                                               | 2.09 sec: 1.51x faster                                           |
| xml_etree_process    | 79.1 ms                                                | 56.3 ms: 1.40x faster                                            |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.36x faster                                            |
| xml_etree_generate   | 99.4 ms                                                | 80.7 ms: 1.23x faster                                            |
| xml_etree_iterparse  | 115 ms                                                 | 98.7 ms: 1.17x faster                                            |
| xml_etree_parse      | 168 ms                                                 | 148 ms: 1.14x faster                                             |
| json_loads           | 31.2 us                                                | 28.0 us: 1.11x faster                                            |
| Geometric mean       | (ref)                                                  | 1.34x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240812-linux-x86_64-brandtbucher-underflow-3.14.0a0-8c45870 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.38x faster                                            |
| python_startup_no_site | 5.93 ms                                                | 7.17 ms: 1.21x slower                                            |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240812-linux-x86_64-brandtbucher-underflow-3.14.0a0-8c45870 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.74 ms: 1.68x faster                                            |
| genshi_text     | 31.8 ms                                                | 23.8 ms: 1.34x faster                                            |
| django_template | 48.2 ms                                                | 36.8 ms: 1.31x faster                                            |
| genshi_xml      | 66.0 ms                                                | 63.5 ms: 1.04x faster                                            |
| Geometric mean  | (ref)                                                  | 1.32x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240812-linux-x86_64-brandtbucher-underflow-3.14.0a0-8c45870 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 171 us: 3.17x faster                                             |
| deltablue                | 7.91 ms                                                | 3.17 ms: 2.50x faster                                            |
| generators               | 80.1 ms                                                | 33.5 ms: 2.39x faster                                            |
| async_tree_none          | 728 ms                                                 | 324 ms: 2.25x faster                                             |
| deepcopy_memo            | 58.5 us                                                | 26.3 us: 2.23x faster                                            |
| richards_super           | 94.7 ms                                                | 43.4 ms: 2.19x faster                                            |
| richards                 | 79.3 ms                                                | 38.4 ms: 2.06x faster                                            |
| async_tree_memoization   | 870 ms                                                 | 425 ms: 2.05x faster                                             |
| scimark_monte_carlo      | 118 ms                                                 | 58.2 ms: 2.03x faster                                            |
| async_tree_io            | 1.77 sec                                               | 902 ms: 1.96x faster                                             |
| chaos                    | 115 ms                                                 | 58.9 ms: 1.96x faster                                            |
| logging_silent           | 190 ns                                                 | 97.0 ns: 1.96x faster                                            |
| crypto_pyaes             | 128 ms                                                 | 66.1 ms: 1.93x faster                                            |
| raytrace                 | 507 ms                                                 | 265 ms: 1.92x faster                                             |
| nbody                    | 154 ms                                                 | 82.3 ms: 1.87x faster                                            |
| deepcopy                 | 479 us                                                 | 260 us: 1.84x faster                                             |
| scimark_sor              | 220 ms                                                 | 121 ms: 1.82x faster                                             |
| asyncio_tcp              | 922 ms                                                 | 512 ms: 1.80x faster                                             |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 566 ms: 1.79x faster                                             |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                            |
| unpickle_pure_python     | 331 us                                                 | 194 us: 1.71x faster                                             |
| mako                     | 16.3 ms                                                | 9.74 ms: 1.68x faster                                            |
| float                    | 117 ms                                                 | 70.7 ms: 1.66x faster                                            |
| spectral_norm            | 170 ms                                                 | 103 ms: 1.65x faster                                             |
| go                       | 240 ms                                                 | 146 ms: 1.65x faster                                             |
| pyflate                  | 716 ms                                                 | 442 ms: 1.62x faster                                             |
| scimark_lu               | 176 ms                                                 | 110 ms: 1.60x faster                                             |
| pickle_pure_python       | 484 us                                                 | 304 us: 1.60x faster                                             |
| deepcopy_reduce          | 4.17 us                                                | 2.69 us: 1.55x faster                                            |
| hexiom                   | 10.4 ms                                                | 6.80 ms: 1.53x faster                                            |
| coroutines               | 35.1 ms                                                | 23.1 ms: 1.52x faster                                            |
| scimark_fft              | 466 ms                                                 | 307 ms: 1.52x faster                                             |
| tomli_loads              | 3.14 sec                                               | 2.09 sec: 1.51x faster                                           |
| sqlglot_parse            | 2.17 ms                                                | 1.44 ms: 1.50x faster                                            |
| sqlglot_transpile        | 2.57 ms                                                | 1.72 ms: 1.50x faster                                            |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.32 ms: 1.50x faster                                            |
| logging_simple           | 8.30 us                                                | 5.68 us: 1.46x faster                                            |
| fannkuch                 | 532 ms                                                 | 367 ms: 1.45x faster                                             |
| logging_format           | 9.09 us                                                | 6.31 us: 1.44x faster                                            |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.82 sec: 1.42x faster                                           |
| tornado_http             | 136 ms                                                 | 96.9 ms: 1.41x faster                                            |
| xml_etree_process        | 79.1 ms                                                | 56.3 ms: 1.40x faster                                            |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.38x faster                                            |
| pprint_safe_repr         | 1.02 sec                                               | 746 ms: 1.36x faster                                             |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.36x faster                                            |
| pylint                   | 551 ms                                                 | 408 ms: 1.35x faster                                             |
| pprint_pformat           | 2.10 sec                                               | 1.56 sec: 1.35x faster                                           |
| thrift                   | 1.07 ms                                                | 797 us: 1.35x faster                                             |
| genshi_text              | 31.8 ms                                                | 23.8 ms: 1.34x faster                                            |
| django_template          | 48.2 ms                                                | 36.8 ms: 1.31x faster                                            |
| html5lib                 | 88.9 ms                                                | 68.6 ms: 1.30x faster                                            |
| regex_compile            | 188 ms                                                 | 146 ms: 1.29x faster                                             |
| nqueens                  | 106 ms                                                 | 83.1 ms: 1.27x faster                                            |
| pycparser                | 1.58 sec                                               | 1.24 sec: 1.27x faster                                           |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                            |
| 2to3                     | 348 ms                                                 | 280 ms: 1.24x faster                                             |
| xml_etree_generate       | 99.4 ms                                                | 80.7 ms: 1.23x faster                                            |
| sqlglot_normalize        | 143 ms                                                 | 117 ms: 1.22x faster                                             |
| bench_thread_pool        | 986 us                                                 | 821 us: 1.20x faster                                             |
| xml_etree_iterparse      | 115 ms                                                 | 98.7 ms: 1.17x faster                                            |
| sqlglot_optimize         | 69.2 ms                                                | 59.9 ms: 1.16x faster                                            |
| xml_etree_parse          | 168 ms                                                 | 148 ms: 1.14x faster                                             |
| regex_v8                 | 27.8 ms                                                | 24.6 ms: 1.13x faster                                            |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                             |
| json                     | 5.69 ms                                                | 5.10 ms: 1.11x faster                                            |
| json_loads               | 31.2 us                                                | 28.0 us: 1.11x faster                                            |
| sympy_str                | 346 ms                                                 | 318 ms: 1.09x faster                                             |
| regex_dna                | 227 ms                                                 | 210 ms: 1.08x faster                                             |
| sympy_expand             | 566 ms                                                 | 531 ms: 1.06x faster                                             |
| sympy_integrate          | 25.8 ms                                                | 24.4 ms: 1.06x faster                                            |
| sympy_sum                | 196 ms                                                 | 187 ms: 1.05x faster                                             |
| genshi_xml               | 66.0 ms                                                | 63.5 ms: 1.04x faster                                            |
| mdp                      | 2.85 sec                                               | 2.74 sec: 1.04x faster                                           |
| pidigits                 | 191 ms                                                 | 188 ms: 1.01x faster                                             |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                             |
| async_generators         | 444 ms                                                 | 452 ms: 1.02x slower                                             |
| gc_traversal             | 3.62 ms                                                | 3.76 ms: 1.04x slower                                            |
| telco                    | 7.27 ms                                                | 7.68 ms: 1.06x slower                                            |
| create_gc_cycles         | 1.62 ms                                                | 1.78 ms: 1.10x slower                                            |
| coverage                 | 79.4 ms                                                | 90.9 ms: 1.14x slower                                            |
| python_startup_no_site   | 5.93 ms                                                | 7.17 ms: 1.21x slower                                            |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                     |

Benchmark hidden because not significant (3): docutils, bench_mp_pool, regex_effbot
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240812-3.14.0a0-8c45870-JIT/bm-20240812-linux-x86_64-brandtbucher-underflow-3.14.0a0-8c45870.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.21x