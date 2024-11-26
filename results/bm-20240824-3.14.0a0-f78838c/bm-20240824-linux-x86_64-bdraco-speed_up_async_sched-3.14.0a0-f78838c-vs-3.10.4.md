# Results vs. 3.10.4

- fork: bdraco
- ref: speed_up_async_sched
- machine: linux-x86_64
- commit hash: f78838c
- commit date: 2024-08-24
- overall geometric mean: 1.440x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 255 ms: 1.37x faster                                                  |
| docutils       | 3.30 sec                                               | 2.69 sec: 1.23x faster                                                |
| html5lib       | 88.9 ms                                                | 65.2 ms: 1.36x faster                                                 |
| tornado_http   | 136 ms                                                 | 89.9 ms: 1.52x faster                                                 |
| Geometric mean | (ref)                                                  | 1.36x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 321 ms: 2.27x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 402 ms: 2.16x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 891 ms: 1.98x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 544 ms: 1.87x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.07x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 85.5 ms: 1.79x faster                                                 |
| float          | 117 ms                                                 | 77.7 ms: 1.51x faster                                                 |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.40x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.47x faster                                                  |
| regex_v8       | 27.8 ms                                                | 24.1 ms: 1.15x faster                                                 |
| regex_dna      | 227 ms                                                 | 220 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.15x faster                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 301 us: 1.61x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 213 us: 1.55x faster                                                  |
| tomli_loads          | 3.14 sec                                               | 2.07 sec: 1.52x faster                                                |
| json_dumps           | 14.2 ms                                                | 10.3 ms: 1.37x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 58.2 ms: 1.36x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 83.8 ms: 1.19x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 104 ms: 1.11x faster                                                  |
| json_loads           | 31.2 us                                                | 28.2 us: 1.10x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 156 ms: 1.08x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.31x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.38x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.10 ms: 1.20x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.1 ms: 1.47x faster                                                 |
| genshi_text     | 31.8 ms                                                | 21.8 ms: 1.46x faster                                                 |
| django_template | 48.2 ms                                                | 33.7 ms: 1.43x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 49.5 ms: 1.34x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 159 us: 3.43x faster                                                  |
| generators               | 80.1 ms                                                | 27.6 ms: 2.91x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.18 ms: 2.49x faster                                                 |
| async_tree_none          | 728 ms                                                 | 321 ms: 2.27x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 402 ms: 2.16x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 891 ms: 1.98x faster                                                  |
| chaos                    | 115 ms                                                 | 58.2 ms: 1.98x faster                                                 |
| deepcopy_memo            | 58.5 us                                                | 29.5 us: 1.98x faster                                                 |
| raytrace                 | 507 ms                                                 | 262 ms: 1.93x faster                                                  |
| asyncio_tcp              | 922 ms                                                 | 477 ms: 1.93x faster                                                  |
| logging_silent           | 190 ns                                                 | 101 ns: 1.88x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 544 ms: 1.87x faster                                                  |
| deepcopy                 | 479 us                                                 | 259 us: 1.85x faster                                                  |
| richards_super           | 94.7 ms                                                | 52.0 ms: 1.82x faster                                                 |
| nbody                    | 154 ms                                                 | 85.5 ms: 1.79x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 72.0 ms: 1.77x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 67.3 ms: 1.76x faster                                                 |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.75x faster                                                 |
| scimark_sor              | 220 ms                                                 | 127 ms: 1.74x faster                                                  |
| pylint                   | 551 ms                                                 | 320 ms: 1.72x faster                                                  |
| richards                 | 79.3 ms                                                | 46.2 ms: 1.71x faster                                                 |
| sqlglot_parse            | 2.17 ms                                                | 1.27 ms: 1.70x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.11 ms: 1.70x faster                                                 |
| sqlglot_transpile        | 2.57 ms                                                | 1.57 ms: 1.64x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 301 us: 1.61x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.64 us: 1.58x faster                                                 |
| scimark_lu               | 176 ms                                                 | 113 ms: 1.56x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 213 us: 1.55x faster                                                  |
| coroutines               | 35.1 ms                                                | 22.9 ms: 1.53x faster                                                 |
| spectral_norm            | 170 ms                                                 | 111 ms: 1.53x faster                                                  |
| pyflate                  | 716 ms                                                 | 470 ms: 1.53x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 2.07 sec: 1.52x faster                                                |
| tornado_http             | 136 ms                                                 | 89.9 ms: 1.52x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.48 us: 1.52x faster                                                 |
| float                    | 117 ms                                                 | 77.7 ms: 1.51x faster                                                 |
| logging_format           | 9.09 us                                                | 6.03 us: 1.51x faster                                                 |
| go                       | 240 ms                                                 | 162 ms: 1.48x faster                                                  |
| mako                     | 16.3 ms                                                | 11.1 ms: 1.47x faster                                                 |
| regex_compile            | 188 ms                                                 | 128 ms: 1.47x faster                                                  |
| genshi_text              | 31.8 ms                                                | 21.8 ms: 1.46x faster                                                 |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.79 sec: 1.44x faster                                                |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.43x faster                                                |
| django_template          | 48.2 ms                                                | 33.7 ms: 1.43x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 720 ms: 1.41x faster                                                  |
| thrift                   | 1.07 ms                                                | 764 us: 1.40x faster                                                  |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.38x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.14 sec: 1.38x faster                                                |
| json_dumps               | 14.2 ms                                                | 10.3 ms: 1.37x faster                                                 |
| 2to3                     | 348 ms                                                 | 255 ms: 1.37x faster                                                  |
| html5lib                 | 88.9 ms                                                | 65.2 ms: 1.36x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 58.2 ms: 1.36x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.76 ms: 1.36x faster                                                 |
| sympy_sum                | 196 ms                                                 | 146 ms: 1.35x faster                                                  |
| sqlglot_normalize        | 143 ms                                                 | 107 ms: 1.34x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 49.5 ms: 1.34x faster                                                 |
| nqueens                  | 106 ms                                                 | 79.3 ms: 1.33x faster                                                 |
| fannkuch                 | 532 ms                                                 | 401 ms: 1.33x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 19.5 ms: 1.33x faster                                                 |
| pathlib                  | 20.5 ms                                                | 15.7 ms: 1.30x faster                                                 |
| sympy_str                | 346 ms                                                 | 265 ms: 1.30x faster                                                  |
| sqlglot_optimize         | 69.2 ms                                                | 53.3 ms: 1.30x faster                                                 |
| scimark_fft              | 466 ms                                                 | 365 ms: 1.28x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 783 us: 1.26x faster                                                  |
| sympy_expand             | 566 ms                                                 | 451 ms: 1.25x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.69 sec: 1.23x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 83.8 ms: 1.19x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 24.1 ms: 1.15x faster                                                 |
| mdp                      | 2.85 sec                                               | 2.53 sec: 1.13x faster                                                |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 104 ms: 1.11x faster                                                  |
| json_loads               | 31.2 us                                                | 28.2 us: 1.10x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 156 ms: 1.08x faster                                                  |
| json                     | 5.69 ms                                                | 5.33 ms: 1.07x faster                                                 |
| regex_dna                | 227 ms                                                 | 220 ms: 1.03x faster                                                  |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                                  |
| async_generators         | 444 ms                                                 | 434 ms: 1.02x faster                                                  |
| gc_traversal             | 3.62 ms                                                | 3.75 ms: 1.03x slower                                                 |
| coverage                 | 79.4 ms                                                | 85.4 ms: 1.08x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 1.76 ms: 1.08x slower                                                 |
| telco                    | 7.27 ms                                                | 8.36 ms: 1.15x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.10 ms: 1.20x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.44x faster                                                          |

Benchmark hidden because not significant (3): regex_effbot, bench_mp_pool, asyncio_websockets
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240824-3.14.0a0-f78838c/bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.440x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.35x
- 95% likely to have a speedup of 1.34x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: 1.13x