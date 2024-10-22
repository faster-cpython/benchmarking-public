# Results vs. 3.10.4

- fork: brandtbucher
- ref: cache_dynamic_exits
- machine: linux-x86_64
- commit hash: 55bff1c
- commit date: 2024-08-28
- overall geometric mean: 1.43x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-linux-x86_64-brandtbucher-cache_dynamic_exits-3.14.0a0-55bff1c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 274 ms: 1.27x faster                                                       |
| docutils       | 3.30 sec                                               | 3.05 sec: 1.08x faster                                                     |
| html5lib       | 88.9 ms                                                | 66.8 ms: 1.33x faster                                                      |
| tornado_http   | 136 ms                                                 | 94.3 ms: 1.45x faster                                                      |
| Geometric mean | (ref)                                                  | 1.28x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-linux-x86_64-brandtbucher-cache_dynamic_exits-3.14.0a0-55bff1c |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 322 ms: 2.26x faster                                                       |
| async_tree_memoization  | 870 ms                                                 | 398 ms: 2.19x faster                                                       |
| async_tree_io           | 1.77 sec                                               | 933 ms: 1.90x faster                                                       |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 561 ms: 1.81x faster                                                       |
| Geometric mean          | (ref)                                                  | 2.03x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-linux-x86_64-brandtbucher-cache_dynamic_exits-3.14.0a0-55bff1c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 79.7 ms: 1.93x faster                                                      |
| float          | 117 ms                                                 | 70.5 ms: 1.66x faster                                                      |
| pidigits       | 191 ms                                                 | 185 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                  | 1.49x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-linux-x86_64-brandtbucher-cache_dynamic_exits-3.14.0a0-55bff1c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 143 ms: 1.32x faster                                                       |
| regex_v8       | 27.8 ms                                                | 24.4 ms: 1.14x faster                                                      |
| regex_dna      | 227 ms                                                 | 217 ms: 1.04x faster                                                       |
| regex_effbot   | 3.63 ms                                                | 3.56 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.12x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-linux-x86_64-brandtbucher-cache_dynamic_exits-3.14.0a0-55bff1c |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.94 sec: 1.62x faster                                                     |
| pickle_pure_python   | 484 us                                                 | 305 us: 1.59x faster                                                       |
| unpickle_pure_python | 331 us                                                 | 215 us: 1.54x faster                                                       |
| xml_etree_process    | 79.1 ms                                                | 54.2 ms: 1.46x faster                                                      |
| json_dumps           | 14.2 ms                                                | 9.99 ms: 1.42x faster                                                      |
| xml_etree_generate   | 99.4 ms                                                | 76.6 ms: 1.30x faster                                                      |
| xml_etree_iterparse  | 115 ms                                                 | 98.3 ms: 1.17x faster                                                      |
| xml_etree_parse      | 168 ms                                                 | 146 ms: 1.15x faster                                                       |
| json_loads           | 31.2 us                                                | 28.6 us: 1.09x faster                                                      |
| Geometric mean       | (ref)                                                  | 1.36x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-linux-x86_64-brandtbucher-cache_dynamic_exits-3.14.0a0-55bff1c |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                      |
| python_startup_no_site | 5.93 ms                                                | 7.14 ms: 1.20x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-linux-x86_64-brandtbucher-cache_dynamic_exits-3.14.0a0-55bff1c |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.87 ms: 1.65x faster                                                      |
| genshi_text     | 31.8 ms                                                | 23.8 ms: 1.34x faster                                                      |
| django_template | 48.2 ms                                                | 37.7 ms: 1.28x faster                                                      |
| genshi_xml      | 66.0 ms                                                | 56.4 ms: 1.17x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-linux-x86_64-brandtbucher-cache_dynamic_exits-3.14.0a0-55bff1c |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 164 us: 3.32x faster                                                       |
| deltablue                | 7.91 ms                                                | 3.20 ms: 2.47x faster                                                      |
| generators               | 80.1 ms                                                | 33.9 ms: 2.37x faster                                                      |
| async_tree_none          | 728 ms                                                 | 322 ms: 2.26x faster                                                       |
| async_tree_memoization   | 870 ms                                                 | 398 ms: 2.19x faster                                                       |
| deepcopy_memo            | 58.5 us                                                | 27.1 us: 2.16x faster                                                      |
| richards_super           | 94.7 ms                                                | 45.4 ms: 2.09x faster                                                      |
| richards                 | 79.3 ms                                                | 39.6 ms: 2.00x faster                                                      |
| chaos                    | 115 ms                                                 | 58.4 ms: 1.98x faster                                                      |
| crypto_pyaes             | 128 ms                                                 | 65.9 ms: 1.94x faster                                                      |
| nbody                    | 154 ms                                                 | 79.7 ms: 1.93x faster                                                      |
| async_tree_io            | 1.77 sec                                               | 933 ms: 1.90x faster                                                       |
| scimark_monte_carlo      | 118 ms                                                 | 62.6 ms: 1.89x faster                                                      |
| asyncio_tcp              | 922 ms                                                 | 491 ms: 1.88x faster                                                       |
| logging_silent           | 190 ns                                                 | 103 ns: 1.84x faster                                                       |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 561 ms: 1.81x faster                                                       |
| raytrace                 | 507 ms                                                 | 281 ms: 1.81x faster                                                       |
| deepcopy                 | 479 us                                                 | 269 us: 1.78x faster                                                       |
| scimark_sor              | 220 ms                                                 | 127 ms: 1.73x faster                                                       |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                                      |
| spectral_norm            | 170 ms                                                 | 101 ms: 1.68x faster                                                       |
| float                    | 117 ms                                                 | 70.5 ms: 1.66x faster                                                      |
| mako                     | 16.3 ms                                                | 9.87 ms: 1.65x faster                                                      |
| tomli_loads              | 3.14 sec                                               | 1.94 sec: 1.62x faster                                                     |
| pyflate                  | 716 ms                                                 | 445 ms: 1.61x faster                                                       |
| sqlglot_parse            | 2.17 ms                                                | 1.35 ms: 1.60x faster                                                      |
| pickle_pure_python       | 484 us                                                 | 305 us: 1.59x faster                                                       |
| coroutines               | 35.1 ms                                                | 22.5 ms: 1.56x faster                                                      |
| deepcopy_reduce          | 4.17 us                                                | 2.69 us: 1.55x faster                                                      |
| scimark_lu               | 176 ms                                                 | 114 ms: 1.55x faster                                                       |
| unpickle_pure_python     | 331 us                                                 | 215 us: 1.54x faster                                                       |
| logging_simple           | 8.30 us                                                | 5.49 us: 1.51x faster                                                      |
| pylint                   | 551 ms                                                 | 367 ms: 1.50x faster                                                       |
| sqlglot_transpile        | 2.57 ms                                                | 1.71 ms: 1.50x faster                                                      |
| logging_format           | 9.09 us                                                | 6.06 us: 1.50x faster                                                      |
| hexiom                   | 10.4 ms                                                | 6.95 ms: 1.50x faster                                                      |
| scimark_fft              | 466 ms                                                 | 311 ms: 1.50x faster                                                       |
| xml_etree_process        | 79.1 ms                                                | 54.2 ms: 1.46x faster                                                      |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.44 ms: 1.46x faster                                                      |
| tornado_http             | 136 ms                                                 | 94.3 ms: 1.45x faster                                                      |
| fannkuch                 | 532 ms                                                 | 370 ms: 1.44x faster                                                       |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                                     |
| json_dumps               | 14.2 ms                                                | 9.99 ms: 1.42x faster                                                      |
| go                       | 240 ms                                                 | 171 ms: 1.40x faster                                                       |
| pprint_pformat           | 2.10 sec                                               | 1.50 sec: 1.40x faster                                                     |
| pprint_safe_repr         | 1.02 sec                                               | 726 ms: 1.40x faster                                                       |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                      |
| thrift                   | 1.07 ms                                                | 788 us: 1.36x faster                                                       |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.34x faster                                                     |
| genshi_text              | 31.8 ms                                                | 23.8 ms: 1.34x faster                                                      |
| html5lib                 | 88.9 ms                                                | 66.8 ms: 1.33x faster                                                      |
| regex_compile            | 188 ms                                                 | 143 ms: 1.32x faster                                                       |
| xml_etree_generate       | 99.4 ms                                                | 76.6 ms: 1.30x faster                                                      |
| pathlib                  | 20.5 ms                                                | 15.8 ms: 1.29x faster                                                      |
| django_template          | 48.2 ms                                                | 37.7 ms: 1.28x faster                                                      |
| 2to3                     | 348 ms                                                 | 274 ms: 1.27x faster                                                       |
| nqueens                  | 106 ms                                                 | 83.8 ms: 1.26x faster                                                      |
| sqlglot_normalize        | 143 ms                                                 | 113 ms: 1.26x faster                                                       |
| bench_thread_pool        | 986 us                                                 | 820 us: 1.20x faster                                                       |
| sqlglot_optimize         | 69.2 ms                                                | 58.0 ms: 1.19x faster                                                      |
| xml_etree_iterparse      | 115 ms                                                 | 98.3 ms: 1.17x faster                                                      |
| genshi_xml               | 66.0 ms                                                | 56.4 ms: 1.17x faster                                                      |
| sympy_sum                | 196 ms                                                 | 169 ms: 1.17x faster                                                       |
| sympy_str                | 346 ms                                                 | 299 ms: 1.16x faster                                                       |
| sympy_integrate          | 25.8 ms                                                | 22.3 ms: 1.15x faster                                                      |
| xml_etree_parse          | 168 ms                                                 | 146 ms: 1.15x faster                                                       |
| regex_v8                 | 27.8 ms                                                | 24.4 ms: 1.14x faster                                                      |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                       |
| mdp                      | 2.85 sec                                               | 2.54 sec: 1.12x faster                                                     |
| sympy_expand             | 566 ms                                                 | 514 ms: 1.10x faster                                                       |
| json_loads               | 31.2 us                                                | 28.6 us: 1.09x faster                                                      |
| docutils                 | 3.30 sec                                               | 3.05 sec: 1.08x faster                                                     |
| json                     | 5.69 ms                                                | 5.30 ms: 1.07x faster                                                      |
| regex_dna                | 227 ms                                                 | 217 ms: 1.04x faster                                                       |
| pidigits                 | 191 ms                                                 | 185 ms: 1.03x faster                                                       |
| regex_effbot             | 3.63 ms                                                | 3.56 ms: 1.02x faster                                                      |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                                       |
| gc_traversal             | 3.62 ms                                                | 3.75 ms: 1.03x slower                                                      |
| async_generators         | 444 ms                                                 | 461 ms: 1.04x slower                                                       |
| telco                    | 7.27 ms                                                | 7.75 ms: 1.07x slower                                                      |
| coverage                 | 79.4 ms                                                | 86.2 ms: 1.08x slower                                                      |
| create_gc_cycles         | 1.62 ms                                                | 1.78 ms: 1.10x slower                                                      |
| python_startup_no_site   | 5.93 ms                                                | 7.14 ms: 1.20x slower                                                      |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                               |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240828-3.14.0a0-55bff1c-JIT/bm-20240828-linux-x86_64-brandtbucher-cache_dynamic_exits-3.14.0a0-55bff1c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.22x