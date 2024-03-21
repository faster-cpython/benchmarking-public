# Results vs. 3.10.4

- fork: faster-cpython
- ref: fix_gc_counting
- machine: linux-x86_64
- commit hash: d0672a4
- commit date: 2024-03-21
- overall geometric mean: 1.35x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240321-linux-x86_64-faster%2dcpython-fix_gc_counting-3.13.0a5+-d0672a4 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 268 ms: 1.30x faster                                                        |
| chameleon      | 9.68 ms                                                | 6.95 ms: 1.39x faster                                                       |
| docutils       | 3.30 sec                                               | 2.74 sec: 1.20x faster                                                      |
| html5lib       | 88.9 ms                                                | 65.4 ms: 1.36x faster                                                       |
| tornado_http   | 136 ms                                                 | 94.8 ms: 1.44x faster                                                       |
| Geometric mean | (ref)                                                  | 1.34x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240321-linux-x86_64-faster%2dcpython-fix_gc_counting-3.13.0a5+-d0672a4 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 374 ms: 1.95x faster                                                        |
| async_tree_io           | 1.77 sec                                               | 917 ms: 1.93x faster                                                        |
| async_tree_memoization  | 870 ms                                                 | 461 ms: 1.89x faster                                                        |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 590 ms: 1.72x faster                                                        |
| Geometric mean          | (ref)                                                  | 1.87x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240321-linux-x86_64-faster%2dcpython-fix_gc_counting-3.13.0a5+-d0672a4 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 89.9 ms: 1.71x faster                                                       |
| float          | 117 ms                                                 | 78.5 ms: 1.49x faster                                                       |
| pidigits       | 191 ms                                                 | 190 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.37x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240321-linux-x86_64-faster%2dcpython-fix_gc_counting-3.13.0a5+-d0672a4 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 135 ms: 1.39x faster                                                        |
| regex_v8       | 27.8 ms                                                | 24.8 ms: 1.12x faster                                                       |
| regex_dna      | 227 ms                                                 | 218 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                  | 1.13x faster                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240321-linux-x86_64-faster%2dcpython-fix_gc_counting-3.13.0a5+-d0672a4 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 302 us: 1.61x faster                                                        |
| unpickle_pure_python | 331 us                                                 | 220 us: 1.51x faster                                                        |
| tomli_loads          | 3.14 sec                                               | 2.19 sec: 1.43x faster                                                      |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                       |
| xml_etree_process    | 79.1 ms                                                | 59.8 ms: 1.32x faster                                                       |
| xml_etree_generate   | 99.4 ms                                                | 85.5 ms: 1.16x faster                                                       |
| json_loads           | 31.2 us                                                | 28.6 us: 1.09x faster                                                       |
| xml_etree_iterparse  | 115 ms                                                 | 107 ms: 1.08x faster                                                        |
| xml_etree_parse      | 168 ms                                                 | 162 ms: 1.04x faster                                                        |
| unpickle             | 14.4 us                                                | 14.6 us: 1.01x slower                                                       |
| pickle_list          | 5.08 us                                                | 5.36 us: 1.06x slower                                                       |
| pickle               | 10.7 us                                                | 11.8 us: 1.11x slower                                                       |
| pickle_dict          | 29.6 us                                                | 35.3 us: 1.19x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.14x faster                                                                |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240321-linux-x86_64-faster%2dcpython-fix_gc_counting-3.13.0a5+-d0672a4 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.4 ms: 1.40x faster                                                       |
| python_startup_no_site | 5.93 ms                                                | 8.83 ms: 1.49x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240321-linux-x86_64-faster%2dcpython-fix_gc_counting-3.13.0a5+-d0672a4 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.5 ms: 1.42x faster                                                       |
| django_template | 48.2 ms                                                | 34.0 ms: 1.42x faster                                                       |
| genshi_text     | 31.8 ms                                                | 23.1 ms: 1.38x faster                                                       |
| genshi_xml      | 66.0 ms                                                | 52.1 ms: 1.27x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.37x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240321-linux-x86_64-faster%2dcpython-fix_gc_counting-3.13.0a5+-d0672a4 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 113 us: 4.82x faster                                                        |
| generators               | 80.1 ms                                                | 30.1 ms: 2.66x faster                                                       |
| deltablue                | 7.91 ms                                                | 3.28 ms: 2.41x faster                                                       |
| async_tree_none          | 728 ms                                                 | 374 ms: 1.95x faster                                                        |
| async_tree_io            | 1.77 sec                                               | 917 ms: 1.93x faster                                                        |
| logging_silent           | 190 ns                                                 | 99.8 ns: 1.90x faster                                                       |
| raytrace                 | 507 ms                                                 | 268 ms: 1.89x faster                                                        |
| async_tree_memoization   | 870 ms                                                 | 461 ms: 1.89x faster                                                        |
| chaos                    | 115 ms                                                 | 61.7 ms: 1.87x faster                                                       |
| asyncio_tcp              | 922 ms                                                 | 503 ms: 1.83x faster                                                        |
| richards_super           | 94.7 ms                                                | 53.1 ms: 1.78x faster                                                       |
| comprehensions           | 28.8 us                                                | 16.4 us: 1.76x faster                                                       |
| crypto_pyaes             | 128 ms                                                 | 72.9 ms: 1.75x faster                                                       |
| pylint                   | 551 ms                                                 | 317 ms: 1.74x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 590 ms: 1.72x faster                                                        |
| richards                 | 79.3 ms                                                | 46.1 ms: 1.72x faster                                                       |
| nbody                    | 154 ms                                                 | 89.9 ms: 1.71x faster                                                       |
| scimark_monte_carlo      | 118 ms                                                 | 69.6 ms: 1.70x faster                                                       |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.70x faster                                                       |
| go                       | 240 ms                                                 | 142 ms: 1.69x faster                                                        |
| scimark_sor              | 220 ms                                                 | 131 ms: 1.68x faster                                                        |
| hexiom                   | 10.4 ms                                                | 6.34 ms: 1.64x faster                                                       |
| sqlglot_transpile        | 2.57 ms                                                | 1.58 ms: 1.63x faster                                                       |
| pickle_pure_python       | 484 us                                                 | 302 us: 1.61x faster                                                        |
| scimark_lu               | 176 ms                                                 | 113 ms: 1.56x faster                                                        |
| deepcopy_memo            | 58.5 us                                                | 38.1 us: 1.54x faster                                                       |
| coroutines               | 35.1 ms                                                | 23.2 ms: 1.51x faster                                                       |
| unpickle_pure_python     | 331 us                                                 | 220 us: 1.51x faster                                                        |
| float                    | 117 ms                                                 | 78.5 ms: 1.49x faster                                                       |
| spectral_norm            | 170 ms                                                 | 114 ms: 1.49x faster                                                        |
| pyflate                  | 716 ms                                                 | 483 ms: 1.48x faster                                                        |
| tornado_http             | 136 ms                                                 | 94.8 ms: 1.44x faster                                                       |
| tomli_loads              | 3.14 sec                                               | 2.19 sec: 1.43x faster                                                      |
| logging_simple           | 8.30 us                                                | 5.84 us: 1.42x faster                                                       |
| mako                     | 16.3 ms                                                | 11.5 ms: 1.42x faster                                                       |
| django_template          | 48.2 ms                                                | 34.0 ms: 1.42x faster                                                       |
| python_startup           | 14.6 ms                                                | 10.4 ms: 1.40x faster                                                       |
| logging_format           | 9.09 us                                                | 6.49 us: 1.40x faster                                                       |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.84 sec: 1.40x faster                                                      |
| regex_compile            | 188 ms                                                 | 135 ms: 1.39x faster                                                        |
| pprint_pformat           | 2.10 sec                                               | 1.51 sec: 1.39x faster                                                      |
| chameleon                | 9.68 ms                                                | 6.95 ms: 1.39x faster                                                       |
| genshi_text              | 31.8 ms                                                | 23.1 ms: 1.38x faster                                                       |
| pprint_safe_repr         | 1.02 sec                                               | 741 ms: 1.37x faster                                                        |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                       |
| html5lib                 | 88.9 ms                                                | 65.4 ms: 1.36x faster                                                       |
| unpack_sequence          | 60.0 ns                                                | 44.2 ns: 1.36x faster                                                       |
| deepcopy                 | 479 us                                                 | 353 us: 1.36x faster                                                        |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.35x faster                                                      |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.81 ms: 1.35x faster                                                       |
| thrift                   | 1.07 ms                                                | 805 us: 1.33x faster                                                        |
| sqlglot_normalize        | 143 ms                                                 | 108 ms: 1.33x faster                                                        |
| xml_etree_process        | 79.1 ms                                                | 59.8 ms: 1.32x faster                                                       |
| deepcopy_reduce          | 4.17 us                                                | 3.16 us: 1.32x faster                                                       |
| fannkuch                 | 532 ms                                                 | 406 ms: 1.31x faster                                                        |
| 2to3                     | 348 ms                                                 | 268 ms: 1.30x faster                                                        |
| scimark_fft              | 466 ms                                                 | 360 ms: 1.30x faster                                                        |
| nqueens                  | 106 ms                                                 | 81.8 ms: 1.29x faster                                                       |
| sympy_integrate          | 25.8 ms                                                | 20.0 ms: 1.29x faster                                                       |
| sympy_sum                | 196 ms                                                 | 154 ms: 1.28x faster                                                        |
| genshi_xml               | 66.0 ms                                                | 52.1 ms: 1.27x faster                                                       |
| sqlglot_optimize         | 69.2 ms                                                | 54.8 ms: 1.26x faster                                                       |
| sympy_str                | 346 ms                                                 | 277 ms: 1.25x faster                                                        |
| dulwich_log              | 84.3 ms                                                | 67.9 ms: 1.24x faster                                                       |
| aiohttp                  | 1.44 ms                                                | 1.17 ms: 1.23x faster                                                       |
| djangocms                | 38.4 us                                                | 31.3 us: 1.23x faster                                                       |
| sympy_expand             | 566 ms                                                 | 463 ms: 1.22x faster                                                        |
| mypy2                    | 894 ms                                                 | 738 ms: 1.21x faster                                                        |
| gunicorn                 | 1.53 ms                                                | 1.27 ms: 1.21x faster                                                       |
| docutils                 | 3.30 sec                                               | 2.74 sec: 1.20x faster                                                      |
| dask                     | 441 ms                                                 | 368 ms: 1.20x faster                                                        |
| bench_thread_pool        | 986 us                                                 | 831 us: 1.19x faster                                                        |
| xml_etree_generate       | 99.4 ms                                                | 85.5 ms: 1.16x faster                                                       |
| create_gc_cycles         | 1.62 ms                                                | 1.44 ms: 1.12x faster                                                       |
| regex_v8                 | 27.8 ms                                                | 24.8 ms: 1.12x faster                                                       |
| pathlib                  | 20.5 ms                                                | 18.4 ms: 1.11x faster                                                       |
| json_loads               | 31.2 us                                                | 28.6 us: 1.09x faster                                                       |
| meteor_contest           | 120 ms                                                 | 110 ms: 1.08x faster                                                        |
| xml_etree_iterparse      | 115 ms                                                 | 107 ms: 1.08x faster                                                        |
| json                     | 5.69 ms                                                | 5.31 ms: 1.07x faster                                                       |
| mdp                      | 2.85 sec                                               | 2.71 sec: 1.05x faster                                                      |
| sqlite_synth             | 3.02 us                                                | 2.89 us: 1.05x faster                                                       |
| regex_dna                | 227 ms                                                 | 218 ms: 1.04x faster                                                        |
| xml_etree_parse          | 168 ms                                                 | 162 ms: 1.04x faster                                                        |
| async_generators         | 444 ms                                                 | 440 ms: 1.01x faster                                                        |
| pidigits                 | 191 ms                                                 | 190 ms: 1.01x faster                                                        |
| bench_mp_pool            | 24.0 ms                                                | 23.9 ms: 1.01x faster                                                       |
| gc_traversal             | 3.62 ms                                                | 3.65 ms: 1.01x slower                                                       |
| asyncio_websockets       | 559 ms                                                 | 563 ms: 1.01x slower                                                        |
| unpickle                 | 14.4 us                                                | 14.6 us: 1.01x slower                                                       |
| pickle_list              | 5.08 us                                                | 5.36 us: 1.06x slower                                                       |
| pickle                   | 10.7 us                                                | 11.8 us: 1.11x slower                                                       |
| telco                    | 7.27 ms                                                | 8.41 ms: 1.16x slower                                                       |
| pickle_dict              | 29.6 us                                                | 35.3 us: 1.19x slower                                                       |
| coverage                 | 79.4 ms                                                | 96.1 ms: 1.21x slower                                                       |
| python_startup_no_site   | 5.93 ms                                                | 8.83 ms: 1.49x slower                                                       |
| Geometric mean           | (ref)                                                  | 1.35x faster                                                                |

Benchmark hidden because not significant (2): regex_effbot, unpickle_list
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240321-3.13.0a5+-d0672a4/bm-20240321-linux-x86_64-faster%2dcpython-fix_gc_counting-3.13.0a5+-d0672a4.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.27x


# Memory

- memory change: 1.08x