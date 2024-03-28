# Results vs. 3.10.4

- fork: faster-cpython
- ref: no_thresholds
- machine: linux-x86_64
- commit hash: 174fc24
- commit date: 2024-03-28
- overall geometric mean: 1.27x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-174fc24 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 280 ms: 1.25x faster                                                      |
| chameleon      | 9.68 ms                                                | 7.16 ms: 1.35x faster                                                     |
| docutils       | 3.30 sec                                               | 2.93 sec: 1.13x faster                                                    |
| html5lib       | 88.9 ms                                                | 66.4 ms: 1.34x faster                                                     |
| tornado_http   | 136 ms                                                 | 96.9 ms: 1.41x faster                                                     |
| Geometric mean | (ref)                                                  | 1.29x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-174fc24 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 360 ms: 2.03x faster                                                      |
| async_tree_io           | 1.77 sec                                               | 932 ms: 1.90x faster                                                      |
| async_tree_memoization  | 870 ms                                                 | 458 ms: 1.90x faster                                                      |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 613 ms: 1.66x faster                                                      |
| Geometric mean          | (ref)                                                  | 1.86x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-174fc24 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 92.7 ms: 1.66x faster                                                     |
| float          | 117 ms                                                 | 79.6 ms: 1.47x faster                                                     |
| pidigits       | 191 ms                                                 | 189 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.35x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-174fc24 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 151 ms: 1.25x faster                                                      |
| regex_v8       | 27.8 ms                                                | 25.7 ms: 1.08x faster                                                     |
| regex_dna      | 227 ms                                                 | 234 ms: 1.03x slower                                                      |
| regex_effbot   | 3.63 ms                                                | 3.78 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                  | 1.06x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-174fc24 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 309 us: 1.57x faster                                                      |
| tomli_loads          | 3.14 sec                                               | 2.13 sec: 1.47x faster                                                    |
| json_dumps           | 14.2 ms                                                | 10.7 ms: 1.33x faster                                                     |
| xml_etree_process    | 79.1 ms                                                | 62.6 ms: 1.26x faster                                                     |
| unpickle_pure_python | 331 us                                                 | 268 us: 1.23x faster                                                      |
| json_loads           | 31.2 us                                                | 28.6 us: 1.09x faster                                                     |
| xml_etree_generate   | 99.4 ms                                                | 92.9 ms: 1.07x faster                                                     |
| xml_etree_parse      | 168 ms                                                 | 160 ms: 1.05x faster                                                      |
| xml_etree_iterparse  | 115 ms                                                 | 112 ms: 1.03x faster                                                      |
| pickle_list          | 5.08 us                                                | 5.12 us: 1.01x slower                                                     |
| pickle               | 10.7 us                                                | 12.1 us: 1.14x slower                                                     |
| unpickle             | 14.4 us                                                | 17.1 us: 1.19x slower                                                     |
| pickle_dict          | 29.6 us                                                | 36.5 us: 1.23x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                              |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-174fc24 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.1 ms: 1.32x faster                                                     |
| python_startup_no_site | 5.93 ms                                                | 9.54 ms: 1.61x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-174fc24 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.8 ms: 1.51x faster                                                     |
| django_template | 48.2 ms                                                | 37.1 ms: 1.30x faster                                                     |
| genshi_text     | 31.8 ms                                                | 25.8 ms: 1.23x faster                                                     |
| genshi_xml      | 66.0 ms                                                | 57.3 ms: 1.15x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.29x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-174fc24 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 116 us: 4.68x faster                                                      |
| generators               | 80.1 ms                                                | 29.9 ms: 2.68x faster                                                     |
| async_tree_none          | 728 ms                                                 | 360 ms: 2.03x faster                                                      |
| deltablue                | 7.91 ms                                                | 4.15 ms: 1.91x faster                                                     |
| async_tree_io            | 1.77 sec                                               | 932 ms: 1.90x faster                                                      |
| async_tree_memoization   | 870 ms                                                 | 458 ms: 1.90x faster                                                      |
| asyncio_tcp              | 922 ms                                                 | 511 ms: 1.80x faster                                                      |
| logging_silent           | 190 ns                                                 | 106 ns: 1.79x faster                                                      |
| chaos                    | 115 ms                                                 | 65.4 ms: 1.77x faster                                                     |
| crypto_pyaes             | 128 ms                                                 | 75.6 ms: 1.69x faster                                                     |
| raytrace                 | 507 ms                                                 | 303 ms: 1.67x faster                                                      |
| scimark_sor              | 220 ms                                                 | 132 ms: 1.66x faster                                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 613 ms: 1.66x faster                                                      |
| nbody                    | 154 ms                                                 | 92.7 ms: 1.66x faster                                                     |
| pylint                   | 551 ms                                                 | 340 ms: 1.62x faster                                                      |
| richards_super           | 94.7 ms                                                | 59.7 ms: 1.59x faster                                                     |
| sqlglot_parse            | 2.17 ms                                                | 1.37 ms: 1.58x faster                                                     |
| scimark_monte_carlo      | 118 ms                                                 | 75.3 ms: 1.57x faster                                                     |
| pickle_pure_python       | 484 us                                                 | 309 us: 1.57x faster                                                      |
| coroutines               | 35.1 ms                                                | 22.6 ms: 1.55x faster                                                     |
| mako                     | 16.3 ms                                                | 10.8 ms: 1.51x faster                                                     |
| sqlglot_transpile        | 2.57 ms                                                | 1.71 ms: 1.51x faster                                                     |
| spectral_norm            | 170 ms                                                 | 114 ms: 1.49x faster                                                      |
| comprehensions           | 28.8 us                                                | 19.4 us: 1.48x faster                                                     |
| tomli_loads              | 3.14 sec                                               | 2.13 sec: 1.47x faster                                                    |
| float                    | 117 ms                                                 | 79.6 ms: 1.47x faster                                                     |
| pyflate                  | 716 ms                                                 | 488 ms: 1.47x faster                                                      |
| richards                 | 79.3 ms                                                | 54.0 ms: 1.47x faster                                                     |
| tornado_http             | 136 ms                                                 | 96.9 ms: 1.41x faster                                                     |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.86 sec: 1.38x faster                                                    |
| go                       | 240 ms                                                 | 175 ms: 1.37x faster                                                      |
| logging_simple           | 8.30 us                                                | 6.07 us: 1.37x faster                                                     |
| scimark_fft              | 466 ms                                                 | 342 ms: 1.36x faster                                                      |
| logging_format           | 9.09 us                                                | 6.71 us: 1.35x faster                                                     |
| chameleon                | 9.68 ms                                                | 7.16 ms: 1.35x faster                                                     |
| html5lib                 | 88.9 ms                                                | 66.4 ms: 1.34x faster                                                     |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.84 ms: 1.34x faster                                                     |
| scimark_lu               | 176 ms                                                 | 132 ms: 1.33x faster                                                      |
| pprint_safe_repr         | 1.02 sec                                               | 767 ms: 1.33x faster                                                      |
| json_dumps               | 14.2 ms                                                | 10.7 ms: 1.33x faster                                                     |
| pprint_pformat           | 2.10 sec                                               | 1.60 sec: 1.32x faster                                                    |
| python_startup           | 14.6 ms                                                | 11.1 ms: 1.32x faster                                                     |
| deepcopy_memo            | 58.5 us                                                | 44.8 us: 1.30x faster                                                     |
| thrift                   | 1.07 ms                                                | 822 us: 1.30x faster                                                      |
| django_template          | 48.2 ms                                                | 37.1 ms: 1.30x faster                                                     |
| deepcopy                 | 479 us                                                 | 370 us: 1.30x faster                                                      |
| fannkuch                 | 532 ms                                                 | 410 ms: 1.30x faster                                                      |
| hexiom                   | 10.4 ms                                                | 8.12 ms: 1.28x faster                                                     |
| deepcopy_reduce          | 4.17 us                                                | 3.27 us: 1.27x faster                                                     |
| xml_etree_process        | 79.1 ms                                                | 62.6 ms: 1.26x faster                                                     |
| pycparser                | 1.58 sec                                               | 1.25 sec: 1.26x faster                                                    |
| sqlglot_normalize        | 143 ms                                                 | 114 ms: 1.25x faster                                                      |
| regex_compile            | 188 ms                                                 | 151 ms: 1.25x faster                                                      |
| 2to3                     | 348 ms                                                 | 280 ms: 1.25x faster                                                      |
| genshi_text              | 31.8 ms                                                | 25.8 ms: 1.23x faster                                                     |
| unpickle_pure_python     | 331 us                                                 | 268 us: 1.23x faster                                                      |
| djangocms                | 38.4 us                                                | 32.2 us: 1.19x faster                                                     |
| aiohttp                  | 1.44 ms                                                | 1.21 ms: 1.19x faster                                                     |
| sympy_sum                | 196 ms                                                 | 167 ms: 1.17x faster                                                      |
| dulwich_log              | 84.3 ms                                                | 71.8 ms: 1.17x faster                                                     |
| gunicorn                 | 1.53 ms                                                | 1.31 ms: 1.17x faster                                                     |
| sympy_str                | 346 ms                                                 | 296 ms: 1.17x faster                                                      |
| dask                     | 441 ms                                                 | 378 ms: 1.17x faster                                                      |
| sqlglot_optimize         | 69.2 ms                                                | 59.5 ms: 1.16x faster                                                     |
| sympy_integrate          | 25.8 ms                                                | 22.4 ms: 1.15x faster                                                     |
| genshi_xml               | 66.0 ms                                                | 57.3 ms: 1.15x faster                                                     |
| sympy_expand             | 566 ms                                                 | 500 ms: 1.13x faster                                                      |
| docutils                 | 3.30 sec                                               | 2.93 sec: 1.13x faster                                                    |
| mypy2                    | 894 ms                                                 | 801 ms: 1.12x faster                                                      |
| bench_thread_pool        | 986 us                                                 | 890 us: 1.11x faster                                                      |
| json_loads               | 31.2 us                                                | 28.6 us: 1.09x faster                                                     |
| regex_v8                 | 27.8 ms                                                | 25.7 ms: 1.08x faster                                                     |
| meteor_contest           | 120 ms                                                 | 111 ms: 1.07x faster                                                      |
| xml_etree_generate       | 99.4 ms                                                | 92.9 ms: 1.07x faster                                                     |
| pathlib                  | 20.5 ms                                                | 19.4 ms: 1.05x faster                                                     |
| xml_etree_parse          | 168 ms                                                 | 160 ms: 1.05x faster                                                      |
| sqlite_synth             | 3.02 us                                                | 2.88 us: 1.05x faster                                                     |
| json                     | 5.69 ms                                                | 5.47 ms: 1.04x faster                                                     |
| mdp                      | 2.85 sec                                               | 2.75 sec: 1.04x faster                                                    |
| xml_etree_iterparse      | 115 ms                                                 | 112 ms: 1.03x faster                                                      |
| pidigits                 | 191 ms                                                 | 189 ms: 1.01x faster                                                      |
| pickle_list              | 5.08 us                                                | 5.12 us: 1.01x slower                                                     |
| asyncio_websockets       | 559 ms                                                 | 570 ms: 1.02x slower                                                      |
| nqueens                  | 106 ms                                                 | 109 ms: 1.03x slower                                                      |
| regex_dna                | 227 ms                                                 | 234 ms: 1.03x slower                                                      |
| regex_effbot             | 3.63 ms                                                | 3.78 ms: 1.04x slower                                                     |
| gc_traversal             | 3.62 ms                                                | 3.78 ms: 1.04x slower                                                     |
| create_gc_cycles         | 1.62 ms                                                | 1.69 ms: 1.05x slower                                                     |
| async_generators         | 444 ms                                                 | 502 ms: 1.13x slower                                                      |
| pickle                   | 10.7 us                                                | 12.1 us: 1.14x slower                                                     |
| unpickle                 | 14.4 us                                                | 17.1 us: 1.19x slower                                                     |
| telco                    | 7.27 ms                                                | 8.85 ms: 1.22x slower                                                     |
| coverage                 | 79.4 ms                                                | 97.8 ms: 1.23x slower                                                     |
| pickle_dict              | 29.6 us                                                | 36.5 us: 1.23x slower                                                     |
| unpack_sequence          | 60.0 ns                                                | 88.0 ns: 1.47x slower                                                     |
| python_startup_no_site   | 5.93 ms                                                | 9.54 ms: 1.61x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.27x faster                                                              |

Benchmark hidden because not significant (2): unpickle_list, bench_mp_pool
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240328-3.13.0a5+-174fc24-JIT/bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-174fc24.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.19x


# Memory

- memory change: 1.19x