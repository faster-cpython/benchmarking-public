# Results vs. 3.10.4

- fork: savannahostrowski
- ref: jit_mem_10000
- machine: linux-x86_64
- commit hash: 398f45a
- commit date: 2024-08-13
- overall geometric mean: 1.41x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_10000-3.14.0a0-398f45a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 301 ms: 1.16x faster                                                      |
| docutils       | 3.30 sec                                               | 2.82 sec: 1.17x faster                                                    |
| html5lib       | 88.9 ms                                                | 70.0 ms: 1.27x faster                                                     |
| tornado_http   | 136 ms                                                 | 95.6 ms: 1.43x faster                                                     |
| Geometric mean | (ref)                                                  | 1.25x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_10000-3.14.0a0-398f45a |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 325 ms: 2.24x faster                                                      |
| async_tree_memoization  | 870 ms                                                 | 414 ms: 2.10x faster                                                      |
| async_tree_io           | 1.77 sec                                               | 892 ms: 1.98x faster                                                      |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 567 ms: 1.79x faster                                                      |
| Geometric mean          | (ref)                                                  | 2.02x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_10000-3.14.0a0-398f45a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.9 ms: 1.90x faster                                                     |
| float          | 117 ms                                                 | 74.6 ms: 1.57x faster                                                     |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.45x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_10000-3.14.0a0-398f45a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 141 ms: 1.34x faster                                                      |
| regex_v8       | 27.8 ms                                                | 24.5 ms: 1.13x faster                                                     |
| regex_dna      | 227 ms                                                 | 219 ms: 1.03x faster                                                      |
| regex_effbot   | 3.63 ms                                                | 3.76 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                  | 1.11x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_10000-3.14.0a0-398f45a |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.93 sec: 1.62x faster                                                    |
| pickle_pure_python   | 484 us                                                 | 305 us: 1.59x faster                                                      |
| unpickle_pure_python | 331 us                                                 | 215 us: 1.54x faster                                                      |
| json_dumps           | 14.2 ms                                                | 10.3 ms: 1.38x faster                                                     |
| xml_etree_process    | 79.1 ms                                                | 59.5 ms: 1.33x faster                                                     |
| xml_etree_generate   | 99.4 ms                                                | 86.1 ms: 1.15x faster                                                     |
| xml_etree_iterparse  | 115 ms                                                 | 105 ms: 1.10x faster                                                      |
| xml_etree_parse      | 168 ms                                                 | 154 ms: 1.09x faster                                                      |
| json_loads           | 31.2 us                                                | 28.8 us: 1.08x faster                                                     |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_10000-3.14.0a0-398f45a |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                     |
| python_startup_no_site | 5.93 ms                                                | 7.14 ms: 1.20x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_10000-3.14.0a0-398f45a |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.73 ms: 1.68x faster                                                     |
| django_template | 48.2 ms                                                | 35.6 ms: 1.35x faster                                                     |
| genshi_text     | 31.8 ms                                                | 25.8 ms: 1.23x faster                                                     |
| genshi_xml      | 66.0 ms                                                | 61.2 ms: 1.08x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.32x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_10000-3.14.0a0-398f45a |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 172 us: 3.17x faster                                                      |
| deltablue                | 7.91 ms                                                | 3.37 ms: 2.35x faster                                                     |
| generators               | 80.1 ms                                                | 35.2 ms: 2.28x faster                                                     |
| async_tree_none          | 728 ms                                                 | 325 ms: 2.24x faster                                                      |
| deepcopy_memo            | 58.5 us                                                | 26.7 us: 2.19x faster                                                     |
| async_tree_memoization   | 870 ms                                                 | 414 ms: 2.10x faster                                                      |
| richards_super           | 94.7 ms                                                | 46.3 ms: 2.05x faster                                                     |
| chaos                    | 115 ms                                                 | 58.0 ms: 1.99x faster                                                     |
| async_tree_io            | 1.77 sec                                               | 892 ms: 1.98x faster                                                      |
| richards                 | 79.3 ms                                                | 41.1 ms: 1.93x faster                                                     |
| crypto_pyaes             | 128 ms                                                 | 66.6 ms: 1.92x faster                                                     |
| scimark_monte_carlo      | 118 ms                                                 | 62.3 ms: 1.90x faster                                                     |
| nbody                    | 154 ms                                                 | 80.9 ms: 1.90x faster                                                     |
| scimark_sor              | 220 ms                                                 | 117 ms: 1.88x faster                                                      |
| raytrace                 | 507 ms                                                 | 271 ms: 1.87x faster                                                      |
| logging_silent           | 190 ns                                                 | 103 ns: 1.85x faster                                                      |
| deepcopy                 | 479 us                                                 | 261 us: 1.84x faster                                                      |
| asyncio_tcp              | 922 ms                                                 | 504 ms: 1.83x faster                                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 567 ms: 1.79x faster                                                      |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.74x faster                                                     |
| spectral_norm            | 170 ms                                                 | 101 ms: 1.69x faster                                                      |
| mako                     | 16.3 ms                                                | 9.73 ms: 1.68x faster                                                     |
| pyflate                  | 716 ms                                                 | 433 ms: 1.65x faster                                                      |
| go                       | 240 ms                                                 | 147 ms: 1.64x faster                                                      |
| tomli_loads              | 3.14 sec                                               | 1.93 sec: 1.62x faster                                                    |
| scimark_lu               | 176 ms                                                 | 110 ms: 1.61x faster                                                      |
| pickle_pure_python       | 484 us                                                 | 305 us: 1.59x faster                                                      |
| deepcopy_reduce          | 4.17 us                                                | 2.65 us: 1.57x faster                                                     |
| float                    | 117 ms                                                 | 74.6 ms: 1.57x faster                                                     |
| sqlglot_parse            | 2.17 ms                                                | 1.40 ms: 1.55x faster                                                     |
| unpickle_pure_python     | 331 us                                                 | 215 us: 1.54x faster                                                      |
| coroutines               | 35.1 ms                                                | 22.9 ms: 1.53x faster                                                     |
| hexiom                   | 10.4 ms                                                | 6.83 ms: 1.52x faster                                                     |
| pylint                   | 551 ms                                                 | 365 ms: 1.51x faster                                                      |
| scimark_fft              | 466 ms                                                 | 311 ms: 1.50x faster                                                      |
| logging_simple           | 8.30 us                                                | 5.56 us: 1.49x faster                                                     |
| logging_format           | 9.09 us                                                | 6.14 us: 1.48x faster                                                     |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.49 ms: 1.44x faster                                                     |
| fannkuch                 | 532 ms                                                 | 369 ms: 1.44x faster                                                      |
| sqlglot_transpile        | 2.57 ms                                                | 1.80 ms: 1.43x faster                                                     |
| tornado_http             | 136 ms                                                 | 95.6 ms: 1.43x faster                                                     |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                                    |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                     |
| json_dumps               | 14.2 ms                                                | 10.3 ms: 1.38x faster                                                     |
| thrift                   | 1.07 ms                                                | 779 us: 1.38x faster                                                      |
| pprint_pformat           | 2.10 sec                                               | 1.54 sec: 1.36x faster                                                    |
| django_template          | 48.2 ms                                                | 35.6 ms: 1.35x faster                                                     |
| pprint_safe_repr         | 1.02 sec                                               | 753 ms: 1.35x faster                                                      |
| regex_compile            | 188 ms                                                 | 141 ms: 1.34x faster                                                      |
| xml_etree_process        | 79.1 ms                                                | 59.5 ms: 1.33x faster                                                     |
| pycparser                | 1.58 sec                                               | 1.19 sec: 1.33x faster                                                    |
| html5lib                 | 88.9 ms                                                | 70.0 ms: 1.27x faster                                                     |
| pathlib                  | 20.5 ms                                                | 16.2 ms: 1.26x faster                                                     |
| sqlglot_normalize        | 143 ms                                                 | 114 ms: 1.25x faster                                                      |
| genshi_text              | 31.8 ms                                                | 25.8 ms: 1.23x faster                                                     |
| nqueens                  | 106 ms                                                 | 85.9 ms: 1.23x faster                                                     |
| bench_thread_pool        | 986 us                                                 | 823 us: 1.20x faster                                                      |
| docutils                 | 3.30 sec                                               | 2.82 sec: 1.17x faster                                                    |
| sympy_str                | 346 ms                                                 | 297 ms: 1.16x faster                                                      |
| 2to3                     | 348 ms                                                 | 301 ms: 1.16x faster                                                      |
| xml_etree_generate       | 99.4 ms                                                | 86.1 ms: 1.15x faster                                                     |
| sympy_sum                | 196 ms                                                 | 171 ms: 1.15x faster                                                      |
| regex_v8                 | 27.8 ms                                                | 24.5 ms: 1.13x faster                                                     |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                      |
| sqlglot_optimize         | 69.2 ms                                                | 61.0 ms: 1.13x faster                                                     |
| sympy_integrate          | 25.8 ms                                                | 22.9 ms: 1.13x faster                                                     |
| sympy_expand             | 566 ms                                                 | 504 ms: 1.12x faster                                                      |
| xml_etree_iterparse      | 115 ms                                                 | 105 ms: 1.10x faster                                                      |
| xml_etree_parse          | 168 ms                                                 | 154 ms: 1.09x faster                                                      |
| json_loads               | 31.2 us                                                | 28.8 us: 1.08x faster                                                     |
| genshi_xml               | 66.0 ms                                                | 61.2 ms: 1.08x faster                                                     |
| json                     | 5.69 ms                                                | 5.31 ms: 1.07x faster                                                     |
| regex_dna                | 227 ms                                                 | 219 ms: 1.03x faster                                                      |
| mdp                      | 2.85 sec                                               | 2.77 sec: 1.03x faster                                                    |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                                      |
| async_generators         | 444 ms                                                 | 454 ms: 1.02x slower                                                      |
| regex_effbot             | 3.63 ms                                                | 3.76 ms: 1.03x slower                                                     |
| gc_traversal             | 3.62 ms                                                | 3.75 ms: 1.04x slower                                                     |
| telco                    | 7.27 ms                                                | 7.81 ms: 1.07x slower                                                     |
| create_gc_cycles         | 1.62 ms                                                | 1.74 ms: 1.08x slower                                                     |
| coverage                 | 79.4 ms                                                | 85.8 ms: 1.08x slower                                                     |
| python_startup_no_site   | 5.93 ms                                                | 7.14 ms: 1.20x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                              |

Benchmark hidden because not significant (2): bench_mp_pool, asyncio_websockets
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240813-3.14.0a0-398f45a-JIT/bm-20240813-linux-x86_64-savannahostrowski-jit_mem_10000-3.14.0a0-398f45a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.17x