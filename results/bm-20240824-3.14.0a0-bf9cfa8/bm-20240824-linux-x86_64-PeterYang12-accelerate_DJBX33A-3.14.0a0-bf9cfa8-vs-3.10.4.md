# Results vs. 3.10.4

- fork: PeterYang12
- ref: accelerate_DJBX33A
- machine: linux-x86_64
- commit hash: bf9cfa8
- commit date: 2024-08-24
- overall geometric mean: 1.44x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240824-linux-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 254 ms: 1.37x faster                                                     |
| docutils       | 3.30 sec                                               | 2.69 sec: 1.23x faster                                                   |
| html5lib       | 88.9 ms                                                | 64.9 ms: 1.37x faster                                                    |
| tornado_http   | 136 ms                                                 | 90.2 ms: 1.51x faster                                                    |
| Geometric mean | (ref)                                                  | 1.37x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240824-linux-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 321 ms: 2.27x faster                                                     |
| async_tree_memoization  | 870 ms                                                 | 388 ms: 2.24x faster                                                     |
| async_tree_io           | 1.77 sec                                               | 926 ms: 1.91x faster                                                     |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 556 ms: 1.83x faster                                                     |
| Geometric mean          | (ref)                                                  | 2.05x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240824-linux-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 86.0 ms: 1.79x faster                                                    |
| float          | 117 ms                                                 | 76.9 ms: 1.52x faster                                                    |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                  | 1.41x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240824-linux-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 126 ms: 1.49x faster                                                     |
| regex_v8       | 27.8 ms                                                | 25.0 ms: 1.11x faster                                                    |
| regex_effbot   | 3.63 ms                                                | 3.48 ms: 1.04x faster                                                    |
| regex_dna      | 227 ms                                                 | 219 ms: 1.04x faster                                                     |
| Geometric mean | (ref)                                                  | 1.16x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240824-linux-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 298 us: 1.63x faster                                                     |
| unpickle_pure_python | 331 us                                                 | 211 us: 1.57x faster                                                     |
| tomli_loads          | 3.14 sec                                               | 2.07 sec: 1.52x faster                                                   |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                    |
| xml_etree_process    | 79.1 ms                                                | 58.3 ms: 1.36x faster                                                    |
| xml_etree_generate   | 99.4 ms                                                | 84.6 ms: 1.18x faster                                                    |
| xml_etree_iterparse  | 115 ms                                                 | 105 ms: 1.10x faster                                                     |
| json_loads           | 31.2 us                                                | 28.6 us: 1.09x faster                                                    |
| xml_etree_parse      | 168 ms                                                 | 157 ms: 1.07x faster                                                     |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240824-linux-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                    |
| python_startup_no_site | 5.93 ms                                                | 7.05 ms: 1.19x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240824-linux-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 21.5 ms: 1.48x faster                                                    |
| mako            | 16.3 ms                                                | 11.4 ms: 1.44x faster                                                    |
| django_template | 48.2 ms                                                | 33.8 ms: 1.43x faster                                                    |
| genshi_xml      | 66.0 ms                                                | 48.6 ms: 1.36x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240824-linux-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 159 us: 3.42x faster                                                     |
| generators               | 80.1 ms                                                | 27.9 ms: 2.87x faster                                                    |
| deltablue                | 7.91 ms                                                | 3.17 ms: 2.49x faster                                                    |
| async_tree_none          | 728 ms                                                 | 321 ms: 2.27x faster                                                     |
| async_tree_memoization   | 870 ms                                                 | 388 ms: 2.24x faster                                                     |
| deepcopy_memo            | 58.5 us                                                | 29.0 us: 2.01x faster                                                    |
| logging_silent           | 190 ns                                                 | 94.5 ns: 2.01x faster                                                    |
| chaos                    | 115 ms                                                 | 58.0 ms: 1.99x faster                                                    |
| raytrace                 | 507 ms                                                 | 259 ms: 1.96x faster                                                     |
| asyncio_tcp              | 922 ms                                                 | 479 ms: 1.93x faster                                                     |
| async_tree_io            | 1.77 sec                                               | 926 ms: 1.91x faster                                                     |
| deepcopy                 | 479 us                                                 | 261 us: 1.83x faster                                                     |
| richards_super           | 94.7 ms                                                | 51.7 ms: 1.83x faster                                                    |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 556 ms: 1.83x faster                                                     |
| nbody                    | 154 ms                                                 | 86.0 ms: 1.79x faster                                                    |
| scimark_sor              | 220 ms                                                 | 123 ms: 1.78x faster                                                     |
| crypto_pyaes             | 128 ms                                                 | 72.4 ms: 1.77x faster                                                    |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                                    |
| richards                 | 79.3 ms                                                | 45.8 ms: 1.73x faster                                                    |
| pylint                   | 551 ms                                                 | 319 ms: 1.73x faster                                                     |
| scimark_monte_carlo      | 118 ms                                                 | 68.7 ms: 1.72x faster                                                    |
| sqlglot_parse            | 2.17 ms                                                | 1.27 ms: 1.71x faster                                                    |
| hexiom                   | 10.4 ms                                                | 6.12 ms: 1.70x faster                                                    |
| sqlglot_transpile        | 2.57 ms                                                | 1.56 ms: 1.65x faster                                                    |
| pickle_pure_python       | 484 us                                                 | 298 us: 1.63x faster                                                     |
| pyflate                  | 716 ms                                                 | 454 ms: 1.58x faster                                                     |
| unpickle_pure_python     | 331 us                                                 | 211 us: 1.57x faster                                                     |
| scimark_lu               | 176 ms                                                 | 113 ms: 1.57x faster                                                     |
| spectral_norm            | 170 ms                                                 | 110 ms: 1.54x faster                                                     |
| deepcopy_reduce          | 4.17 us                                                | 2.72 us: 1.53x faster                                                    |
| float                    | 117 ms                                                 | 76.9 ms: 1.52x faster                                                    |
| tomli_loads              | 3.14 sec                                               | 2.07 sec: 1.52x faster                                                   |
| coroutines               | 35.1 ms                                                | 23.2 ms: 1.51x faster                                                    |
| tornado_http             | 136 ms                                                 | 90.2 ms: 1.51x faster                                                    |
| go                       | 240 ms                                                 | 159 ms: 1.51x faster                                                     |
| regex_compile            | 188 ms                                                 | 126 ms: 1.49x faster                                                     |
| genshi_text              | 31.8 ms                                                | 21.5 ms: 1.48x faster                                                    |
| logging_simple           | 8.30 us                                                | 5.62 us: 1.48x faster                                                    |
| logging_format           | 9.09 us                                                | 6.22 us: 1.46x faster                                                    |
| pprint_pformat           | 2.10 sec                                               | 1.46 sec: 1.44x faster                                                   |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.79 sec: 1.44x faster                                                   |
| mako                     | 16.3 ms                                                | 11.4 ms: 1.44x faster                                                    |
| pprint_safe_repr         | 1.02 sec                                               | 714 ms: 1.43x faster                                                     |
| django_template          | 48.2 ms                                                | 33.8 ms: 1.43x faster                                                    |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.55 ms: 1.42x faster                                                    |
| thrift                   | 1.07 ms                                                | 768 us: 1.40x faster                                                     |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                    |
| pycparser                | 1.58 sec                                               | 1.14 sec: 1.38x faster                                                   |
| 2to3                     | 348 ms                                                 | 254 ms: 1.37x faster                                                     |
| html5lib                 | 88.9 ms                                                | 64.9 ms: 1.37x faster                                                    |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                    |
| genshi_xml               | 66.0 ms                                                | 48.6 ms: 1.36x faster                                                    |
| xml_etree_process        | 79.1 ms                                                | 58.3 ms: 1.36x faster                                                    |
| sqlglot_normalize        | 143 ms                                                 | 106 ms: 1.34x faster                                                     |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.34x faster                                                     |
| fannkuch                 | 532 ms                                                 | 399 ms: 1.33x faster                                                     |
| sympy_integrate          | 25.8 ms                                                | 19.4 ms: 1.33x faster                                                    |
| nqueens                  | 106 ms                                                 | 79.7 ms: 1.33x faster                                                    |
| sqlglot_optimize         | 69.2 ms                                                | 53.1 ms: 1.30x faster                                                    |
| sympy_str                | 346 ms                                                 | 267 ms: 1.30x faster                                                     |
| scimark_fft              | 466 ms                                                 | 359 ms: 1.30x faster                                                     |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.29x faster                                                    |
| bench_thread_pool        | 986 us                                                 | 780 us: 1.26x faster                                                     |
| sympy_expand             | 566 ms                                                 | 455 ms: 1.24x faster                                                     |
| docutils                 | 3.30 sec                                               | 2.69 sec: 1.23x faster                                                   |
| xml_etree_generate       | 99.4 ms                                                | 84.6 ms: 1.18x faster                                                    |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                     |
| regex_v8                 | 27.8 ms                                                | 25.0 ms: 1.11x faster                                                    |
| xml_etree_iterparse      | 115 ms                                                 | 105 ms: 1.10x faster                                                     |
| json_loads               | 31.2 us                                                | 28.6 us: 1.09x faster                                                    |
| json                     | 5.69 ms                                                | 5.26 ms: 1.08x faster                                                    |
| mdp                      | 2.85 sec                                               | 2.65 sec: 1.08x faster                                                   |
| xml_etree_parse          | 168 ms                                                 | 157 ms: 1.07x faster                                                     |
| regex_effbot             | 3.63 ms                                                | 3.48 ms: 1.04x faster                                                    |
| regex_dna                | 227 ms                                                 | 219 ms: 1.04x faster                                                     |
| async_generators         | 444 ms                                                 | 431 ms: 1.03x faster                                                     |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                     |
| gc_traversal             | 3.62 ms                                                | 3.72 ms: 1.03x slower                                                    |
| coverage                 | 79.4 ms                                                | 85.3 ms: 1.07x slower                                                    |
| create_gc_cycles         | 1.62 ms                                                | 1.75 ms: 1.08x slower                                                    |
| telco                    | 7.27 ms                                                | 8.34 ms: 1.15x slower                                                    |
| python_startup_no_site   | 5.93 ms                                                | 7.05 ms: 1.19x slower                                                    |
| Geometric mean           | (ref)                                                  | 1.44x faster                                                             |

Benchmark hidden because not significant (2): bench_mp_pool, asyncio_websockets
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240824-3.14.0a0-bf9cfa8/bm-20240824-linux-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.35x
- 95% likely to have a speedup of 1.34x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: 1.12x