# Results vs. 3.10.4

- fork: gvanrossum
- ref: func_version_cache
- machine: linux-x86_64
- commit hash: 0fd96be
- commit date: 2024-03-19
- overall geometric mean: 1.30x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240319-linux-x86_64-gvanrossum-func_version_cache-3.13.0a5+-0fd96be |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 281 ms: 1.24x faster                                                     |
| chameleon      | 9.68 ms                                                | 6.93 ms: 1.40x faster                                                    |
| docutils       | 3.30 sec                                               | 2.75 sec: 1.20x faster                                                   |
| html5lib       | 88.9 ms                                                | 67.0 ms: 1.33x faster                                                    |
| tornado_http   | 136 ms                                                 | 99.1 ms: 1.38x faster                                                    |
| Geometric mean | (ref)                                                  | 1.30x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240319-linux-x86_64-gvanrossum-func_version_cache-3.13.0a5+-0fd96be |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 450 ms: 1.62x faster                                                     |
| async_tree_memoization  | 870 ms                                                 | 575 ms: 1.51x faster                                                     |
| async_tree_io           | 1.77 sec                                               | 1.22 sec: 1.45x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 730 ms: 1.39x faster                                                     |
| Geometric mean          | (ref)                                                  | 1.49x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240319-linux-x86_64-gvanrossum-func_version_cache-3.13.0a5+-0fd96be |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 92.6 ms: 1.66x faster                                                    |
| float          | 117 ms                                                 | 81.4 ms: 1.44x faster                                                    |
| pidigits       | 191 ms                                                 | 190 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                  | 1.34x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240319-linux-x86_64-gvanrossum-func_version_cache-3.13.0a5+-0fd96be |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 143 ms: 1.32x faster                                                     |
| regex_v8       | 27.8 ms                                                | 24.3 ms: 1.14x faster                                                    |
| regex_dna      | 227 ms                                                 | 219 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                  | 1.12x faster                                                             |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240319-linux-x86_64-gvanrossum-func_version_cache-3.13.0a5+-0fd96be |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 304 us: 1.60x faster                                                     |
| tomli_loads          | 3.14 sec                                               | 2.06 sec: 1.52x faster                                                   |
| unpickle_pure_python | 331 us                                                 | 237 us: 1.39x faster                                                     |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                    |
| xml_etree_process    | 79.1 ms                                                | 60.1 ms: 1.32x faster                                                    |
| xml_etree_generate   | 99.4 ms                                                | 88.0 ms: 1.13x faster                                                    |
| json_loads           | 31.2 us                                                | 28.7 us: 1.09x faster                                                    |
| xml_etree_iterparse  | 115 ms                                                 | 109 ms: 1.06x faster                                                     |
| xml_etree_parse      | 168 ms                                                 | 161 ms: 1.04x faster                                                     |
| pickle_list          | 5.08 us                                                | 4.93 us: 1.03x faster                                                    |
| unpickle_list        | 5.20 us                                                | 5.05 us: 1.03x faster                                                    |
| unpickle             | 14.4 us                                                | 15.1 us: 1.05x slower                                                    |
| pickle               | 10.7 us                                                | 11.6 us: 1.08x slower                                                    |
| pickle_dict          | 29.6 us                                                | 33.5 us: 1.13x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240319-linux-x86_64-gvanrossum-func_version_cache-3.13.0a5+-0fd96be |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.5 ms: 1.26x faster                                                    |
| python_startup_no_site | 5.93 ms                                                | 10.1 ms: 1.71x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.16x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240319-linux-x86_64-gvanrossum-func_version_cache-3.13.0a5+-0fd96be |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.0 ms: 1.49x faster                                                    |
| django_template | 48.2 ms                                                | 34.5 ms: 1.40x faster                                                    |
| genshi_text     | 31.8 ms                                                | 24.2 ms: 1.31x faster                                                    |
| genshi_xml      | 66.0 ms                                                | 55.0 ms: 1.20x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240319-linux-x86_64-gvanrossum-func_version_cache-3.13.0a5+-0fd96be |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 111 us: 4.88x faster                                                     |
| generators               | 80.1 ms                                                | 29.6 ms: 2.70x faster                                                    |
| deltablue                | 7.91 ms                                                | 3.46 ms: 2.29x faster                                                    |
| logging_silent           | 190 ns                                                 | 101 ns: 1.87x faster                                                     |
| asyncio_tcp              | 922 ms                                                 | 504 ms: 1.83x faster                                                     |
| richards_super           | 94.7 ms                                                | 52.5 ms: 1.80x faster                                                    |
| chaos                    | 115 ms                                                 | 64.3 ms: 1.80x faster                                                    |
| raytrace                 | 507 ms                                                 | 294 ms: 1.72x faster                                                     |
| richards                 | 79.3 ms                                                | 46.2 ms: 1.72x faster                                                    |
| scimark_sor              | 220 ms                                                 | 129 ms: 1.71x faster                                                     |
| pylint                   | 551 ms                                                 | 324 ms: 1.70x faster                                                     |
| crypto_pyaes             | 128 ms                                                 | 75.6 ms: 1.69x faster                                                    |
| scimark_monte_carlo      | 118 ms                                                 | 70.7 ms: 1.67x faster                                                    |
| nbody                    | 154 ms                                                 | 92.6 ms: 1.66x faster                                                    |
| sqlglot_parse            | 2.17 ms                                                | 1.32 ms: 1.64x faster                                                    |
| async_tree_none          | 728 ms                                                 | 450 ms: 1.62x faster                                                     |
| comprehensions           | 28.8 us                                                | 17.9 us: 1.61x faster                                                    |
| pickle_pure_python       | 484 us                                                 | 304 us: 1.60x faster                                                     |
| sqlglot_transpile        | 2.57 ms                                                | 1.66 ms: 1.55x faster                                                    |
| coroutines               | 35.1 ms                                                | 22.7 ms: 1.55x faster                                                    |
| tomli_loads              | 3.14 sec                                               | 2.06 sec: 1.52x faster                                                   |
| go                       | 240 ms                                                 | 158 ms: 1.52x faster                                                     |
| deepcopy_memo            | 58.5 us                                                | 38.5 us: 1.52x faster                                                    |
| async_tree_memoization   | 870 ms                                                 | 575 ms: 1.51x faster                                                     |
| mako                     | 16.3 ms                                                | 11.0 ms: 1.49x faster                                                    |
| spectral_norm            | 170 ms                                                 | 115 ms: 1.48x faster                                                     |
| hexiom                   | 10.4 ms                                                | 7.03 ms: 1.48x faster                                                    |
| async_tree_io            | 1.77 sec                                               | 1.22 sec: 1.45x faster                                                   |
| pyflate                  | 716 ms                                                 | 495 ms: 1.45x faster                                                     |
| float                    | 117 ms                                                 | 81.4 ms: 1.44x faster                                                    |
| logging_simple           | 8.30 us                                                | 5.84 us: 1.42x faster                                                    |
| logging_format           | 9.09 us                                                | 6.48 us: 1.40x faster                                                    |
| chameleon                | 9.68 ms                                                | 6.93 ms: 1.40x faster                                                    |
| django_template          | 48.2 ms                                                | 34.5 ms: 1.40x faster                                                    |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 730 ms: 1.39x faster                                                     |
| unpickle_pure_python     | 331 us                                                 | 237 us: 1.39x faster                                                     |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.85 sec: 1.39x faster                                                   |
| tornado_http             | 136 ms                                                 | 99.1 ms: 1.38x faster                                                    |
| deepcopy                 | 479 us                                                 | 351 us: 1.36x faster                                                     |
| pprint_pformat           | 2.10 sec                                               | 1.55 sec: 1.36x faster                                                   |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                    |
| scimark_lu               | 176 ms                                                 | 131 ms: 1.35x faster                                                     |
| pprint_safe_repr         | 1.02 sec                                               | 760 ms: 1.34x faster                                                     |
| scimark_fft              | 466 ms                                                 | 348 ms: 1.34x faster                                                     |
| deepcopy_reduce          | 4.17 us                                                | 3.13 us: 1.33x faster                                                    |
| thrift                   | 1.07 ms                                                | 805 us: 1.33x faster                                                     |
| fannkuch                 | 532 ms                                                 | 400 ms: 1.33x faster                                                     |
| html5lib                 | 88.9 ms                                                | 67.0 ms: 1.33x faster                                                    |
| regex_compile            | 188 ms                                                 | 143 ms: 1.32x faster                                                     |
| xml_etree_process        | 79.1 ms                                                | 60.1 ms: 1.32x faster                                                    |
| genshi_text              | 31.8 ms                                                | 24.2 ms: 1.31x faster                                                    |
| pycparser                | 1.58 sec                                               | 1.20 sec: 1.31x faster                                                   |
| sqlglot_normalize        | 143 ms                                                 | 109 ms: 1.31x faster                                                     |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.06 ms: 1.28x faster                                                    |
| python_startup           | 14.6 ms                                                | 11.5 ms: 1.26x faster                                                    |
| 2to3                     | 348 ms                                                 | 281 ms: 1.24x faster                                                     |
| sympy_integrate          | 25.8 ms                                                | 21.3 ms: 1.21x faster                                                    |
| sqlglot_optimize         | 69.2 ms                                                | 57.2 ms: 1.21x faster                                                    |
| aiohttp                  | 1.44 ms                                                | 1.19 ms: 1.21x faster                                                    |
| djangocms                | 38.4 us                                                | 31.9 us: 1.20x faster                                                    |
| dulwich_log              | 84.3 ms                                                | 70.2 ms: 1.20x faster                                                    |
| sympy_sum                | 196 ms                                                 | 164 ms: 1.20x faster                                                     |
| genshi_xml               | 66.0 ms                                                | 55.0 ms: 1.20x faster                                                    |
| docutils                 | 3.30 sec                                               | 2.75 sec: 1.20x faster                                                   |
| sympy_str                | 346 ms                                                 | 289 ms: 1.20x faster                                                     |
| dask                     | 441 ms                                                 | 371 ms: 1.19x faster                                                     |
| gunicorn                 | 1.53 ms                                                | 1.29 ms: 1.18x faster                                                    |
| nqueens                  | 106 ms                                                 | 90.2 ms: 1.17x faster                                                    |
| bench_thread_pool        | 986 us                                                 | 848 us: 1.16x faster                                                     |
| sympy_expand             | 566 ms                                                 | 490 ms: 1.16x faster                                                     |
| regex_v8                 | 27.8 ms                                                | 24.3 ms: 1.14x faster                                                    |
| xml_etree_generate       | 99.4 ms                                                | 88.0 ms: 1.13x faster                                                    |
| pathlib                  | 20.5 ms                                                | 18.7 ms: 1.09x faster                                                    |
| json_loads               | 31.2 us                                                | 28.7 us: 1.09x faster                                                    |
| mdp                      | 2.85 sec                                               | 2.63 sec: 1.08x faster                                                   |
| meteor_contest           | 120 ms                                                 | 110 ms: 1.08x faster                                                     |
| json                     | 5.69 ms                                                | 5.27 ms: 1.08x faster                                                    |
| sqlite_synth             | 3.02 us                                                | 2.85 us: 1.06x faster                                                    |
| create_gc_cycles         | 1.62 ms                                                | 1.53 ms: 1.06x faster                                                    |
| xml_etree_iterparse      | 115 ms                                                 | 109 ms: 1.06x faster                                                     |
| xml_etree_parse          | 168 ms                                                 | 161 ms: 1.04x faster                                                     |
| regex_dna                | 227 ms                                                 | 219 ms: 1.03x faster                                                     |
| pickle_list              | 5.08 us                                                | 4.93 us: 1.03x faster                                                    |
| unpickle_list            | 5.20 us                                                | 5.05 us: 1.03x faster                                                    |
| pidigits                 | 191 ms                                                 | 190 ms: 1.01x faster                                                     |
| asyncio_websockets       | 559 ms                                                 | 564 ms: 1.01x slower                                                     |
| unpickle                 | 14.4 us                                                | 15.1 us: 1.05x slower                                                    |
| gc_traversal             | 3.62 ms                                                | 3.85 ms: 1.06x slower                                                    |
| async_generators         | 444 ms                                                 | 478 ms: 1.08x slower                                                     |
| pickle                   | 10.7 us                                                | 11.6 us: 1.08x slower                                                    |
| pickle_dict              | 29.6 us                                                | 33.5 us: 1.13x slower                                                    |
| telco                    | 7.27 ms                                                | 8.42 ms: 1.16x slower                                                    |
| coverage                 | 79.4 ms                                                | 98.6 ms: 1.24x slower                                                    |
| unpack_sequence          | 60.0 ns                                                | 87.7 ns: 1.46x slower                                                    |
| python_startup_no_site   | 5.93 ms                                                | 10.1 ms: 1.71x slower                                                    |
| Geometric mean           | (ref)                                                  | 1.30x faster                                                             |

Benchmark hidden because not significant (3): regex_effbot, bench_mp_pool, mypy2
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240319-3.13.0a5+-0fd96be-JIT/bm-20240319-linux-x86_64-gvanrossum-func_version_cache-3.13.0a5+-0fd96be.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.21x


# Memory

- memory change: 1.22x