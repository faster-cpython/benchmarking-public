# Results vs. 3.10.4

- fork: nick-arm
- ref: codecache_rwx
- machine: linux-aarch64
- commit hash: 0442576
- commit date: 2024-10-07
- overall geometric mean: 1.12x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 365 ms: 1.04x faster                                                 |
| docutils       | 3.53 sec                                                              | 3.56 sec: 1.01x slower                                               |
| html5lib       | 86.5 ms                                                               | 70.6 ms: 1.22x faster                                                |
| tornado_http   | 178 ms                                                                | 149 ms: 1.20x faster                                                 |
| Geometric mean | (ref)                                                                 | 1.11x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|-------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 442 ms: 2.15x faster                                                 |
| async_tree_io           | 2.28 sec                                                              | 1.15 sec: 2.00x faster                                               |
| async_tree_memoization  | 1.13 sec                                                              | 585 ms: 1.94x faster                                                 |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 754 ms: 1.69x faster                                                 |
| Geometric mean          | (ref)                                                                 | 1.93x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 111 ms: 1.50x faster                                                 |
| float          | 135 ms                                                                | 90.2 ms: 1.49x faster                                                |
| Geometric mean | (ref)                                                                 | 1.31x faster                                                         |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 31.3 ms: 1.03x faster                                                |
| regex_compile  | 177 ms                                                                | 174 ms: 1.02x faster                                                 |
| regex_dna      | 257 ms                                                                | 263 ms: 1.02x slower                                                 |
| regex_effbot   | 4.25 ms                                                               | 5.00 ms: 1.18x slower                                                |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 265 us: 1.38x faster                                                 |
| pickle_pure_python   | 529 us                                                                | 395 us: 1.34x faster                                                 |
| tomli_loads          | 3.36 sec                                                              | 2.64 sec: 1.27x faster                                               |
| json_dumps           | 16.7 ms                                                               | 13.1 ms: 1.27x faster                                                |
| xml_etree_process    | 99.5 ms                                                               | 79.4 ms: 1.25x faster                                                |
| xml_etree_generate   | 123 ms                                                                | 109 ms: 1.12x faster                                                 |
| xml_etree_parse      | 212 ms                                                                | 190 ms: 1.11x faster                                                 |
| unpickle_list        | 6.99 us                                                               | 6.37 us: 1.10x faster                                                |
| xml_etree_iterparse  | 156 ms                                                                | 151 ms: 1.03x faster                                                 |
| pickle_list          | 5.24 us                                                               | 5.19 us: 1.01x faster                                                |
| pickle_dict          | 35.1 us                                                               | 37.8 us: 1.08x slower                                                |
| unpickle             | 17.5 us                                                               | 19.1 us: 1.10x slower                                                |
| pickle               | 12.5 us                                                               | 13.8 us: 1.10x slower                                                |
| Geometric mean       | (ref)                                                                 | 1.11x faster                                                         |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.1 ms: 1.17x slower                                                |
| python_startup_no_site | 6.89 ms                                                               | 8.75 ms: 1.27x slower                                                |
| Geometric mean         | (ref)                                                                 | 1.22x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.2 ms: 1.44x faster                                                |
| genshi_text     | 35.2 ms                                                               | 33.1 ms: 1.06x faster                                                |
| django_template | 53.3 ms                                                               | 51.2 ms: 1.04x faster                                                |
| genshi_xml      | 69.8 ms                                                               | 78.1 ms: 1.12x slower                                                |
| Geometric mean  | (ref)                                                                 | 1.09x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|--------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 205 us: 3.22x faster                                                 |
| async_tree_none          | 950 ms                                                                | 442 ms: 2.15x faster                                                 |
| deltablue                | 8.94 ms                                                               | 4.34 ms: 2.06x faster                                                |
| async_tree_io            | 2.28 sec                                                              | 1.15 sec: 2.00x faster                                               |
| async_tree_memoization   | 1.13 sec                                                              | 585 ms: 1.94x faster                                                 |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 754 ms: 1.69x faster                                                 |
| logging_silent           | 222 ns                                                                | 132 ns: 1.68x faster                                                 |
| raytrace                 | 573 ms                                                                | 345 ms: 1.66x faster                                                 |
| deepcopy_memo            | 61.7 us                                                               | 37.4 us: 1.65x faster                                                |
| scimark_sor              | 246 ms                                                                | 151 ms: 1.63x faster                                                 |
| richards                 | 91.7 ms                                                               | 56.9 ms: 1.61x faster                                                |
| richards_super           | 107 ms                                                                | 67.3 ms: 1.59x faster                                                |
| asyncio_tcp              | 944 ms                                                                | 622 ms: 1.52x faster                                                 |
| crypto_pyaes             | 134 ms                                                                | 88.6 ms: 1.51x faster                                                |
| scimark_lu               | 227 ms                                                                | 151 ms: 1.50x faster                                                 |
| nbody                    | 166 ms                                                                | 111 ms: 1.50x faster                                                 |
| float                    | 135 ms                                                                | 90.2 ms: 1.49x faster                                                |
| go                       | 264 ms                                                                | 182 ms: 1.45x faster                                                 |
| scimark_monte_carlo      | 128 ms                                                                | 88.2 ms: 1.45x faster                                                |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.28 sec: 1.44x faster                                               |
| mako                     | 18.9 ms                                                               | 13.2 ms: 1.44x faster                                                |
| sqlglot_parse            | 2.40 ms                                                               | 1.68 ms: 1.43x faster                                                |
| chaos                    | 121 ms                                                                | 86.4 ms: 1.40x faster                                                |
| unpickle_pure_python     | 366 us                                                                | 265 us: 1.38x faster                                                 |
| comprehensions           | 33.1 us                                                               | 24.6 us: 1.35x faster                                                |
| pickle_pure_python       | 529 us                                                                | 395 us: 1.34x faster                                                 |
| thrift                   | 1.26 ms                                                               | 959 us: 1.31x faster                                                 |
| logging_format           | 10.6 us                                                               | 8.10 us: 1.31x faster                                                |
| logging_simple           | 9.78 us                                                               | 7.49 us: 1.31x faster                                                |
| coroutines               | 37.2 ms                                                               | 28.6 ms: 1.30x faster                                                |
| sqlglot_transpile        | 2.84 ms                                                               | 2.21 ms: 1.29x faster                                                |
| pyflate                  | 795 ms                                                                | 620 ms: 1.28x faster                                                 |
| tomli_loads              | 3.36 sec                                                              | 2.64 sec: 1.27x faster                                               |
| json_dumps               | 16.7 ms                                                               | 13.1 ms: 1.27x faster                                                |
| deepcopy                 | 511 us                                                                | 402 us: 1.27x faster                                                 |
| spectral_norm            | 186 ms                                                                | 147 ms: 1.27x faster                                                 |
| xml_etree_process        | 99.5 ms                                                               | 79.4 ms: 1.25x faster                                                |
| html5lib                 | 86.5 ms                                                               | 70.6 ms: 1.22x faster                                                |
| pathlib                  | 26.3 ms                                                               | 21.9 ms: 1.20x faster                                                |
| tornado_http             | 178 ms                                                                | 149 ms: 1.20x faster                                                 |
| deepcopy_reduce          | 4.60 us                                                               | 3.94 us: 1.17x faster                                                |
| bench_thread_pool        | 1.59 ms                                                               | 1.37 ms: 1.16x faster                                                |
| generators               | 68.1 ms                                                               | 58.8 ms: 1.16x faster                                                |
| pycparser                | 1.69 sec                                                              | 1.47 sec: 1.15x faster                                               |
| xml_etree_generate       | 123 ms                                                                | 109 ms: 1.12x faster                                                 |
| scimark_fft              | 500 ms                                                                | 446 ms: 1.12x faster                                                 |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.83 ms: 1.12x faster                                                |
| xml_etree_parse          | 212 ms                                                                | 190 ms: 1.11x faster                                                 |
| hexiom                   | 10.9 ms                                                               | 9.90 ms: 1.10x faster                                                |
| unpickle_list            | 6.99 us                                                               | 6.37 us: 1.10x faster                                                |
| fannkuch                 | 546 ms                                                                | 504 ms: 1.08x faster                                                 |
| mdp                      | 3.70 sec                                                              | 3.45 sec: 1.07x faster                                               |
| sqlite_synth             | 4.12 us                                                               | 3.87 us: 1.06x faster                                                |
| genshi_text              | 35.2 ms                                                               | 33.1 ms: 1.06x faster                                                |
| json                     | 5.88 ms                                                               | 5.54 ms: 1.06x faster                                                |
| sqlglot_normalize        | 156 ms                                                                | 149 ms: 1.05x faster                                                 |
| 2to3                     | 381 ms                                                                | 365 ms: 1.04x faster                                                 |
| django_template          | 53.3 ms                                                               | 51.2 ms: 1.04x faster                                                |
| xml_etree_iterparse      | 156 ms                                                                | 151 ms: 1.03x faster                                                 |
| regex_v8                 | 32.2 ms                                                               | 31.3 ms: 1.03x faster                                                |
| meteor_contest           | 126 ms                                                                | 123 ms: 1.03x faster                                                 |
| regex_compile            | 177 ms                                                                | 174 ms: 1.02x faster                                                 |
| pickle_list              | 5.24 us                                                               | 5.19 us: 1.01x faster                                                |
| docutils                 | 3.53 sec                                                              | 3.56 sec: 1.01x slower                                               |
| sqlglot_optimize         | 75.4 ms                                                               | 76.1 ms: 1.01x slower                                                |
| asyncio_websockets       | 657 ms                                                                | 665 ms: 1.01x slower                                                 |
| regex_dna                | 257 ms                                                                | 263 ms: 1.02x slower                                                 |
| nqueens                  | 117 ms                                                                | 123 ms: 1.04x slower                                                 |
| sympy_str                | 329 ms                                                                | 346 ms: 1.05x slower                                                 |
| sympy_expand             | 543 ms                                                                | 573 ms: 1.06x slower                                                 |
| pprint_safe_repr         | 1.15 sec                                                              | 1.22 sec: 1.07x slower                                               |
| sympy_integrate          | 26.5 ms                                                               | 28.5 ms: 1.07x slower                                                |
| pickle_dict              | 35.1 us                                                               | 37.8 us: 1.08x slower                                                |
| pprint_pformat           | 2.36 sec                                                              | 2.54 sec: 1.08x slower                                               |
| unpickle                 | 17.5 us                                                               | 19.1 us: 1.10x slower                                                |
| pickle                   | 12.5 us                                                               | 13.8 us: 1.10x slower                                                |
| telco                    | 8.49 ms                                                               | 9.37 ms: 1.10x slower                                                |
| dulwich_log              | 73.5 ms                                                               | 81.3 ms: 1.11x slower                                                |
| genshi_xml               | 69.8 ms                                                               | 78.1 ms: 1.12x slower                                                |
| sympy_sum                | 184 ms                                                                | 210 ms: 1.14x slower                                                 |
| async_generators         | 452 ms                                                                | 517 ms: 1.14x slower                                                 |
| python_startup           | 11.2 ms                                                               | 13.1 ms: 1.17x slower                                                |
| coverage                 | 83.6 ms                                                               | 98.2 ms: 1.17x slower                                                |
| regex_effbot             | 4.25 ms                                                               | 5.00 ms: 1.18x slower                                                |
| gc_traversal             | 4.15 ms                                                               | 5.21 ms: 1.26x slower                                                |
| python_startup_no_site   | 6.89 ms                                                               | 8.75 ms: 1.27x slower                                                |
| bench_mp_pool            | 14.5 ms                                                               | 2.94 sec: 202.55x slower                                             |
| Geometric mean           | (ref)                                                                 | 1.12x faster                                                         |

Benchmark hidden because not significant (4): pylint, pidigits, json_loads, create_gc_cycles
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241007-3.14.0a0-0442576-JIT/bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.22x