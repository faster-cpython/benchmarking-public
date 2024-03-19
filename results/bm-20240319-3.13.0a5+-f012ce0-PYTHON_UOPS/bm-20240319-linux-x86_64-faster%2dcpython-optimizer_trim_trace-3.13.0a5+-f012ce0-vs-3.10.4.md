# Results vs. 3.10.4

- fork: faster-cpython
- ref: optimizer_trim_trace
- machine: linux-x86_64
- commit hash: f012ce0
- commit date: 2024-03-19
- overall geometric mean: 1.21x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240319-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-f012ce0 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 299 ms: 1.16x faster                                                             |
| chameleon      | 9.68 ms                                                | 7.35 ms: 1.32x faster                                                            |
| docutils       | 3.30 sec                                               | 2.92 sec: 1.13x faster                                                           |
| html5lib       | 88.9 ms                                                | 68.9 ms: 1.29x faster                                                            |
| tornado_http   | 136 ms                                                 | 105 ms: 1.30x faster                                                             |
| Geometric mean | (ref)                                                  | 1.24x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240319-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-f012ce0 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 468 ms: 1.56x faster                                                             |
| async_tree_memoization  | 870 ms                                                 | 599 ms: 1.45x faster                                                             |
| async_tree_io           | 1.77 sec                                               | 1.25 sec: 1.42x faster                                                           |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 748 ms: 1.36x faster                                                             |
| Geometric mean          | (ref)                                                  | 1.45x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240319-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-f012ce0 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 125 ms: 1.23x faster                                                             |
| float          | 117 ms                                                 | 97.7 ms: 1.20x faster                                                            |
| pidigits       | 191 ms                                                 | 191 ms: 1.00x slower                                                             |
| Geometric mean | (ref)                                                  | 1.14x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240319-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-f012ce0 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_v8       | 27.8 ms                                                | 25.2 ms: 1.10x faster                                                            |
| regex_compile  | 188 ms                                                 | 178 ms: 1.06x faster                                                             |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                     |

Benchmark hidden because not significant (2): regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240319-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-f012ce0 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 309 us: 1.57x faster                                                             |
| json_dumps           | 14.2 ms                                                | 10.7 ms: 1.33x faster                                                            |
| tomli_loads          | 3.14 sec                                               | 2.48 sec: 1.27x faster                                                           |
| xml_etree_process    | 79.1 ms                                                | 63.5 ms: 1.25x faster                                                            |
| unpickle_pure_python | 331 us                                                 | 278 us: 1.19x faster                                                             |
| json_loads           | 31.2 us                                                | 27.9 us: 1.12x faster                                                            |
| xml_etree_generate   | 99.4 ms                                                | 92.7 ms: 1.07x faster                                                            |
| xml_etree_parse      | 168 ms                                                 | 163 ms: 1.03x faster                                                             |
| unpickle_list        | 5.20 us                                                | 5.07 us: 1.03x faster                                                            |
| xml_etree_iterparse  | 115 ms                                                 | 113 ms: 1.02x faster                                                             |
| pickle_list          | 5.08 us                                                | 5.19 us: 1.02x slower                                                            |
| pickle               | 10.7 us                                                | 11.6 us: 1.09x slower                                                            |
| unpickle             | 14.4 us                                                | 16.0 us: 1.12x slower                                                            |
| pickle_dict          | 29.6 us                                                | 35.6 us: 1.20x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240319-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-f012ce0 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                            |
| python_startup_no_site | 5.93 ms                                                | 9.08 ms: 1.53x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240319-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-f012ce0 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 37.6 ms: 1.28x faster                                                            |
| mako            | 16.3 ms                                                | 13.7 ms: 1.20x faster                                                            |
| genshi_text     | 31.8 ms                                                | 27.5 ms: 1.16x faster                                                            |
| genshi_xml      | 66.0 ms                                                | 63.9 ms: 1.03x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.16x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240319-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-f012ce0 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 118 us: 4.61x faster                                                             |
| generators               | 80.1 ms                                                | 29.6 ms: 2.71x faster                                                            |
| deltablue                | 7.91 ms                                                | 3.86 ms: 2.05x faster                                                            |
| logging_silent           | 190 ns                                                 | 105 ns: 1.81x faster                                                             |
| asyncio_tcp              | 922 ms                                                 | 510 ms: 1.81x faster                                                             |
| pylint                   | 551 ms                                                 | 333 ms: 1.66x faster                                                             |
| pickle_pure_python       | 484 us                                                 | 309 us: 1.57x faster                                                             |
| async_tree_none          | 728 ms                                                 | 468 ms: 1.56x faster                                                             |
| coroutines               | 35.1 ms                                                | 22.7 ms: 1.54x faster                                                            |
| richards_super           | 94.7 ms                                                | 62.0 ms: 1.53x faster                                                            |
| scimark_sor              | 220 ms                                                 | 144 ms: 1.53x faster                                                             |
| chaos                    | 115 ms                                                 | 75.7 ms: 1.52x faster                                                            |
| sqlglot_parse            | 2.17 ms                                                | 1.45 ms: 1.50x faster                                                            |
| raytrace                 | 507 ms                                                 | 345 ms: 1.47x faster                                                             |
| async_tree_memoization   | 870 ms                                                 | 599 ms: 1.45x faster                                                             |
| crypto_pyaes             | 128 ms                                                 | 88.2 ms: 1.45x faster                                                            |
| sqlglot_transpile        | 2.57 ms                                                | 1.79 ms: 1.44x faster                                                            |
| richards                 | 79.3 ms                                                | 55.7 ms: 1.42x faster                                                            |
| async_tree_io            | 1.77 sec                                               | 1.25 sec: 1.42x faster                                                           |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                            |
| deepcopy_memo            | 58.5 us                                                | 42.2 us: 1.38x faster                                                            |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.86 sec: 1.38x faster                                                           |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 748 ms: 1.36x faster                                                             |
| go                       | 240 ms                                                 | 180 ms: 1.34x faster                                                             |
| json_dumps               | 14.2 ms                                                | 10.7 ms: 1.33x faster                                                            |
| scimark_monte_carlo      | 118 ms                                                 | 89.3 ms: 1.32x faster                                                            |
| chameleon                | 9.68 ms                                                | 7.35 ms: 1.32x faster                                                            |
| deepcopy                 | 479 us                                                 | 367 us: 1.31x faster                                                             |
| tornado_http             | 136 ms                                                 | 105 ms: 1.30x faster                                                             |
| thrift                   | 1.07 ms                                                | 824 us: 1.30x faster                                                             |
| html5lib                 | 88.9 ms                                                | 68.9 ms: 1.29x faster                                                            |
| logging_simple           | 8.30 us                                                | 6.45 us: 1.29x faster                                                            |
| django_template          | 48.2 ms                                                | 37.6 ms: 1.28x faster                                                            |
| comprehensions           | 28.8 us                                                | 22.6 us: 1.27x faster                                                            |
| tomli_loads              | 3.14 sec                                               | 2.48 sec: 1.27x faster                                                           |
| deepcopy_reduce          | 4.17 us                                                | 3.30 us: 1.26x faster                                                            |
| logging_format           | 9.09 us                                                | 7.26 us: 1.25x faster                                                            |
| xml_etree_process        | 79.1 ms                                                | 63.5 ms: 1.25x faster                                                            |
| nbody                    | 154 ms                                                 | 125 ms: 1.23x faster                                                             |
| pyflate                  | 716 ms                                                 | 589 ms: 1.22x faster                                                             |
| spectral_norm            | 170 ms                                                 | 140 ms: 1.21x faster                                                             |
| pycparser                | 1.58 sec                                               | 1.31 sec: 1.20x faster                                                           |
| float                    | 117 ms                                                 | 97.7 ms: 1.20x faster                                                            |
| mako                     | 16.3 ms                                                | 13.7 ms: 1.20x faster                                                            |
| sqlglot_normalize        | 143 ms                                                 | 120 ms: 1.19x faster                                                             |
| unpickle_pure_python     | 331 us                                                 | 278 us: 1.19x faster                                                             |
| djangocms                | 38.4 us                                                | 32.5 us: 1.18x faster                                                            |
| aiohttp                  | 1.44 ms                                                | 1.22 ms: 1.18x faster                                                            |
| 2to3                     | 348 ms                                                 | 299 ms: 1.16x faster                                                             |
| gunicorn                 | 1.53 ms                                                | 1.32 ms: 1.16x faster                                                            |
| dask                     | 441 ms                                                 | 379 ms: 1.16x faster                                                             |
| genshi_text              | 31.8 ms                                                | 27.5 ms: 1.16x faster                                                            |
| sympy_integrate          | 25.8 ms                                                | 22.3 ms: 1.16x faster                                                            |
| sympy_sum                | 196 ms                                                 | 170 ms: 1.16x faster                                                             |
| dulwich_log              | 84.3 ms                                                | 73.6 ms: 1.15x faster                                                            |
| bench_thread_pool        | 986 us                                                 | 866 us: 1.14x faster                                                             |
| sqlglot_optimize         | 69.2 ms                                                | 61.2 ms: 1.13x faster                                                            |
| unpack_sequence          | 60.0 ns                                                | 53.1 ns: 1.13x faster                                                            |
| pprint_safe_repr         | 1.02 sec                                               | 901 ms: 1.13x faster                                                             |
| docutils                 | 3.30 sec                                               | 2.92 sec: 1.13x faster                                                           |
| sympy_str                | 346 ms                                                 | 308 ms: 1.12x faster                                                             |
| hexiom                   | 10.4 ms                                                | 9.27 ms: 1.12x faster                                                            |
| json_loads               | 31.2 us                                                | 27.9 us: 1.12x faster                                                            |
| pprint_pformat           | 2.10 sec                                               | 1.89 sec: 1.11x faster                                                           |
| fannkuch                 | 532 ms                                                 | 481 ms: 1.10x faster                                                             |
| regex_v8                 | 27.8 ms                                                | 25.2 ms: 1.10x faster                                                            |
| json                     | 5.69 ms                                                | 5.20 ms: 1.09x faster                                                            |
| sympy_expand             | 566 ms                                                 | 517 ms: 1.09x faster                                                             |
| xml_etree_generate       | 99.4 ms                                                | 92.7 ms: 1.07x faster                                                            |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 6.07 ms: 1.07x faster                                                            |
| scimark_fft              | 466 ms                                                 | 437 ms: 1.06x faster                                                             |
| regex_compile            | 188 ms                                                 | 178 ms: 1.06x faster                                                             |
| mdp                      | 2.85 sec                                               | 2.70 sec: 1.06x faster                                                           |
| scimark_lu               | 176 ms                                                 | 168 ms: 1.05x faster                                                             |
| create_gc_cycles         | 1.62 ms                                                | 1.56 ms: 1.04x faster                                                            |
| pathlib                  | 20.5 ms                                                | 19.8 ms: 1.03x faster                                                            |
| genshi_xml               | 66.0 ms                                                | 63.9 ms: 1.03x faster                                                            |
| xml_etree_parse          | 168 ms                                                 | 163 ms: 1.03x faster                                                             |
| unpickle_list            | 5.20 us                                                | 5.07 us: 1.03x faster                                                            |
| nqueens                  | 106 ms                                                 | 103 ms: 1.02x faster                                                             |
| sqlite_synth             | 3.02 us                                                | 2.96 us: 1.02x faster                                                            |
| xml_etree_iterparse      | 115 ms                                                 | 113 ms: 1.02x faster                                                             |
| pidigits                 | 191 ms                                                 | 191 ms: 1.00x slower                                                             |
| asyncio_websockets       | 559 ms                                                 | 563 ms: 1.01x slower                                                             |
| pickle_list              | 5.08 us                                                | 5.19 us: 1.02x slower                                                            |
| async_generators         | 444 ms                                                 | 477 ms: 1.08x slower                                                             |
| pickle                   | 10.7 us                                                | 11.6 us: 1.09x slower                                                            |
| gc_traversal             | 3.62 ms                                                | 3.96 ms: 1.09x slower                                                            |
| unpickle                 | 14.4 us                                                | 16.0 us: 1.12x slower                                                            |
| pickle_dict              | 29.6 us                                                | 35.6 us: 1.20x slower                                                            |
| telco                    | 7.27 ms                                                | 8.85 ms: 1.22x slower                                                            |
| coverage                 | 79.4 ms                                                | 97.0 ms: 1.22x slower                                                            |
| python_startup_no_site   | 5.93 ms                                                | 9.08 ms: 1.53x slower                                                            |
| Geometric mean           | (ref)                                                  | 1.21x faster                                                                     |

Benchmark hidden because not significant (5): meteor_contest, regex_dna, bench_mp_pool, regex_effbot, mypy2
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240319-3.13.0a5+-f012ce0-PYTHON_UOPS/bm-20240319-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-f012ce0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.12x


# Memory

- memory change: 1.08x