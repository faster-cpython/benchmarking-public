# Results vs. 3.10.4

- fork: python
- ref: 16cd6cc86b3ba20074ae
- machine: linux-aarch64
- commit hash: 16cd6cc
- commit date: 2024-10-05
- overall geometric mean: 1.11x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 3.53 sec                                                              | 3.71 sec: 1.05x slower                                                  |
| html5lib       | 86.5 ms                                                               | 71.0 ms: 1.22x faster                                                   |
| tornado_http   | 178 ms                                                                | 147 ms: 1.21x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.09x faster                                                            |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 445 ms: 2.13x faster                                                    |
| async_tree_io           | 2.28 sec                                                              | 1.15 sec: 1.99x faster                                                  |
| async_tree_memoization  | 1.13 sec                                                              | 591 ms: 1.92x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 753 ms: 1.69x faster                                                    |
| Geometric mean          | (ref)                                                                 | 1.93x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 90.0 ms: 1.50x faster                                                   |
| nbody          | 166 ms                                                                | 112 ms: 1.49x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.31x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 31.0 ms: 1.04x faster                                                   |
| regex_dna      | 257 ms                                                                | 262 ms: 1.02x slower                                                    |
| regex_compile  | 177 ms                                                                | 184 ms: 1.04x slower                                                    |
| regex_effbot   | 4.25 ms                                                               | 5.02 ms: 1.18x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 386 us: 1.37x faster                                                    |
| unpickle_pure_python | 366 us                                                                | 268 us: 1.36x faster                                                    |
| json_dumps           | 16.7 ms                                                               | 13.1 ms: 1.28x faster                                                   |
| tomli_loads          | 3.36 sec                                                              | 2.64 sec: 1.27x faster                                                  |
| xml_etree_process    | 99.5 ms                                                               | 81.5 ms: 1.22x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 188 ms: 1.13x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 112 ms: 1.10x faster                                                    |
| unpickle_list        | 6.99 us                                                               | 6.37 us: 1.10x faster                                                   |
| xml_etree_iterparse  | 156 ms                                                                | 150 ms: 1.04x faster                                                    |
| pickle_dict          | 35.1 us                                                               | 37.7 us: 1.07x slower                                                   |
| unpickle             | 17.5 us                                                               | 19.2 us: 1.10x slower                                                   |
| pickle               | 12.5 us                                                               | 13.8 us: 1.10x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.10x faster                                                            |

Benchmark hidden because not significant (2): pickle_list, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 12.9 ms: 1.16x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 8.73 ms: 1.27x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.21x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.0 ms: 1.45x faster                                                   |
| django_template | 53.3 ms                                                               | 51.8 ms: 1.03x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 34.4 ms: 1.02x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 83.1 ms: 1.19x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.06x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 213 us: 3.10x faster                                                    |
| async_tree_none          | 950 ms                                                                | 445 ms: 2.13x faster                                                    |
| deltablue                | 8.94 ms                                                               | 4.35 ms: 2.05x faster                                                   |
| async_tree_io            | 2.28 sec                                                              | 1.15 sec: 1.99x faster                                                  |
| async_tree_memoization   | 1.13 sec                                                              | 591 ms: 1.92x faster                                                    |
| logging_silent           | 222 ns                                                                | 131 ns: 1.70x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 753 ms: 1.69x faster                                                    |
| raytrace                 | 573 ms                                                                | 350 ms: 1.64x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 37.9 us: 1.63x faster                                                   |
| scimark_sor              | 246 ms                                                                | 152 ms: 1.62x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 611 ms: 1.55x faster                                                    |
| scimark_lu               | 227 ms                                                                | 150 ms: 1.51x faster                                                    |
| float                    | 135 ms                                                                | 90.0 ms: 1.50x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 89.9 ms: 1.49x faster                                                   |
| richards_super           | 107 ms                                                                | 72.0 ms: 1.49x faster                                                   |
| nbody                    | 166 ms                                                                | 112 ms: 1.49x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.0 ms: 1.45x faster                                                   |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.27 sec: 1.45x faster                                                  |
| richards                 | 91.7 ms                                                               | 63.8 ms: 1.44x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 89.1 ms: 1.43x faster                                                   |
| go                       | 264 ms                                                                | 185 ms: 1.43x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.74 ms: 1.38x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 386 us: 1.37x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 268 us: 1.36x faster                                                    |
| chaos                    | 121 ms                                                                | 90.5 ms: 1.34x faster                                                   |
| comprehensions           | 33.1 us                                                               | 24.9 us: 1.33x faster                                                   |
| thrift                   | 1.26 ms                                                               | 960 us: 1.31x faster                                                    |
| logging_format           | 10.6 us                                                               | 8.11 us: 1.31x faster                                                   |
| logging_simple           | 9.78 us                                                               | 7.54 us: 1.30x faster                                                   |
| spectral_norm            | 186 ms                                                                | 145 ms: 1.29x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 2.21 ms: 1.28x faster                                                   |
| coroutines               | 37.2 ms                                                               | 29.0 ms: 1.28x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 13.1 ms: 1.28x faster                                                   |
| deepcopy                 | 511 us                                                                | 400 us: 1.27x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.64 sec: 1.27x faster                                                  |
| pyflate                  | 795 ms                                                                | 640 ms: 1.24x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 81.5 ms: 1.22x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 71.0 ms: 1.22x faster                                                   |
| tornado_http             | 178 ms                                                                | 147 ms: 1.21x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 21.8 ms: 1.21x faster                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 3.93 us: 1.17x faster                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.37 ms: 1.16x faster                                                   |
| generators               | 68.1 ms                                                               | 59.2 ms: 1.15x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.48 sec: 1.14x faster                                                  |
| xml_etree_parse          | 212 ms                                                                | 188 ms: 1.13x faster                                                    |
| scimark_fft              | 500 ms                                                                | 446 ms: 1.12x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.87 ms: 1.11x faster                                                   |
| xml_etree_generate       | 123 ms                                                                | 112 ms: 1.10x faster                                                    |
| unpickle_list            | 6.99 us                                                               | 6.37 us: 1.10x faster                                                   |
| fannkuch                 | 546 ms                                                                | 503 ms: 1.08x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 10.1 ms: 1.08x faster                                                   |
| mdp                      | 3.70 sec                                                              | 3.48 sec: 1.06x faster                                                  |
| json                     | 5.88 ms                                                               | 5.57 ms: 1.05x faster                                                   |
| sqlite_synth             | 4.12 us                                                               | 3.91 us: 1.05x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 150 ms: 1.04x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 31.0 ms: 1.04x faster                                                   |
| django_template          | 53.3 ms                                                               | 51.8 ms: 1.03x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 34.4 ms: 1.02x faster                                                   |
| meteor_contest           | 126 ms                                                                | 124 ms: 1.02x faster                                                    |
| asyncio_websockets       | 657 ms                                                                | 664 ms: 1.01x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 2.29 ms: 1.01x slower                                                   |
| regex_dna                | 257 ms                                                                | 262 ms: 1.02x slower                                                    |
| regex_compile            | 177 ms                                                                | 184 ms: 1.04x slower                                                    |
| docutils                 | 3.53 sec                                                              | 3.71 sec: 1.05x slower                                                  |
| nqueens                  | 117 ms                                                                | 124 ms: 1.06x slower                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 1.23 sec: 1.07x slower                                                  |
| pickle_dict              | 35.1 us                                                               | 37.7 us: 1.07x slower                                                   |
| dulwich_log              | 73.5 ms                                                               | 80.1 ms: 1.09x slower                                                   |
| sqlglot_optimize         | 75.4 ms                                                               | 82.2 ms: 1.09x slower                                                   |
| unpickle                 | 17.5 us                                                               | 19.2 us: 1.10x slower                                                   |
| sympy_expand             | 543 ms                                                                | 598 ms: 1.10x slower                                                    |
| pickle                   | 12.5 us                                                               | 13.8 us: 1.10x slower                                                   |
| pprint_pformat           | 2.36 sec                                                              | 2.61 sec: 1.11x slower                                                  |
| sympy_integrate          | 26.5 ms                                                               | 29.6 ms: 1.11x slower                                                   |
| sympy_str                | 329 ms                                                                | 366 ms: 1.12x slower                                                    |
| async_generators         | 452 ms                                                                | 508 ms: 1.12x slower                                                    |
| telco                    | 8.49 ms                                                               | 9.75 ms: 1.15x slower                                                   |
| python_startup           | 11.2 ms                                                               | 12.9 ms: 1.16x slower                                                   |
| regex_effbot             | 4.25 ms                                                               | 5.02 ms: 1.18x slower                                                   |
| sympy_sum                | 184 ms                                                                | 218 ms: 1.18x slower                                                    |
| genshi_xml               | 69.8 ms                                                               | 83.1 ms: 1.19x slower                                                   |
| coverage                 | 83.6 ms                                                               | 101 ms: 1.20x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 5.05 ms: 1.21x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.73 ms: 1.27x slower                                                   |
| bench_mp_pool            | 14.5 ms                                                               | 2.07 sec: 142.24x slower                                                |
| Geometric mean           | (ref)                                                                 | 1.11x faster                                                            |

Benchmark hidden because not significant (6): pickle_list, pidigits, sqlglot_normalize, pylint, 2to3, json_loads
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241005-3.14.0a0-16cd6cc-JIT/bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.21x