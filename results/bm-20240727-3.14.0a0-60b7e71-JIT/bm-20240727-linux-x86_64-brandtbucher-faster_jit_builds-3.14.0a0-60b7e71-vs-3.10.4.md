# Results vs. 3.10.4

- fork: brandtbucher
- ref: faster_jit_builds
- machine: linux-x86_64
- commit hash: 60b7e71
- commit date: 2024-07-27
- overall geometric mean: 1.43x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 271 ms: 1.29x faster                                                     |
| docutils       | 3.30 sec                                               | 2.90 sec: 1.14x faster                                                   |
| html5lib       | 88.9 ms                                                | 65.6 ms: 1.35x faster                                                    |
| tornado_http   | 136 ms                                                 | 92.9 ms: 1.47x faster                                                    |
| Geometric mean | (ref)                                                  | 1.31x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 326 ms: 2.23x faster                                                     |
| async_tree_memoization  | 870 ms                                                 | 413 ms: 2.11x faster                                                     |
| async_tree_io           | 1.77 sec                                               | 896 ms: 1.97x faster                                                     |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 562 ms: 1.81x faster                                                     |
| Geometric mean          | (ref)                                                  | 2.02x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 81.4 ms: 1.89x faster                                                    |
| float          | 117 ms                                                 | 70.0 ms: 1.67x faster                                                    |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                  | 1.48x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 132 ms: 1.42x faster                                                     |
| regex_v8       | 27.8 ms                                                | 25.1 ms: 1.11x faster                                                    |
| regex_dna      | 227 ms                                                 | 228 ms: 1.01x slower                                                     |
| regex_effbot   | 3.63 ms                                                | 3.86 ms: 1.06x slower                                                    |
| Geometric mean | (ref)                                                  | 1.10x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 294 us: 1.65x faster                                                     |
| tomli_loads          | 3.14 sec                                               | 1.91 sec: 1.64x faster                                                   |
| unpickle_pure_python | 331 us                                                 | 214 us: 1.55x faster                                                     |
| xml_etree_process    | 79.1 ms                                                | 56.4 ms: 1.40x faster                                                    |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.36x faster                                                    |
| xml_etree_generate   | 99.4 ms                                                | 80.7 ms: 1.23x faster                                                    |
| xml_etree_iterparse  | 115 ms                                                 | 99.5 ms: 1.16x faster                                                    |
| xml_etree_parse      | 168 ms                                                 | 147 ms: 1.14x faster                                                     |
| json_loads           | 31.2 us                                                | 27.7 us: 1.13x faster                                                    |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                    |
| python_startup_no_site | 5.93 ms                                                | 7.16 ms: 1.21x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.95 ms: 1.64x faster                                                    |
| django_template | 48.2 ms                                                | 35.4 ms: 1.36x faster                                                    |
| genshi_text     | 31.8 ms                                                | 24.6 ms: 1.29x faster                                                    |
| genshi_xml      | 66.0 ms                                                | 58.9 ms: 1.12x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.34x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 169 us: 3.23x faster                                                     |
| generators               | 80.1 ms                                                | 28.5 ms: 2.81x faster                                                    |
| deltablue                | 7.91 ms                                                | 3.48 ms: 2.27x faster                                                    |
| async_tree_none          | 728 ms                                                 | 326 ms: 2.23x faster                                                     |
| async_tree_memoization   | 870 ms                                                 | 413 ms: 2.11x faster                                                     |
| deepcopy_memo            | 58.5 us                                                | 28.1 us: 2.08x faster                                                    |
| richards_super           | 94.7 ms                                                | 46.7 ms: 2.03x faster                                                    |
| chaos                    | 115 ms                                                 | 58.1 ms: 1.99x faster                                                    |
| async_tree_io            | 1.77 sec                                               | 896 ms: 1.97x faster                                                     |
| richards                 | 79.3 ms                                                | 40.3 ms: 1.97x faster                                                    |
| scimark_monte_carlo      | 118 ms                                                 | 60.2 ms: 1.96x faster                                                    |
| raytrace                 | 507 ms                                                 | 266 ms: 1.90x faster                                                     |
| crypto_pyaes             | 128 ms                                                 | 67.4 ms: 1.90x faster                                                    |
| nbody                    | 154 ms                                                 | 81.4 ms: 1.89x faster                                                    |
| logging_silent           | 190 ns                                                 | 101 ns: 1.88x faster                                                     |
| asyncio_tcp              | 922 ms                                                 | 496 ms: 1.86x faster                                                     |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 562 ms: 1.81x faster                                                     |
| deepcopy                 | 479 us                                                 | 270 us: 1.77x faster                                                     |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                                    |
| spectral_norm            | 170 ms                                                 | 98.4 ms: 1.73x faster                                                    |
| sqlglot_parse            | 2.17 ms                                                | 1.26 ms: 1.73x faster                                                    |
| scimark_sor              | 220 ms                                                 | 128 ms: 1.72x faster                                                     |
| go                       | 240 ms                                                 | 143 ms: 1.68x faster                                                     |
| float                    | 117 ms                                                 | 70.0 ms: 1.67x faster                                                    |
| pyflate                  | 716 ms                                                 | 431 ms: 1.66x faster                                                     |
| pickle_pure_python       | 484 us                                                 | 294 us: 1.65x faster                                                     |
| tomli_loads              | 3.14 sec                                               | 1.91 sec: 1.64x faster                                                   |
| mako                     | 16.3 ms                                                | 9.95 ms: 1.64x faster                                                    |
| sqlglot_transpile        | 2.57 ms                                                | 1.59 ms: 1.62x faster                                                    |
| hexiom                   | 10.4 ms                                                | 6.55 ms: 1.59x faster                                                    |
| pylint                   | 551 ms                                                 | 349 ms: 1.58x faster                                                     |
| unpickle_pure_python     | 331 us                                                 | 214 us: 1.55x faster                                                     |
| coroutines               | 35.1 ms                                                | 22.7 ms: 1.54x faster                                                    |
| logging_simple           | 8.30 us                                                | 5.47 us: 1.52x faster                                                    |
| scimark_fft              | 466 ms                                                 | 308 ms: 1.51x faster                                                     |
| logging_format           | 9.09 us                                                | 6.00 us: 1.51x faster                                                    |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.31 ms: 1.50x faster                                                    |
| deepcopy_reduce          | 4.17 us                                                | 2.78 us: 1.50x faster                                                    |
| tornado_http             | 136 ms                                                 | 92.9 ms: 1.47x faster                                                    |
| pprint_pformat           | 2.10 sec                                               | 1.46 sec: 1.44x faster                                                   |
| pprint_safe_repr         | 1.02 sec                                               | 708 ms: 1.44x faster                                                     |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.79 sec: 1.43x faster                                                   |
| regex_compile            | 188 ms                                                 | 132 ms: 1.42x faster                                                     |
| fannkuch                 | 532 ms                                                 | 374 ms: 1.42x faster                                                     |
| xml_etree_process        | 79.1 ms                                                | 56.4 ms: 1.40x faster                                                    |
| scimark_lu               | 176 ms                                                 | 126 ms: 1.40x faster                                                     |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                    |
| thrift                   | 1.07 ms                                                | 785 us: 1.36x faster                                                     |
| django_template          | 48.2 ms                                                | 35.4 ms: 1.36x faster                                                    |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.36x faster                                                    |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                                   |
| html5lib                 | 88.9 ms                                                | 65.6 ms: 1.35x faster                                                    |
| genshi_text              | 31.8 ms                                                | 24.6 ms: 1.29x faster                                                    |
| 2to3                     | 348 ms                                                 | 271 ms: 1.29x faster                                                     |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.28x faster                                                    |
| sqlglot_normalize        | 143 ms                                                 | 112 ms: 1.27x faster                                                     |
| sqlglot_optimize         | 69.2 ms                                                | 55.8 ms: 1.24x faster                                                    |
| xml_etree_generate       | 99.4 ms                                                | 80.7 ms: 1.23x faster                                                    |
| nqueens                  | 106 ms                                                 | 86.6 ms: 1.22x faster                                                    |
| dask                     | 441 ms                                                 | 364 ms: 1.21x faster                                                     |
| bench_thread_pool        | 986 us                                                 | 824 us: 1.20x faster                                                     |
| sympy_sum                | 196 ms                                                 | 168 ms: 1.17x faster                                                     |
| sympy_str                | 346 ms                                                 | 295 ms: 1.17x faster                                                     |
| sympy_integrate          | 25.8 ms                                                | 22.2 ms: 1.16x faster                                                    |
| xml_etree_iterparse      | 115 ms                                                 | 99.5 ms: 1.16x faster                                                    |
| meteor_contest           | 120 ms                                                 | 104 ms: 1.15x faster                                                     |
| xml_etree_parse          | 168 ms                                                 | 147 ms: 1.14x faster                                                     |
| docutils                 | 3.30 sec                                               | 2.90 sec: 1.14x faster                                                   |
| sympy_expand             | 566 ms                                                 | 501 ms: 1.13x faster                                                     |
| json_loads               | 31.2 us                                                | 27.7 us: 1.13x faster                                                    |
| mdp                      | 2.85 sec                                               | 2.53 sec: 1.12x faster                                                   |
| genshi_xml               | 66.0 ms                                                | 58.9 ms: 1.12x faster                                                    |
| json                     | 5.69 ms                                                | 5.13 ms: 1.11x faster                                                    |
| regex_v8                 | 27.8 ms                                                | 25.1 ms: 1.11x faster                                                    |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                     |
| regex_dna                | 227 ms                                                 | 228 ms: 1.01x slower                                                     |
| gc_traversal             | 3.62 ms                                                | 3.73 ms: 1.03x slower                                                    |
| async_generators         | 444 ms                                                 | 461 ms: 1.04x slower                                                     |
| regex_effbot             | 3.63 ms                                                | 3.86 ms: 1.06x slower                                                    |
| telco                    | 7.27 ms                                                | 7.82 ms: 1.08x slower                                                    |
| create_gc_cycles         | 1.62 ms                                                | 1.75 ms: 1.08x slower                                                    |
| coverage                 | 79.4 ms                                                | 91.3 ms: 1.15x slower                                                    |
| python_startup_no_site   | 5.93 ms                                                | 7.16 ms: 1.21x slower                                                    |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                             |

Benchmark hidden because not significant (2): bench_mp_pool, asyncio_websockets
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240727-3.14.0a0-60b7e71-JIT/bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.19x